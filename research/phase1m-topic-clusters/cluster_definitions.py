"""SEO topic cluster definitions — maps inventory article IDs to CL### clusters."""

from __future__ import annotations


def ids(lo: int, hi: int) -> list[str]:
    return [f"A{i:03d}" for i in range(lo, hi + 1)]


def _c(
    cid: str,
    name: str,
    primary_sc: str,
    reader_problem: str,
    intent: str,
    article_list: list[str],
    lead: str = "",
    secondary_sc: str = "",
    priority: str = "P3",
    priority_reason: str = "",
    confidence: str = "medium",
    commercial: str = "low",
    evidence_note: str = "",
    related_clusters: str = "",
    unresolved: str = "",
) -> dict:
    return {
        "cluster_id": cid,
        "cluster_name": name,
        "primary_subcategory_id": primary_sc,
        "secondary_subcategory_ids": secondary_sc,
        "reader_problem": reader_problem,
        "main_search_intent": intent,
        "lead_article_id": lead or (article_list[0] if article_list else ""),
        "article_ids": article_list,
        "initial_priority": priority,
        "priority_reason": priority_reason,
        "confidence": confidence,
        "commercial_relevance": commercial,
        "evidence_summary": evidence_note,
        "related_cluster_ids": related_clusters,
        "unresolved_questions": unresolved,
    }


