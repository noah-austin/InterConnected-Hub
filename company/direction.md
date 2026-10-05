# Direction

> **The steering file.** Every role reads it first. Noah steers by telling any session what he wants; the session updates this file for him (see "Steering by conversation" in `CLAUDE.md`). Noah doesn't edit it by hand.
> Seeded Oct 2, 2026 from the build instructions' addendum + the four Sep 24 handoffs. **Phase 2 reconciliation done Oct 2:** the inbox shows no change since Sep 24 (no replies, no sends, no bounces), so the priorities below reflect what's actually live. Pipeline: `pipeline/tracker.md`.

## Do now (in order)
1. **DMARC record.** Noah, from a desktop (the TXT field truncates on phones), **before** the recovery sends below. Squarespace: account.squarespace.com → Domains → joininterconnected.com → DNS → DNS Settings → Custom records → Add record → Host `_dmarc` · Type `TXT` · Data `v=DMARC1; p=none; rua=mailto:noah@joininterconnected.com; fo=1` → Save. Touch nothing else on that page. Verify at mxtoolbox.com/dmarc.aspx after ~1 hour. (Mack §6.1)
2. **Rick Randall re-schedule.** Noah promised Sep 8 to "reach back out soon." **Drafted Oct 3:** `work/bd/outbox/2026-10-03-rick-randall-reschedule.md`. Send first (DMARC not needed for a reply in an existing thread).
3. **Chris Smith, via Rebecca** (rebecca@f-pc.org), with fresh dates and the gap owned in one sentence. **Drafted Oct 3:** `work/bd/outbox/2026-10-03-fellowship-plum-creek-via-rebecca.md`.
4. **Eric Bryant consultation form** (ericbryant.org/consultation), text rewritten to v3.1. **Ready Oct 3:** `work/bd/outbox/2026-10-03-eric-bryant-consultation-form.md`.
4b. **Re-approach the 21 silent threads**, one honest note each, about 7 a day after DMARC is live: `work/bd/outbox/2026-10-03-silent-threads-reapproach.md`. Each note ends with a referral ask for anyone who can't meet now.
5. **2FA + recovery codes confirmed** on Google and GitHub. GitHub → Settings → Password and authentication; Google → myaccount.google.com → Security → 2-Step Verification. Both `noahaustin15` and `noah-austin` GitHub accounts now matter. Log the end state (no codes in the repo, ever).
6. **The month-old taste check.** `og-image.png` + `apple-touch-icon.png`, Noah + wife. A veto is a cheap re-export by Dex. Send her exact words.
7. **OG client-preview checklist** (Mack §2a), five minutes with Noah's phone: fresh iMessage thread, WhatsApp, Slack, Facebook Sharing Debugger, LinkedIn Post Inspector. Log results.

