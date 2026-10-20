"""Generate Phase 1M Master SEO Topic-Cluster Map deliverables (research only)."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

from cluster_definitions import CLUSTERS

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
INVENTORY = ROOT / "research/phase1h-master-toc/master-article-inventory.csv"
SUBCAT = ROOT / "research/phase1g-subcategory-review/subcategory-master.csv"

PUBLISHED = {
    "A181": "https://plumberswebsites.com/academy/how-to-build-a-plumbing-website/",
    "A201": "https://plumberswebsites.com/academy/best-plumber-website-builder/",
    "A219": "https://plumberswebsites.com/academy/plumbing-website-cost/",
    "A200": "https://plumberswebsites.com/academy/plumbing-website-examples/",
    "A185": "https://plumberswebsites.com/academy/plumbing-website-checklist/",
}

COMMERCIAL_OWNERSHIP = {
    "plumber website builder": "Homepage / (commercial primary)",
    "plumbing website design": "Features /features/ (commercial primary)",
    "plumbing website template": "Designs /designs/ (commercial primary)",
    "plumbing website cost (product)": "Homepage /#pricing (commercial offer — Academy A219 is TCO education)",
}


def load_inventory() -> list[dict]:
    return list(csv.DictReader(INVENTORY.open(encoding="utf-8")))


def article_to_cluster() -> dict[str, str]:
    m: dict[str, str] = {}
    for cl in CLUSTERS:
        for aid in cl["article_ids"]:
            m[aid] = cl["cluster_id"]
    return m


def cluster_keywords(cl: dict, rows_by_id: dict[str, dict]) -> tuple[str, str, str]:
    pks: list[str] = []
    statuses: set[str] = set()
    for aid in cl["article_ids"]:
        r = rows_by_id.get(aid, {})
        if r.get("primary_keyword"):
            pks.append(r["primary_keyword"].strip())
        if r.get("evidence_status"):
            statuses.add(r["evidence_status"].strip())
    primary = pks[0] if pks else ""
    secondary = " | ".join(sorted(set(pks[1:])))[:500]
    ev = "; ".join(sorted(statuses)) if statuses else "intent_hypothesis"
    return primary, secondary, ev


def build_registry(rows_by_id: dict[str, dict]) -> list[dict]:
    reg: list[dict] = []
    for cl in CLUSTERS:
        pk, sec, ev = cluster_keywords(cl, rows_by_id)
        reg.append(
            {
                "cluster_id": cl["cluster_id"],
                "cluster_name": cl["cluster_name"],
                "parent_category_id": rows_by_id[cl["article_ids"][0]]["parent_category_id"],
                "primary_subcategory_id": cl["primary_subcategory_id"],
                "secondary_subcategory_ids": cl.get("secondary_subcategory_ids", ""),
                "reader_problem": cl["reader_problem"],
                "main_search_intent": cl["main_search_intent"],
                "lead_article_id": cl["lead_article_id"],
                "article_count": len(cl["article_ids"]),
                "article_ids": " ".join(cl["article_ids"]),
                "primary_keyword_cluster": pk,
                "secondary_keywords_cluster": sec,
                "keyword_evidence_status": ev,
                "evidence_sources": "master-article-inventory.csv",
                "related_cluster_ids": cl.get("related_cluster_ids", ""),
                "commercial_relevance": cl.get("commercial_relevance", "low"),
                "initial_priority": cl.get("initial_priority", "P3"),
                "priority_reason": cl.get("priority_reason", ""),
                "confidence": cl.get("confidence", "medium"),
                "unresolved_questions": cl.get("unresolved_questions", ""),
                "missing_supporting_articles": "",
            }
        )
    return reg


def build_assignments(rows: list[dict], a2c: dict[str, str]) -> list[dict]:
    out: list[dict] = []
    for r in rows:
        aid = r["article_id"]
        cid = a2c.get(aid, "UNASSIGNED")
        issue = ""
        if r.get("overlap_risk") in ("high", "medium") and r.get("overlap_with_article_ids"):
            issue = f"overlap_risk={r['overlap_risk']}; overlap_with={r['overlap_with_article_ids']}"
        if aid in PUBLISHED and r.get("status") != "published":
            issue = (issue + "; " if issue else "") + "inventory status may lag live publish"
        out.append(
            {
                "article_id": aid,
                "proposed_title": r["proposed_title"],
                "proposed_url": r["proposed_url"],
                "primary_cluster_id": cid,
                "parent_category_id": r["parent_category_id"],
                "subcategory_id": r["subcategory_id"],
                "primary_keyword": r.get("primary_keyword", ""),
                "evidence_status": r.get("evidence_status", ""),
                "volume_band": r.get("volume_band", ""),
                "publication_status": r.get("status", ""),
                "priority": r.get("priority", ""),
                "review_flag": issue or "",
            }
        )
    return out


def build_internal_links(rows_by_id: dict[str, dict]) -> list[dict]:
    links: list[dict] = []

    def add(src: str, dst: str, reason: str, anchor: str, status: str):
        links.append(
            {
                "source_article_id": src,
                "source_title": rows_by_id[src]["proposed_title"],
                "destination": dst,
                "link_reason": reason,
                "anchor_text_concept": anchor,
                "destination_status": status,
            }
        )

    # Published website cluster cross-links (approved boundaries)
    pub_links = [
        ("A181", "/academy/plumbing-website-checklist/", "Fuller staged checklist after inline minimum", "plumbing website checklist", "live"),
        ("A181", "/academy/plumbing-website-cost/", "TCO education distinct from pricing section", "how much a plumbing website costs", "live"),
        ("A181", "/academy/best-plumber-website-builder/", "Platform comparison after build-path overview", "compare website builder approaches", "live"),
        ("A181", "/academy/plumbing-website-examples/", "Design patterns after approach selection", "plumbing website examples", "live"),
        ("A181", "/features/", "Product page structure detail", "what is included on Features", "live"),
        ("A181", "/#design", "Preview workflow", "how the preview process works", "live"),
        ("A201", "/", "Commercial overview when reader wants done-for-you path", "PlumbersWebsites.com homepage", "live"),
        ("A201", "/academy/plumbing-website-cost/", "Budget TCO after comparing approaches", "plumbing website cost guide", "live"),
        ("A201", "/features/", "Product design/detail — not primary keyword target", "Features and supported fields", "live"),
        ("A201", "/#pricing", "Product subscription amounts", "homepage pricing section", "live"),
        ("A219", "/#pricing", "Commercial plan amounts only", "Pricing section", "live"),
        ("A219", "/academy/best-plumber-website-builder/", "Compare approaches before pricing math", "builder comparison guide", "live"),
        ("A219", "/academy/how-to-build-a-plumbing-website/", "Scope work before budgeting", "how to build a plumbing website", "live"),
        ("A200", "/designs/", "Template gallery — Designs owns plumbing website template", "Design gallery", "live"),
        ("A200", "/features/", "Five-page product structure", "Features page", "live"),
        ("A200", "/#design", "Preview workflow", "preview workflow on homepage", "live"),
        ("A185", "/academy/how-to-build-a-plumbing-website/", "Full build process complement", "how to build a plumbing website", "live"),
        ("A185", "/features/", "Field support verification", "Features and supported fields", "live"),
    ]
    for src, dst, reason, anchor, st in pub_links:
        add(src, dst, reason, anchor, st)

    # Cluster lead → commercial (planned articles with inventory destinations)
    for cl in CLUSTERS:
        if cl.get("commercial_relevance") not in ("high", "medium"):
            continue
        lead = cl["lead_article_id"]
        r = rows_by_id.get(lead, {})
        dest = r.get("commercial_destination", "").split(";")[0].strip()
        if dest and lead not in PUBLISHED:
            add(lead, dest, "Inventory commercial_destination for cluster lead", r.get("suggested_anchor_concept", "contextual product link"), "planned")

    # Subcategory hub links from published articles
    for aid in PUBLISHED:
        sc = rows_by_id[aid]["subcategory_id"]
        slug_map = {
            "SC18": "/academy/plumbing-websites-digital-tools/planning-and-building-your-plumbing-website/",
            "SC19": "/academy/plumbing-websites-digital-tools/website-builders-templates-and-examples/",
            "SC20": "/academy/plumbing-websites-digital-tools/website-costs-hosting-and-maintenance/",
        }
        if sc in slug_map:
            add(aid, slug_map[sc], "Section hub for related guides", "more guides in this section", "live")

    return links


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_master_md(registry: list[dict]) -> None:
    lines = [
        "# Master SEO Topic-Cluster Map (Phase 1M)",
        "",
        "**Date:** 2026-10-18 | **Planning only** | **Does not change Academy navigation**",
        "",
        "## Architecture layers",
        "",
        "1. **Six categories** (Phase 1F) — unchanged.",
        "2. **24 subcategories** (Phase 1G) — unchanged.",
        "3. **~54 SEO topic clusters** (this document) — planning layer only.",
        "4. **300 articles** A001–A300 — IDs, titles, URLs unchanged.",
        "",
        "## Published articles (live)",
        "",
        "| ID | Title | URL | Cluster |",
        "|----|-------|-----|---------|",
        "| A181 | How to Build a Plumbing Website | `/academy/how-to-build-a-plumbing-website/` | CL037 |",
        "| A201 | Best Plumber Website Builder | `/academy/best-plumber-website-builder/` | CL041 |",
        "| A219 | Plumbing Website Cost | `/academy/plumbing-website-cost/` | CL044 |",
        "| A200 | Plumbing Website Examples | `/academy/plumbing-website-examples/` | CL042 |",
        "| A185 | Plumbing Website Checklist | `/academy/plumbing-website-checklist/` | CL037 |",
        "",
        "## Commercial keyword ownership (preserve)",
        "",
    ]
    for k, v in COMMERCIAL_OWNERSHIP.items():
        lines.append(f"- **{k}** → {v}")
    lines.extend(
        [
            "",
            "## Assumptions",
            "",
            "- Cluster boundaries are derived from `master-article-inventory.csv` plus Phase 1D–1G evidence fields.",
            "- Volume **bands** (e.g. >100, <100) are not exact monthly searches.",
            "- `no_exact_match_returned` does **not** mean zero demand.",
            "- Several Cat 1–3 clusters lack keyword tool data (`intent_hypothesis`) — lower confidence.",
            "",
            "## Cluster summary by priority",
            "",
        ]
    )
    by_pri: dict[str, list[dict]] = defaultdict(list)
    for r in registry:
        by_pri[r["initial_priority"]].append(r)
    for pri in ("P1", "P2", "P3"):
        lines.append(f"### Priority {pri} ({len(by_pri[pri])} clusters)")
        lines.append("")
        for r in sorted(by_pri[pri], key=lambda x: x["cluster_id"]):
            lines.append(
                f"- **{r['cluster_id']}** — {r['cluster_name']} ({r['primary_subcategory_id']}, {r['article_count']} articles, lead {r['lead_article_id']})"
            )
        lines.append("")
    lines.append("Full row-level data: `topic-cluster-registry.csv`, `cluster-article-assignments.csv`.")
    (OUT / "MASTER-SEO-TOPIC-CLUSTER-MAP.md").write_text("\n".join(lines), encoding="utf-8")


def write_roadmap() -> None:
    text = """# Publication roadmap (Phase 1M)

