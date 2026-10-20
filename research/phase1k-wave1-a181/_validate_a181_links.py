import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
art = (ROOT / "academy/how-to-build-a-plumbing-website/index.html").read_text(encoding="utf-8")
hrefs = re.findall(r'href="([^"]+)"', art)
index = (ROOT / "index.html").read_text(encoding="utf-8")
ids = set(re.findall(r'id="([^"]+)"', index))
errors = []
for h in hrefs:
    if h.startswith("http") or h.startswith("mailto:"):
        continue
    if h.startswith("/#"):
        if h[2:] not in ids:
            errors.append(f"missing fragment {h}")
        continue
    if h.startswith("/"):
        p = h.rstrip("/")
        rel = p[1:]
        candidates = [ROOT / f"{rel}.html", ROOT / rel / "index.html", ROOT / rel]
        if not any(c.exists() for c in candidates):
            errors.append(f"missing path {h}")
print("OK" if not errors else "FAIL")
for e in errors:
    print(e)
