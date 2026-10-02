# Interconnected — Company Brain

This repo is Interconnected's company brain plus the forward copy of the website in `/docs/`.
Every agent session reads it before working and writes back what it did. Threads are disposable; files are the job.

The company name is **Interconnected** — never "Believers In Business," never "Interconnect."

## Read order (every session)
1. `/company/direction.md` — the steering file. Current priorities, what's working, what to stop.
2. `/company/overview.md`
3. Your role file in `/roles/`
4. The files your task touches.

## End of every session
- Update the files you changed.
- Append one entry to `/logs/` (date, role, what was done, what changed).
- Update `/company/decisions.md` if anything was decided.

## Guardrails (verbatim — these are law)
- A human approves anything that leaves the building. Agents draft; Noah sends, publishes, and spends. No agent ever sends email, submits forms, or posts publicly.
- No agent gets payment methods.
- A session that reads untrusted content (websites, inbound email) must not also send messages externally.
- Credentials live in environment/MCP config, never in repo files.
- Every run leaves a log entry; every claim of completed work points to its output (file path or diff).
- Site deploys touch `/docs/index.html` only; the site's *content* is Dex's role, its *deployment* is a mechanical step any session may perform when Noah says deploy.

Connector rule: BD (Sonny) sessions get Gmail read/draft, never send. Drafts are staged in the repo under `/work/bd/outbox/`, not in Gmail. Product and IT sessions get no inbox access.

## Interim deploy rule (until the domain cutover)
- The **live** site at www.joininterconnected.com is still served by the OLD repo, `noahaustin15/interconnected-demo`. Live deploys go there — Noah, manually, old workflow.
- This repo's `/docs/` is the **forward copy**. Keep it in sync with every new build, but changing it does **not** change the live site yet.
- Do **not** add a `CNAME` file to `/docs/` until cutover day. The domain is still bound to the old account's Pages; a CNAME here causes a conflict. The cutover steps are logged in `/company/direction.md`.
- `/docs/` holds only the site: `index.html`, `og-image.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`. Nothing else lives there.

## Growth rules
Two active roles only (Sonny — BD, Dex — Product). Add a role only after the current ones run ~2 weeks with few outputs needing major rewrites. No inter-agent messaging, orchestration dashboards, manager agents, databases, or send-automation. Markdown files are the database. If a step feels like infrastructure for infrastructure's sake, stop and ask Noah.
