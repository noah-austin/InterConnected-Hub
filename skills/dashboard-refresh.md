# Skill — The company dashboard (Interconnected HQ)

**Live page:** https://interconnected-hq.up.railway.app (no login; unlisted, `noindex`)
**Hosting:** Railway project `interconnected-hq`, service `dashboard` (project `38f9581f-de93-4d51-a215-593784b18fce`, service `c00eec95-f6f6-4163-8f20-2f20f569d571`). It's connected to `noah-austin/InterConnected-Hub`, branch `main`.
**Source:** `tools/dashboard.py` reads `company/direction.md`, `pipeline/tracker.md`, `work/bd/outbox/` and `logs/` and writes the page. `dashboard/Dockerfile` runs it during each Railway build and serves the result. The generated `dashboard/index.html` is **not** committed.

## How it refreshes
**Automatically, on every push to `main`** that touches `company/direction.md`, `pipeline/tracker.md`, `work/bd/outbox/`, `logs/`, `tools/` or `dashboard/` (Railway watch paths). A build takes a minute or two. There's no schedule and nothing to publish by hand: if a session lands its work on `main` (per `CLAUDE.md`), the dashboard follows.

## Changing it
- **What it says:** change the source files (direction, tracker, outbox, logs). Never edit the page.
- **How it looks or what it shows:** edit `tools/dashboard.py`. Preview locally with `python3 tools/dashboard.py` (writes `dashboard/index.html`, which git ignores), then push.
- **If a deploy fails:** check the Railway build logs (Railway connector: `list-deployments`, `get-logs` with `types: ["build"]`). The previous version keeps serving until a build succeeds.

## What the page reads (keep these formats stable)
- `direction.md`: "Do now" numbered items (`N. **Title.** detail`; mark done with `DONE` or strike the line with `~~`), "Decisions waiting on Noah" bullets, "Parked" bullets, "Standing operations" bullets.
- `tracker.md`: the Scoreboard table and rows in sections A–D (`| # | Church | Contact | Status | Last touch | Next action | Next date |`).
- `work/bd/outbox/*.md`: the `# Title` and `**Why now:**` lines.
- `logs/*.md`: the `# ` heading of the 8 newest files.

## Later
- Custom address `hq.joininterconnected.com`: add it on cutover day (Railway `generate-domain` with the custom domain, then one CNAME in Squarespace).
- The old claude.ai page (https://claude.ai/artifact/9H74hgAVxvCa6VqW6cwYcu) is retired and no longer refreshed.
