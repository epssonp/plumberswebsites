# Phase 1E — Commercial keyword-to-page map (summary)

**Date:** 2026-10-18  
**Planning only** — no live site or Academy content changes.  
**Sources preserved:** Phase 1C, Phase 1D (`research/phase1d/`).

---

## Verified commercial URLs (repository)

| User-facing name | Verified URL | Implementation |
|------------------|--------------|----------------|
| Homepage | `https://plumberswebsites.com/` | `index.html` — live |
| Features | `https://plumberswebsites.com/features/` | `features/index.html` — live |
| How It Works | `https://plumberswebsites.com/#design` | Section on homepage (`id=design`); nav label “How It Works” |
| Designs | `https://plumberswebsites.com/#business` | Section on homepage (`id=business`); six-design gallery |
| Pricing | `https://plumberswebsites.com/#pricing` | Section on homepage (`id=pricing`) |
| FAQ | `https://plumberswebsites.com/#faq` | Section on homepage (`id=faq`) |
| Academy (future) | `https://plumberswebsites.com/academy.html` | **Stub only** (empty file) — future `/academy/…` slugs |

**Homepage primary keyword unchanged:** `plumber website builder` (H1, title, canonical).

---

## Keyword ownership at a glance

| Page | Primary keyword | Ahrefs US band (2026-10-18) |
|------|-----------------|-----------------------------|
| Homepage | plumber website builder | >100 |
| Features | plumbing website design | >100 (features support <100) |
| How It Works | preview plumbing website before paying | No data returned |
| Designs | plumbing website template | >100 |
| Pricing | plumbing website cost | <100 |
| FAQ | (support) free / trial / product questions | No data returned for free variants |

Bands are **not** exact monthly averages — see Phase 1D summary.

---

## Initial Academy: 11 candidates → **7 standalone URLs + 4 pillar sections**

| ID | Decision |
|----|----------|
| AC-01 How to build | **Standalone** P1 |
| AC-02 Examples | **Standalone** P1 |
| AC-03 Best builder | **Standalone pillar** P1 (includes Wix, AI, WordPress as H2 until validated) |
| AC-04 Cost | **Standalone** P1 |
| AC-05 What pages | **No standalone** — expand `/features/` + section in AC-01 |
| AC-06 vs Wix | **Section in AC-03** |
| AC-07 AI builder | **Section in AC-03** |
| AC-08 Checklist | **Standalone** P2 |
| AC-09 Worth it | **Standalone** P2 |
| AC-10 WordPress | **Section in AC-03** |
| AC-11 Hosting & maintenance | **Standalone consolidated** P3 |

This keeps the first Academy wave focused and avoids near-duplicate comparison URLs.

---

## Deliverables in this folder

| File | Purpose |
|------|---------|
| `commercial-keyword-page-map.csv` | Commercial keyword ownership |
| `academy-initial-topic-map.csv` | Academy candidates and format decisions |
| `phase1e-internal-linking-plan.md` | Link graph and anchors |
| `generate_phase1e_maps.py` | Regenerate CSVs |

---

## Evidence gaps (do not invent volume)

Validate in Semrush/GKP before promoting:

- `best plumber website builder` / `best website builder for plumbers`
- `done for you plumber website`, `preview plumbing website before paying`
- `plumber website builder vs wix`, `ai plumbing website builder`
- `what pages should a plumbing website have` (standalone URL not recommended until data supports)

---

## Alignment with ~300-article / six-category plan

Initial articles seed **four** of six proposed hubs (Build, Choose builder, Cost/ROI, Design/examples, Features/maintenance). **Online visibility** hub (GBP, local SEO) remains Phase 1C Wave 3 — intentionally **not** in this initial map.

Regenerate CSVs: `python research/phase1e/generate_phase1e_maps.py`
