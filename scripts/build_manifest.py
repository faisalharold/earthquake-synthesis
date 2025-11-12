#!/usr/bin/env python3
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "data" / "raw"
manifest = Path(__file__).resolve().parents[1] / "data" / "manifest.csv"

with open(manifest, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["path", "size_kb"])
    for p in sorted(root.rglob("*")):
        if p.is_file():
            w.writerow([str(p.relative_to(root)), round(p.stat().st_size/1024, 2)])
print(f"Manifest written to {manifest}")
