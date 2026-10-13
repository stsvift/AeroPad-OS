import json, csv
from pathlib import Path

for f in Path(".").glob("*.json"):
    data = json.loads(f.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict):
        data = data["records"]

    if not data:
        continue

    with open(f.with_suffix(".csv"), "w", newline="", encoding="utf-8-sig") as out:
        w = csv.DictWriter(out, dict.fromkeys(k for row in data for k in row))
        w.writeheader()
        w.writerows(data)
