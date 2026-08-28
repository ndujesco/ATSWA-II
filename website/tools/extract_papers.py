#!/usr/bin/env python3
"""
Turn the five INSIGHT past-question packs into structured JSON.

Each pack holds four papers (FA, PS, QA, IT). Each paper is:
    Section A Part I   30 multiple-choice questions      (30 marks)
    Section A Part II  20 short-answer questions         (20 marks)
    Section B          6 questions, attempt any four     (50 marks)
followed by the official solutions for all three, plus examiner comments.

Output: data/papers.json
"""
import json, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import strip_furniture, tidy, money, squeeze, desymbol

ROOT = Path(__file__).resolve().parents[2]
PQ   = ROOT / 'materials' / 'past-questions'
OUT  = ROOT / 'website' / 'data'

DIETS = [
    ('2024-03', 'March 2024',     'INSIGHT Part II - 2024-03 March 2024.pdf'),
    ('2024-09', 'September 2024', 'INSIGHT Part II - 2024-09 September 2024.pdf'),
    ('2025-03', 'March 2025',     'INSIGHT Part II - 2025-03 March 2025.pdf'),
    ('2025-09', 'September 2025', 'INSIGHT Part II - 2025-09 September 2025.pdf'),
    ('2026-03', 'March 2026',     'INSIGHT Part II - 2026-03 March 2026.pdf'),
]
SUBJECTS = [
    ('FA', 'FINANCIAL ACCOUNTING'),
    ('PS', 'PUBLIC SECTOR ACCOUNTING'),
    ('QA', 'QUANTITATIVE ANALYSIS'),
    ('IT', 'INFORMATION TECHNOLOGY'),
]

# ── markers ───────────────────────────────────────────────────────────────
RE_PAPERHEAD = re.compile(r'PART\s+II\s+EXAMINATIONS?\s*[-–]', re.I)
RE_SECA1 = re.compile(r'^\s*SECTION\s+A[:\s]*PART\s+(?:I|1)\b.*MULTIPLE', re.I)
RE_SECA2 = re.compile(r'^\s*SECTION\s+A[:\s]*PART\s+(?:II|2)\b.*SHORT', re.I)
RE_SECB  = re.compile(r'^\s*SECTION\s+B\s*[:.]', re.I)
RE_MCSOL = re.compile(r'^\s*(?:PART\s*(?:1|I)[:\s]*)?MULTI(?:PLE)?[-\s]*CHOICE\s+'
                      r'(?:QUESTIONS?.*|SOLUTIONS?)\s*$', re.I)
RE_SASOL = re.compile(r'^\s*(?:PART\s*(?:II|2)[:\s]*)?SHORT[-\s]*ANSWERS?\s+'
                      r'(?:QUESTIONS?|SOLUTIONS?)\s*$', re.I)
RE_WORK  = re.compile(r'^\s*WORKINGS?\b', re.I)
RE_BSOL  = re.compile(r'^\s*SOLUTION\s+(\d+)\s*[A-Za-z]?\s*$', re.I)
RE_EXAM  = re.compile(r"^\s*EXAMINER'?S?\s+(COMMENT|REPORT)", re.I)

RE_QNUM_P = re.compile(r'^\s{0,14}(\d{1,2})[.)]\s*(.*)$')
RE_QNUM_B = re.compile(r'^\s{0,14}(\d{1,2})\s{2,24}([^\s\d].*)$')

class _QNum:
    """A question number is `7.` / `7)` / a bare `7` followed by prose."""
    @staticmethod
    def match(line):
        return RE_QNUM_P.match(line) or RE_QNUM_B.match(line)

RE_QNUM = _QNum
RE_OPT   = re.compile(r'^\s{0,24}([A-E])[.,)]\s*(\S.*)?$')
RE_PRE   = re.compile(r'^\s*Use\s+the\s+(following|data|table|information|Euler)', re.I)
RE_KEY   = re.compile(r'^\s*(\d{1,2})[.)]?\s*([A-E])[.)]?\s*$')


TABULAR = re.compile(r'\S {3,}\S')

def is_tabular(lines):
    """A wide internal gap means pdftotext preserved a column layout."""
    return any(TABULAR.search(l) for l in lines)


