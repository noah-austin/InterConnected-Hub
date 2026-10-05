# Skill — Refresh the company dashboard (Interconnected HQ)

**Live page:** https://claude.ai/artifact/9H74hgAVxvCa6VqW6cwYcu (private to Noah)
**Source:** `tools/dashboard.py` reads `company/direction.md`, `pipeline/tracker.md`, `work/bd/outbox/` and `logs/` and writes `dashboard/index.html`. **Never edit `dashboard/index.html` by hand.** To change what the page says, change the source files. To change how it looks or what it shows, edit the script.

## When it refreshes
- **Automatically:** routine "Interconnected HQ dashboard refresh" (`trig_019BdXbuz6TTfAQQ4LqyXKgX`), weekdays at 7:27am, 12:27pm and 5:27pm Central. It fires into the build session (`session_01DeSJtB5vfZZxrV7NHb3cab`), which owns the page.
- **At the end of any session** that changed one of the source files, if that session has the Artifact tool.

## Steps
1. `python3 tools/dashboard.py`
2. Publish `dashboard/index.html` with the Artifact tool. In the session that first published it, use the same file path. From any other session, pass `url: https://claude.ai/artifact/9H74hgAVxvCa6VqW6cwYcu` (read it first, as the tool requires). Never publish without the url from another session; that creates a second, separate page.
3. Commit `dashboard/index.html` to `main` with the source changes.

If a session has no Artifact tool, do steps 1 and 3 only; the next scheduled refresh republishes.

## What the page reads (keep these formats stable)
- `direction.md` → "Do now" numbered items (`N. **Title.** detail`; mark done with `DONE` or strike the line with `~~`), "Decisions waiting on Noah" bullets, "Parked" bullets, "Standing operations" bullets.
- `tracker.md` → the Scoreboard table, and rows in sections A–D (`| # | Church | Contact | Status | Last touch | Next action | Next date |`).
- `work/bd/outbox/*.md` → `# Title` and the `**Why now:**` line.
- `logs/*.md` → the `# ` heading of the 8 newest files.
