#!/usr/bin/env python3
"""Build vk-resources-inventory.xlsx — team audit / gap-analysis spreadsheet.

5 tabs, columns per team request:
  Resource | Live link | Define | Comments | Additional Link 1 | Additional Link 2 | Vintageking.com equivalent
"""
from __future__ import annotations
import re, html, sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
LIVE = "https://barreletics.github.io/vk-secondary-pages"
CORE = "https://barreletics.github.io/vintage-king-redesign"

# ---------- helpers ----------
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
META_DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']', re.I
)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")

def clean(s: str) -> str:
    s = TAG_RE.sub(" ", s or "")
    return html.unescape(re.sub(r"\s+", " ", s)).strip()

def extract(path: Path) -> dict:
    if not path.exists():
        return {"title": "", "desc": "", "h1": ""}
    txt = path.read_text(encoding="utf-8", errors="ignore")
    title = clean((TITLE_RE.search(txt) or [None, ""])[1] if TITLE_RE.search(txt) else "")
    desc = (META_DESC_RE.search(txt) or [None, ""])[1] if META_DESC_RE.search(txt) else ""
    h1 = clean((H1_RE.search(txt) or [None, ""])[1] if H1_RE.search(txt) else "")
    return {"title": title, "desc": clean(desc), "h1": h1}

def url(rel: str) -> str:
    return f"{LIVE}/{rel}"

def define_for(meta: dict, fallback: str = "") -> str:
    return meta["desc"] or meta["h1"] or meta["title"] or fallback

# ---------- row builder ----------
def row(name, link, define, comments="", add1=("",""), add2=("",""), vk_equiv=""):
    """Returns 7-tuple: Resource, Live link, Define, Comments, Add1, Add2, VK equivalent."""
    return [name, link, define, comments, add1[1] if add1[0] else "",
            add2[1] if add2[0] else "", vk_equiv]

def labeled_link(label, url_):
    return (label, f"{label} — {url_}") if url_ else ("", "")

