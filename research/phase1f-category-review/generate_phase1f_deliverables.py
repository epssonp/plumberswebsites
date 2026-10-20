"""Generate Phase 1F CSV deliverables. Planning only; does not modify Phase 1C–1E files."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Current titles from Phase 1F brief (not found in repo HTML or prior research files).
# Category 5 previous title noted in brief; descriptions only approved for Cat 5 in brief.
CATEGORIES = [
    {
        "category_number": 1,
        "current_title": "Techniques, Technology & Equipment",
        "current_description": "NOT FOUND IN REPOSITORY — title only supplied in Phase 1F brief (2026-10-18)",
        "recommended_title": "Plumbing Techniques, Tools & Equipment",
        "recommended_description": (
            "Hands-on guidance for plumbing business owners and field teams on proven techniques, "
            "jobsite tools, and equipment choices that affect quality, safety, and efficiency on the job."
        ),
        "decision": "revise",
        "keyword_opportunities": (
            "No List A/B/C owner-intent clusters validated for this pillar in Phase 1C–1D; "
            "consumer DIY repair terms excluded (Phase 1 exclusion report)"
        ),
        "evidence_status": "Research gap — category not covered by Phase 1 keyword audit",
        "evidence_source": "Phase 1C scope; exclusion-report.csv (EX_homeowner_local_service)",
        "volume_band": "",
        "numeric_volume": "",
        "commercial_overlap_risk": "Low — distinct from commercial website pages",
        "description_rationale": (
            "Adds industry specificity ('Plumbing') and separates field tools from digital tools (Category 5). "
            "Reader-focused scope statement without keyword stuffing."
        ),
        "title_rationale": (
            "Shorter, clearer for owners; avoids bare 'Technology' which overlaps Category 5. "
            "No validated head term justifies a more SEO-aggressive title at category level."
        ),
        "validation_needed": "Dedicated keyword discovery for owner-intent technique/equipment topics; SERP intent checks",
        "notes": "Alternative title: keep current if brand prefers ampersand style — preferred revision above.",
    },
    {
        "category_number": 2,
        "current_title": "Training, Licensing & Certifications",
        "current_description": "NOT FOUND IN REPOSITORY — title only supplied in Phase 1F brief (2026-10-18)",
        "recommended_title": "Licensing, Training & Credentials",
        "recommended_description": (
            "Clear explanations of licensing, training, and credential requirements for plumbing "
            "business owners — including compliance basics, continuing education, and what to verify "
            "when hiring licensed plumbers."
        ),
        "decision": "revise",
        "keyword_opportunities": (
            "plumbing business license and website (List B — no Ahrefs band); "
            "plumbing license exam / become a plumber (EX career — not primary audience)"
        ),
        "evidence_status": "Partial — only tangential List B; career queries rejected in Phase 1C",
        "evidence_source": "unverified-keyword-opportunities.csv; exclusion-report.csv",
        "volume_band": "",
        "numeric_volume": "",
        "commercial_overlap_risk": "Low",
        "description_rationale": (
            "Frames content for business owners (compliance, hiring), not job-seeker exam prep. "
            "Distinguishes from Category 6 (industry trends) and Category 3 (daily operations)."
        ),
        "title_rationale": (
            "'Credentials' signals professional standards without duplicating 'Professional Development' in Category 6. "
            "Does not force unvalidated license-exam keywords into the hub title."
        ),
        "validation_needed": "State-level licensing keyword research with owner-intent SERP validation",
        "notes": "Alternative: keep 'Training, Licensing & Certifications' if legal/compliance team prefers formal wording.",
    },
    {
        "category_number": 3,
        "current_title": "Starting & Running a Plumbing Business",
        "current_description": "NOT FOUND IN REPOSITORY — title only supplied in Phase 1F brief (2026-10-18)",
        "recommended_title": "Starting & Running a Plumbing Business",
        "recommended_description": (
            "Practical guidance for starting, structuring, and operating a plumbing company — "
            "from early planning and pricing to hiring, scheduling, and day-to-day business decisions. "
            "Website and marketing topics live in other Academy categories."
        ),
        "decision": "revise",
        "keyword_opportunities": (
            "starting a plumbing business checklist (secondary-shortlist — volume not collected); "
            "start a plumbing business website (List B — no Ahrefs exact row); "
            "best software for plumbing business (List B — defer to subcategory)"
        ),
        "evidence_status": "Topic map only — no Phase 1D volume bands for business-operations seeds",
        "evidence_source": "secondary-shortlist.csv; keyword-opportunity-registry.csv TG-06",
        "volume_band": "",
        "numeric_volume": "",
        "commercial_overlap_risk": "Medium for 'start a plumbing business website' — route to Category 5 articles + homepage, not Cat 3 hub title",
        "description_rationale": (
            "Explicit boundary prevents catch-all overlap with Categories 4 and 5. "
            "Natural mention of scope without a keyword list."
        ),
        "title_rationale": "Current title is clear and standard for owners; no stronger validated phrase warrants change.",
        "validation_needed": "Semrush/GKP seeds for starting/running plumbing business (owner intent)",
        "notes": "",
    },
    {
        "category_number": 4,
        "current_title": "Finding Customers & Growing Locally",
        "current_description": "NOT FOUND IN REPOSITORY — title only supplied in Phase 1F brief (2026-10-18)",
        "recommended_title": "Finding Customers & Growing Locally",
        "recommended_description": (
            "Marketing and visibility strategies for plumbing business owners who want more local "
            "customers — including Google Business Profile, local search basics, reviews, referrals, "
            "and lead generation, with your website as one part of the system."
        ),
        "decision": "revise",
        "keyword_opportunities": (
            "google business profile for plumbers (<100); seo for plumbing business (<100); "
            "how to get more plumbing customers (<100); local seo for plumbing company (no data returned)"
        ),
        "evidence_status": "Ahrefs US bands / no data — Phase 1D 2026-10-18",
        "evidence_source": "phase1d-keyword-volume-audit.csv; qualified-keyword-opportunities.csv TG-03/TG-04/TG-01",
        "volume_band": "Mixed: <100 bands and no-data rows",
        "numeric_volume": "",
        "commercial_overlap_risk": "Medium — avoid targeting 'plumber website builder' or 'plumbing website design' at category level (commercial + Cat 5)",
        "description_rationale": (
            "Uses validated topic language (GBP, local search, leads) at description level where bands exist or List A intent is clear. "
            "Clarifies relationship to website without owning website-build keywords."
        ),
        "title_rationale": "Title already matches owner local-growth intent; no validated alternative beats clarity.",
        "validation_needed": "SERP intent validation for local seo for plumbing company; Semrush numeric volumes",
        "notes": "",
    },
    {
        "category_number": 5,
        "current_title": "Websites, Digital Tools & Online Presence",
        "current_description": (
            "NOT FOUND IN REPOSITORY — previous working title documented in Phase 1F brief. "
            "Agreed replacement description supplied in Phase 1F brief (2026-10-18)."
        ),
        "recommended_title": "Plumbing Websites & Digital Tools",
        "recommended_description": (
            "Practical guides for plumbing business owners on building a plumbing website, choosing "
            "website templates and digital tools, improving their online presence, and helping "
            "potential customers find their business online."
        ),
        "decision": "revise",
        "keyword_opportunities": (
            "plumber website builder (>100 — commercial homepage); plumbing website design (>100 — /features/); "
            "plumbing website template (>100 — #business); plumbing website examples (>100); "
            "how to build a plumbing website (>100); plumbing website cost (<100); plus List A/B comparison and feature terms"
        ),
        "evidence_status": "Strongest evidence in Phase 1C–1D; bands not exact volumes",
        "evidence_source": "phase1d-keyword-volume-audit.csv 2026-10-18; phase1e maps",
        "volume_band": ">100 and <100 bands per Phase 1D",
        "numeric_volume": "",
        "commercial_overlap_risk": "High if hub targets plumber website builder — keep head term on homepage; hub uses 'plumbing website(s)' phrasing",
        "description_rationale": "Approved working direction in Phase 1F brief — retained verbatim.",
        "title_rationale": "Approved working direction in Phase 1F brief — retained verbatim.",
        "validation_needed": "Semrush validation for comparison terms (best plumber website builder — no Ahrefs row)",
        "notes": "Category 5 worked example; do not use category hub to compete with homepage H1.",
    },
    {
        "category_number": 6,
        "current_title": "Industry Intelligence & Professional Development",
        "current_description": "NOT FOUND IN REPOSITORY — title only supplied in Phase 1F brief (2026-10-18)",
        "recommended_title": "Industry Trends & Professional Growth",
        "recommended_description": (
            "Stay current with plumbing industry trends, business best practices, and professional "
            "growth topics that help owners lead stronger companies — separate from licensing exams, "
            "field technique tutorials, and website how-to guides."
        ),
        "decision": "revise",
        "keyword_opportunities": "No dedicated List A clusters; avoid career/exam terms (Phase 1 exclusions)",
        "evidence_status": "Research gap at category level",
        "evidence_source": "Phase 1C scope; exclusion-report.csv EX_career_or_supply",
        "volume_band": "",
        "numeric_volume": "",
        "commercial_overlap_risk": "Low",
        "description_rationale": (
            "Defines boundaries vs Categories 1, 2, and 5 to prevent duplication. "
            "No invented search-demand claims."
        ),
        "title_rationale": (
            "Shorter navigation label; 'Industry Trends' is clearer than 'Intelligence' for owners. "
            "Reduces overlap with Category 2 'Training' wording."
        ),
        "validation_needed": "Optional later: owner-intent research on plumbing industry trends / business leadership",
        "notes": "Alternative: keep current title if editorial voice prefers 'Intelligence & Professional Development'.",
    },
]

# keyword allocation rows: (keyword, cat, level, evidence_status, source, band, reason, overlap, validation)
KEYWORD_ROWS = [
    # Category 5 — website / digital (Phase 1D unless noted)
    ("plumber website builder", 5, "article_or_commercial", "Band only — not exact volume", "phase1d 2026-10-18", ">100", "Head term — homepage owns; Cat 5 hub links to commercial, does not target as primary H1", "High vs homepage", "Semrush numeric volume"),
    ("plumbing website design", 5, "subcategory_or_article", "Band only", "phase1d 2026-10-18", ">100", "Features page primary; Cat 5 description natural fit", "Medium vs /features/", "Semrush"),
    ("plumbing website template", 5, "subcategory_or_article", "Band only", "phase1d 2026-10-18", ">100", "Templates/examples subcategory; #business gallery", "Medium vs #business", "Semrush"),
    ("plumbing website examples", 5, "article", "Band only", "phase1d 2026-10-18", ">100", "AC-02 article owner", "Medium vs #business", "SERP intent for best plumbing websites"),
    ("how to build a plumbing website", 5, "article", "Band only", "phase1d 2026-10-18", ">100", "AC-01 flagship guide", "Low", "Semrush"),
    ("plumbing website cost", 5, "article", "Band only", "phase1d 2026-10-18", "<100", "AC-04 TCO; #pricing owns transactional", "Medium vs #pricing", "Semrush"),
    ("plumbing website features", 5, "article", "Band only", "phase1d 2026-10-18", "<100", "Supports Features page; subcategory on inclusions", "Medium vs /features/", "Semrush"),
    ("best plumber website builder", 5, "article", "No data returned", "phase1d 2026-10-18", "", "AC-03 comparison pillar", "Medium vs homepage", "Validate best website builder for plumbers"),
    ("best website builder for plumbers", 5, "article", "No data returned", "phase1d investigate", "", "Alternate seed for AC-03", "Medium vs homepage", "Semrush required"),
    ("plumber website builder vs wix", 5, "article_section", "No data returned", "phase1d 2026-10-18", "", "H2 in AC-03 initially", "Low", "Semrush"),
    ("ai plumbing website builder", 5, "article_section", "No data returned", "phase1d 2026-10-18", "", "H2 in AC-03", "Low", "Semrush"),
    ("wordpress for plumbing business", 5, "article_section", "No data returned", "phase1d 2026-10-18", "", "H2 in AC-03", "Low", "Semrush"),
    ("what pages should a plumbing website have", 5, "subcategory_or_article", "No data returned", "phase1d 2026-10-18", "", "Features + AC-01 section — not hub title", "Medium vs /features/", "Semrush"),
    ("plumbing website checklist", 5, "article", "No data returned", "phase1d 2026-10-18", "", "AC-08", "Low", "Semrush"),
    ("is a website worth it for plumbers", 5, "article", "No data returned", "phase1d 2026-10-18", "", "AC-09 ROI", "Low", "Semrush"),
    ("plumbing website hosting", 5, "article", "Band only", "phase1d 2026-10-18", "<100", "AC-11 consolidated guide", "Low", "Semrush"),
    ("click to call plumber website", 5, "article", "No data returned", "phase1d 2026-10-18", "", "Future conversion hub (Phase 1C TR-09)", "Low", "Semrush"),
    ("plumbing web design agency", 5, "article", "Band only", "phase1d 2026-10-18", "<100", "Agency alternative content", "Low vs /features/", "SERP owner intent"),
    ("website for plumbers", 5, "description_only", "Band only; ambiguous SERP", "phase1d 2026-10-18", "<100", "Supporting copy only — homepage owner", "High vs homepage", "Intent validation required"),
    ("done for you plumber website", 5, "article", "No data returned", "phase1d 2026-10-18", "", "Process/preview story #design — not hub title", "Medium vs #design", "Semrush"),
    ("preview plumbing website before paying", 5, "article", "No data returned", "phase1d 2026-10-18", "", "#design section owner", "Medium vs #design", "Semrush"),
    ("best plumbing websites", 5, "article", "Band only; ambiguous intent", "phase1d 2026-10-18", ">100", "Secondary on AC-02 after SERP test", "Medium", "SERP intent test"),
    # Category 4 — growth / local
    ("google business profile for plumbers", 4, "subcategory_or_article", "Band only", "phase1d 2026-10-18", "<100", "GBP pillar (Phase 1C TG-03)", "Low vs Cat 5", "Semrush + SERP"),
    ("seo for plumbing business", 4, "subcategory", "Band only", "phase1d 2026-10-18", "<100", "Owner SEO pillar — not homeowner rank tactics", "Medium — SERP noise", "SERP validation"),
    ("how to get more plumbing customers", 4, "subcategory_or_article", "Band only", "phase1d 2026-10-18", "<100", "Broad marketing — website-as-hub angle", "Low", "Semrush"),
    ("local seo for plumbing company", 4, "subcategory", "No data returned", "phase1d 2026-10-18", "", "Reserved for subcategory after SERP check", "Medium", "SERP validation mandatory"),
    ("plumbing business marketing ideas", 4, "subcategory", "Topic map only", "secondary-shortlist.csv", "", "Wave 3 marketing hub", "Low", "Volume unknown"),
    ("plumbing leads online", 4, "article", "Topic map only", "qualified TG-01 cluster", "", "Spoke under leads pillar", "Low", "Semrush"),
    ("google reviews for plumbing business", 4, "article", "Topic map only", "secondary-shortlist.csv", "", "Reviews/reputation subcategory", "Low", "SERP owner intent"),
    # Category 3 — operations / starting
    ("starting a plumbing business checklist", 3, "subcategory_or_article", "Topic map only", "secondary-shortlist.csv", "", "Operations onboarding — exclude website deep-dive", "Medium vs Cat 5 AC-01", "Semrush/GKP"),
    ("start a plumbing business website", 3, "article", "Topic map only", "secondary-shortlist.csv", "", "Cross-link to Cat 5 — digital setup slice only", "High vs Cat 5", "Intent split: business start vs build guide"),
    ("best software for plumbing business", 3, "subcategory", "Topic map only", "secondary-shortlist.csv", "", "Field service software — website integrations in Cat 5", "Low", "Semrush"),
    ("plumbing business online presence", 3, "nowhere_at_category_level", "Topic map only", "secondary-shortlist.csv", "", "Phrase too broad — allocate to Cat 4 description or Cat 5 subcategory, not Cat 3 title", "High vs Cat 4/5", "Defer to subcategory phase"),
    # Category 2 — licensing (weak evidence)
    ("plumbing business license and website", 2, "article", "List B unverified", "unverified-keyword-opportunities.csv", "", "Compliance + digital presence crossover — article not hub", "Medium vs Cat 5", "SERP + volume"),
    # Category 1 & 6 — gaps
    ("how to fix a leaky faucet", 1, "nowhere", "Rejected", "exclusion-report.csv", "", "Homeowner DIY — out of scope", "N/A", "N/A"),
    ("plumbing license exam", 2, "nowhere", "Rejected career intent", "exclusion-report.csv", "", "Job seeker — not owner academy focus", "N/A", "N/A"),
]


def cat_title(num: int) -> str:
    for c in CATEGORIES:
        if c["category_number"] == num:
            return c["recommended_title"]
    return ""


def write_decisions_csv() -> None:
    path = ROOT / "category-title-description-decisions.csv"
    fields = [
        "category_number",
        "current_title",
        "current_description",
        "recommended_title",
        "recommended_description",
        "decision",
        "keyword_opportunities",
        "evidence_status",
        "evidence_source",
        "volume_band",
        "numeric_volume",
        "commercial_overlap_risk",
        "description_rationale",
        "title_rationale",
        "validation_needed",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in CATEGORIES:
            w.writerow({k: row[k] for k in fields})


def write_allocation_csv() -> None:
    path = ROOT / "category-keyword-allocation.csv"
    fields = [
        "keyword",
        "category_number",
        "category_title",
        "recommended_hierarchy_level",
        "evidence_status",
        "source",
        "volume_band",
        "numeric_volume",
        "reason_for_allocation",
        "overlap_risk",
        "validation_needed",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for kw, num, level, ev, src, band, reason, overlap, val in KEYWORD_ROWS:
            w.writerow(
                {
                    "keyword": kw,
                    "category_number": num,
                    "category_title": cat_title(num),
                    "recommended_hierarchy_level": level,
                    "evidence_status": ev,
                    "source": src,
                    "volume_band": band,
                    "numeric_volume": "",
                    "reason_for_allocation": reason,
                    "overlap_risk": overlap,
                    "validation_needed": val,
                }
            )


def main() -> None:
    write_decisions_csv()
    write_allocation_csv()
    print("Wrote Phase 1F CSV deliverables")


if __name__ == "__main__":
    main()
