"""Generate Academy category/subcategory pages and academy-data.js from research CSVs."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SC_CSV = REPO / "research" / "phase1g-subcategory-review" / "subcategory-master.csv"
ART_CSV = REPO / "research" / "phase1h-master-toc" / "master-article-inventory.csv"

CATEGORIES = {
    1: {
        "title": "Plumbing Techniques, Tools & Equipment",
        "description": (
            "Hands-on guidance for plumbing business owners and field teams on proven techniques, "
            "jobsite tools, and equipment choices that affect quality, safety, and efficiency on the job."
        ),
        "slug": "plumbing-techniques-tools-equipment",
        "icon": "wrench",
    },
    2: {
        "title": "Licensing, Training & Credentials",
        "description": (
            "Clear explanations of licensing, training, and credential requirements for plumbing "
            "business owners — including compliance basics, continuing education, and what to verify "
            "when hiring licensed plumbers."
        ),
        "slug": "licensing-training-credentials",
        "icon": "badge",
    },
    3: {
        "title": "Starting & Running a Plumbing Business",
        "description": (
            "Practical guidance for starting, structuring, and operating a plumbing company — from "
            "early planning and pricing to hiring, scheduling, and day-to-day business decisions. "
            "Website and marketing topics live in other Academy categories."
        ),
        "slug": "starting-running-plumbing-business",
        "icon": "briefcase",
    },
    4: {
        "title": "Finding Customers & Growing Locally",
        "description": (
            "Marketing and visibility strategies for plumbing business owners who want more local "
            "customers — including Google Business Profile, local search basics, reviews, referrals, "
            "and lead generation, with your website as one part of the system."
        ),
        "slug": "finding-customers-growing-locally",
        "icon": "map-pin",
    },
    5: {
        "title": "Plumbing Websites & Digital Tools",
        "description": (
            "Practical guides for plumbing business owners on building a plumbing website, choosing "
            "website templates and digital tools, improving their online presence, and helping "
            "potential customers find their business online."
        ),
        "slug": "plumbing-websites-digital-tools",
        "icon": "monitor",
    },
    6: {
        "title": "Industry Trends & Professional Growth",
        "description": (
            "Stay current with plumbing industry trends, business best practices, and professional "
            "growth topics that help owners lead stronger companies — separate from licensing exams, "
            "field technique tutorials, and website how-to guides."
        ),
        "slug": "industry-trends-professional-growth",
        "icon": "trending",
    },
}


def slugify(text: str) -> str:
    s = text.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def load_subcategories() -> list[dict]:
    rows = []
    with SC_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pid = int(row["parent_category_id"])
            cat = CATEGORIES[pid]
            rows.append(
                {
                    **row,
                    "category_slug": cat["slug"],
                    "category_title": cat["title"],
                    "sub_slug": slugify(row["subcategory_title"]),
                }
            )
    return rows


def load_articles_by_sc() -> dict[str, list[dict]]:
    by_sc: dict[str, list[dict]] = {}
    with ART_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sc = row["subcategory_id"]
            by_sc.setdefault(sc, []).append(
                {
                    "id": row["article_id"],
                    "title": row["proposed_title"],
                    "slug": row["proposed_slug"],
                    "status": row.get("status", "proposed"),
                    "priority": row.get("priority", ""),
                    "scope": row.get("scope_statement", "")[:200],
                }
            )
    return by_sc


def header_html(academy_current: bool = False) -> str:
    ac = ' aria-current="page"' if academy_current else ""
    return f"""    <header class="site-header" id="site-header">
        <div class="container header-inner">
            <a href="/" class="site-logo" aria-label="PlumbersWebsites.com — Home">
                plumbers<span>websites</span><small>.com</small>
            </a>
            <nav class="site-nav" aria-label="Main navigation">
                <a href="/#design">How It Works</a>
                <a href="/features/">Features</a>
                <a href="/#business">Designs</a>
                <a href="/#pricing">Pricing</a>
                <a href="/#faq">FAQ</a>
                <a href="/academy/"{ac}>Academy</a>
            </nav>
            <a href="https://app.plumberswebsites.com/sign-in" class="hero-cta">BUILD IT</a>
            <button class="mobile-menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false"
                aria-controls="mobile-navigation">
                <span></span><span></span><span></span>
            </button>
        </div>
        <nav class="mobile-navigation" id="mobile-navigation" aria-label="Mobile navigation">
            <a href="/#design">How It Works</a>
            <a href="/features/">Features</a>
            <a href="/#business">Designs</a>
            <a href="/#pricing">Pricing</a>
            <a href="/#faq">FAQ</a>
            <a href="/academy/"{ac}>Academy</a>
        </nav>
    </header>"""


def footer_html(back_href: str = "/academy/", back_label: str = "Back to Academy") -> str:
    return f"""    <footer class="site-footer" id="site-footer">
        <div class="container">
            <div class="footer-main">
                <div class="footer-brand">
                    <a href="/" class="site-logo footer-logo" aria-label="PlumbersWebsites.com — Home">
                        plumbers<span>websites</span><small>.com</small>
                    </a>
                    <p class="footer-tagline">Your Plumber Website Builder — Built for You.</p>
                </div>
                <div class="footer-links">
                    <div class="footer-column">
                        <h3>Explore</h3>
                        <a href="/academy/">Academy</a>
                        <a href="/features/">Features</a>
                        <a href="/#business">Website Designs</a>
                        <a href="/#design">How It Works</a>
                        <a href="/#pricing">Pricing</a>
                    </div>
                    <div class="footer-column">
                        <h3>Company</h3>
                        <a href="/about/">About Us</a>
                        <a href="/our-approach/">Our Approach</a>
                        <a href="/contact/">Contact</a>
                    </div>
                    <div class="footer-column">
                        <h3>Help</h3>
                        <a href="/#faq">Frequently Asked Questions</a>
                        <a href="https://app.plumberswebsites.com/sign-in">Get Started</a>
                    </div>
                    <div class="footer-column">
                        <h3>Legal</h3>
                        <a href="/privacy/">Privacy Policy</a>
                        <a href="/terms/">Terms of Service</a>
                        <a href="/cancellation-refund/">Cancellation &amp; Refund Policy</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 PlumbersWebsites.com. All rights reserved.</p>
                <a href="{back_href}">{back_label} ↑</a>
            </div>
        </div>
    </footer>"""


def head_html(title: str, description: str, canonical: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical}">
    <meta name="application-name" content="PlumbersWebsites.com">
    <meta name="theme-color" content="#171f36">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="PlumbersWebsites.com">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/academy/academy.css">
</head>
<body class="academy-page">"""


