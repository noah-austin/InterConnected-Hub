#!/usr/bin/env python3
"""Build the company dashboard from the brain's own files.

Reads company/direction.md, pipeline/tracker.md, work/bd/outbox/ and logs/,
writes dashboard/index.html. Railway runs this on every push to main (see
dashboard/Dockerfile), so the live page always matches the repo. The output is
not committed. To preview locally:  python3 tools/dashboard.py
"""
import html
import os
import re
import subprocess
from datetime import datetime, timezone, timedelta
try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dashboard", "index.html")
try:
    CENTRAL = ZoneInfo("America/Chicago")
except Exception:
    CENTRAL = timezone(timedelta(hours=-5))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def section(md, heading_prefix):
    """Body of the first '## ' section whose heading starts with heading_prefix."""
    m = re.search(r"^## " + re.escape(heading_prefix) + r".*?$\n(.*?)(?=^## |\Z)", md, re.M | re.S)
    return m.group(1) if m else ""


def inline(text):
    """Escape, then render the small markdown subset the brain uses."""
    t = html.escape(text.strip(), quote=False)
    t = re.sub(r"~~(.+?)~~", r"<s>\1</s>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"(?<![\w*])\*([^*]+)\*(?!\w)", r"<em>\1</em>", t)
    return t


def plain(text):
    return re.sub(r"[*`~]", "", text).strip()


def first_sentence(text):
    return re.split(r"(?<=[.])\s", plain(text))[0]


def table_rows(md):
    rows = []
    for line in md.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


# ---------- direction.md ----------
direction = read("company/direction.md")

do_now = []
for line in section(direction, "Do now").splitlines():
    m = re.match(r"^(\d+[a-z]?)\.\s+(.*)$", line.strip())
    if not m:
        continue
    num, body = m.groups()
    title_m = re.match(r"\*\*(.+?)\*\*\.?\s*(.*)", body)
    title, rest = (title_m.group(1), title_m.group(2)) if title_m else (body, "")
    done = bool(re.search(r"\bDONE\b|^~~", body)) or "✓" in body
    sentences = re.split(r"(?<=[.)])\s+", rest)
    detail = sentences[0] if sentences and sentences[0] else ""
    do_now.append({"num": num, "title": title.rstrip("."), "detail": detail, "done": done})

waiting = []
decided_note = ""
for line in section(direction, "Decisions waiting on Noah").splitlines():
    s = line.strip()
    if s.startswith("- "):
        waiting.append(s[2:])
    elif s.lower().startswith("decided"):
        decided_note = s

parked = []
for line in section(direction, "Parked").splitlines():
    s = line.strip()
    if s.startswith("- "):
        m = re.match(r"- \*\*(.+?)\*\*[.:]?\s*(.*)", s)
        if m:
            first = re.split(r"(?<=\.)\s", m.group(2))[0] if m.group(2) else ""
            parked.append((m.group(1).rstrip(".:"), first))
        else:
            parked.append((plain(s[2:]), ""))

standing = [l.strip()[2:] for l in section(direction, "Standing operations").splitlines() if l.strip().startswith("- ")]

# ---------- tracker.md ----------
tracker = read("pipeline/tracker.md")

score = []
for cells in table_rows(section(tracker, "Scoreboard")):
    if len(cells) >= 2 and cells[0] != "Metric":
        score.append((cells[0], cells[1]))
score_heading = re.search(r"^## (Scoreboard.*)$", tracker, re.M)
score_heading = score_heading.group(1) if score_heading else "Scoreboard"

verified = re.search(r"^\*\*Last verified:\*\*\s*(.+)$", tracker, re.M)
verified = verified.group(1) if verified else ""
latest_note = ""
for m in re.finditer(r"^\*\*(Oct|Nov|Dec|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep)\s+\d+[^*]*\*\*.*$", tracker, re.M):
    latest_note = m.group(0)  # keep the last dated note in the header block


def bucket(status, action):
    s, a = status.lower(), action.lower()
    if any(k in s for k in ("loi", "meeting booked", "met (")):
        return "hot"
    if s.startswith("replied"):
        return "hot"
    if "declined" in s or "dormant" in s or s.startswith("closed") or s.startswith("see row"):
        return "closed"
    if "no touch" in a or "do not touch" in a:
        return "hold"
    if "drafted" in a or "draft:" in a or "drafted" in s or "never contacted" in s:
        return "ready"
    if s.startswith("sent"):
        return "waiting"
    return "hold"


BUCKETS = [
    ("hot", "In conversation", "Replied, meeting, or LOI"),
    ("ready", "Ready to send", "Drafted; waiting on Noah to press send"),
    ("waiting", "Sent, no reply", "Out in the field, nothing drafted"),
    ("hold", "On hold / research", "Sequenced, needs a contact, or Noah's lane"),
    ("closed", "Closed or dormant", "Declined, parked, or merged into another row"),
]

pipeline = []
current_group = ""
for line in tracker.splitlines():
    h = re.match(r"^## ([A-D])\. (.*)$", line)
    if h:
        current_group = h.group(2)
        continue
    if not current_group or not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 7 or not cells[0].isdigit():
        continue
    num, church, contact, status, last, action, nxt = cells[:7]
    pipeline.append({
        "num": int(num), "church": church, "contact": contact.split(" · ")[0],
        "status": status, "last": last, "action": action, "next": nxt,
        "group": current_group, "bucket": bucket(status, action),
    })
counts = {k: sum(1 for p in pipeline if p["bucket"] == k) for k, _, _ in BUCKETS}
live = [p for p in pipeline if p["group"].startswith("Live")]

# ---------- outbox ----------
outbox = []
obdir = os.path.join(ROOT, "work", "bd", "outbox")
for name in sorted(os.listdir(obdir)):
    if not name.endswith(".md") or name == "README.md":
        continue
    text = read(os.path.join("work", "bd", "outbox", name))
    title = re.search(r"^# (.+)$", text, re.M)
    why = re.search(r"^\*\*Why now:\*\*\s*(.+)$", text, re.M)
    outbox.append({
        "date": name[:10],
        "title": title.group(1) if title else name,
        "why": re.split(r"(?<=\.)\s", why.group(1))[0] if why else "",
        "path": "work/bd/outbox/" + name,
    })
outbox.sort(key=lambda o: o["date"], reverse=True)

# ---------- logs ----------
logs = []
for name in sorted(os.listdir(os.path.join(ROOT, "logs")), reverse=True):
    if not name.endswith(".md"):
        continue
    title = re.search(r"^# (.+)$", read(os.path.join("logs", name)), re.M)
    t = title.group(1) if title else name
    t = re.sub(r"^\d{4}-\d{2}-\d{2}\s*[—-]\s*", "", t)
    logs.append((name[:10], t))
logs = logs[:8]

commit = os.environ.get("RAILWAY_GIT_COMMIT_SHA", "")[:7]
if not commit:
    try:
        commit = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%h"], capture_output=True, text=True).stdout.strip()
    except Exception:
        commit = ""
now = datetime.now(CENTRAL)
stamp = now.strftime("%a %b %-d, %-I:%M %p") + " Central"


# ---------- render ----------
def esc(s):
    return html.escape(s, quote=True)


def short_date(iso):
    return esc(iso[5:].replace("-", "/"))


def score_value(label):
    for k, v in score:
        if label.lower() in k.lower():
            return v
    return "—"


def big(v):
    m = re.match(r"^\s*(\d+)\s*/\s*(\d+)", v)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"^\s*(\d+)", v)
    return (m.group(1), "") if m else (v, "")


