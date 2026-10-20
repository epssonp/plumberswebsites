# Phase 1F — Category review README

## Purpose

Phase 1F reviews the **six top-level PlumbersWebsites Academy categories** (titles and descriptions only) before subcategory design or a ~300-article master TOC.

## Method

1. **Locate current copy** in the repository and on the live site (if any).  
2. **Apply Phase 1C–1E evidence** — qualified clusters, Ahrefs Free US **volume bands** (2026-10-18), and explicit “no data returned” states.  
3. **Per category:** scope, title/description critique, keyword allocation at the correct hierarchy level (title vs description vs subcategory vs article vs nowhere).  
4. **System review:** navigation clarity, overlap, commercial cannibalisation vs Phase 1E map.  
5. **Category 5:** adopt the **approved** working title and description from the Phase 1F brief as the quality bar.

## Evidence limitations

- Ahrefs Free bands (`>100`, `<100`) are **not** average monthly search volumes.  
- Missing Ahrefs exact-match rows = **no data returned**, not zero searches.  
- No numeric volumes are stored in Phase 1F CSVs unless a future Semrush export adds them.  
- Categories **1, 2, 3, and 6** have thin or no Phase 1D validation — gaps are called out, not filled with invented metrics.

## Files created

| File | Contents |
|------|----------|
| `PHASE1F-CATEGORY-TITLE-DESCRIPTION-REVIEW.md` | Full analysis and recommendations |
| `category-title-description-decisions.csv` | One row per category — current vs recommended |
| `category-keyword-allocation.csv` | Keywords → category + hierarchy level |
| `generate_phase1f_deliverables.py` | Regenerate the two CSVs |

## What this feeds next

**Subcategory review (Phase 1G or equivalent):** Use `recommended_hierarchy_level` in `category-keyword-allocation.csv` to assign phrases to subcategory hubs without promoting article-level terms (e.g. `best plumber website builder`) to category titles.

**Article TOC:** Only after category + subcategory approval; initial Cat 5 articles remain as defined in `research/phase1e/academy-initial-topic-map.csv`.

## Regeneration

```bash
python research/phase1f-category-review/generate_phase1f_deliverables.py
```

## Preservation

Phase 1C, Phase 1D, and Phase 1E source files are **read-only** for this phase. All Phase 1F output lives under `research/phase1f-category-review/` only.
