# CHANGELOG_APPLIED — items baked into the source (.py) but NOT yet generated to PDF

This ledger tracks which changelist items are implemented in the source code.
The .py files in this folder are the latest accumulated state.
PDF generated and TOC verified against actual pages (48pp).

## Implemented so far
- [x] 1 — Cover subtitle now "Independent Self-Study — Kyle Miskell  —  kmiskell@protonmail.com"
- [x] 2 — Removed cover "Orientation → … → Job" arrow-progression text (gold underline kept)
- [x] 3 — Weeks→Months convention at PHASE LEVEL: timeline cells, phase banner durations,
        and phase section sub-headers now use "Months" for phases past week 8 (II–IX);
        phases 0 and I stay in "Weeks". Phase II = Months 1.5–2 (per your example).
        NOTE: granular per-step labels (e.g. "· Week 11", "Weeks 10–11") were left as
        weeks pending your confirmation (see status note in chat).

- [x] 4 — Interview Prep (VIII) moved to start week 27 (month 6.75): banner now "Months 6.75–7.25";
        First Days (IX) banner now "Months 7+"; timeline VIII/IX cells updated. Security+ exam
        stays Week 26 (no overlap). NOTE: IX "First Days" set to 7+ for sequential consistency
        (it follows interview prep); flagged in chat. No internal week numbers existed in VIII/IX.
- [x] 5 — Phase Timeline fixed to match the 10 real phases (0–IX): removed the spurious
        "Portfolio" column, so VIII = Interview Prep and IX = First Days now carry the correct
        roman numerals; reduced to 10 colored columns.
- [x] 6 — Removed "Conceptual Questions — Know These Cold" section (all Q&A entries) and its TOC sub-entry.

- [x] 7 — Phase VIII renamed "Interview Preparation & Interviewing" (banner, TOC title, comment).
- [x] 8 — Reworked Phase VIII: removed "Pre-Interview Portfolio Checklist" (not relocated — the
        underlying project work already lives in earlier phases; flagged in chat). Added three
        method sections: Behavioral Question Rehearsals; Technical Note Cards (with the 7-card
        sub-group / 5x / combine-into-reviewed-pile spaced-repetition method); Technical
        Programming Practice (secure code review via GitHub Security Lab CVE writeups; light
        scripting via CoderPad drills + Impractical Python Projects (2019); security-focused
        system design). Renamed "Interview Format: What to Expect" -> "Interview Preparation",
        now mapping each format to its prep method. Kept "Framing Your Background". No
        NeetCode/LeetCode recommended (security-appropriate resources used).
- [x] 9 — Already satisfied by item 5: "Expected First Days on the Job" now carries roman IX in
        the Phase Timeline.

- [x] 8-followup (A–D) — restored the substance of the removed Pre-Interview Portfolio
        Checklist into the earlier phases where the work happens:
        A. Phase IV Juice Shop step: export the report as a polished, shareable standalone PDF.
        B. Study Methodology / Portfolio: READMEs explain methodology + what each artifact
           demonstrates (was just "Clean READMEs").
        C. Application Strategy: pin the new AppSec artifacts (Juice Shop report, Semgrep rule,
           threat model) on GitHub.
        D. LinkedIn profile setup — early (Phase 0 GitHub-hygiene step: About-section transition
           narrative) + application-ready (Application Strategy: Security+/BSCP listed, projects
           linked, About narrative).
        (Item 4 of the old checklist — 4+ writeups published on LinkedIn — was already covered.)

- [x] 10 — Cover pills updated: VIII pill now "Interview / Prep" (matches the renamed phase and the
        timeline label). The pills were already 0–IX with correct romans (no Portfolio pill bug),
        so only VIII's label needed changing.
- [x] 11 — Reworded: "...insecure deserialization. These are not abstract academic concerns — they
        are the specific vulnerability classes..." (was "— these are not abstract academic
        concerns. They are...").
- [x] 12 — Replaced "— they understand for five years." with "— they have already built the
        software systems being tested for security risks and strength themselves."

- [x] 13 — Fixed the 60/40 math: "Over 60% ... integrate ... which means nearly 40% still do not"
        (was "over 40%", which summed past 100%).
- [x] 14 — Verified AppSec salaries via web (Indeed ~$148K avg, ZipRecruiter ~$138K avg /
        $117.5K–$157K typical, Glassdoor ~$181K total, base-only aggregators ~$98K). The
        compensation table (entry $90–130K, mid $130–180K, senior $170–240K, top $250K+) is
        realistic; the outlier was the prose claim "$126,000–$194,000 at mid-level", now aligned
        to "$130,000–$180,000" to match the table.
- [x] 15 — (a) Added "poorly written legacy PHP codebases" to the "You know FastAPI ... Docker
        containers" stack sentence. (b) Added a "Legacy PHP and hand-rolled SQL" transferable-skill
        bullet covering legacy PHP, legacy/raw SQL (-> SQL injection / IDOR / unsanitized input
        from the inside) and modern DynamoDB (-> NoSQL injection / cloud data-access control).
        NOTE: the resume PDF was not present in uploads this session, so I used the experience
        facts you stated (legacy PHP, legacy SQL, DynamoDB) rather than reading the resume.

