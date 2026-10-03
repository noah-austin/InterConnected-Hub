# 2026-10-03 — Sonny, first run: recovery drafts, silent-thread plan, daily routine

**Role:** Sonny (BD). Gmail was read-only: search and read only. Nothing was sent, no Gmail drafts were created, no labels changed.

**Pipeline check:** `after:2026/10/01 in:anywhere` → only Google Workspace billing mail. Read the Rick Randall and Chris Smith threads for routing and voice. No change since Oct 2.

**Noah's steering (Oct 3):** he approved the plan. "Be creative. Your job is get me in front of people." He asked for a daily scheduled run.

**Outputs**
- `work/bd/outbox/2026-10-03-rick-randall-reschedule.md`: in-thread reply to rickr@, offering Thu Oct 8, Tue Oct 13, Wed Oct 14 at Red Horn.
- `work/bd/outbox/2026-10-03-fellowship-plum-creek-via-rebecca.md`: to Rebecca, cc Chris, offering Tue Oct 13/20/27 in Kyle.
- `work/bd/outbox/2026-10-03-eric-bryant-consultation-form.md`: v3.1 form text.
- `work/bd/outbox/2026-10-03-silent-threads-reapproach.md`: one re-approach note for 21 threads in three batches of about 7 a day after DMARC, closing with a referral ask. Walt Lengel goes Dormant; Kevin and Austin Ridge stay untouched. This changes my Oct 2 proposal: the v2 threads now get a note too instead of going Dormant.
- Routine "Sonny daily BD run" (trigger `trig_011S8K8Uo4m1aVKzCwKtdrtX`), weekdays at 6:47am America/Chicago, fresh session each time, push notification. **Caveat:** it was created without the Gmail connector, because connectors can't be attached from this tool. Noah needs to add Gmail to it in the claude.ai Routines settings, or those runs work from the repo only.

**Files changed:** `pipeline/tracker.md` (verification stamp, rows 37/4/6 point to their drafts, silent rows marked by batch, row 5 Dormant) · `company/direction.md` (do-now items 2–4b, the silent-thread decision, "Standing operations") · `company/decisions.md` (three Oct 3 lines) · `roles/sonny.md` (mandate and daily run).

- `work/bd/2026-10-03-get-in-the-room-plays.md`: 8 ranked plays (warm-path text, FaithTech at Gateway Oct 13, XPastor multiplier, October association meetings, office calls, Austin Seminary Nov 6–7, Texas Baptists Nov 15–17, Christian business rooms). Event dates came from search summaries; unverified ones are marked.

**Later Oct 3: Gmail drafts.** Noah said: "I want those drafts there and ready to go." I flagged the conflict with the repo-only drafts rule once, and he chose to change the rule. I created 23 Gmail drafts: Rick (in-thread, to rickr@), Chris via Rebecca (new thread, cc Chris), and all 21 re-approaches as in-thread replies. Nothing was sent. The Eric form stays as paste text. Rule updated in `CLAUDE.md` (connector rule), `roles/sonny.md`, `company/decisions.md` and `work/bd/outbox/README.md`. The routine prompt was updated to match.
