# Implementation Plan — Expanded Church Page + Groups as Headquarters

**From:** Dex (Product) · **To:** Noah / home base · **Status:** PROPOSAL — no edits made to the file
**Source of truth:** `Interconnected_Website_and_Demo.html` (1,883 lines, verified current)

---

## 0. What I found in the file (so the plan is grounded)

- **Church tab** (`renderChurch()`): hero → 3 announcements → 4 events with RSVP (`EVENTS[]`, index-based `toggleRsvp(i)`) → 4 staff cards. No calendar, no groups, no service times, no contact info.
- **Events** are stored as `{d:"18", m:"APR", name, sub, going}` — display strings, not dates. A month view needs real dates, so the data model changes (backward-compatible; RSVP keeps working).
- **Groups** open via `openSheet('sheet-group')` → `renderGroupFeed()`: header + Leader Tools + posts. That is the whole "home" today. Only *joined* groups open; non-joined cards have no tap target at all.
- **Official** is a mutable `OFFICIAL` set (admin "Make official ministry" adds to it). `markOfficial()`/`removeGroup()` re-render Groups and Feed but **not** Church — I'll wire that so cross-demo state stays shared.
- **Confidential** isn't a real flag yet — Recovering & Renewed is just `open:false` + a description. Guardrail (1) needs a real `confidential:true` flag and a single gate function.
- **Demo "today."** Posts and events already agree on a world date without saying so: Ruth's "Wednesday: James chapter 2" (6h ago), Beth's "Thursday meeting moved" (3h ago), Serve Day "Saturday, April 18," Sunday Worship on the 26th, New Member Lunch on Sunday May 3 — all consistent with **Wednesday, April 15, 2026**. The calendar will anchor there, not to the real clock (a live clock would show an empty August). One stray: David's "Tuesday evenings in **March**" — I'll change to **May** (one word) when I touch events.

---

## A. Expanded Church Page

### A1. Calendar (month view, integrated with events + RSVP)

**Build**
- Replace the "Upcoming events" list header with a **month grid** card: month title with ‹ › navigation, 7-column grid, dots on days with events (dot color = group accent; church-wide = blue), "today" ring on Apr 15.
- Tap a day → the list under the grid shows that day's events. Default (no day selected) shows the next 5 upcoming with "See all." Same event card + RSVP button you have now, so `toggleRsvp` and the "You're going to…" toast keep working (I'll switch from array index to event `id`).
- **Data:** `EVENTS` becomes `{id, date:"2026-04-18", time:"8:00 AM", place:"Main lobby", name, group:"main", going, recurring?}`. The `d`/`m` display is derived. Grow the seed from 4 events to ~12–14 across April–May so the month isn't empty: worship each Sunday, Wednesday Small Group (weekly), MIB Breakfast (Apr 22), Prayer Night (Apr 21), Young Professionals dinner (Apr 28), Seniors lunch (May 2), New Member Lunch (May 3), **Kyle launch-team info night (May 7)** — ties to the "Kyle, fastest growing" insight, Baptism Sunday at the lake (May 17), youth summer kickoff at Buda campus (May 24), and Beth's R&R Thursday meeting (Apr 16) which **must not appear** for Noah — it's the built-in privacy test case. Chris's basketball stays off the calendar on purpose ("if we get 10+ regulars I'll make it official") — that story line is good.
- **Group-scoped events**: giving events a `group` field is what lets the calendar respect privacy *and* lets each group HQ (Part B) show its own "Upcoming." One field serves both mandates.

**Where it lives:** Church tab, second section (after Announcements). No new tab, no segmented control — single scroll stays.

**Decisions for you**
1. **Calendar scope.** (a) church-wide only · **(b) church-wide + groups I've joined ← recommend** · (c) everything except confidential. (b) makes the calendar *mine*, and privacy holds by construction; discovery is the Ministries section's job, not the calendar's.
2. **Where do events come from?** Today nothing creates events. Options: (i) admin adds a small "Add to the church calendar" form inside the existing Announcements view — no new sidebar item, mirrors the announcement composer, and demonstrates cross-demo state (publish in admin → appears on the phone) ← **recommend**; (ii) leave events seed-only. Also: group leaders add group events from Leader Tools (member-led, on-brand) — I'd include it with Part B.
3. **Announcements length.** Keep all 3 stacked (calendar starts below the fold) or show latest 2 + "See all" so the calendar is visible sooner. I lean "latest 2 + See all."

