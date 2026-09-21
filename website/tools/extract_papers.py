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
    ('2014-03', 'March 2014',     'INSIGHT Part II - 2014-03 March 2014.pdf'),
    ('2014-09', 'September 2014', 'INSIGHT Part II - 2014-09 September 2014.pdf'),
    ('2015-03', 'March 2015',     'INSIGHT Part II - 2015-03 March 2015.pdf'),
    ('2015-09', 'September 2015', 'INSIGHT Part II - 2015-09 September 2015.pdf'),
    ('2016-09', 'September 2016', 'INSIGHT Part II - 2016-09 September 2016.pdf'),
    ('2017-03', 'March 2017',     'INSIGHT Part II - 2017-03 March 2017.pdf'),
    ('2017-09', 'September 2017', 'INSIGHT Part II - 2017-09 September 2017.pdf'),
    ('2018-03', 'March 2018',     'INSIGHT Part II - 2018-03 March 2018.pdf'),
    ('2018-09', 'September 2018', 'INSIGHT Part II - 2018-09 September 2018.pdf'),
    ('2019-03', 'March 2019',     'INSIGHT Part II - 2019-03 March 2019.pdf'),
    ('2019-09', 'September 2019', 'INSIGHT Part II - 2019-09 September 2019.pdf'),
    ('2020-03', 'March 2020',     'INSIGHT Part II - 2020-03 March 2020.pdf'),
    ('2020-09', 'September 2020', 'INSIGHT Part II - 2020-09 September 2020.pdf'),
    ('2021-03', 'March 2021',     'INSIGHT Part II - 2021-03 March 2021.pdf'),
    ('2021-09', 'September 2021', 'INSIGHT Part II - 2021-09 September 2021.pdf'),
    ('2022-03', 'March 2022',     'INSIGHT Part II - 2022-03 March 2022.pdf'),
    ('2022-09', 'September 2022', 'INSIGHT Part II - 2022-09 September 2022.pdf'),
    ('2023-03', 'March 2023',     'INSIGHT Part II - 2023-03 March 2023.pdf'),
    ('2023-09', 'September 2023', 'INSIGHT Part II - 2023-09 September 2023.pdf'),
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

# Older diets wrap "MULTIPLE-CHOICE QUESTIONS" / "SHORT-ANSWER QUESTIONS" onto
# their own line below the "SECTION A: PART I/II ATTEMPT ALL QUESTIONS" banner
# rather than trailing it on the same line, and print "SECTION B" with no
# colon at all — so none of these three markers require what follows on the
# same physical line, only the banner phrase itself, which is distinctive
# enough on its own not to appear anywhere but at each part's true start.
# One diet drops "PART II" from the Part II banner entirely ("SECTION A:
# SHORT-ANSWER QUESTIONS"), so both banners also accept "SECTION A" directly
# followed, on the same line, by the part's own keyword.
# One diet drops "SECTION A:" entirely from the Part II banner, leaving a
# bare "PART II   SHORT-ANSWER QUESTIONS (20 Marks)" — safe to accept without
# that prefix specifically because it still requires the part's own keyword
# on the same line, unlike the page-footer "ATSWA PART II <diet>" that
# repeats on every page and never carries that keyword.
RE_SECA1 = re.compile(r'^\s*SECTION\s+A[:\s]*PART\s+(?:I|1)\b|'
                      r'^\s*SECTION\s+A[:\s]*MU(?:L)?TI(?:PLE)?[\s\-–—:()]*CHOICE|'
                      r'^\s*PART\s+(?:I|1)\b[:\s]*MU(?:L)?TI(?:PLE)?[\s\-–—:()]*CHOICE', re.I)
RE_SECA2 = re.compile(r'^\s*SECTION\s+A[:\s]*PART\s+(?:II|2)\b|'
                      r'^\s*SECTION\s+A[:\s]*SHORT[\s\-]*ANSWERS?\b|'
                      r'^\s*PART\s+(?:II|2)\b[:\s]*SHORT[\s\-]*ANSWERS?', re.I)
