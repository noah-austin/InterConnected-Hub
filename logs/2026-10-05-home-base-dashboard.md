# 2026-10-05 — Home base: company dashboard (Interconnected HQ)

**Noah's call:** option C, a full dashboard updated every few hours. This overrides the build instructions' "no web dashboard"; flagged once, and Noah chose it.

**Built**
- `tools/dashboard.py` builds `dashboard/index.html` from `direction.md`, `tracker.md`, `work/bd/outbox/` and `logs/`. Nothing on the page is kept by hand.
- Page sections: standings (sent, replies, meetings, LOIs, referrals, pricing reads) · pipeline by stage (in conversation / ready to send / sent with no reply / on hold / closed) · Noah's moves in order · drafts ready to send · warmest leads · waiting on Noah · recent activity · the full pipeline table · parked · standing operations.
- Published privately: https://claude.ai/artifact/9H74hgAVxvCa6VqW6cwYcu
- Routine `trig_019BdXbuz6TTfAQQ4LqyXKgX`, weekdays 7:27am, 12:27pm and 5:27pm Central, fires into this session to rebuild and republish.

**Rules updated:** `CLAUDE.md` (end-of-session refresh step, repo map, growth-rule exception) · `company/decisions.md` · `company/direction.md` (standing operations) · new `skills/dashboard-refresh.md`.

**First build:** 39 pipeline rows (2 in conversation, 23 ready to send, 7 on hold, 5 closed), 8 open moves, 5 drafts.
**Watch item:** like Sonny's run, the refresh depends on one long-lived session. If the page's "Updated" stamp stops moving, ask a session to check the routine.
