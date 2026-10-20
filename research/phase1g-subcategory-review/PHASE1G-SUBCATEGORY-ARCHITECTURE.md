# Phase 1G — Academy subcategory architecture

**Date:** 2026-10-18  
**Planning only** — no live site, code, or article drafts.

---

## Executive summary

This phase defines **24 subcategories** under the six **approved Phase 1F parent categories**, with **300 planned article slots** (estimates, not an article list). The structure follows the brief’s **5+4+4+4+4+3** distribution.

**Strongest keyword evidence** concentrates in **Category 5** (Phase 1D Ahrefs bands + Phase 1E article map) and **Category 4** (GBP, owner SEO, leads — mostly `<100` bands or no exact match). **Categories 1, 2, and 6** subcategories are **scope- and intent-led** (`intent_hypothesis` / `unverified_candidate`) until dedicated keyword discovery runs.

**Key boundary decisions:**

- **SC05** (field/jobsite tech) vs **SC23** (business/ops tech) vs **SC19** (website builders).
- **SC15** (local SEO off-site) vs **SC21** (on-site SEO/conversion).
- **SC11** (trade pricing/finance) vs **SC20** (website TCO) vs **#pricing** (commercial offer).
- **Commercial:** No subcategory primary keyword is `plumber website builder` or `plumbing website design`.

Machine-readable master: `subcategory-master.csv`. Keyword rows: `subcategory-keyword-allocation.csv`.

---

## Source files

### Found and used

Phase 1C–1F files listed in the Phase 1G brief were present, including `phase1d/ahrefs_free_us_2026-10-18.json`, `phase1d/entries.json`, and all Phase 1F category review files.

### Limitations

- No Semrush numeric volumes in repository.
- Ahrefs Free = **bands only** (2026-10-18).
- Categories 1, 2, 6 lack Phase 1D-validated head terms.

---

## Six approved parent categories (unchanged)

| ID | Title | Subcats | Article target |
|----|-------|--------:|---------------:|
| 1 | Plumbing Techniques, Tools & Equipment | 5 | 30 |
| 2 | Licensing, Training & Credentials | 4 | 35 |
| 3 | Starting & Running a Plumbing Business | 4 | 55 |
| 4 | Finding Customers & Growing Locally | 4 | 60 |
| 5 | Plumbing Websites & Digital Tools | 4 | 75 |
| 6 | Industry Trends & Professional Growth | 3 | 45 |
| | **Total** | **24** | **300** |

Parent descriptions are identical to the Phase 1F approved text (see `subcategory_data.py` / Phase 1F CSV).

---

## Category 1 — Plumbing Techniques, Tools & Equipment (30 articles)

| ID | Title | Articles | Primary keyword evidence |
|----|-------|----------:|---------------------------|
| SC01 | Jobsite Tools & Hand Equipment | 6 | intent_hypothesis |
| SC02 | Power Tools, Specialty Equipment & Vehicles | 6 | intent_hypothesis |
| SC03 | Diagnostics, Inspection & Troubleshooting | 6 | intent_hypothesis — exclude homeowner DIY |
| SC04 | Field Techniques & Installation Methods | 6 | intent_hypothesis |
| SC05 | Field Technology & Jobsite Innovations | 6 | intent_hypothesis — vs SC23/SC22 |

**Rationale:** Initial five “topic ideas” kept as distinct hubs; “plumbing technology” split so **jobsite** tech (SC05) does not collide with **business** tech (SC23) or **website** tools (Cat 5).

---

## Category 2 — Licensing, Training & Credentials (35 articles)

| ID | Title | Articles | Primary keyword evidence |
|----|-------|----------:|---------------------------|
| SC06 | Apprenticeships & Building Your Team's Skills | 9 | intent_hypothesis — owner hiring angle |
| SC07 | Plumbing Licensing & State Requirements | 9 | unverified — `plumbing business license and website` (article) |
| SC08 | Certifications & Professional Credentials | 9 | intent_hypothesis |
| SC09 | Continuing Education & Code Awareness | 8 | intent_hypothesis — not exam prep |

**Overlap:** SC06/SC09 vs SC24 (leadership); SC07 vs SC10 (business formation). **Rejected:** `plumbing license exam` as owner Academy focus.

---

## Category 3 — Starting & Running a Plumbing Business (55 articles)

| ID | Title | Articles | Primary keyword evidence |
|----|-------|----------:|---------------------------|
| SC10 | Starting a Plumbing Business | 14 | unverified — `starting a plumbing business checklist` |
| SC11 | Pricing, Estimating & Business Finances | 14 | intent_hypothesis |
| SC12 | Operations, Scheduling & Customer Service | 14 | unverified — `best software for plumbing business` (how-to here) |
| SC13 | Hiring, Management & Scaling | 13 | intent_hypothesis |

