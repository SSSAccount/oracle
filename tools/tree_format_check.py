#!/usr/bin/env python3
"""Format checker for expected-structure tree files (spec v0.1).

Checks the mechanical rules of the tree notation spec v0.1 (rules A1-A6):
  A1 block headers, A2 root lines, A3 2-space indent, A4 leaf content,
  A5 element refs resolve, A6 same-refs point backward,
  plus: roles valid for parent type, reachability from element 1,
  known types only, at most one block per element number.

Usage: python3 tree_format_check.py FILE [FILE ...]
Exit 0 = all PASS; exit 1 = any FAIL.
"""
import re
import sys

STRUCTURAL = {
    "eq": {"lhs", "rhs"},
    "frac": {"num", "den"},
    "sup": {"base", "exp"},
    "sub": {"base", "sub"},
    "subsup": {"base", "sub", "exp"},
    "sum": {"lo", "hi", "body"},
    "int": {"lo", "hi", "body"},
    "lim": {"lo", "body"},
    "sqrt": {"radicand", "index"},
    "mat": set(),  # positional only
}
CONTAINER = {"group", "flat"}
LEAF = {"ident", "num", "op", "text"}
ALL_TYPES = set(STRUCTURAL) | CONTAINER | LEAF

HEADER = re.compile(r"^element (\d+)\s*[—–-]+\s*(.+)$")
ROOT = re.compile(r"^(\d+)\s+([a-z]+)$")
ROLE = re.compile(r"^(\s+)([a-z]+):\s*(.+)$")
SIB = re.compile(r"^(\s+)-\s+(.+)$")


