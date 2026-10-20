"""Generate Phase 1 keyword opportunity registry (research only). No invented volumes/KD."""
import csv
from pathlib import Path

OUT = Path(__file__).parent / "keyword-opportunity-registry.csv"

FIELDS = [
    "keyword",
    "close_variants",
    "cluster",
    "tier",
    "intent_class",
    "audience_fit",
    "buying_strength",
    "us_monthly_volume",
    "global_monthly_volume",
    "keyword_difficulty",
    "cpc_usd",
    "competitor_urls",
    "serp_page_types",
    "existing_plumberswebsites_url",
    "proposed_page_topic",
    "primary_intent_owner_url",
    "secondary_keywords",
    "commercial_relevance",
    "evidence_source",
    "confidence",
    "priority",
    "cannibal_group",
    "notes",
]

rows: list[dict] = []


def add(keyword: str, **kwargs) -> None:
    base = {f: "" for f in FIELDS}
    base["keyword"] = keyword
    base["audience_fit"] = "plumbing_business_owner"
    base["confidence"] = "medium"
    base["evidence_source"] = kwargs.pop(
        "evidence_source", "Topic map; quantitative metrics not collected"
    )
    base.update(kwargs)
    rows.append(base)


# --- Tier 1: direct buying ---
T1 = [
    (
        "plumber website builder",
        dict(
            cluster="TB-01_head_builder",
            tier="1",
            intent_class="commercial_transactional",
            buying_strength="high",
            competitor_urls=(
                "https://getsiimple.com/; https://www.butternut.ai/; "
                "https://growlocal.build/plumber-website-builder; "
                "https://elmsite.com/compare/best-website-builder-for-plumbers"
            ),
            serp_page_types="product_landing; ai_builder; comparison; forum",
            existing_plumberswebsites_url="https://plumberswebsites.com/",
            proposed_page_topic="Homepage — primary commercial landing",
            primary_intent_owner_url="homepage",
            close_variants=(
                "plumbing website builder|website builder for plumbers|"
                "plumber site builder|plumbing site builder"
            ),
            commercial_relevance="critical",
            evidence_source=(
                "Google SERP US qualitative check 2026-10-18; "
                "plumberswebsites.com index.html H1/title"
            ),
            confidence="high",
            priority="P0",
            cannibal_group="CG-01",
            notes="Homepage owns head term; Features/Academy must not compete on H1",
        ),
    ),
    (
        "website for plumbers",
        dict(
            cluster="TB-02_website_for_plumbers",
            tier="1",
            intent_class="commercial",
            buying_strength="high",
            serp_page_types="guide; product; template_gallery",
            proposed_page_topic="Homepage hero/FAQ + optional future /for-plumbers/ if SERP splits",
            primary_intent_owner_url="homepage",
            close_variants="websites for plumbers|plumbing business website|website for plumbing company",
            commercial_relevance="high",
            priority="P1",
            cannibal_group="CG-01",
            evidence_source="Homepage meta description + FAQ copy on plumberswebsites.com",
        ),
    ),
    (
        "plumbing website design",
        dict(
            cluster="TB-03_design_service",
            tier="1",
            intent_class="commercial_investigation",
            buying_strength="medium-high",
            serp_page_types="agency_service; guide; portfolio",
            existing_plumberswebsites_url="https://plumberswebsites.com/features/",
            proposed_page_topic="Features page + design gallery on homepage",
            primary_intent_owner_url="features_page",
            close_variants="plumber website design|web design for plumbers|plumbing web design",
            commercial_relevance="high",
            priority="P1",
            cannibal_group="CG-02",
        ),
    ),
    (
        "plumbing website template",
        dict(
            cluster="TB-05_templates",
            tier="1",
            intent_class="commercial",
            buying_strength="medium",
            competitor_urls="https://www.wix.com/website/templates/refine/plumbing",
            serp_page_types="template_marketplace; diy_builder",
            existing_plumberswebsites_url="https://plumberswebsites.com/#business",
            proposed_page_topic="Six-design gallery + template vs done-for-you explainer",
            primary_intent_owner_url="homepage_design_gallery",
            close_variants="plumber website template|plumbing website templates",
            priority="P1",
            cannibal_group="CG-03",
        ),
    ),
    (
        "plumbing website examples",
        dict(
            cluster="TB-06_examples",
            tier="1",
            intent_class="commercial_investigation",
            buying_strength="medium",
            competitor_urls="https://www.skillmammoth.com/blog/plumber-website-design",
            serp_page_types="listicle; portfolio",
            proposed_page_topic="Examples hub + Proton Plumbing live preview",
            primary_intent_owner_url="academy_examples_hub",
            close_variants="plumber website examples|plumbing website design examples",
            priority="P2",
            cannibal_group="CG-03",
        ),
    ),
    (
        "plumbing website cost",
        dict(
            cluster="TB-07_pricing",
            tier="1",
            intent_class="commercial",
            buying_strength="high",
            competitor_urls="https://www.wix.com/blog/plumbing-website-cost",
            serp_page_types="guide; pricing; paa",
            existing_plumberswebsites_url="https://plumberswebsites.com/#pricing",
            proposed_page_topic="Pricing section + total-cost-of-ownership guide",
            primary_intent_owner_url="homepage_pricing + academy_cost_guide",
            close_variants=(
                "how much does a plumbing website cost|plumber website price|"
                "cost of plumber website|how much does a professional website cost"
            ),
            priority="P1",
            cannibal_group="CG-04",
            evidence_source="Google PAA observed on plumber website builder SERP 2026-10-18",
        ),
    ),
    (
        "done for you plumber website",
        dict(
            cluster="TB-09_dfy",
            tier="1",
            intent_class="commercial_transactional",
            buying_strength="high",
            existing_plumberswebsites_url="https://plumberswebsites.com/features/",
            proposed_page_topic="Homepage + Features foundation narrative",
            primary_intent_owner_url="homepage+features",
            close_variants="plumber website done for you|we build your plumbing website",
            priority="P1",
            cannibal_group="CG-01",
        ),
    ),
    (
        "preview plumbing website before paying",
        dict(
            cluster="TB-10_preview",
            tier="1",
            intent_class="commercial",
            buying_strength="high",
            existing_plumberswebsites_url="https://plumberswebsites.com/#design",
            proposed_page_topic="How It Works + FAQ (differentiator)",
            primary_intent_owner_url="how_it_works_section",
            close_variants="see my plumbing website before I pay|preview plumber website",
            priority="P1",
            cannibal_group="CG-05",
            notes="Unique product angle vs generic AI builders",
        ),
    ),
    (
        "plumber website service",
        dict(
            cluster="TB-11_service",
            tier="1",
            intent_class="commercial",
            buying_strength="medium-high",
            proposed_page_topic="Homepage positioning",
            primary_intent_owner_url="homepage",
            priority="P2",
            cannibal_group="CG-01",
        ),
    ),
    (
        "create plumbing business website",
        dict(
            cluster="TB-04_obtain_website",
            tier="1",
            intent_class="transactional",
            buying_strength="high",
            proposed_page_topic="Homepage CTA journey",
            primary_intent_owner_url="homepage",
            close_variants="get a website for my plumbing business|make a website for my plumbing company",
            priority="P1",
            cannibal_group="CG-01",
        ),
    ),
]

