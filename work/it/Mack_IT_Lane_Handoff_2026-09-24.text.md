Interconnected — IT Lane: Full Handoff (System Migration)
Prepared by: Mack (IT lane) · Date: Wednesday, September 24, 2026 For: the agent taking over IT.
Assume you have nothing else — no chat history, no prior briefs. This file is self-contained and
supersedes Mack_Domain_Scout_Interconnect_2026-08-24.md (whose findings are folded in below,
since session outputs don't survive migrations). Verified against: live DNS and the live site on Sep
24, 2026. Every claim below is tagged [verified Sep 24] (checked today, from this session), [cross-
ref] (verified today by another lane's Sep 24 handoff), or [unconfirmed] (instructed but never
confirmed executed — treat as not done).




0. What this lane is
You are Mack, IT Manager at Interconnected (rename to "Interconnect" proposed, not cleared —
see §4). You own website hosting and deployment, domains and DNS, Google Workspace email
infrastructure, account security, connected services, and infrastructure decisions. You report to
Buford (Co-CEO, home base) and Noah (Founder & CEO, final say, non-technical but fast; give the
why in one sentence then exact numbered click-paths; he's often on his phone; screenshots resolve
most issues; he prefers honest pushback over validation).

Lanes cannot talk to each other; Noah carries files. Write every output for cold handoff. Peers: Dex
(product — owns everything inside index.html ; you own everything around serving it), Sonny (BD —
the outreach campaign your email infrastructure carries), June (marketing), Pearl (fundraising/co-
founder), Ada (legal), Gus (CFO).

Standing rules of this lane:

1. Deploy only when Noah hands you a file and says deploy. Never proactively. Flag issues; don't
   act unasked.

2. Never edit the contents of index.html . Move it, verify it, revert it from git history if a deploy
   breaks — the insides are Dex's.

3. Never touch MX, SPF, or DKIM records. Absolute. (Full never-touch list in §7.)

4. Everything without a connector (Squarespace, Google admin, GitHub until a connector exists —
   see §5) is advise-and-verify: exact click-paths, Noah executes, every change logged in your
   outputs so home base holds the record.

5. Findings before purchases. Deliverability is sales infrastructure. Security posture checked without
   being asked twice.

Onboarding gap you inherit: the original IT_Infrastructure_Briefing.md — described as the
complete technical inheritance (every configuration, credential location, past incident) — was never
delivered to this lane. Only the shorter Mack_IT_Brief.md arrived (Aug 24). Everything below was
built from that brief plus direct verification. If the infrastructure briefing surfaces, it may contain
incident history and credential locations this file lacks — reconcile, and flag conflicts to Noah.


1. Infrastructure state of record

Serving stack [verified Sep 24]
    Live site: https://www.joininterconnected.com — GitHub Pages from repo
    noahaustin15/interconnected-demo , current commit 8335d29 (Aug 26; no commits since)
    [cross-ref: Dex handoff, repo checked Sep 24].

    HTTPS works end-to-end: http://joininterconnected.com redirects to
    https://www.joininterconnected.com with a valid certificate [verified Sep 24 by live fetch]. The
    Enforce HTTPS checkbox state in Pages settings was never screenshotted back to this lane
    [unconfirmed], but the observable behavior is what the checkbox exists to produce — treat the
    task as functionally done, confirm the checkbox opportunistically next time someone is in Pages
    settings.

    DNS (registrar: Squarespace Domains), full read as of today [verified Sep 24]:


      Record                    Value                           Status

                                185.199.108.153 /
      A (apex) ×4               .109.153 / .110.153 /           Correct GitHub Pages set
                                .111.153


                                                                Correct — and proof the account transfer
      www CNAME                 noahaustin15.github.io
                                                                in §3 never happened

                                                                Google's modern single-record form.
      MX                        1 smtp.google.com               Correct. Do not "fix" it to the legacy five-
                                                                record set.

                                v=spf1
      TXT (apex)                include:_spf.google.com         SPF correct, untouched
                                ~all


      google._domainkey
                                RSA key present                 DKIM is published and signing — good
      TXT

                                NXDOMAIN — record               DMARC was never created. Top open
      _dmarc TXT
                                does not exist                  item, §6.


    Site head tags serving live [verified Sep 24]: og:title , og:description , og:image →
    https://www.joininterconnected.com/og-image.png (1200×630, absolute on the www host),
    og:url , og:site_name , twitter:card summary_large_image + twitter set, theme-color
     #F7FAFF , color-scheme: light only . All under the Interconnected name. Asset files ( og-
     image.png , favicon.svg , favicon.ico , apple-touch-icon.png , CNAME ) confirmed at repo root
     [cross-ref: Dex, Sep 24].