def pdf_lines(path):
    txt = subprocess.run(['pdftotext', '-layout', str(path), '-'],
                         capture_output=True, text=True, check=True).stdout
    return txt.replace('\f', '\n').split('\n')


def find(lines, rx, start=0, end=None):
    end = len(lines) if end is None else end
    for i in range(start, end):
        if rx.search(lines[i]):
            return i
    return -1


def split_papers(lines):
    """Locate each subject's paper by its 'PART II EXAMINATIONS' banner."""
    heads = [i for i, l in enumerate(lines) if RE_PAPERHEAD.search(l)]
    out = []
    for i, h in enumerate(heads):
        title = ''
        for l in lines[h + 1:h + 6]:
            t = l.strip()
            if t and not re.match(r'^\(?PART', t, re.I) and 'Time Allowed' not in t:
                title = t
                break
        code = None
        for c, name in SUBJECTS:
            if title.upper().startswith(name[:12]):
                code = c
        if code is None:
            continue
        end = heads[i + 1] if i + 1 < len(heads) else len(lines)
        out.append((code, h, end))
    return out


# ── question parsing ──────────────────────────────────────────────────────
def _finish(part):
    """A stem or option becomes prose, or keeps its lines when it is a table."""
    lines = squeeze(part)
    if not lines:
        return {'t': ''}
    if is_tabular(lines):
        return {'t': tidy(' '.join(lines[:1])),
                'pre': [money(desymbol(l)) for l in lines]}
    return {'t': money(tidy(' '.join(l.strip() for l in lines if l.strip())))}


def parse_mcq(block):
    """Numbered stems with A-E options; a shared preamble carries onto its group."""
    qs, cur, pre, pending = [], None, [], []
    expect = 1

    def close():
        """Materialise the open question's raw buffers."""
        if not cur:
            return
        cur['stem'] = _finish(cur['_stem'])
        cur['options'] = [_finish(o) for o in cur['_opts']]
        del cur['_stem'], cur['_opts']

    def flush():
        nonlocal cur
        if cur:
            close()
            if len(cur['options']) >= 2:
                qs.append(cur)
        cur = None

    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            if cur and cur['_opts']:
                cur['_opts'][-1].append('')
            elif cur:
                cur['_stem'].append('')
            elif pending:
                pending.append('')
            continue

        mq = RE_QNUM.match(line)
        if mq and int(mq.group(1)) == expect:
            flush()
            if pending:
                pre = squeeze(pending)
                pending = []
            cur = {'n': expect, '_stem': [mq.group(2)], '_opts': [], 'pre': pre}
            expect += 1
            continue

        if RE_PRE.match(line):
            flush()
            pre = []
            pending = [line.strip()]
            continue

        mo = RE_OPT.match(line)
        if cur and mo and ord(mo.group(1)) == ord('A') + len(cur['_opts']):
            cur['_opts'].append([mo.group(2) or ''])
            continue

        if cur and cur['_opts']:
            cur['_opts'][-1].append(raw.rstrip())
        elif cur:
            cur['_stem'].append(raw.rstrip())
        elif pending:
            pending.append(raw.rstrip())
    flush()
    return qs


def parse_numbered(block, limit=40, expect=1):
    """Short-answer questions or their solutions: numbered prose, table-tolerant."""
    items, cur, pre, pending = [], None, [], []
    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            if cur:
                cur['body'].append('')
            elif pending:
                pending.append('')
            continue

        m = RE_QNUM.match(line)
        if m and int(m.group(1)) == expect and expect <= limit:
            if cur:
                items.append(cur)
            if pending:
                pre = squeeze(pending)
                pending = []
            cur = {'n': expect, 'body': [tidy(m.group(2))], 'pre': pre}
            pre = []
            expect += 1
            continue

        if RE_PRE.match(line):
            if cur:
                items.append(cur)
                cur = None
            pending = [line.strip()]
            continue

        if cur:
            cur['body'].append(raw.rstrip())
        elif pending:
            pending.append(raw.rstrip())
    if cur:
        items.append(cur)
    for it in items:
        it['body'] = squeeze(it['body'])
    return items


def parse_key(block):
    key = {}
    for l in block:
        for m in re.finditer(r'(?:^|\s)(\d{1,2})[.)]\s*([A-E])(?=[\s.)]|$)', l):
            n = int(m.group(1))
            if 1 <= n <= 40 and n not in key:
                key[n] = m.group(2)
    return key


