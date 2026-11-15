# 2026-11-15 · home base · Precepts audit fixes

**Asked (Noah):** run a Fable audit on every aspect of the demo, then "go ahead with the fixes the agent suggested." Answers: meeting this week; Thursday meets before Saturday; email fallback for notifications; leaders can delete announcements/files/lessons; reword number privacy; trim.

**Done:** `work/product/precepts-demo/index.html`, every must-fix, should-fix and nice-to-have from the audit (details in plan Revision 15). Biggest change: weeks run Sun–Sat and roll over Sunday morning. `tests/rotation-test.js` now calls `sundayMorning()`. Decisions logged.

**Checked (headless Chromium, Central time):** a 45-point click-through of every fix passes, with 0 page errors, including Thanksgiving and Thursday dates, pin per group, guards in the schedule editor, a date move across the daylight-saving change, deletes, welcome/sign-in, profile Save, Feed draft/cancel and Manage. Small phones (320×568, 360×640, 375×548, 390, 430): welcome scrolls, Send buttons visible, no sideways scroll, tabs don't overlap. Rotation stress test: 0 self-calls, 0 broken weeks. Found and fixed a fast-double-back bug that left an invisible sheet over the app.

**Not changed:** refreshing the page resets the demo (by design). The group switcher pill is 36px tall (header space).
