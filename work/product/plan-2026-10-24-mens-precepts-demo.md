# Plan — Men's Precepts demo (Austin Ridge)

**Owner:** this session (Noah, Oct 24: "we'll just do everything from here"). **Asked for by:** Noah, Oct 24, 2026. **Due:** shown to Bryan Bailey after class the weekend of Oct 31–Nov 1. Draft to Noah by Wed Oct 28.
**Status:** **built Oct 25** (Noah: "Build it"). Live demo: https://mens-precepts.up.railway.app · source `work/product/precepts-demo/index.html`. Answers: Noah is in Bryan's **Saturday** group; current study is **Matthew**; Bryan's real name OK in the demo.

## The situation
- **Men's Precepts at Austin Ridge:** an inductive Bible study ministry, about a dozen leader-led groups meeting **Thursday** and **Saturday**, some on **Zoom**. Bryan Bailey leads a Thursday (Zoom) and a Saturday group. Noah is a member, not a leader. Noah's estimate is two groups of about 25 men each in his part of it.
- **Today:** everything runs over email.
- **Noah's text to Bryan (Oct 24):** a central place for announcements first, then for the guys to chat, ask questions, get advice, share prayer requests and run a prayer chain. Bryan: "Let me check it out, or maybe you can show me a demo after class." Noah: "I'll have a demo ready for you next weekend."

## What the demo is
A clickable phone demo built from the existing Interconnected demo's components, re-shaped for one men's ministry. Like the main demo, it uses sample data, keeps nothing between visits, and has no real logins. Shown on Noah's phone.

**Member side (the phone):**
1. **Home:** this week at a glance: this week's lesson and homework, your group's meeting time (Zoom link button for Zoom groups), the newest announcement.
2. **Announcements:** from the ministry coordinator to all groups, or from a leader to one group. This is what replaces the email chain, so it's the first screen Bryan sees.
3. **My group:** the group's own feed for questions, advice and discussion of the week's homework.
4. **Prayer:** prayer requests with a **prayer chain**. Tap "I'm praying," see how many men are praying (count only, never a list), and mark a request **answered**, which stays visible as an answered prayer. Private requests go to the group leader only.
5. **Resources:** lesson notes, the workbook schedule, recordings.
6. **Men:** a directory with what each man does for work and what he can help with (the Interconnected thesis in one screen), plus private messages.

**Leader side (a short second view):** post an announcement to one group or all groups · see who's new · group roster. No attendance tracking, which matches the product rules.

## Product rules that still apply
No algorithm, no rankings or streaks, no pressure nudges. Prayer counts are encouragement, never a leaderboard. The confidential pattern applies to private prayer requests. Emoji-free. Brand: Interconnected, quietly ("Powered by Interconnected").

## Real names
Repo is public. **Default:** real ministry structure (Thursday/Saturday, Zoom), Bryan's name as the leader he'll see, and **fictional names for every other man**. Other leaders' real names stay out unless Noah says otherwise.

## Where it lives
A standalone file in `work/product/precepts-demo/`, kept off the public site (`/docs`). Hosted for Noah's phone as a no-login, unindexed link on Railway (a second service in the `interconnected-hq` project).

