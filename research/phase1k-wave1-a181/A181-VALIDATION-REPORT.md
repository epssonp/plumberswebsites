# A181 — Validation report

**Date:** 2026-10-18 (local implementation)

## Automated / script checks

| Check | Result |
|-------|--------|
| Article file exists at `academy/how-to-build-a-plumbing-website/index.html` | Pass |
| Canonical matches planned URL | Pass |
| No `href` to unpublished article slugs (A200/A201/A219/A185) | Pass |
| Internal paths resolve to existing files (features, subcategories, homepage fragments) | Pass |
| `publishedArticles` in `academy-data.js` includes A181 with `status: published` | Pass |
| Subcategory SC18 lists clickable published guide | Pass |
| `master-article-inventory.csv` A181 status `published` | Pass |

## Manual review

| Check | Result |
|-------|--------|
| HTML title, meta description, H1 aligned with informational query | Pass |
| Breadcrumb links match Academy hierarchy | Pass |
| Article-end CTA → `https://app.plumberswebsites.com/sign-in` | Pass |
| Commercial pages unchanged in git diff (index, features/index, designs/index) | Pass (not in diff) |
| Legal drafts not exposed | Pass (no legal dir changes) |

## Academy search / browse

- `academy.js` indexes `publishedArticles` when query or category filter active.
- **Expected:** Searching “build plumbing website” on `/academy/` returns Guide result for A181 after page load.
- **Note:** Default idle message still mentions guides “when available”; results appear once user searches or filters category 5.

## Not run in this session

- Live HTTP server browser test (recommend local static server open URL).
- Lighthouse / mobile overflow pixel audit (CSS uses max-width 720px and standard prose — low overflow risk).
- Production deploy verification (explicitly out of scope until commit/push approved).

## Remaining issues

1. **`generate-academy-pages.py`** still renders all subcategory items as Planned if regenerated — manual SC18 edit would be overwritten unless generator is enhanced to read `published` status from CSV.
2. **`datePublished`** omitted from Article schema — add when publish policy is fixed.
3. **SERP re-validation** not performed in this session.
4. **Inbound links** from homepage/Features to A181 not added (out of scope; Phase 1E commercial→Academy table is future work).

## Git

- **Do not commit/push** per task instructions unless user approves publish.
