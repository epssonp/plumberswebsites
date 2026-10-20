# Phase 1B — Ranked Master Keyword Opportunity List

**Site:** PlumbersWebsites.com  
**Market:** United States  
**Date:** 2026-10-18  
**Ranking type:** **Provisional, evidence-based priority ranking** — not a prediction of Google rankings or traffic.

Phase 1 source files are unchanged. This phase adds ranked outputs only.

---

## Executive summary

We ranked **130 keyword opportunities** from the Phase 1 registry (171 non-excluded rows). **41 registry rows** sit below tier score floors or beyond the cap and are **deferred** (see § Deferred / rejected).

**What to tackle first**

1. **Protect and strengthen commercial ownership** — homepage for **plumber website builder**; `/features/` for inclusion/design/structure; `#pricing`, `#design`, `#business` for cost, preview, and designs.  
2. **Publish two consideration-stage Academy pillars** — **best plumber website builder** (comparison) and **plumbing website cost** (TCO guide linked from pricing).  
3. **Publish one education flagship** — **how to build a plumbing website** (links to Features + app; does not target head term as H1).  
4. **Only then** expand comparison spokes (Wix, AI builders, WordPress) and Tier 3 pillars (GBP, local SEO, leads) with **SERP validation** on each.

**Distinct pages the research justifies now**

| Layer | Count | Notes |
|-------|------:|-------|
| URLs referenced in top-130 ranked list | **26** | Many keywords share one URL |
| Primary intent owners (target_role = primary) | **21** | One principal query per page |
| Credible total page roadmap (incl. deferred pillars/spokes) | **~55–72** | See `page-and-linking-map.md` |
| **Not justified:** 130 separate URLs for 130 keywords | — | By design |

**Principal keyword:** Homepage retains **“Plumber Website Builder.”** Features explains product depth; it must **not** use that phrase as primary H1/title.

---

## Scoring methodology (transparent, no invented metrics)

Each opportunity receives a **priority_score** (rough band **33–95** in this run). Components:

| Factor | Weight (approx.) | Rationale |
|--------|------------------|-----------|
| Tier | 40 / 28 / 16 | Buying intent weighted heavily (Tier 1 > 2 > 3) |
| Buying strength | 0–15 | high / medium-high / medium from Phase 1 |
| Commercial relevance | 0–10 | critical / high from registry |
| Confidence | 2–8 | SERP observation quality |
| Registry priority | 2–12 | P0–P3 from Phase 1 |
| SERP / competitor evidence | 0–7 | Documented URLs or SERP notes |
| Existing page leverage | +3 | Improve existing commercial URL first |
| Tier 3 pillar clusters | +6 | GBP, owner SEO, leads pillars only |
| Tier 3 non-website phrasing | −4 | Reduces noisy marketing long-tail |

**Tier score floors** (must pass to enter ranked list):

- Tier 1: **≥ 40**
- Tier 2: **≥ 38**
- Tier 3: **≥ 33**

**Sort order:** All Tier 1 opportunities first (by score), then Tier 2, then Tier 3 — so business-growth topics **cannot displace** direct commercial terms in rank order.

**Not used:** search volume, keyword difficulty, traffic forecasts (no reliable source).

Regenerate: `python research/generate_phase1b_ranking.py` → `ranked-keyword-opportunities.csv`

---

## Ranked priority list (summary)

Full sortable data: **`ranked-keyword-opportunities.csv`**.

### Tier 1 — Direct buying intent (ranks 1–19)

| Rank | Keyword | Score | Primary page | Role |
|-----:|---------|------:|--------------|------|
| 1 | plumber website builder | 95 | `/` | **Primary** — site-wide commercial anchor |
| 2 | plumberswebsites.com | 85 | `/` | Primary (navigational) |
| 3 | website for plumbers | 82 | `/` | Supporting on homepage |
| 4 | plumbing website cost | 80 | `/#pricing` + Academy cost guide | Primary (split: commercial + research) |
| 5 | plumbing website design | 79 | `/features/` | Primary |
| 6–7 | create plumbing business website; done for you plumber website | 76 | `/` | Supporting |
| 8–10 | preview / template / plumbers websites preview | 76 | `#design`, `#business` | Primary / supporting |
| 11–19 | examples, free/affordable/pricing variants | 65–69 | Homepage sections / FAQ | Mostly supporting — **one URL each section** |

**Why rank 1 beats rank 20:** Head term combines highest tier weight, critical relevance, P0 registry priority, and direct product fit. Free/cheap variants rank lower: still commercial but require **honest preview-before-pay** messaging (not fake “free forever”).

### Tier 2 — Website research (ranks 20–103)

**Highest-value (20–35):**

| Rank | Keyword | Primary URL (proposed unless noted) |
|-----:|---------|-------------------------------------|
| 20 | best plumber website builder | `/academy/best-plumber-website-builder/` |
| 22 | how to build a plumbing website | `/academy/how-to-build-a-plumbing-website/` |
| 23–24 | plumbing website features; what pages should a plumbing website have | **`/features/`** (existing) |
| 21 | ai plumbing website builder | `/academy/ai-plumbing-website-builder/` |
| 25+ | five-page structure, comparisons, checklist, conversion, hosting, examples | Features or Academy owners |

**Why comparison ranks above Wix spoke:** Broader consideration intent; Wix spoke is valuable but **narrower** — implement after pillar exists.

**Combine, don’t split:** `plumber website builder vs squarespace`, `yola plumber website`, `godaddy website for plumbing business` → sections or spokes under **comparison pillar**, not 8 standalone pages at launch.

### Tier 3 — Business growth (ranks 104–130)

