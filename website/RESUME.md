# Where the build stopped

## Session 2026-09-14 — 19 more past-paper diets ingested (5 → 24 diets), plus
## per-chapter-quiz and past-paper citation links that scroll to the exact section
- **Chapter-quiz citations now link to source, not just cite it.** `src/quiz.js`
  `chapterQuestions()` was dropping `sec` off authored `quiz.mcq` entries before
  `citeHTML()` ever saw it (theory questions were unaffected — they pass through
  `.slice()` untouched). Fixed the mapping to carry `sec` through. Then added a
  `sec` field to all 100 authored quiz questions across IT ch01–ch06, derived
  from each question's own `src` label (e.g. `"Chapter 3.2.6"` → `sec: "3.2"`,
  matched against that chapter's actual top-level `secs[].n` list — the exact
  values the reader-view anchors on, `id="sec-3-2"`). This reuses machinery
  that already existed for past-question citations (`#/s/CODE/N?sec=X-Y` +
  `scrollToAnchor()` in `app.js`) — it just wasn't wired up for a chapter's own
  quiz. IT was the ask; the same fix is live for any other subject whose
  authored quiz items later gain a `sec` field.
- **19 older INSIGHT past-question PDFs (2014–2023, one per March/September
  diet except March 2016, which the publisher didn't produce) moved from
  `~/Downloads` into `materials/past-questions/`, renamed to match the
  existing `INSIGHT Part II - YYYY-MM Month YYYY.pdf` convention.** Diet count
  5 → 24 (2014-03 through 2026-03). These are the same INSIGHT publication as
  the existing 5, just a different re-upload/watermark ("ATS 2_..._#ifrsiseasy"),
  so the existing extractor mostly worked — but older diets' print layout
  drifted enough from the 2024+ house style to need real fixes, not just a
  DIETS-list update, in `tools/extract_papers.py`:
  - FA's paper title reads "PRINCIPLES [AND/&] PRACTICE OF FINANCIAL
    ACCOUNTING" pre-2022-09 vs bare "FINANCIAL ACCOUNTING" after — subject
    matching switched from `title.startswith(name)` to `name in title`.
  - "MULTIPLE-CHOICE QUESTIONS" / "SHORT-ANSWER QUESTIONS" often wrap onto
    their own line below the "SECTION A: PART I/II ATTEMPT ALL..." banner
    instead of trailing it, and "SECTION B" is often printed with no colon at
    all, and occasionally with no "SECTION A:" prefix at all (bare
    "PART II   SHORT-ANSWER QUESTIONS") — `RE_SECA1/RE_SECA2/RE_SECB` no
    longer require same-line trailing text or a colon.
  - The header introducing the printed MCQ/SAQ answer key is wildly
    inconsistent across 20 years — "MULTIPLE CHOICE QUESTIONS", "MCQ –
    SOLUTION", "SOLUTION TO MULTIPLE CHOICE QUESTIONS (MCQ)", a bare "MCQ" on
    its own line, even the typo "MUTIPLE" (missing the L) in one diet.
    `RE_MCSOL`/`RE_SASOL` now match the word *combination* anywhere on a
    line via `.search()`, not an anchored exact heading.
  - The key itself is sometimes one-per-line with **no punctuation at all**
    ("1   C", with only a single trailing space after 2-digit numbers because
    of fixed-width column alignment) — `parse_key()`'s inline regex needed
    its `[.)]` requirement loosened to `(?:[.)]|\s+)`.
  - Section B solutions are marked "SOLUTION 1", or "SOLUTION TO QUESTION 1",
    or (one diet) "SOLUTION TO QUESTION ONE" (spelled out) — `RE_BSOL` and a
    new `bsol_num()` handle all three.
  - A handful of diets append a "MARKING GUIDE" pass that **re-uses**
    "SOLUTION 1".."SOLUTION 6" a second time for mark breakdowns — sometimes
    as one block at the end, sometimes interleaved after each real solution.
    Detected structurally now (a real run only holds steady or increases; a
    "2A"/"2B" pair repeats a number legitimately, but a *decrease* means a
    second pass has started) rather than by searching for the literal phrase,
    since the phrase's position relative to the real solutions isn't fixed.
  - One diet numbers SAQ questions with lower-case roman numerals
    (i./ii./.../xx.) instead of arabic digits — `parse_numbered()` now tries
    `RE_QNUM_ROMAN` as a fallback.
  - A stray page-number digit occasionally lands on the same line as the next
    question ("4.   2.   Which of the following...", where "4." is a leaked
    page number) — stripped in `pdf_lines()` via `RE_STRAY_NUM` before any
    other parsing runs.
  - **Result: 90 of 96 papers (24 diets × 4 subjects) extract essentially
    perfectly** (30/30 MCQ+key, ~20/20 SAQ+solutions, 6/6 Section B). 6 papers
    have a small, *documented, fail-safe* gap rather than wrong content —
    missing items just don't appear, nothing is ever shown attributed to the
    wrong chapter or with a fabricated answer:
    - `2020-03 PS`: 12/20 SAQ solutions (item 13 in the source is printed
      "13 The Treasurer" — no period at all — and loosening that further would
      risk false question-splits elsewhere in ordinary prose, so left alone).
    - `2021-09 IT`: 0/6 Section B solutions (this paper's Section B has no
      per-question delimiter of any kind after the first — the six answers
      run together labelled only by sub-part, e.g. "ai)", "ii)" — genuinely
      ambiguous without deeper structural guessing).
    - `2022-09 IT`: 2/6 (solutions 3–6 have no "SOLUTION N" header at all,
      jumping straight to "3a." — same ambiguity as above).
    - `2019-03`/`2021-03`/`2021-09 QA`: 2–5 individual MCQs each missing,
      because those questions' options are lettered F–J (continuing from an
      earlier group) instead of A–E, which `RE_OPT` doesn't recognise —
      accepted as a one-off print quirk not worth the false-positive risk of
      widening the option-letter range paper-wide.
    None of the original 5 diets (2024-03 through 2026-03) regressed — same
    counts before and after every fix, verified by re-running after each change.
  - **Chapter/section mapping re-run for all 24 diets**: `python3 tools/aim.py`
    then `python3 tools/aim_sec.py FA PS QA IT` (both already existed, tuned
    for the original 5 diets via `CHAPTER_KEYS` seed vocab in
    `tools/corrections.py` — no `PIN` overrides were needed for the new diets).
    Confidence split: mcq 2337 hi / 522 lo, saq 1538 hi / 382 lo, secb 429 hi /
    133 lo (all `>= 0.12`/`< 0.12` on aim.py's retrieval-margin score).
  - **New: a confidence gate in `tools/build_exams.py`.** Previously `ch` was
    written to `exams.js` unconditionally (only `sec` was gated, inside
    aim_sec.py, before this session) — meaning a low-confidence chapter guess
    could still render a "Chapter N →" link on a past question. Added
    `CH_CONF_MIN = 0.12` (matching aim.py's own hi/lo split) via a `chsec()`
    helper: below that, both `ch` and `sec` are dropped to `None` and no
    citation renders at all, rather than risk sending the reader to the wrong
    chapter. This is the same "silence over a wrong link" principle
    `aim_sec.py` already used for `sec`, now applied to `ch` too.
  - **Fixed several now-stale hardcoded stats** the 5→24 diet jump exposed:
    homepage tally ("5 exam diets" → "24", "600"/"400"/"120" → "2,859"/
    "1,920"/"562"), the "Sit a whole paper" panel, the About page, the exams
    index header (now computed live from the data instead of hardcoded "Five
    diets, twenty papers"), the `<meta description>`, and two lines in
    `README.md`.
  - Rebuild chain used throughout:
    `python3 tools/extract_papers.py && python3 tools/aim.py && python3
    tools/aim_sec.py FA PS QA IT && python3 tools/build_exams.py`, then
    `python3 tools/build_content.py && ./build.sh` for the full site. All
    clean; `node --check` on the assembled `<script>` bundle passes.
  - `jsdom` still isn't installed, so no headless render test this session —
    verified instead via a direct Node `require('./data/exams.js')` smoke
    test (96 papers, 2859 MCQs, 2338 with a chapter link, 1887 with a
    section-level link) and by hand-checking a handful of citations resolve
    to topically-correct sections (e.g. a 2014-03 FA subscriptions-account
    question → FA ch8 §8.6, "The accumulated fund and the statement of
    financial position").

## Session 2026-09-12 (cont.) — PS chapters 17–20 (all four subjects now complete)
- **PS is now complete: 20/20 chapters.** Authored fresh from the re-extracted study-text
  PDF (PS.txt lines 22105–25292), same full-fidelity style as IT ch2–6 this session: every
  definition/list/table plus the study text's complete Section A + Section B end-of-chapter
  question banks with full worked solutions, bolded crammable terms.
  - **ch17 — Accounting for Public Sector Organisations and GBEs**: Enabling Act contents,
    the 5 defining GBE characteristics, the minimum disclosure lists for not-for-profit
    enterprise financial statements, educational institution books of account (cash book,
    personal ledger sub-registers), audit of government enterprises. Section A (10 items)
    + Section B (6 questions: Bolus Electricity Board and Okokomaiko State University
    full statements, accounting-policy essay, bank reconciliation, two net-asset/cash-flow
    calculations) all reproduced with full workings.
  - **ch18 — Financial Management Control System in the Public Sector**: legislative
    control (PAC role/weaknesses, Ghana's Appropriation concept), executive control,
    Ministry of Finance control (virement rules, FGN cash management committees), Treasury/
    OAGF control, departmental controls, the Vote Book (full 15-column format + a worked
    DVEA illustration), Efficiency Unit, Finance & General-Purpose Committee, Audit
    Committee. Section A (10) + Section B (4 questions) with full solutions.
  - **ch19 — Interpretation of Public Sector Financial Statements**: variance analysis
    (IPSAS 24 budget-vs-actual format), liquidity ratios (quick, current — with a 2-company
    worked comparison), solvency ratios (debt, debt-to-equity, debt-to-capital — each
    worked), receivables/payables payment period and inventory turnover period, advantages/
    limitations of ratio analysis. Section A (12) + Section B (4 questions, incl. the
    6-ratio Danduala Local Government computation) with full solutions.
  - **ch20 — Investment/Project Appraisal in the Public Sector**: ARR, Payback Period and
    NPV, each with the study text's full worked illustration (Agbede LG, Omidan LG, Yabus
    LG) plus the combined Omuro LG Section B question comparing all three methods on the
    same three projects. Section A (8) + Section B (1 multi-method question) with full
    solutions.
  - Build clean: `python3 tools/build_content.py ps` → 20/20 chapters, 169 sections,
    49 formulas, 127 MCQ, 28 theory. Full `./build.sh` clean — **FA, PS, QA and IT are now
    all complete (16/16, 20/20, 20/20, 6/6)**.

## Session 2026-09-12 — IT chapters 2–6 (full fidelity transcription)
- **IT is now complete: 6/6 chapters.** Per the explicit instruction "continue with IT,
  chapters 2-6... no information should be lost... thoroughly transcribe it all", each
  chapter was authored as a full, well-formatted transcription of the study text (not the
  lighter QA-style summary pass) — every definition, list, table, worked note and the
  study text's own end-of-chapter question bank (MCQ + short-answer + Section B/self-
  assessment), with full answer keys, bolded crammable terms.
  - **ch02 — Hardware Fundamentals**: input/output devices, CPU (ALU/CU, MIPS/FLOPS,
    RISC), primary/cache memory, external storage (magnetic/optical/solid-state/cloud),
    application controls. 33 MCQs + 24 short-answer + 6 theory Qs from the study text.
    Flagged (not silently fixed) a likely book answer-key inconsistency on ch2 Q2.
  - **ch03 — Computer Software**: system vs application software, OS classifications,
    language processors (assembler/compiler/interpreter), multi-user/tasking/programming/
    processing environments, application packages, all 5 generations of computer
    language, grid computing, MS Windows/Explorer. 29 MCQs + 31 short-answer + 5 theory Qs.
  - **ch04 — Data Processing**: processing techniques/configurations, CPU/OS effects,
    microcomputers in accounting, Information Centre/computer bureau, the full family of
    information systems (MIS/DSS/ESS/TPS/OIS/KMS/ES/KWS) plus Nigerian public-sector
    systems (GIFMIS/IPPIS/UTAS/ATRRS/Open Treasury Portal/Remita/Taxpro-Max), e-commerce
    models, e-government (G2G/G2B/G2C/G2E), e-payment/ATM, digitized middleman, revenue
    models. 27 MCQs (flagged one book gap: Q19 has an answer key entry but no printed
    question stem) + 5 self-assessment Qs.
  - **ch05 — Computer Networks and Data Communication**: LAN/MAN/WAN, all 5 LAN
    topologies, OSI 7-layer model, Internet/DNS/intranet/extranet, transmission media/
    modes/equipment (modem/MUX/FEP/NIC/hub-switch/bridge/router/gateway/repeater), email/
    e-banking/EDI/telecommuting/teleconferencing/social media, cloud computing
    (IaaS/PaaS/SaaS). 17 MCQs + 14 short-answer + 11 self-assessment Qs.
  - **ch06 — Systems Development and Issues in Management of Information** (largest
    chapter): full SDLC (7 stages, feasibility criteria, NPV/IRR/payback/cost-benefit
    ratio, fact-finding methods with interview DO/DON'T table, all 4 changeover
    strategies), SSADM, prototyping/JAD/RAD, outsourcing, computer security/viruses/
    worms/cybercrime (25+ named crimes), Nigeria's Cybercrimes Act 2015/2024 + NDPA 2023,
    workplace health, computer forensics, Big Data (6 Vs), AI/machine learning, IoT
    (3-tier architecture), distributed ledgers/blockchain/cryptocurrency, robotics/BPA,
    drone technology (incl. NCAA rules). 49 MCQs + 11 short-answer + 7 self-assessment +
    all 15 "standard examination type" cross-chapter questions from the end of the book,
    reproduced in full since this is the study text's final chapter.
  - Build clean: `python3 tools/build_content.py it` → 6/6 chapters, 78 sections,
    5 formulas, 63 MCQ, 37 theory. Full `./build.sh` also clean across all subjects.

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
- **QA ch 1 and ch 2** — lighter touch, per request:
  - ch 1 §1.5 "Full revision summary (listed)" — the whole chapter as recall
    lists (data types, collection methods with pros/cons, all sampling methods
    with pros/cons, presentation, and the class limits/boundaries/width/mark
    definitions); §1.6 adds the study text's 10 MCQ/short-answer Q&A.
  - ch 2 §2.5 "Class limits vs class boundaries" — clarifies that L in the
    median/mode/quantile formulas is always the lower *boundary* and c the
    boundary-to-boundary width; explains why continuous classes (0–10, 10–20)
    make limit = boundary while gapped classes (1–10, 11–20) do not; flags that
    the study text's **Example 2.18 uses L = 8.5 where the true lower boundary
    is 7.5**, making its Mode (9.5) and Median (10) each exactly 1.0 too high —
    Example 2.19 does it correctly. §2.6 adds an easy-to-miss checklist and the
    study text's end-of-chapter Q&A.
- Build clean: `python3 tools/build_content.py && ./build.sh`. Headless test
  (`tools/test.mjs`) needs `npm install jsdom` — not run this session.
- **PS ch 8–12 NOT done** — a "next 5" request was interrupted mid-research to
  pivot to QA. Source Q&A already located: PS.txt Section A/B blocks at ch8 ~10411,
  ch9 illust 11601 + Section A 12374, ch10 14069, ch11 15645, ch12 16548.
- **QA all 20 chapters — "worksheet summary" pass.** Added a final section to
  every QA chapter (ch1 §1.5 revision list; ch2 §2.6 easy-to-miss; ch3–20
  §X.last "Worksheet summary — every term defined and every formula"). Each has
  a full definitions list and every formula spelled out, including the
  intermediate ones (regression normal equations before b and a; Σ-column sets;
  AP/GP n-th terms; MODI duals; PERT variances; etc.). Enumerable "types of X"
  are listed as name + formula only. Probability (ch7) and every OR chapter
  define all terms. Top-level `formulas` lists expanded from 137 → 223 entries
  for the formula index. Build clean.
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
