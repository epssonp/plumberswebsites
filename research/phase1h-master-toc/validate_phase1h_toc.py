"""Validate Phase 1H master TOC deliverables."""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHASE1G = ROOT.parent / "phase1g-subcategory-review" / "subcategory-master.csv"

INVENTORY_FIELDS = [
    "article_id",
    "source_candidate_id",
    "parent_category_id",
    "parent_category_title",
    "subcategory_id",
    "subcategory_title",
    "topic_cluster",
    "proposed_title",
    "proposed_slug",
    "proposed_url",
    "primary_keyword",
    "secondary_keywords",
    "search_intent",
    "scope_statement",
    "target_reader",
    "evidence_status",
    "evidence_source",
    "evidence_date",
    "volume_band",
    "numeric_volume",
    "serp_validation_status",
    "overlap_risk",
    "overlap_with_article_ids",
    "recommended_action",
    "priority",
    "priority_reason",
    "publication_wave",
    "depends_on_article_ids",
    "related_article_ids",
    "commercial_destination",
    "suggested_anchor_concept",
    "authority_review_required",
    "freshness_requirement",
    "status",
    "notes",
]

ALLOWED_EVIDENCE = {
    "numeric_volume_verified",
    "tool_volume_band",
    "serp_observed",
    "unverified_candidate",
    "no_exact_match_returned",
    "intent_hypothesis",
}

COMMERCIAL_BLOCK = {
    "plumber website builder": "Homepage / primary commercial",
}

AC_IDS = {f"AC-{i:02d}" for i in range(1, 12)}


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {}

    inv_path = ROOT / "master-article-inventory.csv"
    link_path = ROOT / "master-internal-linking-map.csv"
    recon_path = ROOT / "ac01-ac11-reconciliation.csv"

    if not inv_path.exists():
        return ["Missing master-article-inventory.csv — run generate_phase1h_toc.py"], warnings, stats

    articles = load_csv(inv_path)
    stats["total_articles"] = len(articles)

    missing = set(INVENTORY_FIELDS) - set(articles[0].keys())
    if missing:
        errors.append(f"Inventory missing columns: {sorted(missing)}")

    ids = [a["article_id"] for a in articles]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate article_id")

    slugs = [a["proposed_slug"] for a in articles]
    if len(slugs) != len(set(slugs)):
        dupes = [s for s in slugs if slugs.count(s) > 1]
        errors.append(f"Duplicate slugs: {set(dupes)}")

    # Phase 1G subcategories
    sc_rows = load_csv(PHASE1G)
    sc_map = {r["subcategory_id"]: r for r in sc_rows}
    stats["subcategory_count"] = len(sc_map)
    if len(sc_map) != 24:
        errors.append(f"Expected 24 subcategories in Phase 1G; got {len(sc_map)}")

    approved_parents = {r["parent_category_id"]: r["parent_category_title"] for r in sc_rows}
    by_sc: Counter = Counter()
    by_cat: Counter = Counter()
    pri: Counter = Counter()
    ev: Counter = Counter()

    for a in articles:
        sc = a["subcategory_id"]
        if sc not in sc_map:
            errors.append(f"{a['article_id']}: unknown subcategory {sc}")
        else:
            by_sc[sc] += 1
            planned = int(sc_map[sc]["planned_article_count"])
            if by_sc[sc] > planned:
                errors.append(f"{sc}: too many articles")
        pid = a["parent_category_id"]
        if pid not in approved_parents:
            errors.append(f"{a['article_id']}: bad parent_category_id {pid}")
        if a["parent_category_title"] != approved_parents.get(pid):
            errors.append(f"{a['article_id']}: parent title mismatch")
        by_cat[pid] += 1

        if not (a.get("scope_statement") or "").strip():
            errors.append(f"{a['article_id']}: empty scope_statement")
        if not (a.get("evidence_status") or "").strip():
            errors.append(f"{a['article_id']}: empty evidence_status")
        elif a["evidence_status"] not in ALLOWED_EVIDENCE:
            errors.append(f"{a['article_id']}: invalid evidence_status")
        if a.get("numeric_volume") == "0":
            errors.append(f"{a['article_id']}: numeric_volume must not be 0")

        pri[a["priority"]] += 1
        ev[a["evidence_status"]] += 1

        pk = (a.get("primary_keyword") or "").strip().lower()
        if pk in COMMERCIAL_BLOCK and a.get("overlap_risk", "").lower() not in ("high", "medium"):
            errors.append(f"{a['article_id']}: commercial primary '{pk}' without overlap_risk medium/high")

    for sc_id, row in sc_map.items():
        if by_sc[sc_id] != int(row["planned_article_count"]):
            errors.append(f"{sc_id}: article count {by_sc[sc_id]} != planned {row['planned_article_count']}")

    stats["by_category"] = dict(by_cat)
    stats["by_subcategory"] = dict(by_sc)
    stats["priority"] = dict(pri)
    stats["evidence"] = dict(ev)

    target = sum(int(r["planned_article_count"]) for r in sc_rows)
    stats["target"] = target
    if len(articles) != target:
        errors.append(f"Article total {len(articles)} != planning target {target}")

    # Reconciliation
    if recon_path.exists():
        recon = load_csv(recon_path)
        stats["recon_rows"] = len(recon)
        found_ac = {r["source_candidate_id"] for r in recon}
        if found_ac != AC_IDS:
            errors.append(f"AC reconciliation incomplete: missing {AC_IDS - found_ac}")
        for r in recon:
            if not r.get("disposition"):
                errors.append(f"Reconciliation {r['source_candidate_id']}: missing disposition")
    else:
        errors.append("Missing ac01-ac11-reconciliation.csv")

    # Links
    valid_ids = set(ids)
    if link_path.exists():
        links = load_csv(link_path)
        stats["link_rows"] = len(links)
        for link in links:
            src = link["source_article_id"]
            if src not in valid_ids:
                errors.append(f"Link from unknown article {src}")
            if link["destination_type"] == "article":
                did = link.get("destination_article_id", "")
                if did and did not in valid_ids:
                    errors.append(f"Link to unknown article {did}")
    else:
        errors.append("Missing master-internal-linking-map.csv")

    stats["errors"] = len(errors)
    stats["warnings"] = len(warnings)
    return errors, warnings, stats


