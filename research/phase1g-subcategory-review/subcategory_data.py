"""Phase 1G subcategory definitions — planning data only."""

from __future__ import annotations

# Approved parent categories (Phase 1F / Phase 1G brief — do not alter).
PARENT_CATEGORIES = {
    1: {
        "title": "Plumbing Techniques, Tools & Equipment",
        "description": (
            "Hands-on guidance for plumbing business owners and field teams on proven techniques, "
            "jobsite tools, and equipment choices that affect quality, safety, and efficiency on the job."
        ),
        "target_subcategories": 5,
        "target_articles": 30,
    },
    2: {
        "title": "Licensing, Training & Credentials",
        "description": (
            "Clear explanations of licensing, training, and credential requirements for plumbing "
            "business owners — including compliance basics, continuing education, and what to verify "
            "when hiring licensed plumbers."
        ),
        "target_subcategories": 4,
        "target_articles": 35,
    },
    3: {
        "title": "Starting & Running a Plumbing Business",
        "description": (
            "Practical guidance for starting, structuring, and operating a plumbing company — from "
            "early planning and pricing to hiring, scheduling, and day-to-day business decisions. "
            "Website and marketing topics live in other Academy categories."
        ),
        "target_subcategories": 4,
        "target_articles": 55,
    },
    4: {
        "title": "Finding Customers & Growing Locally",
        "description": (
            "Marketing and visibility strategies for plumbing business owners who want more local "
            "customers — including Google Business Profile, local search basics, reviews, referrals, "
            "and lead generation, with your website as one part of the system."
        ),
        "target_subcategories": 4,
        "target_articles": 60,
    },
    5: {
        "title": "Plumbing Websites & Digital Tools",
        "description": (
            "Practical guides for plumbing business owners on building a plumbing website, choosing "
            "website templates and digital tools, improving their online presence, and helping "
            "potential customers find their business online."
        ),
        "target_subcategories": 4,
        "target_articles": 75,
    },
    6: {
        "title": "Industry Trends & Professional Growth",
        "description": (
            "Stay current with plumbing industry trends, business best practices, and professional "
            "growth topics that help owners lead stronger companies — separate from licensing exams, "
            "field technique tutorials, and website how-to guides."
        ),
        "target_subcategories": 3,
        "target_articles": 45,
    },
}