def write_data_js(subcats: list[dict], articles_by_sc: dict) -> None:
    cats_out = []
    for cid in sorted(CATEGORIES.keys()):
        c = CATEGORIES[cid]
        subs = [s for s in subcats if int(s["parent_category_id"]) == cid]
        cats_out.append(
            {
                "id": cid,
                "slug": c["slug"],
                "title": c["title"],
                "description": c["description"],
                "icon": c["icon"],
                "url": f"https://plumberswebsites.com/academy/{c['slug']}/",
                "subcategories": [
                    {
                        "id": s["subcategory_id"],
                        "slug": s["sub_slug"],
                        "title": s["subcategory_title"],
                        "description": s["subcategory_description"],
                        "url": f"https://plumberswebsites.com/academy/{c['slug']}/{s['sub_slug']}/",
                    }
                    for s in subs
                ],
            }
        )

    published = []  # Populated when articles are approved and pages exist

    payload = {
        "version": 1,
        "publishedArticles": published,
        "categories": cats_out,
        "plannedArticleCount": sum(len(v) for v in articles_by_sc.values()),
    }
    path = ROOT / "academy-data.js"
    path.write_text(
        "/* Implementation metadata — not raw research CSVs. */\n"
        f"window.PLW_ACADEMY = {json.dumps(payload, indent=2)};\n",
        encoding="utf-8",
    )