## Archetype (Oct 24)
**Pilot scope:** Bryan's two groups (Saturday in person, Thursday Zoom), about 50 men, built as the whole ministry so the other ~10 groups can join without a rebuild.
**Roles:** member · group leader (Bryan) · ministry coordinator (who? ask) · new guy.
**Rhythm:** homework on your own during the week (Matthew), then group discussion and a lecture. The app follows this week.
**Tabs:** (1) This Week: lesson, passage, private homework check-off, meeting time and place or Zoom button, newest announcement, resources. (2) Announcements: coordinator to all or leader to one group, pinned; also sent by email during the switch. (3) My Group: threaded feed, no likes contest. (4) Prayer: audience choice (group / all men / leader only), "I'm praying" (count to all, names to the requester only), updates, mark answered → Answered Prayers wall, urgent = immediate notification (the prayer chain). (5) Men: directory with work and how he can help, private DMs leaders can't read.
**Leader view:** post with audience, private prayer inbox, roster, new this week, invite. No attendance or activity scores.
**Demo script (3 min):** This Week (his study) → Announcements (no more email chain) → Prayer (count climbs, answered wall) → Men (who does HVAC?) → leader view post appears on the phone → "try it with the Saturday group for a month?"
**Real-build decisions (later):** web app on the home screen, no app store · sign in by emailed link, no passwords · email stays as safety net · data structure: ministry → groups → members (roles), announcements, posts, prayer requests (who can see, status, updates, who's praying), lessons, resources, messages. This is the same structure the church-wide product needs.

## Still open
1. Is Bryan the coordinator for all of Men's Precepts or just his two groups?
2. Saturday meeting time and place; current lesson number in Matthew.
3. Do they record lectures or share files today?
4. Does Austin Ridge need to approve, or is it Bryan's call? (Austin Ridge runs on Rock RMS; we don't replace it.)

## After the demo (only if Bryan says yes)
The first real build: logins, saved posts, notifications, on Railway with a database. Estimate 2–3 weeks to a version the men can trust. Scope set with Bryan; no date promised before he's seen the demo.

