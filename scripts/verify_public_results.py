#!/usr/bin/env python3
"""Validate the curated public SHADOW-Q result files.

This utility intentionally contains no SHADOW-Q optimisation implementation.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

required = [f"b{i}_summary.json" for i in range(1, 9)]
errors = []

for name in required:
    path = RESULTS / name
    if not path.exists():
        errors.append(f"missing: {name}")
        continue
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {name}: {exc}")
        continue
    expected = name.split("_")[0].upper()
    if data.get("benchmark") != expected:
        errors.append(f"{name}: benchmark field should be {expected}")
    if "status" not in data or "note" not in data:
        errors.append(f"{name}: missing status/note")

if errors:
    print("Public evidence validation FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("Public evidence validation PASS")
print(f"Validated {len(required)} curated benchmark summaries.")
