# Where the build stopped

## Done and verified
- Materials reorganised into `materials/study-texts/` and `materials/past-questions/`.
- Extraction pipeline complete. All 20 past papers parse: 600 MCQs + keys,
  400 short answers + solutions, 120 Section B questions + official solutions
  and examiner reports. Symbol-font codepoints decoded; column layouts preserved.
- Question→chapter mapping across all 62 chapters (seed lexicon in
  `tools/corrections.py`).
- App complete and regression-tested (14/14 headless tests pass): routing,
  chapter reader with sticky TOC, TeX→MathML renderer, quiz engine (MCQ +
  theory with model answers), exam mode with 3-hour timer, past-paper reader,
  formula index, progress dashboard, search, light/dark, keyboard shortcuts.
- **Financial Accounting: all 16 chapters** — 86 sections, 57 formulas,
  93 authored MCQs, 24 theory questions with model answers.
- **Quantitative Analysis: chapters 1–7** — 28 sections, 51 formulas,
  43 MCQs, 7 theory questions.

## Next, in order
1. **QA chapters 8–20** — hypothesis testing, profit/loss on sales, set theory,
   functional relationships, maths of finance, calculus, OR intro, linear
   programming, EOQ, network analysis, replacement, transportation/assignment,
   simulation. Same house style: formula box, worked example taken to a number,
   focus/errors, quiz.
2. **Public Sector Accounting, chapters 1–20** (`content/ps/`), then
   **Information Technology, chapters 1–6** (`content/it/`).
3. **Expanded exam answers.** `tools/expansions.py` does not exist yet; the
   builder already imports it optionally. Create it with two dicts:
   `NOTES = {"2026-03/FA/mcq/7": "...expansion..."}` for MCQ workings shown in
   quizzes and exam review, and `SECB_NOTES = {"2026-03/FA/1": [blocks]}` for a
   worked expansion rendered above the official Section B solution. Priority:
   FA and QA calculation questions.
4. **Pin the ~100 low-confidence question mappings** in `PIN` in
   `tools/corrections.py`, then re-run `tools/aim.py` and `tools/build_exams.py`.

## Rebuild
```sh
cd website
python3 tools/build_content.py && ./build.sh
python3 -m http.server 8000
```

## Test harness
`/private/tmp/.../scratchpad/test2.mjs` (jsdom). Recreate if the scratchpad is
cleared — it boots `index.html`, stubs the `data/*.js` script injection from
disk, and asserts each view renders.
