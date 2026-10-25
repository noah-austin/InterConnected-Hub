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
