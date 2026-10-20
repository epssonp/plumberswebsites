"""Generate Phase 1H master TOC CSVs and supporting markdown."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from article_topics import TOPICS_BY_SUBCATEGORY

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

LINK_FIELDS = [
    "source_article_id",
    "destination_type",
    "destination_article_id",
    "destination_url",
    "anchor_concept",
    "link_purpose",
    "priority",
    "verification_required",
]

RECON_FIELDS = [
    "source_candidate_id",
    "original_title",
    "disposition",
    "final_article_id",
    "final_title",
    "reason",
    "evidence_status",
    "validation_needed",
]


def load_subcategories() -> dict[str, dict]:
    out = {}
    with PHASE1G.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["subcategory_id"]] = row
    return out


def build_articles(subcats: dict[str, dict]) -> list[dict]:
    articles: list[dict] = []
    n = 0
    for sc_id in sorted(TOPICS_BY_SUBCATEGORY.keys()):
        sc = subcats[sc_id]
        topics = TOPICS_BY_SUBCATEGORY[sc_id]
        if len(topics) != int(sc["planned_article_count"]):
            raise ValueError(f"{sc_id}: topic count {len(topics)} != planned {sc['planned_article_count']}")
        for topic in topics:
            n += 1
            aid = f"A{n:03d}"
            slug = topic["proposed_slug"]
            url = f"https://plumberswebsites.com/academy/{slug}/"
            pri = topic.get("priority", "P3")
            wave = topic.get("publication_wave", "3")
            pri_reason = {
                "P1": "Foundational cluster / Phase 1E wave / validated or strategic Cat 4–5",
                "P2": "Supporting cluster content",
                "P3": "Narrower topic or pending keyword validation",
            }.get(pri, "Supporting content")
            articles.append(
                {
                    "article_id": aid,
                    "source_candidate_id": topic.get("source_candidate_id", ""),
                    "parent_category_id": sc["parent_category_id"],
                    "parent_category_title": sc["parent_category_title"],
                    "subcategory_id": sc_id,
                    "subcategory_title": sc["subcategory_title"],
                    "topic_cluster": sc["subcategory_title"],
                    "proposed_title": topic["proposed_title"],
                    "proposed_slug": slug,
                    "proposed_url": url,
                    "primary_keyword": topic.get("primary_keyword", ""),
                    "secondary_keywords": topic.get("secondary_keywords", ""),
                    "search_intent": topic.get("search_intent", "informational"),
                    "scope_statement": topic.get("scope_statement", ""),
                    "target_reader": "US plumbing business owners",
                    "evidence_status": topic.get("evidence_status", "intent_hypothesis"),
                    "evidence_source": topic.get("evidence_source", "Phase 1G scope"),
                    "evidence_date": "2026-10-18",
                    "volume_band": topic.get("volume_band", ""),
                    "numeric_volume": "",
                    "serp_validation_status": topic.get("serp_validation_status", "not_started"),
                    "overlap_risk": topic.get("overlap_risk", "low"),
                    "overlap_with_article_ids": "",
                    "recommended_action": "publish_standalone",
                    "priority": pri,
                    "priority_reason": pri_reason,
                    "publication_wave": wave,
                    "depends_on_article_ids": topic.get("depends_on_article_ids", ""),
                    "related_article_ids": topic.get("related_article_ids", ""),
                    "commercial_destination": topic.get("commercial_destination", ""),
                    "suggested_anchor_concept": "",
                    "authority_review_required": topic.get("authority_review_required", "no"),
                    "freshness_requirement": "review_annually" if sc["parent_category_id"] in ("2", "7") else "as_needed",
                    "status": "proposed",
                    "notes": "",
                }
            )
    return articles


def resolve_candidate_ids(articles: list[dict]) -> dict[str, str]:
    mapping = {}
    for a in articles:
        cid = a.get("source_candidate_id") or ""
        if cid:
            mapping[cid] = a["article_id"]
    return mapping


def patch_dependencies(articles: list[dict], cand_map: dict[str, str]) -> None:
    for a in articles:
        deps = a.get("depends_on_article_ids", "")
        if deps == "AC-01":
            a["depends_on_article_ids"] = cand_map.get("AC-01", "")
        rel = a.get("related_article_ids", "")
        if "AC-" in rel:
            parts = [cand_map.get(p.strip(), p.strip()) for p in rel.split(";")]
            a["related_article_ids"] = ";".join(parts)


def build_reconciliation(cand_map: dict[str, str]) -> list[dict]:
    rows = [
        {
            "source_candidate_id": "AC-01",
            "original_title": "How to Build a Plumbing Website: A Practical Guide for Plumbing Business Owners",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-01", ""),
            "final_title": "How to Build a Plumbing Website: A Practical Guide for Plumbing Business Owners",
            "reason": "Distinct how-to intent; >100 band; includes merged AC-05 page-structure section",
            "evidence_status": "tool_volume_band",
            "validation_needed": "Semrush numeric; AC-05 section scope vs Features",
        },
        {
            "source_candidate_id": "AC-02",
            "original_title": "Plumbing Website Examples: What Strong Plumbing Business Sites Include",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-02", ""),
            "final_title": "Plumbing Website Examples: What Strong Plumbing Business Sites Include",
            "reason": "Distinct inspiration intent vs AC-01; >100 band for examples",
            "evidence_status": "tool_volume_band",
            "validation_needed": "SERP for best plumbing websites; no unverified demo URL endorsements",
        },
        {
            "source_candidate_id": "AC-03",
            "original_title": "Best Plumber Website Builder: An Honest Comparison for Plumbing Businesses",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-03", ""),
            "final_title": "Best Plumber Website Builder: An Honest Comparison for Plumbing Businesses",
            "reason": "Comparison pillar; H1 framing avoids homepage head-term competition; hosts AC-06/07/10 sections",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Semrush; serp_observed Phase 1C",
        },
        {
            "source_candidate_id": "AC-04",
            "original_title": "How Much Does a Plumbing Website Cost? (Realistic Ranges for Owners)",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-04", ""),
            "final_title": "How Much Does a Plumbing Website Cost? Realistic Ranges for Owners",
            "reason": "TCO education distinct from #pricing commercial section",
            "evidence_status": "tool_volume_band",
            "validation_needed": "Semrush numeric",
        },
        {
            "source_candidate_id": "AC-05",
            "original_title": "What Pages Should a Plumbing Website Have?",
            "disposition": "merged_section",
            "final_article_id": cand_map.get("AC-01", ""),
            "final_title": "How to Build a Plumbing Website (section: essential pages)",
            "reason": "No standalone URL; complements /features/ five-page story per Phase 1E",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Semrush before standalone spin-out",
        },
        {
            "source_candidate_id": "AC-06",
            "original_title": "Plumber Website Builder vs Wix",
            "disposition": "merged_section",
            "final_article_id": cand_map.get("AC-03", ""),
            "final_title": "Best Plumber Website Builder (H2: vs Wix)",
            "reason": "No distinct Ahrefs row; spoke inside comparison pillar",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Semrush before standalone URL",
        },
        {
            "source_candidate_id": "AC-07",
            "original_title": "AI Plumbing Website Builder: What Plumbers Should Know Before Using One",
            "disposition": "merged_section",
            "final_article_id": cand_map.get("AC-03", ""),
            "final_title": "Best Plumber Website Builder (H2: AI builders)",
            "reason": "No exact match; section in AC-03",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Semrush",
        },
        {
            "source_candidate_id": "AC-08",
            "original_title": "Plumbing Website Checklist: What to Prepare Before You Launch",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-08", ""),
            "final_title": "Plumbing Website Checklist: What to Prepare Before You Launch",
            "reason": "Actionable checklist distinct from full AC-01 guide",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Publish after AC-01 draft",
        },
        {
            "source_candidate_id": "AC-09",
            "original_title": "Is a Website Worth It for Plumbers?",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-09", ""),
            "final_title": "Is a Website Worth It for Plumbers?",
            "reason": "ROI/decision intent distinct from AC-04 cost ranges",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Semrush",
        },
        {
            "source_candidate_id": "AC-10",
            "original_title": "WordPress for Plumbing Businesses: When It Makes Sense",
            "disposition": "merged_section",
            "final_article_id": cand_map.get("AC-03", ""),
            "final_title": "Best Plumber Website Builder (H2: WordPress)",
            "reason": "Deferred standalone per Phase 1E",
            "evidence_status": "no_exact_match_returned",
            "validation_needed": "Semrush",
        },
        {
            "source_candidate_id": "AC-11",
            "original_title": "Plumbing Website Hosting, Domain, and Maintenance: An Owner's Guide",
            "disposition": "standalone_article",
            "final_article_id": cand_map.get("AC-11", ""),
            "final_title": "Plumbing Website Hosting, Domain, and Maintenance: An Owner's Guide",
            "reason": "Consolidated infrastructure guide; hosting <100 band",
            "evidence_status": "tool_volume_band",
            "validation_needed": "Verify product facts in FAQ only",
        },
    ]
    return rows


def build_links(articles: list[dict], cand_map: dict[str, str]) -> list[dict]:
    by_id = {a["article_id"]: a for a in articles}
    links: list[dict] = []

    def add(src: str, dtype: str, dest_id: str = "", dest_url: str = "", anchor: str = "", purpose: str = "", pri: str = "P1", verify: str = "no"):
        links.append(
            {
                "source_article_id": src,
                "destination_type": dtype,
                "destination_article_id": dest_id,
                "destination_url": dest_url,
                "anchor_concept": anchor,
                "link_purpose": purpose,
                "priority": pri,
                "verification_required": verify,
            }
        )

    a01 = cand_map.get("AC-01")
    a03 = cand_map.get("AC-03")
    a04 = cand_map.get("AC-04")
    a02 = cand_map.get("AC-02")
    a08 = cand_map.get("AC-08")
    a09 = cand_map.get("AC-09")
    a11 = cand_map.get("AC-11")

    if a01:
        add(a01, "commercial", dest_url="https://plumberswebsites.com/#design", anchor="see how the preview process works", purpose="Process CTA")
        add(a01, "commercial", dest_url="https://plumberswebsites.com/features/", anchor="what's included in your plumbing site", purpose="Features depth")
        if a03:
            add(a01, "article", dest_id=a03, anchor="compare plumber website builders", purpose="Consideration funnel")
        if a04:
            add(a01, "article", dest_id=a04, anchor="what a plumbing website costs", purpose="Budget planning")
        if a08:
            add(a01, "article", dest_id=a08, anchor="pre-launch checklist", purpose="Actionable next step")

    if a03:
        add(a03, "commercial", dest_url="https://plumberswebsites.com/", anchor="preview your own plumbing website", purpose="Product next step", verify="avoid exact-match spam")
        if a04:
            add(a03, "article", dest_id=a04, anchor="plumbing website pricing ranges", purpose="Post-comparison budget")
        if a01:
            add(a03, "article", dest_id=a01, anchor="how to build a plumbing website", purpose="Implementation path")

    if a04:
        add(a04, "commercial", dest_url="https://plumberswebsites.com/#pricing", anchor="see our website pricing", purpose="Commercial offer after TCO")
        if a09:
            add(a04, "article", dest_id=a09, anchor="is a website worth it", purpose="ROI framing")

    if a02:
        add(a02, "commercial", dest_url="https://plumberswebsites.com/#business", anchor="choose a design for your business", purpose="Gallery selection")
        if a03:
            add(a02, "article", dest_id=a03, anchor="compare website builders", purpose="After inspiration")

    # GBP pillar to site
    gbp = next((a for a in articles if a.get("primary_keyword") == "google business profile for plumbers"), None)
    if gbp and a01:
        add(gbp["article_id"], "article", dest_id=a01, anchor="building your plumbing website", purpose="GBP → site creation")

    return links


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def write_master_toc_md(articles: list[dict], subcats: dict[str, dict]) -> None:
    lines = [
        "# Phase 1H — Master Table of Contents",
        "",
        "**Date:** 2026-10-18 | **Planning only** | **300 proposed standalone articles**",
        "",
        "## Executive summary",
        "",
        "Article-level master TOC under the approved **6 categories / 24 subcategories** (Phase 1F–1G). ",
        "Phase 1E candidates **AC-01–AC-11** reconciled (5 standalone, 4 merged sections, AC-05 → AC-01 + Features). ",
        "Authoritative row-level data: `master-article-inventory.csv`.",
        "",
        "## Source files",
        "",
        "Phase 1C–1G paths from brief were present in repository at generation time.",
        "",
        "## Publication waves (recommended sequence)",
        "",
        "1. **Wave 1:** Category 5 P1 cluster (SC18–SC21 core) + SC14–SC15 GBP/local SEO foundations.",
        "2. **Wave 2:** SC16–SC17, SC20 worth-it/hosting, Cat 3 P2 operations.",
        "3. **Wave 3:** Cat 1, 2, 6 breadth where evidence remains `intent_hypothesis`.",
        "",
        "## TOC by category",
        "",
    ]
    by_sc: dict[str, list[dict]] = defaultdict(list)
    for a in articles:
        by_sc[a["subcategory_id"]].append(a)

    for sc_id in sorted(by_sc.keys(), key=lambda x: (int(subcats[x]["parent_category_id"]), x)):
        sc = subcats[sc_id]
        lines.append(f"### {sc['parent_category_title']} → {sc['subcategory_title']} (`{sc_id}`)")
        lines.append("")
        for a in by_sc[sc_id]:
            pk = f" — *{a['primary_keyword']}*" if a["primary_keyword"] else ""
            cand = f" [{a['source_candidate_id']}]" if a["source_candidate_id"] else ""
            lines.append(f"- **{a['article_id']}** {a['proposed_title']}{pk}{cand} (`{a['priority']}`, wave {a['publication_wave']})")
        lines.append("")

    lines.extend(
        [
            "## AC-01–AC-11 reconciliation",
            "",
            "See `ac01-ac11-reconciliation.csv`.",
            "",
            "## Commercial keyword ownership",
            "",
            "- Homepage `plumber website builder` — not assigned as Academy article primary except educational comparison context in AC-03 article with high overlap flag.",
            "- Features `plumbing website design` — one supporting explainer article (SC19) with `overlap_risk=high` and link to /features/.",
            "",
            "## Research gaps",
            "",
            "- Semrush/GKP numerics; SERP validation for local SEO and comparison terms.",
            "- Cat 1/2/6 articles largely `intent_hypothesis`.",
            "",
        ]
    )
    (ROOT / "PHASE1H-MASTER-TOC.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    subcats = load_subcategories()
    articles = build_articles(subcats)
    cand_map = resolve_candidate_ids(articles)
    patch_dependencies(articles, cand_map)
    recon = build_reconciliation(cand_map)
    links = build_links(articles, cand_map)

    write_csv(ROOT / "master-article-inventory.csv", INVENTORY_FIELDS, articles)
    write_csv(ROOT / "master-internal-linking-map.csv", LINK_FIELDS, links)
    write_csv(ROOT / "ac01-ac11-reconciliation.csv", RECON_FIELDS, recon)
    write_master_toc_md(articles, subcats)

    c = Counter(a["parent_category_id"] for a in articles)
    print(f"Generated {len(articles)} articles; by category: {dict(sorted(c.items()))}")


if __name__ == "__main__":
    main()
