# 2026-10-05 — Home base: check that Sonny's work landed on main

**Asked by Noah:** confirm the Sonny session handled improvement #1 (work lands on `main`).

**Found**
- All five Sonny commits (Oct 3–5) are on `origin/main`. No stray branches; the only other branch is this build session's. In practice, nothing is lost.
- But the rule itself was never written down, so the next session could still leave work on a side branch. **Fixed:** added "Land your work on main" to "End of every session" in `CLAUDE.md`.
- Checked Sonny's drafts against the guardrails: nothing sent; no note to Austin Ridge (Jeff Rutter) or Kevin; Walt Lengel set Dormant so Austin Stone keeps one thread. Gmail drafts plus a repo copy, per Noah's Oct 3 call. OK.
- **Stale rules tidied in `company/decisions.md`:** the growth rule's no-cron clause is now marked as overridden by Noah's Oct 3 daily-run decision; the daily-run line notes the Oct 5 move to the persistent session; the Oct 2 "drafts in repo, not Gmail" line is marked superseded.

**Watch item:** the daily routine now fires into one specific long-lived session (`session_01RpYqGgViyotN6xTacN72hs`). If that session is ever archived or expires, the 6:47am run stops silently. If a morning goes by with no push notification, ask a session to check the routine.
