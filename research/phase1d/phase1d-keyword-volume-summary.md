# Phase 1D — US keyword volume validation summary

**Audit date:** 2026-10-18  
**Market:** United States, English  
**Phase 1C files:** Preserved unchanged in `research/`

---

## 1. Tools and data sources actually used

| Source | Used? | Result |
|--------|-------|--------|
| **Semrush** (Keyword Overview, US) | Attempted | Page loads at `semrush.com/analytics/keywordoverview/?db=us` but **national metrics require login** — no volume exported |
| **Ahrefs** (paid / API) | No | No subscription or API key in environment |
| **Ahrefs Free Keyword Generator** (US) | **Yes** | Browser retrieval **2026-10-18** — see `ahrefs_free_us_2026-10-18.json` |
| **Google Keyword Planner** | No | No Google Ads account / API configured |
| **Google Search Console** | No | Not connected in this workspace |
| **Web search / SERP** | Supplemental | Intent ambiguity note for `website for plumbers` (Ahrefs KD SERP sample showed local hire-a-plumber results) |

**Critical limitation:** Ahrefs Free shows **US volume bands** (`>100`, `<100`) from clickstream-based estimates — **not** the exact average monthly Google search volume Semrush/GKP report. Those bands are recorded as **`volume_type = third-party estimate`** with **`verification_status = Band only — not exact volume`**. We did **not** invent numeric monthly averages.

---

## 2. Counts

| Metric | Count |
|--------|------:|
| Total entries audited | **52** |
| Unique keyword strings | **51** (`click to call plumber website` duplicated at entries **18** and **31**) |
| Entries with Ahrefs **exact-match** band | **16** |
| Entries with **>100** band (exact match) | **6** |
| Entries with **<100** band (exact match) | **10** |
| Entries with **no Ahrefs exact-match** / zero ideas | **35** |
| Entries with **verified exact US monthly volume** (numeric) | **0** |
| Semrush numeric volume | **0** |

---

## 3. Highest-volume signals (Ahrefs US bands only — not comparable to exact counts)

Only keywords with exact-match **`>100`** band:

1. plumber website builder  
2. plumbing website design  
3. plumbing website template  
4. plumbing website examples  
5. how to build a plumbing website  
6. best plumbing websites  

**Do not rank these by precise traffic** — bands are ordinal (more than 100 vs less than 100), not calibrated to each other beyond that threshold.

---

## 4. Strongest commercial-intent keywords (evidence-based)

Combining **product fit (Phase 1C)** + **Ahrefs band when present**:

| Keyword | Volume band | Why it matters |
|---------|-------------|----------------|
| **plumber website builder** | >100 | Homepage owner; builder purchase intent |
| **plumbing website design** | >100 | Features / design purchase research |
| **how to build a plumbing website** | >100 | Consideration funnel → Academy + preview CTA |
| **plumbing website template** | >100 | Design gallery / template vs DFY |
| **plumbing website examples** | >100 | Examples hub + live proof |
| **plumbing website cost** | <100 | Still high commercial value; PAA competitor content exists |

Keywords with **no Ahrefs row** but **high strategic value** (validate in Semrush next):  
`best plumber website builder`, `best website builder for plumbers` (suggested alternate seed), `plumber website builder vs wix`, `ai plumbing website builder`.

---

## 5. Volume but weaker or ambiguous product fit

| Keyword | Band | Issue |
|---------|------|--------|
| **best plumbing websites** | >100 | Inspiration / portfolio intent; may include consumers or mixed SERP |
| **housecall pro website** | <100 | Often **product/navigational** to Housecall Pro, not a new builder purchase |
| **how to get more plumbing customers** | <100 | General marketing; noisy SERP |
| **seo for plumbing business** | <100 | Owner SEO vs homeowner SEO tactics — framing risk |

---

## 6. Low volume but still useful commercially

| Keyword | Band | Use |
|---------|------|-----|
| plumbing website features | <100 | Supporting copy on `/features/` |
| plumbing website cost | <100 | `#pricing` + TCO guide |
| google business profile for plumbers | <100 | Tier 3 pillar after SERP check |
| plumbing website hosting | <100 | Section in hosting guide only |

---

## 7. Tool disagreements

Only **one** tool contributed volume bands (Ahrefs Free). Semrush was **not** available for numeric comparison. **No cross-tool disagreement table** is possible until Semrush or GKP export is supplied.

---

## 8. Limitations and next steps

1. **Import Semrush US Keyword Overview CSV** for all 51 unique strings (and variant `best website builder for plumbers` for entry 11).  
2. **Google Keyword Planner** ranges for the same seeds — store as `volume_type = range`.  
3. **GSC** query report for any impressions on brand and head terms.  
4. Re-run `generate_phase1d_deliverables.py` after merging a `semrush_us_*.json` sidecar (future script extension).  
5. **Do not** treat Ahrefs `>100` as “at least 101 visits/month to our site.”

---

## 9. Files produced

| File | Purpose |
|------|---------|
| `phase1d-keyword-volume-audit.csv` | 52-row audit |
| `phase1d-keyword-priorities.csv` | Recommended actions |
| `ahrefs_free_us_2026-10-18.json` | Raw Ahrefs free pulls |
| `entries.json` | Entry list with duplicate flag |
| `generate_phase1d_deliverables.py` | Regenerate CSVs |
