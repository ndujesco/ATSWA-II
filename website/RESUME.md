# Where the build stopped

## Session 2026-09-06 — fidelity pass on FA + IT ch1
- **FA ch 9, 10, 11 expanded** to carry the study text's own material, not just
  the house-style rewrite. Added, without removing anything:
  - ch9 §§9.7–9.10: study-text Illustrations 9.1–9.9 verbatim (questions) with
    rebuilt solutions, plus all 10 end-of-chapter MCQ/short-answers and the 3
    examination-type questions with worked ledger accounts. OCR garbles in the
    printed solutions are flagged inline.
  - ch10 §10.6: Illustrations 10.1–10.3 (distribution of income, adjustments
    before appropriation, revaluation on admission). The study text has no
    end-of-chapter question bank for ch10.
  - ch11 §§11.7–11.8: Illustrations 11.1–11.7 (goodwill in/out, revaluation,
    retirement, amalgamation, dissolution + Garner v Murray, conversion to a
    company) and the MCQ/short-answer set with the tutorial workings.
- **IT ch1 authored** (`content/it/ch01.py` + `content/it/meta.py`): 11 sections
  covering system theory, control systems, data vs information, information
  systems/AIS, IT, decision types, data representation with all number-base
  worked examples, database elements, data acquisition/cleansing/analysis, and
  computer evolution/types. All 33 study-text MCQs, 16 short-answers and 11
  Section B theory questions with the answer key.
- **PS ch 1–7** given the same treatment — a new "End-of-chapter questions
  (study text)" section per chapter (§1.10, §2.14, §3.7, §4.22, §5.11, §6.13,
  §7.13) carrying the study text's Section A (10 Q) + Section B (theory)
  end-of-chapter questions with the answer key, crammable answers **bolded**;
  3–4 Section A MCQs folded into each chapter quiz. Also: PS ch 5 §5.11 adds
  Illustration 5-1 (payroll accounting entries). Printed answer keys in ch 2, 3
  and 6 are misnumbered in the scan — realigned inline. The existing PS section
  prose was already faithful and bolded; only the question banks were missing.
  PS ch 8–16 and 17–20 still untouched.
- Build clean: `python3 tools/build_content.py && ./build.sh`. Headless test
  (`tools/test.mjs`) needs `npm install jsdom` — not run this session.
- **Still a rewrite, not a transcription, for FA ch 1–8** (esp. 1, 2, 7, 8) and
  everything in PS/QA: house-style prose + authored quizzes; the study texts'
  own illustrations and end-of-chapter question banks are not carried over.
  ch 3–6 do reproduce the numbered illustrations.

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