**Planning only** — sequence by cluster value and evidence, not numeric article ID order.

## Recommended next 5 clusters

| Rank | Cluster | Why now | First article batch (IDs) | Link updates when published |
|------|---------|---------|---------------------------|-----------------------------|
| 1 | **CL027** GBP setup | P1 local foundation; partial Phase 1D evidence | A121–A125 | Cross-link from A181/A200; GBP → homepage URL article A123 |
| 2 | **CL029** Local SEO strategy | Pairs with GBP; distinct from SC21 on-page | A136–A139 | Link from CL027/CL028; avoid duplicating SC21 |
| 3 | **CL047** Mobile & click-to-call | P1 conversion; supports `/features/` | A239–A240, A243 | Link from published A181/A185 checklists |
| 4 | **CL041** Builder comparison (extend) | A201 live; fill gaps without homepage cannibalization | A211, A204, A212 (after SERP check) | Already interlinked with A219/A200 |
| 5 | **CL038** Page content planning | Natural follow-on to A181/A185 | A186–A189 | Add links from A181 related reading |

## Clusters to defer pending evidence

- **CL041** deep comparisons (A206–A209) until `best plumber website builder` / platform SERPs validated.
- **CL029** until mandatory SERP validation on `seo for plumbing business` (Phase 1G note).
- **CL043** A210 (`plumbing website design`) — human approval required so Features primary keyword is supported, not competed with.