SUBCATEGORIES: list[dict] = [
    {
        "subcategory_id": "SC01",
        "parent_category_id": 1,
        "subcategory_title": "Jobsite Tools & Hand Equipment",
        "subcategory_description": (
            "Choose, use, and maintain the hand tools and everyday jobsite equipment your crews rely "
            "on — with practical guidance on durability, organization, and safe use on residential and "
            "commercial plumbing work."
        ),
        "included_topics": "Hand tools; tool bags and storage; basic jobsite setup; tool quality for owners",
        "scope_boundaries": (
            "In: hand tools and portable jobsite equipment. Out: power/specialty tools (SC02), "
            "diagnostics (SC03), business software (SC23), website tools (Cat 5)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — owner/lead tech equipment guidance",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F research gap; Phase 1C scope",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "low",
        "overlap_with_subcategory_ids": "SC02",
        "commercial_destination": "",
        "planned_article_count": 6,
        "priority": "P3",
        "validation_needed": "Owner-intent keyword discovery; exclude homeowner DIY repair SERPs",
        "status": "proposed",
        "notes": "No Phase 1D volume data for technique/equipment pillar.",
    },
    {
        "subcategory_id": "SC02",
        "parent_category_id": 1,
        "subcategory_title": "Power Tools, Specialty Equipment & Vehicles",
        "subcategory_description": (
            "Evaluate power tools, specialty plumbing equipment, and vehicle or van setups that affect "
            "productivity — including when upgraded equipment pays off for a growing plumbing business."
        ),
        "included_topics": "Power tools; drain machines; torches; van stock and vehicle equipment",
        "scope_boundaries": (
            "In: powered and specialty field equipment. Out: diagnostic cameras as a topic hub (SC03), "
            "industry product trends without how-to (SC22)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — equipment purchase and operations",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F research gap",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "low",
        "overlap_with_subcategory_ids": "SC01;SC05",
        "commercial_destination": "",
        "planned_article_count": 6,
        "priority": "P3",
        "validation_needed": "Keyword discovery with owner-intent SERP checks",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC03",
        "parent_category_id": 1,
        "subcategory_title": "Diagnostics, Inspection & Troubleshooting",
        "subcategory_description": (
            "Systematic approaches to finding problems, inspecting work, and troubleshooting common "
            "plumbing failures — written for owners and senior techs who train crews and review job quality."
        ),
        "included_topics": "Leak detection workflows; inspection checklists; troubleshooting decision trees",
        "scope_boundaries": (
            "In: diagnostic process and field troubleshooting for businesses. Out: consumer DIY fixes "
            "(Phase 1 exclusions); pure marketing content (Cat 4)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — technical troubleshooting",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1 exclusion-report (DIY out of scope)",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC04;SC05",
        "commercial_destination": "",
        "planned_article_count": 6,
        "priority": "P3",
        "validation_needed": "SERP intent — owner/education vs homeowner DIY",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC04",
        "parent_category_id": 1,
        "subcategory_title": "Field Techniques & Installation Methods",
        "subcategory_description": (
            "Proven installation and repair techniques your team can standardize on — focused on quality, "
            "code-aware workmanship, and consistent results across jobs."
        ),
        "included_topics": "Installation best practices; crew standards; quality control on site",
        "scope_boundaries": (
            "In: field technique and workmanship standards. Out: licensing/code interpretation hub (SC09), "
            "industry trend pieces (SC22)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — field craft",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F Cat 1 gap",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC03;SC09",
        "commercial_destination": "",
        "planned_article_count": 6,
        "priority": "P3",
        "validation_needed": "Keyword discovery; avoid homeowner repair queries",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC05",
        "parent_category_id": 1,
        "subcategory_title": "Field Technology & Jobsite Innovations",
        "subcategory_description": (
            "How newer field technologies — such as inspection cameras, locators, and digital job aids — "
            "fit into a plumbing company's workflow, without covering office business software or websites."
        ),
        "included_topics": "Inspection cameras; locators; digital tickets on site; tool tech adoption",
        "scope_boundaries": (
            "In: technology used on the jobsite by techs. Out: CRM/dispatch software (SC13/SC23), "
            "website/digital marketing (Cat 4–5), industry macro trends (SC22)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — field tech adoption",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1G boundary review Cat 1 vs 6",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC23;SC22",
        "commercial_destination": "",
        "planned_article_count": 6,
        "priority": "P3",
        "validation_needed": "Differentiate field vs business technology in SERP samples",
        "status": "proposed",
        "notes": "Split from initial 'plumbing technology' idea to reduce Cat 6 overlap.",
    },
    {
        "subcategory_id": "SC06",
        "parent_category_id": 2,
        "subcategory_title": "Apprenticeships & Building Your Team's Skills",
        "subcategory_description": (
            "Understand apprenticeship pathways, training expectations, and how plumbing business owners "
            "hire and develop entry-level talent — not exam-prep content for individuals entering the trade alone."
        ),
        "included_topics": "Apprentice hiring; training plans; mentoring; workforce pipeline",
        "scope_boundaries": (
            "In: owner perspective on apprenticeships and team skill-building. Out: job-seeker 'become a "
            "plumber' content (excluded); formal licensing rules (SC07)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — hiring and workforce development",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "exclusion-report.csv EX_career_or_supply",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC09;SC24",
        "commercial_destination": "",
        "planned_article_count": 9,
        "priority": "P3",
        "validation_needed": "SERP check — owner vs job seeker intent",
        "status": "proposed",
        "notes": "Avoid plumbing license exam primary targeting.",
    },
    {
        "subcategory_id": "SC07",
        "parent_category_id": 2,
        "subcategory_title": "Plumbing Licensing & State Requirements",
        "subcategory_description": (
            "Navigate licensing obligations for plumbing businesses — what owners must maintain, how "
            "requirements vary by state, and how to stay compliant as you hire and expand."
        ),
        "included_topics": "Contractor licensing; state boards; business license vs trade license; compliance calendars",
        "scope_boundaries": (
            "In: regulatory requirements for businesses. Out: exam study guides for applicants (excluded); "
            "general business formation (SC10). Legal facts require authoritative sources when published."
        ),
        "primary_keyword": "",
        "secondary_keywords": "plumbing business license and website",
        "search_intent": "informational — compliance",
        "evidence_status": "unverified_candidate",
        "evidence_source": "unverified-keyword-opportunities.csv",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC10;SC08",
        "commercial_destination": "",
        "planned_article_count": 9,
        "priority": "P2",
        "validation_needed": "State-level keyword research; legal review for accuracy",
        "status": "proposed",
        "notes": "plumbing business license and website → article cross-link to Cat 5, not hub primary.",
    },
    {
        "subcategory_id": "SC08",
        "parent_category_id": 2,
        "subcategory_title": "Certifications & Professional Credentials",
        "subcategory_description": (
            "Learn which certifications and credentials matter for plumbing businesses and customers — "
            "including specialty qualifications owners should verify when bidding specialized work."
        ),
        "included_topics": "Backflow certification; medical gas; manufacturer certs; displaying credentials",
        "scope_boundaries": "In: professional credentials for businesses and techs. Out: generic leadership (SC24); field technique (SC04).",
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — credentials",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F Cat 2 gap",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "low",
        "overlap_with_subcategory_ids": "SC07;SC09",
        "commercial_destination": "",
        "planned_article_count": 9,
        "priority": "P3",
        "validation_needed": "Keyword discovery",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC09",
        "parent_category_id": 2,
        "subcategory_title": "Continuing Education & Code Awareness",
        "subcategory_description": (
            "Stay current with code changes, continuing education requirements, and training programs "
            "relevant to licensed plumbing businesses — with clear owner responsibilities for team compliance."
        ),
        "included_topics": "CEU requirements; code update summaries; training documentation",
        "scope_boundaries": (
            "In: ongoing education and code awareness for businesses. Out: exam prep (excluded); "
            "industry trend commentary (SC22)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — compliance and education",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F Cat 2 scope",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC06;SC24",
        "commercial_destination": "",
        "planned_article_count": 8,
        "priority": "P3",
        "validation_needed": "Authoritative code sources; state-specific research",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC10",
        "parent_category_id": 3,
        "subcategory_title": "Starting a Plumbing Business",
        "subcategory_description": (
            "Plan and launch a plumbing company with realistic steps — entity setup, insurance basics, "
            "service positioning, and early operational decisions before you scale marketing or web presence."
        ),
        "included_topics": "Business plans; legal structure; insurance; first hires; startup checklists",
        "scope_boundaries": (
            "In: business formation and launch. Out: detailed marketing (Cat 4); website build deep-dives (SC18); "
            "licensing detail (SC07)."
        ),
        "primary_keyword": "starting a plumbing business checklist",
        "secondary_keywords": "start a plumbing business website",
        "search_intent": "informational — business startup",
        "evidence_status": "unverified_candidate",
        "evidence_source": "secondary-shortlist.csv; keyword-opportunity-registry TG-06",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC07;SC18",
        "commercial_destination": "",
        "planned_article_count": 14,
        "priority": "P2",
        "validation_needed": "Semrush/GKP for startup seeds; route website article to SC18",
        "status": "proposed",
        "notes": "start a plumbing business website → article in SC18 with link from SC10, not primary here.",
    },
    {
        "subcategory_id": "SC11",
        "parent_category_id": 3,
        "subcategory_title": "Pricing, Estimating & Business Finances",
        "subcategory_description": (
            "Price plumbing work profitably, estimate jobs accurately, and manage the financial basics "
            "owners need — separate from website package pricing or digital advertising budgets."
        ),
        "included_topics": "Flat-rate vs T&M; margins; cash flow; estimating workflows",
        "scope_boundaries": "In: trade pricing and company finances. Out: plumbing website cost (SC20); ad spend tactics (SC17).",
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — financial operations",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1 keyword registry Tier 3 adjacent",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC20;SC17",
        "commercial_destination": "",
        "planned_article_count": 14,
        "priority": "P2",
        "validation_needed": "Keyword discovery for owner finance topics",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC12",
        "parent_category_id": 3,
        "subcategory_title": "Operations, Scheduling & Customer Service",
        "subcategory_description": (
            "Run day-to-day operations smoothly — scheduling, dispatch, job documentation, and customer "
            "communication that keeps repeat business strong without duplicating marketing playbooks."
        ),
        "included_topics": "Dispatch; SLA for callbacks; job notes; service agreements",
        "scope_boundaries": "In: internal operations and service delivery. Out: lead generation (SC17); field techniques (Cat 1).",
        "primary_keyword": "",
        "secondary_keywords": "best software for plumbing business",
        "search_intent": "informational — operations",
        "evidence_status": "unverified_candidate",
        "evidence_source": "secondary-shortlist.csv TG-08",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "low",
        "overlap_with_subcategory_ids": "SC13;SC23",
        "commercial_destination": "",
        "planned_article_count": 14,
        "priority": "P2",
        "validation_needed": "Software keywords — owner intent vs product nav",
        "status": "proposed",
        "notes": "Field service software articles here; website integrations in SC21.",
    },
    {
        "subcategory_id": "SC13",
        "parent_category_id": 3,
        "subcategory_title": "Hiring, Management & Scaling",
        "subcategory_description": (
            "Grow from owner-operator to managed team — hiring plumbers, setting roles, performance "
            "expectations, and scaling without losing quality or compliance."
        ),
        "included_topics": "Hiring licensed plumbers; team structure; delegation; growth milestones",
        "scope_boundaries": "In: people management and scale. Out: apprentice pathways detail (SC06); leadership mindset (SC24).",
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — management",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F Cat 3 scope",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC06;SC24",
        "commercial_destination": "",
        "planned_article_count": 13,
        "priority": "P2",
        "validation_needed": "Keyword discovery",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC14",
        "parent_category_id": 4,
        "subcategory_title": "Google Business Profile & Local Listings",
        "subcategory_description": (
            "Set up, optimize, and maintain your Google Business Profile and core local listings so "
            "nearby customers can find and trust your plumbing business."
        ),
        "included_topics": "GBP setup; categories; photos; posts; linking your website URL",
        "scope_boundaries": (
            "In: GBP and listings management. Out: full website build (SC18); broad SEO theory without "
            "local maps focus (SC15)."
        ),
        "primary_keyword": "google business profile for plumbers",
        "secondary_keywords": "google my business for plumbers|add website to google business profile plumbing",
        "search_intent": "informational — local visibility",
        "evidence_status": "tool_volume_band",
        "evidence_source": "phase1d-keyword-volume-audit.csv",
        "evidence_date": "2026-10-18",
        "volume_band": "<100",
        "numeric_volume": "",
        "serp_validation_status": "partial — Phase 1C SERP noted",
        "overlap_risk": "low",
        "overlap_with_subcategory_ids": "SC15",
        "commercial_destination": "https://plumberswebsites.com/ (website URL on GBP — contextual)",
        "planned_article_count": 15,
        "priority": "P1",
        "validation_needed": "Semrush numeric volume; owner-intent SERP refresh",
        "status": "proposed",
        "notes": "Band is not exact monthly volume.",
    },
    {
        "subcategory_id": "SC15",
        "parent_category_id": 4,
        "subcategory_title": "Local SEO & Maps Visibility",
        "subcategory_description": (
            "Improve how your plumbing business ranks in local search and maps — service area strategy, "
            "on-site local signals, and owner-focused SEO without homeowner 'rank for emergency plumber' tactics."
        ),
        "included_topics": "Local SEO pillars; service area pages strategy; NAP consistency; local content principles",
        "scope_boundaries": (
            "In: local/search visibility off-site and strategy. Out: on-page website SEO implementation (SC21); "
            "national/generic seo spam lists."
        ),
        "primary_keyword": "local seo for plumbing company",
        "secondary_keywords": "seo for plumbing business",
        "search_intent": "informational — local SEO",
        "evidence_status": "no_exact_match_returned",
        "evidence_source": "phase1d-keyword-volume-audit.csv",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "required",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC14;SC21",
        "commercial_destination": "",
        "planned_article_count": 15,
        "priority": "P1",
        "validation_needed": "Mandatory SERP validation — seo for plumbing business has <100 band but noisy SERP",
        "status": "proposed",
        "notes": "seo for plumbing business: tool_volume_band <100 in Phase 1D.",
    },
    {
        "subcategory_id": "SC16",
        "parent_category_id": 4,
        "subcategory_title": "Reviews, Reputation & Referrals",
        "subcategory_description": (
            "Earn more reviews, protect your reputation, and build referral systems that bring trusted "
            "local customers — including ethical review practices and responding to feedback."
        ),
        "included_topics": "Review requests; reputation management; referrals; Nextdoor and community referrals",
        "scope_boundaries": "In: reputation and word-of-mouth. Out: paid ads (SC17); website testimonial placement (SC21).",
        "primary_keyword": "google reviews for plumbing business",
        "secondary_keywords": "plumbing company reputation management|plumbing business referral program",
        "search_intent": "informational — reputation",
        "evidence_status": "unverified_candidate",
        "evidence_source": "secondary-shortlist.csv; qualified TG-01 cluster variants",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "low",
        "overlap_with_subcategory_ids": "SC17",
        "commercial_destination": "",
        "planned_article_count": 15,
        "priority": "P2",
        "validation_needed": "Volume and SERP for review/referral seeds",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC17",
        "parent_category_id": 4,
        "subcategory_title": "Marketing, Advertising & Lead Generation",
        "subcategory_description": (
            "Choose marketing channels, advertising options, and lead-generation approaches that fit "
            "local plumbing businesses — with your website as one part of a broader growth plan."
        ),
        "included_topics": "Marketing ideas; Google Ads; lead gen; plumbing leads online; offline + digital mix",
        "scope_boundaries": (
            "In: acquisition and paid/owned marketing beyond GBP/local SEO hubs. Out: website conversion "
            "tactics (SC21); business pricing (SC11)."
        ),
        "primary_keyword": "how to get more plumbing customers",
        "secondary_keywords": "plumbing business marketing ideas|plumbing leads online|plumbing business google ads",
        "search_intent": "informational — marketing and leads",
        "evidence_status": "tool_volume_band",
        "evidence_source": "phase1d-keyword-volume-audit.csv; secondary-shortlist.csv",
        "evidence_date": "2026-10-18",
        "volume_band": "<100",
        "numeric_volume": "",
        "serp_validation_status": "partial",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC15;SC16;SC21",
        "commercial_destination": "https://plumberswebsites.com/",
        "planned_article_count": 15,
        "priority": "P2",
        "validation_needed": "SERP noise check — broad marketing queries",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC18",
        "parent_category_id": 5,
        "subcategory_title": "Planning & Building Your Plumbing Website",
        "subcategory_description": (
            "Plan, structure, and launch a plumbing business website — step-by-step guidance, page "
            "planning, and checklists that complement (not replace) our product pages."
        ),
        "included_topics": "How-to build guides; page structure; checklists; preview/process education",
        "scope_boundaries": (
            "In: build process and site structure education. Out: head term plumber website builder on hub "
            "(homepage); primary plumbing website design (/features/); transactional pricing (#pricing)."
        ),
        "primary_keyword": "how to build a plumbing website",
        "secondary_keywords": "what pages should a plumbing website have|plumbing website checklist|do plumbers need a website",
        "search_intent": "informational — website creation",
        "evidence_status": "tool_volume_band",
        "evidence_source": "phase1d-keyword-volume-audit.csv; phase1e AC-01 AC-05 AC-08",
        "evidence_date": "2026-10-18",
        "volume_band": ">100",
        "numeric_volume": "",
        "serp_validation_status": "partial — Phase 1C SERP",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC19;SC20",
        "commercial_destination": "https://plumberswebsites.com/#design ; https://plumberswebsites.com/features/",
        "planned_article_count": 19,
        "priority": "P1",
        "validation_needed": "what pages / checklist: no_exact_match_returned in Phase 1D",
        "status": "proposed",
        "notes": "Phase 1E maps AC-01, AC-05 section, AC-08 here.",
    },
    {
        "subcategory_id": "SC19",
        "parent_category_id": 5,
        "subcategory_title": "Website Builders, Templates & Examples",
        "subcategory_description": (
            "Compare website builders, templates, and real plumbing site examples so you can choose an "
            "approach that fits your business — with honest comparisons and links to live examples."
        ),
        "included_topics": "Builder comparisons; templates; examples; Wix/AI/WordPress sections; agency alternatives",
        "scope_boundaries": (
            "In: tool selection and inspiration. Out: homepage primary plumber website builder; Features primary "
            "plumbing website design; #business template gallery ownership."
        ),
        "primary_keyword": "best plumber website builder",
        "secondary_keywords": (
            "plumbing website template|plumbing website examples|plumber website builder vs wix|"
            "ai plumbing website builder|wordpress for plumbing business|plumbing web design agency"
        ),
        "search_intent": "comparison / research",
        "evidence_status": "no_exact_match_returned",
        "evidence_source": "phase1d-keyword-volume-audit.csv; phase1e AC-02 AC-03",
        "evidence_date": "2026-10-18",
        "volume_band": "template/examples >100 bands for related terms",
        "numeric_volume": "",
        "serp_validation_status": "serp_observed — Phase 1C comparison SERP",
        "overlap_risk": "high",
        "overlap_with_subcategory_ids": "SC18;SC20",
        "commercial_destination": "https://plumberswebsites.com/ ; https://plumberswebsites.com/#business",
        "planned_article_count": 19,
        "priority": "P1",
        "validation_needed": "Semrush for best plumber website builder; SERP for best plumbing websites (>100, ambiguous)",
        "status": "proposed",
        "notes": "Do NOT use plumbing website design as subcategory primary — Features owns.",
    },
    {
        "subcategory_id": "SC20",
        "parent_category_id": 5,
        "subcategory_title": "Website Costs, Hosting & Maintenance",
        "subcategory_description": (
            "Understand total website costs, hosting, domains, and ongoing maintenance for plumbing "
            "businesses — educational TCO and upkeep guides distinct from our pricing section."
        ),
        "included_topics": "TCO; DIY vs agency; hosting; domain; maintenance; worth-it ROI",
        "scope_boundaries": (
            "In: cost and infrastructure education. Out: commercial offer on #pricing; trade job pricing (SC11)."
        ),
        "primary_keyword": "plumbing website cost",
        "secondary_keywords": "how much does a plumbing website cost|plumbing website hosting|is a website worth it for plumbers",
        "search_intent": "pricing research / TCO",
        "evidence_status": "tool_volume_band",
        "evidence_source": "phase1d-keyword-volume-audit.csv; phase1e AC-04 AC-09 AC-11",
        "evidence_date": "2026-10-18",
        "volume_band": "cost/hosting <100",
        "numeric_volume": "",
        "serp_validation_status": "partial",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC18;SC11",
        "commercial_destination": "https://plumberswebsites.com/#pricing",
        "planned_article_count": 19,
        "priority": "P1",
        "validation_needed": "worth-it phrase: no_exact_match_returned",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC21",
        "parent_category_id": 5,
        "subcategory_title": "Website Conversion, Features & On-Site SEO",
        "subcategory_description": (
            "Turn website visitors into calls and jobs — mobile-friendly layouts, click-to-call, forms, "
            "trust elements, and on-site SEO that supports local visibility without duplicating GBP guides."
        ),
        "included_topics": "Click-to-call; forms; mobile; speed; on-page SEO; plumbing website features",
        "scope_boundaries": (
            "In: on-site UX, conversion, technical on-page SEO. Out: GBP/local maps (SC14–15); "
            "Features page primary plumbing website design."
        ),
        "primary_keyword": "plumbing website features",
        "secondary_keywords": "click to call plumber website|mobile friendly plumber website|plumbing website contact form",
        "search_intent": "informational — conversion and on-site improvement",
        "evidence_status": "tool_volume_band",
        "evidence_source": "phase1d-keyword-volume-audit.csv; Phase 1C TR-09",
        "evidence_date": "2026-10-18",
        "volume_band": "features <100",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC15;SC14",
        "commercial_destination": "https://plumberswebsites.com/features/ ; https://plumberswebsites.com/#faq",
        "planned_article_count": 18,
        "priority": "P1",
        "validation_needed": "Conversion micro-queries mostly no_exact_match_returned",
        "status": "proposed",
        "notes": "Supports /features/ — does not compete for design as hub primary.",
    },
    {
        "subcategory_id": "SC22",
        "parent_category_id": 6,
        "subcategory_title": "Industry Trends & Market Developments",
        "subcategory_description": (
            "Follow changes shaping the plumbing industry — demand patterns, regulations, sustainability "
            "pressures, and market shifts that affect how owners plan for the next few years."
        ),
        "included_topics": "Industry news interpretation; market outlook; regulatory trends; customer expectations",
        "scope_boundaries": (
            "In: macro industry context for owners. Out: hands-on field techniques (Cat 1); licensing detail (SC07); "
            "website how-tos (Cat 5)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — industry awareness",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F Cat 6 gap",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC05;SC23",
        "commercial_destination": "",
        "planned_article_count": 15,
        "priority": "P3",
        "validation_needed": "Owner-intent trend keyword discovery",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC23",
        "parent_category_id": 6,
        "subcategory_title": "Business Technology & Operational Innovation",
        "subcategory_description": (
            "Explore business-side technology — office software, dispatch innovations, and operational "
            "tools that change how plumbing companies run, distinct from jobsite tool tech or website builders."
        ),
        "included_topics": "FSM trends; AI in operations; integration strategies; future of dispatch",
        "scope_boundaries": (
            "In: company-level technology trends. Out: field tool guides (SC05); software how-to hub (SC12); "
            "website builders (SC19)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "best software for plumbing business",
        "search_intent": "informational — business technology",
        "evidence_status": "unverified_candidate",
        "evidence_source": "secondary-shortlist.csv",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC05;SC12;SC19",
        "commercial_destination": "",
        "planned_article_count": 15,
        "priority": "P3",
        "validation_needed": "Split software 'how-to' (SC12) vs trend/innovation (SC23)",
        "status": "proposed",
        "notes": "",
    },
    {
        "subcategory_id": "SC24",
        "parent_category_id": 6,
        "subcategory_title": "Leadership, Culture & Professional Growth",
        "subcategory_description": (
            "Develop leadership skills, company culture, and professional growth habits that help owners "
            "and managers build stronger plumbing businesses over the long term."
        ),
        "included_topics": "Leadership; culture; owner burnout; succession; professional habits",
        "scope_boundaries": (
            "In: leadership and growth mindset for owners. Out: licensing/training compliance (Cat 2); "
            "hiring operations (SC13)."
        ),
        "primary_keyword": "",
        "secondary_keywords": "",
        "search_intent": "informational — professional development",
        "evidence_status": "intent_hypothesis",
        "evidence_source": "Phase 1F Cat 6 scope",
        "evidence_date": "2026-10-18",
        "volume_band": "",
        "numeric_volume": "",
        "serp_validation_status": "not_started",
        "overlap_risk": "medium",
        "overlap_with_subcategory_ids": "SC06;SC13;SC09",
        "commercial_destination": "",
        "planned_article_count": 15,
        "priority": "P3",
        "validation_needed": "Keyword discovery; avoid career/exam overlap",
        "status": "proposed",
        "notes": "",
    },
]

# Keyword → subcategory allocation (hierarchy level per row)
KEYWORD_ALLOCATIONS: list[dict] = [
    {"keyword": "how to build a plumbing website", "parent_category_id": 5, "subcategory_id": "SC18", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d-keyword-volume-audit.csv", "evidence_date": "2026-10-18", "volume_band": ">100", "numeric_volume": "", "allocation_rationale": "Phase 1E AC-01 flagship; SC18 build hub", "overlap_risk": "low", "validation_needed": "Semrush numeric"},
    {"keyword": "what pages should a plumbing website have", "parent_category_id": 5, "subcategory_id": "SC18", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Features section + AC-01; not subcategory title", "overlap_risk": "medium vs /features/", "validation_needed": "Semrush"},
    {"keyword": "plumbing website checklist", "parent_category_id": 5, "subcategory_id": "SC18", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "AC-08", "overlap_risk": "low", "validation_needed": "Semrush"},
    {"keyword": "plumbing website template", "parent_category_id": 5, "subcategory_id": "SC19", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": ">100", "numeric_volume": "", "allocation_rationale": "Gallery #business owns selection; Academy educates", "overlap_risk": "medium vs #business", "validation_needed": "Semrush"},
    {"keyword": "plumbing website examples", "parent_category_id": 5, "subcategory_id": "SC19", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": ">100", "numeric_volume": "", "allocation_rationale": "AC-02", "overlap_risk": "medium vs #business", "validation_needed": "SERP intent"},
    {"keyword": "best plumber website builder", "parent_category_id": 5, "subcategory_id": "SC19", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "AC-03 comparison — not subcategory H1", "overlap_risk": "high vs homepage", "validation_needed": "Semrush + intent"},
    {"keyword": "plumbing website design", "parent_category_id": 5, "subcategory_id": "SC19", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": ">100", "numeric_volume": "", "allocation_rationale": "Commercial /features/ primary — Academy supports only", "overlap_risk": "high vs /features/", "validation_needed": "Do not use as SC19 hub primary"},
    {"keyword": "plumber website builder", "parent_category_id": 5, "subcategory_id": "SC19", "recommended_hierarchy_level": "commercial_only", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": ">100", "numeric_volume": "", "allocation_rationale": "Homepage only — not Academy hub", "overlap_risk": "high", "validation_needed": "N/A — ownership locked"},
    {"keyword": "plumbing website cost", "parent_category_id": 5, "subcategory_id": "SC20", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "<100", "numeric_volume": "", "allocation_rationale": "AC-04 TCO vs #pricing offer", "overlap_risk": "medium vs #pricing", "validation_needed": "Semrush"},
    {"keyword": "plumbing website hosting", "parent_category_id": 5, "subcategory_id": "SC20", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "<100", "numeric_volume": "", "allocation_rationale": "AC-11", "overlap_risk": "low", "validation_needed": "Semrush"},
    {"keyword": "is a website worth it for plumbers", "parent_category_id": 5, "subcategory_id": "SC20", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "AC-09 ROI", "overlap_risk": "low", "validation_needed": "Semrush"},
    {"keyword": "plumbing website features", "parent_category_id": 5, "subcategory_id": "SC21", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "<100", "numeric_volume": "", "allocation_rationale": "Supports /features/", "overlap_risk": "medium vs /features/", "validation_needed": "Semrush"},
    {"keyword": "click to call plumber website", "parent_category_id": 5, "subcategory_id": "SC21", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Conversion hub TR-09", "overlap_risk": "low", "validation_needed": "Semrush"},
    {"keyword": "google business profile for plumbers", "parent_category_id": 4, "subcategory_id": "SC14", "recommended_hierarchy_level": "subcategory_supporting", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "<100", "numeric_volume": "", "allocation_rationale": "Natural fit SC14 hub theme", "overlap_risk": "low", "validation_needed": "Semrush"},
    {"keyword": "local seo for plumbing company", "parent_category_id": 4, "subcategory_id": "SC15", "recommended_hierarchy_level": "subcategory_supporting", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "SC15 title intent — validate before SEO-led rename", "overlap_risk": "medium vs SC21", "validation_needed": "SERP mandatory"},
    {"keyword": "seo for plumbing business", "parent_category_id": 4, "subcategory_id": "SC15", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "<100", "numeric_volume": "", "allocation_rationale": "Owner SEO pillar article(s)", "overlap_risk": "medium SERP noise", "validation_needed": "SERP owner vs agency"},
    {"keyword": "how to get more plumbing customers", "parent_category_id": 4, "subcategory_id": "SC17", "recommended_hierarchy_level": "article", "evidence_status": "tool_volume_band", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "<100", "numeric_volume": "", "allocation_rationale": "Lead gen pillar", "overlap_risk": "low", "validation_needed": "Semrush"},
    {"keyword": "plumbing business marketing ideas", "parent_category_id": 4, "subcategory_id": "SC17", "recommended_hierarchy_level": "article", "evidence_status": "unverified_candidate", "evidence_source": "secondary-shortlist.csv", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Marketing hub spoke", "overlap_risk": "low", "validation_needed": "Volume unknown"},
    {"keyword": "google reviews for plumbing business", "parent_category_id": 4, "subcategory_id": "SC16", "recommended_hierarchy_level": "article", "evidence_status": "unverified_candidate", "evidence_source": "secondary-shortlist.csv", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Reputation subcategory", "overlap_risk": "low", "validation_needed": "SERP"},
    {"keyword": "starting a plumbing business checklist", "parent_category_id": 3, "subcategory_id": "SC10", "recommended_hierarchy_level": "article", "evidence_status": "unverified_candidate", "evidence_source": "secondary-shortlist.csv", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Startup hub anchor article", "overlap_risk": "low", "validation_needed": "Semrush/GKP"},
    {"keyword": "best software for plumbing business", "parent_category_id": 3, "subcategory_id": "SC12", "recommended_hierarchy_level": "article", "evidence_status": "unverified_candidate", "evidence_source": "secondary-shortlist.csv", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Operations software — trend angle SC23", "overlap_risk": "medium vs SC23", "validation_needed": "Intent split"},
    {"keyword": "plumbing business license and website", "parent_category_id": 2, "subcategory_id": "SC07", "recommended_hierarchy_level": "article", "evidence_status": "unverified_candidate", "evidence_source": "unverified-keyword-opportunities.csv", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Cross-link to SC18", "overlap_risk": "medium vs Cat 5", "validation_needed": "Volume + SERP"},
    {"keyword": "done for you plumber website", "parent_category_id": 5, "subcategory_id": "SC18", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "Process story — link #design", "overlap_risk": "medium vs #design", "validation_needed": "Semrush"},
    {"keyword": "preview plumbing website before paying", "parent_category_id": 5, "subcategory_id": "SC18", "recommended_hierarchy_level": "article", "evidence_status": "no_exact_match_returned", "evidence_source": "phase1d 2026-10-18", "evidence_date": "2026-10-18", "volume_band": "", "numeric_volume": "", "allocation_rationale": "#design section owner", "overlap_risk": "medium vs #design", "validation_needed": "Semrush"},
]

COMMERCIAL_CONFLICT_KEYWORDS = {
    "plumber website builder": "Homepage / — Academy must not use as subcategory hub primary",
    "plumbing website design": "Features /features/ — Academy must not use as subcategory hub primary",
}
