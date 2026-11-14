# 2026-11-14 — Prayer chain rotation: full test

**Noah:** test a full rotation; worried a man eventually gets himself; does it work with odd and even counts?
**Test:** `work/product/precepts-demo/tests/rotation-test.js` drives the app's own functions in a headless browser.
- Every chain size from 1 to 40 men (odd and even), three full rotations each: **0 self-calls**, every man called exactly once every week, and every man calls every other man exactly once per cycle.
- 5,000 random steps of men joining, leaving and weeks advancing (chain between 2 and 30 men): **0 self-calls, 0 broken weeks**.
**Why it can't hit himself:** each week a man calls the man N spots below him (wrapping around); N runs 1, 2, … up to one less than the chain size, then starts over. N is never 0 or the chain size, which is the only way to land on yourself. Joins and leaves keep N in that range.
**Fixed:** a one-man chain no longer shows "X calls X"; it says he's the only man so far and the chain starts once a second man joins. (Zero men: "Nobody has joined yet.")
