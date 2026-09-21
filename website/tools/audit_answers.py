#!/usr/bin/env python3
"""
Precision audit: for every PS MCQ, does the *correct answer's own text*
actually appear anywhere in the site's authored PS chapters — and if so,
which chapter, and does it match what the question is currently tagged to?

This sidesteps all the ambiguity of stem-based TF-IDF matching (generic
distractor words, shared vocabulary between chapters, etc.) by searching for
something much more specific: the literal answer phrase itself. An MCQ
answer is usually a short, distinctive term ("Specific grant", "Board of
Enquiry") — if that phrase exists nowhere in any PS chapter, that is real,
concrete evidence of a content gap, not a retrieval failure. If it exists in
exactly one chapter that differs from the current tag, that is real,
concrete evidence of a mis-link.

Numeric-only or very short/generic answers (dates, percentages, single common
words) are skipped — they are not distinctive enough for phrase search to
mean anything.
"""
import importlib.util, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'website' / 'data'
SUBJECT = (sys.argv[1] if len(sys.argv) > 1 else 'PS').upper()
CONTENT = ROOT / 'website' / 'content' / SUBJECT.lower()
MAXCH = {'PS': 23, 'FA': 16, 'QA': 20, 'IT': 6}[SUBJECT]

STOP = set('''a an the and or but if of to in on at by for with from as is are was were be been
being it its this that these those which who whom what when where how why not no nor so than
following use used using given the a an under per each which of and or'''.split())


def bag_of(node, acc):
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


def load_chapter(n):
    path = CONTENT / f'ch{n:02d}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f'{SUBJECT}_{n}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CH


