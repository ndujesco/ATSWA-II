# Where the build stopped

## Session 2026-09-20 (cont. again) — guides are now one click from the home
## page, not just linked from inside a chapter
User: "Like can't I from home page?" — the three guides were only reachable
by navigating into a specific chapter section first. Added a data-driven
`GUIDES` array to `subjects.js` (same pattern as `SUBJECTS` — add an entry,
it shows up automatically) and a "Study guides" section to `VIEWS.home()`
in `app.js`, reusing the existing `.subcard`/`.subs` grid styling so it
looks like a natural extension of the subject cards above it rather than a
bolted-on block. Added one new CSS rule (`.ghead`) for the section's own
heading, since nothing existing fit a plain mid-page `h2`. New regression
test confirms all three guide hrefs appear on the home page. 22/22 passing.

## Session 2026-09-20 (cont.) — three standalone study-guide pages added under
## website/guides/, discoverable from inside the app, not just as artifacts
User asked for a detailed CRF summary "as a doc"; got a Claude.ai artifact
first, then said sharing wasn't working and asked to "just give me as a page
on this app" — so the pattern for the rest of this session became: build a
real static HTML page under `website/guides/`, styled to match the site's
own light/dark tokens, with a "note" block linking to it from the relevant
chapter (render.js already supports `[label](url)` with any relative path,
not just `#/` routes, so no app-code changes were needed to wire this in).

- **`guides/crf.html`** — Consolidated Revenue Fund: all 11 sources of CRF
  income, the 3 categories of charge against it (recurrent expenditure,
  statutory first-charge officers, pensions/gratuities), the full warrant
  system (PGW/AGW/SGW/REW/Virement/Contingencies), the Development and
  Contingency Funds, a worked month-in-the-life illustration, and — after
  the user pushed back twice on a half-remembered "fund types" detail —
  **Ghana's entire parallel fund system**, which turned up a genuine
  confirmed confusion pair worth adding to the actual site content, not
  just the guide: Ghana's **Contingency Fund** (constitutional, Parliament-
  controlled, refilled by supplementary estimate) vs **Contingency
  *Reserve* Fund** (a slice of the Executive's own already-approved budget,
  no Parliament involvement) — two different funds whose names differ by
  one inserted word. Added a `warn` block distinguishing them to PS ch9
  §9.9 itself, plus the 3 Ghanaian "public funds" examples (Business
  Assistance Fund, HIPC Fund, Social Investment Fund) that were missing
  from the site's own prose list. ~45 past questions on the whole fund
  topic, organised into 7 groups (which section establishes which fund,
  sources, charges, Contingency Fund, Development Fund, FAAC mechanics,
  fund administration).
- **`guides/ipsas.html`** — every IPSAS number the course actually cites
  (21 standards + the unnumbered Cash Basis IPSAS), pulled from every PS
  chapter via `grep -rhoE "IPSAS[[:space:]]+[0-9]+"`, each with its real
  IFAC/IPSASB title, what it covers, and a link to the exact chapter/
  section. Flags both supersessions (17→45 PP&E, 25→39 Employee Benefits)
  and the study text's own "IPSAS 49" (Retirement Benefit Plans) — IPSASB
  has never issued a standard with that number; the content itself mirrors
  IAS 26, already flagged as a probable source error in ch5 §5.8 earlier
  this session. Grouped a second way, by theme, for "which IPSAS deals
  with X" questions. Nigeria's own two-step adoption timeline (cash basis
  2014, accrual basis 2016) is the one date that's actually examined, not
  each standard's own IPSASB issue year, and is what's foregrounded.
- **`guides/statements.html`** — every required statement, cash basis
  (ch14) and accrual basis (ch16) side by side, each with what it reports,
  the worked-example checkpoints (e.g. the CRF/Assets-and-Liabilities
  articulation check, the accrual surplus vs cash-flow reconciliation),
  and IPSAS 3's policy/estimate/error distinction. Found and flagged a
  **genuine unresolved inconsistency in the past papers themselves**: two
  diets (2016-09, 2024-03) answer "Modified Cash Basis" for "revenue on
  cash, expenditure on accrual", but a separate diet's own MCQ (2020-03
  Q27) defines "Modified Accrual Basis" as that exact combination, and
  2020-09's key agrees with 2020-03 — 2 sources against 1. Presented the
  majority position as the default and said so explicitly, rather than
  picking one silently or refusing to answer.

Rebuilt the full pipeline after each content change (`build_content.py` →
`aim.py` → `aim_sec.py FA PS QA IT` → `build_exams.py` →
`final_revision.py` → `build.sh`) and re-ran `tools/test.mjs` — 21/21
still passing throughout.

## Session 2026-09-20 — QA's earlier "worksheet summary" pass was not a real
## fidelity pass; ch7 (Probability) done properly as the pilot, 18 more
## chapters likely need the same treatment
User: the QA chapters (ch7/Probability given as the example) are "not '
remotely thorough" — asked for every definition, schools of thought, term
and outcome, sourced from the QA study text PDF directly, with question
links fixed/added where the underlying content was missing.

**Confirmed the complaint is structurally real, not a citation-only issue.**
Checked which QA chapters actually have an "End-of-chapter questions (study
text)" section (the full fidelity-pass treatment every FA/PS/IT chapter
got): only **ch01 and ch02 of QA's 20 chapters** have it. The
"Section-by-section checklist" + "Worksheet summary" pass done earlier this
week for all 20 QA chapters was real but was always a *narrower*, formula-
and-definition-reference pass — it never went back to the source PDF for
each chapter's own expository prose, "schools of thought"-style discussion,
or its own worked Illustrations/end-of-chapter Q&A, the way the FA/PS/IT
full fidelity pass did.

