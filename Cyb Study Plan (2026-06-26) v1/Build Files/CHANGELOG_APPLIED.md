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

## 2nd Changelist — items 1–3 (source applied, not yet generated)
- **1. Bump Phase VI to next page** — added a forced blank page (PageBreak + nbsp paragraph + PageBreak) before the "VI — Secure Code Review & Threat Modeling" banner, so VI starts one page later than it otherwise would. Subsequent page numbers shift +1; self-correcting TOC reconciles at GENERATE.
- **2. Move "Application Strategy"** — removed from end of "Study Methodology"; reinserted verbatim at the end of Phase VIII "Interview Preparation & Interviewing", after "Framing Your Background" (the natural prep → framing → apply capstone).
- **3. OWASP list close** — "…security misconfigurations, insecure deserialization." → "…security misconfigurations, insecure deserialization, and other key risks." (in "What Is Application Security?").

## 2nd Changelist — items 4–6 (source applied, not yet generated)
- **4. Shortened the two resume bullets** — "Legacy PHP, raw SQL, and NoSQL" (6 lines → 3) and "Architecture & domain modeling" (5 lines → 4) trimmed to match the length of the surrounding transferable-skills bullets; core point of each preserved.
- **5. Expanded the "relief" clause** — "The relief this should produce is real and substantial" → "…this should produce as part of a break from never-ending leetcode grinding, contrived software engineering interviews, and poor communication during the full software eng interview lifecycle is real and substantial." (in "Why AppSec Engineering").
- **6. Philadelphia AppSec Community → Appendix** — (a) entire section relocated to the end of the Appendix; (b) "Human Mentorship: MentorCruise" → "Human Mentorship: MentorCruise (or Koz)"; (c) added a short new "Local & Regional Events" subsection after it (events as part of studying — networking + reconnecting to the industry; brief highlights: OWASP Philadelphia, Philly 2600, OWASP Global AppSec DC; points to the Appendix section for full details). TOC reconciled (Philadelphia entry moved below Appendix; new subsection listed; Study-Methodology subs updated). build_appsec.py SECTIONS reordered (Philadelphia now scanned after Appendix) so the self-correcting TOC resolves its new page and the new cross-reference text can't be false-matched.
- **(item 2 follow-up)** TOC subs corrected for last batch's move: removed "Application Strategy" from Study Methodology, added it under Phase VIII.

## 2nd Changelist — item 7 (source applied, not yet generated)
- **7. Spring 2026 → Summer 2026** — "Compensation — Spring 2026" subsection heading and its TOC entry both updated to "Compensation — Summer 2026". These were the only "Spring 2026" references in the document. (The five "transition into application security since May 2026" references were left unchanged — they state when the career transition began, not a Spring/Summer label; flagged for the user to revisit if desired.)

## 2nd Changelist — item 8 (sequential-steps + full timeline reconciliation; source applied)
Verified mapping: Month = Week / 4 (checked against Phases III & VII, exact).
- **"Start applying" conflict** (Month 3-4 / 4-5 / 5 / 5-6 across 4 places) reconciled to a single timeline: **begin Month 4** (after Phases I-III complete at Mo 3.5, with 2+ writeups), **main push Month 6** (Security+ on resume). Updated Target Role nb, Schedule nb, Portfolio target, and Application Strategy.
- **Added explicit application steps** so the floating directives map to real phase steps: Phase IV step 09 "APPLY: Begin Job Applications" (Month 4), Phase VII step 04 "APPLY: Main Application Push" (Month 6).
- **Phase II duration** relabeled Months 1.5-2 -> **1.5-2.25** (banner + timeline chart + schedule heading) to match its actual Week 6-9 span; eliminates steps running past the stated phase end and normalizes the II->III buffer to 0.25 like other boundaries.
- **Phase II step 03** week tag fixed Week 5 -> **Week 7** (Week 5 belongs to Phase I; this was the only break in the otherwise-continuous Weeks 1-26 schedule).
- **Phase IV step numbering** fixed: two "05"s + missing "04" -> Semgrep step renumbered to 04; phase now 01-09 sequential.
- **Prose duration fixes:** Phase II intro "two focused study weeks" -> "a focused final week" (crypto + networking are both Week 9); Phase I intro "in three weeks" -> "in two weeks" (Phase I is Weeks 4-5).
- Left intact (internally consistent, flagged): the five "transition since May 2026" references, and "Commit history from Month 2 onward" (covered by Phase 0 GitHub setup + ongoing project/writeup steps).
- Final re-scan: step numbering sequential in every phase; weeks continuous 1-26 with no gaps/backward jumps; all "start applying" = Month 4; main push = Month 6; phase duration labels (banner = chart = schedule heading) agree for all 10 phases.

