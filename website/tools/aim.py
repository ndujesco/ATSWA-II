#!/usr/bin/env python3
"""
Assign every past question to the study-text chapter it belongs to.

Retrieval, not classification: the words of a question (stem, options, official
solution) are scored against each chapter of that subject by inverse document
frequency computed *within the subject* — a word spread over every chapter counts
for little, a word that lives in one chapter counts for a lot. A hit in the
chapter's own title is weighted heavily; chapter length is discounted so the
longest chapter cannot win by bulk alone.

Writes the chapter id back into data/papers.json and prints the confidence split.
"""
import json, math, re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import tidy, desymbol
from outline import chapters, FILES, ST
from corrections import CHAPTER_KEYS, PIN

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'website' / 'data'

STOP = set('''a an the and or but if of to in on at by for with from as is are was were be been
being it its this that these those which who whom what when where how why not no nor so than then
there here all any each every both few more most other some such only own same too very can will
just should now also may might must shall would could into over under above below out up down off
following use used using given calculate compute determine find state list explain describe outline
question questions answer answers option options correct following amount total value figure figures
value values year years period end ended during above below shown table data information account
accounts b c d e i ii iii iv v vi n gh le d one two three four five six seven eight nine ten'''.split())

WORD = re.compile(r"[a-z][a-z'-]{2,}")


def tokens(s):
    s = desymbol(s).lower()
    return [w for w in WORD.findall(s) if w not in STOP and len(w) > 2]


def stem(w):
    for suf in ('ies', 'ing', 'ers', 'es', 's'):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[:-len(suf)] + ('y' if suf == 'ies' else '')
    return w


def chapter_text(code):
    """Chapter number -> (title, bag of stemmed words)."""
    txt = subprocess.run(['pdftotext', '-layout', str(ST / FILES[code]), '-'],
                         capture_output=True, text=True, check=True).stdout
    lines = txt.replace('\f', '\n').split('\n')
    chs = chapters(code)
    marks = []
    idx = 0
    for n, title, secs, span in chs:
        # relocate the chapter start: chapters() already knows the span
        marks.append((n, title, span))
    # rebuild positions by re-scanning, mirroring outline.chapters()
    from outline import RE_CH, NUM
    pos = []
    for i, l in enumerate(lines):
        m = RE_CH.match(l)
        if not m:
            continue
        tail = [x for x in lines[i + 1:i + 8] if x.strip()][:4]
        if any('....' in x for x in tail):
            continue
        g = m.group(1).upper()
        pos.append((NUM.get(g) or int(m.group(1)), i))
    best = []
    for n, i in pos:
        if n == 1:
            best = []
        if not best or n >= best[-1][0]:
            best.append((n, i))
    out = {}
    for j, (n, i) in enumerate(best):
        end = best[j + 1][1] if j + 1 < len(best) else len(lines)
        title = next((tidy(x) for x in lines[i + 1:i + 6] if x.strip()), '')
        body = ' '.join(lines[i:end])
        out[n] = (title, Counter(stem(w) for w in tokens(body)))
    return out


def build_index(code):
    chs = chapter_text(code)
    # fold the curated seed vocabulary in as a separate, heavily weighted signal
    keys = {n: set(stem(w) for w in tokens(v))
            for n, v in CHAPTER_KEYS.get(code, {}).items()}
    N = len(chs)
    df = Counter()
    for n, (t, bag) in chs.items():
        for w in bag:
            df[w] += 1
    idf = {w: math.log(1 + N / d) for w, d in df.items()}
    titles = {n: set(stem(w) for w in tokens(t)) | keys.get(n, set())
              for n, (t, bag) in chs.items()}
    lens = {n: sum(bag.values()) for n, (t, bag) in chs.items()}
    avg = sum(lens.values()) / max(N, 1)
    # a seed term is worth far more than a word that merely occurs in the chapter
    seed_idf = {}
    owners = Counter()
    for n, ks in keys.items():
        for w in ks:
            owners[w] += 1
    for w, o in owners.items():
        seed_idf[w] = 9.0 / o
    return chs, idf, titles, lens, avg, keys, seed_idf


def score(qwords, chs, idf, titles, lens, avg, keys, seed_idf):
    out = {}
    for n, (title, bag) in chs.items():
        s = 0.0
        norm = 0.4 + 0.6 * (lens[n] / avg)          # length discount
        ks = keys.get(n, ())
        for w, c in qwords.items():
            if w in ks:
                s += c * seed_idf.get(w, 3.0) * norm  # seed hits ignore length
            if w not in bag:
                continue
            tf = 1 + math.log(bag[w])
            s += c * idf.get(w, 0) * tf
            if w in titles[n]:
                s += c * idf.get(w, 0) * 4.0        # a hit in the chapter title
        out[n] = s / norm
    return out


def flatten(node, acc):
    if isinstance(node, str):
        acc.append(node)
    elif isinstance(node, list):
        for v in node:
            flatten(v, acc)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k not in ('pre',):
                flatten(v, acc)
    return acc


def main():
    papers = json.loads((DATA / 'papers.json').read_text())
    idx = {c: build_index(c) for c in ('FA', 'PS', 'QA', 'IT')}
    stats = Counter()
    per = defaultdict(Counter)

    for p in papers:
        chs, idf, titles, lens, avg, keys, seed_idf = idx[p['subject']]

        def assign(text_parts):
            qw = Counter(stem(w) for w in tokens(' '.join(text_parts)))
            if not qw:
                return None, 0.0
            sc = score(qw, chs, idf, titles, lens, avg, keys, seed_idf)
            rank = sorted(sc.items(), key=lambda kv: -kv[1])
            top, second = rank[0], (rank[1] if len(rank) > 1 else (0, 0.0))
            margin = (top[1] - second[1]) / top[1] if top[1] else 0
            return top[0], margin

        for q in p['mcq']:
            parts = flatten(q['stem'], []) + flatten(q['options'], []) + q.get('pre', [])
            ch, m = assign(parts)
            pin = PIN.get((p['diet'], p['subject'], 'mcq', q['n']))
            if pin:
                ch, m = pin, 1.0
            q['ch'], q['chConf'] = ch, round(m, 3)
            stats['mcq_hi' if m >= .12 else 'mcq_lo'] += 1
            per[p['subject']][ch] += 1

        sol = {s['n']: s for s in p['saq_solutions']}
        for q in p['saq']:
            parts = q['body'] + q.get('pre', []) + (sol[q['n']]['body'] if q['n'] in sol else [])
            ch, m = assign(parts)
            q['ch'], q['chConf'] = ch, round(m, 3)
            stats['saq_hi' if m >= .12 else 'saq_lo'] += 1

        for s in p['secb_solutions']:
            ch, m = assign(s['solution'][:60])
            s['ch'], s['chConf'] = ch, round(m, 3)
            stats['secb_hi' if m >= .12 else 'secb_lo'] += 1

    (DATA / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=1))
    print('confidence split:', dict(stats))
    for c in ('FA', 'PS', 'QA', 'IT'):
        chs = idx[c][0]
        print(f'\n{c}: questions per chapter')
        for n in sorted(chs):
            print(f'   {n:>2} {chs[n][0][:52]:54s} {per[c][n]:>3}')


if __name__ == '__main__':
    main()