- [x] 16 — "AppSec testing follows the same deterministic logic: ..." (added "deterministic").
- [x] 17 — "The relief this should produce is real and substantial." (was "real and earned").
- [x] 18 — "The 2026 job market is highly difficult for web development." (added "highly").
        NOTE: this sentence sits inside "The Timing Argument" subsection, which item 19 is slated
        to REMOVE — so this edit will be discarded by item 19 unless we choose to preserve the
        point elsewhere. Flagged in chat for decision at item 19.

- [x] 15-resume — Resume now available; enhanced the transferable-skills section: refined the
        legacy-code bullet to "Legacy PHP, raw SQL, and NoSQL" (you maintained poorly written
        legacy PHP and hand-rolled MySQL AND refactored 'big ball of mud' procedural PHP to OOP
        — recognize + remediate; DynamoDB -> NoSQL injection). Added a new "Architecture &
        domain modeling" bullet (your microservice/domain-service design experience maps directly
        to threat modeling). [Discretionary architecture bullet flagged in chat.]
- [x] 19 (COMPLETE) — Removed "The Timing Argument" subsection (last sub-section of Why AppSec
        Engineering; not in TOC, so no TOC sub-entry change). This supersedes item 18's edit per
        higher-number-wins. STILL PENDING: move "Why This Moment" to AFTER "Why AppSec Engineering"
        + swapped their order in the TOC (page numbers deferred to item 24).

- [x] 20 — Reduced FastAPI focus: genericized 8 generic stand-in references (Why AppSec, Target
        Role, Phases III/V/VI, appendix) to "web application" / "software system" / "Python web
        application (Django, Flask, or FastAPI)" / "API". Kept FastAPI where it is genuinely your
        resume background (transferable-skills bullets) and the concrete pre-study build project
        (Phase 0). FastAPI mentions: 23 -> 16.
- [x] 21 — Removed cross-section redundancy: the "developer-background-is-the-advantage" argument
        now lives only in "Why AppSec Engineering". Trimmed it from "What Is AppSec" para 5 (kept
        the scoping sentence) and removed the "Why your background fits this moment specifically"
        subsection from "Why This Moment" (it duplicated both the adjacent Why-AppSec section and
        the workforce-gap point; kept the market nb-box closer). Target Role left untouched.

- [x] 22 — Schedule table: removed the "Rest w/ Short Study" row; now 21 study hours/week across
        3 Long Study days x 7 hrs, with 2 full rest days/week (week = 3 study + 2 gig + 2 rest = 7
        days). Intro updated "20-23" -> "21 study hours per week". Folded the dropped day's
        activities (note-card review, writeups) into the Long Study notes so nothing is lost.
- [x] 23 — Work (Gigs) days set to 7 hrs (was 6-7 hrs).

- [x] 24 (COMPLETE) — Reconciled the Contents:
        all section titles verified against actual H()/banner headers (all match); fixed the
        roman-numeral bug (a second "VIII" -> "IX" for Expected First Days). TOC romans are now a
        clean 0,I,II,III,IV,V,VI,VII,VIII,IX. Order already swapped in item 19.
        PAGE NUMBERS finalized by building the PDF and scanning actual page positions (pdfplumber,
        no image rendering). Updated 5 stale entries: Why AppSec 6->4, Why This Moment 4->6,
        II Web&Network 19->22, IX 45->44, Appendix 47->46. Verified by an independent
        TOC-page-skipping sequential scan: all 19 entries match actual pages, monotonic increasing.
        Also hardened build_appsec.py scan_pages to skip TOC pages so the build self-verifies.
        Final PDF: 48 pages.

## Not yet implemented
- [ ] (none — ALL 24 CHANGELIST ITEMS COMPLETE)

## Build-system changes (post-changelist)
- Output filename is now date-based: OUTPUT in appsec_infrastructure.py uses
  datetime.date.today() -> "Study_Plan_-_YYYY-MM-DD.pdf" (today: Study_Plan_-_2026-06-25.pdf).
- Self-correcting TOC: build_appsec.py main() now runs a build->scan->fix->rebuild loop.
  * build_content(appsec_content.py) accepts page_overrides={toc_title: page}; the TOC renders
    page_overrides.get(title, <source default>) so the build can override page numbers.
  * Each pass: build, scan ACTUAL section pages (pdfplumber, TOC-page-skipping robust scan),
    and if any TOC page != actual page, set overrides=actual and rebuild. Repeats until the
    printed TOC matches actual pages (handles digit-count-driven repagination), max 8 passes.
  * Ends with an independent final verification printed per-section, and saves the converged
    {toc_title: page} map to appsec_toc_state.json (so later runs converge in ~1 pass).
  * NOTE: TOC sub-entries are descriptive labels and carry no page numbers, so only section-level
    page numbers are reconciled.
- appsec_toc_state.json reset to {} so the next GENERATE PDF starts clean and self-corrects.
