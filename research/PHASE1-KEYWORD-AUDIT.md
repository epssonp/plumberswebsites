# Phase 1 — Keyword Opportunity Discovery Audit  
**Site:** [PlumbersWebsites.com](https://plumberswebsites.com/)  
**Market:** United States  
**Audit date:** 2026-10-18  
**Status:** Research only — no live site or Academy implementation in this phase.

---

## 1. Executive summary

### Commercial objective alignment

PlumbersWebsites.com sells a **done-for-you, personalized five-page plumbing website** with **six designs** and **preview before payment**. The homepage correctly anchors on **“Plumber Website Builder”** (H1/title/canonical). The Features page (`/features/`) should support **inclusion / design / structure** intent without competing for the head term.

### Strongest opportunities (evidence: SERP composition + competitor landscape)

1. **Head term cluster — “plumber website builder” (Tier 1, P0)**  
   Google US results mix **trade-specific builders** (Siimple, Grow Local, Instantsite), **generic AI builders** (Butternut, Replit, Meku), **comparison content** (ElmSite, Zarla, FlashCrafter, Website Builder Report), and **forums**. Few results match your exact model: **structured five-page trade site + real business inputs + preview-before-pay**. Differentiation is narrative and proof (live subdomain example), not keyword density.

2. **Cost / pricing intent (Tier 1–2, P1)**  
   PAA-style questions on the head SERP point to **“plumbing website cost”** and **professional website cost**. Wix publishes a dedicated plumbing cost article — strong content competitor. Your homepage pricing section can anchor commercial intent; an Academy **total-cost guide** (builder vs DIY time vs agency) fills research intent without undercutting honesty.

3. **“Best website builder for plumbers” comparisons (Tier 2, P1)**  
   Multiple refreshed **2026 comparison guides** (Zarla, ElmSite, FlashCrafter, Website Builder Report) rank with structured criteria (booking, mobile, SEO, price). A **fact-checked, transparent comparison** (including where DIY wins) is credible for your audience and supports consideration-stage traffic.

4. **How-to build / site structure (Tier 2, P1)**  
   Wix, trade blogs, and software vendors rank **how to build a plumbing website** and **what pages to include**. Your product *is* a concrete answer (Home, Services, Our Approach, About, Contact). Features page plus one **flagship guide** can own this intent with minimal overlap with the homepage if the guide is educational and the homepage stays transactional.

5. **Preview-before-pay / DFY (Tier 1, P1)**  
   Competitors emphasize AI speed, CRM, or low monthly price. Your verified journey (**enter details → pick design → preview**) is a distinct commercial story for queries around **done-for-you**, **website for plumbers**, and preview-oriented long-tail.

### Secondary (Tier 3) opportunities — with guardrails

- **Google Business Profile** and **local SEO for plumbing companies** are high relevance for owners, but SERPs often blend **agency offers** and **homeowner-ranking tactics**. Content must speak to **business owners** optimizing their *company’s* visibility, not “rank for emergency plumber near me.”
- **Lead gen / marketing ideas** clusters are large but **noisier** commercially. Use as **supporting pillars** that naturally recommend an owned website as the hub.

### Scale answer (final audit question)

**What is the largest credible set of distinct, worthwhile opportunities?**

| Lane | Distinct intent owners (approx.) | Notes |
|------|----------------------------------|--------|
| Commercial site (existing sections + 0–2 new landings) | 6–8 | Homepage, Features, pricing, gallery, FAQ, process |
| Tier 1–2 Academy / guides | 25–40 | Comparisons, how-to, cost, examples, platform spokes |
| Tier 3 owner growth | 35–55 | GBP, local SEO, leads, marketing (SERP-validated) |
| **Total credible distinct URLs** | **~80–130** | See `page-opportunity-map.md` |

**Not credible toward 1,000 pages** under your audience rules: city×service **homeowner SEO** keyword matrices (common in trade SEO blogs), “best plumber in {city}” variants, and pure **consumer plumbing repair** topics.

### Major risks

- **Intent contamination:** Keywords containing “plumber” often mean **hire a plumber**. Every Tier 3 article needs SERP review before writing.
- **Metric gap:** Without Semrush/Keyword Planner/GSC exports, **priority is qualitative** (SERP + commercial fit), not volume-driven.
- **Competitive SERPs:** Head and comparison terms are **content-heavy and affiliate-heavy**; winning requires **original criteria, verified product facts, and live examples** — not thin SEO pages.

---

## 2. Deliverable index

| # | Deliverable | File |
|---|-------------|------|
| 1 | Executive summary | This document §1 |
| 2 | Master keyword registry | `keyword-opportunity-registry.csv` (191 rows; regenerate via `generate_keyword_registry.py`) |
| 3 | Keyword clusters | `keyword-clusters.md` |
| 4 | Commercial shortlist | `commercial-shortlist.csv` |
| 5 | Secondary shortlist | `secondary-shortlist.csv` |
| 6 | Competitor analysis | §6 below |
| 7 | Exclusion report | `exclusion-report.csv` + §7 |
| 8 | Data gaps | §8 |
| 9 | Page-opportunity map | `page-opportunity-map.md` |

---

## 3. Current site (keyword-relevant inventory)

| URL | Role in keyword strategy |
|-----|-------------------------|
| `/` | **P0 owner** — plumber website builder; website for plumbers; DFY |
| `/features/` | **P1 owner** — plumbing website design/features; five pages; mobile |
| `/#business` | Design/template selection |
| `/#pricing` | Cost/commercial |
| `/#design` | Process / preview |
| `/#faq` | Objections, capabilities |
| `/academy.html` | Empty placeholder — **no Academy SEO yet** |
| `protonplumbing.plumberswebsites.com` | Proof asset for examples cluster |

**No Search Console or rank tracking** was available in-repo for this audit.

---

## 4. Search intent methodology

For each cluster we applied:

1. **Query wording** — Does the searcher plausibly *run* a plumbing business?
2. **SERP page types** — Product, comparison, guide, template marketplace, forum, local pack (local pack → usually exclude for content site).
3. **Competitor URL patterns** — Trade builders vs DIY vs agencies.
4. **Tier assignment** — Tier 1 buy / Tier 2 website research / Tier 3 growth / EX exclude.

**Primary SERP observation (US, 2026-10-18):** Query *plumber website builder* returned product landings (Siimple, Butternut, Instantsite), AI builders, comparison/guide URLs, Reddit, and agency service pages — **not** a single dominant brand.

---

## 5. Commercial & secondary shortlists (narrative)

### Commercial shortlist (Tier 1–2, highest priority)

See `commercial-shortlist.csv`. Head terms:

- plumber website builder *(homepage only)*
- website for plumbers / plumbing business website
- plumbing website design / features *(features page)*
- plumbing website cost / pricing / packages
- best plumber website builder / best website builder for plumbers
- how to build a plumbing website
- what pages should a plumbing website have
- plumbing website examples / templates
- done for you plumber website / preview before paying
- ai plumbing website builder *(comparison angle)*

### Secondary shortlist (Tier 3)

See `secondary-shortlist.csv`. Pillars:

- google business profile for plumbers
- local seo for plumbing company
- seo for plumbing business (owner education)
- how to get more plumbing customers / plumbing leads online
- plumbing business marketing ideas
- starting a plumbing business — website checklist

---

## 6. Competitor analysis

### Direct product competitors (trade / field-service website builders)

| Competitor | Typical ranking content | Strengths vs PW | Gaps / your angle |
|------------|-------------------------|-----------------|-------------------|
| [Grow Local](https://growlocal.build/plumber-website-builder) | Product + “best builder” blog | CRM/local marketing bundle | Your **preview-first**, five-page **trade narrative** |
| [Siimple](https://getsiimple.com/) | Product landing | Simplicity, trade focus | Emphasize **design choice + personalization table** |
| Instantsite / similar | Product | Speed | **Proof** via live customer subdomain |
| [ElmSite](https://elmsite.com/compare/best-website-builder-for-plumbers) | Comparison + product | Honest comparison format, monthly price | You can publish **similar transparency** with your model |
| [Zarla](https://www.zarla.com/guides/best-website-builder-for-plumbers) | Comparison + CRM/booking | Full funnel (CRM, bookings) | Stay honest on **unverified** features (forms delivery, booking) |
| [FlashCrafter](https://www.flashcrafter.ai/compare/best-website-builders-for-plumbers) | Long comparison table | Managed positioning | Differentiate **self-serve preview** vs managed sales process |

### DIY platform content competitors

| Competitor | Content type | Implication |
|------------|--------------|-------------|
| [Wix](https://www.wix.com/blog/how-to-make-a-plumbing-website) | How-to + templates + cost | **Must-have** comparison and how-to content to intercept research intent |
| Squarespace / WordPress ecosystem | Guides, templates | Spoke pages only — avoid duplicate intent |
| [Website Builder Report](https://websitebuilderreport.com/business/best-website-builder-for-plumbers/) | Editorial comparison | Match **criteria-based** reviews |

### AI builder entrants (SERP noise)

Butternut, Replit, Meku, Durable — rank on speed/AI. **Counter-message:** speed without **verified business inputs** and **trade-specific page set** is a different purchase.

### Agencies / marketing (Tier 3 overlap)

Relentless Digital and similar **agency service pages** rank on head terms. Optional **“agency alternatives”** content for owners who want fixed price and preview.

### Content farms / trade SEO (mostly exclusion)

Sites publishing **“1000 plumber keywords”** (e.g. plumberseo.net-style lists) target **homeowner local service rankings** — **not** your audience. Do not use those lists as Academy seeds without intent filtering.

---

## 7. Exclusion report (summary)

Full list: `exclusion-report.csv`.

| Exclusion type | Example | Reason |
|----------------|---------|--------|
| Homeowner local service | plumber near me, emergency plumber | Hire a pro, not buy a website |
| Geo traps | plumber website design tampa | Often local service or agency lead-gen |
| Consumer DIY repair | how to fix a leaky faucet | No product fit |
| Career / supply | plumber salary, plumbing supply store | Wrong audience |

**Rule:** Location keywords qualify only when the searcher is a **business owner** seeking marketing/website help — confirm with SERP, not keyword text alone.

---

## 8. Data gaps

| Missing input | Impact | Request |
|---------------|--------|---------|
| **Semrush (US) export** — keyword magic + domain gap vs growlocal, siimple, wix.com/blog | No volume, KD, CPC, or gap prioritization | CSV export: US, plumbing + website modifiers, competitor domains |
| **Google Keyword Planner** | No official volume ranges | Account access + seed list from registry Tier 1–2 |
| **Google Search Console** | No actual queries/impressions for plumberswebsites.com | Read-only user access or monthly export |
| **Rank tracking** | No baseline positions | Optional Semrush/Ahrefs project |
| **SERP API / scale** | Only spot checks performed | Manual second pass on top 30 registry P1 keywords |

**Registry convention:** Empty `us_monthly_volume`, `keyword_difficulty`, and `cpc_usd` mean **not collected** — not zero demand.

---

## 9. Cannibalization (homepage vs Features vs Academy)

| Intent | Owner |
|--------|--------|
| Plumber website builder (head) | Homepage H1/title |
| What's included / five pages / mobile / vs DIY | `/features/` |
| Best builder / vs Wix / vs AI | Academy comparison pillar |
| Plumbing website cost (research) | Academy guide; commercial on `/#pricing` |
| How to build (education) | Academy; CTA to app |

Use `cannibal_group` column in CSV when filtering.

---

## 10. Recommended next steps (post-audit, pre-implementation)

1. **Import** Semrush US export; merge into registry (preserve source column).
2. **SERP-validate** all P1 Tier 3 keywords; move misclassified rows to `EX`.
3. **Approve** page-opportunity map counts before Academy TOC.
4. **Draft** comparison pillar + cost guide first (highest research-stage leverage).
5. **Keep** homepage as single commercial owner for head term through any Academy launch.

---

## 11. Regenerating artifacts

```bash
python research/generate_keyword_registry.py
```

Outputs: `keyword-opportunity-registry.csv`, `commercial-shortlist.csv`, `secondary-shortlist.csv`, `exclusion-report.csv`.
