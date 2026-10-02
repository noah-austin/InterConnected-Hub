# Interconnected — IT & Infrastructure Briefing
**For the IT workstream agent · Current as of mid-August 2026 · Confidential**

You own: website hosting and deployment, domains and DNS, Google Workspace email, account security, and infrastructure decisions. This document is the complete technical/operational history. The product-development agent owns the *content* of the site file; you own everything around getting it served, secured, and reachable. Coordinate with them on anything touching the file itself (e.g., favicon, meta tags).

---

## 1. Infrastructure at a glance

| Component | Provider | Identifier / Detail |
|---|---|---|
| Website hosting | GitHub Pages (free) | Repo: `noahaustin15/interconnected-demo` (public) |
| Live URL | — | https://www.joininterconnected.com (also noahaustin15.github.io/interconnected-demo) |
| Primary domain | Bought through Google Workspace; DNS managed at **Squarespace Domains** | joininterconnected.com |
| Email | Google Workspace | noah@joininterconnected.com (working, send + receive) |
| Site tech | Static | One self-contained `index.html` — no backend, no database, no build step |
| Secondary domain | Possibly Namecheap (UNVERIFIED — see §7) | interconnecteddemo.com |

The site is the company's primary asset right now: marketing page + interactive product demos used in live investor and pastor meetings. Uptime and correct deployment matter commercially.

## 2. GitHub Pages hosting — configuration and deploy workflow

**Configuration:**
- Repo `interconnected-demo` under account `noahaustin15`, public (required for free Pages).
- Pages source: **Deploy from a branch → main → / (root)**.
- The entire site is one file, named exactly **`index.html`** (lowercase, single extension).
- Custom domain set in repo Settings → Pages: **www.joininterconnected.com**.
- **Enforce HTTPS**: certificate issuance was in progress at last check ("Unavailable... certificate has not yet been issued"). **First task: verify the checkbox is now enabled; if the cert is still stuck days later, the standard reset is remove the custom domain, wait 5 minutes, re-add it once — never toggle it repeatedly, each toggle restarts certificate issuance.**

**Noah's deploy workflow (he does this himself from a Windows machine):**
1. Download the new HTML build from the product-dev workstream.
2. Rename to `index.html`.
3. In the repo: delete the old `index.html`, then Add file → Upload files → commit.
4. Wait for the green "pages build and deployment" check under Actions.
5. Verify in an incognito tab or with a hard refresh (Ctrl+Shift+R). Appending `?v=2` to the URL is the cache-busting trick he knows.

**Known gotchas (all have actually happened):**
- **`index.html.html` trap:** Windows hides extensions; a file "named" index.html was actually index.html.html and the site 404'd. Always confirm the true filename in the repo file list.
- **Stale cache:** after deploys, the old version often shows until a hard refresh; GitHub's edge cache can lag a few minutes beyond that.
- **GitHub Pages deploy outage (503):** a deployment failed twice with `Failed to create deployment (status: 503)`; confirmed as a GitHub-side incident (major outage that day). Resolution: Actions → failed run → **Re-run failed jobs** once GitHub recovers. Important reassurance: the previously deployed version keeps serving during failed deploys — visitors see nothing broken.
- A clean-slate delete-everything-and-reupload has been used once to resolve filename confusion; it's an acceptable recovery move.

## 3. DNS — joininterconnected.com (managed at Squarespace Domains)

The domain was purchased through Google Workspace signup; Google's registrar operations route to Squarespace, so **DNS lives at account.squarespace.com/domains** (log in with Noah's Google account). Squarespace shows a "This domain is managed by Google Workspace" banner — informational, not blocking.

**Current intended record set (configured and verified working):**

*Website (added manually):*
- A record, host `@` → `185.199.108.153`
- A record, host `@` → `185.199.109.153`
- A record, host `@` → `185.199.110.153`
- A record, host `@` → `185.199.111.153`
- CNAME, host `www` → `noahaustin15.github.io`

*Email + plumbing (pre-existing — NEVER delete or modify):*
- MX, host `@`, priority 1 → `smtp.google.com` (Google Workspace mail)
- TXT, host `@` → `v=spf1 include:_spf.google.com ~all` (SPF)
- TXT, host `google._domainkey` → DKIM key
- CNAME, host `_domainconnect` → Squarespace plumbing (harmless)

*Removed during setup (should stay gone):* the "Squarespace Defaults" preset — four A records to 198.x addresses, a `www` CNAME to `ext-sq.squarespace.com`, and an HTTPS record — all pointed the domain at Squarespace's own hosting and were deleted.

**Checks worth running:** bare-domain behavior (`joininterconnected.com` without www should redirect to the www version via GitHub); confirm no duplicate/conflicting records have crept back.

## 4. Google Workspace

