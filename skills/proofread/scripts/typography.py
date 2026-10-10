#!/usr/bin/env python3
"""Deterministic French typography check for one chapter.

Prints a JSON list of findings: line, extract, correction, rule, and for
rules that apply to the whole chapter, count and lines. Each choice takes
`ignore` to skip its check.
"""
import argparse
import json
import re
import sys

SPACES = {"nnbsp": " ", "nbsp": " ", "space": " "}
ANY_SPACE = "[   ]"


def window(line, start, end):
    """Widen [start, end) to whole words around it."""
    start, end = max(0, start - 8), min(len(line), end + 8)
    while start > 0 and not line[start - 1].isspace():
        start -= 1
    while end < len(line) and not line[end].isspace():
        end += 1
    return start, end


def rows_for_line(n, line, edits):
    """One row per group of edits whose windows overlap, so that every
    extract occurs once on its line and rows never conflict."""
    rows, group = [], []
    for edit in sorted(edits) + [None]:
        if group and (edit is None or window(line, *edit[:2])[0] >= group_end):
            s, e = window(line, group[0][0], max(g[1] for g in group))
            while line.count(line[s:e]) > 1 and (s > 0 or e < len(line)):
                s, e = max(0, s - 3), min(len(line), e + 3)
            fixed = line[s:e]
            for start, end, repl, _ in sorted(group, reverse=True):
                fixed = fixed[:start - s] + repl + fixed[end - s:]
            rules = list(dict.fromkeys(g[3] for g in group))
            rows.append({"line": n, "extract": line[s:e], "correction": fixed, "rule": " ; ".join(rules)})
            group = []
        if edit is not None:
            group.append(edit)
            group_end = max(window(line, *g[:2])[1] for g in group)
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--apostrophe", default="’", choices=["’", "'", "ignore"])
    p.add_argument("--ellipsis", default="…", choices=["…", "...", "ignore"])
    p.add_argument("--space-before-high", default="nnbsp", choices=[*SPACES, "ignore"])
    p.add_argument("--quotes", default="«»", choices=["«»", "“”", "ignore"])
    p.add_argument("--quote-space", default="nnbsp", choices=[*SPACES, "ignore"])
    p.add_argument("--dialogue-dash", default="—", choices=["—", "–", "ignore"])
    p.add_argument("--scene-break", default="* * *")
    a = p.parse_args()

    lines = open(a.file, encoding="utf-8").read().split("\n")
    rows, aggregate = [], {}

    def count(rule, fixed_from, fixed_to, n, k):
        entry = aggregate.setdefault(rule, {"extract": fixed_from, "correction": fixed_to, "count": 0, "lines": []})
        entry["count"] += k
        entry["lines"].append(n)

    for n, line in enumerate(lines, 1):
        if not line.strip() or line.strip() == a.scene_break:
            continue
        edits = []

        def finding(_rows, _n, _line, start, end, fixed, rule):
            if not any(start < e2 and s2 < end for s2, e2, _, _ in edits):
                edits.append((start, end, fixed, rule))
        if line != line.lstrip():
            finding(rows, n, line, 0, len(line) - len(line.lstrip()) + 1, line.lstrip()[:1], "espace en début de ligne")
        if line != line.rstrip():
            k = len(line.rstrip())
            finding(rows, n, line, k - 1, len(line), line[k - 1], "espace en fin de ligne")
        body = line.strip()
        offset = line.index(body)

        if a.dialogue_dash != "ignore" and body[:1] in "—–-":
            dash = body[0]
            m = re.match(f"[—–-]({ANY_SPACE}*)", body)
            if dash != a.dialogue_dash or m.group(1) != " ":
                finding(rows, n, line, offset, offset + m.end(), a.dialogue_dash + " ", "tiret de dialogue")

        for m in re.finditer(f"(?<=\\S){ANY_SPACE}{{2,}}(?=\\S)", line):
            finding(rows, n, line, m.start(), m.end(), " ", "espace doublée")
        for m in re.finditer(f"(?<=\\w){ANY_SPACE}+([,.])(?!\\.)", line):
            finding(rows, n, line, m.start(), m.end(), m.group(1), "espace avant « , » ou « . »")

        if a.apostrophe != "ignore":
            wrong = "'" if a.apostrophe == "’" else "’"
            if line.count(wrong):
                count("apostrophe", wrong, a.apostrophe, n, line.count(wrong))
        if a.ellipsis != "ignore":
            wrong = "..." if a.ellipsis == "…" else "…"
            if line.count(wrong):
                count("points de suspension", wrong, a.ellipsis, n, line.count(wrong))

        if a.space_before_high != "ignore":
            want = SPACES[a.space_before_high]
            for m in re.finditer(f"({ANY_SPACE}?)([;:!?])", line):
                before = line[m.start() - 1] if m.start() > 0 else ""
                if m.group(1) == "" and (before in ";:!?…»" + want or not before):
                    continue  # ?! sequences, …? and line starts
                if m.group(2) == ":" and before.isdigit() and line[m.end():m.end() + 1].isdigit():
                    continue  # times such as 10:30
                if m.group(1) != want:
                    finding(rows, n, line, m.start(), m.end(), want + m.group(2), f"espace avant « {m.group(2)} »")

        if a.quotes != "ignore":
            wrong = "“”" if a.quotes == "«»" else "«»"
            for ch in wrong:
                for m in re.finditer(re.escape(ch), line):
                    finding(rows, n, line, m.start(), m.end(), a.quotes[wrong.index(ch)], "guillemets")
            if a.quotes == "«»" and a.quote_space != "ignore":
                want = SPACES[a.quote_space]
                for m in re.finditer(f"«({ANY_SPACE}*)", line):
                    if m.group(1) != want:
                        finding(rows, n, line, m.start(), m.end(), "«" + want, "espace après « « »")
                for m in re.finditer(f"({ANY_SPACE}*)»", line):
                    if m.group(1) != want:
                        finding(rows, n, line, m.start(), m.end(), want + "»", "espace avant « » »")

        rows.extend(rows_for_line(n, line, edits))

    for rule, e in aggregate.items():
        rows.append({"line": "tout le chapitre", "rule": rule, **e})
    json.dump(rows, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