for kw, extra in T1:
    add(kw, **extra)

# --- Tier 2: research / comparison ---
T2_HEAD = [
    (
        "best plumber website builder",
        dict(
            cluster="TR-01_comparisons",
            tier="2",
            intent_class="commercial_investigation",
            buying_strength="high",
            competitor_urls=(
                "https://www.zarla.com/guides/best-website-builder-for-plumbers; "
                "https://elmsite.com/compare/best-website-builder-for-plumbers; "
                "https://www.flashcrafter.ai/compare/best-website-builders-for-plumbers; "
                "https://websitebuilderreport.com/business/best-website-builder-for-plumbers/"
            ),
            serp_page_types="comparison_article; affiliate; product",
            proposed_page_topic="Honest comparison hub (DIY vs trade-specific vs done-for-you)",
            primary_intent_owner_url="academy_comparison_pillar",
            close_variants="best website builder for plumbers|top plumber website builders",
            commercial_relevance="high",
            priority="P1",
            cannibal_group="CG-06",
            evidence_source="Web search competitor URLs verified 2026-10-18",
            confidence="high",
        ),
    ),
    (
        "how to build a plumbing website",
        dict(
            cluster="TR-04_how_to_build",
            tier="2",
            intent_class="informational_commercial",
            buying_strength="medium",
            competitor_urls=(
                "https://www.wix.com/blog/how-to-make-a-plumbing-website; "
                "https://gasengineersoftware.co.uk/blog/how-to-build-a-plumber-website-that-gets-you-jobs/"
            ),
            serp_page_types="step_by_step_guide",
            proposed_page_topic="Flagship Academy guide with product as one path",
            primary_intent_owner_url="academy_how_to_build",
            close_variants="how to make a plumbing website|how to create a plumbing business website",
            priority="P1",
            cannibal_group="CG-08",
        ),
    ),
    (
        "what pages should a plumbing website have",
        dict(
            cluster="TR-06_site_structure",
            tier="2",
            intent_class="informational_commercial",
            buying_strength="medium-high",
            existing_plumberswebsites_url="https://plumberswebsites.com/features/",
            proposed_page_topic="Five-page breakdown (Features) + expanded Academy",
            primary_intent_owner_url="features_five_pages",
            priority="P1",
            cannibal_group="CG-09",
        ),
    ),
    (
        "plumber website builder vs wix",
        dict(
            cluster="TR-02_vs_wix",
            tier="2",
            intent_class="commercial_investigation",
            buying_strength="medium-high",
            proposed_page_topic="Wix vs PlumbersWebsites (time, preview, trade focus)",
            primary_intent_owner_url="academy_comparison_wix",
            priority="P2",
            cannibal_group="CG-06",
        ),
    ),
    (
        "plumber website builder vs squarespace",
        dict(
            cluster="TR-02_vs_squarespace",
            tier="2",
            intent_class="commercial_investigation",
            buying_strength="medium",
            proposed_page_topic="Squarespace comparison",
            primary_intent_owner_url="academy_comparison_squarespace",
            priority="P3",
            cannibal_group="CG-06",
        ),
    ),
    (
        "wordpress for plumbing business",
        dict(
            cluster="TR-03_wordpress",
            tier="2",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="WordPress vs managed plumber builder",
            primary_intent_owner_url="academy_wordpress",
            priority="P2",
            cannibal_group="CG-07",
        ),
    ),
    (
        "ai plumbing website builder",
        dict(
            cluster="TR-14_ai_builders",
            tier="2",
            intent_class="commercial",
            buying_strength="medium-high",
            competitor_urls=(
                "https://replit.com/; https://meku.dev/; https://durable.com/; "
                "https://www.butternut.ai/"
            ),
            serp_page_types="ai_product_landing",
            proposed_page_topic="Generic AI vs personalized five-page preview story",
            primary_intent_owner_url="academy_ai_builders",
            priority="P2",
            cannibal_group="CG-06",
            evidence_source="Google SERP US qualitative check 2026-10-18",
        ),
    ),
    (
        "plumbing website checklist",
        dict(
            cluster="TR-05_checklist",
            tier="2",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="Checklist mapped to product deliverables",
            primary_intent_owner_url="academy_checklist",
            priority="P2",
            cannibal_group="CG-08",
        ),
    ),
    (
        "plumbing website features",
        dict(
            cluster="TR-07_features",
            tier="2",
            intent_class="commercial_investigation",
            buying_strength="medium-high",
            existing_plumberswebsites_url="https://plumberswebsites.com/features/",
            proposed_page_topic="Features page (existing)",
            primary_intent_owner_url="features_page",
            priority="P1",
            cannibal_group="CG-02",
        ),
    ),
    (
        "is a website worth it for plumbers",
        dict(
            cluster="TR-04_how_to_build",
            tier="2",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="ROI / when to invest guide",
            primary_intent_owner_url="academy_worth_it",
            priority="P2",
            cannibal_group="CG-08",
        ),
    ),
]