# ---------- tab data ----------
def tab_pages():
    """Built secondary marketing/info pages. v2 = primary, v1 = Additional Link 1."""
    rows = []
    # (display name, base filename without -v2.html, has_v2, vk-equivalent path-hint)
    items = [
        ("About VK", "about", True, "/about"),
        ("Hall of Fame", "hall-of-fame", False, ""),
        ("Make Your Mark", "make-your-mark", False, ""),
        ("PLAYBACK Magazine", "playback", False, ""),
        ("Careers", "careers", False, "/careers"),
        ("Studio Professionals", "studio-professionals", False, ""),
        ("Trade Program", "trade-program", False, ""),
        ("Audio Consultants", "audio-consultants", False, ""),
        ("Section 179 Tax Savings", "section-179", False, ""),
        ("VK Warranty", "warranty", False, "/warranty"),
        ("VK Credit Card", "vk-credit-card", False, ""),
        ("Live Sound How-To", "live-sound-how", False, ""),
        ("Recording at Home", "recording-at-home", False, ""),
        ("Classic Studios Gone Modern", "classic-studios-gone-modern", False, ""),
        ("25 Years of Pro Audio", "25-years-of-pro-audio", True, ""),
        ("Multi-Room Recording Studios", "multi-room-recording-studios", True, ""),
        ("Back to School", "back-to-school", True, ""),
        ("Black Friday Microphone Deals", "black-friday-microphone-deals", True, ""),
        ("New at NAMM — Microphones", "new-at-namm-microphones", True, ""),
        ("Universal Audio Promotions", "universal-audio-promotions", True, ""),
        ("Avid Pro Tools Trade-In", "avid-pro-tools-trade-in", True, ""),
        ("Avid S4 Control Surface Configurations", "avid-s4-control-surface-configurations", True, ""),
        ("Avid S6 Control Surface Configurations", "avid-s6-control-surface-configurations", True, ""),
        ("Privacy Policy", "privacy-policy", True, "/policies/privacy-policy"),
        ("Shipping Policy", "shipping-policy", True, "/policies/shipping-policy"),
        ("Returns", "returns", True, "/policies/refund-policy"),
        # Hall of Fame deep articles
        ("HOF — Neve 1073 (overview)", "neve-1073", False, ""),
        ("HOF — Neve 1073 Buyer's Guide", "neve-1073-guide", True, ""),
        ("HOF — Neve 1081", "neve-1081", True, ""),
        ("HOF — Neumann U47", "neumann-u47", False, ""),
        ("HOF — Neumann U67", "neumann-u67", False, ""),
        ("HOF — Neumann U47 FET", "neumann-u47-fet", True, ""),
        ("HOF — Neumann Mic Comparison", "neumann-mic-comparison", False, ""),
        ("HOF — Telefunken ELA-M 251", "telefunken-ela-m-251", True, ""),
        ("HOF — TAB Telefunken V72/V76", "tab-telefunken-v72-v76", True, ""),
        ("HOF — Coles 4038", "coles-4038", True, ""),
        ("HOF — Fairchild 660/670", "fairchild-660-670", False, ""),
        ("HOF — UREI 1176", "urei-1176", False, ""),
        ("HOF — LA-2A", "la-2a", False, ""),
        ("HOF — Universal Audio 175B", "universal-audio-175b", True, ""),
        ("HOF — Universal Audio Apollo X", "universal-audio-apollo-x", True, ""),
    ]
    for name, base, has_v2, vk_path in items:
        v2_file = f"{base}-v2.html"
        v1_file = f"{base}.html"
        primary = v2_file if has_v2 and (ROOT / v2_file).exists() else v1_file
        meta = extract(ROOT / primary)
        define = define_for(meta, name)
        comments = ""
        add1 = ("", "")
        if has_v2 and (ROOT / v1_file).exists() and primary == v2_file:
            add1 = labeled_link("v1 (older variant)", url(v1_file))
            comments = "v2 is current; v1 kept for reference and may move to /archive/."
        vk_equiv = f"https://www.vintageking.com{vk_path}" if vk_path else ""
        rows.append(row(name, url(primary), define, comments, add1, ("",""), vk_equiv))
    return rows

def tab_prototype_demos():
    """Core ecommerce screens — extracted from main prototype as standalone files."""
    rows = []
    # Reference to the live core demo prototype
    rows.append(row(
        "Core single-file prototype (latest)",
        f"{CORE}/VintageKing-Redesign-v2_67-Mar2026.html",
        "Full single-file VK redesign prototype — homepage, category, product, FAQ, deals, sell/trade, studio installs, tech shop, financing, open box. All 10 core ecommerce screens in one HTML page-switcher.",
        "Source of truth for core ecommerce screens. DO NOT EDIT from this repo.",
        labeled_link("Mega-menu demo", f"{CORE}/mega-menu/VintageKing-MegaMenu-CursorLab-v2.html"),
        labeled_link("Filter / PLP demo (v4)", f"{CORE}/mega-menu/VK-Microphones-CategoryDemo-v4-refined.html"),
        "https://www.vintageking.com",
    ))
    pages = [
        ("Homepage", "pages/home.html", "https://www.vintageking.com"),
        ("Category page", "pages/category.html", "https://www.vintageking.com/collections/microphones"),
        ("Product page", "pages/product.html", "https://www.vintageking.com/products/"),
        ("FAQ", "pages/faq.html", "https://www.vintageking.com/pages/faq"),
        ("Demo Deals", "pages/deals.html", "https://www.vintageking.com/collections/demo-deals"),
        ("Sell or Trade", "pages/sell.html", "https://www.vintageking.com/sell-or-trade"),
        ("Studio Installations", "pages/studio.html", "https://www.vintageking.com/studio-design"),
        ("Tech Shop", "pages/techshop.html", "https://www.vintageking.com/tech-shop"),
        ("Financing", "pages/financing.html", "https://www.vintageking.com/financing"),
        ("Open Box", "pages/openbox.html", "https://www.vintageking.com/collections/open-box"),
    ]
    for name, rel, vk in pages:
        meta = extract(ROOT / rel)
        rows.append(row(name, url(rel), define_for(meta, name),
                        "Standalone extract from core prototype.", ("",""), ("",""), vk))
    return rows

