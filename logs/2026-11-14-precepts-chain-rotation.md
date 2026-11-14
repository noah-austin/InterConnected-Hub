# 2026-11-14 — Precepts demo: "A calls B" list + weekly rotation

**Noah:** show the chain as "A calls B / B calls C / C calls D"; each week shift the right side down, bottom to top.
**Built (`work/product/precepts-demo/index.html`):** rows "X calls Y"; fixed left column; the right column is the same list shifted by a weekly offset. Week 1 = A calls B. "Move to next week" rotates and advances the week label. **Direction note for Noah:** with week 1 = A calls B, a downward shift puts every man on himself, so the right side moves **up** one (top to bottom); the self week is skipped at the end of each cycle.
**Tested (new suite):** the format is "A calls B" for all rows; week 1 is the next man down; everyone is called once a week; the left side stays fixed; the right side moves up one with the top going to the bottom; the week label advances; over 19 weeks (20 men) nobody calls himself and each man calls all 19 others. Earlier suites still pass. No overflow, no script errors.
