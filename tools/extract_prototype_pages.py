#!/usr/bin/env python3
"""Split VK-secondary-pages-source.html into standalone page HTML files under pages/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "VK-secondary-pages-source.html"
OUT_DIR = ROOT / "pages"

# Line numbers are 1-based, inclusive ranges for page <div> blocks and optional JSON-LD before them.
PAGES = [
    {
        "page_id": "home",
        "file": "home.html",
        "title": "Vintage King — Homepage (standalone)",
        "lines": (2485, 3089),
        "ldjson": None,
    },
    {
        "page_id": "category",
        "file": "category.html",
        "title": "Vintage King — Category (standalone)",
        "lines": (3094, 3372),
        "ldjson": None,
    },
    {
        "page_id": "product",
        "file": "product.html",
        "title": "Vintage King — Product (standalone)",
        "lines": (3378, 3535),
        "ldjson": None,
    },
    {
        "page_id": "faq",
        "file": "faq.html",
        "title": "Vintage King — FAQ (standalone)",
        "lines": (3540, 3707),
        "ldjson": None,
    },
    {
        "page_id": "deals",
        "file": "deals.html",
        "title": "Vintage King — Demo Deals (standalone)",
        "lines": (3712, 3866),
        "ldjson": None,
    },
    {
        "page_id": "sell",
        "file": "sell.html",
        "title": "Vintage King — Sell or Trade (standalone)",
        "lines": (4190, 4514),
        "ldjson": (4137, 4189),
    },
    {
        "page_id": "techshop",
        "file": "techshop.html",
        "title": "Vintage King — Tech Shop (standalone)",
        "lines": (4781, 5133),
        "ldjson": (4751, 4779),
    },
    {
        "page_id": "studio",
        "file": "studio.html",
        "title": "Vintage King — Studio Installations (standalone)",
        "lines": (5170, 5510),
        "ldjson": (5139, 5168),
    },
    {
        "page_id": "fin-page",
        "file": "financing.html",
        "title": "Vintage King — Financing (standalone)",
        "lines": (5518, 5770),
        "ldjson": (5514, 5516),
    },
    {
        "page_id": "openbox",
        "file": "openbox.html",
        "title": "Vintage King — Open Box (standalone)",
        "lines": (5778, 6247),
        "ldjson": (5774, 5776),
    },
]

# Shared slices (1-based, inclusive)
HEAD_END = 1724  # through </head>
NAV_TEMPLATE = (1758, 2480)
FOOTER_TEMPLATE = (3868, 3978)
SCRIPT_NAV_SETUP = (3980, 4074)
STICKY_LB = (4077, 4132)
MAIN_SCRIPT = (4516, 4747)

def lines_slice(path: Path, start: int, end: int) -> str:
    data = path.read_text(encoding="utf-8")
    all_lines = data.splitlines(keepends=True)
    return "".join(all_lines[start - 1 : end])


def patch_main_script(script: str, page_id: str) -> str:
    """Single-page injectShared + safe toggles + cross-page navigation."""
    script = script.replace(
        """  function injectShared() {
    ['home','category','product','faq','deals','sell','studio','techshop','fin-page','openbox'].forEach(p => {
      const navTarget = document.getElementById('nav-' + p);
      const footerTarget = document.getElementById('footer-' + p);
      if (navTarget) navTarget.innerHTML = document.getElementById('nav-template').innerHTML;
      if (footerTarget) footerTarget.innerHTML = document.getElementById('footer-template').innerHTML;
    });
  }""",
        f"""  function injectShared() {{
    const p = '{page_id}';
    const navTarget = document.getElementById('nav-' + p);
    const footerTarget = document.getElementById('footer-' + p);
    if (navTarget) navTarget.innerHTML = document.getElementById('nav-template').innerHTML;
    if (footerTarget) footerTarget.innerHTML = document.getElementById('footer-template').innerHTML;
  }}""",
    )
    script = script.replace(
        """  function goToDeals() {
    const btn = document.querySelector('.page-switcher button:nth-child(5)');
    if (btn) showPage('deals', btn);
  }""",
        """  function goToDeals() {
    window.location.href = 'deals.html';
  }""",
    )
    script = script.replace(
        """  function showPage(id, btn) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    document.querySelectorAll('.page-switcher button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    window.scrollTo(0, 0);
  }""",
        """  var __vkPageFiles = {
    'home': 'home.html', 'category': 'category.html', 'product': 'product.html', 'faq': 'faq.html',
    'deals': 'deals.html', 'sell': 'sell.html', 'studio': 'studio.html', 'techshop': 'techshop.html',
    'fin-page': 'financing.html', 'openbox': 'openbox.html'
  };
  function showPage(id, btn) {
    var href = __vkPageFiles[id];
    if (href) { window.location.href = href; return; }
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    var el = document.getElementById(id);
    if (el) el.classList.add('active');
    if (btn && btn.classList) btn.classList.add('active');
    window.scrollTo(0, 0);
  }""",
    )
    script = script.replace(
        """  function toggleFilterPanel() {
    const panel = document.getElementById('filter-panel');
    const btn = document.getElementById('more-filters-btn');
    panel.classList.toggle('open');
    btn.textContent = panel.classList.contains('open') ? 'Less Filters ↑' : 'More Filters ↓';
  }""",
        """  function toggleFilterPanel() {
    const panel = document.getElementById('filter-panel');
    const btn = document.getElementById('more-filters-btn');
    if (!panel || !btn) return;
    panel.classList.toggle('open');
    btn.textContent = panel.classList.contains('open') ? 'Less Filters ↑' : 'More Filters ↓';
  }""",
    )
    return script


def normalize_page_div(html: str, page_id: str) -> str:
    """Ensure single visible page: class is 'page active'."""
    import re

    # Replace id="x" class="page" or class="page active" with stable active
    pat = re.compile(
        rf'(<div\s+id="{re.escape(page_id)}"\s+class=")page(\s+active)?(")',
        re.I,
    )

    def repl(m: re.Match) -> str:
        return m.group(1) + "page active" + m.group(3)

    return pat.sub(repl, html, count=1)


def build_head(base_head: str, title: str) -> str:
    import re

    base_head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", base_head, count=1, flags=re.S)
    extra = """

  <!-- Standalone page: show single .page -->
  <style id="vk-standalone-patch">
    .page { display: block !important; }
  </style>
