# Semrush / Ahrefs / Google Keyword Planner — validation plan

**Purpose:** Turn **UNVERIFIED — VOLUME UNKNOWN** List A clusters into evidence-backed priorities.  
**Status:** No Semrush, Ahrefs, or Keyword Planner access was used in Phase 1C (2026-10-18).

---

## 1. What to export (minimum fields)

For each seed keyword below, collect for **United States** only:

| Field | Use |
|-------|-----|
| Keyword | Match or close variant |
| Monthly search volume (US) | Traffic potential gate |
| Keyword difficulty (or Ahrefs KD) | Ranking effort (not a guarantee) |
| CPC (USD) | Commercial value signal |
| SERP features | Local pack, PAA, ads — intent check |
| Top 10 ranking URLs | Owner vs homeowner vs agency |
| Trend (12 mo) | Seasonality |

**Export format:** CSV with source tool name and export date in filename.

---

## 2. Seed keywords — List A primaries (validate first)

Copy-paste batch for Semrush Keyword Magic Tool (exact match + related):

```
plumber website builder
website for plumbers
plumbing website design
plumbing website cost
how much does a plumbing website cost
done for you plumber website
preview plumbing website before paying
plumbing website template
plumbing website examples
best plumber website builder
best website builder for plumbers
how to build a plumbing website
what pages should a plumbing website have
plumbing website features
plumber website builder vs wix
ai plumbing website builder
plumbing website checklist
is a website worth it for plumbers
click to call plumber website
wordpress for plumbing business
google business profile for plumbers
local seo for plumbing company
seo for plumbing business
how to get more plumbing customers
plumberswebsites.com
```

**Combined-volume rule:** After export, group variants (e.g. *plumber website builder* + *website builder for plumbers*) only when Semrush shows **same SERP** in a manual spot-check — do not sum unrelated intents.

---

## 3. Competitor domains — gap analysis

Run **Domain Organic Keywords** or **Keyword Gap** (your site vs competitors) for US:

| Domain | Why |
|--------|-----|
| `plumberswebsites.com` | Baseline (GSC + Semrush when connected) |
| `growlocal.build` | Trade builder + content |
| `getsiimple.com` | Product landing competitor |
| `elmsite.com` | Comparison + product |
| `www.zarla.com` | Comparison guide |
| `www.flashcrafter.ai` | Comparison guide |
| `websitebuilderreport.com` | Editorial comparison |
| `www.wix.com` | Blog: plumbing website, cost, how-to |
| `www.butternut.ai` | AI builder SERP presence |
| `mixo.io` | AI plumber builder landing |

**Filter gap results to:**

- Keyword contains: `website`, `web design`, `website builder`, `site builder`, `web site`
- AND NOT: `near me`, `emergency`, city names (use Semrush exclude list)
- Intent label **Commercial** or **Informational** with SERP = guides/comparisons/products

---

## 4. List B promotion criteria

Promote a List B keyword to List A only when **all** pass:

1. **US volume** ≥ threshold you set (suggest: **≥ 50/mo** for Tier 2+, **≥ 20/mo** for long-tail Tier 1) — adjust after first export.  
2. **SERP check:** Top 5 results are product pages, comparisons, or owner guides — **not** local pack / homeowner hire intent.  
3. **Distinct intent:** Not coverable as H2 on an existing List A URL.  
4. **Product honesty:** Page does not require unverified features.

---

## 5. Google Keyword Planner (optional supplement)

Use **same seeds** with location **United States**, language English.  
Planner gives ranges — record as `GKP range low-high` with date; treat as directional only.

---

## 6. Google Search Console (if available)

Pull 16 months **Queries** for `plumberswebsites.com`:

- Filter queries containing `website`, `builder`, `plumb`
- Exclude queries with city names or `near me`
- Use impressions/clicks to **re-rank List A** where you already earn visibility

---

## 7. Deliverables after validation

1. Merge volumes into a **new column** on `qualified-keyword-opportunities.csv` (Phase 1D or manual update — do not overwrite Phase 1C archive).  
2. Move promoted List B rows → List A; demote List A clusters with zero volume **and** weak SERP to List B or C.  
3. Re-run content roadmap Wave order based on **volume × commercial fit**, not provisional 1B scores.

---

## 8. What we are not doing

- Treating low KD as “easy rank”  
- Importing plumberseo.net-style **homeowner local** keyword dumps without intent filters  
- Creating city × service pages from gap exports
