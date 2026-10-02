# Skill — Site deploy checklist

> Source: Mack's Sep 24 handoff, the IT briefing §2, Dex's Sep 24 handoff §1. Deploys happen **only when Noah says "deploy."** The contents of `index.html` are Dex's; deploying it is a mechanical step any session may perform.

## Before anything
- [ ] Noah has said "deploy" for this specific build.
- [ ] Dex's QA checklist (`roles/dex.md`) passed and is recorded next to the staged file in `work/product/staging/`.
- [ ] Filename is exactly **`index.html`**: lowercase, one extension. **Windows hides extensions; `index.html.html` has shipped before and 404'd the site.** Confirm the true filename in the repo's file list.
- [ ] If any root asset changed (`og-image.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), it goes **in the same commit**.

## A. Interim — until the domain cutover (the live site is the OLD repo)
The live site is served from `noahaustin15/interconnected-demo` (repo root). **Noah does this himself, manually:**
1. Download the staged `index.html` (and any changed assets).
2. Confirm the filename is exactly `index.html`, not `index.html.html`.
3. Old repo → delete the old `index.html` → Add file → Upload files → commit. **Do not touch the `CNAME` file there.**
4. Actions tab → wait for the green **"pages build and deployment"** check.
5. Verify with a hard refresh (Ctrl+Shift+R), an incognito window, or `?v=2` on the URL. The edge cache can lag a few minutes.
6. Then, in **this** repo, copy the same files into `docs/` and commit ("sync forward copy"). The forward copy must always match what's live.

## B. After the domain cutover (this repo serves the site)
1. Copy the staged files into `docs/`. Only the site lives there.
2. Commit to `main` → wait for the green "pages build and deployment" check.
3. Verify: hard refresh / incognito, padlock present, the change visible.

## If it goes wrong
- **503 "Failed to create deployment"** is usually a GitHub-side outage. Actions → failed run → **Re-run failed jobs** once GitHub recovers. Don't change files. The previous version keeps serving meanwhile.
- **Broken build live:** revert from git history (previous commit's `index.html`) and redeploy. Tell Dex what broke.
- **Never** toggle the Pages custom domain or Enforce HTTPS to "fix" a deploy.

## Log it
`/logs/` entry: what deployed, commit hash, md5 of `index.html`, verification result.
