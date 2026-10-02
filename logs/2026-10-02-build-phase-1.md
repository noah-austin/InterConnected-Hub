# 2026-10-02 — Build session, Phase 0.5 + Phase 1 (skeleton + seed)

**Role:** build session (Claude Code), authorized by Noah. Phase 0 confirmed by Noah (Pages enabled, source files supplied).

**Done**
- Skeleton: `/company`, `/roles`, `/pipeline`, `/skills`, `/work/{bd,product,marketing,it}`, `/logs`. CLAUDE.md extended with a repo map and the product-facts rule.
- `company/overview.md`: synthesized from Plan v5.1 + handoffs (two-sided value prop, member-complete test, pricing marked HYPOTHESIS, target market, GTM incl. feedback-first / pastor-is-the-channel / no-link).
- `company/brand-guidelines.md`: `June_Brand_Guidelines_v1.md` byte-for-byte (verified with cmp).
- `company/decisions.md`: consolidated from Dex §4, Sonny §3–4, June §1, Mack §7 and the build instructions' decision record and addendum.
- `company/direction.md`: the addendum's seven "do now" items in order, decisions waiting on Noah, what's working / what to stop, parked list, cutover runbook.
- `roles/sonny.md`, `roles/dex.md`: ported from the briefs and updated with the Sep 24 handoffs. Chat-era mechanics (Noah carrying files, cowork) replaced with read-direction-first / write-back / log. Stale "Interconnect rename pending" language removed (rename is closed). Dormant: `june.md`, `mack.md`. Never stood up: `ada.md`, `pearl.md`, `gus.md`.
- `pipeline/*`: seeded from Sonny's Sep 24 handoff (39 rows, real rows only, no EXAMPLE markers). Objections: 2 real entries. Pricing reactions and referrals: empty, which is true.
- `skills/`: deploy checklist (interim old-repo path + post-cutover path), meeting prep, debrief, pricing three questions, cold-email template v3.1 with its rules.
- `work/` and `company/reference/`: every supplied source file filed by lane. PDFs and docx kept as originals, with `*.text.md` extractions for agents.

**Flags found while seeding**
- `Interconnected_Brand_Guidelines_v1.docx` is actually a text file with a .docx name. Stored as `…docx-as-text.md`; the .md mirror is canon anyway.
- The Plan v5.1 docx's title block still says "Version 5 · August 2026." The filename is the version marker; noted in `company/reference/README.md`.
- Sonny's and Mack's Sep 24 handoffs still describe the Interconnect rename as pending; June's and the addendum say it's closed. The repo follows the addendum (closed).
- Noah deferred the three open BD questions (Kevin, Austin Ridge, warm names) on Oct 2. Logged in direction.md as waiting on Noah.

**Not done here:** Phase 2 inbox reconciliation (next).
