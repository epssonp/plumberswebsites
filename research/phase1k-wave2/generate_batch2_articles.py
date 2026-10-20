"""Generate Batch 2 Academy articles (local tool). Run from repo root."""
from __future__ import annotations
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"

CAT = "Plumbing Websites &amp; Digital Tools"
CAT_URL = "/academy/plumbing-websites-digital-tools/"

HEADER = """    <header class="site-header" id="site-header">
        <div class="container header-inner">
            <a href="/" class="site-logo" aria-label="PlumbersWebsites.com — Home">
                plumbers<span>websites</span><small>.com</small>
            </a>
            <nav class="site-nav" aria-label="Main navigation">
                <a href="/#design">How It Works</a>
                <a href="/features/">Features</a>
                <a href="/designs/">Designs</a>
                <a href="/#pricing">Pricing</a>
                <a href="/#faq">FAQ</a>
                <a href="/academy/">Academy</a>
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
            <a href="/designs/">Designs</a>
            <a href="/#pricing">Pricing</a>
            <a href="/#faq">FAQ</a>
            <a href="/academy/">Academy</a>
        </nav>
    </header>"""

FOOTER = """    <footer class="site-footer" id="site-footer">
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
                        <a href="/designs/">Website Designs</a>
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
                <a href="#article-content">Back to top ↑</a>
            </div>
        </div>
    </footer>
    <script src="/script.js"></script>"""


def render(article: dict) -> str:
    slug = article["slug"]
    canonical = f"https://plumberswebsites.com/academy/{slug}/"
    bc_items = [
        ("Academy", "https://plumberswebsites.com/academy/"),
        ("Plumbing Websites & Digital Tools", f"https://plumberswebsites.com{CAT_URL}"),
        (article["subcategory_name"], f"https://plumberswebsites.com{article['subcategory_url']}"),
        (article["breadcrumb_short"], canonical),
    ]
    bc_html = "\n".join(
        f'                    <li><a href="{u.replace("https://plumberswebsites.com", "")}">{n}</a></li>'
        if i < len(bc_items) - 1
        else f'                    <li aria-current="page">{n}</li>'
        for i, (n, u) in enumerate(bc_items)
    )
    bc_ld = json.dumps(
        [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": html.unescape(n),
                "item": u,
            }
            for i, (n, u) in enumerate(bc_items)
        ],
        indent=20,
    )[1:-1]

    related = article.get("related_html", "")
    cta_h = article.get("cta_heading", "Preview a plumbing website with your business details")
    cta_p = article.get("cta_text", "See a personalized five-page preview before you choose a plan — no coding required.")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article["title"]}</title>
    <meta name="description" content="{article["meta_description"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical}">
    <meta name="application-name" content="PlumbersWebsites.com">
    <meta name="theme-color" content="#171f36">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="PlumbersWebsites.com">
    <meta property="og:locale" content="en_US">
    <meta property="og:title" content="{article["title"]}">
    <meta property="og:description" content="{article["og_description"]}">
    <meta property="og:url" content="{canonical}">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{article["title"]}">
    <meta name="twitter:description" content="{article["twitter_description"]}">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@graph": [
            {{
                "@type": "Organization",
                "@id": "https://plumberswebsites.com/#organization",
                "name": "PlumbersWebsites.com",
                "url": "https://plumberswebsites.com/"
            }},
            {{
                "@type": "WebSite",
                "@id": "https://plumberswebsites.com/#website",
                "url": "https://plumberswebsites.com/",
                "name": "PlumbersWebsites.com",
                "publisher": {{ "@id": "https://plumberswebsites.com/#organization" }},
                "inLanguage": "en-US"
            }},
            {{
                "@type": "Article",
                "@id": "{canonical}#article",
                "headline": "{article["title"]}",
                "description": "{article["schema_description"]}",
                "url": "{canonical}",
                "inLanguage": "en-US",
                "isPartOf": {{ "@id": "https://plumberswebsites.com/#website" }},
                "publisher": {{ "@id": "https://plumberswebsites.com/#organization" }},
                "mainEntityOfPage": "{canonical}",
                "about": "{article["about"]}"
            }},
            {{
                "@type": "BreadcrumbList",
                "@id": "{canonical}#breadcrumb",
                "itemListElement": [
{bc_ld}
                ]
            }}
        ]
    }}
    </script>
    <link rel="stylesheet" href="/styles.css">
    <link rel="stylesheet" href="/academy/academy.css">
</head>
<body class="academy-page">
{HEADER}
    <main id="main-content" class="academy-main">
        <div class="container academy-article-main">
            <nav class="academy-breadcrumbs" aria-label="Breadcrumb">
                <ol>
                    <li><a href="/academy/">Academy</a></li>
                    <li><a href="{CAT_URL}">{CAT}</a></li>
                    <li><a href="{article["subcategory_url"]}">{article["subcategory_name"]}</a></li>
                    <li aria-current="page">{article["breadcrumb_short"]}</li>
                </ol>
            </nav>
            <header class="academy-page-header">
                <p class="academy-eyebrow">{article["id"]} · {article["eyebrow"]}</p>
                <h1>{article["h1"]}</h1>
                <p class="academy-lead">{article["lead"]}</p>
            </header>
            <p class="academy-article-meta">For US plumbing business owners · Part of the <a href="{article["subcategory_url"]}">{article["subcategory_short"]}</a> section</p>
            <article class="academy-article-prose" id="article-content">
{article["body"]}
            </article>
            <aside class="academy-related-reading" aria-labelledby="related-heading">
                <h2 id="related-heading">Related reading</h2>
                <ul>
{related}
                </ul>
            </aside>
            <section class="academy-commercial-cta" aria-labelledby="article-cta-heading">
                <h2 id="article-cta-heading">{cta_h}</h2>
                <p>{cta_p}</p>
                <a href="https://app.plumberswebsites.com/sign-in" class="hero-cta">Get Started — Preview First</a>
            </section>
        </div>
    </main>
{FOOTER}
</body>
</html>
"""


def main() -> None:
    bodies_dir = Path(__file__).parent / "bodies"
    articles = json.loads((Path(__file__).parent / "articles.json").read_text(encoding="utf-8"))
    for art in articles:
        body_path = bodies_dir / f"{art['slug']}.html"
        art["body"] = body_path.read_text(encoding="utf-8")
        out = ACADEMY / art["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(art), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
