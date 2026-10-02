# Link Preview + Favicon — Handoff to Dex
**From:** June (Marketing Director) · **To:** Dex (Head of Product Development), via home base · **Date:** Mon Aug 24, 2026
**Verify after deploy:** Mack (IT Manager) — checklist in §5
**Status:** Ready to implement. No copy decisions left open except the one flagged in §1.

**Why this matters:** the site link gets texted to pastors and investors. Today the text shows a bare URL. After this, it shows our mark, our name, and our tagline before anyone taps. It is the first impression, and right now it is going to waste.

**Name:** Interconnected. Confirmed by Noah on Aug 24. Bake it in with full confidence.

---

## 1. Copy (final unless Noah overrides)

| Tag | Copy | Notes |
|---|---|---|
| `og:site_name` | `Interconnected` | |
| `og:title` / `twitter:title` / `<title>` | `Interconnected: your church, connected every day of the week` | 60 chars. Name first because iMessage and WhatsApp show the title far bigger than the description, and the name is the thing we need a pastor to remember when the text comes back up a week later. |
| `og:description` / `twitter:description` / `<meta name="description">` | `A private, invitation-only network for one church. Members find each other's skills, gifts, and needs during the week. Leaders finally see what the body can do.` | 160 chars. Two-sided value prop: members join for community, the church pays for community plus insight. The last sentence is the church-side beat (gifts census) without naming a feature we can't show. |
| `og:url` | the site's canonical URL (Dex: the one in the outreach emails, no trailing `index.html`) | Absolute. |
| `og:type` | `website` | |
| `og:image` / `twitter:image` | absolute URL to `/og-image.png` (spec in §2) | Must be an absolute https URL, hosted on our domain. Not SVG. |
| `og:image:width` / `og:image:height` | `1200` / `630` | |
| `og:image:alt` | `Interconnected. Your church, connected every day of the week.` | |
| `twitter:card` | `summary_large_image` | |
| `theme-color` | the site's primary brand background color | Colors the browser chrome on mobile when a pastor opens the link. Small, free polish. |

**One flag for Noah.** The description above is the two-sided version. The alternative is the roofer line, which is our best spoken hook:
> `When someone at church needs a roofer, a tutor, or a babysitter, the first thought becomes someone at church instead of Google. One private network per church.` (159 chars)

I recommend the two-sided version for the tag. Reason: on WhatsApp and Slack the description truncates at roughly 100 characters on a phone, and the roofer line's payoff is in its second half. The two-sided version lands its first sentence intact. The roofer line stays where it works best: in the room, and in the hero. If Noah prefers the roofer line anyway, it's a one-line swap.

**Head snippet (paste-ready, fill the two URLs):**

