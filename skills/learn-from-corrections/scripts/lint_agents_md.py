#!/usr/bin/env python3
"""Lint an AGENTS.md / CLAUDE.md rules file.

Flags duplicate or near-duplicate rules, vague rules, rules without a reason,
overlong rules, and a file that has grown too large to load every session.

Usage:
    python3 lint_agents_md.py [path]          # default: ./AGENTS.md, then ./CLAUDE.md
    python3 lint_agents_md.py path --json     # machine-readable output

Exit code: 0 = clean, 1 = warnings found, 2 = file not found.
Works on Python 3.8+ with no dependencies.
"""
import difflib
import json
import os
import re
import sys

MAX_LINES = 150
MAX_RULE_CHARS = 200
SIMILARITY = 0.82

VAGUE = [
    r"\bbe careful\b", r"\bbest practices?\b", r"\bclean code\b", r"\bgood code\b",
    r"\bproperly\b", r"\bas needed\b", r"\bwhen appropriate\b", r"\bif possible\b",
    r"\bmake sure (it|everything) works\b", r"\bbe smart\b", r"\buse common sense\b",
    r"\bkeep it simple\b", r"\bhigh[- ]quality\b",
]
REASON_MARKERS = re.compile(r"(—|--| - |\bbecause\b|\bso that\b|\bso\b|\bsince\b|\botherwise\b|:|;|\()", re.I)
SHOUTING = re.compile(r"!{2,}|\b[A-Z]{5,}\b")
STOP = set("a an the to for of in on and or with is are be it this that use always never do don't not".split())


def normalize(text):
    text = re.sub(r"`[^`]*`", lambda m: m.group(0).lower(), text)
    words = re.findall(r"[a-z0-9_./-]+", text.lower())
    return " ".join(w for w in words if w not in STOP)


def find_default():
    for name in ("AGENTS.md", "CLAUDE.md"):
        if os.path.exists(name):
            return name
    return None


def extract_rules(lines):
    """Yield (line_no, section, text) for every bullet rule outside code fences."""
    section = "(top)"
    in_fence = False
    for i, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = re.match(r"^#{1,6}\s+(.*)", line)
        if heading:
            section = heading.group(1).strip()
            continue
        bullet = re.match(r"^\s*(?:[-*+]|\d+\.)\s+(.*)", line)
        if bullet and bullet.group(1).strip():
            yield i, section, bullet.group(1).strip()


def lint(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    issues = []

    def add(line, kind, msg):
        issues.append({"line": line, "kind": kind, "message": msg})

    if len(lines) > MAX_LINES:
        add(0, "size", "File has %d lines (limit %d). Merge overlapping rules or move detail into a linked doc."
            % (len(lines), MAX_LINES))

    rules = list(extract_rules(lines))
    seen = []
    for line_no, section, text in rules:
        if text.startswith("<") and text.endswith(">"):
            add(line_no, "placeholder", "Template placeholder not filled in: %s" % text)
            continue
        norm = normalize(text)
        for other_no, other_norm, other_text in seen:
            if norm and (norm == other_norm or difflib.SequenceMatcher(None, norm, other_norm).ratio() >= SIMILARITY):
                add(line_no, "duplicate", "Looks like a duplicate of line %d: \"%s\"" % (other_no, other_text))
                break
        seen.append((line_no, norm, text))

        for pattern in VAGUE:
            if re.search(pattern, text, re.I):
                add(line_no, "vague", "Vague wording (%s). Say exactly what to do, so it can be checked."
                    % re.search(pattern, text, re.I).group(0))
                break
        if len(text) > MAX_RULE_CHARS:
            add(line_no, "long", "Rule is %d characters. Split it or move detail into a linked doc." % len(text))
        if SHOUTING.search(re.sub(r"`[^`]*`", "", text)):
            add(line_no, "shouting", "Caps or '!!' don't make agents comply more; a reason does.")
        is_command_line = re.match(r"^[A-Z][\w /-]{0,20}:\s*`", text)
        if not is_command_line and re.match(r"^(never|don't|do not|always|avoid|only)\b", text, re.I) \
                and not REASON_MARKERS.search(text):
            add(line_no, "no-reason", "Strict rule without a reason. Add why (e.g. '— the lockfile is pnpm-lock.yaml').")

    if not rules:
        add(0, "empty", "No bullet rules found.")
    return {"path": path, "lines": len(lines), "rules": len(rules), "issues": issues}


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    path = args[0] if args else find_default()
    if not path or not os.path.exists(path):
        print("No AGENTS.md or CLAUDE.md found%s." % ((" at " + path) if path else ""), file=sys.stderr)
        return 2
    report = lint(path)
    if as_json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print("%s: %d lines, %d rules" % (report["path"], report["lines"], report["rules"]))
        if not report["issues"]:
            print("No issues found.")
        for issue in report["issues"]:
            where = "line %d" % issue["line"] if issue["line"] else "file"
            print("  [%s] %s: %s" % (issue["kind"], where, issue["message"]))
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