for kw, extra in T2_HEAD:
    add(kw, **extra)

# Long-tail Tier 2 expansion (distinct intents grouped by cluster)
T2_LONG = {
    "TR-09_conversion_elements": [
        "click to call plumber website",
        "plumbing website contact form",
        "plumbing website quote form",
        "plumbing website conversion rate",
        "best call to action for plumber website",
        "plumbing website phone number placement",
        "add online booking plumbing website",
        "plumbing website lead capture",
    ],
    "TR-08_mobile": [
        "mobile friendly plumber website",
        "plumber website speed",
        "plumbing website accessibility",
        "plumbing website mobile menu",
    ],
    "TR-10_hosting": [
        "plumbing website hosting",
        "plumbing website domain",
        "plumbing website subdomain",
        "where is my plumbing website hosted",
    ],
    "TR-11_maintenance": [
        "plumbing website maintenance",
        "update plumbing website business hours",
        "plumbing website privacy policy",
        "plumbing website terms of service",
    ],
    "TR-12_improve": [
        "redesign plumbing website",
        "improve plumbing website",
        "plumbing website before and after",
        "outdated plumber website",
    ],
    "TR-03_agency_alt": [
        "plumbing web design agency",
        "hire web designer for plumbing business",
        "plumbing website design company",
        "alternatives to plumbing web design agency",
    ],
    "TR-06_site_structure": [
        "one page plumber website",
        "five page plumber website",
        "plumbing website sitemap",
        "service area pages for plumbers",
        "plumbing service area pages seo",
        "plumbing website about page",
        "plumbing website services page",
    ],
    "TR-13_examples": [
        "plumber website design examples 2026",
        "best plumbing websites",
        "plumbing company website inspiration",
    ],
    "TR-15_crm_bundled": [
        "jobber website for plumbers",
        "housecall pro website",
        "service titan website for plumbers",
        "crm website vs custom plumbing website",
    ],
    "TR-16_competitor_brands": [
        "grow local plumber website",
        "siimple plumber website",
        "elmsite plumber website",
        "zarla plumber website",
        "instantsite plumber website",
        "butternut plumber website",
    ],
    "TB-07_pricing": [
        "cheap plumbing website",
        "plumbing website packages",
        "plumbing website pricing",
        "affordable plumber website",
    ],
    "TB-08_free_trial": [
        "free plumbing website",
        "free plumber website builder",
        "try plumbing website free",
    ],
}

