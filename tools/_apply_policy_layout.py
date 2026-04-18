"""Convert policy pages to a clean policy layout.

For each page:
  - Drop the marketing pg-hero + trust strip
  - Add a red Demo Dashboard back-button strip at the very top of body
  - Add a slim policy title block (white bg, title + last-updated + 1-line summary)
  - Wrap .policy-content in a 2-col layout with a sticky TOC sidebar
  - Auto-generate TOC entries from <h2> headings (slug-based ids)
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "privacy-policy-v2.html": {
        "title": "Privacy Policy",
        "summary": "Plain language. We don't sell your data.",
        "updated": "April 18, 2026",
    },
    "returns-v2.html": {
        "title": "Returns Policy",
        "summary": "30-day returns on most gear, no restocking fee.",
        "updated": "April 18, 2026",
    },
    "shipping-policy-v2.html": {
        "title": "Shipping Policy",
        "summary": "Free over $99. Insured. Tracked door-to-door.",
        "updated": "April 18, 2026",
    },
}

# CSS appended in <head> for the policy layout
POLICY_CSS = """
<style id=\"policy-layout-patch\">
/* Demo wrapper */
.demo-bar{background:#1A1A18;padding:10px 24px;display:flex;align-items:center;gap:12px;border-bottom:1px solid rgba(255,255,255,0.08)}
.demo-bar a.back{display:inline-block;background:#C0392B;color:#fff;padding:7px 14px;border-radius:3px;font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;font-family:'DM Sans',sans-serif}
.demo-bar a.back:hover{opacity:0.88}
.demo-bar .label{color:rgba(255,255,255,0.4);font-size:11px;font-family:'DM Sans',sans-serif;letter-spacing:0.06em}
.demo-bar .label strong{color:#fff;font-weight:600}
/* Policy header */
.policy-header{background:#fff;border-bottom:1px solid rgba(26,26,24,0.08);padding:48px 0 36px}
.policy-header-inner{max-width:1160px;margin:0 auto;padding:0 40px}
.policy-eyebrow{font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:rgba(26,26,24,0.45);margin-bottom:14px}
.policy-h1{font-family:var(--font-display);font-size:42px;font-weight:700;color:var(--near-black);line-height:1.05;margin:0 0 10px;letter-spacing:-0.01em}
.policy-updated{font-family:'DM Sans',sans-serif;font-size:13px;color:rgba(26,26,24,0.55);margin-bottom:14px}
.policy-summary{font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.75);max-width:680px;line-height:1.55;margin:0}
/* Two-col policy body */
.policy-body{background:var(--off-white);padding:48px 0 80px}
.policy-body-inner{max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:240px 1fr;gap:48px;align-items:start}
.policy-toc{position:sticky;top:24px;background:#fff;border:1px solid rgba(26,26,24,0.08);padding:18px 18px 16px;border-radius:3px;font-family:'DM Sans',sans-serif}
.policy-toc-label{font-size:10px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.4);margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid rgba(26,26,24,0.06)}
.policy-toc ol{list-style:none;margin:0;padding:0;counter-reset:toc}
.policy-toc li{counter-increment:toc;margin:0;padding:6px 0;font-size:13px;line-height:1.4;color:rgba(26,26,24,0.7);border-bottom:1px solid rgba(26,26,24,0.04)}
.policy-toc li:last-child{border-bottom:none}
.policy-toc li::before{content:counter(toc) \". \";color:rgba(26,26,24,0.32);font-weight:500;margin-right:4px}
.policy-toc a{color:rgba(26,26,24,0.7);text-decoration:none;transition:color 0.15s}
.policy-toc a:hover{color:#C0392B}
.policy-content-wrap{background:#fff;border:1px solid rgba(26,26,24,0.08);padding:48px 56px;border-radius:3px;font-family:'DM Sans',sans-serif}
.policy-content-wrap h2{font-family:var(--font-display);font-size:24px;font-weight:600;color:var(--near-black);margin:36px 0 12px;line-height:1.2;scroll-margin-top:24px}
.policy-content-wrap h2:first-child{margin-top:0}
.policy-content-wrap h2::before{content:counter(sec) \". \";counter-increment:sec;color:rgba(26,26,24,0.3);font-weight:500;margin-right:4px;font-size:20px;font-family:'DM Sans',sans-serif}
.policy-content-wrap{counter-reset:sec}
.policy-content-wrap p{font-size:15px;line-height:1.7;color:rgba(26,26,24,0.78);margin:0 0 14px}
.policy-content-wrap ul{margin:8px 0 18px 22px;font-size:15px;line-height:1.7;color:rgba(26,26,24,0.78)}
.policy-content-wrap li{margin-bottom:6px}
.policy-content-wrap a{color:#C0392B;text-decoration:underline;text-decoration-color:rgba(192,57,43,0.3)}
.policy-content-wrap a:hover{text-decoration-color:#C0392B}
@media(max-width:880px){
  .policy-body-inner{grid-template-columns:1fr;gap:24px}
  .policy-toc{position:static}
  .policy-content-wrap{padding:32px 24px}
  .policy-h1{font-size:32px}
}
</style>
</head>"""


HERO_AND_TRUST_RE = re.compile(
    r'<section class="pg-hero"[^>]*>.*?</section>\s*'
    r'(?:<!--\s*TRUST STRIP[^>]*-->\s*<section[^>]*>.*?</section>\s*)?',
    re.DOTALL,
)

POLICY_CONTENT_RE = re.compile(
    r'<div class="policy-content">(.*?)</div>\s*(?=<section class="pg-section pg-section-cta")',
    re.DOTALL,
)


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def build_demo_bar(title: str) -> str:
    return (
        '<div class="demo-bar">\n'
        '  <a class="back" href="https://barreletics.github.io/vintage-king-redesign/VK-Prototype-Index.html">\u2190 Demo Dashboard</a>\n'
        f'  <span class="label"><strong>VK {title}</strong> &nbsp;\u00b7&nbsp; Sub-navigation page</span>\n'
        '</div>\n'
    )


def build_policy_header(meta: dict) -> str:
    return (
        '<section class="policy-header">\n'
        '  <div class="policy-header-inner">\n'
        '    <div class="policy-eyebrow">Help \u00b7 Policy</div>\n'
        f'    <h1 class="policy-h1">{meta["title"]}</h1>\n'
        f'    <div class="policy-updated">Last updated: {meta["updated"]}</div>\n'
        f'    <p class="policy-summary speakable">{meta["summary"]}</p>\n'
        '  </div>\n'
        '</section>\n'
    )


def build_body(content_inner: str, title: str) -> str:
    # Add IDs to <h2> tags and collect TOC entries
    toc_entries: list[tuple[str, str]] = []

    def add_id(match: re.Match) -> str:
        head = match.group(1)
        slug = slugify(head)
        toc_entries.append((slug, head.strip()))
        return f'<h2 id="{slug}">{head}</h2>'

    new_inner = re.sub(r"<h2>([^<]+)</h2>", add_id, content_inner)

    toc_html = "\n".join(
        f'      <li><a href="#{sid}">{label}</a></li>' for sid, label in toc_entries
    )

    return (
        '<section class="policy-body">\n'
        '  <div class="policy-body-inner">\n'
        '    <aside class="policy-toc">\n'
        '      <div class="policy-toc-label">On this page</div>\n'
        '      <ol>\n'
        f'{toc_html}\n'
        '      </ol>\n'
        '    </aside>\n'
        '    <div class="policy-content-wrap">\n'
        f'{new_inner}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>\n'
    )


def patch(path: Path, meta: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    if "policy-layout-patch" in text:
        return False

    # 1) Inject CSS before </head>
    if "</head>" not in text:
        print(f"  SKIP {path.name}: no </head>")
        return False
    text = text.replace("</head>", POLICY_CSS, 1)

    # 2) Insert demo bar right after <body>
    text = text.replace("<body>", "<body>\n" + build_demo_bar(meta["title"]), 1)

    # 3) Replace pg-hero (and trust strip) with policy-header
    if not HERO_AND_TRUST_RE.search(text):
        print(f"  SKIP {path.name}: hero/trust block not found")
        return False
    text = HERO_AND_TRUST_RE.sub(build_policy_header(meta), text, count=1)

    # 4) Wrap policy-content in 2-col layout with TOC
    pc_match = POLICY_CONTENT_RE.search(text)
    if not pc_match:
        print(f"  SKIP {path.name}: policy-content not found")
        return False
    inner = pc_match.group(1)
    new_block = build_body(inner, meta["title"])
    text = text[: pc_match.start()] + new_block + text[pc_match.end():]

    path.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    changed = 0
    for filename, meta in PAGES.items():
        path = ROOT / filename
        if not path.exists():
            print(f"  MISS {filename}")
            continue
        if patch(path, meta):
            print(f"  OK   {filename}")
            changed += 1
        else:
            print(f"  --   {filename}")
    print(f"Patched {changed}/{len(PAGES)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