## Build-system upgrade — self-correcting TIMELINE check at GENERATE
Added timeline_check.py and wired it into build_appsec.py main(), running BEFORE layout,
mirroring the self-correcting TOC loop (check -> fix -> check -> ... until stable).
Ground-truth convention: Month = Week / 4 (verified against Phases III & VII).

AUTO-FIXED in a loop (each has one deterministic correct value):
  1. Step numbering — steps within a phase must read 01,02,03,... (no gaps/dups); renumbers.
  2. Phase-duration END must cover the last step (label_end == max_step_week/4) — catches a
     phase labelled to end before its own steps finish (the Phase II "1.5-2" vs Week-9 bug).
  3. Three-way agreement — a phase's duration in the banner, the timeline chart, and the
     schedule heading must encode the same numeric range (canonical = the banner); rewrites
     the chart/heading numbers to match. Handles mixed dash styles (literal en/em dash and
     \uXXXX escapes) and the "Mo"/"Wks" vs "Months"/"Weeks" prefix difference.
If it edits the source, build_appsec reloads the content module before building.

REPORTED, never guessed (correct value needs human judgment):
  4. A step whose week falls outside its phase's [start,end] week-bounds
     (e.g. a Phase II step tagged "Week 5" when the phase runs weeks 6-9).
  5. Prose "start applying at Month N" that disagrees with the canonical start (Month 4).

Verified: on the current (reconciled) source the timeline pass makes ZERO edits and reports
ZERO issues; against an injected-fault copy (dup step #, duration undercount, chart/heading
disagreement, out-of-bounds week, prose drift) it auto-fixed the three deterministic classes,
converged on pass 2, and reported the two judgment-class faults.

NOTE: the portable package zip does not yet include timeline_check.py — refresh it before
distributing so a fresh extraction builds with the timeline pass.

## 3rd Changelist — items 1-3 (source applied, not yet generated)
- **1. APPLY steps fixed (order + unit).** Both application steps now use WEEKS instead of months and read in order: Phase IV step 09 "APPLY: Begin Job Applications" tag "Month 4 onward · parallel with study" -> "Throughout Weeks 16-18" (Week 16 = Month 4, mirrors the existing Phase III step 07 "Throughout Weeks 10-14" parallel-step pattern). Phase VII step 04 "APPLY: Main Application Push" tag "Month 6 onward · ..." -> "Week 26 onward" (begins after the Sec+ exam in Week 26). Both now pass the timeline bounds check.
- **2. Philadelphia AppSec Community is now an Appendix subsection, not its own chapter.** Removed its forced page break; demoted its heading H -> SS (matches Books/Certifications/Practical Use Per Phase); demoted its internal "Core Groups"/"Conferences" from SS to bold sub-labels so the nesting reads Appendix > Philadelphia > Core Groups/Conferences. TOC: removed the standalone "Philadelphia AppSec Community" line and added it as a fourth sub under "Appendix". build_appsec.py SECTIONS: removed the Philadelphia entry (it is no longer a page-scanned top-level TOC line).
- **3. Removed "No math prerequisites."** from the Plan Schedule Overview intro paragraph.

