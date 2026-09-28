#!/usr/bin/env python3
"""Compile every vendored Zed query with a local grammar checkout."""

from pathlib import Path
import argparse
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("grammar", type=Path)
args = parser.parse_args()
grammar = args.grammar.resolve()
root = Path(__file__).resolve().parent.parent
for query in sorted((root / "languages/vibescript").glob("*.scm")):
    result = subprocess.run(
        [str(grammar / "node_modules/.bin/tree-sitter"), "query", str(query),
         str(grammar / "test/examples/declarations.vibe")],
        cwd=grammar, capture_output=True, text=True,
    )
    if result.returncode:
        raise SystemExit(f"{query.name}: {result.stderr}")
    print(f"{query.name}: OK")
