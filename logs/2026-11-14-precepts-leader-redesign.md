# 2026-11-14 — Precepts demo: one app for everyone + group switcher

**Noah:** showed Bryan briefly; he liked it and wants to meet. Asked how a man in several groups sees each, worried about complexity, then agreed to redesign the leader side as "same screens, a few extra buttons."
**Changed (`work/product/precepts-demo/index.html`):** removed the separate leader view (shield, leader tabs, leader banner). Added in-place leader buttons, a header group switcher for multi-group men, per-person inboxes, and a demo-only "Switch to Bryan/Noah" bar. Leader actions open as simple sheets (Post an update, Add files, Manage group).
**Tested:** headless at 390px. Noah sees no leader buttons and no switcher; Bryan sees them on every tab; Bryan posts a pinned Saturday update, adds a file, makes pairs, opens Manage, switches to Thursday (Zoom shows, the Saturday-only update hides); Bryan's inbox is his own; switching back, Noah sees Bryan's update and file. No overflow, no script errors.
**Recorded:** decision in `company/decisions.md`; Do-now 4d updated with Bryan's reaction and meeting questions.