**Did ch7 (Probability) as the concrete pilot, re-extracted straight from
the study-text PDF (`pdftotext -layout`, lines 6418–7190 of the raw
extract):**
- **§7.1** renamed "Introduction and basic terms" and given the book's own
  actual introduction (uses of probability: quantitative-analysis tool,
  basis of statistical inference, role in insurance/quality control) plus
  — the specific thing the user named — the **two schools of thought** on
  estimating a probability (classical/*a priori*: equally-likely outcomes
  counted *before* a trial; frequency/*a posteriori*: observed rate *after*
  many trials), the book's own explicit remark on *why* a third,
  **axiomatic** approach was developed (both schools rely on the vague,
  relative terms "equally likely" and "very large"), and a table of
  standard compound sample spaces (coin+die = 12 points, two dice = 36)
  the book works through but the site never had.
- **§7.2** gained the book's own independent/dependent-event examples table
  (Head-then-Tail; passing QA & Economics vs weather/mineral sales, drug/
  recovery) and a new worked illustration (Example 7.10, with vs without
  replacement side-by-side on the same numbers — directly demonstrates why
  replacement changes independence, which the site only asserted before).
- **§7.4** gained an explicit "Properties of expectation" list (was only in
  the worksheet-summary formula box, not the body prose) plus three new
  worked illustrations the site never had: $E(X)$/$E(X^2)$/SD from a full
  distribution table, the fair-price-of-a-lottery-ticket calculation (ties
  directly to the existing "fair game" note, which had no worked example),
  and expected value of the sum of two dice both directly and via the
  $E(X+Y)=E(X)+E(Y)$ shortcut.
- **New §7.6** "End-of-chapter questions (study text)" — the book's own
  10-item MCQ/short-answer bank with official answers (verified every
  arithmetic answer independently before transcribing), matching the
  pattern ch01/ch02 already had and every other chapter lacks.
- 2 new quiz MCQs added testing the schools-of-thought content directly.
  Worksheet-summary checklist updated for §7.1's new scope and the new §7.6.
- Section numbers were **not** rearranged (new material folded into the
  existing 7.1/7.2/7.4, new content appended as 7.6) specifically so no
  existing quiz or past-paper `sec` citation needed touching.

**Real citation improvements fell out of this immediately** — re-ran the
pipeline and two previously mis-linked/unlinked real past questions now
correctly resolve to §7.1: "Probability theory is mainly concerned with
chance and calculated risks in the face of [uncertainty]" (was §7.2, now
§7.1, matching the newly-added intro sentence verbatim) and the coin-and-
die compound-sample-space question (was chapter-only, now §7.1). This is
the same lesson as the PS pass a few days ago: **retrieval mislinks are
very often actually content gaps** — the citation couldn't find the right
section because the right section didn't have that content yet.

Rebuilt the full pipeline (`build_content.py` → `aim.py` → `aim_sec.py FA
PS QA IT` → `build_exams.py` → `final_revision.py` → `build.sh`) and re-ran
`tools/test.mjs` — 21/21 still passing.

**Not done, and worth a direct decision**: the same gap almost certainly
exists in QA chapters 3–20 (18 more chapters) — each would need the same
treatment (re-read its own slice of the study-text PDF in full, compare
against current site content, add missing schools-of-thought/definitions/
illustrations/end-of-chapter Q&A, fix citations that turn out to be content
gaps in disguise). This is a large, multi-hour undertaking done chapter by
chapter the way ch7 was — flagged to the user rather than started
unprompted.

## Session 2026-09-19 (cont. again) — finished wiring up "Final Revision"
User pointed out a much earlier request ("give me the questions all of them
grouped by course and section and priority") had never actually shipped —
`tools/final_revision.py` (clustering script) and `data/revision.js` existed
from earlier the same day, but no UI ever consumed them; the feature was
invisible. Built the missing half:
- **New `src/revision.js`**: `VIEWS.revision` (subject picker, mirrors the
  homepage), `VIEWS.revisionSub` (MCQ / Short answer / Essay picker per
  subject), `VIEWS.revisionList` (the full, frequency-ranked list for one
  subject+type — MCQ shows options with the correct one inline, SAQ shows
  the official answer inline, Essay uses the existing reveal-button pattern
  from the past-paper viewer). Each item carries an "ASKED N×" badge and,
  where confident, the same chapter/section citation link used everywhere
  else on the site.
- **Routing**: `#/revision`, `#/revision/<CODE>`, `#/revision/<CODE>/<kind>`
  added to `app.js`'s `render()`; a "Final Revision" tab added to the nav.
- **Build**: `revision.js` added to `build.sh`'s concatenation (placed
  before `exams.js`, whose `boot()` call needs every `VIEWS.*` already
  registered).
- **Regression suite**: installed `jsdom` (`npm install jsdom --no-save` —
  new `website/.gitignore` added so `node_modules/` is never swept into a
  commit) and ran `tools/test.mjs`, which had gone stale in two ways
  unrelated to this feature — fixed both rather than leaving them broken:
  a "PS and IT degrade gracefully while unwritten" test asserting no
  literal "undefined" substring, written before either subject was fully
  authored, now false-positives on PS ch1's own prose ("...are not left
  completely **undefined** until then") — replaced with real chapter-count
  assertions (23 for PS, 6 for IT) plus one test asserting that exact
  sentence renders, to make the "this is not a bug" reasoning explicit
  in the suite itself, not just in a commit message. Added 4 new tests for
  the revision feature itself (subject picker, type picker, MCQ-list
  most-asked-first ordering via a `& times;` frequency-badge regex, and a
  smoke test that every subject's SAQ/essay lists render). **21/21 passing**
  — the strongest verification this session has had for any UI change,
  actual jsdom-rendered assertions rather than sampling or reasoning about
  code.

Rebuilt (`./build.sh`) clean; `index.html` now 139,124 bytes (was 131,190).

## Session 2026-09-19 (cont.) — user said "do all": extended the answer-text
## audit to SAQ, fixed 11 more confirmed PS mislinks, added a targeted
## abbreviations sweep (exam-tested acronyms, not every acronym in the text)
Continuation of the same day's audit work. User: "do all" (both remaining
threads — keep hunting mislinks, and the full abbreviations-per-chapter ask).

**Extended `tools/audit_answers.py` to SAQ, not just MCQ.** Found and fixed
one more bug in the tool itself first: the "drop the trailing word" fallback
match (added for phrases like "the President and not less than two members")
produced near-worthless fragments for short answers — "Finance or
compliance" → "finance or", "Standing and Special" → "standing and",
"Direct and Indirect" → "direct and" — single real words that match almost
any chapter, producing false mislinks. Fixed by only allowing the fallback
when the trimmed phrase still has ≥2 words that are neither stopwords nor
short (>3 chars) — re-running dropped several previously-reported "mislinks"
that were this bug, not real problems.

**11 more confirmed real mislinks**, `PIN`ned the same way:
Public-Private Partnership (was ch1 → ch21 §21.2, new `def` block added
since the site only had it as one table-row aside — the source PDF itself
has *no* PPP content at all, but the site's own emerging-issues table
already used the term, and the exam tests it directly with a real answer
key, so this is filling in the site's own existing partial coverage, not
inventing new material), Modified Cash Basis (ch14→ch1), Personal Emolument
Record Card (ch11→ch8 §8.7), Rolling Plan ×2 more diets (ch23→ch6),
Appropriation-in-Aid ×2 (untagged/ch14→ch18 §18.5 — new `def` block; also
genuinely absent from the source PDF, added as standard, uncontroversial
Commonwealth public-finance terminology since the exam's own answer key uses
it confidently), Public Finance Committee (ch12→ch18), Subventions
recurrent/capital (ch6→ch17), Defined Benefit Pension Plan (ch4→ch5 — ch4 is
PRA 2014, which is *only* a defined-contribution scheme; "defined benefit"
as a general IPSAS concept belongs in ch5), GIFMIS (ch=null→ch3 §3.5 — also
legitimately covered in ch21, but ch3 already had its own matching "GIFMIS
stands for" quiz item), IFAC (ch=null→ch1 §1.7).

**Also found `PIN` was only wired for MCQ in `aim.py`** (never checked for
SAQ/secb) — extended it to all three types; every SAQ pin above needed this.

**Abbreviations sweep** — new `tools/audit_abbrevs.py`, which flags any
ALL-CAPS 2-6 letter token used in a chapter's own text with no "(ABBR)"
spelled out anywhere in that chapter (cross-referencing `def`-block titles
too, so `{'def': {'t': 'GIFMIS', ...}}` counts as defining GIFMIS even
without literal parentheses). First pass was very noisy — roman numerals,
"NOT"/"EXCEPT" from quiz stems, table-header words like "ASSETS"/"CASH" in
caps, "TV"/"UV" abbreviating nothing — filtered with a broader allow-list.
Even cleaned up, ~90 flagged tokens across 23 chapters is too many to
individually chase (most are ordinary entity-name abbreviations used once
in an illustrative list — NNPC, FIRS, EFCC in a table of examples — which
don't need chapter-local redefinition any more than "IPSAS" does). Instead
cross-referenced the flagged list against every past-exam-question STEM
that actually *names* one of these abbreviations — only 10 do (EFCC, FAAC,
GIFMIS, ICPC, ICT, IPPIS, ISA, NCOA, TF, TSA) — then checked each **site-
wide** (not just its flagged chapter) for a real "(ABBR)" definition.
8 of 10 were already fine (defined once in a canonical home chapter and
correctly referenced elsewhere without redefinition, same pattern as
IPSAS — not a gap). Two real ones fixed: **ISA** (International Standards
on Auditing) was used constantly in ch23 ("ISA 260", "ISA 265"...) but
never once spelled out — added a one-line `note`; **ICT** and **TF**
checked and found already adequately clear in context ("Treasury Form 209"
spelled out on first use, before the "TF 1" shorthand right after).
**The remaining ~80 flagged, never-exam-tested abbreviations were
deliberately left alone** — fixing every acronym that appears once in a
table row, with no evidence any exam question has ever asked about it,
is not a good use of scrupulousness; it would be polish with no verification
signal behind it.

Rebuilt clean throughout. PS: 155 authored MCQs (was 145 at the start of
today), 230 sections, all four subjects' `data/*.js` and `index.html`
regenerated with no errors.

## Session 2026-09-19 — a precision, answer-text-based audit tool
## (`tools/audit_answers.py`), one real content gap fixed properly, four
## more confirmed mislinks pinned, one abbreviations glossary added
User remained unsatisfied after the previous pass's pipeline fixes and gave
a concrete new failure: "A discretional financial assistance to finance a
particular project is known as" (2019-09 Q26, answer "Specific grant") —
tagged to PS ch2 §2.8, and the concept wasn't clearly present there at all.

**New tool: `tools/audit_answers.py`.** Rather than continuing to spot-check
one question at a time, built a precision audit that searches for the
*correct answer's own text* across every PS chapter — far more decisive than
stem-based TF-IDF, since an MCQ answer is usually a short, quotable term. Had
to iterate the methodology twice before it was trustworthy:
- v1 stripped stopwords from the answer phrase but not from chapter text, so
  "Minister of Finance" never matched "minister of finance" (no "of" in the
  search phrase) — produced ~400 false "gaps" on content that plainly exists.
- v2 fixed that, but still flagged full descriptive-sentence answers (a
  distractor option's own prose, or the exam-writer's paraphrase of a
  concept) as "gaps" even when the underlying concept is well covered in
  ordinary prose — narrowed to short (2-6 word) answers only.
- Even then, "Which... is NOT/EXCEPT/CANNOT..." questions were a guaranteed
  false-positive generator, since their correct answer is, **by
  construction**, the one option that is *not* really in the source —
  excluded them (and their OCR-concatenated forms, "NOTa", "CANNOTbe", where
  a missing space defeated a plain regex).
- The result (81 "gaps" + 9 "mislinks" out of ~700 short-answer MCQs, from
  an original ~2860) was finally high-precision enough to hand-check. Most
  of the remaining "gaps" turned out to be a **third** false-positive
  category — the content exists, worded slightly differently ("a President"
  vs "the President", "personnel and payroll" vs "personnel payroll",
  "debt-to-assets" vs "debts to total assets") — confirmed by checking
  several by hand (Board of Survey composition, ZBB, IPPIS expansion, RSA
  access age, PPT as a Federation Account source, the debt/assets ratio)
  against the actual chapter text, all of which are genuinely already there.
- What survived hand-verification: **one real content gap** (below), plus
  **four more confirmed mislinks**, `PIN`ned the same way as the previous
  pass's: "Rolling Plan" (was ch5 Employee Benefits → ch6 Budgeting),
  "IPSAS 5/Borrowing Costs" (was ch20 Investment Appraisal → ch15, where the
  3-year-exemption list actually mentions it), "Sub-Self Accounting unit"
  (was ch7 → ch13 §13.10, which has the actual self-/sub-self-/non-self-
  accounting unit definitions), and the grants question below.

**The one real content gap, fixed properly**: "Specific grant" vs "general
grant" existed on the site only inside a table cell in ch9 §9.9 — the
*Ghana* comparative section — with no standalone definition, and the study
text's own wording of the two definitions is internally contradictory (says
a "specific grant" is "**not** for any particular purpose", then gives an
example of one tied to a named project). Added a proper `def`-block pair to
**ch12 §12.9** (Nigeria's own grants-in-aid section — the right home for a
non-Ghana-specific question) with the source's contradiction flagged via a
`note` and resolved in favour of the examples/answer-key reading (specific =
tied to one named project; general = untied "budget support"), plus a new
quiz MCQ citing it. `PIN`ned the exam question to ch12 §12.9.

**Also handled**: the user separately asked for a Pension Reform Act 2014
abbreviations SAQ (CPS/PTAD/PFA/PFC/RLA/PW) and said "I need all
abbreviations for each chapter." Found the exam's own answer key (CPS =
Contributory Pension Scheme, PTAD = Pension Transitional Arrangement
Directorate, PFA = Pension Fund Administrator, PFC = Pension Fund Custodian,
RLA = Retiree Life Annuity, PW = Programmed Withdrawal) and checked each
against ch4: PTAD/PFA/PFC already had their own titled sections; CPS, RLA
and PW were only ever spelled out in full, never introduced as the
abbreviation itself. Added a full "Abbreviations used in this chapter"
table to ch4 §4.1 and named RLA/PW explicitly at their point of use in §4.6.
**A full 23-chapter (or all-four-subject) abbreviations audit was NOT done**
— this pass only closed ch4's specific gap; flagged to the user as a
separate, larger undertaking if wanted.

**Being honest about scope**: this pass did not re-verify all ~700 PS MCQs,
only the ~90 that survived the audit tool's (now three-times-refined)
filters as plausible real problems, of which 5 were genuinely real (4
mislinks + 1 content gap) and the rest were the tool's own false positives
on already-correct content. The previous pass's four systemic pipeline bugs
plus this pass's precision audit together represent a much more thorough
check than simple stem-based sampling, but "every single PS question
individually verified against the PDF" has still not literally happened and
is not a realistic hand-verification task at this corpus size.

Rebuilt clean throughout (`build_content.py` → `aim.py` → `aim_sec.py FA PS
QA IT` → `build_exams.py` → `build.sh`).

## Session 2026-09-18 (cont. again) — why PSA question→chapter/section
## citations were "really bad": four real bugs, not one, found and fixed
User reported the PS past-question chapter/section grouping was bad and asked
for a scrupulous, question-by-question check against the source PDF, with
permission to rewrite chapters for anything genuinely missing. Root-caused
four independent, compounding bugs rather than one:

1. **`tools/aim.py`'s chapter-level matcher was scored against raw PDF text**,
   not our own authored chapters — a full `pdftotext` dump of everything
   between one "CHAPTER N" heading and the next, worked examples, OCR noise,
   tables and all, counted as plain word frequency. A question mentioning
   "grants" several times could out-score the chapter that actually explains
   grants-in-aid, because some *other* chapter's worked example happened to
   repeat "grants" in a numbers table more often. **Fixed**: `chapter_text()`
   now builds each chapter's reference corpus from `content/<code>/ch*.py` —
   title, brief, outcomes, every section's own text, focus and errors — the
   same source `aim_sec.py`'s (better-performing) section-level pass already
   used. The two passes are now consistent, and any content fix improves
   retrieval immediately with no separate re-extraction step.
2. **MCQ wrong-answer options were weighted equally with the stem.** A stores/
   inventory question whose five options were all officer titles (Auditor-
   General, Minister, Accountant-General, Permanent Secretary, Chief Store
   Officer) got dragged toward the "officers and their responsibilities"
   chapter, because those titles are that chapter's own dense seed vocabulary
   — regardless of what the *stem* was actually asking about. **Fixed**: the
   stem (+ any shared preamble) is now weighted 3x over the options in the
   query representation for both `aim.py` (chapter) and, analogously, the
   secb pass now also weights the question's own scenario text 3x over the
   solution's numeric working (previously secb classification used *only*
   the solution, never the actual question text).
3. **A stale-data bug in `aim_sec.py`**: a question left unplaced on a re-run
   (margin too thin under its chapter tag *this* run) kept whatever `sec` it
   had been given under a *previous* run's different chapter tag, since the
   code only ever wrote `sec` on success and never cleared it on failure.
   Confirmed live in `data/papers.json` before the fix: **243 of 4259
   sec-tagged questions across all four subjects** had `sec`'s own chapter
   prefix not matching `ch` — pointing at a different chapter's section
   entirely. **Fixed**: `aim_sec.py` now explicitly clears every question's
   `sec`/`secConf` to `None` at the start of each run, before recomputing —
   243 mismatches confirmed down to 0.
4. **A real extraction bug in `tools/extract_papers.py`**, and the biggest
   single contributor: a shared preamble ("Use the following information to
   answer questions 9 to 12") was being attached to every question **from
   then on**, not just the 4 it named — because the code that carries `pre`
   forward across a group of questions never had a mechanism to *stop*
   carrying it once that group's range was exhausted. A Public Procurement
   sanctions question (Q22) was found with an entirely unrelated pensions
   scenario (Q9-12's "Gabriel Matiluko... Retirement Savings Account...")
   stuck in its `pre`, and — weighted into the query — that scenario's words
   dominated the real content words enough to misfile it under Pensions with
   real confidence. **Fixed**: added `pre_range_end()`, which reads the
   preamble's own first line for every integer following the word
   "question(s)" (robust to "9 to 12", "9 & 10", "13" alone, "4, 5 and 6",
   "16 – 19" — every phrasing found across all 96 papers) and clears `pre`
   once the running question number moves past that range. Applied to both
   `parse_mcq` (which previously carried forever) and `parse_numbered` (which
   previously *under*-attached — clearing `pre` after the very first question
   in the range, leaving the rest of the range with no shared data at all).
   One rare case (the range stated on a line *after* the first) falls back to
   the old unbounded behaviour rather than being over-engineered further.

Re-ran the full pipeline (`extract_papers.py` → `aim.py` → `aim_sec.py FA PS
QA IT` → `build_exams.py` → `build_content.py` → `build.sh`) and hand-verified
~95 PS MCQs against actual chapter content across two independent samples
post-fix — the large majority now correct, including several that now
correctly hit content added earlier this session (Board of Survey, the new
Procurement §10.6, NCPP objectives) and the very question that motivated the
original ch10 rewrite ("Which Tender Board can approve contracts whose values
exceed ₦50,000,000?" now correctly cites ch10 §10.6). Also spot-checked FA/
QA/IT post-fix (the `aim.py` rewrite touches all four subjects) — no
regressions found.

Two more confirmed content gaps found and closed in PS ch11 while auditing
(same "check the PDF, add if genuinely missing" rule as the earlier pass):
**§11.5** now states the Board of Survey's actual composition (a President —
Grade Level 08+ — and not less than two members, Grade Level 06+, convened by
the Accountant-General) alongside its already-covered duties; **§11.6** now
covers the **Conversion Voucher** (evidences stores issued within the same
store for manufacture/conversion) and the rule that **government property
must not be sold except with the Minister of Finance's specific authority**.

One remaining seed-vocabulary gap closed generally rather than one-off:
ch10's `CHAPTER_KEYS` predated this session's big §10.6 addition (Tenders'
Boards, contract register, retention fee, etc.) and so under-weighted it;
added those terms as seeds, which correctly pulled a "contents of a contract
register" question from the Vouchers chapter to Procurement §10.6 without
needing a manual per-question override. Two individual per-question `PIN`
overrides were added for a recurring "Financial Reporting Council Chairman
tenure" question that a bag-of-words matcher will likely always misfile
toward whichever chapter has the *most* boards-with-chairmen-and-tenure
content (ch10's Tenders' Boards) rather than the actually-correct ch1 §1.7 —
this class of confusion (generic board-composition/tenure wording shared
across many unrelated statutory bodies: FRC, ICPC, PENCOM, NCPP, Tenders
Boards, CCB/CCT, PCC) is a genuine hard case for word-overlap retrieval and
is the kind of thing `PIN` exists for, rather than a further seed-tuning
target.

**What this doesn't claim**: "check each and every" of ~1,300+ PS past
questions individually against the PDF was not literally done — that isn't
finishable by hand in any reasonable time. What was done is root-causing and
fixing four systemic bugs that were miscategorizing a meaningful fraction of
*all* questions (not just PS's), verified by hand-checking two substantial,
independent, stratified samples (~95 PS MCQs total) plus a smaller cross-
subject sample, both before and after each fix. A long tail of individually
hard, ambiguous cases will remain — a bag-of-words system cannot perfectly
disambiguate two chapters that both legitimately discuss "Chairman",
"tenure" or "grants" — but the failure mode changed from "confidently pointing
at the wrong chapter" (the reported symptom) to "occasionally too unsure to
show a citation at all," which is the app's existing, deliberate fail-safe.

**Also noted, not part of this fix**: the repo's git history contains several
commits (spanning 2026-09-14 to 2026-09-18, e.g. "finalize PSA", "update",
"Add final_revision.py...") that were not made via an explicit `git commit`
in any session transcript available to this assistant — they read as
periodic automatic checkpoints of in-progress work, authored under the
user's own git identity. Flagged for the user's awareness; not investigated
further or acted on (no destructive git action was taken).

## Session 2026-09-18 (cont.) — PSA answer-in-source-material audit: PS ch10
## (Public Procurement) was missing most of its Tenders'-Board/threshold
## content; three smaller confirmed gaps closed in ch11/ch15
User asked: "if there is any question that the answer is not in the study
material (for PSA) search the main source (PDF) and if it is found there
modify the chapter accordingly to include it" (permission given mid-task to
rearrange/renumber sections if needed).
- **Method**: pulled every PS past-question (`data/exams.js`) with no
  confident chapter match — 183/716 MCQ, 139 SAQ, 34 SecB — as the candidate
  pool, then triaged each stem by topic recognition, checked it against the
  actual chapter body (many "unmatched" turned out to be **retrieval false
  positives**: content already exists, e.g. ch07's Auditor-General section
  fully covers appointment/90-day-reporting; ch01's FRCN section fully covers
  the 4-year tenure/vacancy conditions; ch04/ch05 fully cover PENCOM,
  restricted pension investments and "statement of changes in net assets
  available for benefits"; ch06/ch16/ch19 fully cover IPSAS 24), then grepped
  the re-extracted source PDF text for anything that still looked missing.
  **Per the user's explicit constraint, anything not actually in the source
  PDF was left alone, not fabricated** — confirmed absent: IPSAS 31 detail,
  IPSAS 11, IPSAS 15, computer/EDP audit, debt relief, Advance Payment
  Voucher, Accountant-General's Office internal departments, Bureau of
  Public Enterprises/commercialisation, PPA "scope of application" (s.15),
  ICPC-remuneration mechanism, PenCom Chairman/DG's own tenure clause,
  "movement of accounting staff between MDAs" approval authority, and the
  specific "retirement benefits with immediate effect" condition-list.
- **Largest confirmed real gap — PS ch10, Public Procurement**: the source
  (§10.1, §10.5.1–10.5.3, §10.3–10.4 of the book) has a great deal that our
  chapter never carried:
  - §10.1: NCPP's **six specific named part-time member bodies** (Nigeria
    Institute of Purchasing and Supply Management, Nigerian Bar Association,
    NACCIMA, Nigerian Society of Engineers, civil society, the media) —
    previously only a generic "professional and private sector bodies" line —
    and the Bureau's fuller objectives + ~15-item functions list, replacing a
    one-line description.
  - §10.4: replaced the old generic 3-row threshold table and its "don't
    memorize figures" warn-box with the actual **2025-circular thresholds**
    (Circular Ref. 59780/S.2/B/532): a 5-tier approving-authority table and a
    procurement-method table, both split by Goods/Works/Non-consultant/
    Consultancy; NNPC's own USD-denominated thresholds; three processing-
    timeline tables (NCB 91 days, ICB 107 days, Consultancy 128 days); FEC's
    specific current limits. The old "figures are revised, don't memorise
    them" framing is now a `warn` about the **structure surviving revision**,
    since the source itself commits to concrete, examinable numbers.
  - New **§10.6** ("Tenders' Boards and contract administration"), inserted
    before the existing Q&A section (renumbered §10.6→§10.7 — safe, since
    nothing cited `sec: '10.6'`): Construction Contract definition; history
    (2001 abrogation of the old Departmental/Federal Tenders Boards) and the
    ₦5m no-open-tendering threshold; the three Tenders' Board types and their
    exact compositions (Ministerial, Armed Forces/MoD, Nigeria Police);
    full tender-board operating procedure (notice, deposit, sealed-envelope
    tender procedure, selection, award); audit inspection (7-year record
    retention); contract terms (Contingencies Clause; 5%-for-6-months
    Retention Fee); contract payment voucher contents/attachments; the
    Contract Register's 9 fields plus the Project Register.
  - This directly answers real, previously-unanswerable past questions, e.g.
    "Which Tender Board can approve contracts whose values exceed
    ₦50,000,000?" — added 2 new quiz MCQs citing §10.6, 145→151 PS MCQs.
- **Three smaller confirmed gaps, also fixed**: PS ch15 §15.2 never spelled
  out that **PSE = Public Sector Entity** (IPSAS 33's own acronym, used
  throughout the chapter but never defined) — added a `def` + quiz item;
  ch11 §11.5 never gave the Board of Survey's **composition** (President +
  ≥2 members, Grade Level 08/06 minimums) even though duties were covered —
  added, with 2 quiz items (who convenes it — the Accountant-General — and
  its composition); ch11 §11.6 never mentioned the **Conversion Voucher**
  (evidences stores issued *within the same store* for manufacture) among
  the storekeeper's vouchers — added a small table + 1 quiz item.
- Rebuilt clean throughout: `python3 tools/build_content.py ps` after each
  edit, then `python3 tools/build_content.py` (all 4 subjects) →
  `tools/aim.py` (PS ch10's matched-question count rose to 21) →
  `tools/aim_sec.py FA PS QA IT` → `tools/build_exams.py` → `./build.sh`. PS
  is now 230 sections / 49 formulas / 151 MCQ / 31 theory, all clean.
  (Numeric-heavy exam stems like the ₦50,000,000 one may still fall below
  the TF-IDF confidence threshold that gates automatic citation — a known,
  pre-existing pipeline limitation, not a content gap; the content itself
  now exists on the site either way.)
- Triage was not fully exhaustive on the SecB pool (34 essay questions) —
  spot-checked roughly two-thirds against source/site and found no further
  gaps beyond the three above, but a handful of broad essay stems (Local
  Government Treasurer functions, TIMSEL University-style numeric problems)
  were not individually re-verified line-by-line.

## Session 2026-09-18 — quiz citations didn't scroll (root cause: `sec` was
## unset on 443 of 543 authored quiz questions), + a section-by-section
## revision checklist added to every QA chapter's summary
User reported that chapter-quiz citations in PS (and, on checking, every subject
except IT) weren't scrolling to the cited section, and asked for the citation to
show **before** answering too, not just in the post-answer "why" box.
- **Root cause**: `citeHTML()` in `src/quiz.js` only renders a clickable link when
  the question object has a `sec` field; otherwise it silently falls back to
  plain, non-clickable text. A prior session ("2026-09-14") wired up the
  mechanism and populated `sec` for IT's 100 authored quiz items, but never did
  the other 443 (FA 123, PS 176, QA 144) — so for every subject but IT, the
  citation was always the plain-text fallback with nothing to click. The
  scroll mechanism itself (`VIEWS.chapter` → `scrollToAnchor()` reading
  `route.q.sec`) was already correct and needed no fix.
- **Fix**: every authored `quiz.mcq`/`quiz.theory` item's `'src': 'Chapter '
  X.Y'` field already names the exact section its answer comes from — a
  script parsed that string, resolved it (with dotted-suffix truncation, e.g.
  `18.8.2` → `18.8`) against the chapter's own `secs[].n` list, and inserted
  a matching `'sec': 'X.Y'` right after `src` wherever one didn't already
  exist. 434/443 resolved on the first pass; the remaining 9 (PS ch17/18/19,
  sub-numbered references like `19.3.2(a)`) resolved once truncation was
  added. **443/443 auto-resolved, 0 needed a manual guess.** Verified every
  inserted `sec` against the built `data/<subj>.js` — all 543 (100 IT + 443
  new) point at a section that actually exists in that chapter; 0 mismatches.
- **New UI**: `citeTop()` in `quiz.js` now renders the same citation link at
  the **top** of the question card (new `.qsrc` CSS in `page.html`), visible
  before the question is answered, in addition to the existing one in the
  post-answer "why"/model-answer block. Suppressed during timed exam-mode
  sitting (`Q.exam`), so a citation never hints at the source chapter before
  a simulated exam question is attempted.
- Verified end-to-end with a Node simulation of `citeHTML()`'s link format →
  `parseHash()`'s query parsing → the DOM anchor `VIEWS.chapter` renders —
  confirms `sec: '8.6'` produces `href="#/s/PS/8?sec=8-6"`, which parses back
  to `sec=8-6`, which matches anchor id `sec-8-6` exactly. (No live browser
  available this session — Claude-in-Chrome extension wasn't connected — so
  this was the strongest verification possible; worth an actual click-through
  next time the browser tool is available.)

User also asked, again, for QA: "a detailed summary of each chapter section by
section such that I do not miss any info... not even one info." Checked the
existing "Worksheet summary" sections first rather than assuming they were
still deficient (per [[fidelity-pass]], an earlier pass already built these) —
spot-checked ch03/ch09/ch19 line by line against their own body content and
found the substance (every definition, every formula, including deliberately-
scoped-out things like ch19's stepping-stone/MODI) was already genuinely
complete. The real gap was **presentation**: the summaries are organised by
*topic* (lettered "A/B/C..." headers), not by the chapter's own section
numbers, so there was no way to confirm every section (2.1, 2.2, 2.3...) had
actually been captured without re-reading the whole chapter.
- **Fix**: added a **"Section-by-section checklist"** as the first block of
  every QA chapter's Worksheet-summary section (all 20, including ch01's
  differently-named "Full revision summary" and ch14's formula-free "OR
  intro" summary) — one compact, numbered entry per body section (§X.1, §X.2,
  ...), each entry compressing that section's core definitions, formulas and
  gotchas into 2–5 sentences. This sits *alongside* the existing topic-
  organised content (definitions, lettered formula groups), not instead of
  it — nothing was removed, only made independently checkable per section.
- Full rebuild clean: `python3 tools/build_content.py && ./build.sh` — QA
  104 sections (unchanged — checklists are new blocks *within* the existing
  summary sections, not new top-level sections), all four subjects clean.

## Session 2026-09-15 (cont.) — PS chapter 23 added too: it's 23/23, not 22/22
User confirmed (asked via AskUserQuestion) they wanted the discovered-but-not-yet-
authored 23rd PS chapter added rather than left as a flagged gap. **Chapter 23,
"Public Sector Audit"**, authored in the same full-fidelity style as 21/22: legal
basis (Constitution ss.85–87/125, parastatal audit requirements), audit objectives
(completeness/occurrence/measurement/regularity/disclosure) and the 7 factors for
an effective audit, the three main audit types (compliance/financial/performance —
full VFM "3 Es" treatment with the steps in a VFM audit) plus 10 other named audit
types (pre-/post-payment, interim/final, management, operational, vouching,
verification, ad-hoc, annual), the ISA-based steps in auditing government
statements (planning, engagement letter, entrance conference, regularity-audit
scope, fieldwork, draft report, exit conference, report distribution — compressed
from the study text's much longer ISA 300/210/260/265 quotations, since those are
generic auditing-standard boilerplate rather than PS-specific), the Auditor-
General/Public Accounts Committee relationship, internal audit (objectives, scope,
its role in a democracy, how to foster the internal/external audit relationship),
where specialists can assist the Auditor-General, the INTOSAI code of ethics and
basic postulates, and the full **codified audit-query offences/sanctions table**
from FR 2009 ch.31 (19 rows — contractor defaults route to blacklist+EFCC, officer
defaults route to surcharge/removal/discipline) — plus the study text's own
end-of-chapter Q&A. `SUBJECTS`/`src/subjects.js` PS count updated `22 → 23`.
Re-ran the full citation pipeline once more (`aim.py → aim_sec.py → build_exams.py`):
ch23 picked up 10 genuinely-matching questions (mostly reclaimed from ch18's
Financial Management Control, which shares audit/internal-control vocabulary — ch18
dropped 29→24 matched questions as they moved to their real home). Final smoke test
of `data/exams.js`: 96 papers, chapters 21/22/23 all present with real citation
counts, zero citations outside the valid 1–23 range. Full rebuild clean — PS is now
genuinely 23/23, matching the study text exactly; no more discovered-but-unbuilt
chapters remain.

## Session 2026-09-15 — PS was missing 9 chapters' worth of content and 2 whole
## chapters; both now closed. PS is 22/22, not 20/20.
User asked me to verify PS "contains all info in the study text." Checked directly
against the re-extracted study-text PDF instead of trusting earlier session notes,
and found two real gaps:

- **Chapters 8–16 (9 of the then-20 chapters) had no end-of-chapter Q&A section at
  all**, and several also had entire body topics missing that the book covers.
  Fixed chapter by chapter, appending new sections (never rewriting existing ones)
  plus a final "End-of-chapter questions (study text)" section with the book's own
  Section A/B and official answers:
  - **ch08 (Vouchers)**: added §8.7 Payroll accounting in the public sector — PERC
    custody, action by salaries/internal audit/cash office — entirely absent before
    (the site only covered voucher classification/contents/flow/registers/loss, not
    payroll at all) — + §8.8 Q&A.
  - **ch09 (Revenue)**: added funds classification (government/proprietary/
    fiduciary; general/capital-project/special/trust/contingency/inter-govt-service/
    revolving/self-liquidating), the 2025-reform revenue agencies (NNPCL, NUPRC,
    NMDPRA, **Nigeria Revenue Service** replacing FIRS, SBIRS, NCS — including the
    2023 Customs Act's 4% FOB levy replacing the old 7% cost-of-collection cut),
    FAAC technical/plenary sessions, SJLGAAC (+ the July-2024 Supreme Court change
    to direct LG payment), the new **Joint Revenue Board of Nigeria (2025 Act)**,
    RMAFC, the CRF/Development Fund/Contingency Fund with a full worked
    illustration, and Ghana's revenue/fund system — none of this 2025-reform
    material existed on the site before. + Q&A.
  - **ch10 (Procurement)**: body content was already thorough; added the missing
    Q&A (Due Process, post-award voucher requirements, e-payment guidelines,
    direct-procurement circumstances).
  - **ch11 (Stores/losses)**: added the storekeeper's functions and procurement
    procedure, cost-of-inventory valuation (fixed-price/last-known-price methods),
    a full **IPSAS 12 (Inventories)** section (measurement, cost formulas — FIFO/
    weighted-average, disclosure) that didn't exist anywhere on the site, and the
    **Federal Losses Committee** (composition, function) plus TF146 loss-reporting
    procedure and the accounting-entries table for losses — none previously
    covered (the existing Board of Survey/Enquiry content was fine and untouched).
    + Q&A.
  - **ch12 (Local government)**: added Financial Memoranda objectives/contents,
    expenditure accounting treatment, the three cash-basis LG final-accounts
    statements in full, internal/external financial control, spending-limit
    tables by IGR band, grants-in-aid objectives, fee-charging policy factors,
    and budgetary control procedure. + Q&A.
  - **ch13 (Cashbook/transcripts)**: added the cash office (features, functions,
    security-document retention, cash-control measures), the imprest holder
    (standing/special imprest, checks and balances), the revenue collector, the
    personal/non-personal advance types, and self-accounting vs sub-self-
    accounting vs non-self-accounting units (+ the three transcript types, the
    main ledger) — a whole layer of named roles/procedures the site's otherwise
    excellent worked-example content never touched. + Q&A.
  - **ch14 (Cash-basis statutory statements)**: body was already comprehensive;
    added the missing Q&A (a loan-fund set of ledger accounts, a trial-balance
    extraction, a recurrent/capital account with comparatives, and a direct-
    method cash-flow statement with comparatives).
  - **ch15 (IPSAS 33)**: body was already comprehensive; added the missing Q&A
    (MCQ + short-answer + three Section B scenarios: revenue recognition from
    1 Jan 2016, preparing the opening SOFP under three different starting
    conditions, and asset-recognition criteria/steps).
  - **ch16 (Accrual-basis statements)**: added **IPSAS 3** (accounting policies/
    estimates/errors), the full notes-disclosure list and **qualitative
    characteristics of financial reporting** (12 of them — none were on the
    site), **IPSAS 45/17 (PP&E)** in full (heritage/infrastructure/weapons-system
    asset classes, recognition, cost, revaluation-surplus mechanics, depreciation
    review, disclosure), **IPSAS 22** general-government-sector disclosure (GGS/
    PFC/PNFC/GBE definitions), and the 2018 Treasury circular on accrual books of
    account. + Q&A (two worked statements: a direct-method cash flow, and a
    statement of financial performance with depreciation/disposal/accrual
    adjustments).
  - Full audit method: for each chapter, diffed the book's own "chapter contents"
    mini-TOC against the site's section list to find topic-level gaps, not just
    the missing Q&A — this is what caught the ch08 payroll gap and the ch09
    2025-reform gap, which a Q&A-only pass would have missed entirely.

- **The book actually has 22 numbered PS chapters, not 20 — chapters 21
  ("Emerging Issues in the Nigerian Public Sector": TSA, ATRRS, IPPIS, GIFMIS,
  Open Treasury Portal, FTeR, NRS e-invoicing, TMRAS) and 22 ("Ethical
  Considerations in Public Sector Accounting in Managing Economic Crimes": EFCC,
  ICPC, Code of Conduct Bureau/Tribunal, Public Complaints Commission, the Money
  Laundering (Prohibition) Act, the Judiciary) didn't exist on the site at all.**
  Authored both from scratch in the same full-fidelity style as ch17–20 (body
  content + a faithful "End-of-chapter questions (study text)" section with the
  book's own Section A/B and official answers). `tools/build_content.py`'s
  `SUBJECTS` PS count updated `20 → 22`; `src/subjects.js`'s PS `n` likewise —
  the homepage/progress-dashboard chapter tally is computed from that, so no
  other UI file needed a manual count fix.
  - **The book has a 23rd chapter too — "Public Sector Audit"** (legal
    requirements, audit objectives, types of audit, INTOSAI code of ethics,
    the Auditor-General/PAC relationship, internal audit, offences/sanctions
    under the Financial Regulations). **Not authored** — flagged for the user
    to decide on, not silently added, since this pass was already large. If
    they want full parity, this is the one remaining gap.
- **Past-paper citations were actually broken for these two chapters**, and not
  just because the chapters didn't exist. `tools/outline.py`'s chapter-boundary
  regex only recognised chapter-heading number words up to "TWENTY" (`WORDS` list
  capped there), so `tools/aim.py`'s retrieval never even saw chapters 21–22 as
  candidates — any exam question about TSA, GIFMIS, EFCC, ICPC etc. was being
  silently mis-attributed to whichever of chapters 1–20 scored next-best. Fixed by
  extending `WORDS`/`NUM` to `TWENTY-ONE`/`TWENTY-TWO`/`TWENTY-THREE` (the PDF
  prints this as "CHAPTER TWENTY- ONE" with a stray space, so the regex/canon-
  icalisation is whitespace/hyphen-tolerant), then re-ran the full pipeline
  (`aim.py → aim_sec.py → build_exams.py`). Result: 55 questions now correctly
  cite ch21 and 66 cite ch22 (previously 0, wrongly folded into other chapters —
  e.g. ch1 dropped from 48→40 matched questions, ch2 84→64, ch7 77→72, as those
  questions moved to their real home). Also added a **new safety filter** in
  `aim.py`'s `build_index()`: retrieval is now confined to chapters that have a
  `CHAPTER_KEYS` entry (i.e. an authored site chapter) at all, so the newly-
  visible "chapter 23" in the raw PDF (which has no site page) can't attract a
  citation that would point at a non-existent page — its 1 matched question
  falls back to the next-best of chapters 1–22 instead. Verified via a Node
  smoke-test of the built `data/exams.js`: 96 papers, ch21/ch22 citations present,
  zero citations outside the valid 1–22 range.
- Added `CHAPTER_KEYS['PS'][21]`/`[22]` seed vocab to `tools/corrections.py` for
  the new chapters (TSA/ATRRS/IPPIS/GIFMIS/etc.; EFCC/ICPC/money-laundering/etc.).
- Full rebuild clean: `python3 tools/build_content.py && ./build.sh` — PS 22/22
  chapters, 219 sections (up from 169 at the start of this pass), 139 MCQ, 30
  theory; all four subjects build with no regressions.

## Session 2026-09-14 (cont.) — "Examined before" grouped by diet, PS lists
## de-prosed across 13 chapters, QA worksheet-summary gap closed on ch01/ch02
- **Chapter pages now show every past question matched to that chapter**,
  grouped by diet. `fillPqPanel()` in `src/app.js` was already called at the
  bottom of every chapter view but is now a collapsible-by-diet list instead
  of a flat one: `<details class="pqgroup"><summary>{diet name}<span
  class="n">{count} questions</span></summary><div class="pqlist">...</div>
  </details>`, newest diet first, all collapsed by default. Needed once a
  well-covered chapter (e.g. FA ch.8) started matching 100+ questions across
  24 diets — user's explicit choice was "show all, grouped by diet" over
  truncating or paginating. New `.pqgroup`/`.pqgroup > summary` CSS in
  `src/page.html`; the old per-row `.diet` span is gone (redundant with the
  group header now).
- **PS, all 20 chapters: converted every prose-run-on enumeration into a
  real `ol`/`ul` block.** Per the instruction "any list is listed and not
  stated." Found candidates with a semicolon/bold-marker/comma heuristic
  scan (re-run after each batch, refined to exclude worked-example numeric
  narratives and literal exam-question restatements with "(a)...(b)..."
  labels — those stay prose on purpose, they're reproducing the study
  text's own question wording). ~45 conversions across ch01–ch08, ch10,
  ch12, ch17–ch19 (ch09, ch11, ch13–ch16, ch20 needed none). A handful of
  spots were deliberately left as prose after review — two-thing
  comparisons and single-concept explanatory paragraphs aren't lists just
  because they contain semicolons. Build clean: 20/20 chapters, 169
  sections (unchanged — only block types inside existing sections moved),
  49 formulas, 127 MCQ, 28 theory.
- **QA worksheet-summary pass had one real gap: ch02 had no consolidated
  "Worksheet summary" section at all** (its last section was just an
  easy-to-miss checklist + study-text Q&A), unlike ch03–20 which all got
  that treatment in an earlier session. Added `§2.7 Worksheet summary —
  every term defined and every formula`: every definition (measures of
  location/partition, the three means, median, mode, class boundary,
  empirical relationship) plus every formula as an `fbox` with intermediate
  steps spelled out (assumed-mean's `d = x - A` step separated from the
  mean formula itself; mode split into locate-modal-class → Δ₁/Δ₂ → the
  formula). Top-level `formulas` array grew 9 → 15 (step-deviation method,
  median odd/even as separate entries, decile-*k*/percentile-*k* as
  separate entries, the lower-class-boundary derivation).
  - **ch01 was checked, not a gap** — its §1.5 "Full revision summary
    (listed)" already covers the same ground under a different name
    (sections A–J: data collection, sampling, frequency tables, class
    boundaries, charts, software) because ch01 is mostly definitional
    rather than computational; the title difference reflects genuinely
    different content, not a missing section. Added the one formula that
    was discussed in prose but absent from the top-level `formulas` list
    (class boundary, lower). 6 → 7 formulas.
  - Spot-checked the rest (ch01–ch20 `secs`/`formulas` counts) for anything
    that looked truncated — ch14 (0 formulas, Intro to OR) and ch20 (4
    formulas, Simulation) both checked out as genuinely that short given
    their content, not accidentally incomplete.
  - Build clean: `python3 tools/build_content.py qa` → 20/20 chapters, 104
    sections, 230 formulas, 124 MCQ, 20 theory. Full `python3
    tools/build_content.py && ./build.sh` clean across all four subjects.
- **Still open from earlier this session**: user saw a stale "5 diets, 20
  papers" screenshot and asked "what do i do to effect this change" —
  never confirmed whether they're on `localhost` (needs a hard refresh /
  restarted `http.server`) or a real deployed URL (needs a redeploy of
  `index.html` + `data/*.js`). Nothing has been pushed to the git remote
  this session.

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
