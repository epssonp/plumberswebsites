# Priority content roadmap — Phase 1B

**Ordering principle:** Highest commercial intent and existing URL leverage first; new Academy pages only where a **distinct intent** requires them; Tier 3 after core consideration funnel exists.

**Legend:**  
- **Improve** = existing URL/section copy/structure (implementation phase — not done in 1B)  
- **New** = proposed Academy or new section  
- **Validate** = SERP check required before writing  

---

## Wave 0 — Foundation (no new URLs)

| Order | Item | Type | Rank driver | Outcome |
|------:|------|------|-------------|---------|
| 0.1 | Homepage commercial clarity | Improve `/` | 1–3, 6–7 | Head term + DFY + preview story reinforced |
| 0.2 | Pricing + cost cross-link plan | Improve `#pricing` | 4, 17–19 | Buyer pricing; tease TCO guide |
| 0.3 | How It Works / preview | Improve `#design` | 8, 10 | Differentiator vs AI builders |
| 0.4 | Design gallery | Improve `#business` | 9 | Template/design intent |
| 0.5 | FAQ (free vs preview) | Improve `#faq` | 13–15 | Honest trial/preview messaging |
| 0.6 | Features depth pass | Improve `/features/` | 5, 23–24 | Structure, mobile, vs DIY — **no H1 change to head term** |

**Exit criteria:** Clear paths to app sign-in; internal link placeholders documented for Academy (no orphan commercial pages).

---

## Wave 1 — Highest-value new content (consideration funnel)

| Order | Page | Type | Primary keyword | Supports commercial |
|------:|------|------|-----------------|---------------------|
| 1.1 | `/academy/best-plumber-website-builder/` | **New** | best plumber website builder (rank 20) | Homepage |
| 1.2 | `/academy/plumbing-website-cost/` | **New** | plumbing website cost / TCO (rank 4 research leg) | `#pricing`, homepage |
| 1.3 | `/academy/how-to-build-a-plumbing-website/` | **New** | how to build a plumbing website (rank 22) | Homepage, Features |

**Why this order:** Comparison intercepts research traffic closest to purchase; cost answers PAA from head SERP; how-to feeds Features and preview CTA without competing for rank 1 query.

**Supporting links to add when published:**  
Comparison → cost guide, Features, homepage.  
Cost → `#pricing`, comparison (DIY line items).  
How-to → Features (five pages), checklist (Wave 2).

---

## Wave 2 — Product-adjacent research (Tier 2)

| Order | Page | Type | Notes |
|------:|------|------|-------|
| 2.1 | `/academy/plumbing-website-checklist/` | New | Links to how-to + Features |
| 2.2 | `/academy/plumbing-website-examples/` | New | Proton + design gallery; rank 12 cluster |
| 2.3 | `/academy/ai-plumbing-website-builder/` | New | Rank 21; link from comparison pillar |
| 2.4 | `/academy/plumber-website-builder-vs-wix/` | New | Spoke; defer if pillar covers Wix well |
| 2.5 | `/academy/is-a-website-worth-it-for-plumbers/` | New | ROI; links homepage |
| 2.6 | `/academy/plumbing-website-conversion/` | New | Phone/forms; supports Features |
| 2.7 | `/academy/plumbing-website-hosting-and-domain/` | New | **Only verified hosting/domain claims** |

**Combine / defer in Wave 2:**  
Squarespace spoke, agency alternatives, maintenance/legal — **defer** until Wave 1–2 live and resourced.  
WordPress guide — **after** comparison pillar (shared audience).

---

## Wave 3 — Tier 3 pillars (validate SERP first)

| Order | Page | Validate | Rank band |
|------:|------|----------|-----------|
| 3.1 | `/academy/google-business-profile-plumbers/` | Owner intent | 106+ |
| 3.2 | `/academy/seo-for-plumbing-business/` | Not homeowner SEO | 104+ |
| 3.3 | `/academy/local-seo-plumbing-company/` | No city landing matrix | 113+ |
| 3.4 | `/academy/get-more-plumbing-customers/` | Leads hub | 108+ |
| 3.5 | `/academy/plumbing-business-marketing-ideas/` | Hub only if 3.4 needs breadth | tier 3 |

**Defer:** Chatbot, GTM, Nextdoor, franchise, truck-wrap QR topics (below score floor or in `DEFER_KEYWORDS`).

---

## Wave 4 — Optional spokes (only if SERP distinct)

- CRM vs website (Jobber / Housecall Pro)  
- WordPress deep dive  
- Platform micro-spokes (GoDaddy, Yola) as sections first  
- Competitor brand navigational queries (factual comparison rows)

---

## Implementation type summary

| Category | Count (roadmap) |
|----------|----------------:|
| Improve existing commercial | 6 sections/pages (Wave 0) |
| New Academy (priority) | 3 (Wave 1) |
| New Academy (next) | ~7 (Wave 2) |
| New Academy (Tier 3 pillars) | 4–5 (Wave 3) |
| **Reasonable first-year build** | **~15–20 net new URLs** + commercial improvements |
| **Full research ceiling** | **~55–72** distinct intents (Phase 1 estimate) |

---

## What not to build (from ranking)

- **41** registry opportunities below tier floors or beyond rank 130 — see Phase 1B report § Deferred.  
- Separate URL per supporting variation in CSV (`target_role = supporting_variation`).  
- City × plumber landing pages.  
- Homeowner repair / hire-a-plumber content.

---

## After data arrives

1. Merge Semrush volumes into registry; re-run `generate_phase1b_ranking.py`.  
2. Promote/demote Tier 3 Wave 3 items based on volume + SERP purity.  
3. Use GSC to add **Wave 0.7** “quick wins” on existing URLs if impressions exist for ranked keywords.