tiles = []
for label, key, note_fn in [
    ("Emails sent", "Outreach emails sent", lambda v: "since Aug 24"),
    ("Replies", "Replies received", lambda v: re.sub(r"^\d+\s*", "", v).strip("() ") or "received"),
    ("Meetings held", "Meetings offered", lambda v: (big(v)[0] + " offered") if big(v)[1] else ""),
    ("LOIs signed", "LOIs in discussion", lambda v: (big(v)[0] + " in discussion") if big(v)[1] else ""),
    ("Referrals", "Referrals collected", lambda v: "collected"),
    ("Pricing reads", "Pricing reactions", lambda v: "three-question captures"),
]:
    v = score_value(key)
    a, b = big(v)
    value = b if b and label in ("Meetings held", "LOIs signed") else a
    tiles.append((label, value, note_fn(v)))

total = max(1, len(pipeline))
funnel_bar = "".join(
    f'<span class="seg seg-{k}" style="flex:{counts[k]}" title="{esc(name)}: {counts[k]}"></span>'
    for k, name, _ in BUCKETS if counts[k]
)
funnel_legend = "".join(
    f'<li><span class="dot seg-{k}"></span><span class="lg-name">{esc(name)}</span>'
    f'<span class="lg-n">{counts[k]}</span><span class="lg-note">{esc(note)}</span></li>'
    for k, name, note in BUCKETS
)

