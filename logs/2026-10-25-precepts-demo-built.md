# 2026-10-25 — Men's Precepts demo built

**Noah:** removed homework check-off, prayer request submission and the directory; added leader-uploaded weekly files; prayer chain is one-to-one; keep private messages; "Build it."
**Built:** `work/product/precepts-demo/index.html`, one self-contained page (Inter font only; no other external calls), sample data, nothing saved. Member tabs: This Week, Updates, My Group, Prayer, Files, plus messages. Leader view as Bryan: Announce, Upload, Prayer Chain (make and send pairs), Roster (invite). Changes made in leader view show up in member view.
**Tested:** a headless Chromium walkthrough at 390px: sign-in, every tab, a reply, a DM, posting an announcement, uploading files, shuffling pairs, switching back. The announcement and files appear on Noah's This Week; no horizontal overflow; no script errors (the only error was the Google Font being blocked by this sandbox's proxy). Fixed two bugs found in testing: hidden overlays still caught taps, and the screen slid sideways after closing a conversation.
**Hosted:** Railway project `interconnected-hq`, service `precepts-demo` (`work/product/precepts-demo/Dockerfile`, Caddy), https://mens-precepts.up.railway.app. Rebuilds on pushes to `work/product/precepts-demo/`.
**To confirm with Noah:** Saturday and Thursday meeting times; lesson titles and dates.
