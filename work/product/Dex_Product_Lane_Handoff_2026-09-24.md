# Interconnected — Product Lane: Full Handoff (System Migration)
**Prepared by:** Dex (Product lane) · **Date:** Wednesday, September 24, 2026
**For:** the agent taking over product. Assume you have the current `index.html` and nothing else — no chat history, no prior briefs. This file is self-contained and supersedes `Dex_Handoff_to_Buford_2026-08-24.md` and `Dex_Changelog_v3_2026-08-24.md` (both remain in the project as history).
**Verified against:** the live GitHub repo on Sep 24, 2026. Every claim about the current file was checked against the deployed source, not recalled.

---

## 0. What this lane is

You are **Dex, Head of Product Development** at **Interconnected**, a private, invitation-only community platform — one siloed network per church, where members discover each other's skills, gifts, and needs during the week. Churches pay annually ($4,500–$12,000+/yr by size, drafted not validated); members always join free. Stage: pre-product, prototype-proven, pastor-feedback outreach in progress (see the BD lane's `Sonny_BD_Lane_Handoff_2026-09-24.md`).

You own: the demo site/file (the company's primary asset), the eventual technical spec and MVP, and technical evaluation of co-founder candidates (Pearl sources them; you evaluate spec comprehension, stack opinions, portfolio quality; Noah decides with Buford's recommendation).

You report to **Buford** (Co-CEO, home base) and **Noah** (Founder & CEO, final say, non-technical, product-minded, prefers honest pushback over validation, decides fast, works from his phone — keep deliverables concise). Lanes cannot talk to each other; Noah carries files. **Write every output for cold handoff.** Peers: June (marketing/brand), Sonny (BD), Pearl (fundraising/co-founder), Mack (IT/domains/hosting), Ada (legal), Gus (CFO).

**The vision test for every feature: member-complete, not staff-complete.** If a member needs it during their week, it belongs. If it's a staff workflow (volunteer scheduling, check-ins, giving administration, kids registration), it stays out until the member is won. The member's church life through the app: find/offer help (feed) · find people (search) · belong to something smaller (groups) · talk privately (messages) · know what's happening (church page: announcements, events, calendar) · know who leads (leadership directory). The core bet: trust already exists in a congregation; we build rails for it. The pastor is the distribution channel (Launch Sunday solves cold-start).

## 1. Current state — what is live

- **Live site:** https://www.joininterconnected.com (GitHub Pages, HTTPS via Pages cert).
- **Repo:** `noahaustin15/interconnected-demo`. **The repo is the canonical source of the current file** — always pull it before editing; never rebuild from scratch or from an old copy.
- **Current commit:** `8335d29d0dac3d946b346d0074cfd4f877009b56`, Aug 26, 2026 17:51 UTC ("Add files via upload"). No commits since.
- **Files at repo root (all required):** `index.html` (280,443 bytes, md5 `312be94d3c73796bf83e0bc5c1648099`) · `og-image.png` (1200×630 link-preview card) · `favicon.svg` (size-tuned 13-dot cross with dark-mode variant) · `favicon.ico` (16+32) · `apple-touch-icon.png` (180, solid brand blue) · `CNAME` (do not delete — it binds the custom domain).
- **A copy of the current `index.html` accompanies this handoff** so home base holds the file directly; it is byte-identical to the repo at the commit above.
- **One self-contained HTML file**: landing page + interactive member app demo (phone frame) + interactive admin dashboard demo (browser frame), all inline CSS/JS. No build step, no backend, no external JS. The **only** external resource is the Google Fonts Inter stylesheet. No localStorage/sessionStorage — all state is in-memory JS and resets on refresh (fine for a demo; the file gets opened in unpredictable viewers and must keep working offline apart from the font).
- **No analytics of any kind** are installed (deliberately — see §6).

**Deploy workflow (Noah does this himself):** download file → rename to exactly `index.html` — **Windows hides extensions; he has shipped `index.html.html` before, warn every time** → delete old `index.html` in the repo → upload → commit → wait for the green check → hard refresh / incognito to verify. Old version stays live during failed deploys. GitHub 503 deploy errors are usually GitHub-side ("Re-run failed jobs" later, not file changes). If other root assets change, they go **in the same commit**. DNS lives at Squarespace Domains: four A records to GitHub IPs + `www` CNAME to `noahaustin15.github.io`, and **Google Workspace MX/TXT records live in the same DNS — never suggest touching them**. Domain work is Mack's lane. Company email `noah@joininterconnected.com` works and is wired into the site.

