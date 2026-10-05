# 2026-10-05 — Sonny: scheduled run failure, recovery, routine fix

**What failed (6:48am run, session cse_01RUwgXGsPYt4h8Z1pDJk7ZR):** the routine started a fresh session with no repo source and no connectors.
- No Gmail tools. Routines created from a session can't attach connectors (flagged Oct 3), and Noah's settings fix hadn't been made.
- The clone worked (read access), but `git push` returned 403. The repo wasn't in that session's sources, and `add_repo` wasn't available there.
- That run did write a David Fletcher (XPastor) coffee ask and play #9, but they existed only in its container.

**Recovery (this session, which has Gmail and push):**
- Recreated `work/bd/outbox/2026-10-05-david-fletcher-xpastor-coffee-ask.md` and play #9 in `work/bd/2026-10-03-get-in-the-room-plays.md`. The email is unverified; the (214) phone number is a Dallas area code, so it's suspect.
- Gmail check: `after:2026/10/02` excluding billing mail returned nothing. `list_drafts` shows all 23 drafts still unsent.

**Routine fix:** disabled `trig_011S8K8Uo4m1aVKzCwKtdrtX` (fresh session each run). Created `trig_01CcQMh3zeU7CuKBNAXnb5Nw`, same schedule (weekdays 6:47am Central), which fires into this session (`session_01RpYqGgViyotN6xTacN72hs`) so it has both Gmail and push. It reports by push notification.

**Files changed:** `pipeline/tracker.md` (Oct 5 note) · `company/direction.md` · `roles/sonny.md` (routine description) · the two work files above · this log.