def render_category_page(cat_id: int, subcats: list[dict]) -> None:
    c = CATEGORIES[cat_id]
    slug = c["slug"]
    canonical = f"https://plumberswebsites.com/academy/{slug}/"
    title = f"{c['title']} | PlumbersWebsites Academy"
    desc = c["description"][:155] + ("…" if len(c["description"]) > 155 else "")
    subs = [s for s in subcats if int(s["parent_category_id"]) == cat_id]

    sub_cards = []
    for s in subs:
        url = f"/academy/{slug}/{s['sub_slug']}/"
        sub_cards.append(
            f"""                <article class="academy-subcategory-card">
                    <h2 class="academy-subcategory-card-title">
                        <a href="{url}">{s['subcategory_title']}</a>
                    </h2>
                    <p class="academy-subcategory-card-desc">{s['subcategory_description']}</p>
                    <a class="academy-text-link" href="{url}">Browse this section</a>
                </article>"""
        )

    html = (
        head_html(title, desc, canonical)
        + "\n"
        + header_html(False)
        + f"""
    <main id="main-content" class="academy-main">
        <div class="container">
            <nav class="academy-breadcrumbs" aria-label="Breadcrumb">
                <ol>
                    <li><a href="/academy/">Academy</a></li>
                    <li aria-current="page">{c['title']}</li>
                </ol>
            </nav>
            <header class="academy-page-header">
                <p class="academy-eyebrow">Category {cat_id:02d}</p>
                <h1>{c['title']}</h1>
                <p class="academy-lead">{c['description']}</p>
            </header>
            <section class="academy-section" aria-labelledby="subcategories-heading">
                <h2 id="subcategories-heading">Sections in this category</h2>
                <div class="academy-subcategory-grid">
{chr(10).join(sub_cards)}
                </div>
            </section>
        </div>
    </main>
"""
        + footer_html(f"/academy/{slug}/", "Back to top")
        + """
    <script src="/script.js"></script>
</body>
</html>
"""
    )
    out_dir = ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")


def render_subcategory_page(sc: dict, articles: list[dict]) -> None:
    cat_slug = sc["category_slug"]
    sub_slug = sc["sub_slug"]
    canonical = f"https://plumberswebsites.com/academy/{cat_slug}/{sub_slug}/"
    title = f"{sc['subcategory_title']} | {sc['category_title']} | Academy"
    desc = sc["subcategory_description"][:155] + ("…" if len(sc["subcategory_description"]) > 155 else "")

    planned_items = []
    for art in articles:
        planned_items.append(
            f'                    <li class="academy-planned-item"><span>{art["title"]}</span>'
            f' <em class="academy-planned-badge">Planned</em></li>'
        )

    html = (
        head_html(title, desc, canonical)
        + "\n"
        + header_html(False)
        + f"""
    <main id="main-content" class="academy-main">
        <div class="container">
            <nav class="academy-breadcrumbs" aria-label="Breadcrumb">
                <ol>
                    <li><a href="/academy/">Academy</a></li>
                    <li><a href="/academy/{cat_slug}/">{sc['category_title']}</a></li>
                    <li aria-current="page">{sc['subcategory_title']}</li>
                </ol>
            </nav>
            <header class="academy-page-header">
                <p class="academy-eyebrow">{sc['subcategory_id']}</p>
                <h1>{sc['subcategory_title']}</h1>
                <p class="academy-lead">{sc['subcategory_description']}</p>
            </header>
            <section class="academy-section" aria-labelledby="guides-heading">
                <h2 id="guides-heading">Guides in this section</h2>
                <p class="academy-note">These topics are planned for the Academy library. Guides appear here once written, reviewed, and published — links are not shown until then.</p>
                <ul class="academy-planned-list">
{chr(10).join(planned_items)}
                </ul>
            </section>
        </div>
    </main>
"""
        + footer_html(f"/academy/{cat_slug}/{sub_slug}/", "Back to top")
        + """
    <script src="/script.js"></script>
</body>
</html>
"""
    )
    out_dir = ROOT / cat_slug / sub_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")


def main() -> None:
    subcats = load_subcategories()
    articles_by_sc = load_articles_by_sc()
    write_data_js(subcats, articles_by_sc)
    for cid in CATEGORIES:
        render_category_page(cid, subcats)
    for sc in subcats:
        render_subcategory_page(sc, articles_by_sc.get(sc["subcategory_id"], []))
    print(f"Generated academy-data.js, 6 categories, {len(subcats)} subcategories")


if __name__ == "__main__":
    main()
