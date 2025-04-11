import json
import csv

INPUT_JSON = "deck.json"
OUTPUT_TSV = "deck.tsv"

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(OUTPUT_TSV, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")

    for entry in data:
        writer.writerow([
            entry.get("term", ""),
            entry.get("meaning_cn", ""),
            entry.get("meaning_en", ""),
            entry.get("example", ""),
            entry.get("translation", "")
        ])

print(f"✅ Generated: {OUTPUT_TSV}")