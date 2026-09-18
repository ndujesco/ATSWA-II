#!/usr/bin/env python3
"""
Refine the chapter-level tag on each past question into a section-level one,
for subjects whose content/<code>/ch*.py files exist.

Same retrieval idea as aim.py, one level down: instead of scoring a question
against whole chapters, score it against the sections *within* the chapter
aim.py already assigned. IDF here is computed over that chapter's own
sections (a small corpus), so it is noisier than the chapter-level pass —
a 'sec' is only written back when the top section clears the runner-up by a
real margin, and only for questions whose chapter tag itself was confident.
Otherwise the question still links to the chapter, just not to one section
inside it.

Writes 'sec' (e.g. "2.6") and 'secConf' onto each question in data/papers.json.
"""
import importlib.util, json, math, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'website' / 'content'
DATA = ROOT / 'website' / 'data'

CH_CONF_MIN = 0.10   # below this the chapter tag itself is too shaky to refine
MARGIN_MIN = 0.10    # top section must beat the runner-up by at least this much

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
    s = re.sub(r'[₦¢$%,]', ' ', str(s).lower())
    return [w for w in WORD.findall(s) if w not in STOP and len(w) > 2]


def stem(w):
    for suf in ('ies', 'ing', 'ers', 'es', 's'):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[:-len(suf)] + ('y' if suf == 'ies' else '')
    return w


def bag_of(node, acc):
    """Walk the block-schema tree exactly as render.js's text() does."""
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


def section_index(code, n):
    """secId -> Counter of stemmed words, for every section of chapter n."""
    ch = load_chapter(code, n)
    if not ch:
        return {}
    out = {}
    for sec in ch.get('secs', []):
        words = []
        bag_of(sec.get('t'), words)
        bag_of(sec.get('b'), words)
        out[sec['n']] = (sec.get('t', ''), Counter(stem(w) for w in tokens(' '.join(words))))
    return out


def score_sections(qwords, secs):
    if not secs:
        return []
    N = len(secs)
    df = Counter()
    for _, (title, bag) in secs.items():
        for w in bag:
            df[w] += 1
    idf = {w: math.log(1 + N / d) for w, d in df.items()}
    lens = {sid: sum(bag.values()) for sid, (t, bag) in secs.items()}
    avg = sum(lens.values()) / max(N, 1) or 1
    out = []
    for sid, (title, bag) in secs.items():
        norm = 0.4 + 0.6 * (lens[sid] / avg)
        titlew = set(stem(w) for w in tokens(title))
        s = 0.0
        for w, c in qwords.items():
            if w not in bag:
                continue
            tf = 1 + math.log(bag[w])
            s += c * idf.get(w, 0) * tf
            if w in titlew:
                s += c * idf.get(w, 0) * 4.0
        out.append((sid, s / norm))
    out.sort(key=lambda kv: -kv[1])
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


def assign(text_parts, sec_idx):
    qw = Counter(stem(w) for w in tokens(' '.join(text_parts)))
    if not qw:
        return None, 0.0
    ranked = score_sections(qw, sec_idx)
    if not ranked:
        return None, 0.0
    top = ranked[0]
    second = ranked[1][1] if len(ranked) > 1 else 0.0
    if top[1] <= 0:
        return None, 0.0
    margin = (top[1] - second) / top[1]
    return top[0], margin


def main(codes):
    papers = json.loads((DATA / 'papers.json').read_text())
    cache = {}
    stats = Counter()

    def idx_for(code, n):
        key = (code, n)
        if key not in cache:
            cache[key] = section_index(code, n)
        return cache[key]

    for p in papers:
        if p['subject'] not in codes:
            continue
        # Clear any 'sec'/'secConf' left over from a previous run *before*
        # recomputing. aim.py's own chapter tag can (and does) change
        # between runs — e.g. a chapter's seed vocabulary gets refined, or
        # its reference corpus is rebuilt — and a question left unplaced
        # this time (margin too thin under its *new* chapter) would
        # otherwise keep whatever 'sec' it was given under its *old*
        # chapter, silently pointing at a different chapter's section
        # number. Confirmed live in data/papers.json before this fix: 243
        # of 4259 sec-tagged questions across all four subjects had
        # sec.split('.')[0] != ch — a stale cross-chapter citation that
        # would either fail to scroll (right chapter, no such section) or,
        # worse, look confident while pointing at the wrong place entirely.
        for q in p['mcq'] + p['saq']:
            q['sec'], q['secConf'] = None, None
        for s in p['secb_solutions']:
            s['sec'], s['secConf'] = None, None

        for q in p['mcq']:
            if q.get('ch') and q.get('chConf', 0) >= CH_CONF_MIN:
                parts = flatten(q['stem'], []) + flatten(q['options'], []) + q.get('pre', [])
                sec_idx = idx_for(p['subject'], q['ch'])
                sid, m = assign(parts, sec_idx)
                if sid and m >= MARGIN_MIN:
                    q['sec'], q['secConf'] = sid, round(m, 3)
                    stats['mcq_placed'] += 1
                else:
                    stats['mcq_unplaced'] += 1
        sol = {s['n']: s for s in p['saq_solutions']}
        for q in p['saq']:
            if q.get('ch') and q.get('chConf', 0) >= CH_CONF_MIN:
                parts = q['body'] + q.get('pre', []) + (sol[q['n']]['body'] if q['n'] in sol else [])
                sec_idx = idx_for(p['subject'], q['ch'])
                sid, m = assign(parts, sec_idx)
                if sid and m >= MARGIN_MIN:
                    q['sec'], q['secConf'] = sid, round(m, 3)
                    stats['saq_placed'] += 1
                else:
                    stats['saq_unplaced'] += 1
        for s in p['secb_solutions']:
            if s.get('ch') and s.get('chConf', 0) >= CH_CONF_MIN:
                sec_idx = idx_for(p['subject'], s['ch'])
                sid, m = assign(s['solution'][:60], sec_idx)
                if sid and m >= MARGIN_MIN:
                    s['sec'], s['secConf'] = sid, round(m, 3)
                    stats['secb_placed'] += 1
                else:
                    stats['secb_unplaced'] += 1

    (DATA / 'papers.json').write_text(json.dumps(papers, ensure_ascii=False, indent=1))
    print('section assignment:', dict(stats))


if __name__ == '__main__':
    codes = set(sys.argv[1:]) or {'FA'}
    main(codes)
