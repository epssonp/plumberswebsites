# Phase 1C — Strict Keyword Quality Audit

**Site:** PlumbersWebsites.com  
**Market:** United States  
**Date:** 2026-10-18  
**Objective:** Smaller, stronger, evidence-based opportunities — **not** a padded keyword spreadsheet.

Phase 1 and Phase 1B files are **preserved unchanged**. Phase 1C supersedes Phase 1B for **implementation priority** only.

---

## Executive summary

We reassessed **171 non-excluded registry keywords** and the **130-row Phase 1B ranked list** from first principles. **Provisional priority scores from Phase 1B are not evidence of traffic** and were not used as qualification criteria.

| List | What it is | Count |
|------|------------|------:|
| **A — Qualified** | Distinct **clusters** with owner intent, SERP support, and clear page ownership | **23** |
| **B — Promising unverified** | May merit investment after volume + SERP validation | **67** |
| **C — Reject / combine** | Padding, variants, competitor brands, narrow features, exclusions | **105** (+ 20 EX in registry) |

**Bottom line:** Pursue **~23 intent clusters**, implemented as **~12–16 distinct URLs** (including existing homepage, Features, and key sections) — not 130 pages or 130 keyword targets.

---

## Methodology

### What counted as evidence (Phase 1C)

| Evidence type | Used? | Notes |
|---------------|-------|-------|
| US search volume | **No** | Not available — all List A marked **UNVERIFIED — VOLUME UNKNOWN** |
| Keyword difficulty | **No** | Not collected |
| SERP page types & competitor URLs | **Yes** | Phase 1 observations + US web/SERP check **2026-10-18** on head/comparison queries |
| Product / audience fit | **Yes** | Plumbing **business owner** only |
| Phase 1B priority_score | **No** | Explicitly excluded as traffic proxy |

### Three assessment dimensions (every List A cluster)

1. **Traffic potential** — Is there *any* defensible sign of demand? Without volume, we only infer from **SERP competitiveness** (multiple products and guides investing in the topic). Still **UNVERIFIED** until Semrush/GKP/GSC.  
2. **Audience & intent fit** — Is the searcher likely choosing or improving a **business website**?  
3. **Commercial & ranking opportunity** — Can PlumbersWebsites.com credibly compete with **comparison tables, live preview proof, and honest product boundaries**?

Overall opportunity labels in CSV (`strong` / `moderate` / `weak`) combine dimensions (2) and (3) and **penalize unknown volume** — they are **not** traffic forecasts.

### Cluster-first rule

List A contains **one primary keyword per cluster**. Other registry phrases roll to **List C (combine)** unless promoted from List B after validation.

---

## List A — Qualified opportunities (summary)

Full ranked table: **`qualified-keyword-opportunities.csv`**.

| Rank | Cluster | Primary keyword | Page | Action |
|-----:|---------|-----------------|------|--------|
| 1 | TB-01 | plumber website builder | `/` | Improve — **keep H1 ownership** |
| 2 | TB-12 | plumberswebsites.com | `/` | Improve — brand |
| 3 | TB-02 | website for plumbers | `/` | Improve — supporting copy |
| 4 | TB-09 | done for you plumber website | `/` + Features | Improve |
| 5 | TB-10 | preview plumbing website before paying | `/#design` | Improve |
| 6 | TB-03 | plumbing website design | `/features/` | Improve |
| 7 | TR-07 | plumbing website features | `/features/` | Improve — **same URL as #6** |
| 8 | TB-07 | plumbing website cost | `/#pricing` + Academy cost | Improve + new guide |
| 9 | TB-05 | plumbing website template | `/#business` | Improve |
| 10 | TB-06 | plumbing website examples | Academy examples | New |
| 11 | TR-01 | best plumber website builder | Academy comparison | New |
| 12 | TR-04 | how to build a plumbing website | Academy how-to | New |
| 13 | TR-06 | what pages should a plumbing website have | `/features/` | Improve — not separate URL |
| 14 | TR-02 | plumber website builder vs wix | Wix spoke | New or pillar section |
| 15 | TR-14 | ai plumbing website builder | AI spoke | Section under comparison first |
| 16 | TR-05 | plumbing website checklist | Academy checklist | New — Wave 2 |
| 17 | TR-04 | is a website worth it for plumbers | Academy worth-it | New — Wave 2 |
| 18 | TR-09 | click to call plumber website | Conversion hub | New — one hub |
| 19 | TR-03 | wordpress for plumbing business | WordPress spoke | New — lower priority |
| 20 | TG-03 | google business profile for plumbers | GBP guide | New — Wave 3 + SERP check |
| 21 | TG-04 | local seo for plumbing company | Local SEO | New — Wave 3 + SERP check |
| 22 | TG-04 | seo for plumbing business | SEO pillar | New — Wave 3; owner framing |
| 23 | TG-01 | how to get more plumbing customers | Leads pillar | New — Wave 3; noisy SERP |

**Strongest traffic × buying intent combination (pre-volume):** Ranks **1, 8, 11, 12** — head builder, cost, best builder comparison, how-to build. SERPs show **paid competition** (many builders + guides); differentiation is **preview + five-page trade product**, not keyword count.