## Revision (Oct 25, Noah) — what was built
- **Removed:** homework check-off · submitting prayer requests · men directory.
- **Added:** weekly files that a leader or admin uploads; the men open them (members don't submit anything).
- **Prayer chain:** one-to-one pairs, mutual, changing weekly (an odd man out makes one group of three). The leader makes new pairs and sends them by hand for now; **automatic weekly rotation comes later.**
- **Private messages:** kept, behind the message icon in the header.
- **Tabs (member):** This Week · Updates (announcements) · My Group · Prayer · Files. **Leader view (Bryan):** Announce · Upload · Prayer Chain · Roster.
- **Sign-in screen** shows the no-password emailed-link flow (simulated).
- **Sample content to confirm with Noah:** the Saturday time (shown as 8:00 AM) and Thursday time (7:00 PM), the lesson titles and dates in Matthew, and every man's name except Noah and Bryan (fictional).
- **Demo flow:** sign in → This Week → Updates → My Group (reply) → Prayer (Mark, his note, Message Mark) → Files → shield icon → leader view as Bryan: post an announcement, upload files → tap "Member view" → it's on Noah's This Week.

## Revision 2 (Oct 25, Noah) — second pass
- **Prayer → Prayer Chain.** The intent is that partners *call* each other. Partner card shows name, **cell number, Call and Text buttons**. The sample prayer note is removed. This Week shows the partner with a Call button.
- **My Group → Group Chat.** It's a casual group text now (bubbles, input at the bottom). An **Ask** toggle marks a message as "Asking for help"; open asks are summarized at the top; the asker can mark it "taken care of." No threads.
- **Phone numbers:** collected once at sign-up ("Welcome" step: name, cell, group); shared only with your prayer partner and leaders. Leader roster shows numbers.
- **Leader Prayer Chain:** "Send this week's pairs" texts each man his partner's name and number. Later: new pairs go out automatically every Saturday morning.
- **Flow (member):** sign in by emailed link → confirm name, cell, group (first time only) → This Week (lesson, meeting, latest update, your partner with Call, this week's files) → Updates → Group Chat → Prayer Chain → Files. Private messages stay behind the chat icon at the top.
- Sample phone numbers are fictional (555-01xx).

## Revision 3 (Oct 25, Noah) — My Group, in the middle
Group Chat was too much like a group text. **My Group** is now a casual feed: a short "share something or ask the guys" box at the top with an **Ask for help** toggle; posts show newest first with short, chat-style replies underneath; Reply opens a one-line reply box inline. Asks carry an "Asking for help" tag and an amber edge until the asker marks them "Taken care of." No separate screens.

## Revision 4 (Oct 25, Noah)
Removed "Ask for help" from My Group (the toggle, the tags, "taken care of"). My Group is a plain casual feed: post box, posts newest first, short replies, inline Reply. Men can still ask for things in an ordinary post.

## Revision 5 (Nov 14, Noah) — after showing Bryan
**Bryan (Nov 8):** liked it; wants to meet to go over it more.
**Leader side redesigned:** no separate leader view. Same five tabs for everyone; leaders see extra buttons in place: **Post an update** (Updates), **Add files** (This Week and Files), **Make new pairs / Text each man his partner** (Prayer Chain), **Manage group: men and numbers** (bottom of My Group). Posting offers "this group" or "All groups."
**Group switcher:** a man in more than one group (Bryan) taps the group name in the header to switch; everything in the app follows. A one-group man never sees it.
**Demo control:** a thin bar, "Demo: you're Noah, a member · Switch to Bryan," exists only in the demo. In the real app people sign in as themselves.
**Messages** are per person: Bryan's inbox is his own.
**Open for the Bryan meeting:** keep or cut private messages and the Files tab; who's the ministry coordinator; real meeting times and lesson list; email-to-post for leaders.

## Revision 6 (Nov 14, Noah)
- **No texting system.** Leader button is now **"Notify everyone of their partner"**: a push notification to each man's phone with his partner's name. (The partner card's Call and Text buttons still open the man's own phone apps; nothing is sent by us.)
- **Post box** is one tidy row (avatar · "Write to the group…" · Post) that grows as you type.
- **Bryan is in the Saturday prayer chain.** Leaders can be paired too; a man's partner card shows while he's viewing his own chain's group.
- **Add files** lives only on the Files tab (removed from This Week).

## Revision 7 (Nov 14, Noah) — prayer chain is opt-in; profiles
- **Prayer chain is opt-in, default No** (Noah). The welcome step asks "Join the weekly prayer chain?" (No preselected). Men who aren't in it see "You're not in the prayer chain" with **Join the prayer chain** on that tab and no partner card on This Week; only men who join are paired. Leaders can add or remove a man from **Manage group** (In prayer chain / Not in chain), and a man can change it in his profile. Joining mid-week pairs him right away (with the odd man out); leaving re-homes his partner into another pair.
- **My profile:** tap your circle in the top bar. Photo, name, cell, email, group(s) (read-only; ask your leader to change), prayer chain (I'm in / Not now), Save, Sign out. Contact info is shared only with your prayer partner and leaders.

## Revision 8 (Nov 14, Noah) — it's a chain, not pairs
**Prayer chain = an order, each man calls the next.** A calls B, B calls C, C calls D… and the last man calls the first, so every man makes one call and gets one call. (Loop-back is the working assumption; Noah can flip it.)
- Each man sees **"This week, you call [name]"** with number, Call and Text, plus **"[name] will call you."** This Week shows "You call [name]" with a Call button.
- The full chain is a numbered list ("1 Jim Whitaker · calls 2"…, the last "calls 1"), with you highlighted.
- Leader: **Make a new order** (shuffle) and **Notify everyone who to call** (push notification). Later: automatic every Saturday morning.
- Joining adds a man into the order (demo: Noah lands just before Mark, so Noah calls Mark); leaving removes him and the chain closes up.

## Revision 9 (Nov 14, Noah) — "A calls B" list and weekly rotation
- **The list reads "A calls B / B calls C / C calls D…"** (the last man calls the first). Your rows are highlighted.
- **Weekly rotation:** the left column stays fixed; each week the right column moves **up** one (the top name goes to the bottom), so every man calls someone new; over a full cycle every man calls every other man once, then it starts over. *Why up, not down as first asked:* with week 1 as "A calls B," shifting the right side down one would have every man calling himself that week, so the move is upward.
- **Leader:** "Move to next week" (rotates and advances the week label) and "Notify everyone who to call."

## Revision 10 (Nov 14): the chain runs itself
- Joining or leaving never changes the chain right away. A man who joins (at sign-up, from the Prayer Chain tab, in his profile, or added by a leader) sees "You're in, starting Saturday, Nov 14" and is added at the next Saturday-morning move. A man who leaves keeps this week's call and drops off that Saturday.
- The weekly move is automatic: every Saturday morning the app drops leavers, moves the right side up one, adds joiners, and notifies every man who he calls. The leader "Move to next week" and "Notify everyone" buttons are gone.
- Manage group chips show In prayer chain / Joins Saturday / Leaves Saturday / Not in chain. The Prayer Chain tab lists upcoming changes ("Saturday, Nov 14: Pete Langley joins").
- Demo only: a dashed "skip ahead to Saturday morning" button at the bottom of the Prayer Chain tab, so the move can be shown in the meeting.
- Stress test now joins and leaves through the waiting path: 5,000 steps, chain size 2–30, 0 self-calls, 0 broken weeks.

## Revision 11 (Nov 15): Manage group is easy to find
- "Manage group" moved from the bottom of My Group to the top (same spot as "Post an update" and "Add files" on their tabs).
- The Prayer Chain tab gets its own "Manage prayer chain" button at the top for leaders. It opens the same sheet. Members see neither.
- No "take him off now" option: removals wait for Saturday (Noah: too much).

## Revision 12 (Nov 15): lesson schedule
- This Week is worked out from the lesson schedule: it shows the lesson dated in the current week (Saturday to Friday) and switches on its own every Saturday morning, together with the prayer chain. A week with no lesson shows "No class this week · Next: Lesson 10, Sat, Dec 5".
- The coordinator (Bryan in the demo) gets a "Lesson schedule" button at the top of Files: every lesson with its date, title and passage, gaps shown as "No class · Sat, Nov 28", and "Add a lesson". Tapping a lesson edits it; moving its date moves the later lessons by the same amount (how a skipped week is handled). Group leaders and members don't see it.
- For the pilot we type the schedule in from the Precepts materials before launch; leaders only touch it when a week changes.
- Sample schedule runs through Lesson 11 with no class Thanksgiving weekend (Nov 28). Titles and dates are made up until Bryan gives us the real list.
- The demo-only "skip ahead to Saturday morning" now moves This Week too. "Add files" defaults to the current (or next) lesson.

## Revision 13 (Nov 15): Announcements tab, pin and unpin
- The "Updates" tab is now "Announcements" ("Post an announcement", "Latest announcement" on This Week). The tab bar sizes each tab to its label so the longer name fits, down to 320px-wide phones.
- Leaders see "Unpin" or "Pin to top" under each announcement on the Announcements tab. One announcement is pinned at a time (pinning one unpins the other). The pinned one shows first on the tab and as the announcement on This Week; with none pinned, This Week shows the newest. Members see no buttons.
- "Manage group" (My Group) and "Manage prayer chain" (Prayer Chain) open the same screen: the men, their numbers, and each man's prayer chain button. They're two doors to the same room.

## Revision 14 (Nov 15): Feed tab, delete posts, remove from group
- "My Group" tab is now "Feed".
- Delete: every man can delete his own posts and replies; leaders can delete any post or reply in their group's Feed. One confirm step ("Delete this post? Delete / Cancel"). No approval queue, no filters. Leaders never see or delete private messages.
- Remove from group (Manage group, under each man's number, with a confirm step): he loses access right away. If he's in the prayer chain, the gap closes for the rest of the week: whoever was calling him calls the man he would have called, and only those two get a notification. He drops out of the order at the Saturday move. If closing the gap would leave a man calling himself (only in tiny chains), the chain is rebuilt on the spot and everyone gets a new name.
- Stress test, part 3: 5,000 steps with 1,036 mid-week removals mixed with joins, leaves and Saturdays: 0 self-calls, 0 weeks where anyone was missed or called twice (29 rebuilds).
- Nov 15 follow-up: the "Delete" under every reply was too busy. Replies now show nothing extra; tapping a reply you're allowed to delete brings up "Delete this reply? Delete / Cancel". A one-line note at the bottom of the Feed says how ("Tap any reply to delete it" for leaders). Post deletes stay as a quiet "Delete" next to Reply.