for cluster, kws in T2_LONG.items():
    tier = "1" if cluster.startswith("TB") else "2"
    for kw in kws:
        add(
            kw,
            cluster=cluster,
            tier=tier,
            intent_class="informational_commercial",
            buying_strength="medium",
            priority="P2-P3",
            evidence_source="Competitor/topic expansion; validate intent via SERP before publish",
        )

# --- Tier 3: business growth (owner) ---
T3 = [
    (
        "google business profile for plumbers",
        dict(
            cluster="TG-03_gbp",
            tier="3",
            intent_class="informational_commercial",
            buying_strength="low-medium",
            proposed_page_topic="GBP setup for plumbing companies (owner)",
            primary_intent_owner_url="academy_gbp",
            close_variants="google my business for plumbers|gbp for plumbing company",
            priority="P1",
            cannibal_group="CG-14",
            notes="Not 'plumber near me' — owner-operated profile optimization",
        ),
    ),
    (
        "local seo for plumbing company",
        dict(
            cluster="TG-04_seo_owner",
            tier="3",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="Local SEO pillar (website + GBP + reviews)",
            primary_intent_owner_url="academy_local_seo",
            priority="P1",
            cannibal_group="CG-15",
        ),
    ),
    (
        "plumber seo",
        dict(
            cluster="TG-04_seo_owner",
            tier="3",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="SEO for plumbing businesses — disambiguate from homeowner SEO spam",
            primary_intent_owner_url="academy_seo_pillar",
            priority="P1",
            cannibal_group="CG-15",
            notes="Many SERP results target ranking FOR plumbers (homeowner queries); filter content",
        ),
    ),
    (
        "how to get more plumbing customers",
        dict(
            cluster="TG-01_leads",
            tier="3",
            intent_class="informational_commercial",
            buying_strength="low-medium",
            proposed_page_topic="Lead gen pillar — owned website as hub",
            primary_intent_owner_url="academy_leads",
            priority="P1",
            cannibal_group="CG-13",
        ),
    ),
    (
        "plumbing business marketing ideas",
        dict(
            cluster="TG-02_marketing",
            tier="3",
            intent_class="informational",
            buying_strength="low",
            proposed_page_topic="Marketing ideas hub",
            primary_intent_owner_url="academy_marketing",
            priority="P2",
            cannibal_group="CG-13",
        ),
    ),
    (
        "plumbing leads online",
        dict(
            cluster="TG-01_leads",
            tier="3",
            intent_class="commercial_investigation",
            buying_strength="medium",
            proposed_page_topic="Lead marketplaces vs owned website",
            primary_intent_owner_url="academy_online_leads",
            priority="P2",
            cannibal_group="CG-13",
        ),
    ),
    (
        "start a plumbing business website",
        dict(
            cluster="TG-06_new_business",
            tier="3",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="New business digital checklist",
            primary_intent_owner_url="academy_new_business",
            priority="P2",
            cannibal_group="CG-17",
        ),
    ),
    (
        "plumbing business online presence",
        dict(
            cluster="TG-06_new_business",
            tier="3",
            intent_class="informational_commercial",
            buying_strength="medium",
            proposed_page_topic="Online presence overview",
            primary_intent_owner_url="academy_online_presence",
            priority="P2",
            cannibal_group="CG-17",
        ),
    ),
    (
        "reviews on plumbing website",
        dict(
            cluster="TG-07_trust",
            tier="3",
            intent_class="informational",
            buying_strength="low",
            proposed_page_topic="Testimonials policy — align with FAQ (no fabricated reviews)",
            primary_intent_owner_url="academy_reviews",
            priority="P3",
            cannibal_group="CG-16",
        ),
    ),
    (
        "plumbing company branding",
        dict(
            cluster="TG-05_brand",
            tier="3",
            intent_class="informational",
            buying_strength="low",
            proposed_page_topic="Trust signals on site (license, photos)",
            primary_intent_owner_url="academy_branding",
            priority="P3",
            cannibal_group="CG-16",
        ),
    ),
]

