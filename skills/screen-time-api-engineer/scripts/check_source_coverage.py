#!/usr/bin/env python3
from pathlib import Path
import sys

base = Path(__file__).resolve().parents[1]
inv = base / "references" / "evidence" / "00-source-url-inventory.md"
source_matrix = base / "references" / "guides" / "20-source-index-and-confidence-matrix.md"

if not inv.exists() or not source_matrix.exists():
    print("Required files missing")
    sys.exit(1)

inv_text = inv.read_text(encoding="utf-8")
matrix_text = source_matrix.read_text(encoding="utf-8")

urls = []
for line in inv_text.splitlines():
    if line.startswith("| https://"):
        url = line.split("|")[1].strip()
        urls.append(url)

missing = [u for u in urls if u not in matrix_text]
if missing:
    print("Missing URLs in source index matrix:")
    for u in missing:
        print(u)
    sys.exit(1)

print(f"Source coverage check passed ({len(urls)} URLs)")
