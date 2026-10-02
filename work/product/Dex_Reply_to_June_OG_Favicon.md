# Link Preview + Favicon — Dex reply to June
**From:** Dex (Product) · **To:** June (Marketing), Mack (IT), via home base · **Date:** Aug 24, 2026
**Status:** Built. Ships with the next site file (bundle attached to Noah).

## What June asked for (§6)
- **Canonical URL used:** `https://www.joininterconnected.com/` (the www host is the one with the CNAME; GitHub Pages redirects the bare domain to it). All `og:` and `twitter:` image URLs are absolute on that host.
- **Primary background hex:** two, on purpose. `og-image.png` and `apple-touch-icon.png` use the primary brand blue **`#2563EB`** (solid, no gradient, per §2). `theme-color` is **`#F7FAFF`** — the site's nav surface (white at 78% over the hero's `#DBEAFE`), so mobile browser chrome blends into the top of the page instead of putting a deep-blue bar over a light site. If you'd rather the chrome go brand-blue, it's a one-value change.
- **Description:** built with the two-sided version per your recommendation. Roofer line is a one-line swap if Noah prefers it.

## What was built
- **Head tags:** exactly your §1 snippet, URLs filled. `<title>` and `<meta name="description">` updated to the new copy site-wide (they were the older tagline versions).
- **og-image.png:** 1200×630, 60 KB. Laid out as an HTML block in the site's own CSS and Inter, screenshot at 2× and downsampled. Mark ~140 px tall, wordmark 72 px Inter 800 white, tagline 36 px `#BFDBFE`, everything inside the center 630×630 square (the tagline wraps to two lines to stay inside the square). No stats, no screenshot, no "demo."
- **favicon.svg:** the dot-cross **simplified for small sizes** — 13 thicker dots, same silhouette, same four blues. At 16 px the original 47-dot mark merges into a blob, so this is the size-tuned variant your §3 legibility rule calls for. Includes a `prefers-color-scheme: dark` variant (light dots) inside the SVG. No letter, no text.
- **favicon.ico:** 16 and 32 in one file, rasterized from the same simplified mark.
- **apple-touch-icon.png:** 180×180, solid `#2563EB`, full 47-dot mark (light-on-blue palette from the app splash) at ~67% of the canvas, clear of the corner radius. No transparency.
- **icon-192 / icon-512:** generated since it was free; not referenced anywhere until a manifest exists.

## Deploy (Noah)
Five files go to the **repo root**, same commit: `index.html`, `og-image.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`. The zip is already named correctly — unzip and upload all five together. Delete the old `index.html` first as usual. Windows note still applies: confirm the file is `index.html`, not `index.html.html`.

## For Mack's checklist (§5)
- Previews will show stale for any thread where the link was already sent; test in a fresh thread.
- If iMessage shows the old bare link even in a fresh thread, it's Apple's cache; wait an hour and retry before changing anything.
- Facebook Sharing Debugger and LinkedIn Post Inspector both force a re-crawl; run them once after the green check.

## Also in this file (product, not marketing)
Two sample-data corrections from the Sonny inventory: the care-signal line no longer implies attendance tracking, and Year in Review now says 8 member-started groups to match the roster.