- Tenant: joininterconnected.com. Primary user: **noah@joininterconnected.com**. Admin console: admin.google.com (Noah's account is super-admin).
- MX/SPF/DKIM were auto-configured at purchase and are live (records above). Mail flow is confirmed working both directions.
- **Recommended improvements (not yet done):**
  - Add a **DMARC** TXT record (`_dmarc`, e.g. `v=DMARC1; p=none; rua=mailto:noah@joininterconnected.com` to start) — improves deliverability reputation for cold pastor outreach, which is an active campaign where landing in spam has real cost.
  - Create a **hello@** alias (free) routed to Noah — it was part of the original plan; the site's CTA currently uses noah@ directly, which is fine.
  - Verify 2-Step Verification is enforced on the Google account — it is the root of trust for email, domain DNS (via Squarespace login), and Workspace billing.
- Billing to track: Workspace subscription (monthly, per user) and domain renewal (~$12/yr) — confirm auto-renew is on. A lapsed domain kills site + email simultaneously.

## 5. The site file — technical profile (context you need, product-dev owns it)

- Single self-contained HTML: all CSS/JS inline; interactive demos run entirely client-side with in-memory state; **no localStorage**, no cookies, no analytics, no forms posting anywhere (the pilot CTA is a `mailto:` link).
- **Only external dependency:** Google Fonts (Inter). Everything else — including all avatar images and the logo — is inline SVG by design, because an earlier build that pulled avatar photos from an external service (pravatar) failed to load in Noah's viewer. Keep the site dependency-free; flag any change that adds external calls.
- **Light-mode lock:** `<meta name="color-scheme" content="light only">`, `theme-color` white, and `color-scheme: light only` in CSS. These exist because Android Chrome's forced dark mode auto-inverted the site and made it ugly. Do not remove; know that aggressive extensions/Samsung force-dark can still override (nothing can be done about those).
- Mobile responsiveness is deliberate and tested by Noah on his own devices; the admin demo intentionally side-scrolls on phones inside its frame.

## 6. Hosting strategy and future infrastructure

- **Decision on record: stay on GitHub Pages** for the marketing site. It was explicitly evaluated against Netlify/Vercel (lateral convenience move — drag-and-drop deploys, free form handling), Cloudflare Pages, and paid site builders (rejected). Revisit only on a concrete trigger — e.g., wanting a contact form that captures pilot-church leads server-side (that would favor Netlify), or recurring deploy pain.
- **The future product is a separate universe:** the real app is planned as React Native (mobile) + Node/Express + PostgreSQL + JWT + Socket.io/Firebase on AWS or GCP, multi-tenant with per-church silos, mobile app first and an admin web app second. None of it exists yet (pre-funding). The marketing site can and likely will remain on Pages even after the product launches. When engineering starts, infrastructure decisions belong to the technical co-founder/dev team — your role then becomes accounts, access, and domains.
- Email/domain architecture note: joininterconnected.com is the company's permanent home (chosen after interconnected.com proved taken by an unrelated IT firm, and hyphen/"get" variants were considered and rejected in favor of "join").

## 7. Loose ends and first tasks

1. **Verify Enforce HTTPS is checked** on GitHub Pages and the padlock shows at https://www.joininterconnected.com.
2. **Determine the status of interconnecteddemo.com.** It was selected and set up for purchase at Namecheap earlier in the company's history before plans shifted to joininterconnected.com; whether the purchase completed is unconfirmed in the record. If owned: either 301-redirect it to the main domain or deliberately let it lapse at renewal. If not owned: nothing to do.
3. **Add DMARC**, create hello@ alias, confirm 2FA and auto-renew (see §4).
4. **Favicon + Open Graph / link-preview meta tags** are approved backlog (paused, not rejected): a branded preview card matters because the site link gets texted to pastors and investors. The favicon should use the "gathered dot-cross" logo. Implementation happens in the site file — coordinate with the product-dev agent; your part is verifying the tags render correctly in iMessage/WhatsApp/Slack previews after deploy.
5. **Optional hardening:** free uptime monitor (e.g., UptimeRobot) pinging the live URL; a periodic reminder to keep a local backup copy of the deployed index.html (the chat workstreams currently serve as the de facto backup — the working sandbox has been wiped mid-session before, and the outputs copy was the safety net).

## 8. Access inventory (confirm and secure)

- **GitHub:** account `noahaustin15` — repo admin, Pages settings, Actions.
- **Google:** Noah's Workspace account — email, admin console, billing, and (via Google sign-in) the Squarespace Domains dashboard controlling all DNS.
- **Squarespace Domains:** account.squarespace.com/domains, Google SSO.
- (Possibly) **Namecheap:** only if interconnecteddemo.com was completed — see §7.
- Single-founder reality: everything keys off one Google account and one GitHub account. 2FA on both is the highest-leverage security action available; recovery codes should be stored somewhere safe offline.

## 9. Working with Noah

Non-technical but capable and fast-moving; he executes UI steps himself when given exact click-paths ("Settings → Pages → Custom domain") and screenshots liberally when stuck — screenshots resolve most issues in one round. Explain the *why* in one sentence, then give numbered steps. He's often on his phone; keep instructions copy-pasteable. He has already successfully done: repo creation, uploads, Pages setup, DNS record entry at Squarespace, and Workspace signup — assume competence, skip beginner theory.
