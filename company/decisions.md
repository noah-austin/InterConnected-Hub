# Decisions

> The consolidated decision log, for product and company. One line per decision, with its owner. Don't relitigate without new information. New decisions get appended to the right section with a date.
> Sources: Dex Sep 24 handoff §4 · Sonny Sep 24 handoff §3–4 · June Sep 24 handoff §1 · Mack Sep 24 handoff §7 · the build instructions' decision record and addendum.

## Company and governance
| Date | Decision | Owner |
|---|---|---|
| 2026-08-24 | Name is **Interconnected**. Never "Believers In Business," never "Interconnect." The rename was considered and closed; it reopens only from Noah. | Noah |
| 2026-08-24 | The Aug 24 domain scout found joininterconnect.com taken by a live product and interconnect.com unbuyable. The keep decision is vindicated, not just preferred. The trademark knockout on "Interconnected" stays parked backlog (Ada). | Noah / Mack |
| 2026-09-24 | The company runs from one public repo with ALL company information included, pipeline and contact data too. Buford recommended private; Noah overrode with full knowledge of the tradeoff. Settled. | Noah |
| 2026-09-24 | Growth rules: two active roles (Sonny, Dex). Add a role only after ~2 weeks of clean runs. No inter-agent messaging, orchestration dashboards, manager agents, databases, send-automation, or cron until a routine has run manually for two weeks. | Noah |
| 2026-09-24 | Least-privilege connectors: BD sessions get Gmail read/draft, never send. Product and IT sessions get no inbox access. No session that reads inbound email may send anything externally. | Noah / Buford |
| 2026-10-02 | Phase -1 resolved: the brain and the site's future home live in a new repo on the Claude-connected account (`noah-austin/InterConnected-Hub`, public, used as-is rather than renamed). The old repo `noahaustin15/interconnected-demo` keeps serving the live site until a separate domain-cutover day. No GitHub ownership transfer. Mack's Org recommendation stays on file as a future option. | Noah |
| 2026-10-02 | Interim deploy rule: live deploys go to the old repo, done manually by Noah. `/docs/` here is the forward copy. CNAME held out of the repo until cutover. | Noah |
| 2026-10-02 | BD drafts are staged in the repo (`work/bd/outbox/`), not in Gmail drafts. | Noah |
| standing | Feedback governance: collect for a week, act on patterns of 3+, treat single opinions as taste unless strategically compelling. Noah's wife is the visual taste check ("premium, not busy"). | Noah |
| standing | Detailed financial projections are deferred until field pricing and dev quotes exist. Nothing produced is legal or investment advice. | Noah |

## Product — founding (pre-Aug 24)
| Decision | Owner |
|---|---|
| **Member-complete, not staff-complete.** This is the vision test for every feature. | Noah |
| No reputation scores / gamification. Trust is pre-established; rankings poison it. | Noah |
| No algorithmic feed. Members choose toggles. | Noah |
| Mentorship matching removed. It emerges through posts and groups. | Noah |
| **Member-led groups, admin oversight only.** Admins badge "Official" or remove, never approve. | Noah |
| **No pressure mechanics.** The "3 needs match your skills" banner was built and removed. | Noah |
| **Aggregate-only insights**, with one scoped exception (care signals, below). | Noah |
| Emoji-free, icon-based UI. | Noah |
| Mobile app first, web for admins. | Noah |
| AI moderation rejected. Community reporting plus human judgment. | Noah |
| Honest FAQ about prototype stage. | Noah |
| **Groups as headquarters.** Files and resources make groups a home; ministry-level switching costs are the moat. | Noah |