**Boundary:** Marketing → Cat 4; websites → Cat 5. `start a plumbing business website` → **SC18 article**, linked from SC10.

---

## Category 4 — Finding Customers & Growing Locally (60 articles)

| ID | Title | Articles | Primary keyword evidence |
|----|-------|----------:|---------------------------|
| SC14 | Google Business Profile & Local Listings | 15 | tool_volume_band — `google business profile for plumbers` **<100** |
| SC15 | Local SEO & Maps Visibility | 15 | no_exact_match — `local seo for plumbing company`; article band for `seo for plumbing business` **<100** |
| SC16 | Reviews, Reputation & Referrals | 15 | unverified — reviews/referral cluster |
| SC17 | Marketing, Advertising & Lead Generation | 15 | tool_volume_band — `how to get more plumbing customers` **<100** |

**Decision:** Local SEO **separate** from broad marketing — distinct intents and article families; website mentioned as one channel only.

---

## Category 5 — Plumbing Websites & Digital Tools (75 articles)

| ID | Title | Articles | Primary keyword / evidence |
|----|-------|----------|----------------------------|
| SC18 | Planning & Building Your Plumbing Website | 19 | tool_volume_band — `how to build a plumbing website` **>100** |
| SC19 | Website Builders, Templates & Examples | 19 | no_exact_match — `best plumber website builder`; bands for template/examples **>100** |
| SC20 | Website Costs, Hosting & Maintenance | 19 | tool_volume_band — `plumbing website cost` **<100**; hosting **<100** |
| SC21 | Website Conversion, Features & On-Site SEO | 18 | tool_volume_band — `plumbing website features` **<100** |

**Commercial alignment:**

| Destination | Ownership |
|-------------|-----------|
| `/` | `plumber website builder` — **not** subcategory primary |
| `/features/` | `plumbing website design` — **not** subcategory primary |
| `/#business` | Templates/gallery |
| `/#pricing` | Transactional pricing |
| `/#design` | Preview / How It Works |
| `/#faq` | Product questions |

Phase 1E articles map into SC18–SC21 (AC-01→SC18, AC-02/03→SC19, AC-04/09/11→SC20, conversion/features→SC21).

---

## Category 6 — Industry Trends & Professional Growth (45 articles)

| ID | Title | Articles | Primary keyword evidence |
|----|-------|----------:|---------------------------|
| SC22 | Industry Trends & Market Developments | 15 | intent_hypothesis |
| SC23 | Business Technology & Operational Innovation | 15 | unverified — trend angle on software/innovation |
| SC24 | Leadership, Culture & Professional Growth | 15 | intent_hypothesis |

**vs Cat 1:** SC22 macro trends vs SC05 field tool adoption. **vs Cat 2:** SC24 soft skills vs SC07–SC09 compliance.

---

## Article allocation summary

| Category | SC IDs | Sum |
|----------|--------|----:|
| 1 | SC01–SC05 | 30 |
| 2 | SC06–SC09 | 35 |
| 3 | SC10–SC13 | 55 |
| 4 | SC14–SC17 | 60 |
| 5 | SC18–SC21 | 75 |
| 6 | SC22–SC24 | 45 |
| **Total** | | **300** |

No reallocation vs Phase 1G brief targets — evidence density differs but **planning weights** unchanged to avoid artificial shifts without data.

---

## Coherence & cannibalisation review

1. **Cat 1 ↔ 6:** Field technique/equipment (SC01–SC04) vs industry trends (SC22); jobsite tech (SC05) vs business tech (SC23).
2. **Cat 2 ↔ 6:** Credentials (SC07–SC08) vs leadership growth (SC24).
3. **Cat 3 ↔ 4:** Operations (SC12) vs acquisition (SC17); finances (SC11) vs ad spend (SC17).
4. **Cat 4 ↔ 5:** GBP/local (SC14–SC15) vs website build (SC18–SC19); local strategy (SC15) vs on-page implementation (SC21).
5. **Cat 3 ↔ 5:** Business investment (SC11) vs website TCO (SC20).

---

## Research gaps & validation

- **Semrush/GKP** per `semrush-validation-plan.md` for non-band keywords.
- **SERP:** `local seo for plumbing company`, `seo for plumbing business`, `website for plumbers`, `best plumbing websites`.
- **Cat 1, 2, 6:** Dedicated owner-intent keyword discovery before SEO-led subcategory renames.
- **Legal:** SC07/SC09 require authoritative sources when published.

---

## Recommended next step

Approve subcategory IDs and titles/descriptions → **article-level master TOC** by subcategory (not 300 titles in one pass — prioritize P1 subcategories SC14–SC21 + Phase 1E wave).

---

## Full subcategory copy

Each subcategory’s full description, scope boundaries, overlap IDs, and validation notes are in **`subcategory-master.csv`** (24 rows). This document is the narrative index; the CSV is authoritative for implementation planning.
