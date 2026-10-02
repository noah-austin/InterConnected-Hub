# Dex → Buford · Product handoff
**Date:** Aug 24, 2026 · **From:** Dex (Head of Product Development) · **To:** Buford (Co-CEO, home base) · **Approved by:** Noah
**Live site:** www.joininterconnected.com · **Current file:** `index.html` v3 (self-contained, ~270 KB) · **Repo:** noahaustin15/interconnected-demo

---

## 1. What shipped today (all live)

**Both §3 mandates, in the demo**
- **Expanded church page:** real month calendar (dots by group, tap-a-day, RSVP), "Ministries at Grace" tile grid driven by the Official badge, service times and campuses, Give button (placeholder — we never handle payments), Message buttons on leadership, church resources, visit & contact card. Admin can add events from the Announcements view and they land on the phone.
- **Groups as headquarters:** every group sheet is Feed · Resources · Events. Members add files (picker reads name/size only; nothing stored). Leaders pin/remove, approve requests, add group events. Wednesday Small Group is the showcase (James study guide, notes, chili sign-up). Confidential circles are a real flag with one visibility gate — their posts, files, events, members never render outside the circle or in admin; two planted test cases verify it every build.
- Per-group line icons (replaces letter monograms — brand-system change on Noah's authority; June to log).

**Site redesign (v3)** — replaced the old landing page
- Live phone demo sits in the hero; splash button is "Take the tour" (9 steps); dot-field backdrop with slow drift.
- "One app for a member's whole church life": four rows (Church page · Groups · Feed · Search & messages) with real screen crops. **Every crop and its button opens that exact screen in the live demo.**
- Roofer story strip; leadership section with admin demo; "Why churches subscribe" now shows the real Insights panels (Year in Review/funnel · gifts census/health · member map/growth · care signals/gaps), also clickable into the dashboard.
- Trust (3×2), How it launches (plain pricing line), FAQ, pilot CTA.
- **Request a pilot** is now an in-page form → prefilled email to noah@ with a copy-fallback for devices with no mail app. (Previously a bare mailto that silently failed on many desktops.)
- Admin frame fixed height with internal scroll; sample-data fixes (care-signal wording no longer implies attendance; Year in Review says 8 groups to match roster).

**Link previews + favicon (June's handoff)** — implemented. Head tags per her spec, `og-image.png` 1200×630, `favicon.svg` (size-tuned 13-dot cross, dark-mode variant), `favicon.ico`, `apple-touch-icon.png`. Assets at repo root. Canonical URL `https://www.joininterconnected.com/`; theme-color `#F7FAFF`; card background `#2563EB`. Two-sided description used (Noah can swap to the roofer line).

## 2. Decisions made today (log these)
| Decision | Owner |
|---|---|
| Name stays **Interconnected**; OG/favicon assets baked with it (per June's handoff, "confirmed by Noah Aug 24"). If the rename is still alive, say so — assets are a 5-minute regenerate. | Noah |
| Group tiles use icons, not letter monograms | Noah (brand change) |
| Calendar scope = church-wide + groups you've joined; confidential circles listed in Ministries (existence visible, membership never) | Noah (accepted Dex recs) |
| Any member can add group resources; leaders pin/remove | Noah |
| Noah's demo persona is a member of Wednesday Small Group | Noah |
| Landing page: every product crop is a door into the live demo, not a standalone mini-app | Dex |
| Storage quotas are per church, never per member ("members always free" holds) | flagged for Gus |
| Traffic analytics: **paused** by Noah. Recommendation on file: privacy-first cookieless analytics + per-church `?ref=` links + five behavior events; no database needed | Noah |

## 3. Asks for other lanes (route via Noah)
- **June:** copy pass on everything Dex wrote — hero lede ("the church directory, the bulletin board, and the group text"), feature-tour and Insights row headlines/bullets, trust and launch intros, pilot-form copy. Decide whether the directory/bulletin/group-text comparison becomes standing positioning. Log the icon change in brand guidelines.
- **Mack:** run the §5 link-preview checklist from June's handoff (fresh iMessage thread, WhatsApp, Slack, LinkedIn Post Inspector, FB debugger). If Noah wants pilot requests to arrive without depending on a mail app, set up a form service (Formspree/Netlify Forms class); Dex wires it in one edit.
- **Gus:** storage is the first usage-based cost — note in `Dex_Plan_ChurchPage_GroupsHQ.md` §C (per-church quotas by tier, file-size cap, video by link only, retention tiers, rough cloud cost magnitudes to verify).
- **Sonny:** `Dex_Demo_Inventory_for_Sonny.md` is current except: the pilot CTA is now a form (better for outreach copy: "request a pilot in 60 seconds on the site"), and the landing page now shows real screens so the "what is it" problem for cold visitors is addressed. The do-not-overclaim list still stands; care signals remain the one individual-level panel.
- **Ada:** nothing blocking. When analytics resumes, one honest sentence about cookieless analytics for the footer/FAQ.

## 4. Known limits / watch items
- Pilot requests still travel by the visitor's own email; nothing is captured server-side.
- Noah saw a hairline at the phone's right edge in his browser that doesn't reproduce here; a bezel-colored ring now covers sub-pixel gaps. If it persists on his machine, next step is sizing the hero phone natively instead of via transform.
- Dot drift was turned up at Noah's request; taste check against the "premium, not busy" bar is his wife's call.
- Landing copy is Dex-written and unreviewed by Marketing.

## 5. Backlog (unchanged priority order)
1. Analytics + `?ref=` links (paused)
2. Form service for pilot requests
3. Community-standards step at signup (site claims it; demo lacks it — cheap)
4. Standalone technical spec (co-founder recruiting)
5. Designed dark mode (deferred)

## 6. Files in the project
`Dex_Plan_ChurchPage_GroupsHQ.md` · `Dex_Demo_Inventory_for_Sonny.md` · `Dex_Reply_to_June_OG_Favicon.md` · `Dex_Changelog_v3_2026-08-24.md` · this handoff. Deploy bundle (5 files) delivered to Noah in chat.