class Checker:
    def __init__(self, path):
        self.path = path
        self.errors = []
        self.blocks = {}          # num -> (root_type, line_no)
        self.refs = []            # (num, line_no, kind)
        self.children = {}        # num -> set of referenced child nums
        self.in_tree = False      # prose mode until first element header
        self.last_blank = True    # was the previous line blank/gap

    def err(self, line_no, msg):
        self.errors.append(f"  line {line_no:4d}: {msg}")

    def parse_value(self, val, line_no, indent, stack, in_structural):
        """A child value: element N | same: element N | type [content]."""
        val = val.strip()
        if val == "...":
            return
        m = re.match(r"^same:\s*element\s+(\d+)$", val)
        if m:
            self.refs.append((int(m.group(1)), line_no, "same"))
            return
        m = re.match(r"^element\s+(\d+)$", val)
        if m:
            self.refs.append((int(m.group(1)), line_no, "ref"))
            return
        parts = val.split(None, 1)
        tipe = parts[0]
        content = parts[1].strip() if len(parts) > 1 else None
        if tipe not in ALL_TYPES:
            self.err(line_no, f"unknown type '{tipe}'")
            return
        if tipe in LEAF and not content:
            self.err(line_no, f"leaf '{tipe}' has no content (A4)")
        if tipe in STRUCTURAL or tipe in CONTAINER:
            # structural/container child written inline: it owns the
            # lines indented under it
            stack.append((indent, tipe, line_no))

    def check(self):
        with open(self.path, encoding="utf-8") as f:
            lines = f.readlines()

        stack = []            # (indent, type, line_no) of open inline nodes
        current = None        # element number of current block
        current_type = None
        header_pending = None # header seen, waiting for root line

        for i, raw in enumerate(lines, 1):
            line = raw.rstrip("\n")
            if not line.strip():
                self.last_blank = True
                continue
            # ";" comment lines are ignored anywhere
            if line.lstrip().startswith(";"):
                continue
            if "\t" in line:
                self.err(i, "tab character (A3: 2-space indents only)")

            if HEADER.match(line):
                self.in_tree = True
            elif not self.in_tree:
                # prose before the first element header
                self.last_blank = False
                continue

            if HEADER.match(line):
                n = int(HEADER.match(line).group(1))
                if header_pending is not None:
                    self.err(i, f"block for element {header_pending} has "
                                f"no root line (A2)")
                if n in self.blocks:
                    self.err(i, f"duplicate block for element {n}")
                header_pending = n
                current = n
                current_type = None
                stack = []
                self.blocks[n] = (None, i)
                continue

            if ROOT.match(line) and not line.startswith((" ", "-")):
                m = ROOT.match(line)
                n, tipe = int(m.group(1)), m.group(2)
                if header_pending is None:
                    self.err(i, f"root line outside any block header")
                elif n != header_pending:
                    self.err(i, f"root number {n} != header number "
                                f"{header_pending} (A2)")
                if tipe not in ALL_TYPES:
                    self.err(i, f"unknown type '{tipe}'")
                if n in self.blocks and self.blocks[n][0] is not None:
                    self.err(i, f"duplicate root for element {n}")
                self.blocks[n] = (tipe, self.blocks[n][1] if n in
                                  self.blocks else i)
                # element 1's type is content, not format; any type
                # reaching here already passed the ALL_TYPES check above
                current_type = tipe
                header_pending = None
                stack = [(0, tipe, i)]
                self.children.setdefault(n, set())
                continue

            if line.strip() == "...":
                continue

            m = ROLE.match(line)
            if m:
                indent_s, role, val = m.groups()
                indent = len(indent_s)
                # find parent: nearest open node with smaller indent
                while stack and stack[-1][0] >= indent:
                    stack.pop()
                if not stack:
                    self.err(i, f"role line with no open parent")
                    continue
                p_type = stack[-1][1]
                if p_type in CONTAINER:
                    self.err(i, f"role '{role}:' inside {p_type} "
                                f"(containers take '- ' siblings)")
                elif p_type in STRUCTURAL and role not in STRUCTURAL[p_type]:
                    self.err(i, f"role '{role}' not valid for {p_type} "
                                f"(allowed: "
                                f"{', '.join(sorted(STRUCTURAL[p_type]))})")
                self.parse_value(val, i, indent, stack, True)
                continue

            m = SIB.match(line)
            if m:
                indent_s, val = m.groups()
                indent = len(indent_s)
                while stack and stack[-1][0] >= indent:
                    stack.pop()
                if not stack:
                    self.err(i, f"sibling line with no open parent")
                    continue
                p_type = stack[-1][1]
                if p_type in STRUCTURAL and p_type != "mat":
                    self.err(i, f"'- ' sibling inside {p_type} "
                                f"(structural nodes take roles; only mat "
                                f"takes positional rows/cells)")
                self.parse_value(val, i, indent, stack, False)
                continue

            self.err(i, f"unparseable line: {line.strip()[:50]}")

        if header_pending is not None:
            self.err(len(lines), f"block for element {header_pending} "
                                 f"has no root line (A2)")

        # A5: refs resolve
        for n, ln, kind in self.refs:
            if n not in self.blocks:
                self.err(ln, f"reference to element {n} but no such "
                             f"block (A5)")
        # A6: same refs point backward
        for n, ln, kind in self.refs:
            if kind == "same":
                # find the block we are inside of
                owner = None
                for num, (_t, start) in sorted(self.blocks.items(),
                                               key=lambda kv: kv[1][1]):
                    if start <= ln:
                        owner = num
                if owner is not None and n >= owner:
                    self.err(ln, f"same: element {n} must point to an "
                                 f"EARLIER element (used inside element "
                                 f"{owner}) (A6)")
        # reachability from element 1
        if 1 not in self.blocks:
            self.errors.append("  no element 1 (element 1 = whole "
                               "expression)")
        else:
            # build edges: refs found inside block N link N -> ref
            reach = {1}
            frontier = [1]
            # need ref->owner map
            owner_of = {}
            for n, ln, kind in self.refs:
                owner = None
                for num, (_t, start) in sorted(self.blocks.items(),
                                               key=lambda kv: kv[1][1]):
                    if start <= ln:
                        owner = num
                if owner is not None:
                    owner_of.setdefault(owner, set()).add(n)
            while frontier:
                cur = frontier.pop()
                for child in owner_of.get(cur, ()):  # noqa: B023
                    if child not in reach and child in self.blocks:
                        reach.add(child)
                        frontier.append(child)
            for num in sorted(self.blocks):
                if num not in reach:
                    self.errors.append(f"  element {num} is unreachable "
                                       f"from element 1 (dead element)")
        return not self.errors


def main():
    ok_all = True
    for path in sys.argv[1:]:
        c = Checker(path)
        ok = c.check()
        status = "PASS" if ok else "FAIL"
        print(f"{path}: {status} "
              f"({len(c.blocks)} elements, {len(c.refs)} refs)")
        if not ok:
            ok_all = False
            for e in c.errors:
                print(e)
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