def tab_reference_tools():
    rows = []
    items = [
        ("All Pages (navigator) — start here", "navigator.html",
         "Master index of every demo, page, and tool. Open this first.", ""),
        ("Style Guide — design rules", "style-guide.html",
         "Color tokens, typography scale, badge system (two families: editorial + product card, tinted + outline), spacing, accent rules, no-go list, JSON-LD library.", ""),
        ("Page Layouts — the Lego catalog", "page-layouts.html",
         "Every layout pattern in one place: 4 light heroes, 2 dark heroes, 4 PLP variants, body modules, when-to-use rules, live demo links.", ""),
        ("Page Templates Guide", "templates-guide.html",
         "Agency hand-off: 3 hero variants (A, B, C), 2 body modules (Big, Dual), 2 strips (trust, explore), color tokens, decision rules.", "Likely to move into /archive/ once Page Layouts coverage is confirmed."),
        ("Repo index", "index.html",
         "Repo landing page.", ""),
        ("Source pages (all built secondary content)", "VK-secondary-pages-source.html",
         "Combined source containing copy, hero patterns, and JSON-LD blocks for all secondary pages built so far.", ""),
        ("Open new pages (helper)", "open-new-pages.html",
         "Helper page that opens recently built pages in new tabs.", ""),
    ]
    for name, rel, define, comments in items:
        rows.append(row(name, url(rel), define, comments))
    # Repo docs (markdown) — hosted on GitHub, not GH Pages
    repo_base = "https://github.com/barreletics/vk-secondary-pages/blob/main"
    md_items = [
        ("HANDOFF.md — repo brief", f"{repo_base}/HANDOFF.md",
         "Project guardrails, file inventory, page templates, build rules.", ""),
        ("CLAUDE.md — design system rules", f"{repo_base}/CLAUDE.md",
         "Full design system briefing for AI agents. Read before every edit.", ""),
        ("README.md", f"{repo_base}/README.md",
         "How to open the navigator locally and use the repo.", ""),
    ]
    for name, link, define, comments in md_items:
        rows.append(row(name, link, define, comments))
    return rows

def tab_plp_variants():
    rows = []
    rows.append(row(
        "Page Layouts — overview (Lego catalog)",
        url("page-layouts.html"),
        "Complete catalog of layout patterns — heroes, PLP variants, body modules, badges. Use this to pick a layout, then jump to the live demo.",
        "Cross-listed in Reference & Tools tab.",
    ))
    items = [
        ("Microphones — PLP Default (dark strip)", "microphones-plp-default.html",
         "Dark band hero, no image, headline + lede + 2 CTAs, pill filter row + inline quick filters, 3-up product grid, trust strip. Default for all category landings.",
         "Recommended default."),
        ("Microphones — PLP Spotlight (large)", "microphones-plp-spotlight.html",
         "Dark 50/50 hero, co-op pill, big featured photo right, single featured item meta, pill filter row, 3-up grid. Brand spotlight / partner weeks.",
         "Under team A/B vs Spotlight Compact — pick one within the week, archive the other."),
        ("Microphones — PLP Spotlight Compact", "microphones-plp-spotlight-compact.html",
         "Same content as Spotlight — hero shrunk to ~440px so pill filters land above the fold on standard laptops.",
         "Under team A/B vs Spotlight large — pick one within the week, archive the other."),
        ("Microphones — PLP Editorial (light six-grid)", "microphones-plp-editorial.html",
         "Hero 2 with product grid right side, 6 curated picks, curator notes 3-up, dark process strip, CTA back to full catalog. Opt-in for drops, campaigns, staff picks.", ""),
    ]
    vk_cat = "https://www.vintageking.com/collections/microphones"
    for name, rel, define, comments in items:
        rows.append(row(name, url(rel), define, comments,
                        labeled_link("Page Layouts catalog", url("page-layouts.html#plp")),
                        ("",""), vk_cat))
    return rows