RE_SECB  = re.compile(r'^\s*SECTION\s+B\b', re.I)
# The header introducing the printed MCQ/SAQ answer key varies a lot across
# diets — "MULTIPLE CHOICE QUESTIONS", "MULTIPLE – CHOICE QUESTION", "MCQ –
# SOLUTION", "SOLUTION TO MULTIPLE CHOICE QUESTIONS (MCQ)", "SOLUTIONS - MCQ",
# "SOLUTION TO SAQ", "SHORT-ANSWER SOLUTIONS", etc. Matching is therefore a
# search for the *combination* of words anywhere on the line, not an anchored
# exact heading, and callers use .search() rather than .match().
RE_MCSOL = re.compile(r'MU(?:L)?TI(?:PLE)?[\s\-–—:()]*CHOICE|MCQ[\s\-–—:()]*'
                      r'SOLUTIONS?|SOLUTIONS?[\s\-–—:()]*(?:TO\s*)?MCQ|'
                      r'^\s*MCQ\s*[:\-–—]?\s*$', re.I)
RE_SASOL = re.compile(r'SHORT[\s\-]*ANSWERS?|SAQ[\s\-–—:()]*SOLUTIONS?|'
                      r'SOLUTIONS?[\s\-–—:()]*(?:TO\s*)?SAQ|'
                      r'^\s*SAQ\s*[:\-–—]?\s*$|'
                      # one diet labels this "SECTION A: PART II ANSWER", with
                      # no "SHORT" at all — safe only in this exact combination.
                      r'PART\s+(?:II|2)\b[:\s]*ANSWER\b', re.I)
RE_WORK  = re.compile(r'^\s*WORKINGS?\b', re.I)
# "SOLUTION 1", "SOLUTION TO QUESTION 1" and (one diet) "SOLUTION TO QUESTION
# ONE" all mark a Section B answer; Section B never runs past six questions,
# so a spelled-out word is only ever one of these.
RE_BSOL  = re.compile(r'^\s*SOLUTION\s*(?:TO\s*)?(?:QUESTION\s*)?'
                      r'(\d+|ONE|TWO|THREE|FOUR|FIVE|SIX)\s*[A-Za-z]?\s*$', re.I)
NUM_WORD = {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6}


def bsol_num(m):
    g = m.group(1).upper()
    return NUM_WORD.get(g) or int(g)
RE_EXAM  = re.compile(r"^\s*EXAMINER'?S?\s+(COMMENT|REPORT)", re.I)

RE_QNUM_P = re.compile(r'^\s{0,14}(\d{1,2})[.)]\s*(.*)$')
RE_QNUM_B = re.compile(r'^\s{0,14}(\d{1,2})\s{2,24}([^\s\d].*)$')

class _QNum:
    """A question number is `7.` / `7)` / a bare `7` followed by prose."""
    @staticmethod
    def match(line):
        return RE_QNUM_P.match(line) or RE_QNUM_B.match(line)

RE_QNUM = _QNum

# A few diets number the short-answer questions (only ever up to 20) with
# lower-case roman numerals — "i.", "ii.", … "xx." — instead of arabic
# digits; parse_numbered() tries this once the arabic match fails.
_ROMANS = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
           'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx']
ROMAN_VAL = {w: i + 1 for i, w in enumerate(_ROMANS)}
RE_QNUM_ROMAN = re.compile(
    r'^\s{0,14}(' + '|'.join(sorted(_ROMANS, key=len, reverse=True)) +
    r')[.)]\s*(.*)$', re.I)
RE_OPT   = re.compile(r'^\s{0,24}([A-E])[.,)]\s*(\S.*)?$')
RE_PRE   = re.compile(r'^\s*Use\s+the\s+(following|data|table|information|Euler)', re.I)
RE_PRE_RANGE = re.compile(r'questions?\s+(.+)', re.I)
RE_KEY   = re.compile(r'^\s*(\d{1,2})[.)]?\s*([A-E])[.)]?\s*$')