def norm(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def significant_words(phrase):
    return [w for w in norm(phrase).split(' ') if w and w not in STOP and len(w) > 2]


def txt_of(x):
    if x is None:
        return ''
    if isinstance(x, str):
        return x
    if isinstance(x, dict):
        return x.get('t') or ''
    return ''


def check_answer(ans_text, chapters_text, cur_ch, results):
    sig = significant_words(ans_text)
    # skip answers too short/generic to search meaningfully, or that are
    # essentially just a number (a year, a percentage, a naira figure) —
    # phrase search on those is meaningless noise. Also skip long
    # descriptive-sentence answers (>6 significant words) — those are the
    # exam-writer's own paraphrase of a concept, not a quotable term, so
    # verbatim/near-verbatim phrase search on them produces false "gaps"
    # even when the underlying concept is well covered in ordinary prose
    # elsewhere in the chapter.
    if len(sig) < 2 or len(sig) > 6 or not any(w.isalpha() and len(w) > 4 for w in sig):
        results['skipped'] += 1
        return None
    # search using the FULL normalised phrase (stopwords included —
    # "minister of finance", not "minister finance") since the chapter text
    # itself was never stopword-stripped; searching for the stripped phrase
    # would never match a phrase like "Minister of Finance" at all
    phrase = norm(ans_text)
    words = phrase.split(' ')
    # only try the "drop the trailing word" fallback when what's left is
    # still at least 2 genuinely distinctive words — "Finance or
    # compliance" -> "finance or" is worthless (1 real word) and matches
    # almost anywhere; confirmed live producing false mislinks
    short = None
    if len(words) >= 4:
        cand = ' '.join(words[:-1])
        if len([w for w in cand.split(' ') if w not in STOP and len(w) > 3]) >= 2:
            short = cand
    found_in = []
    for n, full in chapters_text.items():
        if phrase in full or (short and short in full):
            found_in.append(n)
    if not found_in:
        return 'gap'
    if cur_ch in found_in:
        results['ok'] += 1
        return None
    if len(found_in) == 1:
        return ('mislink', found_in[0])
    return ('ambiguous', found_in)


def main():
    chapters_text = {}   # n -> normalised full chapter text
    for n in range(1, MAXCH + 1):
        ch = load_chapter(n)
        if not ch:
            continue
        words = []
        bag_of(ch.get('secs'), words)
        chapters_text[n] = norm(' '.join(words))

    papers = json.loads((DATA / 'papers.json').read_text())
    results = {'ok': 0, 'skipped': 0}
    gaps, mislinks, ambiguous = [], [], []

    NEG = re.compile(r'\bnot\b|\bexcept\b|\bcannot\b|\bnota\b|\bnotan\b', re.I)

    for p in papers:
        if p['subject'] != SUBJECT:
            continue
        key = p['mcq_key']
        for q in p['mcq']:
            ans_letter = key.get(str(q['n']))
            if not ans_letter or ans_letter not in 'ABCDE':
                continue
            stem_check = txt_of(q['stem'])
            # "Which of the following is NOT..." / "...EXCEPT" questions:
            # the correct answer is, BY CONSTRUCTION, the one option that is
            # *not* a real item from the source — it is supposed to be
            # absent. Phrase-searching those for "is it in the text" would
            # report a false gap on almost every one of them; only the
            # "positive" questions (find the one that IS correct/true) are a
            # fair test of "does this term actually appear in the chapter".
            if NEG.search(stem_check):
                results['skipped'] += 1
                continue
            idx = 'ABCDE'.index(ans_letter)
            if idx >= len(q['options']):
                continue
            ans_text = txt_of(q['options'][idx])
            cur_ch = q.get('ch')
            r = check_answer(ans_text, chapters_text, cur_ch, results)
            stem_txt = stem_check[:100]
            if r == 'gap':
                gaps.append(('mcq', p['diet'], q['n'], cur_ch, q.get('sec'), ans_text, stem_txt))
            elif r and r[0] == 'mislink':
                mislinks.append(('mcq', p['diet'], q['n'], cur_ch, q.get('sec'), r[1], ans_text, stem_txt))
            elif r and r[0] == 'ambiguous':
                ambiguous.append(('mcq', p['diet'], q['n'], cur_ch, r[1], ans_text, stem_txt))

        sol = {s['n']: s for s in p['saq_solutions']}
        for q in p['saq']:
            s = sol.get(q['n'])
            if not s or not s.get('body'):
                continue
            body_txt = ' '.join(q['body'])
            if NEG.search(body_txt):
                results['skipped'] += 1
                continue
            ans_text = ' '.join(s['body'])
            # a short-answer solution is sometimes several alternative
            # acceptable phrasings on one line ("Cash and Bank" / "Cash
            # book") — treat the whole line as one phrase; multi-sentence
            # solutions are already excluded by the word-count cap below
            cur_ch = q.get('ch')
            r = check_answer(ans_text, chapters_text, cur_ch, results)
            stem_txt = body_txt[:100]
            if r == 'gap':
                gaps.append(('saq', p['diet'], q['n'], cur_ch, q.get('sec'), ans_text, stem_txt))
            elif r and r[0] == 'mislink':
                mislinks.append(('saq', p['diet'], q['n'], cur_ch, q.get('sec'), r[1], ans_text, stem_txt))
            elif r and r[0] == 'ambiguous':
                ambiguous.append(('saq', p['diet'], q['n'], cur_ch, r[1], ans_text, stem_txt))

    print(f"OK (answer found in currently-assigned chapter): {results['ok']}")
    print(f"Skipped (answer too short/generic/numeric/NOT-style to search): {results['skipped']}")
    print(f'\n=== CONTENT GAPS — answer phrase not found in ANY {SUBJECT} chapter ({len(gaps)}) ===')
    for typ, diet, n, ch, sec, ans, stem in gaps:
        print(f'{typ} {diet} Q{n}  currently ch={ch} sec={sec}  ANSWER="{ans}"  STEM: {stem}')
    print(f'\n=== MISLINKS — answer found in exactly ONE chapter, differs from tag ({len(mislinks)}) ===')
    for typ, diet, n, cur, sec, correct, ans, stem in mislinks:
        print(f'{typ} {diet} Q{n}  tagged ch={cur} sec={sec} -> should be ch={correct}  ANSWER="{ans}"  STEM: {stem}')
    print(f'\n=== AMBIGUOUS — answer found in multiple chapters, current tag not among them ({len(ambiguous)}) ===')
    for typ, diet, n, cur, found, ans, stem in ambiguous:
        print(f'{typ} {diet} Q{n}  tagged ch={cur}, found in {found}  ANSWER="{ans}"  STEM: {stem}')


if __name__ == '__main__':
    main()