for kw, extra in T3:
    add(kw, **extra)

T3_LONG = {
    "TG-04_seo_owner": [
        "plumbing website schema markup",
        "seo for plumbing website",
        "plumbing website meta title",
        "plumbing website keywords",
        "how to rank plumbing business on google",
        "plumbing website blog for seo",
        "service page seo for plumbers",
    ],
    "TG-03_gbp": [
        "google business profile categories for plumber",
        "add website to google business profile plumbing",
        "google reviews for plumbing business",
        "gbp photos for plumbing company",
    ],
    "TG-01_leads": [
        "plumbing website roi",
        "get more plumbing calls from website",
        "plumbing company lead generation",
        "plumbing marketing for small business",
    ],
    "TG-02_marketing": [
        "plumbing business social media marketing",
        "plumbing company facebook page",
        "plumbing business google ads",
        "plumbing email marketing",
    ],
    "TG-06_new_business": [
        "starting a plumbing business checklist",
        "plumbing business license and website",
        "first website for new plumbing company",
    ],
    "TG-08_software": [
        "best software for plumbing business",
        "plumbing business invoicing software",
        "plumbing dispatch software",
        "field service software for plumbers website integration",
    ],
}

for cluster, kws in T3_LONG.items():
    for kw in kws:
        add(
            kw,
            cluster=cluster,
            tier="3",
            intent_class="informational_commercial",
            buying_strength="low-medium",
            priority="P2-P3",
            evidence_source="Topic expansion; confirm owner intent in SERP",
        )

