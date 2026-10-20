"""
Phase 1C — Strict keyword quality audit (research only).
Preserves Phase 1 / 1B files. Outputs List A / B / C CSVs.
No invented search volume or KD.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).parent
REGISTRY = ROOT / "keyword-opportunity-registry.csv"
RANKED = ROOT / "ranked-keyword-opportunities.csv"

OUT_A = ROOT / "qualified-keyword-opportunities.csv"
OUT_B = ROOT / "unverified-keyword-opportunities.csv"
OUT_C = ROOT / "rejected-and-combined-keywords.csv"

# --- List A: qualified clusters (primary keyword only) ---
# evidence_tier: SERP_OBSERVED = multiple commercial/guide results seen (no volume)
QUALIFIED_CLUSTERS: list[dict] = [
    {
        "cluster_id": "TB-01_head_builder",
        "primary_keyword": "plumber website builder",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/",
        "page_action": "improve_existing",
        "serp_evidence": "US Google 2026-10-18: product landings (Grow Local, Siimple, Mixo, Pixlel), comparison guides, AI builders; no single dominant brand",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "SERP density implies commercial demand; volume requires Semrush/GKP",
    },
    {
        "cluster_id": "TB-12_brand",
        "primary_keyword": "plumberswebsites.com",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/",
        "page_action": "improve_existing",
        "serp_evidence": "Navigational — brand queries serve homepage",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Low volume but highest conversion intent when present",
    },
    {
        "cluster_id": "TB-02_website_for_plumbers",
        "primary_keyword": "website for plumbers",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/",
        "page_action": "improve_existing",
        "serp_evidence": "Homepage meta/FAQ already targets; SERP mixes guides and products",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Cover as supporting copy on homepage, not separate URL",
    },
    {
        "cluster_id": "TB-09_dfy",
        "primary_keyword": "done for you plumber website",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/",
        "page_action": "improve_existing",
        "serp_evidence": "Competitors position DFY/managed (FlashCrafter, Pixlel Pro, homepage copy)",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Homepage + Features narrative",
    },
    {
        "cluster_id": "TB-10_preview",
        "primary_keyword": "preview plumbing website before paying",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/#design",
        "page_action": "improve_existing",
        "serp_evidence": "Differentiator vs AI builders; Zarla/Mixo emphasize free preview patterns",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Long-tail likely; high intent when searched",
    },
    {
        "cluster_id": "TB-03_design_service",
        "primary_keyword": "plumbing website design",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/features/",
        "page_action": "improve_existing",
        "serp_evidence": "SERP includes agency services, portfolios, guides — owner intent",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Features page owner; not head builder H1",
    },
    {
        "cluster_id": "TR-07_features",
        "primary_keyword": "plumbing website features",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/features/",
        "page_action": "improve_existing",
        "serp_evidence": "Investigation intent maps to product/feature pages",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Same URL as design cluster — one page serves both",
    },
    {
        "cluster_id": "TB-07_pricing",
        "primary_keyword": "plumbing website cost",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/#pricing",
        "page_action": "improve_existing + new_academy",
        "serp_evidence": "PAA on head SERP; Wix plumbing website cost article ranks",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Split: #pricing (buyers) + Academy TCO guide (researchers)",
    },
    {
        "cluster_id": "TB-05_templates",
        "primary_keyword": "plumbing website template",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/#business",
        "page_action": "improve_existing",
        "serp_evidence": "Wix template marketplace ranks; owner compares DIY templates vs done-for-you",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium-high",
        "traffic_potential_note": "Six-design gallery + short explainer on template vs custom foundation",
    },
    {
        "cluster_id": "TB-06_examples",
        "primary_keyword": "plumbing website examples",
        "tier": "1",
        "page_url": "https://plumberswebsites.com/academy/plumbing-website-examples/",
        "page_action": "new_academy",
        "serp_evidence": "Listicles and portfolios rank (Skill Mammoth-style content)",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium-high",
        "traffic_potential_note": "Use live Proton example; tie to design gallery",
    },
    {
        "cluster_id": "TR-01_comparisons",
        "primary_keyword": "best plumber website builder",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/best-plumber-website-builder/",
        "page_action": "new_academy",
        "serp_evidence": "US Google 2026-10-18: Zarla, ElmSite, FlashCrafter, Yola, Squarespace blog — comparison SERP",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Core consideration-stage asset; links to homepage",
    },
    {
        "cluster_id": "TR-04_how_to_build",
        "primary_keyword": "how to build a plumbing website",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/how-to-build-a-plumbing-website/",
        "page_action": "new_academy",
        "serp_evidence": "Wix how-to, trade blogs rank step-by-step guides",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Educational H1; product as one path",
    },
    {
        "cluster_id": "TR-06_site_structure",
        "primary_keyword": "what pages should a plumbing website have",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/features/",
        "page_action": "improve_existing",
        "serp_evidence": "Aligns with five-page product; guides rank for page-structure questions",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "high",
        "traffic_potential_note": "Expand Features; optional FAQ section — not a separate URL required",
    },
    {
        "cluster_id": "TR-02_vs_wix",
        "primary_keyword": "plumber website builder vs wix",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/plumber-website-builder-vs-wix/",
        "page_action": "new_academy_spoke",
        "serp_evidence": "Wix ranks for plumber website topics; comparison intent common in builder SERPs",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium-high",
        "traffic_potential_note": "Publish after comparison pillar; may be H2 within pillar if volume low",
    },
    {
        "cluster_id": "TR-14_ai_builders",
        "primary_keyword": "ai plumbing website builder",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/ai-plumbing-website-builder/",
        "page_action": "new_academy_spoke",
        "serp_evidence": "Head SERP includes Butternut, Mixo, Pixlel, Replit-class products",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium-high",
        "traffic_potential_note": "Section or spoke under comparison pillar preferred first",
    },
    {
        "cluster_id": "TR-05_checklist",
        "primary_keyword": "plumbing website checklist",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/plumbing-website-checklist/",
        "page_action": "new_academy",
        "serp_evidence": "Standard content format in trade marketing SERPs",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "Defer until how-to + Features strengthened",
    },
    {
        "cluster_id": "TR-04_worth_it",
        "primary_keyword": "is a website worth it for plumbers",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/is-a-website-worth-it-for-plumbers/",
        "page_action": "new_academy",
        "serp_evidence": "ROI/decision content supports consideration funnel",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "Links to homepage after Wave 1",
    },
    {
        "cluster_id": "TR-09_conversion_hub",
        "primary_keyword": "click to call plumber website",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/plumbing-website-conversion/",
        "page_action": "new_academy",
        "serp_evidence": "Competitors emphasize mobile click-to-call (FlashCrafter, ElmSite criteria)",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "One hub page — not separate URLs per micro-feature",
    },
    {
        "cluster_id": "TR-03_wordpress",
        "primary_keyword": "wordpress for plumbing business",
        "tier": "2",
        "page_url": "https://plumberswebsites.com/academy/wordpress-for-plumbing-business/",
        "page_action": "new_academy_spoke",
        "serp_evidence": "Comparison tables include WordPress.com; plugin flexibility angle",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "high",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "Lower priority than Wix spoke",
    },
    {
        "cluster_id": "TG-03_gbp",
        "primary_keyword": "google business profile for plumbers",
        "tier": "3",
        "page_url": "https://plumberswebsites.com/academy/google-business-profile-plumbers/",
        "page_action": "new_academy",
        "serp_evidence": "Owner-operators search GBP setup; SERP must be validated for agency vs owner content",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "medium-high",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "Website URL on GBP — natural product tie-in",
    },
    {
        "cluster_id": "TG-04_local_seo",
        "primary_keyword": "local seo for plumbing company",
        "tier": "3",
        "page_url": "https://plumberswebsites.com/academy/local-seo-plumbing-company/",
        "page_action": "new_academy",
        "serp_evidence": "Risk: homeowner/agency SERPs — owner framing required; no city matrices",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "medium-high",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "SERP validation mandatory before write",
    },
    {
        "cluster_id": "TG-04_seo_pillar",
        "primary_keyword": "seo for plumbing business",
        "tier": "3",
        "page_url": "https://plumberswebsites.com/academy/seo-for-plumbing-business/",
        "page_action": "new_academy",
        "serp_evidence": "Distinct from plumberseo.net homeowner keyword lists if framed for owners",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "medium",
        "commercial_opportunity": "medium",
        "traffic_potential_note": "Do not target 'rank for emergency plumber'",
    },
    {
        "cluster_id": "TG-01_leads",
        "primary_keyword": "how to get more plumbing customers",
        "tier": "3",
        "page_url": "https://plumberswebsites.com/academy/get-more-plumbing-customers/",
        "page_action": "new_academy",
        "serp_evidence": "Broad marketing SERP — noisy; website-as-hub angle only",
        "traffic_evidence": "UNVERIFIED — VOLUME UNKNOWN",
        "audience_fit": "medium",
        "commercial_opportunity": "low-medium",
        "traffic_potential_note": "Wave 3 only after commercial funnel live",
    },
]

QUALIFIED_CLUSTER_IDS = {c["cluster_id"] for c in QUALIFIED_CLUSTERS}

# Patterns → List C
NARROW_FEATURE = re.compile(
    r"(mobile menu|ssl certificate|privacy policy|terms of service|insurance badge|"
    r"service guarantee wording|color scheme|hero section ideas|google tag manager|"
    r"chatbot|live chat|financing banner|stock photos vs|truck wrap|qr code|"
    r"nextdoor for|yard signs and website|franchise website requirements|"
    r"schema markup|meta title|keywords for seo|blog for seo|"
    r"backup|accessibility$|emergency plumbing banner website)",
    re.I,
)

COMPETITOR_BRAND_ONLY = re.compile(
    r"^(grow local|siimple|elmsite|zarla|instantsite|butternut|yola|meku|"
    r"duda|weebly|godaddy|durable|mixo|pixlel|flashcrafter).*plumber website",
    re.I,
)

BRAND_COMPETITOR_PHRASES = {
    "grow local plumber website",
    "siimple plumber website",
    "elmsite plumber website",
    "zarla plumber website",
    "instantsite plumber website",
    "butternut plumber website",
    "yola plumber website",
    "meku plumber website",
}

PROMISING_UNVERIFIED_CLUSTERS = {
    "TR-10_hosting": "plumbing website hosting",
    "TR-11_maintenance": "plumbing website maintenance",
    "TR-12_improve": "redesign plumbing website",
    "TR-03_agency_alt": "plumbing web design agency",
    "TR-15_crm_bundled": "jobber website for plumbers",
    "TR-02_vs_squarespace": "plumber website builder vs squarespace",
    "TR-13_examples": "plumber website design examples 2026",
    "TG-02_marketing": "plumbing business marketing ideas",
    "TG-06_new_business": "start a plumbing business website",
    "TG-06_online_presence": "plumbing business online presence",
    "TG-07_trust": "reviews on plumbing website",
    "TG-05_brand": "plumbing company branding",
    "TG-08_software": "best software for plumbing business",
    "TB-08_free_trial": "free plumbing website",
}

FIELDS_A = [
    "list_a_rank",
    "cluster_id",
    "primary_keyword",
    "secondary_keywords_in_cluster",
    "tier",
    "search_intent_summary",
    "traffic_evidence",
    "traffic_potential",
    "audience_intent_fit",
    "commercial_ranking_opportunity",
    "overall_opportunity",
    "serp_evidence_summary",
    "serp_evidence_date",
    "competitive_landscape",
    "proposed_page_url",
    "page_action",
    "new_url_required",
    "distinct_page_justified",
    "confidence",
    "ranking_rationale",
]

FIELDS_B = [
    "keyword",
    "cluster",
    "tier",
    "why_promising",
    "missing_evidence",
    "validation_priority",
    "proposed_page_if_promoted",
]

FIELDS_C = [
    "keyword",
    "cluster",
    "tier",
    "disposition",
    "reason",
    "merge_into_cluster_or_page",
]


def load_registry() -> list[dict]:
    with REGISTRY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def overall_label(traffic: str, audience: str, commercial: str) -> str:
    scores = {"high": 3, "medium-high": 2.5, "medium": 2, "low-medium": 1, "low": 0}
    t = scores.get(audience.split()[0] if audience else "medium", 2)
    c = scores.get(commercial.split("-")[0] if commercial else "medium", 2)
    if "UNVERIFIED" in traffic:
        t -= 0.5  # penalize unknown volume in overall label
    avg = (t + c) / 2
    if avg >= 2.5:
        return "strong"
    if avg >= 1.8:
        return "moderate"
    return "weak"


def classify_row(row: dict, cluster_primaries: dict[str, str]) -> tuple[str, str, str]:
    """Returns (list, disposition, reason)."""
    kw = row["keyword"].lower().strip()
    cluster = row.get("cluster", "")
    tier = row.get("tier", "")

    if tier == "EX":
        return "C", "reject", "Homeowner, geo trap, or irrelevant (Phase 1 exclusion)"

    if kw in BRAND_COMPETITOR_PHRASES or COMPETITOR_BRAND_ONLY.match(kw):
        return "C", "combine", "Competitor-brand query — mention in comparison pillar only"

    if NARROW_FEATURE.search(kw):
        return "C", "combine", "Narrow feature/legal micro-topic — prose inside hub, not SEO target"

    if kw in (
        "family owned plumbing website",
        "commercial plumbing website vs residential",
        "master plumber business website",
        "plumbing contractor website",
        "small plumbing company website",
        "plumbing website insurance badge",
        "plumbing website mobile menu",
        "plumbing website ssl certificate",
        "plumbing website privacy policy",
        "plumber website service guarantee wording",
    ):
        return "C", "combine", "Obscure or generic business-type phrase — no standalone target"

    if cluster in QUALIFIED_CLUSTER_IDS:
        primary = cluster_primaries.get(cluster, "")
        if kw == primary or kw.replace(" ", "") == primary.replace(" ", ""):
            return "A", "primary", "Qualified cluster primary"
        return "C", "combine", f"Supporting variant — cover on {cluster} primary page"

    if cluster in PROMISING_UNVERIFIED_CLUSTERS or any(
        kw == v for v in PROMISING_UNVERIFIED_CLUSTERS.values()
    ):
        return "B", "watchlist", "Relevant but insufficient SERP/volume evidence"

    # Tier 3 long tail marketing
    if tier == "3" and cluster in ("TG-02_marketing", "TG-01_leads", "TG-08_software"):
        if "website" not in kw and "google business" not in kw and "gbp" not in kw:
            return "C", "reject", "Tier 3 marketing noise — weak product connection"

    # Generic tier 2 long tails from expansion
    if tier == "2" and cluster == "TR-01_comparisons" and kw not in (
        "best plumber website builder",
        "best website builder for plumbers",
    ):
        if any(x in kw for x in ("yola", "godaddy", "weebly", "duda", "squarespace", "wix plumbing")):
            return "C", "combine", "Platform long-tail — section under comparison pillar"

    if tier == "2" and cluster == "TR-16_competitor_brands":
        return "C", "combine", "Competitor brand — not standalone SEO target"

    if tier == "3":
        return "B", "watchlist", "Tier 3 — needs SERP + volume validation"

    if tier == "2" and row.get("priority", "").startswith("P2"):
        return "B", "watchlist", "Tier 2 secondary — validate demand before dedicated page"

    if tier == "1":
        return "B", "watchlist", "Tier 1 variant not promoted to cluster primary — validate"

    return "C", "combine", "Does not meet strict List A evidence bar"


def main() -> None:
    registry = load_registry()
    cluster_primaries = {c["cluster_id"]: c["primary_keyword"] for c in QUALIFIED_CLUSTERS}

    # Build secondary keywords per qualified cluster from registry
    cluster_variants: dict[str, list[str]] = {cid: [] for cid in QUALIFIED_CLUSTER_IDS}
    for row in registry:
        c = row.get("cluster", "")
        if c in QUALIFIED_CLUSTER_IDS:
            pk = cluster_primaries[c]
            if row["keyword"] == pk and row.get("close_variants"):
                for v in row["close_variants"].split("|"):
                    v = v.strip()
                    if v and v not in cluster_variants[c]:
                        cluster_variants[c].append(v)
            elif row["keyword"] != pk:
                cluster_variants[c].append(row["keyword"])

    list_a: list[dict] = []
    for rank, c in enumerate(QUALIFIED_CLUSTERS, start=1):
        sec = cluster_variants.get(c["cluster_id"], [])[:8]
        list_a.append(
            {
                "list_a_rank": rank,
                "cluster_id": c["cluster_id"],
                "primary_keyword": c["primary_keyword"],
                "secondary_keywords_in_cluster": "|".join(sec),
                "tier": c["tier"],
                "search_intent_summary": {
                    "1": "obtain website / builder",
                    "2": "research compare build improve",
                    "3": "grow online presence",
                }.get(c["tier"], ""),
                "traffic_evidence": c["traffic_evidence"],
                "traffic_potential": c["traffic_potential_note"],
                "audience_intent_fit": c["audience_fit"],
                "commercial_ranking_opportunity": c["commercial_opportunity"],
                "overall_opportunity": overall_label(
                    c["traffic_evidence"], c["audience_fit"], c["commercial_opportunity"]
                ),
                "serp_evidence_summary": c["serp_evidence"],
                "serp_evidence_date": "2026-10-18",
                "competitive_landscape": "Trade builders + comparison content + DIY platforms (see SERP summary)",
                "proposed_page_url": c["page_url"],
                "page_action": c["page_action"],
                "new_url_required": "no"
                if "improve" in c["page_action"]
                else "maybe"
                if "spoke" in c["page_action"]
                else "yes",
                "distinct_page_justified": "yes"
                if c["page_action"] not in ("improve_existing",)
                or c["cluster_id"] in ("TB-06_examples", "TR-01_comparisons", "TR-04_how_to_build")
                else "same_url_as_related_cluster",
                "confidence": "medium-high"
                if "2026-10-18" in c["serp_evidence"] or "PAA" in c["serp_evidence"]
                else "medium",
                "ranking_rationale": f"List A cluster {rank}: audience fit + commercial relevance; SERP observed; volume unverified",
            }
        )

    list_b: list[dict] = []
    list_c: list[dict] = []
    seen_b: set[str] = set()

    for row in registry:
        lst, disp, reason = classify_row(row, cluster_primaries)
        kw = row["keyword"]
        if lst == "B" and kw not in seen_b:
            seen_b.add(kw)
            list_b.append(
                {
                    "keyword": kw,
                    "cluster": row.get("cluster", ""),
                    "tier": row.get("tier", ""),
                    "why_promising": "Owner audience plausible from Phase 1 mapping",
                    "missing_evidence": "US monthly search volume; KD; SERP owner-intent check",
                    "validation_priority": "high"
                    if row.get("tier") == "2"
                    else "medium"
                    if row.get("tier") == "3"
                    else "low",
                    "proposed_page_if_promoted": row.get("primary_intent_owner_url", ""),
                }
            )
        elif lst == "C":
            list_c.append(
                {
                    "keyword": kw,
                    "cluster": row.get("cluster", ""),
                    "tier": row.get("tier", ""),
                    "disposition": disp,
                    "reason": reason,
                    "merge_into_cluster_or_page": cluster_primaries.get(
                        row.get("cluster", ""), "comparison pillar or nearest hub"
                    ),
                }
            )

    # Deduplicate List B: keep unique keywords, sort by tier then keyword
    list_b.sort(key=lambda x: (x["tier"], x["keyword"]))

    with OUT_A.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS_A)
        w.writeheader()
        w.writerows(list_a)

    with OUT_B.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS_B)
        w.writeheader()
        w.writerows(list_b)

    with OUT_C.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS_C)
        w.writeheader()
        w.writerows(list_c)

    print(f"List A clusters: {len(list_a)}")
    print(f"List B keywords: {len(list_b)}")
    print(f"List C keywords: {len(list_c)}")


if __name__ == "__main__":
    main()
