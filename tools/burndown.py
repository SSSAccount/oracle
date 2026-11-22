#!/usr/bin/env python3
"""Oracle burndown generator — reads a board export CSV, writes burndown.png.

Board export format (GitHub Projects "Export" or Trello CSV — headers matched
case-insensitively): a title column (name/title/summary), a points column
(points/story points/estimate), and a status column (status/column/list).
Rows without a numeric points value are ignored for the chart.

Usage:
    python3 tools/burndown.py <export.csv> <sprint-label> [sprint-days]

sprint-days defaults to 7 (Mon-Sun). Short sprints (DEC-009 compressed
calendar: Sprint 0 and 1 run 3 days) pass their actual length so the ideal
line is honest.
Writes burndown.png next to the CSV. Chart is committed to the sprint folder.
"""
import csv
import sys
from pathlib import Path

import matplotlib.font_manager as fm

for f in (
    "/usr/share/fonts/truetype/chinese/NotoSansSC-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
):
    try:
        fm.fontManager.addfont(f)
    except Exception:
        pass

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Noto Sans SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print(__doc__)
        return 1
    csv_path, label = Path(sys.argv[1]), sys.argv[2]
    # Map export headers to (name, points, status) case-insensitively
    TITLE = {"name", "title", "summary", "card"}
    POINTS = {"points", "story points", "story_points", "estimate", "est"}
    STATUS = {"status", "column", "list", "stage"}

    def pick(headers, wanted):
        for h in headers:
            if h.strip().lower() in wanted:
                return h
        return None

    with csv_path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        h_title = pick(reader.fieldnames or [], TITLE)
        h_pts = pick(reader.fieldnames or [], POINTS)
        h_status = pick(reader.fieldnames or [], STATUS)
        if not (h_title and h_pts and h_status):
            print(f"Need title/points/status columns; got headers: {reader.fieldnames}")
            return 1
        cards = []
        for row in reader:
            name = (row.get(h_title) or "").strip()
            pts_raw = (row.get(h_pts) or "").strip()
            status = (row.get(h_status) or "").strip().lower()
            if not name or not pts_raw:
                continue
            try:
                pts = int(float(pts_raw))
            except ValueError:
                continue
            cards.append((name, pts, status))

    total = sum(p for _, p, _ in cards)
    remaining = sum(p for _, p, s in cards if s != "done")
    done = total - remaining

    # Ideal vs actual (actual = remaining today; extend as the sprint runs)
    days = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
    ax.plot([0, days], [total, 0], "--", color="#8899aa", label="Ideal")
    ax.plot([0], [total], "o", color="#162235", label="Committed")
    ax.plot([days], [remaining], "o", color="#1B6B7A", label="Remaining")
    ax.set_xlabel("Day of sprint (0 = planning, 7 = review)")
    ax.set_ylabel("Story points remaining")
    ax.set_title(f"{label} — burndown (committed {total} pts, remaining {remaining})")
    ax.set_xticks(range(days + 1))
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0))
    ax.spines[["top", "right"]].set_visible(False)

    out = csv_path.with_name("burndown.png")
    fig.savefig(out, dpi=150)
    print(f"Committed {total} pts; done {done}; remaining {remaining}. Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