## 3rd Changelist — items 4-6 (source applied, not yet generated)
- **4. Plan Schedule Overview chart edits.** "Full Rest" -> "Day Off"; "Income — no study obligation on work days" -> "Income — Two 3–4 hour shifts"; removed "Per week" from the TOTAL STUDY row's Notes cell (now blank); "No study, no work. Required for retention." -> "No study, no work. Required for retention & sanity."
- **5. Internal hyperlink to the Philadelphia appendix subsection.** Added a named destination anchor (<a name="philly_appsec"/>) at the "Philadelphia AppSec Community" heading, and linked the words "Philadelphia AppSec Community" in the Study-Methodology "Local & Regional Events" cross-reference to it using the same color (#3A7AB8) as the web-URL hyperlinks. Markup validated as well-formed reportlab paragraphs.
- **6. Page break before "Portfolio: Writeups & Project Site"** (Study Methodology).

## 3rd Changelist — item 8 (source applied, not yet generated)
- **8. Commit from Day 1.** Rewrote the Portfolio "GitHub:" bullet: "Scripts from the tooling phase... Commit history from Month 2 onward." -> "Commit from Day 1 — the very first commit is this study plan and its build script. Keep one repository for the entire cybersecurity journey: notes, tooling-phase scripts, custom Semgrep rules, automation tools, and lab artifacts, building a continuous commit history from the start. Every README explains the methodology..."
- **7. (Pending)** "4–6 published writeups before the main application push" — recorded with no directive; awaiting clarification on the intended change.

## 3rd Changelist — item 7 (source applied)
- **7. Writeup target reconciled to a ramp.** "Target: 4–6 published writeups before the main application push." -> "Target: at least two published writeups before you begin applying, building to 4–6 before the main application push." Ties the portfolio target to the two defined milestones (begin applying ≈ Month 4 with ~2 writeups, per the Application Strategy; 4–6 by the main push ≈ Month 6) and removes the standalone vague phrasing.

## 4th Changelist — step week-ordering (source applied, not generated)
- **Steps now sorted by week within each phase.** Reordered Phase III and Phase IV so every step reads in ascending (start_week, end_week) order, then renumbered 01,02,…
  - Phase IV before: Burp(15-16), BSCP-Prep(15-17), BSCP-Exam(17-18), Semgrep(16-17), Secrets(17), ZAP(17), Snyk(17-18), Juice Shop(18), APPLY(Throughout 16-18, dumped last).
  - Phase IV after: 01 Burp(15-16), 02 BSCP-Prep(15-17), 03 Semgrep(16-17), 04 APPLY(Throughout 16-18), 05 Secrets(17), 06 ZAP(17), 07 BSCP-Exam(17-18), 08 Snyk(17-18), 09 Juice Shop(18). Fixes the reported case (Semgrep 16-17 now precedes the BSCP exam 17-18) and pulls APPLY into its start-week slot instead of last.
  - Phase III: the "Throughout Weeks 10-14" writeup project moved to step 02 (start week 10), ahead of the week-11/12/13 labs.
- **Made it systematic:** added `reorder_steps()` to timeline_check.py as AUTO-FIX 0 (runs before renumbering in the self-correcting loop), so steps are kept in week order on every GENERATE. Verified idempotent (re-running makes no further changes).
- **Phase 0 left as authored** — its pre-study tasks use day-scoped tags (Day 1 / Days 1-3 / Days 2-4) mixed with one Week tag, so a clean week-sort doesn't apply; left for explicit direction.

## 5th Changelist — extend week-ordering to ALL phases (incl. pre-study)
- Generalized the reorder pass to a unified day-scale key (`_order_key`): Week N -> days [(N-1)*7+1 .. N*7], Day N -> day N. This is order-preserving for week-only phases (they sort identically to before) but lets a phase that MIXES Day- and Week-tags sort by the same ascending start-then-end rule.
- **Phase 0 (Pre-Study) reordered:** was FastAPI(Weeks 1-3), HTTP(Days 1-3), Docker(Days 2-4), Git(Day 1). Now: 01 Git & GitHub Hygiene(Day 1), 02 HTTP & Cookies(Days 1-3), 03 FastAPI(Weeks 1-3), 04 Docker(Days 2-4) — ascending by start day, then end. (FastAPI's day-1 start places it ahead of Docker's day-2 start, mirroring how APPLY·Weeks 16-18 sits ahead of Secrets·Week 17 in Phase IV.)
- Verified ALL ten phases (0-IX) are now in ascending time order; pass remains idempotent (re-run = 0 fixes, 0 issues).

## 6th Changelist — items 1-3 of 10 (source applied, not generated)
1. Phase 0 / concept text fixes:
   - "Review existing HTTP notes (HTML intro notes and Odin HTTP notes)." -> "Review existing HTTP notes (PDF, .odt, and note cards)."
   - "Personal notes covering containers" -> "Personal notes and note cards covering containers"
   - "SQL is the canonical example" -> "SQL injection is the canonical example"
2. Date refresh: all five "May 2026" references in content + the running-page-header "May 2026" (infrastructure.py) -> "June 2026". Left the Thotcon conference's recurring "Annual · May" untouched (not a date reference).
3. De-duplicated: "Their absence or misconfiguration is a finding. Their absence or misconfiguration is a finding in any security review." -> "Their absence or misconfiguration is a finding in any security review."

## 7th Changelist — items 4-6 of 10 (source applied, not generated)
4. **AI references — career comparison removed, threat/industry refs kept.** Per clarification, only the AI-career-vs-cyber-career framing goes. Rewrote the Phase I intro ("AppSec has a mysticism problem from the opposite direction of AI: where AI hype makes it seem unknowably complex…") to "AppSec has a mysticism problem: security culture sometimes makes it seem inaccessible without a decade of CTF grinding. That is not true…". KEPT all AI-as-threat-to-industry content (the "AI Replacing AppSec Engineers" pitfall, "AI is automating the lowest-complexity tasks", entry-level hiring compression), AI-as-industry-fact ("faster AI-assisted detection" in the breach stat), and AI-as-target-employer ("AI-native startups", "Legal AI / LegalTech"). (Reverted two over-eager edits to the breach stat and talent blurb after the clarification.)
5. **Book titles in quotes + italics everywhere.** Wrapped all six published books — Real-World Bug Hunting, Alice and Bob Learn Application Security, Hacking APIs, Threat Modeling: Designing for Security, The Web Application Hacker's Handbook, Impractical Python Projects — as "<i>Title</i>" (curly quotes + italics) across every reference: phase source lists (res), step tags, prose chapter refs, and the Appendix Books table. The "WAHH" acronym shorthand italicized (no quotes on an acronym). Left the OWASP Code Review Guide (a guide, not a published book / not in the Books table) untouched. No double-wrapping.
6. **PortSwigger module hyperlinks** in Phase I "EXPLORE: PortSwigger Academy Orientation": linked "Server-side topics" -> portswigger.net/web-security/all-topics, "SQL Injection" -> /sql-injection, "XSS" -> /cross-site-scripting, all as blue (#3A7AB8) links matching the doc's existing hyperlink style. (URLs verified against the live all-labs page.)

## 8th Changelist — items 7-9 of 10 (source applied, not generated)
7. Phase I WebGoat step: "Clone and run OWASP WebGoat locally via Docker" -> "Ensure local WebGoat still executes as expected in local Docker" (already cloned in the Phase 0 Docker step).
8. Exact WebGoat lesson names: "Complete: SQL Injection (basic), XSS (stored and reflected), Broken Authentication, IDOR" -> "Complete these WebGoat lessons: SQL Injection (intro), Cross Site Scripting, Cross Site Scripting (stored), Authentication Bypasses, and Insecure Direct Object References (IDOR)". (Mapped to current WebGoat lesson titles: basic->intro; reflected XSS = "Cross Site Scripting", stored = "Cross Site Scripting (stored)"; Broken Authentication -> the "Authentication Bypasses" lesson; IDOR -> "Insecure Direct Object References (IDOR)".)
9. TryHackMe link: in Phase I "EXPLORE: TryHackMe Orientation", linked "Web Fundamentals" -> https://tryhackme.com/path/outline/web (blue #3A7AB8), the path that contains HTTP in Detail / Burp basics / OWASP Top 10. Left the other two "Web Fundamentals" mentions (the Phase I TryHackMe source entry and the Appendix table note) unlinked — say the word to link those too.

## 9th Changelist — item 10 of 10 + item-9 follow-up (source applied, not generated)
10. Clarified the ambiguous OWASP Top 10 line. "The full list exists and has structure." -> "The full Top 10 is a structured catalog of the most critical web vulnerability classes." (concept "The OWASP Top 10").
9 (follow-up). Linked "Web Fundamentals" in the two remaining spots, both -> https://tryhackme.com/path/outline/web (blue #3A7AB8): the Phase I TryHackMe source entry and the Appendix Books-table TryHackMe note. The doc now has three Web Fundamentals path links total. (Left "Jr Penetration Tester" path mentions unlinked — say the word to link those too.)

=== ALL 10 CHANGELIST ITEMS COMPLETE ===

## Build fix (during GENERATE)
- linkify() now skips spans already inside an <a>...</a> tag. Previously it re-wrapped the URL inside manually-authored href attributes (the new PortSwigger/TryHackMe links), producing nested <a> tags and a paraparser syntax error at build. Bare-URL auto-linking is unchanged. Verified: all 6 authored links render as clickable annotations; bare URLs (tryhackme.com, github.com/..., owasp.org/...) still auto-link.

## 10th Changelist — fix Phase I PortSwigger links (source applied, not generated)
- The PortSwigger orientation step linked to the wrong things: the all-topics index (dozens of labs) and the SQL/XSS *tutorial* pages, while the text said to do labs. Rewrote step 01:
  - "Create a free PortSwigger account"
  - "Read the [SQL injection] material, then complete the first 3-4 Apprentice-level [labs]" -> material = /web-security/sql-injection, labs = /web-security/all-labs#sql-injection
  - "Read the [cross-site scripting] material, then complete the first 3-4 Apprentice-level [labs] (reflected and stored)" -> material = /web-security/cross-site-scripting, labs = /web-security/all-labs#cross-site-scripting
  - Dropped the ambiguous all-topics "Server-side topics overview" link entirely. All four URLs verified against the live pages (each topic page's "View all <topic> labs" points at the all-labs#<topic> anchor).
- Re-verified the two re-listed items: exact WebGoat lesson names (SQL Injection (intro) / Cross Site Scripting / Cross Site Scripting (stored) / Authentication Bypasses / Insecure Direct Object References (IDOR)) and the three "Web Fundamentals" -> tryhackme.com/path/outline/web links are already in place from the prior batch; no change needed.

## 11th Changelist — concrete TryHackMe room links (source applied, not generated)
- The TryHackMe references only linked the (legacy) path outline and listed room topics as plain text, so it was unclear exactly what to study. Now each specific room is named AND linked, in both the Phase I source entry and step 04:
  - HTTP in Detail -> https://tryhackme.com/room/httpindetail
  - Burp Suite: The Basics -> https://tryhackme.com/room/burpsuitebasics
  - OWASP Top 10 -> https://tryhackme.com/room/owasptop102021
- Verified all three are free, public rooms (the owasptop102021 "lv" variant is private/premium, so avoided it). The Web Fundamentals path link is kept for context. ("Jr Penetration Tester" path left unlinked — not part of the orientation step.)

## 12th Changelist — de-vague Phases II–VII: exact names + links for every study target
Searched Phases II through VII for study targets named without links/exact names and linked them all (blue #3A7AB8), URLs verified against live pages (PortSwigger all-topics index, TryHackMe room pages, etc.):
- **PortSwigger Web Security Academy (13 links across II–IV):** every "learning path" / "labs" reference now links to its exact topic page — Authentication, Access control, API testing, SQL injection, OS command injection, Server-side template injection, Cross-site scripting, CSRF, SSRF, XXE, Business logic (logic-flaws), Insecure deserialization, File upload, Path traversal. The two non-existent/vague "PortSwigger 'HTTP fundamentals'" and "'Burp Suite' learning path" references were corrected to the official Burp Suite documentation.
- **BSCP (Phase IV):** "BSCP exam" -> /web-security/certification; "BSCP practice exams" -> /web-security/certification/practice-exam.
- **OWASP (III, VI):** API Security Top 10, Code Review Guide, ASVS, Threat Dragon now link to their owasp.org project pages.
- **AWS (V):** Shared Responsibility Model and IAM documentation linked.
- **Tools (IV):** Semgrep, Bandit, TruffleHog, Gitleaks, OWASP ZAP, Snyk linked to their official sites at point-of-install.
- **TryHackMe Pre-Security (II):** the two res entries previously linked only to the tryhackme.com homepage; now point at the exact Network Fundamentals module (/module/network-fundamentals) and Putting It All Together room (/room/puttingitalltogether), and those names are linked in the step bullets too.
- Resources that already carried a specific bare URL in their res() entry (auto-linked) were left as-is (OWASP cheat sheets, hashcat, bcrypt, GitHub Security Lab, Professor Messer, FreeCodeCamp). Note: flaws.cloud / flaws2.cloud auto-link already (.cloud TLD).
- Validated by constructing all 928 flowables through build_content with linkify applied (no PDF rendered): zero markup errors.

## 12th Changelist — exact links for vague study references, Phases II–VIII (source only)
Swept Phases II–IX. Found most PortSwigger labs (II–IV) and all Phase IV tools (Semgrep, Bandit, TruffleHog, Gitleaks, ZAP, Snyk, BSCP) were ALREADY linked, and bare domains (flaws.cloud, flaws2.cloud) already auto-link. Remaining prose-named resources lacked inline links; now linked to exact pages:
- Phase II: OWASP Cryptographic Storage Cheat Sheet, OWASP Transport Layer Security Cheat Sheet, OWASP SSRF Prevention Cheat Sheet -> exact cheatsheetseries.owasp.org pages.
- Phase III: "OWASP Top 10 category" -> owasp.org/www-project-top-ten/.
- Phase IV: "Burp Suite Community Edition" -> portswigger.net/burp/communitydownload.
- Phase V: FreeCodeCamp guide -> freecodecamp.org/news/learn-cloud-security-fundamentals-in-aws-a-guide-for-beginners/. (flaws.cloud / flaws2.cloud already auto-linked.)
- Phase VI + VIII: "GitHub Security Lab" -> securitylab.github.com (both occurrences).
- Phase VII: "Professor Messer" -> professormesser.com/sy0-701-certification-course/.
All verified free/public where applicable; all run clean through linkify (no double-wrap) + Paragraph parse.

## 13th Changelist — fix dead TryHackMe OWASP Top 10 link (source only)
- The OWASP Top 10 room link used /room/owasptop102021, which now 302-redirects to /hacktivities/search ("room doesn't exist") — that room code was retired. Fixed by fetching candidate URLs directly:
  - /room/owasptop102021 -> CONFIRMED DEAD (canonical now hacktivities/search)
  - /room/owasptop102021lv -> private/premium (rejected earlier)
  - /room/owasptop10 -> CONFIRMED LIVE & FREE: title "OWASP Top 10", 31 tasks, 224k+ users, no paywall. THIS IS THE FIX.
- Replaced both occurrences (Phase I res entry + step 04) with https://tryhackme.com/room/owasptop10.
- Also re-verified by direct fetch that the other two rooms resolve as live, free public rooms: /room/httpindetail (7 tasks, 646k users) and /room/burpsuitebasics. All three now confirmed by fetching the actual room page (not just search snippets).

## 14th Changelist — Phase I link/content verification + book accuracy fix (source only)
Verified every Phase I hyperlink against live content and the book against the uploaded PDF (Real-World Bug Hunting, 266pp, full TOC extracted):
- WebGoat, PortSwigger (sql-injection material, all-labs#sql-injection Apprentice labs, cross-site-scripting material), TryHackMe Web Fundamentals path (resolves; titled "Legacy") + 3 rooms (httpindetail/burpsuitebasics/owasptop10, all live & free): ALL PASS.
- Book res entry (organized by vulnerability class, real bug bounty reports, 2019 No Starch): PASS — TOC confirms ~17 vuln-class chapters each with real disclosed reports (Shopify/HackerOne/Twitter/Uber/Google).
- Book step 02 "Ch. 1-5 ... organized by vulnerability class with real bug bounty reports": PARTIAL — Ch 1 ("Bug Bounty Basics") is a foundational primer (client/server, HTTP requests), not a vuln class and has no reports; Ch 2-5 are vuln classes (open redirect, HPP, CSRF, HTML injection/content spoofing) with real reports. FIXED: rewrote bullet to say Ch 1 = basics, Ch 2-5 = named vuln classes with real disclosed reports.

## 15th Changelist — Phase II link+content verification, fixes, integrated checker (source only; no PDF generated)
LINKS (all web-verified live this session; content matches description):
  Burp Proxy/Repeater/Intruder tool pages, PortSwigger cors + jwt + oauth topics, MDN CSP/Methods/Status,
  OWASP TLS/Crypto-Storage/SSRF cheat sheets, PortSwigger authentication/access-control/api-testing/sql-injection
  paths + their all-labs#... lab anchors, freeCodeCamp hashcat MD5 guide, PyPI bcrypt, THM network-fundamentals
  module + puttingitalltogether room. All PASS.
BOOKS (verified via published TOC — PDFs were NOT uploaded for Phase II; only Real-World Bug Hunting is on disk):
  * WAHH (Stuttard/Pinto, Wiley 2011): Ch 6 Attacking Authentication, Ch 7 Attacking Session Management,
    Ch 8 Attacking Access Controls all match. FIX: step 01 + res mislabeled Ch 2 as "core protocols";
    Ch 2 is "Core Defense Mechanisms" -> corrected.
  * Alice and Bob Learn Application Security (Janca, Wiley 2020): Ch 1-5 = Security Fundamentals, Security
    Requirements, Secure Design, Secure Code, Common Pitfalls. FIX: step 06 listed "AppSec program basics"
    inside Ch 1-5, but "An AppSec Program" is Ch 7 -> reading corrected to "Ch. 1-5 and Ch. 7" with accurate topics.
9 USER-REQUESTED FIXES applied to appsec_content.py:
  R1 step01 Burp broad docs link -> 3 specific tool pages (Proxy/Repeater/Intruder)
  R2 step01 note-card topics CORS/CSP/TLS/HTTP methods/status each linked to a teaching page
  R3 step02 Authentication "labs" now links to all-labs#authentication
  R4 step02 note cards JWT->/web-security/jwt, OAuth->/web-security/oauth
  R5 step03 Authentication Audit Checklist: added bullet to run it against the Phase 0 FastAPI app (JWT via Security module)
  R6 step04 added access-control + API testing lab links (paths DO have apprentice+practitioner labs)
  R7 step05 SQLi "labs" now links to all-labs#sql-injection
  R8 step07 hashcat task->freeCodeCamp MD5 guide, bcrypt task->PyPI bcrypt
  R9 step08 "Review existing Odin Project HTTP notes and HTML intro notes" -> "Review existing notes"
COVERAGE CHECK (new): every "Concepts Mastered" + "How These Concepts Are Used" item now cross-checked against
  steps+sources for phases 0, I, II (all trace through). Applied going forward to all phases.
INTEGRATED CHECKER: phase_content_check.py (link inventory + manual verdicts, broad-link flag, resource-link gap,
  note-card backing, concepts coverage). Wired into build_appsec.py. Invoke via command "PHASE CONTENT CHECK <ROMAN>"
  (= python3 build_appsec.py CONTENT-CHECK <ROMAN>, or python3 phase_content_check.py <ROMAN>). Offline; does not build the PDF.
VALIDATION: ast.parse + import + 33 Phase II markup fragments through linkify()+Paragraph (no double-wrap). PDF NOT generated (BUILD = source only).

## 15b — Phase II books PDF-verified (confirmation only; no source change)
Both Phase II books were uploaded and verified against actual PDF content (not just published TOC):
  * WAHH (914pp, 2nd ed): outline confirms Ch2="Core Defense Mechanisms" (Ch2 text: "The defense mechanisms
    employed by web applications..."); Ch3="Web Application Technologies" is where the HTTP protocol is examined.
    Confirms the 15th-changelist fix (Ch2 "core protocols" -> "core defense mechanisms") was correct.
    Ch6 Attacking Authentication, Ch7 Attacking Session Management, Ch8 Attacking Access Controls -> match.
  * Alice and Bob (285pp): Ch1-5 = Security Fundamentals/Requirements/Secure Design/Secure Code/Common Pitfalls;
    Ch7="An AppSec Program" (Ch7 text: "This chapter will discuss application security programs..."). Confirms the
    15th-changelist fix (move "AppSec program" from Ch1-5 to "Ch1-5 and Ch7") was correct.
No new discrepancies; Phase II book descriptions now accurate at title AND content level. PHASE CONTENT CHECK II: PASS (26 links, 0 issues).

## 16th Changelist — Phase II "API security" concept de-duplicated (source only; no PDF generated)
Was: "REST API-specific vulnerability patterns. REST API-specific vulnerability patterns covered in this phase."
(redundant — the sentence repeated itself).
Now: "REST API-specific vulnerability patterns — broken object-level authorization (IDOR), mass assignment, and
excessive data exposure — and why APIs widen the attack surface beyond traditional server-rendered applications."
Validated: ast.parse + import + Paragraph parse. PDF NOT generated (BUILD = source only).

## 17th Changelist — GENERATE PDF + packaging
- Generated Study_Plan_-_2026-06-26.pdf (50pp); all TOC page numbers verified against actual pages.
- Added present_build_zip.py (assembles the full package). New command: PRESENT BUILD ZIP
  (= python3 build_appsec.py PRESENT-ZIP, or python3 present_build_zip.py). Bundles every prior package
  file (updated) PLUS new files phase_content_check.py and present_build_zip.py, with the latest PDF as
  *_LATEST.pdf and the original source as *_SOURCE.pdf.
- README updated to document phase_content_check.py and the verification command.