## Dependencies

- Complete **CL037** support articles (A183 preview, A184 done-for-you) before heavy CL041 promotion.
- **CL044** / **CL045** — keep A219 as TCO lead; A220 worth-it separate intent.
- **SC15 vs SC21** — local strategy (CL029–CL031) before on-page checklist lead A246.

## Proposed merges / conflicts needing approval

| Issue | Articles | Recommendation |
|-------|----------|----------------|
| `plumbing website design` on A210 | A210 vs `/features/` | Publish only as Features-support explainer; do not target Features H1 |
| `best plumbing websites` SERP ambiguity | A203 | Validate hire-a-plumber vs inspiration intent before drafting |
| AC-05 pages merged into A181 | inventory scope | No standalone URL unless new keyword evidence |
| Overlap high on A201 | A201 vs homepage | Keep comparison title; monitor GSC after batch 2 |

## Batches not started

No article HTML generation in Phase 1M. Next wave after clusters 1–5: **CL028** (GBP optimization), **CL049** (on-page SEO), **CL046** (hosting/maintenance).
"""
    (OUT / "publication-roadmap.md").write_text(text, encoding="utf-8")


def main() -> None:
    rows = load_inventory()
    rows_by_id = {r["article_id"]: r for r in rows}
    a2c = article_to_cluster()
    registry = build_registry(rows_by_id)
    assignments = build_assignments(rows, a2c)
    links = build_internal_links(rows_by_id)

    write_csv(
        OUT / "topic-cluster-registry.csv",
        list(registry[0].keys()),
        registry,
    )
    write_csv(
        OUT / "cluster-article-assignments.csv",
        list(assignments[0].keys()),
        assignments,
    )
    write_csv(
        OUT / "internal-linking-map.csv",
        list(links[0].keys()),
        links,
    )
    write_master_md(registry)
    write_roadmap()
    print(f"Wrote {len(CLUSTERS)} clusters, {len(assignments)} assignments, {len(links)} link rows to {OUT}")


if __name__ == "__main__":
    main()
