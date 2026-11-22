#!/usr/bin/env python3
"""Spike 3 (PB-07): smallest tikz-cd parser — fixture D-01 source to
nodes/edges/paths JSON.

Scope (the "smallest" spike, per the card):
    IN  fixtures/diagrams/pullback-intersection.tex  (\\begin{tikzcd}...\\end{tikzcd})
    OUT a nodes/edges/paths JSON exactly matching fixtures/diagrams/
        pullback-intersection.json (the PB-06 hand-encoded oracle), plus a
        paths list (the spoken-navigation reading order over nodes+edges).

Acceptance (from Sprint 1 planning):
    parse D-01's tikz-cd and match the hand-encoded JSON's nodes and edges
    exactly — labels, rows, cols, from/to, direction, style. Anything beyond
    D-01's constructs is out of scope; hitting an unsupported construct ends
    the spike with a recorded NO-GO or a scope note, never a silent guess
    (working agreement §8).

Grammar handled (exactly D-01's constructs, verified against the fixture):
    rows   := cells separated by \\\\, rows end the row; & separates cells
    cell   := [label] [arrow-spec]*        label may be empty
    arrow  := \\arrow[<options>]{<dir>}      options: hook; dir: r, d (l, u free)
    grid   := cell positions map to (row, col); node ids assigned row-major
Run:
    python3 spikes/spike3-tikzcd/parse_tikzcd.py <fixture.tex> [out.json]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- tokenizer

ARROW_RE = re.compile(r"\\arrow\[(?P<opts>[^\]]*)\]\{(?P<dir>[a-z]+)\}")
LABEL_RE = re.compile(r'"(?P<label>[^"]*)"')
# A cell's label is whatever remains after removing all \arrow specs.
DIRECTIONS = {"r": (0, 1), "l": (0, -1), "d": (1, 0), "u": (-1, 0)}


def split_rows(body: str) -> list[list[str]]:
    """Split the tikzcd body into rows of raw cell strings."""
    rows = []
    for raw_row in body.split("\\\\"):
        cells = [c.strip() for c in raw_row.split("&")]
        # a trailing \\ often leaves a final empty cell after the last &
        # only when the source genuinely ends with & (not in D-01)
        rows.append(cells)
    return rows


def parse_cell(cell: str) -> tuple[str, list[dict]]:
    """Return (label, arrows) for one raw cell string."""
    arrows = []
    def take(m: re.Match) -> str:
        opts = m.group("opts")
        lm = LABEL_RE.search(opts)
        # label text in quotes ("p_2"); a trailing ' after the quotes is a
        # visual placement modifier (swap side) — not recorded (visual-only)
        arrows.append({
            "direction": m.group("dir"),
            "style": "hook" if "hook" in opts.split(",") else "plain",
            "label": lm.group("label") if lm else None,
        })
        return " "
    label = ARROW_RE.sub(take, cell).strip()
    return label, arrows


# ------------------------------------------------------------------- parser

def parse_tikzcd(source: str) -> dict:
    m = re.search(r"\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}", source, re.S)
    if not m:
        raise ValueError("no tikzcd environment found")
    body = m.group(1)

    nodes, edges = [], []
    for row_idx, row in enumerate(split_rows(body)):
        for col_idx, cell in enumerate(row):
            label, arrows = parse_cell(cell)
            nodes.append({
                "id": f"n{len(nodes)}",
                "label": label if label else None,
                "row": row_idx,
                "col": col_idx,
            })
            for arrow in arrows:
                edges.append({"from": f"n{len(nodes)-1}", **arrow})

    # resolve each edge's target from the grid: direction letters are
    # relative cell references in tikz-cd (r = one cell right, etc.).
    grid = {(n["row"], n["col"]): n["id"] for n in nodes}
    for i, e in enumerate(edges):
        src = next(n for n in nodes if n["id"] == e["from"])
        dr, dc = DIRECTIONS[e["direction"]]
        target = grid.get((src["row"] + dr, src["col"] + dc))
        if target is None:
            raise ValueError(
                f"arrow {e['direction']} from {e['from']} leaves the grid"
            )
        # field order matches the oracle JSON schema (fixtures/diagrams/)
        edges[i] = {
            "id": f"e{i+1}",
            "from": e["from"],
            "to": target,
            "kind": "arrow",
            "style": e["style"],
            "direction": e["direction"],
            "label": e["label"],
        }

    # reading order for spoken navigation: p1 = nodes row-major (the
    # overview); arrow-following paths = DFS from in-degree-0 nodes with
    # out-edges, branches in source (edge) order, stopping at dead ends.
    paths = [{
        "id": "p1", "kind": "node-reading", "order": "row-major",
        "traversal": [n["id"] for n in nodes],
    }]
    out_edges: dict[str, list[dict]] = {}
    for e in edges:
        out_edges.setdefault(e["from"], []).append(e)
    in_degree = {n["id"]: 0 for n in nodes}
    for e in edges:
        in_degree[e["to"]] += 1
    path_no = 1
    for n in nodes:  # row-major start order
        if in_degree[n["id"]] == 0 and n["id"] in out_edges:
            stack = [(n["id"], [n["id"]], [])]  # node, trail, edge trail
            while stack:
                cur, trail, etrail = stack.pop()
                if cur not in out_edges:
                    path_no += 1
                    paths.append({
                        "id": f"p{path_no}", "kind": "arrow-following",
                        "traversal": trail, "edges": [e["id"] for e in etrail],
                    })
                    continue
                # push branches in reverse so the FIRST source edge is
                # popped first (source-order DFS)
                for e in reversed(out_edges[cur]):
                    stack.append((e["to"], trail + [e["to"]], etrail + [e]))
    return {"nodes": nodes, "edges": edges, "paths": paths}


# ------------------------------------------------------------------- report

def compare_with_oracle(parsed: dict, oracle_path: Path) -> list[str]:
    """Diff parsed output against the PB-06 hand-encoded JSON (exact match
    on nodes, edges and paths)."""
    oracle = json.loads(oracle_path.read_text())
    problems = []
    for key in ("nodes", "edges", "paths"):
        if parsed[key] != oracle[key]:
            problems.append(f"{key}: parsed != oracle")
            for i, (a, b) in enumerate(zip(parsed[key], oracle[key])):
                if a != b:
                    problems.append(f"  first diff at index {i}: {a} vs {b}")
            if len(parsed[key]) != len(oracle[key]):
                problems.append(
                    f"  count: parsed {len(parsed[key])} vs oracle {len(oracle[key])}"
                )
    return problems


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    src_path = Path(sys.argv[1])
    parsed = parse_tikzcd(src_path.read_text())

    out_path = (
        Path(sys.argv[2]) if len(sys.argv) > 2
        else src_path.with_name(src_path.stem + ".parsed.json")
    )
    out_path.write_text(json.dumps(parsed, indent=2) + "\n")
    print(f"parsed {len(parsed['nodes'])} nodes, {len(parsed['edges'])} edges "
          f"-> {out_path}")

    # default oracle sits next to the fixture with the same stem
    oracle = (
        src_path.with_suffix(".json") if src_path.with_suffix(".json").exists()
        else Path(__file__).resolve().parents[2]
        / "fixtures/diagrams/pullback-intersection.json"
    )
    if oracle.exists():
        problems = compare_with_oracle(parsed, oracle)
        if problems:
            print(f"ORACLE COMPARISON ({oracle.name}): FAIL")
            print("\n".join(problems))
            return 2
        print(f"ORACLE COMPARISON ({oracle.name}): PASS — nodes, edges and "
              "paths match exactly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
