"""Add inline-styled Explore Vintage King strip just above the footer
on every secondary page that doesn't have one.

Inline styles only - no class collisions on bespoke manual pages.
Per-template-family card preset.
Skips pages already containing `pg-explore` or `EXPLORE STRIP (rolled out)`.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPLORE_PRESETS = {
    "hof": [
        ("Hall of Fame", "Legendary Gear and Rooms",
         "The consoles, microphones, and outboard that defined recording history.", "Browse all", "hall-of-fame.html"),
        ("Expert Consulting", "Talk to an Audio Consultant",
         "Our team has tracked sessions on this gear. Call, chat, or email.", "Call 888.653.1184", "audio-consultants.html"),
        ("Tech Shop", "Service and Restoration",
         "VK Tech Shop services, restores, and warranties pro audio gear in-house.", "Learn more", "warranty.html"),
    ],
    "program": [
        ("Expert Consulting", "Talk to an Audio Consultant",
         "Our team has tracked sessions on legendary gear. Call, chat, or email.", "Call 888.653.1184", "audio-consultants.html"),
        ("Trade Program", "Sell, trade, or upgrade",
         "Top-dollar appraisals on used pro audio gear. Fast offers, faster payment.", "Get an offer", "trade-program.html"),
        ("Hall of Fame", "Legendary Gear and Rooms",
         "The consoles, microphones, and outboard that defined recording history.", "Browse all", "hall-of-fame.html"),
    ],
    "editorial": [
        ("Hall of Fame", "Legendary Gear and Rooms",
         "The consoles, microphones, and outboard that defined recording history.", "Browse all", "hall-of-fame.html"),
        ("Expert Consulting", "Talk to an Audio Consultant",
         "Our team has tracked sessions on legendary gear. Call, chat, or email.", "Call 888.653.1184", "audio-consultants.html"),
        ("About VK", "Pro Audio Outfitter Since 1993",
         "Three decades of equipping pro studios. Family-owned, expert-led.", "Read more", "about.html"),
    ],
    "campaign": [
        ("Hall of Fame", "Legendary Gear and Rooms",
         "The consoles, microphones, and outboard that defined recording history.", "Browse all", "hall-of-fame.html"),
        ("Expert Consulting", "Talk to an Audio Consultant",
         "Real humans on the phone. Call, chat, or email.", "Call 888.653.1184", "audio-consultants.html"),
        ("Trade Program", "Sell, trade, or upgrade",
         "Top-dollar appraisals on used pro audio gear.", "Get an offer", "trade-program.html"),
    ],
}

PAGE_PRESET = {
    "fairchild-660-670.html": "hof",
    "la-2a.html": "hof",
    "neumann-u47.html": "hof",
    "neumann-u67.html": "hof",
    "neve-1073.html": "hof",
    "neve-1073-guide.html": "hof",
    "urei-1176.html": "hof",
    "neumann-u47-fet.html": "hof",
    "neve-1081.html": "hof",
    "coles-4038.html": "hof",
    "tab-telefunken-v72-v76.html": "hof",
    "telefunken-ela-m-251.html": "hof",
    "universal-audio-175b.html": "hof",
    "universal-audio-apollo-x.html": "hof",
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
    "neumann-mic-comparison.html": "editorial",
    "playback.html": "editorial",
    "recording-at-home.html": "editorial",
    "25-years-of-pro-audio.html": "editorial",
    "warranty.html": "editorial",
    "returns.html": "editorial",
    "shipping-policy.html": "editorial",
    "privacy-policy.html": "editorial",
    "black-friday-microphone-deals.html": "campaign",
    "back-to-school.html": "campaign",
    "new-at-namm-microphones.html": "campaign",
    "universal-audio-promotions.html": "campaign",
    "avid-pro-tools-trade-in.html": "campaign",
    "avid-s4-control-surface-configurations.html": "campaign",
    "avid-s6-control-surface-configurations.html": "campaign",
}

CARD_TPL = (
    '<a href="{href}" style="background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;'
    'text-decoration:none;display:block;border-radius:3px;color:inherit">'
    '<div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;'
    'color:#C0392B;margin-bottom:10px;font-family:\'DM Sans\',sans-serif">{eyebrow}</div>'
    '<div style="font-family:\'Playfair Display\',serif;font-size:19px;font-weight:700;'
    'color:#1A1A18;margin-bottom:8px;line-height:1.3">{title}</div>'
    '<div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6;'
    'font-family:\'DM Sans\',sans-serif">{body}</div>'
    '<div style="margin-top:16px;font-size:12px;font-weight:700;color:#C0392B;'
    'letter-spacing:0.06em;font-family:\'DM Sans\',sans-serif">{cta} \u2192</div>'
    '</a>'
)

def build_strip(preset_key: str) -> str:
    cards = EXPLORE_PRESETS[preset_key]
    cards_html = "".join(
        CARD_TPL.format(eyebrow=e, title=t, body=b, cta=c, href=h)
        for e, t, b, c, h in cards
    )
    return (
        '\n<!-- EXPLORE STRIP (rolled out) -->\n'
        '<section style="background:#F7F5F2;padding:64px 0;border-top:1px solid rgba(26,26,24,0.07);'
        'font-family:\'DM Sans\',sans-serif">\n'
        '  <div style="max-width:1280px;margin:0 auto;padding:0 40px">\n'
        '    <div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;'
        'color:#C0392B;margin-bottom:10px">Explore Vintage King</div>\n'
        '    <h2 style="font-family:\'Playfair Display\',serif;font-size:28px;font-weight:700;'
        'color:#1A1A18;margin:0 0 28px">More from VK</h2>\n'
        f'    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">{cards_html}</div>\n'
        '  </div>\n'
        '</section>\n'
    )

FOOTER_RE = re.compile(r'(<footer[^>]*>|<div\s+id="footer-[^"]*"[^>]*>)', re.IGNORECASE)

def main():
    touched = []
    skipped = []
    for name, preset in PAGE_PRESET.items():
        path = ROOT / name
        if not path.exists():
            skipped.append((name, "missing"))
            continue
        text = path.read_text(encoding="utf-8")
        if "pg-explore" in text or "EXPLORE STRIP (rolled out)" in text:
            skipped.append((name, "already has explore"))
            continue
        m = FOOTER_RE.search(text)
        if not m:
            skipped.append((name, "no footer marker"))
            continue
        insert_at = m.start()
        new_text = text[:insert_at] + build_strip(preset) + text[insert_at:]
        path.write_text(new_text, encoding="utf-8")
        touched.append((name, preset))

    print(f"Added explore strip to {len(touched)} page(s):")
    for n, p in touched:
        print(f"  [{p:9}] {n}")
    if skipped:
        print(f"\nSkipped {len(skipped)} page(s):")
        for n, why in skipped:
            print(f"  [{why}] {n}")

if __name__ == "__main__":
    main()
