#!/usr/bin/env python3
import sys, json, yaml, datetime, pathlib

if len(sys.argv) < 2:
    print("Usage: python build_json.py today.yaml")
    sys.exit(1)

src = pathlib.Path(sys.argv[1])
data = yaml.safe_load(src.read_text(encoding="utf-8"))

# ajoute date ISO si absent
data.setdefault("date", datetime.date.today().isoformat())

# 1️⃣ facultatif : conserver un today.json lisible
pathlib.Path("today.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# 2️⃣ nécessaire : produire today.js
pathlib.Path("today.js").write_text(
    "window.CHECKLIST_DATA = " + json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8")

print("✅ today.js et today.json générés.")
