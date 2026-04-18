#!/usr/bin/env python3
"""Bulk CSS hardening for secondary pages.

Targets the shared inline CSS injected during the v3 rollout:
  - Explore strip: cards as flex columns; CTA pinned to bottom (button line aligned)
  - Dual photo strip: figure slot flex column; photo box width 100% with safe sizing
  - Inject minimal pg-wrap/pg-section/pg-eyebrow primitives ONLY where the markup
    uses them but the page never defined them (e.g. multi-room v2, 25-years v2).

Idempotent: re-running on patched files is a no-op.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_GRID = ".pg-explore-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}"
NEW_GRID = ".pg-explore-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;align-items:stretch}"

OLD_CARD = (
    ".pg-explore-card{background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;"
    "text-decoration:none;display:block;transition:transform 0.18s,box-shadow 0.18s;border-radius:3px}"
)
NEW_CARD = (
    ".pg-explore-card{background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;"
    "text-decoration:none;display:flex;flex-direction:column;min-height:100%;"
    "box-sizing:border-box;transition:transform 0.18s,box-shadow 0.18s;border-radius:3px}"
)

OLD_CTA = (
    ".pg-explore-cta{margin-top:16px;font-size:12px;font-weight:700;"
    "color:var(--page-accent);letter-spacing:0.06em}"
)
NEW_CTA = (
    ".pg-explore-cta{margin-top:auto;padding-top:16px;font-size:12px;font-weight:700;"
    "color:var(--page-accent);letter-spacing:0.06em}"
)

OLD_PHOTO_SLOT = ".pg-photo-slot{margin:0}"
NEW_PHOTO_SLOT = ".pg-photo-slot{margin:0;display:flex;flex-direction:column;align-items:stretch}"

OLD_PHOTO_PREFIX = (
    ".pg-photo{background:var(--off-white);border:1px solid rgba(26,26,24,0.08);"
    "border-radius:3px;aspect-ratio:1/1;max-width:580px;display:flex;"
)
NEW_PHOTO_PREFIX = (
    ".pg-photo{background:var(--off-white);border:1px solid rgba(26,26,24,0.08);"
    "border-radius:3px;aspect-ratio:1/1;width:100%;max-width:580px;"
    "box-sizing:border-box;display:flex;"
)

PG_PRIMITIVES = (
    "/* pg-section primitives (dual-photo blocks) */\n"
    ".pg-wrap{max-width:1160px;margin:0 auto;padding:0 40px}\n"
    ".pg-eyebrow{font-family:var(--font-body);font-size:11px;font-weight:700;"
    "letter-spacing:0.22em;text-transform:uppercase;color:var(--page-accent);margin-bottom:14px}\n"
    ".pg-section{padding:80px 0}\n"
    ".pg-section-off{background:var(--off-white)}\n"
    ".pg-section-white{background:#fff}\n"
)


def needs_primitives(html: str) -> bool:
    return (
        'class="pg-wrap"' in html
        and ".pg-wrap{" not in html
        and "pg-section primitives" not in html
    )


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if OLD_GRID not in text and ".pg-photo-slot{" not in text and not needs_primitives(text):
        return False
    new = text
    for old, replacement in (
        (OLD_GRID, NEW_GRID),
        (OLD_CARD, NEW_CARD),
        (OLD_CTA, NEW_CTA),
        (OLD_PHOTO_SLOT, NEW_PHOTO_SLOT),
        (OLD_PHOTO_PREFIX, NEW_PHOTO_PREFIX),
    ):
        if old in new:
            new = new.replace(old, replacement)
    if needs_primitives(new):
        anchor = ".pg-hero-img-v2{"
        idx = new.find(anchor)
        if idx != -1:
            new = new[:idx] + PG_PRIMITIVES + new[idx:]
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for path in sorted(ROOT.glob("*.html")):
        if patch_file(path):
            changed.append(path.name)
    for name in changed:
        print(name)
    print(f"Patched {len(changed)} files")


if __name__ == "__main__":
    main()