def todo_li(t):
    detail = f'<p class="todo-detail">{inline(t["detail"])}</p>' if t["detail"] else ""
    state = ("pill-done", "Done") if t["done"] else ("pill-open", "Open")
    return (f'<li class="todo{" done" if t["done"] else ""}"><span class="num">{esc(t["num"])}</span>'
            f'<div><p class="todo-title">{inline(t["title"])}</p>{detail}</div>'
            f'<span class="pill {state[0]}">{state[1]}</span></li>')


todo_items = "".join(todo_li(t) for t in do_now)

outbox_items = "".join(
    f'<li><div class="ob-head"><p class="ob-title">{inline(o["title"])}</p><span class="date">{short_date(o["date"])}</span></div>'
    f'<p class="ob-why">{inline(o["why"])}</p><code class="path">{esc(o["path"])}</code></li>'
    for o in outbox
)

live_items = "".join(
    f'<li><div class="lead-head"><p class="lead-name">{inline(p["church"])}</p><span class="pill pill-{p["bucket"]}">{esc(dict((k, n) for k, n, _ in BUCKETS)[p["bucket"]])}</span></div>'
    f'<p class="lead-contact">{inline(p["contact"])}</p>'
    f'<p class="lead-action">{inline(first_sentence(p["action"]))}</p></li>'
    for p in live
)

waiting_items = "".join(f"<li>{inline(w)}</li>" for w in waiting)
parked_items = "".join(
    f'<li><strong>{inline(t)}</strong>{(" " + inline(d)) if d else ""}</li>' for t, d in parked
)
log_items = "".join(
    f'<li><span class="date">{short_date(d)}</span><span>{inline(t)}</span></li>' for d, t in logs
)
standing_items = "".join(f"<li>{inline(s)}</li>" for s in standing)

pipe_rows = "".join(
    f'<tr><td class="n">{p["num"]}</td><td>{inline(p["church"])}<span class="sub">{inline(p["contact"])}</span></td>'
    f'<td><span class="pill pill-{p["bucket"]}">{inline(p["status"])}</span></td><td class="n">{inline(p["last"])}</td>'
    f'<td>{inline(first_sentence(p["action"]))}</td></tr>'
    for p in sorted(pipeline, key=lambda p: [b[0] for b in BUCKETS].index(p["bucket"]))
)

