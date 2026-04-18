#!/usr/bin/env python3
"""Roll the Hero A (split-bleed 50/50) patch across every *-v2.html page.

Idempotent: if the <style id="hero-a-patch"> block is already present, the
script leaves the file alone.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HERO_A_BLOCK = """<style id=\"hero-a-patch\">
/* Hero A — Split Bleed. Text left on #EDE8E2, photo right edge-to-edge to viewport. */
.pg-hero{padding:0;border-bottom:1px solid rgba(26,26,24,0.06);background:linear-gradient(to right,#EDE8E2 50%,#FFFFFF 50%)}
.pg-hero-inner{max-width:none;padding:0;grid-template-columns:1fr 1fr;gap:0;min-height:600px;align-items:stretch}
.pg-hero-inner > div:first-child{padding:96px 64px 96px max(40px, calc((100vw - 1160px) / 2 + 40px));display:flex;flex-direction:column;justify-content:center}
.pg-hero-img-v2{min-height:600px;border:none;border-radius:0;background:#FFFFFF;height:100%}
@media(max-width:980px){
  .pg-hero{background:#EDE8E2}
  .pg-hero-inner{grid-template-columns:1fr;min-height:auto}
  .pg-hero-inner > div:first-child{padding:60px 24px 40px}
  .pg-hero-img-v2{min-height:360px;background:#FFFFFF}
}
</style>
</head>"""


def patch(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "hero-a-patch" in text:
        return False
    if "</head>" not in text:
        return False
    new = text.replace("</head>", HERO_A_BLOCK, 1)
    path.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for path in sorted(ROOT.glob("*-v2.html")):
        if patch(path):
            changed.append(path.name)
    for name in changed:
        print(name)
    print(f"Patched {len(changed)} V2 pages")


if __name__ == "__main__":
    main()
