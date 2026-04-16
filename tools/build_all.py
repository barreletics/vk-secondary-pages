#!/usr/bin/env python3
"""
build_all.py — Batch builder for VK secondary pages.

Usage:
    python3 tools/build_all.py --list          # show all pages and status
    python3 tools/build_all.py --build all     # build every planned page
    python3 tools/build_all.py --build trade-program audio-consultants
    python3 tools/build_all.py --dry-run all   # show what would be built, no write

Each page module lives in tools/pages/<slug>.py and must expose:
    build(src_html: str, head_css: str, nav_tpl: str, foot_tpl: str, js_nav: str) -> str
    SLUG   = "trade-program"
    TITLE  = "Trade Program — ..."
    META   = "..."
"""
import argparse, importlib, sys, time
from pathlib import Path

ROOT  = Path(__file__).resolve().parents[1]
SRC   = ROOT / "VK-secondary-pages-source.html"
PAGES = ROOT / "tools" / "pages"

# ── Registry: slug → output filename ──────────────────────────────────────────
REGISTRY = {
    "trade-program":       "trade-program.html",
    "audio-consultants":   "audio-consultants.html",
    "neve-1073":           "neve-1073.html",
    "neve-1073-guide":     "neve-1073-guide.html",
    "neve-1073-guide-v2":  "neve-1073-guide-v2.html",
    "fairchild-660-670":   "fairchild-660-670.html",
    "la-2a":               "la-2a.html",
    "neumann-u47":         "neumann-u47.html",
    "urei-1176":           "urei-1176.html",
    "neve-1081":           "neve-1081.html",
    "telefunken-251":      "telefunken-251.html",
    "neumann-u67":         "neumann-u67.html",
    "neumann-u47-fet":     "neumann-u47-fet.html",
    "coles-4038":          "coles-4038.html",
    "25-years":            "25-years.html",
    "style-guide":         "style-guide.html",
    "warranty":            "warranty.html",
    "section-179":         "section-179.html",
}

def slice_lines(path, start, end):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    return "".join(lines[start - 1 : end])

def load_shared():
    src = SRC.read_text(encoding="utf-8")
    head_css = slice_lines(SRC, 1, 1724)
    nav_tpl  = slice_lines(SRC, 1759, 2480)
    foot_tpl = slice_lines(SRC, 3869, 3978)
    js_nav   = slice_lines(SRC, 3980, 4074)
    return src, head_css, nav_tpl, foot_tpl, js_nav

def build_page(slug, dry_run=False):
    mod_name = slug.replace("-", "_")
    mod_path = PAGES / f"{mod_name}.py"
    if not mod_path.exists():
        print(f"  ⚠  No module: tools/pages/{mod_name}.py — skipping")
        return False

    if str(PAGES.parent) not in sys.path:
        sys.path.insert(0, str(PAGES.parent))
    mod = importlib.import_module(f"pages.{mod_name}")

    src, head_css, nav_tpl, foot_tpl, js_nav = load_shared()
    html = mod.build(src, head_css, nav_tpl, foot_tpl, js_nav)

    out = ROOT / REGISTRY[slug]
    if dry_run:
        print(f"  [dry-run] Would write {out.name} ({len(html)//1024} KB)")
        return True

    out.write_text(html, encoding="utf-8")
    print(f"  ✓  {out.name} ({out.stat().st_size // 1024} KB)")
    return True

def main():
    parser = argparse.ArgumentParser(description="VK batch page builder")
    parser.add_argument("--list",    action="store_true", help="List all pages")
    parser.add_argument("--build",   nargs="+", metavar="SLUG", help="Build pages (use 'all')")
    parser.add_argument("--dry-run", nargs="+", metavar="SLUG", help="Dry-run build")
    args = parser.parse_args()

    if args.list:
        built = {f.stem for f in ROOT.glob("*.html")}
        print(f"\n{'SLUG':<28} {'FILE':<30} STATUS")
        print("-" * 70)
        for slug, fname in REGISTRY.items():
            has_module = (PAGES / f"{slug.replace('-','_')}.py").exists()
            status = "✓ built" if Path(fname).stem in built else ("ready" if has_module else "needs module")
            print(f"  {slug:<26} {fname:<30} {status}")
        print()
        return

    targets = None
    dry = False

    if args.dry_run:
        targets = list(REGISTRY.keys()) if args.dry_run == ["all"] else args.dry_run
        dry = True
    elif args.build:
        targets = list(REGISTRY.keys()) if args.build == ["all"] else args.build

    if not targets:
        parser.print_help()
        return

    print(f"\nBuilding {len(targets)} page(s){'  [DRY RUN]' if dry else ''}...\n")
    ok = err = 0
    for slug in targets:
        if slug not in REGISTRY:
            print(f"  ✗  Unknown slug: {slug}")
            err += 1
            continue
        t = time.time()
        success = build_page(slug, dry_run=dry)
        elapsed = time.time() - t
        if success:
            ok += 1
            if not dry:
                print(f"     {elapsed:.1f}s")
        else:
            err += 1

    print(f"\nDone. {ok} built, {err} skipped/errored.\n")

if __name__ == "__main__":
    main()