# 52 candidate clusters — SEO planning layer (not Academy nav).
CLUSTERS: list[dict] = [
    # Cat 1 — Techniques & equipment (10)
    _c("CL001", "Essential jobsite hand tools", "SC01", "Which hand tools crews need daily", "informational", ids(1, 3), "A001", priority="P3", confidence="low", evidence_note="intent_hypothesis — no Phase 1D volumes"),
    _c("CL002", "Hand tool organization, safety and procurement", "SC01", "Organize, maintain and buy hand tools", "informational", ids(4, 6), "A004", priority="P3", confidence="low"),
    _c("CL003", "Power and drain equipment choices", "SC02", "Select drain machines and power tools", "informational", ids(7, 9), "A007", priority="P3", confidence="low"),
    _c("CL004", "Specialty tools, vans and rent-vs-buy", "SC02", "Van setup and specialty equipment economics", "informational", ids(10, 12), "A010", priority="P3", confidence="low"),
    _c("CL005", "Leak detection and field diagnostics", "SC03", "Find leaks and troubleshoot systematically", "informational", ids(13, 15), "A013", priority="P3", confidence="low"),
    _c("CL006", "Inspection, callbacks and escalation", "SC03", "Reduce misdiagnoses and document findings", "informational", ids(16, 18), "A016", priority="P3", confidence="low"),
    _c("CL007", "Installation standards and code-aware work", "SC04", "Standardize quality and rough-in/finish", "informational", ids(19, 21), "A019", priority="P3", confidence="medium", evidence_note="authority review on code sections"),
    _c("CL008", "Field documentation and QC", "SC04", "Photos, training and QC walkthroughs", "informational", ids(22, 24), "A022", priority="P3", confidence="low"),
    _c("CL009", "Inspection cameras and locators", "SC05", "When camera/locator tech pays off", "informational", ids(25, 26), "A025", priority="P3", confidence="low", related_clusters="CL023"),
    _c("CL010", "Jobsite digital tools and adoption", "SC05", "Field apps and evaluating new jobsite tech", "informational", ids(27, 30), "A027", priority="P3", confidence="low", related_clusters="CL023", unresolved="Boundary vs SC23 office software"),
    # Cat 2 — Licensing (8)
    _c("CL011", "Apprenticeships and team skill building", "SC06", "Build apprentice and mentoring programs", "informational", ids(31, 35), "A031", priority="P3", confidence="medium"),
    _c("CL012", "Recruiting and external training partnerships", "SC06", "Recruit entry talent and trade school ties", "informational", ids(36, 39), "A036", priority="P3", confidence="low"),
    _c("CL013", "Contractor licensing and multi-state compliance", "SC07", "Track licenses and state requirements", "informational", ids(40, 44), "A040", priority="P2", confidence="medium", evidence_note="legal/licensing review required"),
    _c("CL014", "License display, insurance and web presence", "SC07", "Show licenses online and verify hires", "informational", ids(45, 48), "A045", secondary_sc="SC18", priority="P2", confidence="medium", commercial="medium", related_clusters="CL028", unresolved="A047/A048 website cross-links — verify against SC18"),
    _c("CL015", "Specialty certifications and credentials", "SC08", "Backflow, medical gas, manufacturer certs", "informational", ids(49, 53), "A049", priority="P3", confidence="low"),
    _c("CL016", "Credentials for bidding and customer trust", "SC08", "Use credentials in sales and marketing", "informational", ids(54, 57), "A054", priority="P3", confidence="low"),
    _c("CL017", "Continuing education and code updates", "SC09", "CEU and staying current on code", "informational", ids(58, 61), "A058", priority="P3", confidence="medium", evidence_note="state-specific research needed"),
    _c("CL018", "Team code training and documentation", "SC09", "Assign and document code training", "informational", ids(62, 65), "A062", priority="P3", confidence="low"),
    # Cat 3 — Business operations (8)
    _c("CL019", "Plumbing business startup essentials", "SC10", "Launch a new plumbing company", "informational", ids(66, 72), "A066", priority="P2", confidence="medium", evidence_note="starting a plumbing business checklist — unverified_candidate", related_clusters="CL028"),
    _c("CL020", "Startup finance, planning and operations setup", "SC10", "Bookkeeping, business plan, office decisions", "informational", ids(73, 79), "A073", priority="P2", confidence="low"),
    _c("CL021", "Pricing models and price books", "SC11", "Price jobs profitably", "informational", ids(80, 86), "A080", priority="P2", confidence="low", related_clusters="CL037", unresolved="Distinct from SC20 website TCO and #pricing"),
    _c("CL022", "Estimating, margins and job costing", "SC11", "Estimate consistently and protect margin", "informational", ids(87, 93), "A087", priority="P2", confidence="low"),
    _c("CL023", "Field service software and dispatch", "SC12", "Choose FSM and scheduling workflows", "informational", ids(94, 100), "A094", priority="P2", confidence="medium", evidence_note="best software for plumbing business — unverified_candidate", related_clusters="CL010;CL051"),
    _c("CL024", "Customer service and call handling", "SC12", "Scripts, SLAs and communication", "informational", ids(101, 107), "A096", priority="P2", confidence="low", related_clusters="CL042"),
    _c("CL025", "Hiring and team structure", "SC13", "Interview, roles and onboarding", "informational", ids(108, 114), "A108", priority="P2", confidence="low"),
    _c("CL026", "Scaling, culture and succession", "SC13", "Grow crews, culture and exit planning", "informational", ids(115, 120), "A115", priority="P2", confidence="low", related_clusters="CL052"),
    # Cat 4 — Local growth (10)
    _c("CL027", "Google Business Profile setup and categories", "SC14", "Set up GBP for a plumbing company", "informational", ids(121, 125), "A121", priority="P1", priority_reason="tool_volume_band; Wave 1 local foundation", confidence="medium", evidence_note="google business profile for plumbers — band <100 not exact volume", commercial="medium", related_clusters="CL028;CL029"),
    _c("CL028", "GBP optimization, listings and NAP", "SC14", "Photos, NAP, citations, multi-location GBP", "informational", ids(126, 135), "A126", priority="P1", priority_reason="GBP + website URL alignment", confidence="medium", commercial="medium", related_clusters="CL027;CL029;CL031"),
    _c("CL029", "Local SEO strategy for plumbing companies", "SC15", "Owner-focused local SEO overview", "informational", ids(136, 139), "A136", priority="P1", priority_reason="SC15 distinct from SC21 on-page", confidence="low", evidence_note="local seo for plumbing company — no_exact_match_returned", related_clusters="CL030;CL031", unresolved="SERP validation required for seo for plumbing business"),
    _c("CL030", "Service area and local content strategy", "SC15", "Service area pages without city spam", "informational", ids(140, 143), "A138", priority="P1", confidence="medium", related_clusters="CL032;CL028"),
    _c("CL031", "Local links, measurement and audits", "SC15", "Links, audits, rebrand local SEO", "informational", ids(144, 150), "A144", priority="P2", confidence="low", related_clusters="CL029"),
    _c("CL032", "Google reviews and reputation systems", "SC16", "Ethical review requests and reputation", "informational", ids(151, 155), "A151", priority="P2", confidence="low", evidence_note="google reviews — unverified_candidate", related_clusters="CL033;CL042"),
    _c("CL033", "Referrals, community and crisis reputation", "SC16", "Referrals, Nextdoor, negative reviews", "informational", ids(156, 165), "A153", priority="P2", confidence="low"),
    _c("CL034", "Plumbing customer acquisition overview", "SC17", "Channels to get more customers", "informational", ids(166, 170), "A166", priority="P2", confidence="medium", evidence_note="how to get more plumbing customers — tool_volume_band <100", commercial="medium", related_clusters="CL035"),
    _c("CL035", "Digital ads, leads and attribution", "SC17", "Ads, lead gen, attribution", "informational", ids(171, 174), "A168", priority="P2", confidence="low", evidence_note="plumbing leads online — unverified", commercial="medium"),
    _c("CL036", "Offline marketing and marketing operations", "SC17", "Direct mail, wraps, calendar, seasonality", "informational", ids(175, 180), "A175", priority="P3", confidence="low"),
    # Cat 5 — Websites & digital (16)
    _c("CL037", "Build and launch a plumbing website", "SC18", "End-to-end website build process", "informational", ["A181", "A182", "A183", "A184", "A185"], "A181", priority="P1", priority_reason="Published lead A181 + checklist A185", confidence="high", evidence_note="how to build — tool_volume_band >100", commercial="high", related_clusters="CL038;CL039;CL040;CL041"),
    _c("CL038", "Website page content and copy planning", "SC18", "Services, about, contact, service area copy", "informational", ids(186, 191), "A186", priority="P2", confidence="medium", related_clusters="CL037;CL042", commercial="medium"),
    _c("CL039", "Trust content, media and legal pages", "SC18", "Photos, galleries, legal pages on site", "informational", ids(192, 195), "A191", priority="P2", confidence="low", unresolved="Legal page articles need legal review"),
    _c("CL040", "Website migration, domain and launch QA", "SC18", "Migrate, subdomain, call tracking, launch QA", "informational", ids(196, 199), "A196", priority="P2", confidence="low", related_clusters="CL037;CL044"),
    _c("CL041", "Website builder comparison (platform choice)", "SC19", "Compare builders and approaches fairly", "informational/comparison", ["A201", "A204", "A205", "A211", "A212", "A213"], "A201", priority="P1", priority_reason="Published A201; homepage owns plumber website builder", confidence="medium", evidence_note="best plumber website builder — no_exact_match_returned; serp_observed", commercial="high", related_clusters="CL037;CL042;CL043", unresolved="Do not target homepage H1 phrasing as primary"),
    _c("CL042", "Examples, templates and design patterns", "SC19", "Learn from examples and templates", "informational/visual", ["A200", "A202", "A203", "A216", "A217", "A218"], "A200", priority="P1", priority_reason="Published A200", confidence="medium", evidence_note="plumbing website examples — tool_volume_band >100", commercial="high", related_clusters="CL041", unresolved="/designs/ owns plumbing website template — link not #business alone"),
    _c("CL043", "DIY platforms, CRM sites and niche comparisons", "SC19", "Wix, Squarespace, CRM bundled sites, AI", "informational/comparison", ["A206", "A207", "A208", "A209", "A210", "A214", "A215"], "A206", priority="P2", confidence="low", evidence_note="Many no_exact_match_returned", commercial="medium", related_clusters="CL041", unresolved="A210 uses plumbing website design — must support /features/ not compete"),
    _c("CL044", "Website total cost and budgeting (TCO)", "SC20", "Understand website cost of ownership", "informational/pricing research", ["A219", "A222", "A223", "A224", "A230", "A231", "A233", "A234", "A236"], "A219", priority="P1", priority_reason="Published A219; distinct from #pricing", confidence="medium", evidence_note="plumbing website cost — tool_volume_band <100", commercial="medium", related_clusters="CL041;CL045", unresolved="Homepage pricing section owns product offer"),
    _c("CL045", "Website worth-it and ROI decisions", "SC20", "Decide if a site is worth the investment", "informational", ["A220", "A235", "A232"], "A220", priority="P2", confidence="low", evidence_note="is a website worth it — no_exact_match_returned", related_clusters="CL044"),
    _c("CL046", "Hosting, domain, SSL and maintenance", "SC20", "Hosting, domain, security, upkeep schedules", "informational", ["A221", "A225", "A226", "A227", "A228", "A229", "A237"], "A221", priority="P2", confidence="medium", evidence_note="hosting band <100 in Phase 1D", related_clusters="CL044"),
    _c("CL047", "Mobile contact and click-to-call", "SC21", "Phone UX and mobile-friendly sites", "informational", ["A239", "A240", "A243"], "A239", priority="P1", priority_reason="Conversion foundation; supports /features/", confidence="low", evidence_note="click-to-call — no_exact_match_returned", commercial="high", related_clusters="CL048;CL049"),
    _c("CL048", "Forms, quotes and lead capture UX", "SC21", "Contact forms and quote requests", "informational", ["A241", "A242", "A247", "A248"], "A241", priority="P2", confidence="low", related_clusters="CL047"),
    _c("CL049", "On-site SEO and page optimization", "SC21", "On-page SEO for plumbing service pages", "informational", ["A246", "A244", "A245"], "A246", priority="P1", confidence="medium", related_clusters="CL029", unresolved="SC21 on-page vs SC15 local strategy — keep distinct"),
    _c("CL050", "Website features, trust UI and performance", "SC21", "Features, speed, badges, showcases", "informational", ["A238", "A250", "A249", "A251", "A252", "A253", "A254", "A255"], "A238", priority="P1", confidence="medium", evidence_note="plumbing website features — tool_volume_band <100", commercial="high", related_clusters="CL042;CL047", unresolved="plumbing website features supports Features page — not primary design term"),
    # Cat 6 — Trends & growth (4)
    _c("CL051", "Industry trends and market outlook", "SC22", "Macro trends affecting plumbing businesses", "informational", ids(256, 262), "A256", priority="P3", confidence="low", evidence_note="intent_hypothesis"),
    _c("CL052", "Regulatory, sustainability and customer expectations", "SC22", "Regulations and demand shifts", "informational", ids(263, 270), "A258", priority="P3", confidence="low"),
    _c("CL053", "Business technology trends and integrations", "SC23", "FSM trends, AI ops, phone/CRM/web integration", "informational", ids(271, 285), "A271", priority="P3", confidence="low", evidence_note="best software — unverified", related_clusters="CL023", unresolved="SC23 trends vs SC12 how-to software"),
    _c("CL054", "Leadership, culture and owner professional growth", "SC24", "Leadership, burnout, succession habits", "informational", ids(286, 300), "A286", priority="P3", confidence="low", related_clusters="CL026"),
]

