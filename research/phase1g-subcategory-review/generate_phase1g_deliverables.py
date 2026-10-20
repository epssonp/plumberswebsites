"""Write Phase 1G CSV deliverables from subcategory_data.py."""
from __future__ import annotations

import csv
from pathlib import Path

from subcategory_data import KEYWORD_ALLOCATIONS, PARENT_CATEGORIES, SUBCATEGORIES

ROOT = Path(__file__).resolve().parent

MASTER_FIELDS = [
    "subcategory_id",
    "parent_category_id",
    "parent_category_title",
    "subcategory_title",
    "subcategory_description",
    "included_topics",
    "scope_boundaries",
    "primary_keyword",
    "secondary_keywords",
    "search_intent",
    "evidence_status",
    "evidence_source",
    "evidence_date",
    "volume_band",
    "numeric_volume",
    "serp_validation_status",
    "overlap_risk",
    "overlap_with_subcategory_ids",
    "commercial_destination",
    "planned_article_count",
    "priority",
    "validation_needed",
    "status",
    "notes",
]

KW_FIELDS = [
    "keyword",
    "parent_category_id",
    "subcategory_id",
    "subcategory_title",
    "recommended_hierarchy_level",
    "evidence_status",
    "evidence_source",
    "evidence_date",
    "volume_band",
    "numeric_volume",
    "allocation_rationale",
    "overlap_risk",
    "validation_needed",
]


def enrich_row(sc: dict) -> dict:
    pid = sc["parent_category_id"]
    row = dict(sc)
    row["parent_category_title"] = PARENT_CATEGORIES[pid]["title"]
    return row


def write_master_csv() -> None:
    path = ROOT / "subcategory-master.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MASTER_FIELDS)
        w.writeheader()
        for sc in SUBCATEGORIES:
            w.writerow({k: enrich_row(sc)[k] for k in MASTER_FIELDS})


def write_keyword_csv() -> None:
    path = ROOT / "subcategory-keyword-allocation.csv"
    id_to_title = {s["subcategory_id"]: s["subcategory_title"] for s in SUBCATEGORIES}
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=KW_FIELDS)
        w.writeheader()
        for row in KEYWORD_ALLOCATIONS:
            out = dict(row)
            out["subcategory_title"] = id_to_title.get(row["subcategory_id"], "")
            w.writerow({k: out.get(k, "") for k in KW_FIELDS})


def main() -> None:
    write_master_csv()
    write_keyword_csv()
    print(f"Wrote {len(SUBCATEGORIES)} subcategories and {len(KEYWORD_ALLOCATIONS)} keyword rows")


if __name__ == "__main__":
    main()
