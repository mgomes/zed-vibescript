#!/usr/bin/env python3
"""Compile vendored Zed queries and check indentation captures."""

from pathlib import Path
import argparse
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("grammar", type=Path)
args = parser.parse_args()
grammar = args.grammar.resolve()
root = Path(__file__).resolve().parent.parent


def run_query(query, fixture):
    result = subprocess.run(
        [str(grammar / "node_modules/.bin/tree-sitter"), "query", str(query),
         str(fixture)],
        cwd=grammar, capture_output=True, text=True,
    )
    if result.returncode:
        raise SystemExit(f"{query.name}: {result.stderr}")
    return result.stdout


for query in sorted((root / "languages/vibescript").glob("*.scm")):
    run_query(query, grammar / "test/examples/declarations.vibe")
    print(f"{query.name}: OK")

fixture = root / "tests/indents.vibe"
output = run_query(root / "languages/vibescript/indents.scm", fixture)
actual = [(int(row), int(column)) for row, column in re.findall(
    r"capture: \d+ - outdent, start: \((\d+), (\d+)\)", output,
)]
expected = [(row, line.index(">"))
            for row, line in enumerate(fixture.read_text().splitlines())
            if line.strip() == ">"]
if actual != expected:
    raise SystemExit(f"{fixture.name}: expected outdents {expected}, got {actual}")
print(f"{fixture.name}: OK")
