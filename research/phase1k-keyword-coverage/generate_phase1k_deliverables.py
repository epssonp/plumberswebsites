#!/usr/bin/env python3
"""Phase 1K — target keyword title coverage snapshot (read-only on research sources)."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"
OUT_DIR = Path(__file__).resolve().parent

VOLUME_AUDIT = RESEARCH / "phase1d" / "phase1d-keyword-volume-audit.csv"
PRIORITIES = RESEARCH / "phase1d" / "phase1d-keyword-priorities.csv"
COMMERCIAL_MAP = RESEARCH / "phase1e" / "commercial-keyword-page-map.csv"
ACADEMY_TOPICS = RESEARCH / "phase1e" / "academy-initial-topic-map.csv"
INVENTORY = RESEARCH / "phase1h-master-toc" / "master-article-inventory.csv"
INDEX_HTML = ROOT / "index.html"
FEATURES_HTML = ROOT / "features" / "index.html"

# Known research variants (Phase 1E / 1D notes) — matched only when exact phrase is absent.
EXPLICIT_VARIANTS: dict[str, list[str]] = {
    "best plumber website builder": ["best website builder for plumbers"],
    "plumber website builder vs wix": ["vs wix", "wix for plumbing"],
    "ai plumbing website builder": [
        "ai-generated plumbing websites",
        "ai plumbing websites",
        "best plumber website builder",
        "evaluating ai-generated plumbing websites",
    ],
    "wordpress for plumbing business": ["wordpress for plumbing"],
    "google business profile for plumbers": [
        "google business profile for plumbers",
        "google business profile posts",
    ],
    "click to call plumber website": ["click-to-call", "click to call"],
    "mobile friendly plumber website": ["mobile-friendly plumber", "mobile friendly plumber"],
    "plumbing website phone number placement": ["phone number placement on plumbing"],
    "how to put phone number on plumbing website": ["phone number placement on plumbing"],
    "update plumbing website business hours": ["updating business hours", "business hours and seasonal"],
    "plumber website design examples 2026": ["plumbing website examples", "plumber website design"],
    "plumbing company website inspiration": ["plumbing website examples", "strong plumbing business sites"],
    "housecall pro website": ["housecall pro"],
    "jobber website for plumbers": ["jobber"],
    "service titan website for plumbers": ["servicetitan"],
    "create plumbing business website": ["start a plumbing business website", "create a plumbing business website"],
    "website for plumbers": ["website for your plumbing business"],
    "done for you plumber website": ["done-for-you plumbing websites", "done for you plumbing"],
    "preview plumbing website before paying": ["previewing your plumbing website before you pay"],
    "free plumbing website": ["free plumbing website offers"],
    "free plumber website builder": ["free plumbing website offers"],
    "try plumbing website free": ["preview before you pay", "preview your plumbing website"],
    "plumber website service": ["plumbing website service", "plumber website builder"],
    "plumbing website design company": ["plumbing web design agency", "web design agency alternatives"],
    "what pages should a plumbing website have": [
        "what your plumbing website includes",
        "five dedicated views",
        "your five website pages",
    ],
    "plumber website builder vs wix": ["best plumber website builder"],
    "wordpress for plumbing business": ["best plumber website builder"],
    "local seo for plumbing company": ["local seo for plumbing companies"],
    "hire web designer for plumbing business": ["hire a web designer vs use a plumbing website builder"],
    "plumber website builder vs squarespace": ["squarespace vs trade builders for plumbing websites"],
    "crm website vs custom plumbing website": ["crm-bundled websites vs dedicated plumbing sites"],
    "plumber website speed": ["page speed and core web vitals for local plumbing sites"],
    "plumbing website lead capture": [
        "lead capture without aggressive popups",
        "contact page essentials for plumbing lead capture",
    ],
    "plumbing website quote form": ["quote request forms vs click-to-call for plumbers"],
    "best call to action for plumber website": ["best call-to-action patterns for plumber homepages"],
    "how to put phone number on plumbing website": ["phone number placement on plumbing websites"],
}

COMMERCIAL_PRIMARY = {
    "plumber website builder": "Homepage (primary)",
    "plumbing website design": "Features (primary)",
    "plumbing website features": "Features (title/supporting)",
    "plumbing website template": "Homepage #business (primary)",
    "plumbing website examples": "Homepage #business + Academy AC-02",
    "plumbing website cost": "Homepage #pricing (primary)",
    "preview plumbing website before paying": "Homepage #design (primary)",
    "free plumbing website": "Homepage #faq (supporting)",
    "free plumber website builder": "Homepage #faq (supporting)",
    "try plumbing website free": "Homepage #faq (supporting)",
    "website for plumbers": "Homepage (supporting)",
    "done for you plumber website": "Homepage / #design (supporting)",
    "create plumbing business website": "Homepage (supporting)",
    "plumber website service": "Homepage (supporting)",
    "what pages should a plumbing website have": "Features (primary supporting)",
}

WEAK_INTENT_KEYWORDS = {
    "plumberswebsites.com",
    "best plumbing websites",
    "housecall pro website",
    "jobber website for plumbers",
    "service titan website for plumbers",
}

CANNIBALIZATION_PAIRS = [
    ("plumber website builder", "Best Plumber Website Builder"),
    ("plumbing website design", "What 'Plumbing Website Design' Means"),
    ("plumbing website features", "Plumbing Website Features That Drive"),
    ("plumbing website cost", "How Much Does a Plumbing Website Cost"),
]


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def token_variants(token: str) -> set[str]:
    base = {token}
    if token == "plumber":
        base.update({"plumbing", "plumbers"})
    elif token == "plumbing":
        base.update({"plumber", "plumbers"})
    elif token == "plumbers":
        base.update({"plumber", "plumbing"})
    return base


STOP_TOKENS = {"a", "an", "the", "for", "to", "on", "in", "and", "or", "vs", "your", "with"}


def exact_in_text(keyword: str, text: str) -> bool:
    nk = normalize(keyword)
    nt = normalize(text)
    if not nk or not nt:
        return False
    return nk in nt


def stem(token: str) -> str:
    if len(token) > 3 and token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def token_in_text(token: str, text: str, start: int) -> int:
    """Return start index of token (with plumber/plumbing swap and simple plural) or -1."""
    candidates = set(token_variants(token))
    candidates.add(stem(token))
    for cand in sorted(candidates, key=len, reverse=True):
        idx = text.find(cand, start)
        if idx != -1:
            return idx
    return -1


def ordered_token_variant(keyword: str, text: str) -> bool:
    """Non-contiguous ordered token match with limited plumber/plumbing swaps."""
    if exact_in_text(keyword, text):
        return False
    nt = normalize(text)
    tokens = [t for t in normalize(keyword).split() if t not in STOP_TOKENS]
    # Two-token phrases are too noisy across 300 titles — explicit variants only.
    if len(tokens) < 3:
        return False
    pos = 0
    for token in tokens:
        idx = token_in_text(token, nt, pos)
        if idx == -1:
            return False
        pos = idx + len(token)
    return True


def explicit_variant(keyword: str, text: str) -> bool:
    if exact_in_text(keyword, text):
        return False
    nt = normalize(text)
    for phrase in EXPLICIT_VARIANTS.get(keyword, []):
        if normalize(phrase) in nt:
            return True
    return False


def is_variant_match(keyword: str, text: str) -> bool:
    return explicit_variant(keyword, text) or ordered_token_variant(keyword, text)


def extract_tag(html: str, tag: str) -> str:
    pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
    m = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    inner = re.sub(r"<[^>]+>", " ", m.group(1))
    return re.sub(r"\s+", " ", inner).strip()


def load_commercial_texts() -> list[tuple[str, str]]:
    texts: list[tuple[str, str]] = []
    index = INDEX_HTML.read_text(encoding="utf-8")
    features = FEATURES_HTML.read_text(encoding="utf-8")
    texts.append(("Homepage", extract_tag(index, "title")))
    hero = re.search(r'id="hero-title"[^>]*>(.*?)</h1>', index, re.S | re.I)
    if hero:
        h1 = re.sub(r"<[^>]+>", " ", hero.group(1))
        texts.append(("Homepage H1", re.sub(r"\s+", " ", h1).strip()))
    texts.append(("Features page", extract_tag(features, "title")))
    fh = re.search(r'id="features-hero-title"[^>]*>(.*?)</h1>', features, re.S | re.I)
    if fh:
        texts.append(("Features H1", re.sub(r"<[^>]+>", " ", fh.group(1)).strip()))
    return texts


@dataclass
class MatchResult:
    exact_academy: list[tuple[str, str]] = field(default_factory=list)
    variant_academy: list[tuple[str, str]] = field(default_factory=list)
    exact_commercial: list[tuple[str, str]] = field(default_factory=list)
    variant_commercial: list[tuple[str, str]] = field(default_factory=list)


def classify_keyword(
    keyword: str,
    owner: str,
    exact_a: int,
    var_a: int,
    exact_c: int,
    var_c: int,
) -> str:
    if keyword in COMMERCIAL_PRIMARY and (exact_c > 0 or var_c > 0):
        if exact_a + var_a > 0 and keyword == "plumber website builder":
            return "Commercial-page owned (Academy comparison title present — monitor cannibalization)"
        if exact_a + var_a == 0:
            return "Commercial-page owned"
        return "Covered (commercial + Academy)"
    if keyword == "plumberswebsites.com":
        return "Weakly covered" if exact_c + var_c else "Not covered"
    total = exact_a + var_a + exact_c + var_c
    if total == 0:
        return "Not covered"
    if keyword in WEAK_INTENT_KEYWORDS and var_a + exact_a <= 1:
        return "Weakly covered"
    if exact_a + var_a > 0 and var_a > 0 and exact_a == 0 and keyword not in WEAK_INTENT_KEYWORDS:
        # variant-only academy
        if any(k in keyword for k in ("housecall", "jobber", "service titan")):
            return "Weakly covered"
    if exact_a + var_a + exact_c + var_c > 0:
        if keyword in WEAK_INTENT_KEYWORDS:
            return "Weakly covered"
        if keyword in (
            "plumber website builder vs wix",
            "wordpress for plumbing business",
            "ai plumbing website builder",
        ) and exact_a == 0:
            return "Weakly covered (comparison pillar title only — H2 subtopic)"
        return "Covered"
    return "Not covered"


def recommended_action(keyword: str, classification: str, owner: str) -> str:
    if classification.startswith("Commercial-page owned"):
        if "cannibalization" in classification.lower():
            return "Keep homepage H1 as sole primary; ensure comparison article targets 'best' intent and internal links to product."
        return "No duplicate Academy primary title needed; support in body/FAQ if useful."
    if classification == "Not covered":
        if owner and "Academy" in owner:
            return "Add or retitle a planned article only if Semrush/SERP confirms intent — avoid keyword stuffing."
        if keyword in ("plumber website builder vs wix", "wordpress for plumbing business", "ai plumbing website builder"):
            return "Coverage is via A201 comparison pillar H2 sections — acceptable if sections ship with exact subheadings."
        return "Confirm whether a commercial H2/FAQ mention is enough before new URL."
    if classification == "Weakly covered":
        return "Validate SERP intent; tighten title toward exact phrase only if content truly matches query."
    if keyword == "plumbing website design":
        return "Accept split: Features owns inclusion H1; Academy educates on design term (A210) — watch overlap."
    return "Proceed with planned article; title already aligned."


def load_volume_rows() -> list[dict]:
    rows = []
    with VOLUME_AUDIT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def unique_keywords(rows: list[dict]) -> list[dict]:
    """One row per unique phrase; duplicate entries point to canonical entry_id."""
    by_phrase: dict[str, dict] = {}
    for row in rows:
        phrase = row["exact_keyword"].strip()
        dup = (row.get("duplicate_of_entry_id") or "").strip()
        if phrase not in by_phrase:
            by_phrase[phrase] = {**row, "source_entry_ids": [row["entry_id"]], "is_duplicate_entry": bool(dup)}
        else:
            by_phrase[phrase]["source_entry_ids"].append(row["entry_id"])
            if dup:
                by_phrase[phrase]["is_duplicate_entry"] = True
    return sorted(by_phrase.values(), key=lambda r: int(r["entry_id"]))


def load_articles() -> list[dict]:
    with INVENTORY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_owner_map() -> dict[str, str]:
    owners = {}
    with PRIORITIES.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            owners[row["keyword"].strip()] = row.get("intended_page", "")
    with COMMERCIAL_MAP.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pk = row["primary_keyword"].strip()
            owners.setdefault(pk, row["page_name"])
    return owners


def volume_evidence(row: dict) -> str:
    vol = (row.get("us_monthly_volume") or "").strip()
    vtype = (row.get("volume_type") or "").strip()
    status = (row.get("verification_status") or "").strip()
    parts = []
    if vol:
        parts.append(f"US volume: {vol}")
    elif status:
        parts.append(status)
    if vtype:
        parts.append(vtype)
    return "; ".join(parts) if parts else "No volume data in Phase 1D"


def main() -> None:
    volume_rows = load_volume_rows()
    keywords = unique_keywords(volume_rows)
    articles = load_articles()
    commercial = load_commercial_texts()
    owners = load_owner_map()

    assert len(volume_rows) == 52, f"Expected 52 audit entries, got {len(volume_rows)}"
    assert len(keywords) == 51, f"Expected 51 unique phrases, got {len(keywords)}"
    assert len(articles) == 300, f"Expected 300 articles, got {len(articles)}"

    results: dict[str, MatchResult] = {k["exact_keyword"]: MatchResult() for k in keywords}

    for art in articles:
        aid = art["article_id"]
        title = art["proposed_title"]
        for kw in results:
            if exact_in_text(kw, title):
                results[kw].exact_academy.append((aid, title))
            elif is_variant_match(kw, title):
                results[kw].variant_academy.append((aid, title))

    for label, text in commercial:
        for kw in results:
            if exact_in_text(kw, text):
                results[kw].exact_commercial.append((label, text[:80]))
            elif is_variant_match(kw, text):
                results[kw].variant_commercial.append((label, text[:80]))

    csv_path = OUT_DIR / "target-keyword-title-counts.csv"
    fieldnames = [
        "exact_target_phrase",
        "source_entry_ids",
        "exact_academy_title_match_count",
        "relevant_variant_academy_count",
        "matching_article_ids",
        "matching_article_titles",
        "exact_commercial_title_h1_match_count",
        "relevant_variant_commercial_count",
        "commercial_match_surfaces",
        "assigned_owner",
        "coverage_classification",
        "volume_evidence",
        "recommended_action",
        "cannibalization_notes",
    ]

    rows_out = []
    exact_total_academy = 0
    freq_buckets = defaultdict(int)

    for kw_row in keywords:
        kw = kw_row["exact_keyword"]
        r = results[kw]
        ea = len(r.exact_academy)
        va = len(r.variant_academy)
        ec = len(r.exact_commercial)
        vc = len(r.variant_commercial)
        exact_total_academy += ea

        combined_exact = ea + ec
        combined_any = ea + va + ec + vc
        freq_key = combined_exact
        if freq_key >= 3:
            bucket = "3+"
        else:
            bucket = str(freq_key)
        freq_buckets[bucket] += 1

        owner = COMMERCIAL_PRIMARY.get(kw, owners.get(kw, ""))
        classification = classify_keyword(kw, owner, ea, va, ec, vc)
        action = recommended_action(kw, classification, owner)

        cann_notes = ""
        for pk, frag in CANNIBALIZATION_PAIRS:
            if kw == pk and any(frag in t for _, t in r.exact_academy + r.variant_academy):
                cann_notes = f"Multiple surfaces target '{kw}' — coordinate primary vs comparison intent."

        ids = "|".join(sorted({x[0] for x in r.exact_academy + r.variant_academy}))
        titles = " | ".join({x[1] for x in r.exact_academy + r.variant_academy})
        comm_surf = " | ".join({x[0] for x in r.exact_commercial + r.variant_commercial})

        rows_out.append(
            {
                "exact_target_phrase": kw,
                "source_entry_ids": "|".join(kw_row["source_entry_ids"]),
                "exact_academy_title_match_count": ea,
                "relevant_variant_academy_count": va,
                "matching_article_ids": ids,
                "matching_article_titles": titles,
                "exact_commercial_title_h1_match_count": ec,
                "relevant_variant_commercial_count": vc,
                "commercial_match_surfaces": comm_surf,
                "assigned_owner": owner,
                "coverage_classification": classification,
                "volume_evidence": volume_evidence(kw_row),
                "recommended_action": action,
                "cannibalization_notes": cann_notes,
            }
        )

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    def covered_count(predicate):
        return sum(1 for row in rows_out if predicate(row))

    academy_covered = covered_count(
        lambda r: int(r["exact_academy_title_match_count"]) + int(r["relevant_variant_academy_count"]) > 0
    )
    commercial_covered = covered_count(
        lambda r: int(r["exact_commercial_title_h1_match_count"]) + int(r["relevant_variant_commercial_count"]) > 0
    )
    not_covered = covered_count(lambda r: r["coverage_classification"] == "Not covered")
    weak = covered_count(lambda r: "Weakly covered" in r["coverage_classification"])
    commercial_owned = covered_count(lambda r: r["coverage_classification"].startswith("Commercial-page owned"))

    # Strongest: sort by exact academy + variant + commercial exact
    scored = []
    for row in rows_out:
        score = (
            int(row["exact_academy_title_match_count"]) * 3
            + int(row["relevant_variant_academy_count"])
            + int(row["exact_commercial_title_h1_match_count"]) * 2
        )
        scored.append((score, row))
    scored.sort(key=lambda x: (-x[0], x[1]["exact_target_phrase"]))
    top10 = [
        s[1]
        for s in scored
        if (int(s[1]["exact_academy_title_match_count"]) > 0 or int(s[1]["exact_commercial_title_h1_match_count"]) > 0)
        and s[1]["exact_target_phrase"] not in ("plumberswebsites.com",)
        and "Weakly covered" not in s[1]["coverage_classification"]
    ][:10]

    gaps = [r for r in rows_out if r["coverage_classification"] == "Not covered"]
    gaps += [
        r
        for r in rows_out
        if "Weakly covered" in r["coverage_classification"]
        and r not in gaps
    ]
    # prioritize gaps with volume >100 or critical commercial
    def gap_priority(r):
        vol = r["volume_evidence"]
        pri = 0
        if ">100" in vol:
            pri += 10
        if r["coverage_classification"] == "Not covered":
            pri += 5
        return -pri

    gaps.sort(key=gap_priority)
    top_gaps = gaps[:10]

    md_path = OUT_DIR / "PHASE1K-KEYWORD-COVERAGE-SNAPSHOT.md"
    val_path = OUT_DIR / "PHASE1K-VALIDATION-REPORT.md"

    combined_covered = covered_count(
        lambda r: int(r["exact_academy_title_match_count"])
        + int(r["relevant_variant_academy_count"])
        + int(r["exact_commercial_title_h1_match_count"])
        + int(r["relevant_variant_commercial_count"])
        > 0
    )

    md_lines = [
        "# Phase 1K — Keyword Coverage Snapshot",
        "",
        "Audit of **Phase 1D target phrases** (52 registry entries → **51 unique phrases**) against **planned Academy article titles** (`master-article-inventory.csv`, 300 rows) and **live commercial `<title>` + H1** text only (`index.html`, `features/index.html`).",
        "",
        "## Headline numbers",
        "",
        f"| Metric | Value |",
        f"|--------|------:|",
        f"| Original keyword registry entries | 52 |",
        f"| Unique target phrases (deduped) | 51 |",
        f"| Unique phrases with ≥1 relevant **Academy** title (exact or variant) | {academy_covered} |",
        f"| Unique phrases with ≥1 **commercial** title/H1 match (exact or variant) | {commercial_covered} |",
        f"| Unique phrases covered by **either** Academy or commercial titles | {combined_covered} |",
        f"| **Not covered** (no title/H1 match) | {not_covered} |",
        f"| **Weakly covered** (intent or variant-only / navigational risk) | {weak} |",
        f"| **Commercial-page owned** (by design, little/no Academy title) | {commercial_owned} |",
        f"| Total **exact** phrase hits across all 300 Academy titles | {exact_total_academy} |",
        f"| Phrases with **0** exact title hits (Academy + commercial combined) | {freq_buckets.get('0', 0)} |",
        f"| Phrases with **1** exact title hit | {freq_buckets.get('1', 0)} |",
        f"| Phrases with **2** exact title hits | {freq_buckets.get('2', 0)} |",
        f"| Phrases with **3+** exact title hits | {freq_buckets.get('3+', 0)} |",
        "",
        "## Ten strongest coverage results",
        "",
    ]
    for i, row in enumerate(top10, 1):
        md_lines.append(
            f"{i}. **{row['exact_target_phrase']}** — Academy exact {row['exact_academy_title_match_count']}, "
            f"variant {row['relevant_variant_academy_count']}; commercial exact {row['exact_commercial_title_h1_match_count']}. "
            f"({row['volume_evidence']})"
        )

    md_lines.extend(["", "## Ten most important gaps", ""])
    for i, row in enumerate(top_gaps, 1):
        md_lines.append(
            f"{i}. **{row['exact_target_phrase']}** — {row['coverage_classification']}. "
            f"Academy exact/variant: {row['exact_academy_title_match_count']}/{row['relevant_variant_academy_count']}. "
            f"Commercial: {row['exact_commercial_title_h1_match_count']}/{row['relevant_variant_commercial_count']}. "
            f"{row['recommended_action']}"
        )

    md_lines.extend(
        [
            "",
            "## Candid assessment",
            "",
            "The **website / local growth keyword set** is largely reflected in planned Category 4–5 article titles (GBP, local SEO, builders, cost, conversion). High-priority commercial head terms (`plumber website builder`, `plumbing website design`, template/examples/cost) are **assigned to commercial surfaces** by Phase 1E; the Academy plan adds educational and comparison titles without trying to repeat every exact phrase 300 times.",
            "",
            "**Gaps that matter most** are usually (a) **homepage-supporting** phrases still missing from `<title>`/H1 (`website for plumbers`, `try plumbing website free`), (b) **comparison subtopics** living only as H2s inside A201 (Wix/WordPress/AI exact phrases absent from any title), and (c) **navigational/CRM** queries where a single roundup title (A208) is only a partial fit. Supporting copy for several homepage phrases exists in meta/body but was **out of scope** for this title-only audit.",
            "",
            "Title coverage is a **useful planning diagnostic**, not a ranking guarantee. Competing in Google still depends on content quality, SERP intent fit (especially ambiguous queries like `best plumbing websites`), internal linking, and validated volume—not repeating keywords across dozens of titles.",
            "",
            "Full per-keyword rows: `target-keyword-title-counts.csv`.",
        ]
    )
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    val_lines = [
        "# Phase 1K — Validation Report",
        "",
        "## Source reconciliation",
        "",
        f"- Loaded `{VOLUME_AUDIT.relative_to(ROOT)}`: **{len(volume_rows)}** rows (expected 52).",
        f"- Unique phrases after dedupe: **{len(keywords)}** (expected 51; duplicate entry: `click to call plumber website` entries 18 and 31).",
        f"- Loaded `{INVENTORY.relative_to(ROOT)}`: **{len(articles)}** proposed titles counted.",
        f"- Commercial text extracted from `{INDEX_HTML.relative_to(ROOT)}` (document title + hero H1) and `{FEATURES_HTML.relative_to(ROOT)}` (document title + hero H1) only — no meta descriptions, body copy, or section H2s.",
        "",
        "## Matching rules",
        "",
        "- **Exact:** normalized lowercase phrase appears contiguously in normalized title/H1.",
        "- **Variant:** explicit Phase 1E/1G alternates and ordered multi-token matches with limited plumber/plumbing equivalence; partial single-token matches alone do not count.",
        "- Exact and variant counts are **mutually exclusive per title** (exact wins).",
        "",
        "## Totals check",
        "",
        f"- Sum of Academy exact matches across 51 keywords: **{exact_total_academy}** (reported in snapshot).",
        f"- Keywords with any Academy match: **{academy_covered}**.",
        f"- Keywords with any commercial match: **{commercial_covered}**.",
        f"- Keywords with combined coverage: **{combined_covered}**.",
        "",
        "## Duplicate entry",
        "",
        "- `click to call plumber website`: entry 31 marked `duplicate_of_entry_id=18`; counts attributed once under the canonical phrase.",
        "",
        "## Limitations",
        "",
        "- Merged AC topics (e.g. Wix/WordPress/AI inside A201) are **not** counted as separate title rows until published as H2-only sections.",
        "- `what pages should a plumbing website have` is merged into A181 scope per Phase 1H; Features H1 uses different wording unless variant rules match.",
        "",
        "Generated by `generate_phase1k_deliverables.py` (read-only; no research or site files modified).",
    ]
    val_path.write_text("\n".join(val_lines) + "\n", encoding="utf-8")

    print(f"Wrote {csv_path.name}, {md_path.name}, {val_path.name}")
    print(f"51 unique keywords; academy covered {academy_covered}; combined {combined_covered}; exact academy total {exact_total_academy}")


if __name__ == "__main__":
    main()