Email [verified Sep 24 unless noted]
     Company email noah@joininterconnected.com on Google Workspace; inbox live and reconciled
     Sep 24 [cross-ref: Sonny handoff].

     Authentication: SPF     DKIM          DMARC       . With Gmail/Outlook's bulk-sender rules, missing
     DMARC is the one gap that costs deliverability — and the BD lane's restart plan (Rick Randall
     reschedule, Chris Smith bump, Eric Bryant first touch) means sends are imminent.

     27 outreach emails went out Aug 24–26; campaign dormant since, restarting now [cross-ref:
     Sonny].


Adjacent domains [verified Sep 24]
     interconnecteddemo.com — no DNS records exist (checked Aug 24 and again today). A
     Namecheap-purchased domain would be parked with DNS. Working conclusion: never
     purchased. Noah's 30-second confirmation (Namecheap → Domain List) was requested and
     never returned [unconfirmed]. Recommend the successor close this as "not owned" on Noah's
     one-line say-so.

     interconnect.church and interconnectapp.com — the scout's recommended primary and
     fallback — still show no DNS today, i.e. very likely still available and definitely not purchased by
     us. If the rename ever gets a green light, these get bought the same day — announcement before
     purchase is a squatting invitation.


2. Task scoreboard — verified vs. pending
The §4 task list from the Aug 24 brief, with the honest status. This lane had one working session
(Aug 24); no completion confirmations or screenshots were ever returned, and today's verification is
what separates done from not.


 #      Task                         Status                                                 Evidence

                                     Done Aug 24 — findings + migration map
                                                                                            Scout report
        Domain scout for             delivered (folded into §4 below). Decision
 1                                                                                          delivered Aug
        Interconnect                 pending at home base; rename not cleared
                                                                                            24
                                     [cross-ref: Sonny §1]

                                     Functionally verified — http→https redirect +          [verified Sep
 2      Enforce HTTPS on Pages
                                     valid cert live                                        24]

                                                                                            [verified Sep
                                     NOT DONE. Click-path and exact values delivered        24] — #1
 3      DMARC record
                                     Aug 24; _dmarc is NXDOMAIN today                       open item
                                                                                            [unconfirmed]
         2FA on Google + GitHub,       Unconfirmed. Paths delivered Aug 24; no
  4                                                                                         — #2 open
         recovery codes offline        screenshot ever returned; not externally checkable
                                                                                            item

         Auto-renew on domain +        Unconfirmed. Same. Domain expiry date was
  5                                                                                         [unconfirmed]
         Workspace billing             requested for the record and never supplied

                                       Effectively resolved: no DNS then or now →           [verified Sep
         interconnecteddemo.com
  6                                    presumed never purchased; needs Noah's one-          24] +
         status
                                       line Namecheap confirmation to close                 [unconfirmed]

  7      hello@ alias                  Not done (no Workspace session ever confirmed)       [unconfirmed]

                                       Shipped and serving (commit 8335d29 , Aug 26
                                       — the rename pause was overtaken by events;          [verified Sep
  8      Favicon + OG tags             assets carry the Interconnected name, correctly,     24] /
                                       since the rename isn't cleared). Client-preview      [unconfirmed]
                                       verification checklist never run — see §2a

         Uptime monitor
  9                                    Not done                                             —
         (UptimeRobot-class)



2a. OG-preview verification — results and the outstanding checklist
What is verified (Sep 24, from the served page): the full OG/Twitter tag set is live, syntactically
correct, image URL absolute on the canonical www host, dimensions declared 1200×630,
summary_large_image card set. Everything a crawler needs is in place.

What was never verified: actual rendering in clients. This checklist was assigned Aug 24 and its
completion never confirmed [cross-ref: Dex §6.3 says the same]. It takes five minutes with Noah's
phone; run it once and log results:

1. iMessage — paste the URL in a fresh thread (any thread where the link was ever sent before will
      show the stale/bare preview forever). If even a fresh thread shows the bare link, it's Apple's cache
      — wait an hour and retry before changing anything.

2. WhatsApp — fresh thread; note the square crop behavior (the design keeps everything inside the
      center 630×630, so it should survive).

3. Slack — any channel/DM.

4. Facebook Sharing Debugger and LinkedIn Post Inspector — paste the URL; both force a fresh
      crawl and show exactly what they'll render. Run once, screenshot.

5. Expected card: brand-blue image, wordmark + tagline, title "Interconnected: your church,
      connected every day of the week." If the rename lands, og-image.png gets regenerated by Dex
      (his lane), and this checklist runs again.
3. GitHub account transfer — requested, instructed, not executed
In the Aug 24 session Noah asked to move hosting to another GitHub account. Full click-path was
delivered (built-in Transfer ownership, never re-upload — it preserves git history, Pages config, and
the CNAME file). It never happened: the www CNAME still points at noahaustin15.github.io
[verified Sep 24] and the repo still lives under noahaustin15 [cross-ref: Dex, Sep 24]. Noah also
never answered the blocking question: destination account name, and personal account vs.
Organization.

Standing recommendation, unchanged: a free GitHub Organization owned by Noah, repo transferred
in — a co-founder later becomes a second owner without shared logins. A second personal account
just relocates the single point of failure.

Condensed run for when it revives (full ordering matters): ① destination account exists, 2FA on,
codes stored → ② old repo → Settings → Danger Zone → Transfer ownership (personal destinations
must accept via email within 24h; own Org is instant) → ③ move the domain verification: remove
joininterconnected.com from old account's Settings → Pages → Verified domains; add on the new
account; put the new _github-pages-challenge-<name> TXT in Squarespace; Verify; delete the old
challenge TXT only → ④ Squarespace: edit www CNAME data to <newname>.github.io — the four
apex A records, MX, SPF, DKIM, DMARC all stay untouched → ⑤ new repo → Settings → Pages:
custom domain should persist via the CNAME file; wait for DNS check, then cert, then Enforce HTTPS
— never remove/re-add the domain while waiting → ⑥ verify http:// apex redirects to
https://www. with padlock, incognito, on cellular → ⑦ log everything; re-point any hardcoded
noahaustin15.github.io references; a future GitHub connector must be authorized against the new
account. Expect minutes of propagation wobble; do it on a day with no pastor meeting.


4. The rename ("Interconnect") — scout findings of record + migration
map
Status: rename NOT cleared. All public assets, outreach, and email correctly still say
Interconnected on the existing domain [cross-ref: Sonny §1]. Ada's trademark read status is
unknown to this lane. The go/no-go at home base never happened. Nothing below executes without
it.

Scout findings (Aug 24, availability re-spot-checked Sep 24):

      interconnect.com — taken; owner posts "not for sale, don't ask" since 2019. Dead at any price.

      joininterconnect.com — taken by a live product: "InterConnect," an AI career-guidance
      platform pitched on "meaningful connections." Kills the join-prefix consistency option and is a
      brand-collision flag.

      getinterconnect.com — taken (InterOptic, data-interconnect hardware). interconnect.app ,
      .co , .org , .net , .us , .me , interconnecthq.com — all taken.

      interconnect.io — GoDaddy brokered "get a price" listing = negotiated four-to-five figures. Not
   for our stage.

   Open (no DNS then or now; only a registrar cart proves it): interconnect.church ,
    interconnectapp.com , useinterconnect.com , tryinterconnect.com , myinterconnect.com ,
    interconnectchurch.com .

   Recommendation on record: primary interconnect.church (the address is the positioning —
    noah@interconnect.church says the category before a pastor reads a word; TLD familiar to this
   buyer; deliverability rides on SPF/DKIM/DMARC, not TLD), fallback interconnectapp.com (nearest
   open .com). If green-lit, buy both (~$50/yr total) the same day, before any announcement.

   Flag for Ada / the go-no-go (delivered Aug 24): "Interconnect" is crowded in software; two
   collisions sit near our category — the joininterconnect.com platform and an App Store app
   "Interconnect Network" (private, verified-member community feed with connect requests and
   moderated posts). A pastor Googling "Interconnect app" will not find us first.

Migration map (cost of saying yes — sequencing principle: site and email move on different
days; email moves last; active pastor threads never see a sender change mid-thread):

1. Green light → buy primary + fallback, auto-renew on.

2. Workspace: add new domain as a domain alias (Admin → Account → Domains → Manage
   domains → Add a domain → Alias domain) — not a secondary domain (creates separate users —
   wrong tool), and no tenant migration (never needed). Alias = noah@ at both domains lands in the
   same inbox, so every reply to an old thread still works. Google's TXT verification + the new
   domain's MX/SPF/DKIM/DMARC go in the new domain's DNS only. DMARC on the new domain
   must exist before the first send from it. (Later, optional: Change primary domain is one Admin
   click, but check first whether the Workspace subscription was bought via Squarespace/Google
   Domains, which can block it; not needed for launch.)

3. Dex ships the renamed build; domain switch and copy change land the same day (favicon/OG
   regeneration is his, in the same commit).

4. New domain DNS: same four apex A records; www CNAME → the GitHub Pages host of whatever
   account owns the repo by then.

5. Pages custom-domain switch on the repo (writes a CNAME file — a commit, but not to
    index.html ); wait for DNS check → cert → Enforce HTTPS; no toggling.

6. joininterconnected.com is kept forever — a Pages repo serves one custom domain, so prepare
   before step 5 a tiny redirect repo (one-line meta-refresh/JS index.html , custom domain
    www.joininterconnected.com , HTTPS enforced). This preserves every https:// link in every
   pastor email. Squarespace's own forwarding is the lesser option (HTTPS on forwarded links
   unverified). True 301s only matter for SEO, which at 27 emails is not a factor. Old domain's
   MX/SPF/DKIM/DMARC untouched throughout — email never blinks.

7. Email cutover, two-phase: new first-touch outreach from the new address (Gmail → Settings →
   Accounts → Send mail as → alias → default) once its DNS auth is live; existing threads keep the
   old sender until they close; old address stays alive as an alias indefinitely.
8. Housekeeping: signatures, Workspace org name, optional repo rename, hello@ on both, Gmail
  connector unaffected (bound to the account, not the domain). Total: ~2 hours of Noah across two
  sittings, ~$50/yr, a day of DNS/cert waiting. Only the announcement is irreversible.


5. Access inventory

                                                     Who
                                                                 Connector
 System             Account / identity               holds                      Notes
                                                                 state
                                                     access

                                                                 No
                                                                 connector
                                                                 was ever
                                                                 enabled in
                                                                 this lane.
                                                                 The Aug
                                                                 24 brief
                                                                 said the
                                                                 lane was       If the new system grants a
                                                                 connected;     GitHub connector: verify
                                                                 the chat's     access against the repo
                     noahaustin15 (personal) ·       Noah        tool list      before the first deploy, and
 GitHub
                    repo interconnected-demo         only        never          against the new owner if
                                                                 contained      §3's transfer ever
                                                                 GitHub,        executes. 2FA/recovery-
                                                                 flagged to     code status [unconfirmed].
                                                                 Noah Aug
                                                                 24, never
                                                                 resolved.
                                                                 All deploys
                                                                 remained
                                                                 Noah-
                                                                 manual all
                                                                 period.

                                                                                Auto-renew state and
                    joininterconnected.com                                      expiry date [unconfirmed]
 Squarespace                                         Noah        None (by
                    (registrar + DNS + the never-                               — get both logged. A lapse
 Domains                                             only        design)
                    touch records)                                              kills site + email
                                                                                simultaneously.

                                                                 Gmail
                                                                 connector
                                                                 live on two
                                                                 other
                                                                 lanes:
                                                                 Sonny (BD
                                                                 — reads        Any Workspace "third-
                                                                     and drafts,    party app access" security
                                                                     never          alert is most likely these
                                                                     sends;         connectors — legitimate,
                                                                     Noah           but confirm before
                                                                     sends          dismissing. Least-privilege
  Google               noah@joininterconnected.com                   everything     note for the new system:
                                                         Noah
  Workspace            (admin = Noah)                                personally)    the IT lane doesn't need
                                                                     and Buford     inbox access to do its job;
                                                                     (oversight).   decide deliberately
                                                                     This IT        whether it keeps
                                                                     chat also      Gmail/Drive. 2FA
                                                                     had Gmail      enforcement + backup
                                                                     + Google       codes [unconfirmed].
                                                                     Drive
                                                                     connectors
                                                                     available
                                                                     and never
                                                                     used
                                                                     them.

                                                                                    Contents unverified;
                       Historical account (existence                                 interconnecteddemo.com
  Namecheap                                              Noah        None
                       per brief)                                                   presumed never purchased
                                                                                    (§1).

                                                         Nobody
  Recommended-                                           (open                      Purchase only on rename
                        interconnect.church ,
  but-unbought                                           as of       —              green light — then
                        interconnectapp.com
  domains                                                Sep                        immediately.
                                                         24)

                                                                                    The durable record.
                                                                                    Session workspaces get
  Anthropic /                                            Noah +                     recycled (the BD lane lost
  claude.ai project    Project files                     all         —              its xlsx tracker this way) —
  "InterConnected"                                       lanes                      anything that must survive
                                                                                    goes into the project as a
                                                                                    file.


Single-founder reality, restated: the GitHub account and the Google account are the company. 2FA
+ offline recovery codes on those two is the highest-leverage security action available, and it is still
[unconfirmed].


6. Open items for the successor, in priority order
1. DMARC — create it. Verified absent today; outreach restart is imminent. Squarespace:
   account.squarespace.com → Domains → joininterconnected.com → DNS → DNS Settings →
   Custom records → Add record → Host _dmarc · Type TXT · Data v=DMARC1; p=none;
    rua=mailto:noah@joininterconnected.com; fo=1 → Save. Touch nothing else on that page.
    p=none changes no delivery — it starts reports; read the first XML for Noah, tighten to
    p=quarantine after a clean month. Verify at mxtoolbox.com/dmarc.aspx after ~1 hour. Do this
    before, not after, the Rick Randall / Chris Smith / Eric Bryant sends if at all possible — and
    don't let Noah do the DNS edit from his phone; the TXT field truncates on small screens.

 2. Confirm 2FA + recovery codes on Google and GitHub (paths: GitHub → Settings → Password
    and authentication; Google → myaccount.google.com → Security → 2-Step Verification; enforce
    tenant-wide at admin.google.com → Security → Authentication). Screenshots of end states go in
    the log.

 3. Auto-renew + expiry dates (Squarespace domain overview; admin.google.com → Billing →
    Subscriptions) — log the dates; check the card isn't expiring.

 4. Recover IT_Infrastructure_Briefing.md — the technical inheritance this lane never received. It
    wins over this file on configuration details it documents; flag conflicts.

 5. Close interconnecteddemo.com on Noah's one-line Namecheap check.

 6. GitHub transfer decision (§3): Org vs. stay-personal — get it decided and logged either way;
    execute per §3 if go.

 7. Rename go/no-go (§4): surface it at home base; it has been pending since Aug 24 and the
    recommended domains sit unprotected while it waits.

 8. Run the OG client-preview checklist (§2a) — five minutes, then log.

 9. hello@ alias (Admin → Directory → Users → Noah → Add alternate email) — free, do it alongside
    any Workspace session.

10. Form service for pilot requests (Formspree-class; Dex's standing request — this lane creates
    the account, Dex wires one small edit). Removes the only conversion path's dependency on the
    visitor's mail app. Recommended.

11. Uptime monitor (UptimeRobot-class free tier on the live URL).

12. Analytics account (Plausible/Fathom-class) — paused by Noah; act only when he unpauses; Dex
    holds the implementation spec.


7. Decisions on record (don't relitigate without new information)
    GitHub Pages stays for the marketing site; revisit only on a concrete trigger (server-side form
    capture, recurring deploy pain).

    The site stays dependency-free (Google Fonts only) and light-mode locked — scar tissue from
    real incidents.

    joininterconnected.com never lapses, rename or not — every link ever sent must keep working.

    Never-touch list: MX ( 1 smtp.google.com — modern single-record form, not broken), SPF TXT,
   DKIM ( google._domainkey ). DMARC, once created, joins the change-controlled set.

   Never toggle the Pages custom domain / Enforce HTTPS while a cert is provisioning.

   Deploys only on Noah's explicit hand-off; index.html contents are Dex's; deploy filename is
    index.html exactly (Windows hides extensions — the .html.html trap).

   The future product stack (React Native / Node / PostgreSQL / AWS-or-GCP) belongs to the
   eventual technical co-founder; this lane's role then is accounts, access, domains.

   We never handle payments; the Give button stays a deep-link placeholder.


8. What "good" looks like in this lane
Exact click-paths with the why in one sentence; verification over recollection (today's DNS read is the
model — check, don't assume); findings before purchases; every DNS or account change logged to
home base; the never-touch list respected absolutely; deliverability treated as the sales infrastructure
it is; security posture checked without being asked twice; and honest pushback when a request risks
the domain, the email, or the deploy pipeline — Noah expects it and respects it.
