"""Add inline-styled trust strip to every secondary page that doesn't have one.

Strip is inline-styled (no class) so it doesn't collide with bespoke page CSS.
Inserted directly after the FIRST closing `</section>` inside `<div class="page active">`.

Per-page preset (HOF gear / Program / Editorial / Campaign / Policy) controls the 4 items.
Skips pages already containing `class="pg-strip"`.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PRESETS = {
    "hof": [
        ("Inducted", "VK Hall of Fame"),
        ("Authorized dealer", "for all current versions"),
        ("Tech Shop", "service and restoration"),
        ("VK Warranty", "on every unit"),
    ],
    "program": [
        ("30+ Years", "outfitting pro studios"),
        ("Authorized dealer", "for hundreds of brands"),
        ("Account Manager", "dedicated, real human"),
        ("VK Warranty", "on every order"),
    ],
    "editorial": [
        ("30+ Years", "outfitting pro studios"),
        ("Authorized dealer", "for hundreds of brands"),
        ("Tech Shop", "service and restoration"),
        ("VK Warranty", "on every order"),
    ],
    "campaign": [
        ("Authorized dealer", "for all featured brands"),
        ("Free shipping", "on orders over $99"),
        ("30-day returns", "no restock fee"),
        ("VK Warranty", "on every order"),
    ],
}

PAGE_PRESET = {
    "fairchild-660-670.html": "hof",
    "la-2a.html": "hof",
    "neumann-u47.html": "hof",
    "neumann-u67.html": "hof",
    "neve-1073.html": "hof",
    "neve-1073-guide.html": "hof",
    "neve-1073-guide-v2.html": "hof",
    "urei-1176.html": "hof",
    "audio-consultants.html": "program",
    "careers.html": "program",
    "studio-professionals.html": "program",
    "trade-program.html": "program",
    "vk-credit-card.html": "program",
    "section-179.html": "program",
    "about.html": "editorial",
    "classic-studios-gone-modern.html": "editorial",
    "hall-of-fame.html": "editorial",
    "live-sound-how.html": "editorial",
    "make-your-mark.html": "editorial",
    "multi-room-recording-studios.html": "editorial",
    "multi-room-recording-studios-v2.html": "editorial",
    "neumann-mic-comparison.html": "editorial",
    "playback.html": "editorial",
    "recording-at-home.html": "editorial",
    "25-years-of-pro-audio.html": "editorial",
    "25-years-of-pro-audio-v2.html": "editorial",
    "warranty.html": "editorial",
    "returns.html": "editorial",
    "returns-v2.html": "editorial",
    "shipping-policy.html": "editorial",
    "shipping-policy-v2.html": "editorial",
    "privacy-policy.html": "editorial",
    "privacy-policy-v2.html": "editorial",
}

def build_strip(preset_key: str) -> str:
    items = PRESETS[preset_key]
    item_html = "".join(
        f'<div style="display:flex;align-items:center;gap:8px;font-size:13px;color:rgba(26,26,24,0.65)">'
        f'<strong style="color:#1A1A18;font-weight:600">{strong}</strong> · {sub}</div>'
        for strong, sub in items
    )
    return (
        '\n  <!-- TRUST STRIP (rolled out) -->\n'
        '  <section style="background:#FFFFFF;border-top:1px solid rgba(26,26,24,0.08);'
        'border-bottom:1px solid rgba(26,26,24,0.08);padding:18px 0;font-family:\'DM Sans\',sans-serif">\n'
        '    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:flex;'
        f'justify-content:space-between;gap:24px;flex-wrap:wrap">{item_html}</div>\n'
        '  </section>\n'
    )

PAGE_ACTIVE_RE = re.compile(r'(<div[^>]*class="[^"]*page\s+active[^"]*"[^>]*>)', re.IGNORECASE)
SECTION_CLOSE_RE = re.compile(r'</section>', re.IGNORECASE)

def insert_after_first_section(text: str, strip_html: str) -> str | None:
    m = PAGE_ACTIVE_RE.search(text)
    if not m:
        return None
    start = m.end()
    s = SECTION_CLOSE_RE.search(text, start)
    if not s:
        return None
    insert_at = s.end()
    return text[:insert_at] + strip_html + text[insert_at:]

def main():
    touched = []
    skipped = []
    for name, preset in PAGE_PRESET.items():
        path = ROOT / name
        if not path.exists():
            skipped.append((name, "missing"))
            continue
        text = path.read_text(encoding="utf-8")
        if 'class="pg-strip"' in text or 'TRUST STRIP (rolled out)' in text:
            skipped.append((name, "already has strip"))
            continue
        new_text = insert_after_first_section(text, build_strip(preset))
        if new_text is None:
            skipped.append((name, "no insertion point"))
            continue
        path.write_text(new_text, encoding="utf-8")
        touched.append((name, preset))

    print(f"Added trust strip to {len(touched)} page(s):")
    for n, p in touched:
        print(f"  [{p:9}] {n}")
    if skipped:
        print(f"\nSkipped {len(skipped)} page(s):")
        for n, why in skipped:
            print(f"  [{why}] {n}")

if __name__ == "__main__":
    main()