TABULAR = re.compile(r'\S {3,}\S')

def is_tabular(lines):
    """A wide internal gap means pdftotext preserved a column layout."""
    return any(TABULAR.search(l) for l in lines)


# A stray page number occasionally lands on the same line as the next
# question, immediately before its real number, when pdftotext -layout
# collapses a two-column page footer into the body text — e.g. "4.   2.
# Which of the following...". Genuine prose never opens with two separate
# "N." tokens back to back, so stripping the first is safe.
RE_STRAY_NUM = re.compile(r'^\s*\d{1,2}[.)]\s+(?=\d{1,2}[.)]\s)')


def pdf_lines(path):
    txt = subprocess.run(['pdftotext', '-layout', str(path), '-'],
                         capture_output=True, text=True, check=True).stdout
    lines = txt.replace('\f', '\n').split('\n')
    return [RE_STRAY_NUM.sub('', l) for l in lines]


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
            # older diets title the FA paper "PRINCIPLES [AND/&] PRACTICE OF
            # FINANCIAL ACCOUNTING"; match the subject name anywhere in the
            # title, not just as a prefix, so both eras are found.
            if name in title.upper():
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


def pre_range_end(pre_lines):
    """The last question number a "Use the following ... to answer questions
    9 to 12" preamble applies to — the max of every integer following the
    word "question(s)" in it, which survives every phrasing seen in these
    papers ("9 to 12", "9 & 10", "13" alone, "4, 5 and 6", "16 – 19", ...).
    None if the preamble does not name a range at all (rare; those keep the
    old unbounded behaviour rather than being dropped outright). Only the
    preamble's own first line is examined — the range is always stated
    there ("...to answer questions 9 to 12") — never the scenario text
    that follows on later lines, which is often full of unrelated numbers
    (amounts, years) that would otherwise be mistaken for question numbers."""
    if not pre_lines:
        return None
    m = RE_PRE_RANGE.search(pre_lines[0])
    if not m:
        return None
    nums = [int(x) for x in re.findall(r'\d+', m.group(1))]
    return max(nums) if nums else None


