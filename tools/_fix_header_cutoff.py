"""One-shot patch: fix header right-side cutoff across all secondary pages.

Two changes per file:
1. .nav-search-wrap input: width:180px -> width:140px (gives 40px back to nav)
2. .nav-items: add min-width:0 (lets flex items shrink instead of overflowing)

Also patches tools/build_remaining_pages.py so future regenerations get the fix.
Skips pages/* (main prototype split files) and VK-secondary-pages-source.html.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Patterns handle both compact ("width:180px") and spaced ("width: 180px;") formats.
SEARCH_INPUT_RE = re.compile(r"(\.nav-search-wrap\s+input\s*\{[^}]*?width:\s*)180(px)")
NAV_ITEMS_FLEX1_COMPACT_RE = re.compile(r"(\.nav-items\s*\{[^}]*?flex:\s*1)(\})")
NAV_ITEMS_FLEX1_SPACED_RE = re.compile(r"(\.nav-items\s*\{[^}]*?flex:\s*1;)(\s*\})")

SKIP_PREFIXES = ("pages/",)
SKIP_FILES = {"VK-secondary-pages-source.html"}

NAV_ITEMS_HAS_MINWIDTH_RE = re.compile(r"\.nav-items\s*\{[^}]*?min-width:\s*0")

def patch_text(text: str) -> tuple[str, int]:
    changes = 0
    new_text, n1 = SEARCH_INPUT_RE.subn(r"\g<1>140\g<2>", text)
    changes += n1
    if not NAV_ITEMS_HAS_MINWIDTH_RE.search(new_text):
        new_text, n2 = NAV_ITEMS_FLEX1_COMPACT_RE.subn(r"\g<1>;min-width:0\g<2>", new_text)
        changes += n2
        new_text, n3 = NAV_ITEMS_FLEX1_SPACED_RE.subn(r"\g<1> min-width: 0;\g<2>", new_text)
        changes += n3
    return new_text, changes

def main():
    touched = []
    for path in sorted(ROOT.glob("*.html")):
        if path.name in SKIP_FILES:
            continue
        original = path.read_text(encoding="utf-8")
        if ".nav-search-wrap" not in original:
            continue
        new_text, changes = patch_text(original)
        if changes > 0 and new_text != original:
            path.write_text(new_text, encoding="utf-8")
            touched.append((path.name, changes))

    builder = ROOT / "tools" / "build_remaining_pages.py"
    if builder.exists():
        b_orig = builder.read_text(encoding="utf-8")
        b_new = b_orig.replace(
            ".nav-search-wrap input{border:none;background:none;font-family:var(--font-body);font-size:12.5px;color:var(--charcoal);outline:none;width:180px}",
            ".nav-search-wrap input{border:none;background:none;font-family:var(--font-body);font-size:12.5px;color:var(--charcoal);outline:none;width:140px}",
        ).replace(
            ".nav-items{display:flex;align-items:stretch;height:100%;list-style:none;flex:1}",
            ".nav-items{display:flex;align-items:stretch;height:100%;list-style:none;flex:1;min-width:0}",
        )
        if b_new != b_orig:
            builder.write_text(b_new, encoding="utf-8")
            touched.append(("tools/build_remaining_pages.py", 2))

    print(f"Patched {len(touched)} file(s):")
    for name, n in touched:
        print(f"  {n} change(s) in {name}")

if __name__ == "__main__":
    main()
