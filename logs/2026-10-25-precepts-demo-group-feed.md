# 2026-10-25 — Men's Precepts demo: My Group, middle ground

**Noah:** Group Chat went too far toward a group text; land in the middle.
**Changed:** `work/product/precepts-demo/index.html`. My Group is a casual post feed: an inline composer with an "Ask for help" toggle, newest posts first, short chat-style replies under each post, inline reply, and "Asking for help" → "Taken care of." Removed the chat bar.
**Tested:** headless at 390px: reply, post an ask, mark taken care of; full walkthrough of the other tabs and leader view; no overflow, no script errors. Fixed a tap-target bug (the text box resized on blur and made "Ask for help" miss).