ready_n = counts["ready"]
open_todos = sum(1 for t in do_now if not t["done"])
headline = (
    f"{open_todos} things on your list, {ready_n} conversations drafted and waiting on you to press send."
    if ready_n else f"{open_todos} things on your list."
)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#F6F8FC">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 26 32'%3E%3Cg fill='%232563EB'%3E%3Ccircle cx='13' cy='4' r='3'/%3E%3Ccircle cx='13' cy='11' r='3'/%3E%3Ccircle cx='6' cy='13' r='2.6'/%3E%3Ccircle cx='20' cy='13' r='2.6'/%3E%3Ccircle cx='13' cy='18' r='3'/%3E%3Ccircle cx='13' cy='25' r='3'/%3E%3C/g%3E%3C/svg%3E">
<title>Interconnected HQ</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Layout: one column on phones, a two-column board on desktop. Summary (standings) first, then your moves, then the pipeline detail. */
:root {{
  --bg: #F6F8FC; --surface: #FFFFFF; --ink: #1F2937; --muted: #5B6474; --line: #E3E8F1;
  --brand: #2563EB; --brand-soft: #DBEAFE; --navy: #0F1B33;
  --hot: #059669; --ready: #2563EB; --waiting: #B45309; --hold: #7C3AED; --closed: #94A0B4;
  --hot-bg: #E7F6F0; --ready-bg: #E6EEFD; --waiting-bg: #FDF1E3; --hold-bg: #F1EBFD; --closed-bg: #EEF1F6;
  --font-ui: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0B1426; --surface: #111D35; --ink: #E6ECF7; --muted: #9AA8C1; --line: #22304D;
  --brand: #6B9BFF; --brand-soft: #1B2B4F; --navy: #0F1B33;
  --hot: #34D399; --ready: #6B9BFF; --waiting: #F5B661; --hold: #B69CFF; --closed: #7C89A3;
  --hot-bg: #10352B; --ready-bg: #182A50; --waiting-bg: #3A2A12; --hold-bg: #2A2150; --closed-bg: #1A2640;
  color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #0B1426; --surface: #111D35; --ink: #E6ECF7; --muted: #9AA8C1; --line: #22304D;
  --brand: #6B9BFF; --brand-soft: #1B2B4F; --navy: #0F1B33;
  --hot: #34D399; --ready: #6B9BFF; --waiting: #F5B661; --hold: #B69CFF; --closed: #7C89A3;
  --hot-bg: #10352B; --ready-bg: #182A50; --waiting-bg: #3A2A12; --hold-bg: #2A2150; --closed-bg: #1A2640;
  color-scheme: dark; }}
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font-family: var(--font-ui); font-size: 15px; line-height: 1.5; padding-inline: 16px; padding-block: 20px 48px; }}
.wrap {{ max-width: 1120px; margin: 0 auto; display: grid; gap: 20px; }}
header.top {{ display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 8px 24px; }}
.brand {{ display: flex; align-items: center; gap: 10px; }}
.brand svg {{ width: 26px; height: 32px; flex: none; }}
h1 {{ font-size: 1.5rem; font-weight: 800; letter-spacing: -0.01em; margin: 0; }}
.stamp {{ color: var(--muted); font-size: 0.82rem; margin: 0; }}
.stamp code {{ font-family: var(--font-mono); font-size: 0.78rem; }}
.headline {{ font-size: 1.05rem; font-weight: 500; margin: 0; max-width: 60ch; text-wrap: balance; }}
.label {{ text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.72rem; font-weight: 700; color: var(--muted); margin: 0 0 10px; }}
.panel {{ background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 18px; min-width: 0; }}
.tiles {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; }}
.tile {{ background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 14px; }}
.tile .v {{ font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; line-height: 1.1; }}
.tile .k {{ font-weight: 600; font-size: 0.85rem; }}
.tile .note {{ color: var(--muted); font-size: 0.78rem; }}
.tile.zero .v {{ color: var(--muted); }}
.bar {{ display: flex; height: 14px; border-radius: 7px; overflow: hidden; gap: 2px; background: var(--line); }}
.seg {{ display: block; min-width: 6px; }}
.seg-hot {{ background: var(--hot); }} .seg-ready {{ background: var(--ready); }} .seg-waiting {{ background: var(--waiting); }}
.seg-hold {{ background: var(--hold); }} .seg-closed {{ background: var(--closed); }}
.legend {{ list-style: none; padding: 0; margin: 14px 0 0; display: grid; gap: 6px; }}
.legend li {{ display: grid; grid-template-columns: 12px minmax(0, 9.5rem) 2.2rem minmax(0, 1fr); align-items: baseline; gap: 10px; font-size: 0.88rem; }}
.dot {{ width: 10px; height: 10px; border-radius: 50%; display: inline-block; }}
.lg-name {{ font-weight: 600; }} .lg-n {{ font-variant-numeric: tabular-nums; font-weight: 700; text-align: right; }} .lg-note {{ color: var(--muted); font-size: 0.8rem; }}
.board {{ display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 20px; align-items: start; }}
.col {{ display: grid; gap: 20px; min-width: 0; }}
ul.clean {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 0; }}
ul.clean > li {{ padding-block: 12px; border-top: 1px solid var(--line); min-width: 0; }}
ul.clean > li:first-child {{ border-top: 0; padding-top: 0; }}
.todo {{ display: grid; grid-template-columns: 2rem minmax(0, 1fr) auto; gap: 10px; align-items: start; }}
.num {{ font-family: var(--font-mono); font-size: 0.8rem; color: var(--brand); background: var(--brand-soft); border-radius: 6px; text-align: center; padding: 2px 0; }}
.todo-title {{ font-weight: 600; margin: 0; }}
.todo-detail {{ margin: 2px 0 0; color: var(--muted); font-size: 0.86rem; overflow-wrap: anywhere; }}
.todo.done .todo-title {{ text-decoration: line-through; color: var(--muted); }}
.pill {{ display: inline-block; font-size: 0.72rem; font-weight: 600; border-radius: 999px; padding: 2px 9px; white-space: nowrap; }}
.pill-open {{ background: var(--waiting-bg); color: var(--waiting); }} .pill-done {{ background: var(--hot-bg); color: var(--hot); }}
.pill-hot {{ background: var(--hot-bg); color: var(--hot); }} .pill-ready {{ background: var(--ready-bg); color: var(--ready); }}
.pill-waiting {{ background: var(--waiting-bg); color: var(--waiting); }} .pill-hold {{ background: var(--hold-bg); color: var(--hold); }}
.pill-closed {{ background: var(--closed-bg); color: var(--closed); }}
td .pill {{ white-space: normal; }}
.ob-head, .lead-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 10px; }}
.ob-title, .lead-name {{ font-weight: 600; margin: 0; min-width: 0; }}
.ob-why, .lead-contact, .lead-action {{ margin: 4px 0 0; font-size: 0.86rem; }}
.ob-why, .lead-contact {{ color: var(--muted); }}
.date {{ font-family: var(--font-mono); font-size: 0.78rem; color: var(--muted); white-space: nowrap; }}
code, .path {{ font-family: var(--font-mono); font-size: 0.78em; overflow-wrap: anywhere; }}
.path {{ display: inline-block; margin-top: 6px; color: var(--muted); }}
ul.bullets {{ margin: 0; padding-left: 1.1rem; display: grid; gap: 8px; font-size: 0.9rem; }}
.aside {{ color: var(--muted); font-size: 0.84rem; margin: 12px 0 0; }}
.activity li {{ display: grid; grid-template-columns: 3.2rem minmax(0, 1fr); gap: 10px; font-size: 0.88rem; }}
details.pipe summary {{ cursor: pointer; font-weight: 600; list-style: none; display: flex; justify-content: space-between; align-items: center; gap: 12px; }}
details.pipe summary::-webkit-details-marker {{ display: none; }}
details.pipe summary::after {{ content: "Show"; color: var(--brand); font-size: 0.85rem; }}
details.pipe[open] summary::after {{ content: "Hide"; }}
details.pipe summary:focus-visible, a:focus-visible {{ outline: 2px solid var(--brand); outline-offset: 3px; border-radius: 4px; }}
.tablewrap {{ overflow-x: auto; margin-top: 14px; }}
table {{ border-collapse: collapse; width: 100%; min-width: 640px; font-size: 0.85rem; }}
th {{ text-align: left; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); padding: 6px 8px; border-bottom: 1px solid var(--line); }}
td {{ padding: 9px 8px; border-bottom: 1px solid var(--line); vertical-align: top; }}
td.n {{ font-variant-numeric: tabular-nums; white-space: nowrap; color: var(--muted); }}
.sub {{ display: block; color: var(--muted); font-size: 0.8rem; }}
footer {{ color: var(--muted); font-size: 0.8rem; max-width: 70ch; }}
@media (max-width: 820px) {{ .board {{ grid-template-columns: minmax(0, 1fr); }} .legend li {{ grid-template-columns: 12px minmax(0, 1fr) 2.2rem; }} .lg-note {{ display: none; }} }}
</style>