# --- Exclusions (documented, not targets) ---
EX_HOMEOWNER = [
    "emergency plumber",
    "plumber near me",
    "plumber tampa",
    "best plumber in clearwater",
    "24 hour plumber near me",
    "drain cleaning near me",
    "water heater repair near me",
    "cheap plumber",
    "licensed plumber near me",
    "plumber cost per hour",
    "how to fix a leaky faucet",
    "unclog drain diy",
]

# Tier 3 marketing long-tail (owner-only phrasing)
MKT_LONG = [
    "how to advertise plumbing business online",
    "plumbing business website and google ads",
    "plumbing company reputation management",
    "get more 5 star reviews plumbing business",
    "plumbing business referral program",
    "plumbing website vs facebook page",
    "nextdoor for plumbing business",
    "plumbing business yard signs and website",
    "plumbing truck wrap website url",
    "plumbing business card website qr code",
    "track phone calls from plumbing website",
    "plumbing website analytics google",
    "plumbing website google tag manager",
    "plumbing website live chat",
    "plumbing website chatbot",
    "plumbing website financing banner",
    "plumbing website license number display",
    "plumbing website insurance badge",
    "plumbing website emergency hours",
    "plumbing website service guarantee wording",
    "commercial plumbing website vs residential",
    "plumbing contractor website",
    "master plumber business website",
    "small plumbing company website",
    "family owned plumbing website",
    "plumbing franchise website requirements",
]
for kw in MKT_LONG:
    add(
        kw,
        cluster="TG-02_marketing" if "review" in kw or "advertise" in kw or "facebook" in kw else "TG-01_leads",
        tier="3",
        intent_class="informational_commercial",
        buying_strength="low-medium",
        priority="P2-P3",
        evidence_source="Business-growth topic expansion; exclude if SERP is homeowner/agency lead-gen",
    )

for kw in EX_HOMEOWNER:
    add(
        kw,
        cluster="EX_homeowner_local_service",
        tier="EX",
        intent_class="local_service_homeowner",
        audience_fit="homeowner",
        buying_strength="none",
        commercial_relevance="none",
        priority="exclude",
        evidence_source=(
            "Audience rules Phase 1; typical trade-SEO keyword lists (e.g. plumberseo.net) "
            "are homeowner-intent"
        ),
        confidence="high",
        notes="Out of scope — hiring a plumber for a job",
    )

EX_GEO_TRAP = [
    "plumber website design tampa",
    "plumbing marketing dallas",
    "seo for plumbers chicago",
]

for kw in EX_GEO_TRAP:
    add(
        kw,
        cluster="EX_geo_without_owner_intent",
        tier="EX",
        intent_class="ambiguous_geo",
        audience_fit="mixed_or_homeowner",
        buying_strength="none",
        commercial_relevance="low",
        priority="exclude",
        notes=(
            "Geo modifiers often signal local service or agency lead-gen; "
            "only revisit if SERP shows owner-education content"
        ),
    )

# Supporting questions / PAA-style (Tier 2–3) — one row each; same page owner via cluster
PAA_STYLE = [
    ("how long does it take to build a plumbing website", "TR-04_how_to_build", "2"),
    ("do plumbers need a website", "TR-04_how_to_build", "2"),
    ("what is the best platform for a plumbing website", "TR-01_comparisons", "2"),
    ("how many pages does a plumbing website need", "TR-06_site_structure", "2"),
    ("should plumbers use wix", "TR-02_vs_wix", "2"),
    ("how to add services to plumbing website", "TR-06_site_structure", "2"),
    ("how to show service area on plumbing website", "TR-06_site_structure", "2"),
    ("how to put phone number on plumbing website", "TR-09_conversion_elements", "2"),
    ("how to get plumbing website on google", "TG-04_seo_owner", "3"),
    ("how to link website to google business profile", "TG-03_gbp", "3"),
    ("what to write on plumbing about page", "TR-06_site_structure", "2"),
    ("plumbing website hero section ideas", "TR-13_examples", "2"),
    ("emergency plumbing banner website", "TR-09_conversion_elements", "2"),
    ("plumbing website color scheme", "TR-13_examples", "2"),
    ("plumbing website logo", "TG-05_brand", "3"),
    ("plumbing website stock photos vs real photos", "TG-05_brand", "3"),
    ("how often update plumbing website", "TR-11_maintenance", "2"),
    ("plumbing website ssl certificate", "TR-10_hosting", "2"),
    ("plumbing website backup", "TR-11_maintenance", "2"),
    ("migrate old plumbing website", "TR-12_improve", "2"),
]

