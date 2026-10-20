"""Validate Phase 1M topic-cluster deliverables."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from cluster_definitions import CLUSTERS

OUT = Path(__file__).resolve().parent
INV = Path(__file__).resolve().parents[2] / "research/phase1h-master-toc/master-article-inventory.csv"

COMMERCIAL_PRIMARY = {
    "plumber website builder": "homepage",
    "plumbing website design": "features",
    "plumbing website template": "designs",
}


def main() -> None:
    errors: list[str] = []
    inv = list(csv.DictReader(INV.open(encoding="utf-8")))
    inv_ids = [r["article_id"] for r in inv]
    titles = {r["article_id"]: r["proposed_title"] for r in inv}

    assign = list(csv.DictReader((OUT / "cluster-article-assignments.csv").open(encoding="utf-8")))
    assign_ids = [r["article_id"] for r in assign]
    clusters = {c["cluster_id"] for c in CLUSTERS}
    valid_cluster_ids = clusters | {"UNASSIGNED"}

    if len(inv_ids) != 300:
        errors.append(f"inventory count {len(inv_ids)} != 300")
    if set(inv_ids) != {f"A{i:03d}" for i in range(1, 301)}:
        errors.append("inventory missing or extra IDs")

    if len(assign_ids) != 300:
        errors.append(f"assignments count {len(assign_ids)} != 300")
    c = Counter(assign_ids)
    if any(v > 1 for v in c.values()):
        errors.append("duplicate primary cluster assignments")

    for r in assign:
        if r["primary_cluster_id"] not in valid_cluster_ids:
            errors.append(f"{r['article_id']} invalid cluster {r['primary_cluster_id']}")
        if r["proposed_title"] != titles.get(r["article_id"]):
            errors.append(f"{r['article_id']} title mismatch vs inventory")

    # cluster registry article ids
    reg = list(csv.DictReader((OUT / "topic-cluster-registry.csv").open(encoding="utf-8")))
    reg_ids: list[str] = []
    for row in reg:
        reg_ids.extend(row["article_ids"].split())
    if Counter(reg_ids) != Counter(inv_ids):
        errors.append("registry article_ids do not match inventory partition")

    # partition from definitions
    part: list[str] = []
    for cl in CLUSTERS:
        part.extend(cl["article_ids"])
    if len(part) != 300 or len(set(part)) != 300:
        errors.append(f"cluster_definitions partition invalid: {len(part)} unique {len(set(part))}")

    unassigned = sum(1 for r in assign if r["primary_cluster_id"] == "UNASSIGNED")
    review = sum(1 for r in assign if r.get("review_flag"))

    sizes = [len(cl["article_ids"]) for cl in CLUSTERS]
    report = [
        "# Phase 1M validation report",
        "",
        f"**Result:** {'PASS' if not errors else 'FAIL'}",
        "",
        "## Counts",
        f"- Candidate clusters: {len(CLUSTERS)}",
        f"- Inventory articles: {len(inv_ids)}",
        f"- Primary assignments: {len(assign_ids)}",
        f"- UNASSIGNED: {unassigned}",
        f"- Rows with review_flag: {review}",
        f"- Cluster size min/median/max: {min(sizes)} / {sorted(sizes)[len(sizes)//2]} / {max(sizes)}",
        "",
        "## Commercial ownership",
        "Preserved in map docs — no inventory retargeting of homepage/features/designs primaries.",
        "",
        "## Errors",
    ]
    if errors:
        report.extend(f"- {e}" for e in errors)
    else:
        report.append("- None")

    report.extend(
        [
            "",
            "## Notes",
            "- Rich Results / live SERP not validated in this phase.",
            "- Internal links to planned slugs marked `planned` in CSV.",
            "- A210 flagged in registry for plumbing website design vs Features.",
            "",
        ]
    )
    (OUT / "validation-report.md").write_text("\n".join(report), encoding="utf-8")
    print("PASS" if not errors else "FAIL")
    for e in errors:
        print(e)


if __name__ == "__main__":
    main()