def tab_archive():
    """Archive folder not yet created (pending Phase 4 of buffet reorg).
    List candidates here so team has visibility."""
    rows = []
    rows.append(row(
        "(folder not yet created — pending buffet reorg Phase 4)",
        "",
        "v1 duplicates of secondary pages and the old templates-guide.html will be moved into /archive/ once the new dashboard ships. Until then they remain in repo root and are listed as 'Additional Link 1' on their v2 row in the Pages tab.",
        "No action required from team — internal cleanup.",
    ))
    # List every -v2.html that has a v1 sibling so team can see what's slated for archive
    v1_candidates = sorted([p.name for p in ROOT.glob("*.html")
                            if not p.name.endswith("-v2.html")
                            and (ROOT / p.name.replace(".html", "-v2.html")).exists()])
    for v1 in v1_candidates:
        meta = extract(ROOT / v1)
        rows.append(row(
            f"[archive candidate] {v1}",
            url(v1),
            define_for(meta, v1),
            "Older v1 — superseded by v2 of same name. Currently live; will move to /archive/.",
            labeled_link("Current v2", url(v1.replace(".html", "-v2.html"))),
        ))
    rows.append(row(
        "[archive candidate] templates-guide.html",
        url("templates-guide.html"),
        "Agency hand-off template guide. Superseded by page-layouts.html (the new Lego catalog).",
        "Will move to /archive/ once team confirms Page Layouts has full coverage.",
        labeled_link("Replacement", url("page-layouts.html")),
    ))
    return rows

# ---------- workbook ----------
HEADERS = [
    "Resource",
    "Live link (our prototype)",
    "Define resource",
    "Comments",
    "Additional link 1",
    "Additional link 2",
    "Vintageking.com equivalent (team to confirm)",
]
COL_WIDTHS = [42, 70, 70, 50, 60, 60, 50]

def style_sheet(ws):
    header_fill = PatternFill("solid", fgColor="1A1A18")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    border = Border(*([Side(style="thin", color="DDDDDD")] * 4))
    align = Alignment(vertical="top", wrap_text=True)
    for c, h in enumerate(HEADERS, 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(vertical="center", horizontal="left")
        ws.column_dimensions[get_column_letter(c)].width = COL_WIDTHS[c-1]
    ws.row_dimensions[1].height = 28
    ws.freeze_panes = "A2"
    return border, align

def write_rows(ws, rows):
    border, align = style_sheet(ws)
    link_font = Font(color="C0392B", underline="single")
    for r, row_data in enumerate(rows, 2):
        for c, val in enumerate(row_data, 1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.alignment = align
            cell.border = border
            if c in (2, 7) and val and val.startswith("http"):
                cell.hyperlink = val
                cell.font = link_font
            elif c in (5, 6) and val and " — http" in val:
                # "Label — URL" — make the URL clickable
                u = val.split(" — ", 1)[1]
                cell.hyperlink = u
                cell.font = link_font
        # row height
        ws.row_dimensions[r].height = 60

def main():
    wb = Workbook()
    wb.remove(wb.active)
    sheets = [
        ("Pages", tab_pages()),
        ("Prototype demos", tab_prototype_demos()),
        ("Reference & tools", tab_reference_tools()),
        ("Page Layouts & PLP variants", tab_plp_variants()),
        ("Archive", tab_archive()),
    ]
    for name, rows in sheets:
        ws = wb.create_sheet(name)
        write_rows(ws, rows)
    out = ROOT / "vk-resources-inventory.xlsx"
    wb.save(out)
    total = sum(len(r) for _, r in sheets)
    print(f"wrote {out}")
    print(f"  sheets: {len(sheets)}  rows: {total}")
    for name, rows in sheets:
        print(f"  - {name}: {len(rows)} rows")

if __name__ == "__main__":
    main()