```html
<title>Interconnected: your church, connected every day of the week</title>
<meta name="description" content="A private, invitation-only network for one church. Members find each other's skills, gifts, and needs during the week. Leaders finally see what the body can do.">
<meta name="theme-color" content="[primary brand background hex]">

<meta property="og:site_name" content="Interconnected">
<meta property="og:type" content="website">
<meta property="og:url" content="[canonical site URL]">
<meta property="og:title" content="Interconnected: your church, connected every day of the week">
<meta property="og:description" content="A private, invitation-only network for one church. Members find each other's skills, gifts, and needs during the week. Leaders finally see what the body can do.">
<meta property="og:image" content="[canonical site URL]/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Interconnected. Your church, connected every day of the week.">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Interconnected: your church, connected every day of the week">
<meta name="twitter:description" content="A private, invitation-only network for one church. Members find each other's skills, gifts, and needs during the week. Leaders finally see what the body can do.">
<meta name="twitter:image" content="[canonical site URL]/og-image.png">

<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

Note on the single-file site: because the site and demo live in one HTML file, one set of tags covers every link we send. If the demo ever moves to its own URL, tell me and I'll write a second set.

---

## 2. Preview card creative direction (`og-image.png`)

**Canvas:** 1200 × 630 px, PNG, under 300 KB. Export at 2× if the tooling allows and downsample.

**Composition: mark, wordmark, tagline. Nothing else.**
- Centered, and everything important inside the **center 630 × 630 square**. WhatsApp and some iMessage layouts crop the preview to a square; if the wordmark is off-center it gets chopped.
- Layout, top to bottom, vertically centered as a group: the gathered dot-cross mark (roughly 140 px tall) → wordmark "Interconnected" (the site's display face, roughly 72 px) → tagline "Your church, connected every day of the week" (body face, roughly 36 px, sentence case).
- Minimum text size on this canvas is 32 px. Previews render at thumbnail size; anything smaller turns to fuzz.

**Palette and type:** use the site's existing CSS variables and font stack exactly as they are on the landing page. Solid primary brand background, mark and wordmark in the accent, tagline in the secondary text color. No gradients, no photography, no phone screenshot. A phone screenshot at thumbnail size reads as generic SaaS and the UI text is illegible; a clean mark reads as a real company.

**Do not include:** stats, numbers, "pre-product," church names, competitor names, sample-data screenshots, emoji, the word "demo." The card is a badge, not a pitch.

**Build path suggestion:** lay it out as a 1200 × 630 HTML block using the site's own CSS, screenshot at 1× and 2×, export PNG. That guarantees it matches the live site without a design tool.

---

## 3. Favicon spec

**The mark:** the gathered dot-cross, mark only, no wordmark at any size. The wordmark never survives 16 px.

**Deliverables:**

| File | Size | Notes |
|---|---|---|
| `favicon.svg` | vector | Modern browsers. Transparent background. Include a dark-mode variant inside the SVG via `@media (prefers-color-scheme: dark)` so the mark stays visible on dark tabs. |
| `favicon.ico` | 32 × 32 and 16 × 16 in one file | Legacy fallback. |
| `apple-touch-icon.png` | 180 × 180 | **Solid brand background, no transparency.** iOS fills transparent areas with black and rounds the corners itself. Center the mark at about 60% of the canvas so it clears the corner radius. This is also the icon a pastor sees if they add the site to their home screen, so it matters more than the browser tab does for our audience. |
| `icon-192.png`, `icon-512.png` | 192 and 512 | Optional now. Only needed if we ever ship a web manifest. Skip unless it's free. |

**Legibility rule for small sizes:** test the mark at 16 px. If the dots merge into a blob, produce a simplified small-size variant: fewer dots or thicker dots, same silhouette. Do not add a letter "I" or any text to rescue it. Same mark family, tuned for size, is normal practice and stays on-brand.

**Brand canon note (for the guidelines one-pager later):** the dot-cross is name-independent and settled. Nothing in this handoff changes it.

---

## 4. Deploy notes for Dex

- All files at the site root so relative paths resolve on GitHub Pages: `/og-image.png`, `/favicon.svg`, `/favicon.ico`, `/apple-touch-icon.png`.
- Commit the assets in the same push as the head tags so the first crawl finds both.
- Messaging apps cache previews aggressively. After deploy, expect iMessage to keep showing the old bare-link preview for any thread where the link was already sent. New sends show the new card. Mack's checklist covers this.

---

## 5. Verification checklist for Mack (IT Manager), after deploy

1. Open the site in a fresh browser tab: favicon renders in light and dark tab themes.
2. iPhone Safari → Share → Add to Home Screen: solid-background icon, no black corners.
3. Text the link to yourself in **iMessage** from a thread where it was never sent before: mark, "Interconnected," tagline visible; image not cropped off-center.
4. Send in **WhatsApp**: check the square crop keeps the wordmark whole.
5. Post in **Slack** (any private channel): title, description, and image all populate.
6. Paste in a **LinkedIn** post draft (don't publish): pastors and investors both live there. Use LinkedIn's Post Inspector to force a re-crawl if it shows stale.
7. Run the URL through the Facebook Sharing Debugger and opengraph.xyz once to clear caches and confirm no missing-tag warnings.
8. Report back which of the four surfaces looked right and screenshot any that didn't. I'll adjust copy or crop from there.

---

## 6. What I need back
- Dex: the final canonical URL and the primary background hex you used (for the brand guidelines one-pager).
- Noah: a yes on the two-sided description, or "use the roofer line."
- Mack: the screenshots from §5.