## Product — Aug 24–26 (Noah, Dex recommendations accepted)
| Decision | Owner |
|---|---|
| Calendar scope = church-wide + groups you've joined, anchored to fixed `DEMO_TODAY` (2026-04-15), never the real clock. | Noah / Dex |
| Confidential circles are listed in Ministries (existence visible; membership, posts, files, events never). | Noah / Dex |
| Confidential enforcement is one flag + one gate function (`canSee`/`adminCanSee`) on every render path, with planted test cases. No second code path. | Dex |
| Any member can add group resources; leaders pin/remove. | Noah |
| **Storage quotas are per church, never per member.** | Noah (flagged to Gus) |
| Splash button is "Take the tour" (tour-first). | Noah |
| Per-group line icons replace letter monograms (brand-system change). | Noah |
| Landing page leads with concrete product: plain-language lede, real screen crops, roofer story. | Noah / Dex |
| Every landing crop is a door into the one live demo (`demoJump`), not a mini-app. | Dex |
| "Why churches subscribe" shows real Insights panels, not text cards. | Dex |
| Admin frame is fixed-height with internal scroll. | Dex |
| Pilot CTA is an in-page form → prefilled email + copy fallback. | Dex |
| Volunteer sign-up module refused (staff workflow). | Noah |
| Give button is a deep-link placeholder only. We never handle payments. | Noah |
| Sample-data honesty fixes: care-signal line implies no attendance tracking; Year in Review says 8 groups. | Dex |
| **Traffic analytics paused** by Noah. The recommendation stays on file (Dex handoff §6.5). | Noah |
| Tour is 9 steps (group-HQ step added). | Dex |
| Care signals stay individual-level but metadata-only, and we say so precisely: "Every insight is aggregate except one, quiet-member care signals, and that one uses activity dates only, never content." Never claim 100% aggregate. | Noah / Dex |

## Brand (June, Noah-approved Aug 24) — full canon in `brand-guidelines.md`
| Decision | Owner |
|---|---|
| Canonical URL is the www host; bare domain redirects. | June |
| Logo: gathered dot-cross. Full 47-dot mark ≥48 px; 13-dot variant <48 px only. No redesign proposals unprompted. | Noah |
| og:title name-first; og:description two-sided; card = mark/wordmark/tagline on solid #2563EB. theme-color #F7FAFF. | June / Noah |
| Competitors unnamed in writing ("a group text and a shared drive"); Planning Center always named, as a complement. The confidential business plan's competition table is an allowed exception. | June / Buford |
| Light mode only. No emoji anywhere, ever. Site stays dependency-free (Google Fonts only). | Noah |

## BD (Sonny, ratified by Buford Aug 24; Noah additions Aug 26)
| Decision | Owner |
|---|---|
| **Re-approach, not "bump."** At five weeks of silence, rewrite as one honest re-approach with real news. | Sonny / Buford |
| Church-side value belongs in cold email as one clause only ("There's a part built for pastors too"). | Sonny / Buford |
| **One thread per church at a time.** | Sonny / Buford |
| Subject line stays "Could I get your wisdom on something?" Revisit at 20 sends. | Sonny / Buford |
| **Template v3.1** (Aug 26) is in force. Construction rules in `skills/cold-email-template.md`. | Noah / Buford |
| Every ask is a meeting with that person, never access to a group, event or newsletter. | Noah |
| Never send the demo link in cold outreach. | Noah |
| Austin Ridge is Noah's personal lane. No lane contacts anyone there without his explicit instruction. | Noah |
| The LOI is introduced only after a meeting goes well. Ada's lawyer review is not a gate on conversations. | Noah |
| BD captures pricing reactions; it never changes prices (Gus owns pricing). | Noah |
| Kill rule: a channel with near-zero replies over 20 touches gets replaced, not repeated. | Sonny |

## IT (Mack, on record Sep 24)
| Decision | Owner |
|---|---|
| GitHub Pages stays for the marketing site. Revisit only on a concrete trigger. | Noah / Mack |
| joininterconnected.com never lapses, rename or not. | Noah |
| Never-touch DNS: MX (`1 smtp.google.com`), SPF TXT, DKIM (`google._domainkey`). DMARC joins the change-controlled set once created. | Mack |
| Never toggle the Pages custom domain / Enforce HTTPS while a cert is provisioning. | Mack |
| Deploy filename is `index.html` exactly (the `.html.html` trap). Contents are Dex's; deployment is mechanical. | Mack / Dex |
| The future product stack belongs to the eventual technical co-founder. | Noah |

## Added after the build
| Date | Decision | Owner |
|---|---|---|
| 2026-10-02 | Noah steers by telling any session in plain words; the session updates `direction.md` (plus `decisions.md` and role files as needed), commits, and logs. Noah never edits files by hand. | Noah |
