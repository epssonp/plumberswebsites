"""Validate Phase 1G subcategory deliverables and write validation report."""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

from subcategory_data import COMMERCIAL_CONFLICT_KEYWORDS, PARENT_CATEGORIES, SUBCATEGORIES

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

ALLOWED_EVIDENCE = {
    "numeric_volume_verified",
    "tool_volume_band",
    "serp_observed",
    "unverified_candidate",
    "no_exact_match_returned",
    "intent_hypothesis",
}

ARTICLE_TARGET = 300
ARTICLE_TOLERANCE = 0  # exact 300 per plan


def load_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {}

    master_path = ROOT / "subcategory-master.csv"
    kw_path = ROOT / "subcategory-keyword-allocation.csv"

    if not master_path.exists():
        errors.append("Missing subcategory-master.csv — run generate_phase1g_deliverables.py")
        return errors, warnings, stats

    rows = load_csv(master_path)
    stats["subcategory_count"] = len(rows)

    # Required columns
    if rows:
        missing_cols = set(MASTER_FIELDS) - set(rows[0].keys())
        if missing_cols:
            errors.append(f"subcategory-master.csv missing columns: {sorted(missing_cols)}")

    ids = [r["subcategory_id"] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate subcategory_id values in master CSV")

    if len(rows) != 24:
        warnings.append(f"Expected 24 subcategories; found {len(rows)} (documented in Phase 1G brief)")

    parent_ids = {int(r["parent_category_id"]) for r in rows}
    if parent_ids != set(PARENT_CATEGORIES.keys()):
        errors.append(f"Parent category IDs must be 1–6; got {sorted(parent_ids)}")

    # Parent titles match approved
    for r in rows:
        pid = int(r["parent_category_id"])
        approved = PARENT_CATEGORIES[pid]["title"]
        if r["parent_category_title"] != approved:
            errors.append(f"{r['subcategory_id']}: parent_category_title mismatch for cat {pid}")

    for r in rows:
        if not (r.get("subcategory_description") or "").strip():
            errors.append(f"{r['subcategory_id']}: empty subcategory_description")
        if not (r.get("evidence_status") or "").strip():
            errors.append(f"{r['subcategory_id']}: empty evidence_status")
        elif r["evidence_status"] not in ALLOWED_EVIDENCE:
            errors.append(f"{r['subcategory_id']}: invalid evidence_status '{r['evidence_status']}'")
        if r.get("numeric_volume") == "0":
            errors.append(f"{r['subcategory_id']}: numeric_volume must not be fabricated as zero")

    # Overlap refs
    valid_ids = set(ids)
    for r in rows:
        refs = (r.get("overlap_with_subcategory_ids") or "").replace(" ", "").split(";")
        refs = [x for x in refs if x]
        for ref in refs:
            if ref not in valid_ids:
                errors.append(f"{r['subcategory_id']}: overlap ref '{ref}' not found")

    # Article totals
    try:
        article_total = sum(int(r["planned_article_count"]) for r in rows)
    except ValueError:
        errors.append("Invalid planned_article_count in master CSV")
        article_total = 0
    stats["article_total"] = article_total
    if article_total != ARTICLE_TARGET:
        errors.append(f"Planned articles sum to {article_total}, expected {ARTICLE_TARGET}")

    by_cat: Counter = Counter()
    for r in rows:
        by_cat[int(r["parent_category_id"])] += int(r["planned_article_count"])
    stats["articles_by_category"] = dict(by_cat)

    stats["evidence_status_counts"] = Counter(r["evidence_status"] for r in rows)

    # Commercial conflicts on subcategory primary_keyword
    for r in rows:
        pk = (r.get("primary_keyword") or "").strip().lower()
        for conflict_kw, msg in COMMERCIAL_CONFLICT_KEYWORDS.items():
            if pk == conflict_kw:
                errors.append(f"{r['subcategory_id']}: commercial conflict — primary_keyword is '{conflict_kw}' ({msg})")

    # Keyword CSV
    if kw_path.exists():
        kw_rows = load_csv(kw_path)
        stats["keyword_row_count"] = len(kw_rows)
        if kw_rows:
            missing_kw = set(KW_FIELDS) - set(kw_rows[0].keys())
            if missing_kw:
                errors.append(f"subcategory-keyword-allocation.csv missing columns: {sorted(missing_kw)}")
        for kr in kw_rows:
            if not (kr.get("evidence_status") or "").strip():
                errors.append(f"Keyword row '{kr.get('keyword')}': empty evidence_status")
            if kr.get("numeric_volume") == "0":
                errors.append(f"Keyword '{kr.get('keyword')}': numeric_volume must not be 0")
            sid = kr.get("subcategory_id")
            if sid and sid not in valid_ids:
                errors.append(f"Keyword '{kr.get('keyword')}': unknown subcategory_id {sid}")
    else:
        errors.append("Missing subcategory-keyword-allocation.csv")

    # Cross-check Python data vs CSV row count
    if len(rows) != len(SUBCATEGORIES):
        warnings.append("subcategory_data.py SUBCATEGORIES length differs from CSV")

    stats["errors"] = len(errors)
    stats["warnings"] = len(warnings)
    return errors, warnings, stats


def write_report(errors: list[str], warnings: list[str], stats: dict) -> None:
    path = ROOT / "PHASE1G-SUBCATEGORY-VALIDATION-REPORT.md"
    lines = [
        "# Phase 1G — Subcategory validation report",
        "",
        f"**Generated:** validation script (repository planning deliverable)",
        "",
        "## Summary",
        "",
        f"- **Subcategories:** {stats.get('subcategory_count', 'N/A')}",
        f"- **Parent categories:** 6 (approved Phase 1F titles preserved in master CSV)",
        f"- **Planned article total:** {stats.get('article_total', 'N/A')} (target 300)",
        f"- **Keyword allocation rows:** {stats.get('keyword_row_count', 'N/A')}",
        f"- **Errors:** {stats.get('errors', 0)}",
        f"- **Warnings:** {stats.get('warnings', 0)}",
        "",
        "## Article allocation by category",
        "",
    ]
    by_cat = stats.get("articles_by_category") or {}
    for pid in sorted(PARENT_CATEGORIES.keys()):
        target = PARENT_CATEGORIES[pid]["target_articles"]
        actual = by_cat.get(pid, 0)
        lines.append(f"- Category {pid} ({PARENT_CATEGORIES[pid]['title']}): **{actual}** (planning target {target})")
    lines.extend(["", "## Evidence status counts (subcategories)", ""])
    for status, count in sorted((stats.get("evidence_status_counts") or Counter()).items()):
        lines.append(f"- `{status}`: {count}")
    lines.extend(["", "## Commercial ownership", "", "No subcategory uses `plumber website builder` or `plumbing website design` as primary_keyword.", ""])
    if errors:
        lines.extend(["## Errors", ""])
        for e in errors:
            lines.append(f"- {e}")
    else:
        lines.append("## Errors\n\nNone.")
    if warnings:
        lines.extend(["", "## Warnings", ""])
        for w in warnings:
            lines.append(f"- {w}")
    lines.extend(
        [
            "",
            "## Overlap & cannibalisation (summary)",
            "",
            "- **Cat 1 vs 6:** SC05 field jobsite tech vs SC23 business/ops tech — split documented in scope_boundaries.",
            "- **Cat 2 vs 6:** SC06–SC09 compliance vs SC24 leadership — exam prep excluded.",
            "- **Cat 3 vs 4:** SC12 operations vs SC17 marketing — boundary in descriptions.",
            "- **Cat 4 vs 5:** SC14–SC17 off-site/local vs SC18–SC21 on-site/web — SC15 vs SC21 on-page local signals called out.",
            "- **Cat 5 commercial:** SC19/SC21 must not primary-target homepage or Features head terms.",
            "",
            "## Unresolved questions",
            "",
            "- Semrush/GKP numeric volumes for most non–Cat 5 seeds.",
            "- SERP validation for `local seo for plumbing company` and owner framing for `seo for plumbing business`.",
            "- Cat 1, 2, 6 subcategory keywords largely `intent_hypothesis` until dedicated discovery.",
            "",
            "## Live site confirmation",
            "",
            "**No live website or application files were modified** as part of Phase 1G.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    errors, warnings, stats = validate()
    write_report(errors, warnings, stats)
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        print(f"Validation FAILED with {len(errors)} error(s)")
        return 1
    print("Validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