## Decisions waiting on Noah
Deferred by Noah on Oct 2 ("later"):
- Who is **Kevin** at Austin Stone (tracker row 9)? No touch until answered.
- **Austin Ridge** status (Noah's personal lane, Engine 1). A pastor flagged the credibility gap unprompted (`pipeline/objections.md`).
- **Five warm-path names** from Noah's network (tracker row 21). The highest-yield unworked asset in BD.
Decided Oct 3 (Noah approved Sonny's plan): the silent threads each get one re-approach (item 4b); Walt Lengel (row 5) goes Dormant (one Austin Stone thread); Kevin (row 9) and Austin Ridge (row 11) stay untouched.

## Standing operations
- **Sonny daily run:** a scheduled routine, weekdays at 6:47am Central, runs in the original Sonny session (`session_01RpYqGgViyotN6xTacN72hs`), which has Gmail and repo push. It checks the inbox, updates the tracker, stages drafts and adds one new get-in-the-room play. It never sends. (Routine "Sonny daily BD run (this session)", Oct 5. The Oct 3 fresh-session routine is disabled: its sessions had no Gmail and no repo push access.)

## What's working
- Template v3.1 and its construction rules (`skills/cold-email-template.md`). Too few sends to judge, but it fixed the "read as selling" failure.
- Multipliers: the only live conversation (Rick Randall) came from a multiplier coffee ask.
- The demo itself: verified live by Dex and Mack on Sep 24, sample-data honest, and the overclaim list is current.

## What to stop
- Treating cold email volume as the path to the first LOI. 27 single-touch sends produced one live conversation. Warm, referral and multiplier paths first; bump existing threads before adding new cold names.
- Opening new threads into churches that already have one (one thread per church).
- Letting scheduled follow-ups lapse silently. If a date can't be kept, say so in the tracker.

## Follow-ups from the Oct 2 positioning update (whole-app solution)
- `company/overview.md`, `decisions.md` and `roles/sonny.md` are updated. The cold-email paragraph already matches and stays verbatim.
- **Not yet updated, on purpose:** the Brand Guidelines' "What we are" and the Plan v5.1 executive summary still lead with skills-and-needs. Both are canon and owned (June, and the plan). Update them in the next marketing pass or plan revision; until then, `overview.md` is the current positioning.
- Dex: check that the landing-page hero and FAQ read as the whole-app solution, not mainly needs-matching. Propose copy; don't ship without Noah's go.

## Parked (dormant lanes and infra — activate per growth rules or on Noah's go)
- **Domain cutover** (runbook below). Waiting on Noah's go.
- **Form service for pilot requests.** Mack creates the account, Dex wires one edit. Recommended next infra win.
- **Uptime monitor** (UptimeRobot-class free tier).
- **hello@ alias** (Admin → Directory → Users → Noah → Add alternate email).
- **Analytics.** Paused by Noah; Dex holds the spec.
- **June's site copy pass** and the **Launch Sunday kit**. Marketing lane dormant. Also: June's Plan v5 review queue item (v5.1 now exists with two overclaim fixes; confirm that closes it), the testimonial pipeline, and the "committed pilot churches" deck slide (waits on the first LOI).
- **interconnecteddemo.com closure.** No DNS then or now; close as "not owned" on Noah's one-line Namecheap check.
- **Auto-renew + expiry dates** for the domain and Workspace billing (Mack §6.3). Partial evidence Oct 2: Workspace charged $8.95 on Oct 1 ("Payment received") and issued an invoice due Oct 30, so Workspace billing is live. Domain auto-renew and expiry are still unconfirmed.
- **Ada:** trademark knockout on "Interconnected" (backlog, before major brand spend) · LOI lawyer review (not a gate on conversations).
- **Pearl:** co-founder search, fundraising, accelerator applications.
- **Gus:** pricing validation once `pipeline/pricing-reactions.md` has rows · storage cost model.
- **Mack's GitHub Org recommendation.** On file as a future option for the connected account.

## Logged for later — Domain cutover (do NOT execute until Noah says go)
Pick a day with no pastor meeting. Mack's handoff §3–4 (`work/it/`) holds the detailed reference.
1. Squarespace DNS → edit the `www` CNAME record's data to `noah-austin.github.io`. Touch nothing else: the four apex A records, MX, SPF, DKIM and DMARC all stay.
2. Add the held `CNAME` file (contents: `www.joininterconnected.com`) to `/docs/` of this repo. It is not in the repo until then.
3. This repo → Settings → Pages → custom domain `www.joininterconnected.com`. (The old account's domain verification may need moving first; see Mack §3 step ③.)
4. Wait for the DNS check, then the certificate, then Enforce HTTPS. Never toggle settings while provisioning.
5. Verify the padlock in an incognito window and on cellular.
6. Update `CLAUDE.md` and `skills/deploy-checklist.md`: this repo becomes the live deploy target.
7. Retire the old repo `noahaustin15/interconnected-demo`: archive it, do not delete its history.
