"""Build Phase 1D CSV deliverables from entries + Ahrefs free US bands (2026-10-18)."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent
ENTRIES = ROOT / "entries.json"
AHREFS = ROOT / "ahrefs_free_us_2026-10-18.json"
OUT_AUDIT = ROOT / "phase1d-keyword-volume-audit.csv"
OUT_PRIO = ROOT / "phase1d-keyword-priorities.csv"

RETRIEVAL_DATE = "2026-10-18"

INTENT: dict[str, tuple[str, str, str]] = {
    # keyword -> (search_intent, commercial_relevance, intent_notes)
    "plumber website builder": (
        "Website-builder purchase",
        "Critical",
        "Core commercial head term; homepage owner",
    ),
    "plumberswebsites.com": (
        "Brand/navigation",
        "Critical",
        "Navigational; no Ahrefs phrase-match row",
    ),
    "website for plumbers": (
        "Website-builder purchase",
        "High",
        "Ambiguous: Ahrefs KD SERP (2026-10-18) showed local plumber hire pages — validate intent before scaling",
    ),
    "done for you plumber website": (
        "Website-builder purchase",
        "High",
        "DFY commercial; no Ahrefs exact row — try Semrush seed",
    ),
    "preview plumbing website before paying": (
        "Website-builder purchase",
        "High",
        "Product differentiator; long-tail — validate in Semrush",
    ),
    "plumbing website design": (
        "Website design/service purchase",
        "High",
        "Features page owner",
    ),
    "plumbing website features": (
        "Comparison or alternative research",
        "High",
        "Same URL as design/features",
    ),
    "plumbing website cost": (
        "Pricing or cost research",
        "High",
        "Split pricing section + Academy TCO guide",
    ),
    "plumbing website template": (
        "Website examples or inspiration",
        "Medium-high",
        "Template vs six-design gallery",
    ),
    "plumbing website examples": (
        "Website examples or inspiration",
        "Medium-high",
        "Examples hub + live preview",
    ),
    "best plumber website builder": (
        "Comparison or alternative research",
        "High",
        "No Ahrefs row — validate as 'best website builder for plumbers'",
    ),
    "how to build a plumbing website": (
        "Website creation/how-to",
        "High",
        "Academy flagship",
    ),
    "what pages should a plumbing website have": (
        "Website creation/how-to",
        "High",
        "Features five-page section",
    ),
    "plumber website builder vs wix": (
        "Comparison or alternative research",
        "Medium-high",
        "Spoke under comparison pillar",
    ),
    "ai plumbing website builder": (
        "Comparison or alternative research",
        "Medium-high",
        "Validate exact phrase in Semrush",
    ),
    "plumbing website checklist": (
        "Website creation/how-to",
        "Medium",
        "Checklist asset",
    ),
    "is a website worth it for plumbers": (
        "Pricing or cost research",
        "Medium",
        "ROI decision content",
    ),
    "click to call plumber website": (
        "Website functionality or conversion",
        "Medium",
        "One conversion hub — entries 18 and 31 duplicate",
    ),
    "wordpress for plumbing business": (
        "Comparison or alternative research",
        "Medium",
        "WordPress spoke",
    ),
    "google business profile for plumbers": (
        "SEO or general marketing",
        "Medium",
        "Owner GBP; website URL tie-in",
    ),
    "local seo for plumbing company": (
        "SEO or general marketing",
        "Medium",
        "No Ahrefs row; SERP validation required",
    ),
    "seo for plumbing business": (
        "SEO or general marketing",
        "Medium",
        "Owner SEO — not homeowner rank tactics",
    ),
    "how to get more plumbing customers": (
        "SEO or general marketing",
        "Low-medium",
        "Broad marketing; website as hub only",
    ),
    "create plumbing business website": (
        "Website-builder purchase",
        "High",
        "Homepage supporting variant",
    ),
    "free plumber website builder": (
        "Website-builder purchase",
        "Medium",
        "Honest preview messaging required",
    ),
    "free plumbing website": (
        "Website-builder purchase",
        "Medium",
        "Ahrefs showed related ideas only, not exact seed",
    ),
    "plumber website service": (
        "Website design/service purchase",
        "Medium-high",
        "Homepage supporting",
    ),
    "try plumbing website free": (
        "Website-builder purchase",
        "Medium",
        "FAQ / trial wording",
    ),
    "best call to action for plumber website": (
        "Website functionality or conversion",
        "Low-medium",
        "Section in conversion hub only",
    ),
    "best plumbing websites": (
        "Website examples or inspiration",
        "Medium",
        "Ambiguous: inspiration vs hire-a-plumber; not primary purchase query",
    ),
    "crm website vs custom plumbing website": (
        "Comparison or alternative research",
        "Medium",
        "CRM spoke — defer",
    ),
    "hire web designer for plumbing business": (
        "Website design/service purchase",
        "Medium",
        "Agency alternative angle",
    ),
    "housecall pro website": (
        "Ambiguous or mixed intent",
        "Low-medium",
        "Often navigational to Housecall Pro product",
    ),
    "how to put phone number on plumbing website": (
        "Website functionality or conversion",
        "Low",
        "Combine into conversion hub",
    ),
    "jobber website for plumbers": (
        "Ambiguous or mixed intent",
        "Low-medium",
        "CRM/product navigational risk",
    ),
    "mobile friendly plumber website": (
        "Website functionality or conversion",
        "Medium",
        "Features mobile section",
    ),
    "outdated plumber website": (
        "Website creation/how-to",
        "Low-medium",
        "Refresh guide spoke",
    ),
    "plumber website builder vs squarespace": (
        "Comparison or alternative research",
        "Medium",
        "Comparison spoke",
    ),
    "plumber website design examples 2026": (
        "Website examples or inspiration",
        "Medium",
        "Merge with examples hub",
    ),
    "plumber website speed": (
        "Website functionality or conversion",
        "Low-medium",
        "Section only",
    ),
    "plumbing company website inspiration": (
        "Website examples or inspiration",
        "Medium",
        "Merge with examples hub",
    ),
    "plumbing web design agency": (
        "Website design/service purchase",
        "Medium",
        "Agency alternative content",
    ),
    "plumbing website contact form": (
        "Website functionality or conversion",
        "Low",
        "Conversion hub section",
    ),
    "plumbing website design company": (
        "Website design/service purchase",
        "Medium",
        "Near duplicate of agency/design intents",
    ),
    "plumbing website domain": (
        "Website functionality or conversion",
        "Low-medium",
        "Hosting guide section — verify product facts",
    ),
    "plumbing website hosting": (
        "Website functionality or conversion",
        "Low-medium",
        "Hosting guide",
    ),
    "plumbing website lead capture": (
        "Website functionality or conversion",
        "Low-medium",
        "Conversion hub",
    ),
    "plumbing website phone number placement": (
        "Website functionality or conversion",
        "Low",
        "Combine conversion hub",
    ),
    "plumbing website quote form": (
        "Website functionality or conversion",
        "Low",
        "Combine conversion hub",
    ),
    "service titan website for plumbers": (
        "Ambiguous or mixed intent",
        "Low-medium",
        "CRM/product query",
    ),
    "update plumbing website business hours": (
        "Website functionality or conversion",
        "Low",
        "Maintenance FAQ — not standalone SEO",
    ),
}


def ahrefs_lookup(data: list[dict]) -> dict[str, dict]:
    return {r["keyword"].lower(): r for r in data}


def volume_fields(ah: dict | None) -> dict:
    if not ah or not ah.get("exact_match") == "yes" or not ah.get("volume_band"):
        if ah and ah.get("notes") == "no results":
            return {
                "us_monthly_volume": "",
                "volume_type": "unavailable",
                "volume_source": "Ahrefs Free Keyword Generator",
                "verification_status": "No data returned",
                "confidence": "medium",
                "notes_extra": "Ahrefs returned zero phrase-match ideas for exact seed",
            }
        if ah and ah.get("volume_band") == "No data returned":
            return {
                "us_monthly_volume": "",
                "volume_type": "unavailable",
                "volume_source": "Ahrefs Free Keyword Generator",
                "verification_status": "No data returned",
                "confidence": "medium",
                "notes_extra": ah.get("notes", ""),
            }
        return {
            "us_monthly_volume": "",
            "volume_type": "unavailable",
            "volume_source": "",
            "verification_status": "Not checked or no exact-match row",
            "confidence": "low",
            "notes_extra": "Requires Semrush/Ahrefs paid or GKP for exact US monthly average",
        }
    band = ah["volume_band"]
    return {
        "us_monthly_volume": band,
        "volume_type": "third-party estimate",
        "volume_source": "Ahrefs Free Keyword Generator (US volume band, clickstream-based; not exact monthly average)",
        "verification_status": "Band only — not exact volume",
        "confidence": "medium",
        "notes_extra": "Ahrefs free tier displays bands >100 or <100 searches/month for US",
    }


def recommended_action(kw: str, ah: dict | None, group: str) -> tuple[str, str, str]:
    """action, page, rationale"""
    pages = {
        "plumber website builder": ("https://plumberswebsites.com/", "Homepage H1 owner"),
        "plumbing website design": ("https://plumberswebsites.com/features/", "Features"),
        "plumbing website features": ("https://plumberswebsites.com/features/", "Features"),
        "plumbing website cost": ("https://plumberswebsites.com/#pricing + Academy cost guide", "Pricing + TCO"),
        "how to build a plumbing website": ("/academy/how-to-build-a-plumbing-website/", "Academy"),
        "best plumber website builder": ("/academy/best-plumber-website-builder/", "Academy"),
    }
    default_page = pages.get(kw, ("See Phase 1C cluster owner", ""))

    band = (ah or {}).get("volume_band")
    has_band = (ah or {}).get("exact_match") == "yes" and band in (">100", "<100")

    if kw in ("update plumbing website business hours", "plumbing website phone number placement", "best call to action for plumber website"):
        return ("Combine with another keyword/page", "Academy conversion hub", "Micro-intent; no Ahrefs demand signal")
    if kw in ("housecall pro website", "jobber website for plumbers", "service titan website for plumbers"):
        return ("Defer", "CRM comparison spoke", "Product/navigational risk; no Ahrefs exact row")
    if kw == "best plumbing websites":
        return ("Test further", "Examples hub", ">100 band but inspiration intent — confirm SERP owner audience")
    if kw == "website for plumbers":
        return ("Test further", "Homepage supporting copy", "<100 band; SERP intent ambiguity observed on Ahrefs KD sample")
    if kw == "plumber website builder":
        return ("Prioritise", default_page[0], ">100 band + critical commercial fit")
    if has_band and band == ">100" and INTENT.get(kw, ("", "Medium", ""))[1] in ("Critical", "High", "Medium-high"):
        return ("Prioritise", default_page[0], f"Ahrefs US band {band} + strong product fit")
    if has_band and band == "<100" and INTENT.get(kw, ("", "", ""))[1] in ("High", "Medium-high"):
        return ("Keep as supporting keyword", default_page[0], f"Ahrefs US band {band}; cover on primary page")
    if has_band and band == "<100":
        return ("Keep as supporting keyword", default_page[0], f"Ahrefs US band {band}")
    if group in ("B", "C") and not has_band:
        return ("Combine with another keyword/page", default_page[0], "Merge list entry; no Ahrefs exact-match volume")
    return ("Test further", default_page[0], "Validate exact US volume in Semrush/GKP before dedicated page")


def main() -> None:
    entries = json.loads(ENTRIES.read_text(encoding="utf-8"))
    ahrefs = ahrefs_lookup(json.loads(AHREFS.read_text(encoding="utf-8")))

    audit_fields = [
        "entry_id",
        "group",
        "exact_keyword",
        "duplicate_of_entry_id",
        "us_monthly_volume",
        "volume_type",
        "volume_source",
        "source_database_country",
        "measurement_period",
        "retrieval_date",
        "keyword_difficulty",
        "kd_source",
        "cpc",
        "search_intent",
        "commercial_relevance",
        "verification_status",
        "confidence",
        "notes",
    ]

    audit_rows = []
    prio_rows = []

    for e in entries:
        kw = e["keyword"]
        ah = ahrefs.get(kw.lower())
        vol = volume_fields(ah)
        intent, comm, intent_note = INTENT.get(kw, ("Ambiguous or mixed intent", "Low", ""))
        kd = (ah or {}).get("kd") or ""
        kd_src = "Ahrefs Free Keyword Generator" if kd else ""
        dup = e.get("duplicate_of", "")
        notes = intent_note
        if vol.get("notes_extra"):
            notes = f"{notes}; {vol['notes_extra']}".strip("; ")

        audit_rows.append(
            {
                "entry_id": e["id"],
                "group": e["group"],
                "exact_keyword": kw,
                "duplicate_of_entry_id": dup,
                "us_monthly_volume": vol["us_monthly_volume"],
                "volume_type": vol["volume_type"],
                "volume_source": vol["volume_source"],
                "source_database_country": "United States / English" if vol["volume_source"] else "",
                "measurement_period": "Not disclosed by Ahrefs free tool" if vol["volume_source"] else "",
                "retrieval_date": RETRIEVAL_DATE if ah else RETRIEVAL_DATE,
                "keyword_difficulty": kd,
                "kd_source": kd_src,
                "cpc": "",
                "search_intent": intent,
                "commercial_relevance": comm,
                "verification_status": vol["verification_status"],
                "confidence": vol["confidence"],
                "notes": notes,
            }
        )

        action, page, rationale = recommended_action(kw, ah, e["group"])
        prio_rows.append(
            {
                "keyword": kw,
                "entry_id": e["id"],
                "verified_or_best_available_volume": vol["us_monthly_volume"] or vol["verification_status"],
                "volume_type": vol["volume_type"],
                "commercial_intent": intent,
                "product_fit": comm,
                "keyword_difficulty": kd,
                "recommended_action": action,
                "intended_page": page,
                "evidence_and_rationale": rationale,
            }
        )

    with OUT_AUDIT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=audit_fields)
        w.writeheader()
        w.writerows(audit_rows)

    prio_fields = list(prio_rows[0].keys()) if prio_rows else []
    with OUT_PRIO.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=prio_fields)
        w.writeheader()
        w.writerows(prio_rows)

    print(f"Wrote {len(audit_rows)} audit rows, {len(prio_rows)} priority rows")


if __name__ == "__main__":
    main()
