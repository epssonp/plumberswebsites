# Phase 1K — Keyword Coverage Snapshot

Audit of **Phase 1D target phrases** (52 registry entries → **51 unique phrases**) against **planned Academy article titles** (`master-article-inventory.csv`, 300 rows) and **live commercial `<title>` + H1** text only (`index.html`, `features/index.html`).

## Headline numbers

| Metric | Value |
|--------|------:|
| Original keyword registry entries | 52 |
| Unique target phrases (deduped) | 51 |
| Unique phrases with ≥1 relevant **Academy** title (exact or variant) | 47 |
| Unique phrases with ≥1 **commercial** title/H1 match (exact or variant) | 5 |
| Unique phrases covered by **either** Academy or commercial titles | 49 |
| **Not covered** (no title/H1 match) | 2 |
| **Weakly covered** (intent or variant-only / navigational risk) | 8 |
| **Commercial-page owned** (by design, little/no Academy title) | 2 |
| Total **exact** phrase hits across all 300 Academy titles | 20 |
| Phrases with **0** exact title hits (Academy + commercial combined) | 30 |
| Phrases with **1** exact title hit | 18 |
| Phrases with **2** exact title hits | 2 |
| Phrases with **3+** exact title hits | 1 |

## Ten strongest coverage results

1. **plumber website builder** — Academy exact 1, variant 2; commercial exact 2. (US volume: >100; third-party estimate)
2. **plumbing website features** — Academy exact 1, variant 1; commercial exact 1. (US volume: <100; third-party estimate)
3. **seo for plumbing business** — Academy exact 1, variant 2; commercial exact 0. (US volume: <100; third-party estimate)
4. **google business profile for plumbers** — Academy exact 1, variant 1; commercial exact 0. (US volume: <100; third-party estimate)
5. **plumbing website cost** — Academy exact 1, variant 1; commercial exact 0. (US volume: <100; third-party estimate)
6. **best plumber website builder** — Academy exact 1, variant 0; commercial exact 0. (No data returned; unavailable)
7. **free plumbing website** — Academy exact 1, variant 0; commercial exact 0. (No data returned; unavailable)
8. **how to build a plumbing website** — Academy exact 1, variant 0; commercial exact 0. (US volume: >100; third-party estimate)
9. **how to get more plumbing customers** — Academy exact 1, variant 0; commercial exact 0. (US volume: <100; third-party estimate)
10. **is a website worth it for plumbers** — Academy exact 1, variant 0; commercial exact 0. (No data returned; unavailable)

## Ten most important gaps

1. **best plumbing websites** — Weakly covered. Academy exact/variant: 1/0. Commercial: 0/0. Validate SERP intent; tighten title toward exact phrase only if content truly matches query.
2. **website for plumbers** — Not covered. Academy exact/variant: 0/0. Commercial: 0/0. Confirm whether a commercial H2/FAQ mention is enough before new URL.
3. **try plumbing website free** — Not covered. Academy exact/variant: 0/0. Commercial: 0/0. Confirm whether a commercial H2/FAQ mention is enough before new URL.
4. **plumberswebsites.com** — Weakly covered. Academy exact/variant: 0/0. Commercial: 2/0. Validate SERP intent; tighten title toward exact phrase only if content truly matches query.
5. **plumber website builder vs wix** — Weakly covered (comparison pillar title only — H2 subtopic). Academy exact/variant: 0/1. Commercial: 0/0. Proceed with planned article; title already aligned.
6. **ai plumbing website builder** — Weakly covered (comparison pillar title only — H2 subtopic). Academy exact/variant: 0/2. Commercial: 0/0. Proceed with planned article; title already aligned.
7. **wordpress for plumbing business** — Weakly covered (comparison pillar title only — H2 subtopic). Academy exact/variant: 0/1. Commercial: 0/0. Proceed with planned article; title already aligned.
8. **housecall pro website** — Weakly covered. Academy exact/variant: 0/1. Commercial: 0/0. Validate SERP intent; tighten title toward exact phrase only if content truly matches query.
9. **jobber website for plumbers** — Weakly covered. Academy exact/variant: 0/1. Commercial: 0/0. Validate SERP intent; tighten title toward exact phrase only if content truly matches query.
10. **service titan website for plumbers** — Weakly covered. Academy exact/variant: 0/1. Commercial: 0/0. Validate SERP intent; tighten title toward exact phrase only if content truly matches query.

## Candid assessment

The **website / local growth keyword set** is largely reflected in planned Category 4–5 article titles (GBP, local SEO, builders, cost, conversion). High-priority commercial head terms (`plumber website builder`, `plumbing website design`, template/examples/cost) are **assigned to commercial surfaces** by Phase 1E; the Academy plan adds educational and comparison titles without trying to repeat every exact phrase 300 times.

**Gaps that matter most** are usually (a) **homepage-supporting** phrases still missing from `<title>`/H1 (`website for plumbers`, `try plumbing website free`), (b) **comparison subtopics** living only as H2s inside A201 (Wix/WordPress/AI exact phrases absent from any title), and (c) **navigational/CRM** queries where a single roundup title (A208) is only a partial fit. Supporting copy for several homepage phrases exists in meta/body but was **out of scope** for this title-only audit.

Title coverage is a **useful planning diagnostic**, not a ranking guarantee. Competing in Google still depends on content quality, SERP intent fit (especially ambiguous queries like `best plumbing websites`), internal linking, and validated volume—not repeating keywords across dozens of titles.

Full per-keyword rows: `target-keyword-title-counts.csv`.
