"""
Phase 1B — Provisional ranked keyword opportunities (research only).
Reads Phase 1 registry; does not modify Phase 1 files.
No invented volume/KD/traffic.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).parent
REGISTRY = ROOT / "keyword-opportunity-registry.csv"
OUT_CSV = ROOT / "ranked-keyword-opportunities.csv"
MAX_RANK = 130

# Tier-specific floors (provisional — Tier 3 capped lower so it cannot outrank buying intent)
MIN_SCORE_BY_TIER = {"1": 40, "2": 38, "3": 33}

# Phase 1 P1 business-growth clusters (SERP validation still required before publish)
TIER3_PILLAR_CLUSTERS = {"TG-01_leads", "TG-03_gbp", "TG-04_seo_owner"}

# Owner ID -> canonical URL + content type
PAGE_MAP: dict[str, dict] = {
    "homepage": {
        "url": "https://plumberswebsites.com/",
        "status": "existing",
        "type": "commercial",
        "supports": "academy_comparison_pillar; academy_how_to_build; academy_cost_guide",
    },
    "features_page": {
        "url": "https://plumberswebsites.com/features/",
        "status": "existing",
        "type": "commercial",
        "supports": "academy_how_to_build; academy_comparison_pillar",
    },
    "homepage_design_gallery": {
        "url": "https://plumberswebsites.com/#business",
        "status": "existing",
        "type": "commercial_section",
        "supports": "academy_examples_hub",
    },
    "homepage_pricing": {
        "url": "https://plumberswebsites.com/#pricing",
        "status": "existing",
        "type": "commercial_section",
        "supports": "academy_cost_guide",
    },
    "how_it_works_section": {
        "url": "https://plumberswebsites.com/#design",
        "status": "existing",
        "type": "commercial_section",
        "supports": "academy_how_to_build",
    },
    "homepage+features": {
        "url": "https://plumberswebsites.com/ + /features/",
        "status": "existing",
        "type": "commercial",
        "supports": "",
    },
    "homepage_pricing + academy_cost_guide": {
        "url": "https://plumberswebsites.com/#pricing",
        "status": "existing+proposed",
        "type": "commercial_section",
        "supports": "academy_cost_guide",
    },
    "features_five_pages": {
        "url": "https://plumberswebsites.com/features/",
        "status": "existing",
        "type": "commercial",
        "supports": "academy_how_to_build",
    },
    "academy_comparison_pillar": {
        "url": "https://plumberswebsites.com/academy/best-plumber-website-builder/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "homepage; features_page",
        "related_commercial": "homepage",
    },
    "academy_comparison_wix": {
        "url": "https://plumberswebsites.com/academy/plumber-website-builder-vs-wix/",
        "status": "proposed",
        "type": "academy_comparison",
        "supports": "academy_comparison_pillar; homepage",
        "related_commercial": "homepage",
    },
    "academy_comparison_squarespace": {
        "url": "https://plumberswebsites.com/academy/plumber-website-builder-vs-squarespace/",
        "status": "proposed",
        "type": "academy_comparison",
        "supports": "academy_comparison_pillar",
        "related_commercial": "homepage",
    },
    "academy_how_to_build": {
        "url": "https://plumberswebsites.com/academy/how-to-build-a-plumbing-website/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "homepage; features_page",
        "related_commercial": "homepage",
    },
    "academy_cost_guide": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-cost/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "homepage_pricing; academy_comparison_pillar",
        "related_commercial": "homepage",
    },
    "academy_checklist": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-checklist/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_how_to_build; features_page",
        "related_commercial": "homepage",
    },
    "academy_examples_hub": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-examples/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "features_page; homepage_design_gallery",
        "related_commercial": "features_page",
    },
    "academy_ai_builders": {
        "url": "https://plumberswebsites.com/academy/ai-plumbing-website-builder/",
        "status": "proposed",
        "type": "academy_comparison",
        "supports": "academy_comparison_pillar; homepage",
        "related_commercial": "homepage",
    },
    "academy_wordpress": {
        "url": "https://plumberswebsites.com/academy/wordpress-for-plumbing-business/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_comparison_pillar",
        "related_commercial": "homepage",
    },
    "academy_worth_it": {
        "url": "https://plumberswebsites.com/academy/is-a-website-worth-it-for-plumbers/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_how_to_build; homepage",
        "related_commercial": "homepage",
    },
    "academy_agency_alt": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-agency-alternatives/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_cost_guide; homepage",
        "related_commercial": "homepage",
    },
    "academy_conversion_hub": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-conversion/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "features_page",
        "related_commercial": "features_page",
    },
    "academy_hosting": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-hosting-and-domain/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "homepage_faq",
        "related_commercial": "homepage",
    },
    "academy_maintenance": {
        "url": "https://plumberswebsites.com/academy/plumbing-website-maintenance/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "features_page",
        "related_commercial": "homepage",
    },
    "academy_local_seo": {
        "url": "https://plumberswebsites.com/academy/local-seo-plumbing-company/",
        "status": "proposed",
        "type": "academy_pillar",
        "supports": "features_page; homepage",
        "related_commercial": "homepage",
    },
    "academy_gbp": {
        "url": "https://plumberswebsites.com/academy/google-business-profile-plumbers/",
        "status": "proposed",
        "type": "academy_pillar",
        "supports": "academy_local_seo; homepage",
        "related_commercial": "homepage",
    },
    "academy_seo_pillar": {
        "url": "https://plumberswebsites.com/academy/seo-for-plumbing-business/",
        "status": "proposed",
        "type": "academy_pillar",
        "supports": "academy_local_seo; features_page",
        "related_commercial": "homepage",
    },
    "academy_leads": {
        "url": "https://plumberswebsites.com/academy/get-more-plumbing-customers/",
        "status": "proposed",
        "type": "academy_pillar",
        "supports": "homepage; academy_gbp",
        "related_commercial": "homepage",
    },
    "academy_marketing": {
        "url": "https://plumberswebsites.com/academy/plumbing-business-marketing-ideas/",
        "status": "proposed",
        "type": "academy_hub",
        "supports": "academy_leads",
        "related_commercial": "homepage",
    },
    "academy_new_business": {
        "url": "https://plumberswebsites.com/academy/starting-plumbing-business-website/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "homepage; academy_checklist",
        "related_commercial": "homepage",
    },
    "academy_online_leads": {
        "url": "https://plumberswebsites.com/academy/plumbing-leads-online/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_leads",
        "related_commercial": "homepage",
    },
    "academy_online_presence": {
        "url": "https://plumberswebsites.com/academy/plumbing-business-online-presence/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_new_business; academy_gbp",
        "related_commercial": "homepage",
    },
    "academy_branding": {
        "url": "https://plumberswebsites.com/academy/plumbing-company-branding-website/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "features_page",
        "related_commercial": "features_page",
    },
    "academy_reviews": {
        "url": "https://plumberswebsites.com/academy/reviews-on-plumbing-website/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_gbp; features_page",
        "related_commercial": "features_page",
    },
    "academy_crm_website": {
        "url": "https://plumberswebsites.com/academy/crm-website-vs-plumbing-website/",
        "status": "proposed",
        "type": "academy_guide",
        "supports": "academy_comparison_pillar",
        "related_commercial": "homepage",
    },
    "homepage_faq": {
        "url": "https://plumberswebsites.com/#faq",
        "status": "existing",
        "type": "commercial_section",
        "supports": "",
    },
}

# Cluster-level default owner when primary_intent_owner_url empty
CLUSTER_OWNER = {
    "TR-09_conversion_elements": "academy_conversion_hub",
    "TR-08_mobile": "features_page",
    "TR-10_hosting": "academy_hosting",
    "TR-11_maintenance": "academy_maintenance",
    "TR-12_improve": "academy_maintenance",
    "TR-13_examples": "academy_examples_hub",
    "TR-15_crm_bundled": "academy_crm_website",
    "TR-16_competitor_brands": "academy_comparison_pillar",
    "TR-03_agency_alt": "academy_agency_alt",
    "TR-01_comparisons": "academy_comparison_pillar",
    "TR-02_vs_wix": "academy_comparison_wix",
    "TR-02_vs_squarespace": "academy_comparison_squarespace",
    "TR-03_wordpress": "academy_wordpress",
    "TR-04_how_to_build": "academy_how_to_build",
    "TR-05_checklist": "academy_checklist",
    "TR-06_site_structure": "features_five_pages",
    "TR-07_features": "features_page",
    "TR-14_ai_builders": "academy_ai_builders",
    "TG-01_leads": "academy_leads",
    "TG-02_marketing": "academy_marketing",
    "TG-03_gbp": "academy_gbp",
    "TG-04_seo_owner": "academy_seo_pillar",
    "TG-05_brand": "academy_branding",
    "TG-06_new_business": "academy_new_business",
    "TG-07_trust": "academy_reviews",
    "TG-08_software": "academy_crm_website",
    "TB-07_pricing": "academy_cost_guide",
    "TB-08_free_trial": "homepage_faq",
}

DEFER_KEYWORDS = {
    # thin / weak product tie / likely SERP noise — defer unless SERP validates
    "plumbing website chatbot",
    "plumbing website live chat",
    "plumbing website financing banner",
    "plumbing website google tag manager",
    "plumbing franchise website requirements",
    "nextdoor for plumbing business",
    "plumbing truck wrap website url",
    "plumbing business card website qr code",
    "plumbing website color scheme",
    "plumbing website hero section ideas",
}

BUYING = {"high": 15, "medium-high": 12, "medium": 8, "low-medium": 5, "low": 2, "none": 0}
TIER = {"1": 40, "2": 28, "3": 16}
RELEVANCE = {"critical": 10, "high": 8, "": 4, "none": 0}
CONF = {"high": 8, "medium": 5, "low": 2}
PRIO = {"P0": 12, "P1": 9, "P2": 5, "P3": 2, "P2-P3": 3, "exclude": 0}


def resolve_owner(row: dict) -> str:
    owner = (row.get("primary_intent_owner_url") or "").strip()
    if owner:
        return owner
    return CLUSTER_OWNER.get(row.get("cluster", ""), "academy_marketing")


def score_row(row: dict) -> tuple[int, str]:
    kw = row["keyword"].lower()
    if kw in DEFER_KEYWORDS:
        return 0, "Deferred: weak differentiation or noisy intent — validate SERP before production"

    s = 0
    parts: list[str] = []

    t = row.get("tier", "")
    s += TIER.get(t, 0)
    parts.append(f"tier {t} (+{TIER.get(t, 0)})")

    bs = row.get("buying_strength", "")
    s += BUYING.get(bs, 4)
    parts.append(f"buying {bs} (+{BUYING.get(bs, 4)})")

    cr = row.get("commercial_relevance", "")
    s += RELEVANCE.get(cr, 4)
    parts.append(f"relevance (+{RELEVANCE.get(cr, 4)})")

    cf = row.get("confidence", "medium")
    s += CONF.get(cf, 5)
    parts.append(f"confidence (+{CONF.get(cf, 5)})")

    pr = row.get("priority", "")
    s += PRIO.get(pr, 3)
    parts.append(f"registry priority (+{PRIO.get(pr, 3)})")

    if row.get("competitor_urls") or "SERP" in row.get("evidence_source", ""):
        s += 5
        parts.append("SERP/competitor evidence (+5)")
    if row.get("serp_page_types"):
        s += 2
        parts.append("SERP page types noted (+2)")

    owner = resolve_owner(row)
    pm = PAGE_MAP.get(owner, {})
    if pm.get("status") == "existing":
        s += 3
        parts.append("existing page leverage (+3)")

    # Tier 3 penalty for intent contamination risk unless strong website tie
    if t == "3" and "website" not in kw and "gbp" not in kw and "google business" not in kw:
        s -= 4
        parts.append("Tier 3 non-website phrasing (−4)")

    if row.get("cluster") in TIER3_PILLAR_CLUSTERS and t == "3":
        s += 6
        parts.append("Tier 3 pillar cluster (+6)")

    rationale = "; ".join(parts)
    return s, rationale


def passes_floor(row: dict, score: int) -> bool:
    return score >= MIN_SCORE_BY_TIER.get(row.get("tier", ""), 38)


def primary_in_group(rows_scored: list[tuple[dict, int, str]]) -> set[str]:
    """Highest score per cannibal_group becomes primary target keyword."""
    groups: dict[str, tuple[int, str]] = {}
    for row, sc, _ in rows_scored:
        cg = row.get("cannibal_group") or row.get("cluster", "")
        kw = row["keyword"]
        if cg not in groups or sc > groups[cg][0]:
            groups[cg] = (sc, kw)
    return {kw for _, kw in groups.values()}


def main() -> None:
    with REGISTRY.open(newline="", encoding="utf-8") as f:
        registry = list(csv.DictReader(f))

    candidates = [r for r in registry if r.get("tier") != "EX"]
    scored: list[tuple[dict, int, str]] = []
    for r in candidates:
        sc, rationale = score_row(r)
        if passes_floor(r, sc):
            scored.append((r, sc, rationale))

    # Tier 1 first, then 2, then 3; within tier by score
    scored.sort(
        key=lambda x: (x[0]["tier"], -x[1], x[0]["keyword"]),
    )
    # Re-sort globally but preserve tier ordering: concatenate sorted sublists
    by_tier = {"1": [], "2": [], "3": []}
    for item in scored:
        by_tier[item[0]["tier"]].append(item)
    for t in by_tier:
        by_tier[t].sort(key=lambda x: (-x[1], x[0]["keyword"]))
    scored = by_tier["1"] + by_tier["2"] + by_tier["3"]
    primary_kws = primary_in_group(scored)

    fields = [
        "rank",
        "priority_score",
        "score_rationale",
        "keyword",
        "keyword_cluster",
        "tier",
        "search_intent",
        "audience_fit",
        "buying_intent_class",
        "us_monthly_volume",
        "volume_source",
        "keyword_difficulty",
        "kd_source",
        "serp_evidence",
        "proposed_primary_page_url",
        "page_status",
        "content_type",
        "target_role",
        "related_commercial_page",
        "supporting_content_opportunities",
        "internal_linking_role",
        "confidence_level",
        "research_notes",
    ]

    out_rows: list[dict] = []
    for rank, (row, sc, rationale) in enumerate(scored[:MAX_RANK], start=1):
        owner = resolve_owner(row)
        pm = PAGE_MAP.get(owner, {})
        url = pm.get("url", f"(map owner: {owner})")
        status = pm.get("status", "proposed")
        ctype = pm.get("type", "academy_guide")
        related = pm.get("related_commercial", "homepage" if row["tier"] in ("1", "2") else "homepage")
        related_url = PAGE_MAP.get(related, {}).get("url", "https://plumberswebsites.com/")

        role = "primary" if row["keyword"] in primary_kws else "supporting_variation"
        # Head term always primary
        if row["keyword"] == "plumber website builder":
            role = "primary"

        link_role = {
            "primary": "Owns principal intent; receive links from supporting guides in same cluster",
            "supporting_variation": "Cover naturally on primary page; optional FAQ/H2; no separate URL",
        }[role]

        if row["tier"] == "1" and role == "primary":
            link_role = "Commercial hub; link out to Features and top Academy guides"
        elif ctype.startswith("academy") and role == "primary":
            link_role = "Consideration/education; contextual link to homepage and Features once per article"

        out_rows.append(
            {
                "rank": rank,
                "priority_score": sc,
                "score_rationale": rationale,
                "keyword": row["keyword"],
                "keyword_cluster": row.get("cluster", ""),
                "tier": row.get("tier", ""),
                "search_intent": row.get("intent_class", ""),
                "audience_fit": row.get("audience_fit", ""),
                "buying_intent_class": row.get("buying_strength", ""),
                "us_monthly_volume": row.get("us_monthly_volume", ""),
                "volume_source": "not_collected" if not row.get("us_monthly_volume") else "",
                "keyword_difficulty": row.get("keyword_difficulty", ""),
                "kd_source": "not_collected" if not row.get("keyword_difficulty") else "",
                "serp_evidence": "; ".join(
                    filter(
                        None,
                        [
                            row.get("serp_page_types", ""),
                            row.get("competitor_urls", ""),
                            row.get("evidence_source", ""),
                        ],
                    )
                )[:500],
                "proposed_primary_page_url": url,
                "page_status": status,
                "content_type": ctype,
                "target_role": role,
                "related_commercial_page": related_url,
                "supporting_content_opportunities": pm.get("supports", ""),
                "internal_linking_role": link_role,
                "confidence_level": row.get("confidence", ""),
                "research_notes": row.get("notes", ""),
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out_rows)

    in_pool = len(scored)
    print(f"Ranked {len(out_rows)} opportunities (cap {MAX_RANK}, tier floors {MIN_SCORE_BY_TIER})")
    print(f"Qualified pool: {in_pool}; not ranked (below floor or over cap): {len(candidates) - len(out_rows)}")


if __name__ == "__main__":
    main()