def parse_mcq(block):
    """Numbered stems with A-E options; a shared preamble carries onto its
    group — but only for the range of question numbers it actually names.
    Without this a preamble like "Use the following information to answer
    questions 9 to 12" would keep attaching to every question from 13
    onward until (if ever) the next "Use the following..." line appears,
    silently mixing an unrelated scenario's vocabulary into every question
    in between — confirmed happening live (a Public Procurement question
    was carrying a pensions preamble meant only for questions 9-12)."""
    qs, cur, pre, pending = [], None, [], []
    pre_end = None
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
                pre_end = pre_range_end(pre)
            if pre_end is not None and expect > pre_end:
                pre, pre_end = [], None
            cur = {'n': expect, '_stem': [mq.group(2)], '_opts': [], 'pre': pre}
            expect += 1
            continue

        if RE_PRE.match(line):
            flush()
            pre, pre_end = [], None
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
    """Short-answer questions or their solutions: numbered prose, table-tolerant.

    A shared preamble stays attached for exactly the range of question
    numbers it names (see pre_range_end / parse_mcq above) — not just the
    single question right after it (which would leave the rest of the
    range with no shared data at all) and not forever (which would smear
    it onto every later question until, if ever, a new preamble appears).

    Once the first item has matched arabic or roman numbering, that choice
    is locked in for the rest of the block. Without this, a multi-part
    answer's own "i. / ii. / iii. ..." sub-bullets are indistinguishable
    from top-level roman question numbers whenever a sub-bullet's roman
    value happens to coincide with the next expected arabic question
    number — e.g. an arabic item 3's third sub-bullet "iii." is read as a
    new roman-numbered item 3, silently shredding that item's own answer
    across the two neighbouring items and shifting everything after it by
    one. Confirmed live on FA 2024-03's short-answer key (items 2-5)."""
    items, cur, pre, pending = [], None, [], []
    pre_end = None
    scheme = None  # locked to 'arabic' or 'roman' once item 1 is found
    for raw in block:
        line = raw.rstrip()
        if not line.strip():
            if cur:
                cur['body'].append('')
            elif pending:
                pending.append('')
            continue

        m = RE_QNUM.match(line) if scheme != 'roman' else None
        if m and int(m.group(1)) == expect and expect <= limit:
            scheme = 'arabic'
            if cur:
                items.append(cur)
            if pending:
                pre = squeeze(pending)
                pending = []
                pre_end = pre_range_end(pre)
            if pre_end is not None and expect > pre_end:
                pre, pre_end = [], None
            cur = {'n': expect, 'body': [tidy(m.group(2))], 'pre': pre}
            expect += 1
            continue

        mr = RE_QNUM_ROMAN.match(line) if scheme != 'arabic' else None
        if mr and ROMAN_VAL.get(mr.group(1).lower()) == expect and expect <= limit:
            scheme = 'roman'
            if cur:
                items.append(cur)
            if pending:
                pre = squeeze(pending)
                pending = []
                pre_end = pre_range_end(pre)
            if pre_end is not None and expect > pre_end:
                pre, pre_end = [], None
            cur = {'n': expect, 'body': [tidy(mr.group(2))], 'pre': pre}
            expect += 1
            continue

        if RE_PRE.match(line):
            if cur:
                items.append(cur)
                cur = None
            pre, pre_end = [], None
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
    # Normally "1.  C"; one diet prints the key as a bare "1   C" with no
    # punctuation at all — and its fixed-width columns give a 2-digit "10"
    # only a single trailing space where "1" gets three, so the gap after a
    # punctuation-less number can be as narrow as one space.
    key = {}
    for l in block:
        for m in re.finditer(r'(?:^|\s)(\d{1,2})(?:[.)]|\s+)\s*([A-E])(?=[\s.)]|$)', l):
            n = int(m.group(1))
            if 1 <= n <= 40 and n not in key:
                key[n] = m.group(2)
    return key


def parse_paper(lines, code, diet):
    n = len(lines)
    i_a1 = find(lines, RE_SECA1)
    i_a2 = find(lines, RE_SECA2, max(i_a1, 0))
    i_b  = find(lines, RE_SECB, max(i_a2, 0))

    # A few diets append a "MARKING GUIDE" pass after the real Section B
    # solutions, re-using "SOLUTION 1".."SOLUTION 6" headers a second time for
    # its mark breakdowns — but where that appendix falls varies (sometimes
    # one block at the very end, sometimes interleaved after each solution),
    # so detect it structurally instead: a genuine solution run only ever
    # holds steady or increases (a "2A"/"2B" pair repeats the same number),
    # so the first *decrease* marks the start of a second, spurious pass.
    raw_sols = [(bsol_num(m), i) for i, l in enumerate(lines)
                if (m := RE_BSOL.match(l)) and i > max(i_b, 0)]
    sols, last, sols_end = [], 0, n
    for num, i in raw_sols:
        if num < last:
            sols_end = i
            break
        sols.append((num, i))
        last = num
    sol_start = sols[0][1] if sols else n

    # the solutions region opens with a multiple-choice header somewhere between
    # the Section B paper and SOLUTION 1; take the first such header, since the
    # (deliberately loose) word-combination match can otherwise also catch a
    # later, incidental mention (e.g. an examiner's comment on MCQ performance).
    i_mc = -1
    for i in range(max(i_b, 0) + 1, sol_start):
        if RE_MCSOL.search(lines[i]):
            i_mc = i
            break
    i_sa = -1
    if i_mc > 0:
        for i in range(i_mc + 1, sol_start):
            if RE_SASOL.search(lines[i]):
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
        stop = sols[j + 1][1] if j + 1 < len(sols) else sols_end
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
