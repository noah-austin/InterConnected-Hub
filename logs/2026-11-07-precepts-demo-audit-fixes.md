# 2026-11-07 — Men's Precepts demo: audit and fixes

**Audit:** a separate reviewer (read-only) went through the demo at 390px, 360px and desktop. Verdict: ready to show after small fixes.
**Fixed (`work/product/precepts-demo/index.html`):**
- Must-fix: the spreadsheet file icon was hidden by a class clash (`.sheet` overlay → `#sheet`) · iPhone auto-zoom on text fields (all inputs 16px, including the My Group box and reply box) · the leader view no longer shows Noah's private messages (icon hidden in leader view) · switching views resets scroll · toasts wrap instead of truncating · Leader Prayer Chain buttons moved above the list, with honest copy ("Pairs show in the app right away"; "Text each man his partner").
- Polish: bigger tap targets (Reply, Member view) · one word, "Update," everywhere · leader bar reads "Only leaders see this" · roster "Add a man to the group" · sample file button marked "(demo)" · Back from a private message returns to the message list · darker green tags for contrast · larger tab labels · the sign-in email is required · Mark's message no longer claims he's Noah's partner (pairs can be reshuffled mid-demo).
**Verified:** checks at 390 and 360 for each fix (icon visible, 16px inputs, Back → Messages, scroll 0, no leader message icon, Send visible above the fold at 283px, toast fits); full walkthrough of every member and leader action. No overflow, no script errors.
**Not changed (later, real build):** file sign-ups via My Group instead of a spreadsheet; home-screen icon/manifest; pair history and a draft/send step for leaders.