def parse_paper(lines, code, diet):
    n = len(lines)
    i_a1 = find(lines, RE_SECA1)
    i_a2 = find(lines, RE_SECA2, max(i_a1, 0))
    i_b  = find(lines, RE_SECB, max(i_a2, 0))

    sols = [(int(m.group(1)), i) for i, l in enumerate(lines)
            if (m := RE_BSOL.match(l)) and i > max(i_b, 0)]
    sol_start = sols[0][1] if sols else n

    # the solutions region opens with a multiple-choice header somewhere between
    # the Section B paper and SOLUTION 1; take the last such header.
    i_mc = -1
    for i in range(max(i_b, 0) + 1, sol_start):
        if RE_MCSOL.match(lines[i]):
            i_mc = i
    i_sa = -1
    if i_mc > 0:
        for i in range(i_mc + 1, sol_start):
            if RE_SASOL.match(lines[i]):
                i_sa = i
                break

    def seg(a, b):
        if a < 0:
            return []
        return strip_furniture(lines[a + 1:b if b and b > 0 else n])

    mcq = parse_mcq(seg(i_a1, i_a2))
    saq = parse_numbered(seg(i_a2, i_b))

    # Section B question paper: from the SECTION B banner to the solutions
    secb_q = squeeze(seg(i_b, i_mc if i_mc > 0 else sol_start))

    # multiple-choice key, its workings and the examiner's comment
    key, mc_work, mc_note = {}, [], []
    if i_mc > 0:
        blk = seg(i_mc, i_sa if i_sa > 0 else sol_start)
        e = find(blk, RE_EXAM)
        if e >= 0:
            mc_note = squeeze(blk[e + 1:])
            blk = blk[:e]
        w = find(blk, RE_WORK)
        if w >= 0:
            mc_work = squeeze(blk[w + 1:])
            blk = blk[:w]
        key = parse_key(blk)

    # short-answer solutions, their workings and comment
    sa_sol, sa_work, sa_note = [], [], []
    if i_sa > 0:
        blk = seg(i_sa, sol_start)
        e = find(blk, RE_EXAM)
        if e >= 0:
            sa_note = squeeze(blk[e + 1:])
            blk = blk[:e]
        w = find(blk, RE_WORK)
        if w >= 0:
            sa_work = squeeze(blk[w + 1:])
            blk = blk[:w]
        sa_sol = parse_numbered(blk)

    secb = []
    for j, (num, at) in enumerate(sols):
        stop = sols[j + 1][1] if j + 1 < len(sols) else n
        body = squeeze(strip_furniture(lines[at + 1:stop]))
        e = find(body, RE_EXAM)
        comment = squeeze(body[e + 1:]) if e >= 0 else []
        if e >= 0:
            body = squeeze(body[:e])
        secb.append({'n': num, 'solution': body, 'examiner': comment})

    return {
        'diet': diet, 'subject': code,
        'mcq': mcq, 'mcq_key': key, 'mcq_workings': mc_work, 'mcq_examiner': mc_note,
        'saq': saq, 'saq_solutions': sa_sol, 'saq_workings': sa_work,
        'saq_examiner': sa_note,
        'secb_paper': secb_q, 'secb_solutions': secb,
    }


def main():
    papers = []
    for dcode, dname, fname in DIETS:
        lines = pdf_lines(PQ / fname)
        for code, a, b in split_papers(lines):
            p = parse_paper(lines[a:b], code, dcode)
            p['dietName'] = dname
            papers.append(p)
            print(f'{dcode} {code}: {len(p["mcq"])} mcq '
                  f'(key {len(p["mcq_key"])}), {len(p["saq"])} saq '
                  f'(sol {len(p["saq_solutions"])}), {len(p["secb_solutions"])} section-B solutions')
    # decode Symbol-font glyphs and naira signs everywhere a raw line survived
    def clean(node):
        if isinstance(node, str):
            return money(desymbol(node))
        if isinstance(node, list):
            return [clean(v) for v in node]
        if isinstance(node, dict):
            return {k: clean(v) for k, v in node.items()}
        return node
    papers = clean(papers)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=1))
    print(f'\nwrote {OUT/"papers.json"}  ({(OUT/"papers.json").stat().st_size//1024} KB)')


if __name__ == '__main__':
    main()