---

## List B — Promising but unverified

**File:** `unverified-keyword-opportunities.csv` (67 keywords).

Examples:

- Hosting, maintenance, redesign, agency alternatives, CRM (Jobber/HCP)  
- Free/trial phrasing (needs honest messaging review)  
- Most Tier 3 marketing long-tails  
- Tier 2 platform long-tails (GoDaddy, Yola, Squarespace-only queries)

**Required before promotion:** US volume, SERP owner-intent check, distinct URL need — see **`semrush-validation-plan.md`**.

---

## List C — Reject or combine

**File:** `rejected-and-combined-keywords.csv` (105 rows).

### Removed entirely (examples)

- Phase 1 **EX** clusters (homeowner hire, geo traps, career/supply)  
- **Competitor-brand targets:** `butternut plumber website`, `yola plumber website`, etc. — factual mention only in comparison content  
- **Narrow feature/legal micro-targets:** SSL, privacy policy, mobile menu, insurance badge, guarantee wording, GTM, chatbot, truck wrap QR, etc.  
- **Generic business-type fluff:** `family owned plumbing website`, `commercial vs residential website` as SEO targets

### Combined (not separate SEO targets)

- **~80+ supporting variants** from Phase 1B ranked list (e.g. *website for plumbers*, *cheap plumbing website*, *five page plumber website*) → owned by List A primary pages  
- **Platform comparison long-tails** → sections under **best plumber website builder**  
- **Conversion micro-queries** → **one conversion hub** unless Semrush proves distinct SERP

**Phase 1B ranked list:** Treat as **historical prioritization experiment** — **do not implement as 130 targets**.

---

## Traffic & data limitations

- **No US volume, KD, CPC, or GSC** in repository.  
- Every List A row: **`traffic_evidence = UNVERIFIED — VOLUME UNKNOWN`**.  
- SERP observations dated **2026-10-18** where noted; re-check before writing long-form content.

---

## Answers to final questions

### 1. How many genuinely qualified keyword **clusters** remain?

**23** (List A). These are the working set.

### 2. Strongest combination of traffic potential (inferred) and buying intent?

1. **plumber website builder** (homepage)  
2. **plumbing website cost** (pricing + TCO guide)  
3. **best plumber website builder** (comparison Academy)  
4. **how to build a plumbing website** (Academy)  
5. **plumbing website design / features** (Features page)

*Volume still unverified — validate seeds in Semrush plan first wave.*

### 3. Relevant informational topics that could attract future customers?

- **How-to build**, **page structure**, **worth-it ROI**, **examples** (Tier 2)  
- **GBP**, **local SEO**, **owner SEO**, **leads/customers** (Tier 3) — only with **owner-safe** SERP framing  

### 4. Keywords / clusters to remove entirely?

All **List C** with disposition **reject**; all **exclusion-report** homeowner/geo/career clusters; **competitor-brand SEO targets**; **feature micro-phrases** cited in Phase 1C brief.

### 5. How many distinct pages are justified by qualified clusters?

| Type | Count |
|------|------:|
| Existing commercial URLs/sections to improve | **5** (`/`, `/features/`, `#pricing`, `#design`, `#business`) |
| **New** Academy URLs strongly justified | **7–9** (comparison, cost guide, how-to, examples, conversion hub, worth-it, checklist; optional Wix/AI/WordPress spokes) |
| **New** Tier 3 pillars (after validation) | **4** (GBP, local SEO, SEO pillar, leads) |
| **Total distinct page intents** | **~12–16** near term; **~18–20** if all List A Tier 3 passes SERP gates |

Many List A clusters **share one URL** (homepage or Features).

### 6. Which opportunities require external volume validation before investment?

**All List A** for prioritization ordering; **mandatory before writing** for Tier 3 ranks 20–23 and all **List B**.  
**First validation batch:** 25 seeds in `semrush-validation-plan.md`.

### 7. What to implement first, and why?

| Order | Work | Why |
|------:|------|-----|
| 1 | **Homepage** — head term, DFY, preview, supporting variants | Highest buying intent; already canonical |
| 2 | **Features** — design, features, page structure | Commercial investigation; avoids homepage cannibalisation |
| 3 | **`/#pricing` + `#design` + `#business`** | Cost, preview, templates — Tier 1 support |
| 4 | **Academy: best plumber website builder** | SERP full of comparisons; intercepts research traffic |
| 5 | **Academy: plumbing website cost** | PAA + Wix competitor; supports pricing |
| 6 | **Academy: how to build a plumbing website** | Feeds Features + preview CTA |
| 7 | Examples, checklist, worth-it, conversion hub | Wave 2 |
| 8 | Tier 3 pillars | Only after Semrush + SERP owner check |

**Do not implement:** 130-keyword Phase 1B plan, competitor-brand pages, or feature micro-articles.

---

## Regenerate Phase 1C CSVs

```bash
python research/generate_phase1c_audit.py
```

---

## Recommended next step

Run **`semrush-validation-plan.md`** batch 1 exports, then reorder List A ranks by **volume × commercial fit** in a future **Phase 1D** merge file (preserve this audit as archive).