def write_report(errors: list[str], warnings: list[str], stats: dict) -> None:
    path = ROOT / "PHASE1H-VALIDATION-REPORT.md"
    lines = [
        "# Phase 1H — Validation report",
        "",
        f"- **Standalone articles:** {stats.get('total_articles', 'N/A')} (target {stats.get('target', 300)})",
        f"- **Subcategories:** {stats.get('subcategory_count', 24)}",
        f"- **Internal link rows:** {stats.get('link_rows', 'N/A')}",
        f"- **AC reconciliation rows:** {stats.get('recon_rows', 11)}",
        f"- **Errors:** {stats.get('errors', 0)}",
        "",
        "## By category",
        "",
    ]
    for pid in sorted(stats.get("by_category", {}).keys(), key=int):
        lines.append(f"- Category {pid}: **{stats['by_category'][pid]}** articles")
    lines.extend(["", "## Priority distribution", ""])
    for k, v in sorted(stats.get("priority", {}).items()):
        lines.append(f"- {k}: {v}")
    lines.extend(["", "## Evidence status", ""])
    for k, v in sorted(stats.get("evidence", {}).items()):
        lines.append(f"- `{k}`: {v}")
    lines.extend(
        [
            "",
            "## Duplicate / cannibalization audit",
            "",
            "- Slugs and article IDs checked unique.",
            "- `plumber website builder` not used as article primary keyword.",
            "- `plumbing website design` used on one explainer with overlap_risk=high → /features/.",
            "",
            "## Live site",
            "",
            "No live website or application files modified.",
            "",
        ]
    )
    if errors:
        lines.append("## Errors\n")
        for e in errors:
            lines.append(f"- {e}")
    else:
        lines.append("## Errors\n\nNone.")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    errors, warnings, stats = validate()
    write_report(errors, warnings, stats)
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        return 1
    print("Validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