## 2. What is in the file (site map, then internals)

### Landing page (the "v3" redesign, approved and shipped Aug 24–26)
Order of sections (ids in parentheses):
1. Sticky nav — logo, links (For members / Church leaders / How it launches / FAQ), **Request a pilot** button → opens the pilot form modal.
2. **Hero** (`member-demo`) — headline is the tagline; lede: "A private app for one congregation… The church directory, the bulletin board, and the group text — in one place, for your church only." The **live phone demo sits in the hero** (scaled 88% on desktop). Splash screen button is **"Take the tour"** → starts the 9-step guided tour; small secondary link goes to account-creation onboarding. Backdrop: soft blue gradient with a three-layer drifting dot field (14/18/22s cycles, ~60–70px travel, honors `prefers-reduced-motion`), fading out before the next section.
3. **Feature tour** (`features`, gray) — "One app for a member's whole church life." Four alternating rows, each with copy + a static screen crop built from the app's own components: **Church page · Groups · Feed · Search & messages**. Every crop and its "Try it in the live demo" button calls `demoJump(kind)`, which scrolls to the hero phone, dismisses onboarding, opens that exact screen, and pulses the glow. The crops are doors into the one real demo, not mini-apps.
4. **Story strip** (`story`, white) — "Someone at church needs a roofer. Someone at church *is* one." Three real cards: Rachel posts → Marcus answers (James vouches) → marked as helped.
5. **Leadership** (`admin-demo`, gray) — "Members get community. The church gets stewardship." The live admin dashboard in a browser frame, then `#insights`: "Know your church like never before," four rows of **real Insights panels** (Year in Review + integration funnel · gifts census + community health · member map + growth geography · care signals + group gaps), each clickable via `demoJump('admin:insights')`. Closing line: all insights aggregate; private messages and confidential circles never visible to anyone, including us.
6. **Privacy & trust** (`trust`, navy) — six cards, 3×2.
7. **How it launches** (`how`, white) — three numbered steps; pricing is a plain-text line ("Churches subscribe annually. Members always join free."), deliberately not boxed.
8. **FAQ** (`faq`, gray) — six accordions including the honest "Where is this today?" (prototype stage).
9. **Pilot CTA** (`pilot`, blue) + footer.

**Request a pilot** (nav + CTA): in-page modal form (church, name, role, email, congregation size, note) → builds a complete prefilled email to noah@ and hands off to the visitor's mail app → then shows a fallback screen with the full request text, a Copy button, and "Open email app again." **Nothing is captured server-side; a request only arrives if the visitor actually sends the email** (see §6 for the form-service option).

