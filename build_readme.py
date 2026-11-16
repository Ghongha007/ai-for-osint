#!/usr/bin/env python3
"""Builds README.md from research/entries.json. Usage: python3 build_readme.py (run from this folder)"""
import json, os, re
from collections import Counter, OrderedDict
H = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(H, "research", "entries.json"), encoding="utf-8"))
TYPE = {"open source": "Open source", "free web tool": "Free web tool", "freemium": "Freemium", "paid": "Paid",
        "restricted access": "Restricted", "reading": "Reading"}
def cell(s):
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "\\|").strip()
def anchor(s):
    return re.sub(r"[^a-z0-9 -]", "", s.lower()).replace(" ", "-")
cats = OrderedDict()
for e in E:
    cats.setdefault(e["category"], []).append(e)
head = open(os.path.join(H, "HEADER.md"), encoding="utf-8").read()
head = head.replace("{N}", str(len(E))).replace("{CHECKED}", max(e["checked"] for e in E))
out = [head.rstrip(), "", "## Contents", ""] + [f"- [{c}](#{anchor(c)}) ({len(v)})" for c, v in cats.items()]
for c, items in cats.items():
    reading = all(e["type"] == "reading" for e in items)
    out += ["", f"## {c}", ""]
    if reading:
        out += ["| Reading | What it covers | Publisher | Key point | Date |", "|---|---|---|---|---|"]
    else:
        out += ["| Tool | What it is for | Type | Runs | Known limit | Last activity |", "|---|---|---|---|---|---|"]
    for e in sorted(items, key=lambda e: (e["type"] == "reading", e["name"].lower())):
        link = f"[{cell(e['name'])}]({e['url'].strip()})"
        if reading:
            out.append(f"| {link} | {cell(e['what'])} | {cell(e['maintainer'])} | {cell(e['limit'])} | {e.get('last_activity', '')} |")
        elif e["type"] == "reading":
            out.append(f"| {link} | {cell(e['what'])} | Reading | | {cell(e['limit'])} | {e.get('last_activity', '')} |")
        else:
            act = e.get("last_activity", "") + (" (stale)" if e.get("status") == "stale" else "")
            out.append(f"| {link} | {cell(e['what'])} | {TYPE.get(e['type'], cell(e['type']))} | {e['runs'].capitalize()} | {cell(e['limit'])} | {act.strip()} |")
out += ["", open(os.path.join(H, "FOOTER.md"), encoding="utf-8").read().rstrip(), ""]
open(os.path.join(H, "README.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(E), "entries;", dict(Counter(e["type"] for e in E)))