| Rank band | Focus | Primary owners |
|-----------|--------|----------------|
| 104–107 | Website ↔ Google (GBP, indexing) | SEO pillar + GBP guide |
| 108–130 | Local SEO, leads, marketing, trust | `/academy/local-seo-plumbing-company/`, `/academy/get-more-plumbing-customers/`, etc. |

**Guardrail:** Queries like **plumber seo** rank here but SERPs may mix homeowner tactics — **validate SERP** before writing; frame as **owner education** only.

---

## Highest-value commercial opportunities (shortlist)

1. **Plumber website builder** — homepage; already positioned; optimize on-page sections and proof, not new URL.  
2. **Website for plumbers / DFY / preview** — same homepage + `#design`; differentiation vs AI builders.  
3. **Plumbing website design & features** — `/features/`; expand only where it adds decision value.  
4. **Plumbing website cost** — `#pricing` + **Academy TCO guide** (Wix competes here today).  
5. **Best plumber website builder** — Academy comparison (ElmSite/Zarla/FlashCrafter/WBR pattern).  
6. **How to build + page structure** — Academy guide + Features cross-link.  
7. **Templates / examples** — `#business` + examples Academy + live Proton link.

---

## Major competitive gaps (from Phase 1 + 1B)

| Gap | Who ranks today | Our credible angle |
|-----|-----------------|-------------------|
| Comparison + criteria tables | Zarla, ElmSite, FlashCrafter, WBR | Transparent comparison including **preview-before-pay**, five-page trade set, live subdomain |
| Plumbing website cost | Wix blog, agencies | Honest TCO: DIY time vs done-for-you vs agency |
| How-to + page list | Wix, trade blogs | Concrete five-page model tied to **Features** |
| AI builder buzz | Butternut, Replit, Meku | **Business-input personalization**, not generic prompt sites |
| CRM bundled sites | Grow Local, Zarla | CRM vs dedicated site (defer until fact-checked) |

---

## Keywords on the same page (examples)

| Page | Primary keyword | Supporting variations (no separate URL) |
|------|-----------------|----------------------------------------|
| `/` | plumber website builder | website for plumbers, create plumbing business website, done for you plumber website, plumber website service |
| `/#pricing` | plumbing website cost | cheap/affordable/packages/pricing phrasing |
| `/#design` | preview plumbing website before paying | plumbers websites preview |
| `/features/` | plumbing website design | plumbing website features, what pages should a plumbing website have, five page plumber website |
| Comparison Academy | best plumber website builder | best website builder for plumbers; many TR-16 brand long-tails as H2 sections |
| Cost Academy | (research intent for cost) | how much does a plumbing website cost — anchor on guide; homepage pricing for buyers |

---

## Supporting-content strategy (high-level)

| Commercial page | Supporting articles (distinct user needs) |
|-------------------|-------------------------------------------|
| Homepage | Comparison pillar, cost guide, how-to build, worth-it guide |
| `/features/` | How-to build, page-structure section, conversion hub, examples hub |
| Comparison pillar | Cost guide, AI builders, WordPress, CRM vs site, templates explainer |
| `#pricing` | Cost guide only (deep TCO) |

**Rules:** No link-only articles; no exact-match anchor spam; Features and homepage receive **contextual** links when the reader’s question naturally turns to “what’s included” or “start preview.”

---

## Data limitations

- No Semrush, Keyword Planner, or GSC — **volume and KD columns empty** (`not_collected`).  
- Tier 3 ranks **104–130** are **provisional** until SERP confirms **business-owner** intent.  
- Scores are **ordinal** (who goes first), not calibrated to traffic.

### Data that would most improve prioritisation

1. **US Semrush** (or Ahrefs) export — volume + KD for ranks 1–50 keywords.  
2. **GSC** — which queries already show impressions for plumberswebsites.com.  
3. **SERP spot-check batch** — top 30 Tier 3 keywords for local-pack / homeowner contamination.  
4. **Conversion data** — which pages lead to app sign-in (when available).

---

## Deferred, combined, or rejected

| Action | Items |
|--------|--------|
| **Deferred** (41 registry rows below floor or rank >130) | Low-score Tier 3 marketing fluff (chatbot, GTM, franchise requirements, Nextdoor, etc.); see `generate_phase1b_ranking.py` `DEFER_KEYWORDS` |
| **Combined** | Squarespace vs Wix vs GoDaddy → comparison pillar/spokes; site-structure long-tails → Features + how-to guide |
| **Rejected** | All `EX_*` clusters in `exclusion-report.csv`; city×plumber matrices |
| **Do not implement as separate SEO pages** | Supporting_variation rows in CSV — cover in copy, not new URLs |

---

## Recommended next steps

1. Review **`ranked-keyword-opportunities.csv`** — filter `target_role = primary` for backlog.  
2. Approve **`priority-content-roadmap.md`** sequence before Academy TOC.  
3. Import volume data when available; **re-run** `generate_phase1b_ranking.py` (adjust weights if needed).  
4. SERP-validate Tier 3 ranks 104–130 before writing.

---

## Final decisions (required answers)

1. **Tackle first:** Homepage/pricing/features refinements → comparison pillar → cost guide → how-to build → Wix/AI spokes → GBP/local SEO/leads pillars.  
2. **Distinct pages justified:** **~55–72** over full roadmap; **26 URLs** carry the top-130 keyword map; **21** primary intents.  
3. **Keywords together:** See table above + `cannibal_group` in Phase 1 registry.  
4. **Internal links to commercial pages:** Comparison, cost, how-to, worth-it → homepage; how-to, examples, conversion → Features; GBP/local SEO/leads → homepage (soft CTA).  
5. **Better data:** Semrush US + GSC + SERP validation for Tier 3.  
6. **Defer/combine/reject:** Deferred list in script; combine platform comparisons; reject homeowner/geo matrices.
