# 2026-10-06 — Home base: dashboard moved to Railway

**Noah's call:** host the dashboard somewhere quicker to reach than claude.ai, without a second GitHub repo. Railway, which Noah already uses and which is connected to Claude.

**Done**
- Railway project `interconnected-hq`, service `dashboard`, connected to `noah-austin/InterConnected-Hub` on `main`. `dashboard/Dockerfile` runs `tools/dashboard.py` at build and serves the page with Caddy. Watch paths: direction, tracker, outbox, logs, tools, dashboard.
- Address: https://interconnected-hq.up.railway.app (no login; `noindex`).
- The generated `dashboard/index.html` is no longer committed (it's in `.gitignore`); Railway builds it.
- Disabled the three-times-a-day claude.ai refresh routine (`trig_019BdXbuz6TTfAQQ4LqyXKgX`). The claude.ai page is retired.
- Updated `skills/dashboard-refresh.md`, `CLAUDE.md` (end-of-session step, repo map), `company/direction.md` (standing operations) and `company/decisions.md`.

**Unchanged:** the brain stays in GitHub. The website stays on GitHub Pages until it needs a backend.