"""
    return base_head.replace("</head>", extra + "</head>", 1)


CHROME = """<nav class="vk-secondary-chrome" aria-label="Secondary pages" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="../navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Extracted from VK-secondary-pages-source.html</span>
</nav>
"""

SECONDARY_CTA = """<div class="header-toggle secondary-cta-toggle" style="background:#f0f0ee;border-bottom:1px solid #ddd">
  <span>Secondary Page CTAs:</span>
  <button class="active" onclick="switchSecondaryCTA('var(--vk-red)', this)">Red</button>
  <button onclick="switchSecondaryCTA('#D4860A', this)">Amber</button>
</div>
"""


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"Missing source: {SRC}")

    raw = SRC.read_text(encoding="utf-8")
    all_lines = raw.splitlines(keepends=True)

    head = "".join(all_lines[:HEAD_END])
    nav_tpl = "".join(all_lines[NAV_TEMPLATE[0] - 1 : NAV_TEMPLATE[1]])
    footer_tpl = "".join(all_lines[FOOTER_TEMPLATE[0] - 1 : FOOTER_TEMPLATE[1]])
    script_setup = "".join(all_lines[SCRIPT_NAV_SETUP[0] - 1 : SCRIPT_NAV_SETUP[1]])
    sticky_lb = "".join(all_lines[STICKY_LB[0] - 1 : STICKY_LB[1]])
    main_script_raw = "".join(all_lines[MAIN_SCRIPT[0] - 1 : MAIN_SCRIPT[1]])

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for spec in PAGES:
        pid = spec["page_id"]
        page_script = patch_main_script(main_script_raw, pid)

        body_parts = [
            '<body class="vk-reviewer-pad vk-standalone">\n',
            CHROME,
            SECONDARY_CTA,
            nav_tpl,
            footer_tpl,
        ]
        if spec["ldjson"]:
            a, b = spec["ldjson"]
            body_parts.append("".join(all_lines[a - 1 : b]))
        body_parts.append(normalize_page_div(lines_slice(SRC, *spec["lines"]), pid))
        body_parts.append(sticky_lb)
        body_parts.append(script_setup)
        body_parts.append(page_script)
        body_parts.append("</body>\n</html>\n")

        full = build_head(head, spec["title"]) + "".join(body_parts)
        out_path = OUT_DIR / spec["file"]
        out_path.write_text(full, encoding="utf-8")
        print("Wrote", out_path.relative_to(ROOT))

    readme = OUT_DIR / "README.txt"
    readme.write_text(
        """Standalone HTML files extracted from ../VK-secondary-pages-source.html (10 core prototype sections).

Not the same as HANDOFF.md marketing pages (about, hall-of-fame, etc.) — those are not in the source file.

Open ../navigator.html for the roadmap.
""",
        encoding="utf-8",
    )
    print("Wrote", readme.relative_to(ROOT))


if __name__ == "__main__":
    main()