### Member app demo (phone frame)
Onboarding: church-code splash ("Invited by Grace Community Church") → optional account creation + profile setup (occupation, city/ZIP, age, campus, skills, offerings) → 3 tutorial screens (skippable). No forced actions. Five tabs + floating messages:
- **Feed** — toggle chips (Main Feed + joined groups) blended into one scroll; composer with four categories (Request / Offering / Question / Announcement); threaded comments; anonymous report via ⋯; resolved posts show "Marked as helped." **No "I can help" buttons, no skill-match banners, no algorithm** (all deliberate — see decision log).
- **Groups** — My Groups / Available; "Start a new group" (name, description, **icon picker**, accent color, Open / Request-to-join / **Confidential circle**); creator becomes leader instantly, no admin approval. Tapping a joined group opens its **headquarters**: `Feed · Resources · Events` segments, header with leader + meeting rhythm. Resources: pinned section, typed file cards (PDF/doc/sheet/slides/link — all inline SVG icons), add-resource flow whose file picker reads **name and size only, nothing uploads**; one rendered document preview (the James study guide). Leader Tools: approve/decline join requests, pin/remove resources, add group events (they land on every member's calendar). Unjoined groups open a preview sheet (never a member list). Wednesday Small Group is the showcase HQ; the demo user is a member.
- **Search** — live search by name/skill/occupation → member profile sheet → Message.
- **Church** — banner with service times/campuses, Give button (toast placeholder — we never handle payments), announcements (latest 2 + See all), **month calendar** (April 2026, dots colored by group accent, tap-a-day, one-tap RSVP), **Ministries at Grace** tile grid driven by the Official badge, leadership directory with Message buttons, church resources, visit & contact card.
- **Profile** — about, skills, offerings, spiritual gifts, working privacy toggles (directory visibility, who can message).
- **Messages** — floating icon, unread badge, sendable threads, framed as private/encrypted, never admin-visible.
- Extras: 9-step guided tour (roofer story → groups → **group HQ resources** → search → church → messages → points at admin dashboard); simulated push notification after onboarding or tour end; avatars are fully embedded deterministic SVGs (never external image services).

### Admin dashboard demo (browser frame, navy sidebar)
Fixed-height frame (680px) — **the main pane scrolls internally** so long views like Insights don't stretch the page. Six views, cross-demo state shared with the member app (badge a group Official → it appears on the member Church page; publish an announcement or calendar event → it lands on the phone; approve Pickleball → members can join it — **keep this cross-demo wiring in every future feature**):
- **Dashboard** — stat cards (348/487 weekly active, posts, needs resolved, connections), 8-week chart, activity feed.
- **Insights** (why the church pays) — Year in Review banner (347 needs met, **8** groups started by members, 1,204 connections, 78% monthly active, Download slides) · integration funnel · group gap analysis with "Nudge a launch" · life stage + age · campus + growth geography (Kyle +14) · member map (ZIP-area SVG, never addresses) · gifts & skills census · needs posted vs resolved · **pastoral care signals** (the one individual-level panel — activity dates only, never content; wording deliberately avoids implying attendance tracking) · aggregate-only privacy strip.
- **Moderation** — anonymous report queue, one-tap Dismiss / Warn / Remove / Escalate, celebratory empty state.
- **Groups** — church storage meter (aggregate only) · "New this week" review (Make official ministry / Looks good / Remove — no approval queue) · full roster with resource/event counts. Confidential circles show "members, posts, files, and events are never visible to admins"; Manage is disabled for them.
- **Members** — roster + invite (toast).
- **Announcements & calendar** — announcement composer and an add-event form, both publishing live into the member app.

### Internals a future editor must know
- Data lives in top-of-script structures: `GROUPS`, `PEOPLE`, `POSTS`, `CONVOS`, `AVATARS`, `GROUP_ACCENT`, `GROUP_LEADERS`, `GROUP_ICON`/`GICON`, `OFFICIAL` (a mutable Set), `ICONS` (SVG map), `EVENTS`, `RESOURCES`, `ANNOUNCEMENTS`, `STAFF`, `ME`, `TOUR`, `CHURCH`, `REPORTS`. Sheets render through one dispatcher `openSheet(kind, arg, arg2)`; admin views through `adminGo/renderAdmin`; landing→demo jumps through `demoJump(kind)` (`'church' | 'groups' | 'feed' | 'people' | 'admin:<view>'`).
- **`DEMO_TODAY = "2026-04-15"`** (a Wednesday). The demo world is deliberately anchored there — posts, events, and the calendar all agree with it; the calendar must never use the real clock. Weekly events (Sunday worship, Wednesday small group) are expanded ~6 weeks from seed entries at init.
- **The confidential gate:** `canSee(g)` (member side) and `adminCanSee(g)` (admin side) guard every render path that touches a group's posts, files, events, or members. **Never add a second code path around them.** Two planted test cases exist to prove the gate: Recovering & Renewed's Thursday meeting in `EVENTS` and two R&R files in `RESOURCES` — if either ever renders for the demo user or in admin, the gate is broken.
- Escape user input with `esc()`. Every icon is inline Feather-style SVG.
- **Provenance note:** the v3 landing page was generated by builder scripts in a session workspace that has since been recycled. Those scripts are gone and are not needed — **the live `index.html` is the single source of truth; edit it directly.**

### QA checklist before any delivery (run all of it)
Desktop + 390px phone width, no horizontal overflow · all 5 tabs + messages · full 9-step tour from the splash button · pilot form end-to-end (send + fallback screen) · every `demoJump` target · admin ↔ member cross-state (Official badge → church page; admin event → phone calendar) · the two confidential test cases · admin pane scrolls internally without growing the page · scan for non-SVG glyphs/emoji (the ✕ close glyph is the one allowed character) · zero occurrences of "Interconnect" without "-ed" and zero of the former name ("Believers In Business") · only external reference is fonts.googleapis.com · JS parses clean. Then repeat the deploy instructions to Noah, every time.

## 3. Brand system (locked — June owns changes, not you)
- **Name:** Interconnected. Tagline: "Your church, connected every day of the week." **Naming flag for home base:** June's Aug 24 handoff recorded "Name: Interconnected, confirmed by Noah," and the OG/favicon assets are baked with it; the BD lane's Sep 24 handoff still describes a pending rename to "Interconnect" awaiting Legal/IT. These can't both be current — **get one sentence from Noah and log it.** Nothing in the file hardcodes "Interconnect."
- **Logo:** the "gathered dot-cross" (many dots forming a Latin cross). The rendered SVGs in the file are canonical (five placements with per-background palettes). The favicon uses a simplified 13-dot variant tuned for 16px — same silhouette, deliberate, per June's small-size rule.
- **Colors:** primary blue `#2563EB`; neutrals white/`#F3F4F6`/`#6B7280`/`#1F2937`; navy `#0F1B33`; categories amber Requests / green `#059669` Offerings / violet `#7C3AED` Questions / blue Announcements; per-group accents in `GROUP_ACCENT`. **Typography:** Inter. **Light mode only** — `color-scheme: light only` plus meta tags stop mobile auto-inversion; do not remove.
- **Absolutely no emojis anywhere** (a real cross-platform rendering bug plus a professionalism directive). Group tiles use per-group line icons (this replaced letter monograms on Noah's authority, Aug 24 — June's guidelines should reflect it; verify against `June_Brand_Guidelines_v1.md`).
- **Faith-forward warmth is deliberate** (came from "too techy" feedback): "Built by believers, for the local church," "No ads. No algorithms. Just the Body, connected," 1 Peter 4:10 in the CTA, "Connecting the Body of Christ" in the footer. Preserve it.
- Sample-data world: fictional **Grace Community Church**, ~487 members, South Austin / Buda / Kyle / Manchaca geography (matches Noah's real outreach territory), ~16 recurring personas with embedded SVG avatars. Canonical demo moment: **Rachel needs a roofer → Marcus answers → marked as helped** (used in the tour and every pitch). Keep the professional/communal balance (roofer and financial planning alongside meal trains, borrowed trucks, garden veggies). Say "sample data" out loud in demos.

## 4. Decision log — complete, do not relitigate without new information

Founding decisions (pre-Aug 24):
| Decision | Rationale |
|---|---|
| Member-complete, not staff-complete | The vision test for all features. Member weekday needs belong; staff workflows don't (yet). |
| No reputation scores / gamification | Trust is pre-established in a church; rankings would poison culture. |
| No algorithmic feed | Members choose toggles. Platform doesn't farm attention. |
| Mentorship removed as a feature | Matching makes mentorship transactional; it emerges via posts/groups. |
| Groups member-created, admin oversight only | Mirrors real church life; admins badge "Official" or remove, never approve. Replaced an earlier admin-approval design at Noah's direction. |
| No pressure mechanics | "3 needs match your skills" banner was built and removed — "I don't want to pressure people into helping." |
| Insights aggregate-only (one scoped exception below) | The trust brand collapses if leadership can see private content. |
| Emoji-free, icon-based UI | Professionalism directive + a real tofu-rendering bug. |
| Mobile app first, web for admins | Members live on phones; admins prefer desktop. |
| AI moderation rejected | Cost-unrealistic; community reporting + human judgment fits culture. |
| Honest FAQ about prototype stage | Feedback mode with pastors; no bait-and-switch. |
| Groups as headquarters | Files/resources make groups a home, not a feed; ministry-level switching costs are the moat. |

Aug 24–26 decisions (Noah, with Dex recommendations accepted unless noted):
| Decision | Rationale |
|---|---|
| Calendar scope = church-wide + groups you've joined; anchored to fixed `DEMO_TODAY`, never the real clock | Keeps the calendar personal; privacy holds by construction; a live clock would show an empty month as time passes. |
| Confidential circles are listed in the Ministries directory (existence visible; membership, posts, files, events never) | A recovery group's whole problem is being found by the person who needs it. |
| Confidential enforcement is one flag + one gate function on every render path, with planted test cases | No second code path means no second way to leak. |
| Any member can add group resources; leaders pin/remove | Mirrors the feed and the member-led decision; a Bible study is people sharing notes, not a leader broadcasting. |
| Storage quotas are per church, never per member | "Members always join free" must hold; flagged to Gus for pricing (his note is in `Dex_Plan_ChurchPage_GroupsHQ.md` §C). |
| Splash button is "Take the tour" (tour-first, small account-creation escape link) | Noah: every visitor should be taken through the tour. |
| Per-group line icons replace letter monograms | Noah: tiles blended together; wants at-a-glance identity. Brand-system change on his authority. |
| Landing page leads with concrete product: plain-language lede, real screen crops, roofer story | Cold visitors couldn't tell what the app was. The "directory / bulletin board / group text" comparison line is doing the heavy lifting — June to ratify as standing positioning. |
| Every landing crop is a door into the one live demo (`demoJump`), not a standalone mini-app | The demo is single-instance; a visitor should play with the full app, and everything they touch is what Noah shows in person. |
| "Why churches subscribe" shows real Insights panels, not text cards | Same principle: show, don't describe. |
| Admin frame is fixed-height with internal scroll | Opening Insights must not stretch the whole page. |
| Pilot CTA is an in-page form → prefilled email + copy fallback | A bare mailto silently does nothing on desktops without a mail client; the one conversion path must never dead-end. |
| Volunteer sign-up module refused | Staff workflow; fails the member-complete test. Serve Day RSVP covers the member side. |
| Give button is a deep-link placeholder only | We never handle payments; it answers "does it do giving?" correctly — we don't replace the provider. |
| Sample-data honesty fixes | Care-signal line no longer implies attendance tracking (we collect none); Year in Review says 8 member-started groups to match the roster. |
| Traffic analytics **paused** by Noah | Recommendation on file (see §6); no database needed; revisit when he says go. |
| Tour is 9 steps (added group-HQ step) | The moat thesis belongs in the pitch. |
| Care signals stay individual-level but metadata-only, and we say so precisely | The honest sentence: "Every insight is aggregate except one — quiet-member care signals — and that one uses activity dates only, never content." Never claim 100% aggregate. |

**Feedback governance:** collect feedback, act on patterns (3+ people), treat single opinions as taste unless strategically compelling. Noah's wife vetoes on taste (her bar: "premium, not busy"). His brother-in-law drove the church-warmth direction.

## 5. Known limits — never let Noah claim more than the screen shows

The authoritative list is `claude/Dex_Demo_Inventory_for_Sonny.md` (do-not-overclaim table, per-panel Insights inventory, member-side inventory). Headlines: the Launch Sunday kit, weekly digests, encrypted messaging, church branding controls, and the effect of privacy toggles are **promises/roadmap, not screens**. Many buttons are confirmation toasts only (Check in, Nudge a launch, Download slides, Invite, Manage, Give, Directions, file Open/Share). There is no way for a member to mark their own post as helped (only seeded). "Half the congregation joins in the first weeks" is an expectation, never a statistic. No attendance, check-in, giving, or kids data exists anywhere. Pilot-form requests arrive only if the visitor's email actually sends. Technical: no backend, state resets on refresh, storage/file uploads are simulated (names and sizes only), the demo world is fixed in April 2026 by design.

Watch items: Noah once saw a hairline at the phone's right edge in his browser (never reproduced in QA; a bezel-colored ring now covers sub-pixel gaps — if it recurs, the next step is sizing the hero phone natively instead of `transform: scale`). Dot-field motion was turned up at his request; his wife's "premium, not busy" bar applies if it reads busy. All landing copy is Dex-written; June's pass was requested Aug 24 and is **not confirmed done** — check `June_Brand_Guidelines_v1.md` and ask.

## 6. In flight / awaiting decisions

1. **Naming:** resolve the Interconnected-vs-Interconnect discrepancy (see §3) and log it at home base. If the rename ever lands: retitle/OG tags, regenerate `og-image.png`, coordinate with Mack (domain) and June (rollout). Nothing else in the file is name-sensitive.
2. **June's copy pass** on the v3 landing page (hero lede, tour rows, Insights rows, trust/launch intros, pilot form) — requested, unconfirmed. She also decides whether "the church directory, the bulletin board, and the group text" becomes standing positioning.
3. **Mack's link-preview verification** (fresh iMessage thread, WhatsApp square crop, Slack, LinkedIn Post Inspector, Facebook Sharing Debugger) — assets shipped Aug 24; checklist completion never confirmed.
4. **Form service for pilot requests** (Formspree/Netlify-class): removes the mail-app dependency so requests arrive even if the visitor never hits send. Mack creates the account; one small edit wires it in. Recommended; not yet decided.
5. **Analytics (paused by Noah, recommendation standing):** privacy-first cookieless analytics (Plausible/Fathom-class; GA is off-brand for "no ads, no algorithms"), async and fail-silent to preserve offline behavior; per-recipient `?ref=` links so outreach knows *who* visited (strip the tag client-side after read); five behavior events (tour started, tour completed, admin viewed, Insights opened, pilot form opened/sent). No database needed. Fits Sonny's one-thread-per-church model. Ada supplies one honest footer sentence when it ships.
6. **Community-standards step at signup** — the FAQ claims it; onboarding lacks it; cheap to add.
7. **Formal standalone technical spec** (for co-founder recruiting; expect Pearl to trigger this). Direction on record: React Native · Node/Express · PostgreSQL · JWT · Socket.io/Firebase · AWS or GCP; mobile app first, admin web second. Data-model sketches for Events/RSVPs/Resources and the confidential-storage isolation rule (separate prefix + key per church; analytics ETL excludes confidential groups in code with tests) are in `Dex_Plan_ChurchPage_GroupsHQ.md` §D.

## 7. Backlog, in priority order

1. Whatever pastor feedback generates once meetings happen (triage every request against the §4 decision log; the BD lane logs objections verbatim).
2. Form service for pilot requests (small, high value — the site's only conversion path).
3. Analytics + `?ref=` links (on Noah's go).
4. Community-standards step at signup.
5. Technical spec document (rises to #1 the moment a co-founder candidate is real).
6. Possible entry gate on the site (Noah prefers in-person demos; a curious pastor finding the public site is known and accepted).
7. Designed dark mode (deliberately deferred; light-only is a decision, not an accident).
8. Known future front-door additions, logged but **not to be built unprompted:** Give deep-link wired to a real provider · embedded sermon media (embed-only — video hosting is the storage cost bomb; Gus's note) · prayer requests (likely just a post category).

## 8. Where everything lives

- **The live file:** repo `noahaustin15/interconnected-demo` @ `8335d29` (+ a byte-identical copy delivered with this handoff).
- **Project docs (claude.ai project "InterConnected"):** `claude/Dex_Plan_ChurchPage_GroupsHQ.md` (approved feature plan; Gus storage note §C; spec notes §D) · `claude/Dex_Demo_Inventory_for_Sonny.md` (authoritative product inventory + do-not-overclaim list) · `claude/Dex_Reply_to_June_OG_Favicon.md` (link-preview/favicon implementation record) · `claude/Dex_Handoff_to_Buford_2026-08-24.md` and `claude/Dex_Changelog_v3_2026-08-24.md` (history; superseded by this file) · June's `June_Brand_Guidelines_v1.md` / `.docx` · Sonny's lane files (see his §13) · `Believers_In_Business_Plan_v3.docx` (original plan under the former company name — the old name appears nowhere in the product).
- **Gone and not needed:** all prior session workspaces (builder scripts, QA scripts, intermediate v1/v2 files). The repo + this project are the durable record.

## 9. What "good" looks like in this lane

Fast, surgical edits to one big file; a plan proposed before any large build; visual QA (screenshots at phone and desktop widths) before every delivery; every change consistent with the brand system, the decision log, and the member-complete test; cross-demo state kept alive; the confidential gate never bypassed; deployment instructions repeated with every shipped file; outputs written for cold handoff; and honest pushback when a request conflicts with an established principle — Noah expects it and respects it.
