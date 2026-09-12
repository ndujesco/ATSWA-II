# Where the build stopped

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
