"""Local validation for Batch 2 Academy articles."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLUGS = [
    "best-plumber-website-builder",
    "plumbing-website-cost",
    "plumbing-website-examples",
    "plumbing-website-checklist",
    "how-to-build-a-plumbing-website",
]
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
FRAGMENTS = set(re.findall(r'id="([^"]+)"', INDEX))


def resolve(href: str) -> bool:
    if href.startswith("http") or href.startswith("mailto:"):
        return True
    if href.startswith("/#"):
        return href[2:] in FRAGMENTS
    if not href.startswith("/"):
        return True
    p = href.rstrip("/")
    rel = p[1:]
    candidates = [ROOT / f"{rel}.html", ROOT / rel / "index.html", ROOT / rel]
    return any(c.exists() for c in candidates)


def main() -> None:
    errors: list[str] = []
    titles: list[str] = []
    h1s: list[str] = []
    canonicals: list[str] = []

    for slug in SLUGS[:4]:
        path = ROOT / "academy" / slug / "index.html"
        if not path.exists():
            errors.append(f"missing file {path}")
            continue
        text = path.read_text(encoding="utf-8")
        title_m = re.search(r"<title>([^<]+)</title>", text)
        h1_m = re.search(r"<header class=\"academy-page-header\">.*?<h1>([^<]+)</h1>", text, re.S)
        if not h1_m:
            h1_m = re.search(r"<h1>([^<]+)</h1>", text)
        can_m = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        if title_m:
            titles.append(title_m.group(1))
        if h1_m:
            h1s.append(h1_m.group(1))
        if can_m:
            canonicals.append(can_m.group(1))

        for href in re.findall(r'href="([^"]+)"', text):
            if not resolve(href):
                errors.append(f"{slug}: broken link {href}")

        ld = re.search(
            r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
            text,
            re.S,
        )
        if not ld:
            errors.append(f"{slug}: missing JSON-LD")
        else:
            try:
                json.loads(ld.group(1))
            except json.JSONDecodeError as exc:
                errors.append(f"{slug}: invalid JSON-LD: {exc}")

    if len(set(titles)) != len(titles):
        errors.append("duplicate titles among batch")
    if len(set(h1s)) != len(h1s):
        errors.append("duplicate H1s among batch")
    if len(set(canonicals)) != len(canonicals):
        errors.append("duplicate canonicals among batch")

    data = json.loads((ROOT / "academy/academy-data.js").read_text(encoding="utf-8").split("=", 1)[1].strip().rstrip(";"))
    pub_ids = {a["id"] for a in data.get("publishedArticles", [])}
    for aid in ("A185", "A200", "A201", "A219", "A181"):
        if aid not in pub_ids:
            errors.append(f"missing publishedArticles id {aid}")

    print("OK" if not errors else "FAIL")
    for e in errors:
        print(e)


if __name__ == "__main__":
    main()
