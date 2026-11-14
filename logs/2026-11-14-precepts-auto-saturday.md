# 2026-11-14 · home base · Precepts chain runs itself

**Asked (Noah):** joiners wait for the next shift, right? Is the shift automated? Leaders shouldn't need a new-order button.

**Done:** `work/product/precepts-demo/index.html`
- Join/leave now wait for the automatic Saturday-morning move (pending state, "You're in, starting Saturday, Nov 14", "Joins Saturday" chips, upcoming-changes line).
- Removed leader "Move to next week" and "Notify everyone who to call". Added a demo-only "skip ahead to Saturday morning" button.
- Week labels are computed, so skipping ahead never runs out.
- `tests/rotation-test.js` now churns through the waiting path: 0 self-calls, 0 broken weeks over 5,000 steps; all sizes 1–40 clean.
- Plan Revision 10; decision logged in `company/decisions.md`.
