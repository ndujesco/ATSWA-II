#!/usr/bin/env python3
"""Build data/revision.js — the "Final Revision" question bank.

For each subject, groups every past MCQ / short-answer / Section B question
across all 24 diets into near-duplicate clusters (compilers reuse the same
question, verbatim or lightly reworded, across many diets), then lists every
cluster ordered by how many diets it was asked in — most-asked first. This is
approximate clustering ("how often-ish"), not exact dedup: it is tuned to
catch the very common near-verbatim repeats without merging genuinely
different questions that happen to share a topic.

Reads data/exams.js (already chapter/section-tagged by aim.py/aim_sec.py and
merged with official answers by build_exams.py) so it stays in sync with
whatever the app itself ships. Run after build_exams.py, before build.sh.
"""
import importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
CONTENT = ROOT / 'content'


def chapter_titles(code):
    """Chapter number -> its own title, for grouping the short-answer bank
    by topic instead of showing a bare chapter number."""
    out = {}
    for path in sorted((CONTENT / code.lower()).glob('ch*.py')):
        n = int(path.stem[2:])
        spec = importlib.util.spec_from_file_location(f'{code}_{n}_title', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out[n] = mod.CH.get('t', f'Chapter {n}')
    return out

STOP = {
    'the', 'a', 'an', 'of', 'to', 'in', 'is', 'are', 'and', 'or', 'for',
    'on', 'by', 'as', 'with', 'that', 'which', 'be', 'not', 'it', 'at',
    'from', 'was', 'were', 'this', 'these', 'following', 'each',
}


def txt_of(x):
    """A stem/option/body cell as plain text, for clustering only."""
    if x is None:
        return ''
    if isinstance(x, str):
        return x
    if isinstance(x, dict):
        s = x.get('t') or ''
        if x.get('pre'):
            s += ' ' + ' '.join(x['pre'])
        return s
    if isinstance(x, list):
        return ' '.join(txt_of(i) for i in x)
    return str(x)


RE_WS = re.compile(r'\s+')
RE_NONWORD = re.compile(r'[^a-z0-9 ]+')
RE_FURNITURE = re.compile(
    r'atswa part ii\s+\w+\s+\d{4}|insight|examiner.?s comment.*$', re.I)


def norm(s):
    s = s.lower()
    s = RE_FURNITURE.sub(' ', s)
    s = RE_NONWORD.sub(' ', s)
    s = RE_WS.sub(' ', s).strip()
    return s


def tokens(s):
    return [w for w in norm(s).split(' ') if w]


def cluster(items, threshold, min_len=8):
    """items: list of dicts with a 'norm' key (already normalised text) and
    a 'diet' key. Returns list of lists of indices, each one cluster.

    Two questions are the same "ask" if their significant-word sets overlap
    heavily (Jaccard on stopword-stripped tokens), which tolerates the kind
    of small rewording compilers do across diets ("...the Auditor-General"
    vs "...the Auditor-General for the Federation") far better than a
    character-level or fixed-length-prefix comparison would.

    Clustering is seed-anchored, not transitive union-find: each cluster is
    defined by the first (and longest-processed) text assigned to it, and
    every later candidate is compared directly against that fixed seed —
    never against other members it was chained through. Plain single-linkage
    (merge on any sufficiently-similar pair, transitively) lets A~B~C~D chain
    together four essay questions that share only generic scenario wording
    ("a company... the yearly costs... calculate...") even though A and D
    have nothing else in common; anchoring to a fixed seed avoids that drift
    because every member must itself pass the threshold against the seed,
    not merely against its nearest neighbour in the chain."""
    uniq = {}
    for i, it in enumerate(items):
        uniq.setdefault(it['norm'], []).append(i)
    texts = list(uniq.keys())
    texts.sort(key=len, reverse=True)  # longer, more distinctive text first
    tok = {t: frozenset(tokens(t)) - STOP for t in texts}

    seeds = []  # list of (seed_text, member_texts)
    for t in texts:
        if len(t) < min_len:
            seeds.append((t, [t]))
            continue
        a = tok[t]
        best_j, best_sim = -1, 0.0
        for j, (seed_t, _) in enumerate(seeds):
            b = tok[seed_t]
            if not a or not b:
                continue
            jac = len(a & b) / len(a | b)
            if jac > best_sim:
                best_sim, best_j = jac, j
        if best_j >= 0 and best_sim >= threshold:
            seeds[best_j][1].append(t)
        else:
            seeds.append((t, [t]))

    clusters = []
    for _, member_texts in seeds:
        idxs = []
        for t in member_texts:
            idxs.extend(uniq[t])
        clusters.append(idxs)
    return clusters


def split_by_answer(idxs, items, answer_fn, threshold=0.5):
    """A stem-similarity cluster can wrongly merge different questions that
    share a templated stem ("The necessary accounting entries required to
    record X in a partnership are...") but ask about different X — which
    then surfaces as one repeated-question entry with a single answer that
    contradicts what a candidate remembers seeing for the "same" question in
    another diet. This splits a stem cluster into sub-clusters that also
    agree on the answer, using the same anchored-seed Jaccard approach as
    cluster() so a repeated question with reworded or reordered-option
    phrasing of the *same* answer still merges, while genuinely different
    answers split apart. Confirmed live: roughly half of FA's multi-member
    MCQ and short-answer clusters had at least two distinct answers before
    this split."""
    by_norm = {}
    for i in idxs:
        by_norm.setdefault(norm(answer_fn(items[i])), []).append(i)
    texts = sorted(by_norm.keys(), key=len, reverse=True)
    tok = {t: frozenset(tokens(t)) - STOP for t in texts}
    seeds = []
    for t in texts:
        a = tok[t]
        best_j, best_sim = -1, 0.0
        for j, (seed_t, _) in enumerate(seeds):
            b = tok[seed_t]
            if not a or not b:
                continue
            jac = len(a & b) / len(a | b)
            if jac > best_sim:
                best_sim, best_j = jac, j
        if best_j >= 0 and best_sim >= threshold:
            seeds[best_j][1].append(t)
        else:
            seeds.append((t, [t]))
    out = []
    for _, member_texts in seeds:
        sub = []
        for t in member_texts:
            sub.extend(by_norm[t])
        out.append(sub)
    return out


def best_of(idxs, items, prefer_keys=()):
    """Pick the clearest representative of a cluster: prefer one with a
    confident chapter/section link, then the longest text (least likely to
    be OCR-truncated), then the earliest diet (stable, deterministic)."""
    def score(i):
        it = items[i]
        has_sec = 1 if it.get('sec') else 0
        has_ch = 1 if it.get('ch') else 0
        has_extra = sum(1 for k in prefer_keys if it.get(k))
        return (has_sec, has_ch, has_extra, len(it['norm']), it['diet'])
    return max(idxs, key=score)


def diets_of(idxs, items):
    return sorted({items[i]['diet'] for i in idxs})


def load_exams():
    txt = (DATA / 'exams.js').read_text()
    m = re.match(r'ATSWA\.put\("EXAMS",\s*(.*)\);\s*\Z', txt, re.S)
    if not m:
        sys.exit('data/exams.js not in the expected shape — run build_exams.py first')
    return json.loads(m.group(1))


def build_mcq(papers, code):
    items = []
    for p in papers:
        if p['subject'] != code:
            continue
        for q in p['mcq']:
            ans = p['key'].get(str(q['n']))
            a_idx = 'ABCDE'.index(ans) if ans and ans in 'ABCDE' else None
            stem_txt = txt_of(q['stem'])
            opt_txt = ' | '.join(txt_of(o) for o in q['options'])
            items.append({
                'diet': p['diet'], 'name': p['name'], 'n': q['n'],
                'stem': q['stem'], 'options': q['options'], 'aIdx': a_idx,
                'pre': q.get('pre') or [], 'ch': q.get('ch'), 'sec': q.get('sec'),
                'norm': norm(stem_txt),
                'norm_full': norm(stem_txt + ' ' + opt_txt),
            })
    def ans_text(it):
        if it['aIdx'] is None or it['aIdx'] >= len(it['options']):
            return ''
        return txt_of(it['options'][it['aIdx']])

    clusters = [sub for idxs in cluster(items, threshold=0.55)
                for sub in split_by_answer(idxs, items, ans_text)]
    out = []
    for idxs in clusters:
        rep = best_of(idxs, items)
        it = items[rep]
        if it['aIdx'] is None:
            continue  # no usable answer key — not revisable
        out.append({
            'stem': it['stem'], 'pre': it['pre'], 'options': it['options'],
            'a': it['aIdx'], 'ch': it['ch'], 'sec': it['sec'],
            'freq': len(diets_of(idxs, items)), 'diets': diets_of(idxs, items),
        })
    # Most-recent-diet first — the primary sort. freq and stem text are only
    # stable-sort tiebreakers (applied in reverse priority order, since
    # Python's sort is stable): a question last asked in 2026-03 always
    # outranks one last asked in 2025-09, however many times each has
    # repeated historically.
    out.sort(key=lambda x: norm(txt_of(x['stem'])))
    out.sort(key=lambda x: -x['freq'])
    out.sort(key=lambda x: max(x['diets']), reverse=True)
    for i, o in enumerate(out):
        o['n'] = i + 1
    return out


def build_saq(papers, code):
    items = []
    for p in papers:
        if p['subject'] != code:
            continue
        for q in p['saq']:
            if not q.get('ans'):
                continue
            body_txt = ' '.join(q['body'])
            items.append({
                'diet': p['diet'], 'name': p['name'], 'n': q['n'],
                'body': q['body'], 'ans': q['ans'], 'pre': q.get('pre') or [],
                'ch': q.get('ch'), 'sec': q.get('sec'),
                'norm': norm(body_txt),
            })
    clusters = [sub for idxs in cluster(items, threshold=0.50)
                for sub in split_by_answer(idxs, items, lambda it: ' '.join(it['ans']))]
    out = []
    for idxs in clusters:
        rep = best_of(idxs, items)
        it = items[rep]
        out.append({
            'body': it['body'], 'ans': it['ans'], 'pre': it['pre'],
            'ch': it['ch'], 'sec': it['sec'],
            'freq': len(diets_of(idxs, items)), 'diets': diets_of(idxs, items),
        })
    # Topical grouping, not a flat list: order chapters by how much that
    # chapter's material has been asked as a short answer overall (the sum
    # of each of its clusters' own "asked N times" count) — the best
    # available signal for which topics examiners keep coming back to —
    # then within a chapter, most-recently-asked question first. Chapters
    # that could not be confidently tagged fall in one final group.
    weight = {}
    for o in out:
        if o['ch']:
            weight[o['ch']] = weight.get(o['ch'], 0) + o['freq']

    def diet_num(d):
        return int(d.replace('-', ''))

    def sort_key(o):
        ch = o['ch']
        recency = -max(diet_num(d) for d in o['diets'])
        if not ch:
            return (1, 0, 0, recency, -o['freq'], norm(' '.join(o['body'])))
        return (0, -weight[ch], ch, recency, -o['freq'], norm(' '.join(o['body'])))

    out.sort(key=sort_key)
    for i, o in enumerate(out):
        o['n'] = i + 1
    return out


def build_essay(papers, code):
    items = []
    for p in papers:
        if p['subject'] != code:
            continue
        for b in p['secb']:
            if not b.get('solution'):
                continue
            q_txt = ' '.join(b.get('q') or [])
            items.append({
                'diet': p['diet'], 'name': p['name'], 'n': b['n'],
                'q': b.get('q') or [], 'solution': b['solution'],
                'examiner': b.get('examiner') or [],
                'ch': b.get('ch'), 'sec': b.get('sec'),
                'norm': norm(q_txt),
            })
    clusters = cluster(items, threshold=0.42, min_len=20)
    out = []
    for idxs in clusters:
        rep = best_of(idxs, items, prefer_keys=('examiner',))
        it = items[rep]
        out.append({
            'q': it['q'], 'solution': it['solution'], 'examiner': it['examiner'],
            'ch': it['ch'], 'sec': it['sec'],
            'freq': len(diets_of(idxs, items)), 'diets': diets_of(idxs, items),
        })
    out.sort(key=lambda x: norm(' '.join(x['q'])))
    out.sort(key=lambda x: -x['freq'])
    out.sort(key=lambda x: max(x['diets']), reverse=True)
    for i, o in enumerate(out):
        o['n'] = i + 1
    return out


def main():
    blob = load_exams()
    papers = blob['papers']
    codes = sorted({p['subject'] for p in papers})
    result = {}
    for code in codes:
        mcq = build_mcq(papers, code)
        saq = build_saq(papers, code)
        essay = build_essay(papers, code)
        result[code] = {'mcq': mcq, 'saq': saq, 'essay': essay,
                         'chapters': chapter_titles(code)}
        print(f"{code}: {len(mcq)} MCQ clusters, {len(saq)} short-answer clusters, "
              f"{len(essay)} essay clusters "
              f"(top MCQ freq {mcq[0]['freq'] if mcq else 0}, "
              f"top essay freq {essay[0]['freq'] if essay else 0})")
    js = 'ATSWA.put("REVISION", ' + json.dumps(result, ensure_ascii=False, separators=(',', ':')) + ');\n'
    (DATA / 'revision.js').write_text(js)
    print(f'data/revision.js  {len(js)//1024} KB')


if __name__ == '__main__':
    main()
