# Phase 1G — Subcategory architecture README

## Purpose

Define **24 Academy subcategories** (titles, descriptions, keyword allocation, ~300-article planning split) under the **six approved Phase 1F parent categories**, before any article-level master TOC.

## Method

1. Read Phase 1C–1F research (qualified clusters, Phase 1D Ahrefs **bands**, Phase 1E commercial map, Phase 1F category decisions).
2. Propose subcategories **across all six categories together** — not in isolation.
3. Assign keywords to **subcategory vs article vs commercial** levels with explicit evidence labels.
4. Preserve commercial ownership (homepage, Features, homepage sections).
5. Generate CSVs from `subcategory_data.py` and run `validate_phase1g_subcategories.py`.

## Evidence labels

| Label | Meaning |
|-------|---------|
| `tool_volume_band` | Ahrefs Free US band (`>100` / `<100`) — **not** exact monthly volume |
| `no_exact_match_returned` | Tool returned no exact row — **not** zero volume |
| `unverified_candidate` | Topic map / List B — volume not established |
| `intent_hypothesis` | Scope-fit only; no volume evidence in repo |
| `serp_observed` | Phase 1C SERP notes |
| `numeric_volume_verified` | *(none in Phase 1G — reserved for future Semrush)* |

## Files

| File | Role |
|------|------|
| `PHASE1G-SUBCATEGORY-ARCHITECTURE.md` | Full narrative architecture |
| `subcategory-master.csv` | 24 subcategory rows |
| `subcategory-keyword-allocation.csv` | Keyword → subcategory mapping |
| `PHASE1G-SUBCATEGORY-VALIDATION-REPORT.md` | Auto-generated checks |
| `subcategory_data.py` | Source of truth for regeneration |
| `generate_phase1g_deliverables.py` | Build CSVs |
| `validate_phase1g_subcategories.py` | QA + report |

## Workflow

```bash
python research/phase1g-subcategory-review/generate_phase1g_deliverables.py
python research/phase1g-subcategory-review/validate_phase1g_subcategories.py
```

## Next step after approval

Article-level TOC (Phase 1H or equivalent) using subcategory IDs `SC01`–`SC24` and Phase 1E initial wave for Category 5.

## Preservation

Do not overwrite Phase 1C–1F directories. Phase 1G output stays under `research/phase1g-subcategory-review/` only.