**Decision-log check:** clean. Admin event entry is content input like announcements, not a staff workflow. I will **not** add volunteer scheduling — Pastor Mike's post says "sign up on the Church page," and the Serve Day RSVP already satisfies that; a volunteer module would fail the member-complete test.

### A2. Official ministries on the church page (discovery ramp)

**Build**
- New section **"Ministries at Grace"** between Calendar and Leadership: 2-column tile grid, one tile per group in `OFFICIAL` (so it's live — badge a group official in admin, it appears here; remove it, it disappears). Tile = monogram in accent color, name, member count, meeting rhythm (new `meets` field, e.g. "Wednesdays 6:30 PM"), and a state button: **Join** (open) / **Request** (closed) / **Joined** check.
- Tap a tile → joined: opens the group HQ; not joined: opens a new **group preview sheet** (description, leader, meets, Join/Request). This preview sheet is also wired to the Groups tab's Available list, fixing today's dead tap on non-joined cards.
- Confidential circle preview shows description + "Requests go only to the group leader. Membership is never shown." — no list, ever.

**Decisions for you**
4. **Include confidential circles in the ramp?** I say **yes** — a recovery group's whole problem is being found by the person who needs it; what's hidden is *who's in it*, not *that it exists*. Your call, since it's the trust brand.
5. **Show joined groups in the ramp** (as a "Joined" state) or only unjoined? I recommend showing all — it reads as the church's ministry directory rather than a sales rail, and week-one members see what they've already done.

**Decision-log check — one real tension.** "No pressure mechanics" and "no algorithmic feed." A ministries *directory* is fine; what would violate the log is a nag ("You haven't joined a group yet") or "Recommended for you" ranking. I'll build a neutral directory ordered by the church (official groups, in admin order), no personalization, no banners. The integration funnel *measures* week-one joins; the app doesn't *push* them.

### A3. "And more" — proposals for a member-complete church page

Argued against §2 (member-complete) and §8. Ranked by weekday value ÷ build cost.

| Proposal | Argument | Verdict |
|---|---|---|
| **Service times + campuses** in the hero ("Sundays 9 & 11 AM · South Austin · Buda · Online") | The most basic weekday question — "when and where" — and it's absent today. Onboarding already has the campus selector. | **Build.** ~10 lines. |
| **Visit & contact card** (address, phone, office email, office hours, "Message the office") at the bottom | Member need, zero staff workflow. Directions button opens a maps link — fine offline, it's just an href. | **Build.** Small. |
| **Message button on leadership cards** | Makes "know who leads" actionable via the existing `messagePerson()`. Staff get the same privacy toggles members have. | **Build**, unless you'd rather not imply pastors are DM-able by 487 people — tell me. |
| **Church resources** (bulletin, sermon notes, new-member guide) | Reuses Part B's resource component; the church page becomes the HQ of the main group. Member weekday need (sermon notes, bulletin). | **Build if Part B is approved** — it's ~20 extra lines once the component exists. |
| **Give button** (deep-link to existing provider) | On your known-future list; you said don't build unprompted, so I'm asking. It's a one-line button that toasts "Opens Grace Community's giving page." Pastors *will* ask "does it do giving?" and a deep-link answers correctly: we don't replace your provider. | **Your call.** Cheap; slightly invites a conversation you may not want in feedback mode. I'd include it. |
| Sermon media | Known-future, heavier, and it's the storage cost bomb (see Gus note) — embed links only, later. | Defer. |
| Prayer requests | Post category, not church page. | Defer (separate small item). |
| About / statement of faith | Low weekday utility; Sunday content. | Skip. |
| Volunteer sign-up module | Staff workflow; explicit §2 exclusion. | **No.** |

**Proposed Church tab order:** Hero (+service times) → Announcements → Calendar → Ministries at Grace → Leadership → Church resources (if B) → Visit & contact. Tell me if you want Calendar above Announcements.

---

## B. Groups as Headquarters

### B1. The HQ sheet

**Build** — `renderGroupFeed()` becomes `renderGroupHQ()`:
- **Header** grows one line: leader name and meeting rhythm ("Led by James & Ruth Carter · Wednesdays 6:30 PM at the Carters'").
- **Segmented control inside the sheet: Feed · Resources · Events.** Feed = today's posts (unchanged). Events = this group's calendar entries with RSVP (from A1's `group` field). Resources = the new thing.
- **Resources tab:** "Pinned by leader" block, then a list of resource cards — SVG type icon (document / spreadsheet / slides / link / audio — all added to `ICONS`, no emoji), title, who added it, when, size. Tap → a **preview sheet** for one or two hero files (e.g. the James study guide renders as a real-looking reading plan card), a "Opens in your phone's viewer" toast for the rest.
- **Add a resource:** button → sheet with title, type chips, optional note, and a real `<input type="file">` — we read only the filename and size from the picker, nothing uploads, nothing is stored. It feels real in a pastor's hands and costs nothing. Falls back to a typed title if they cancel the picker.
- **Leader Tools** gains: Pin / Remove on resources, and "Add an event" (writes to `EVENTS` with the group id → shows on the member's calendar).
- **Empty state** for groups you create: "No resources yet — add the first study guide, schedule, or sign-up sheet."

**Where it lives:** Groups tab → tap any joined group. Also reachable from the church page ministries tiles (A2).

**Seed data (Grace Community flavored)**
- *Wednesday Small Group* (the hero): "James — Study Guide, Weeks 1–8.pdf" (pinned), "Spring reading plan.pdf", "Chili night sign-up.xlsx", "Host & snack rotation — April/May.pdf", "Ruth's notes — James 2 (faith and works).docx", link: "Bible Project — James overview."
- *Men in Business*: "Biblical stewardship workbook.pdf", "Breakfast speaker schedule.pdf", "Member business directory.xlsx".
- *Young Professionals*: "Career & Calling reading list.pdf", "Summer socials calendar.pdf".
- *Recovering & Renewed*: two entries that exist in the data purely to prove the gate works — never rendered anywhere for Noah or in admin.

### B2. Confidential-circle guardrail (as rigorous as member lists)

- Add `confidential:true` to Recovering & Renewed (and expose it in the "Start a new group" sheet as a third option: Open / Request to join / **Confidential circle**).
- **One gate function** — `canSee(group)` — used by every render path that touches a group's posts, resources, events, or members: HQ sheet, calendar, ministries tiles, search, admin views. No second code path. Comment block at the top of the data section states the rule.
- **Admin:** Groups roster shows "Confidential circle — members, posts, and files are never visible to admins" on that row; Manage is disabled for it. Insights and the new storage stat never break out confidential groups by name.
- **Demo test:** Beth's Thursday meeting is in `EVENTS` with `group:"rr"`; two R&R files are in `RESOURCES`. If either ever renders for Noah or in admin, the gate is broken. I'll QA that specifically before delivery.

### B3. Admin dashboard implications (small, all cross-demo)

- Groups roster rows: "· 6 resources" for non-confidential groups; the confidential line above for R&R.
- New **Storage** panel in admin Groups: "Church storage: 1.4 GB of 25 GB · 63 files across your groups." (No group count — the roster shows 8 groups while Year in Review says 23; I'll leave that pre-existing mismatch alone unless you want it reconciled.) Aggregate only. It quietly plants storage as a plan feature, which Gus will want.
- Announcements view gets the "Add to the church calendar" form (if Decision 2 = yes).
- Dashboard activity feed gets one line: "Ruth Carter added 'Ruth's notes — James 2' to Wednesday Small Group."

**Decisions for you**
6. **Who can add resources?** (a) any member, leader pins/removes ← **recommend** — mirrors the feed and the member-led decision; a Bible study is people sharing notes, not a leader broadcasting · (b) leader only.
7. **Seed Noah into Wednesday Small Group?** Today he's in Men in Business and Young Professionals only; the brief asks for the *Bible study* to be the headquarters story. Cheapest honest fix: Noah is a member of Wednesday Small Group (joined, but its feed chip starts **off** so the default feed is unchanged), and its description drops "currently at capacity." MIB and YP get resources too so HQ isn't a one-group trick.
8. **Tour:** add one step (8 → 9) after Groups: "Groups are a home, not just a feed — the Wednesday study keeps its notes, reading plan, and sign-ups here, so there's nothing to juggle elsewhere." The tour is the pitch; the moat thesis should be in it. Yes/no?
9. **Preview fidelity:** one rendered "document" preview (the James study guide) + toasts for the rest ← recommend, or toasts only.
10. **Competitor names in-app copy.** The brief's rationale says "no GroupMe + Google Drive." I'd keep in-app copy generic ("nothing to juggle elsewhere") and let June decide if the landing page names names.

**Decision-log check**
- *Member-created, admin oversight only:* preserved — resources follow the same model; admins see non-confidential files but don't approve them.
- *Insights aggregate-only:* storage stat is a total; no file names in Insights, ever.
- *Members always free:* storage quotas are **per church, never per member** — flagging so the pricing model doesn't drift into member-side limits.
- *Emoji-free:* all file-type icons are inline SVG.
- *Naming:* nothing new hardcodes "Interconnect"; all new copy uses the existing brand string. Nothing here gets cheaper after the rename, so no timing dependency.

---

## C. Note for Gus (CFO) — storage cost implications (cold handoff)

Resources are the first cost that scales with **usage**, not seats. Things to price:

1. **Include a per-church storage quota by tier, plus an add-on** (placeholder shape to price, not a decision: e.g. 10 GB / 50 GB / 200 GB for small / mid / large). Per church, never per member.
2. **Cost drivers, rough public-cloud magnitudes (Gus to verify):** object storage is cheap — on the order of $0.02–0.03 per GB-month on S3 Standard; **egress** (members downloading) is the bigger line, on the order of $0.05–0.09 per GB, reduced by CDN caching. A church with 25 groups × 200 MB is ~5 GB → cents per month. Documents don't hurt us.
3. **Video and photo albums are the risk** (Grace Liu the photographer is in our own demo). Policy: per-file size cap (e.g. 25 MB), video by link only (YouTube/Vimeo embeds), photos compressed on upload. Sermon media, when it comes, is embedded from the church's existing host — never stored by us.
4. **Retention:** archive files of inactive groups to cold storage after N months (lifecycle rules) — real savings at scale.
5. **Confidential circles:** separate storage prefix/bucket + separate encryption key per church; small engineering cost, negligible run cost, but it's a line in the spec and a trust talking point.

Sources for the price magnitudes: [CloudZero S3 pricing guide (2026)](https://www.cloudzero.com/blog/s3-pricing/), [Infratally S3 pricing 2026](https://infratally.com/articles/aws-s3-pricing-explained-2026/), [Cloudchipr S3 pricing guide](https://cloudchipr.com/blog/amazon-s3-pricing-explained).

---

## D. Spec notes (for the eventual technical spec / co-founder conversations)

- `Event {id, church_id, group_id?, title, starts_at, ends_at?, location, recurrence?, visibility}` + `RSVP {event_id, member_id}`.
- `Resource {id, group_id, uploader_id, kind, name, size_bytes, storage_key, pinned, created_at}`; served via signed URLs issued only after a membership check.
- Confidential groups: `is_confidential` on Group; storage isolated by prefix and KMS key; analytics ETL excludes them **in code with tests**, not by convention.
- Storage metering per church feeds billing.

---

## E. Build order, sizing, and QA

- **Delivery 1 — Church Page (A1 + A2 + A3 approved items):** data model change for events, calendar, ministries tiles, group preview sheet, service times, contact card, admin calendar form, cross-demo wiring. Roughly +300 lines (~15% file growth).
- **Delivery 2 — Groups HQ (B):** resources data + gate function, HQ sheet with segments, add-resource flow, preview sheet, leader tools, admin storage panel, tour step. Roughly +350 lines.
- Two deliveries so you can QA each on your phone between them. Each ships as the full file; rename to `index.html` (watch for Windows hiding the extension → `index.html.html`), delete the old file in the repo, upload, commit, wait for the green check, hard-refresh/incognito.
- QA before each delivery: phone-width and desktop, all 5 tabs, the tour end to end, admin ↔ member cross-state (badge official → church page updates; admin event → phone calendar), the two confidential test cases, and a scan for any non-SVG glyph.

## F. The ten decisions, in one place

1. Calendar scope — recommend (b) church-wide + my groups
2. Admin "Add to the church calendar" form inside Announcements — recommend yes
3. Announcements: all 3 vs latest 2 + See all — lean "latest 2"
4. Confidential circles listed in Ministries ramp — recommend yes
5. Ramp shows joined groups with "Joined" state — recommend yes
6. Who adds resources — recommend any member, leader pins/removes
7. Seed Noah into Wednesday Small Group — recommend yes
8. Add one tour step for HQ — recommend yes
9. One rendered document preview + toasts — recommend yes
10. Give deep-link button on church page — your call, I'd include it

Reply with numbers and yes/no/override and I'll start Delivery 1.