for kw, cluster, tier in PAA_STYLE:
    add(
        kw,
        cluster=cluster,
        tier=tier,
        intent_class="informational_commercial",
        buying_strength="medium",
        priority="P2-P3",
        evidence_source="Question phrasing from guides/PAA themes; SERP validation required",
    )

# Additional comparison / competitor long-tail (Tier 2)
COMP_LONG = [
    "wix plumbing website template review",
    "squarespace for plumbers review",
    "durable ai website for plumbers",
    "godaddy website for plumbing business",
    "yola plumber website",
    "duda website for plumbers",
    "website builder for plumbing and hvac",
    "trade website builder vs wix",
    "one page website vs multi page plumber",
]
for kw in COMP_LONG:
    add(
        kw,
        cluster="TR-01_comparisons",
        tier="2",
        intent_class="commercial_investigation",
        buying_strength="medium",
        priority="P2-P3",
        competitor_urls="https://www.flashcrafter.ai/compare/best-website-builders-for-plumbers",
        evidence_source="Comparison SERP landscape 2026-10-18",
    )

# Product-adjacent navigational (Tier 1–2)
BRAND = [
    (
        "plumberswebsites.com",
        dict(
            cluster="TB-12_brand",
            tier="1",
            intent_class="navigational",
            buying_strength="high",
            existing_plumberswebsites_url="https://plumberswebsites.com/",
            primary_intent_owner_url="homepage",
            priority="P0",
            commercial_relevance="critical",
        ),
    ),
    (
        "plumbers websites preview",
        dict(
            cluster="TB-10_preview",
            tier="1",
            intent_class="commercial",
            buying_strength="high",
            primary_intent_owner_url="how_it_works_section",
            priority="P1",
        ),
    ),
]
for item in BRAND:
    if isinstance(item, tuple):
        add(item[0], **item[1])
    else:
        add(item)

# Sample page deep links (existing site — not separate SEO targets)
for kw, url in [
    ("plumbing website five pages included", "https://plumberswebsites.com/features/"),
    ("plumbing website mobile friendly included", "https://plumberswebsites.com/features/#features-mobile"),
    ("proton plumbing website example", "https://protonplumbing.plumberswebsites.com/"),
]:
    add(
        kw,
        cluster="TR-07_features",
        tier="2",
        intent_class="commercial_investigation",
        buying_strength="medium",
        existing_plumberswebsites_url=url,
        primary_intent_owner_url="features_page",
        priority="P2",
        notes="Support branded/demo queries; not necessarily standalone Academy URL",
    )

EX_IRRELEVANT = [
    "plumber salary",
    "plumber apprenticeship",
    "plumbing license exam",
    "become a plumber",
    "plumbing supply store near me",
]

for kw in EX_IRRELEVANT:
    add(
        kw,
        cluster="EX_career_or_supply",
        tier="EX",
        intent_class="career_or_retail",
        audience_fit="job_seeker_or_homeowner",
        buying_strength="none",
        commercial_relevance="none",
        priority="exclude",
        notes="Weak product connection unless reframed as business owner hiring/training",
    )

# Write CSV
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

# Derived shortlists
base = Path(__file__).parent

def write_filter(name: str, pred) -> None:
    path = base / name
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            if pred(r):
                w.writerow(r)


write_filter(
    "commercial-shortlist.csv",
    lambda r: r["tier"] in ("1", "2")
    and r["priority"] in ("P0", "P1", "P2")
    and r["buying_strength"] in ("high", "medium-high", "medium"),
)
write_filter(
    "secondary-shortlist.csv",
    lambda r: r["tier"] == "3" and r["priority"] != "exclude",
)
write_filter("exclusion-report.csv", lambda r: r["tier"] == "EX")

print(f"Wrote {len(rows)} rows to {OUT}")