</head>
<body>
<div class="wrap">
  <header class="top">
    <div>
      <div class="brand">
        <svg viewBox="0 0 26 32" aria-hidden="true"><g fill="var(--brand)">
          <circle cx="13" cy="3" r="2.3"/><circle cx="13" cy="9" r="2.3"/><circle cx="7" cy="12" r="2.1"/><circle cx="19" cy="12" r="2.1"/>
          <circle cx="2.5" cy="12" r="1.8" opacity=".7"/><circle cx="23.5" cy="12" r="1.8" opacity=".7"/><circle cx="13" cy="15" r="2.3"/>
          <circle cx="13" cy="21" r="2.3"/><circle cx="13" cy="27" r="2.3"/><circle cx="13" cy="31" r="1" opacity=".6"/></g></svg>
        <h1>Interconnected HQ</h1>
      </div>
      <p class="stamp">Updated {esc(stamp)} · built from the repo{f" at <code>{esc(commit)}</code>" if commit else ""}</p>
    </div>
    <p class="headline">{esc(headline)}</p>
  </header>

  <section aria-labelledby="standings">
    <p class="label" id="standings">Standings · {esc(score_heading.replace("Scoreboard", "").strip(" ()") or "current")}</p>
    <div class="tiles">
      {"".join(f'<div class="tile{" zero" if v in ("0", "—") else ""}"><div class="v">{esc(v)}</div><div class="k">{esc(l)}</div><div class="note">{esc(n)}</div></div>' for l, v, n in tiles)}
    </div>
  </section>

  <section class="panel" aria-labelledby="pipe-label">
    <p class="label" id="pipe-label">Pipeline · {len(pipeline)} churches and multipliers</p>
    <div class="bar" role="img" aria-label="Pipeline by stage">{funnel_bar}</div>
    <ul class="legend">{funnel_legend}</ul>
  </section>

  <div class="board">
    <div class="col">
      <section class="panel" aria-labelledby="todo-label">
        <p class="label" id="todo-label">Your moves, in order</p>
        <ul class="clean">{todo_items}</ul>
      </section>
      <section class="panel" aria-labelledby="ob-label">
        <p class="label" id="ob-label">Drafts ready to send · in Gmail Drafts</p>
        <ul class="clean">{outbox_items or "<li>Nothing drafted right now.</li>"}</ul>
      </section>
    </div>
    <div class="col">
      <section class="panel" aria-labelledby="lead-label">
        <p class="label" id="lead-label">Warmest leads</p>
        <ul class="clean">{live_items}</ul>
      </section>
      <section class="panel" aria-labelledby="wait-label">
        <p class="label" id="wait-label">Waiting on your answer</p>
        <ul class="bullets">{waiting_items or "<li>Nothing.</li>"}</ul>
        {f'<p class="aside">{inline(decided_note)}</p>' if decided_note else ""}
      </section>
      <section class="panel activity" aria-labelledby="log-label">
        <p class="label" id="log-label">Recent activity</p>
        <ul class="clean">{log_items}</ul>
      </section>
    </div>
  </div>

  <section class="panel">
    <details class="pipe" id="pipeline">
      <summary>Every row in the pipeline ({len(pipeline)})</summary>
      <div class="tablewrap"><table>
        <thead><tr><th>#</th><th>Church / contact</th><th>Status</th><th>Last touch</th><th>Next action</th></tr></thead>
        <tbody>{pipe_rows}</tbody>
      </table></div>
    </details>
  </section>

  <div class="board">
    <section class="panel" aria-labelledby="park-label">
      <p class="label" id="park-label">Parked</p>
      <ul class="bullets">{parked_items}</ul>
    </section>
    <section class="panel" aria-labelledby="ops-label">
      <p class="label" id="ops-label">Standing operations</p>
      <ul class="bullets">{standing_items or "<li>None.</li>"}</ul>
      {f'<p class="aside">Inbox last verified: {inline(verified)}</p>' if verified else ""}
    </section>
  </div>

  <footer>
    This page is generated from the company repo (<code>company/direction.md</code>, <code>pipeline/tracker.md</code>,
    <code>work/bd/outbox/</code>, <code>logs/</code>) by <code>tools/dashboard.py</code>. It rebuilds automatically
    every time a change lands on the repo's main branch. To change what it says, tell any session; never edit the page.
  </footer>
</div>
</body>
</html>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(page)
print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(pipeline)} pipeline rows, {len(do_now)} moves, {len(outbox)} drafts, {len(logs)} log entries")
