#!/usr/bin/env python3
"""
Assign every past question to the study-text chapter it belongs to.

Retrieval, not classification: the words of a question (stem, options, official
solution) are scored against each chapter of that subject by inverse document
frequency computed *within the subject* — a word spread over every chapter counts
for little, a word that lives in one chapter counts for a lot. A hit in the
chapter's own title is weighted heavily; chapter length is discounted so the
longest chapter cannot win by bulk alone.

The reference corpus for each chapter is OUR OWN authored content/<code>/ch*.py
— not the raw study-text PDF. It used to be the PDF (a full pdftotext dump from
one chapter heading to the next), which folds in every worked example, every
number in every table, and OCR noise, all counted as plain word frequency; a
question mentioning "grants" several times could out-score the chapter that
actually explains grants-in-aid, just because some other chapter's worked
example happens to repeat the word "grants" in a table more often. Our own
chapters are clean prose organised exactly the way we want questions matched
to them, and aim_sec.py already builds its (better-performing) section-level
index the same way — this makes the two passes consistent, and any content
fix made to a chapter improves its retrieval immediately, with no separate
re-extraction step.

Writes the chapter id back into data/papers.json and prints the confidence split.
"""
import importlib.util, json, math, re, sys
from collections import Counter, defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import desymbol
from corrections import CHAPTER_KEYS, PIN

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'website' / 'data'
CONTENT = ROOT / 'website' / 'content'

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


def bag_of(node, acc):
    """Walk the block-schema tree exactly as render.js's text() does — same
    helper as aim_sec.py's, duplicated rather than imported to keep each
    tool script runnable standalone."""
    if node is None:
        return
    if isinstance(node, str):
        acc.append(node)
    elif isinstance(node, list):
        for v in node:
            bag_of(v, acc)
    elif isinstance(node, dict):
        for v in node.values():
            bag_of(v, acc)


def load_chapter(code, n):
    path = CONTENT / code.lower() / f'ch{n:02d}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f'{code}_{n}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CH


def chapter_text(code):
    """Chapter number -> (title, bag of stemmed words), built from every
    section of our own authored chapter — title, brief, outcomes, body,
    focus and errors all count; formulas/quiz are left out (they are
    exam-facing already, not the explanatory prose a question is "about")."""
    out = {}
    for path in sorted((CONTENT / code.lower()).glob('ch*.py')):
        n = int(path.stem[2:])
        ch = load_chapter(code, n)
        if not ch:
            continue
        words = []
        bag_of(ch.get('t'), words)
        bag_of(ch.get('brief'), words)
        bag_of(ch.get('outcomes'), words)
        for sec in ch.get('secs', []):
            bag_of(sec.get('t'), words)
            bag_of(sec.get('b'), words)
        bag_of(ch.get('focus'), words)
        bag_of(ch.get('errors'), words)
        out[n] = (ch.get('t', ''), Counter(stem(w) for w in tokens(' '.join(words))))
    return out


def build_index(code):
    chs = chapter_text(code)
    # fold the curated seed vocabulary in as a separate, heavily weighted signal
    keys = {n: set(stem(w) for w in tokens(v))
            for n, v in CHAPTER_KEYS.get(code, {}).items()}
    # confine retrieval to chapters the site actually has content for — a study
    # text chapter with no CHAPTER_KEYS entry (and so no authored site chapter)
    # would otherwise attract questions into a citation that has nowhere to go
    if keys:
        chs = {n: v for n, v in chs.items() if n in keys}
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


RE_Q = re.compile(r'^\s*QUESTION\s+(\d)\b', re.I)


def split_secb(lines):
    """Cut the Section B paper into its questions — same logic as
    build_exams.py's split_secb, duplicated so aim.py can score a question
    against its own scenario text, not just its solution's working."""
    marks = [(i, int(m.group(1))) for i, l in enumerate(lines) if (m := RE_Q.match(l))]
    out = {}
    for j, (i, n) in enumerate(marks):
        end = marks[j + 1][0] if j + 1 < len(marks) else len(lines)
        out[n] = [l.rstrip() for l in lines[i + 1:end]]
    return out


def main():
    papers = json.loads((DATA / 'papers.json').read_text())
    idx = {c: build_index(c) for c in ('FA', 'PS', 'QA', 'IT')}
    stats = Counter()
    per = defaultdict(Counter)

    for p in papers:
        chs, idf, titles, lens, avg, keys, seed_idf = idx[p['subject']]
        secb_qs = split_secb(p['secb_paper'])

        def assign(weighted_parts):
            qw = Counter()
            for parts, weight in weighted_parts:
                for w in tokens(' '.join(parts)):
                    qw[stem(w)] += weight
            if not qw:
                return None, 0.0
            sc = score(qw, chs, idf, titles, lens, avg, keys, seed_idf)
            rank = sorted(sc.items(), key=lambda kv: -kv[1])
            top, second = rank[0], (rank[1] if len(rank) > 1 else (0, 0.0))
            margin = (top[1] - second[1]) / top[1] if top[1] else 0
            return top[0], margin

        for q in p['mcq']:
            # the stem carries the actual subject matter; the four wrong
            # options are often just plausible-sounding entities (officer
            # titles, standard numbers) that happen to be another chapter's
            # core vocabulary — weighting them equally with the stem let
            # them drag the match toward whichever chapter's seed words
            # they matched, regardless of what the question was actually
            # about (e.g. a stores/inventory question whose options were
            # five officer titles, pulled toward the "officers" chapter).
            weighted = [
                (flatten(q['stem'], []) + q.get('pre', []), 3.0),
                (flatten(q['options'], []), 1.0),
            ]
            ch, m = assign(weighted)
            pin = PIN.get((p['diet'], p['subject'], 'mcq', q['n']))
            if pin:
                ch, m = pin, 1.0
            q['ch'], q['chConf'] = ch, round(m, 3)
            stats['mcq_hi' if m >= .12 else 'mcq_lo'] += 1
            per[p['subject']][ch] += 1

        sol = {s['n']: s for s in p['saq_solutions']}
        for q in p['saq']:
            weighted = [
                (q['body'] + q.get('pre', []), 2.0),
                (sol[q['n']]['body'] if q['n'] in sol else [], 2.0),
            ]
            ch, m = assign(weighted)
            pin = PIN.get((p['diet'], p['subject'], 'saq', q['n']))
            if pin:
                ch, m = pin, 1.0
            q['ch'], q['chConf'] = ch, round(m, 3)
            stats['saq_hi' if m >= .12 else 'saq_lo'] += 1

        for s in p['secb_solutions']:
            # the question's own scenario text (what it is actually about)
            # is weighted well above the solution's numeric working, which
            # is mostly figures and layout rather than topic vocabulary.
            weighted = [
                (secb_qs.get(s['n'], [])[:40], 3.0),
                (s['solution'][:60], 1.0),
            ]
            ch, m = assign(weighted)
            pin = PIN.get((p['diet'], p['subject'], 'secb', s['n']))
            if pin:
                ch, m = pin, 1.0
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
