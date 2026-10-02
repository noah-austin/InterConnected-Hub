# Direction

> The steering file. Noah/Buford edit it; every role reads it first.
> Phase 0 stub — current priorities are seeded in Phase 1 and reconciled in Phase 2.

## Logged for later — Domain cutover (do NOT execute until Noah says go)
Pick a day with no pastor meeting. Mack's handoff §3–4 holds the detailed reference.
1. Squarespace DNS → edit the `www` CNAME record's data to `noah-austin.github.io`. Touch nothing else — the four apex A records, MX, SPF, DKIM, DMARC all stay.
2. Add the held `CNAME` file (contents: `www.joininterconnected.com`) to `/docs/` of this repo. It is not in the repo until then.
3. This repo → Settings → Pages → custom domain `www.joininterconnected.com`.
4. Wait for the DNS check, then the certificate, then Enforce HTTPS. Never toggle settings while provisioning.
5. Verify the padlock in an incognito window and on cellular.
6. Retire the old repo `noahaustin15/interconnected-demo`: archive it, do not delete its history.
