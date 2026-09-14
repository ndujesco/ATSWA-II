# ATSWA Part II — Study

The four ATSWA Part II subjects as chapter-by-chapter study notes with worked
examples, typeset formulas and per-chapter quizzes, next to 24 diets of past
papers with the official solutions.

## Deploy

The whole folder is the site: `index.html` plus `data/*.js`. No build step at
deploy time, no dependencies, no server-side anything. The only external request
is to Google Fonts.

```sh
python3 -m http.server 8000        # preview at http://localhost:8000
npx netlify-cli deploy --prod --dir .
npx vercel --prod
npx wrangler pages deploy .
npx surge . your-name.surge.sh
```

For GitHub Pages: commit the folder, then Settings → Pages → deploy from branch → `/`.

Serve it over `http://` rather than opening `index.html` from the filesystem —
the chapter data is fetched by script injection and some browsers block that on
`file://`.

## What is here

| | |
|---|---|
| `index.html` | Generated. The whole app: markup, CSS, TeX renderer, quiz engine. |
| `data/fa.js` `ps.js` `qa.js` `it.js` | Generated chapter content, loaded when a subject is opened. |
| `data/exams.js` | Generated. 20 past papers with solutions. |
| `data/papers.json` | Intermediate extraction output; not needed at runtime. |
| `src/` | App sources. |
| `content/<code>/ch*.py` | The authored chapter notes, one module per chapter. |
| `tools/` | The extraction and build pipeline. |

## Rebuilding

```sh
python3 tools/extract_papers.py    # PDFs  -> data/papers.json
python3 tools/aim.py               # map every question to a chapter
python3 tools/build_exams.py       # papers.json -> data/exams.js
python3 tools/build_content.py     # content/ -> data/fa.js etc
./build.sh                         # src/ -> index.html
```

`extract_papers.py` needs `pdftotext` (poppler). Nothing else has dependencies.

`build_content.py` validates as it builds: unknown block types, unbalanced TeX
braces and out-of-range answer indices fail the build rather than the page.

## Where the material comes from

Chapter notes are written from the **2025 ATSWA Part II study texts (fifth
edition)** in `../materials/study-texts/`. Past papers are the real papers from
the 24 **INSIGHT** packs in `../materials/past-questions/`, March 2014 to March
2026 (missing only March 2016), with the examiners' own solutions and reports.

Every past question is assigned to a chapter by in-subject IDF retrieval against
the study text, boosted by a curated per-chapter vocabulary in
`tools/corrections.py`. Chapter quizzes draw on those mapped questions as well as
the questions written for the chapter.

Where a printed paper is defective, `FLAGS` in `tools/corrections.py` records it
and the site shows a "check this" note rather than silently picking a side.

## Content schema

A chapter module defines `CH`:

```python
CH = {
  'n': 9, 't': 'Accounting for Non-Current Assets',
  'brief': '...', 'outcomes': [...],
  'secs': [{'n': '9.1', 't': 'What goes into cost', 'b': [ ...blocks... ]}],
  'formulas': [{'lb': '...', 'tex': '...', 'nt': '...'}],
  'focus': '...', 'errors': [...],
  'quiz': {'mcq': [{'q','o','a','w','calc','src'}], 'theory': [{'q','marks','a','src'}]},
}
```

Blocks: `p` `h3` `h4` `ul` `ol` `steps` `tex` `def` `note` `key` `warn` `pre`
`table` `eg` `tacc` `stmt` `fbox`. Inside any string: `$tex$` for maths,
`**bold**`, `*italic*`, `` `mono` ``, `~aside~`, `[label](#/route)`.

## Maths

`src/math.js` renders a LaTeX subset to MathML Core — real fractions, radicals,
summations with limits, stretchy delimiters, matrices, aligned blocks — laid out
natively by the browser with no library. A Unicode one-liner is the fallback
where MathML is unavailable.

## Keys

`A`–`E` answer · `S` show answer · `J` jump · `←` `→` move · `/` search · `Esc` close
