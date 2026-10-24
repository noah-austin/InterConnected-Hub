# Plan — Men's Precepts demo (Austin Ridge)

**Owner:** Dex (Product). **Asked for by:** Noah, Oct 24, 2026. **Due:** shown to Bryan Bailey after class the weekend of Oct 31–Nov 1. Draft to Noah by Wed Oct 28.
**Status:** plan proposed; build starts on Noah's OK.

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

## Open questions for Noah
1. Which group are you in: Bryan's Saturday or Thursday (Zoom)?
2. What's the current Precepts study (book or course)? It makes the homework screens feel real.
3. OK to show Bryan's name as leader in the demo?

## After the demo (only if Bryan says yes)
The first real build: logins, saved posts, notifications, on Railway with a database. Estimate 2–3 weeks to a version the men can trust. Scope set with Bryan; no date promised before he's seen the demo.
