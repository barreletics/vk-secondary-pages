"""Hero variant rollout:

1. Bump v2 hero image slot from min-height:380px -> 520px (all v2 pages + builder).
2. Append V3 stack to 9 HOF v2 pages: big contained gear photo + spec strip
   inserted directly after the trust strip.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HOF_V2_PAGES = {
    "neumann-u47-fet-v2.html": {
        "title": "Neumann U47 FET",
        "specs": [("1972", "Year"), ("K47", "Capsule"), ("FET", "Solid-state"), ("140 dB", "Max SPL"), ("Cardioid", "Pattern")],
        "caption": "Neumann U47 FET — solid-state successor to the legendary U47 tube. Reissued by Neumann to original spec.",
    },
    "neve-1081-v2.html": {
        "title": "Neve 1081",
        "specs": [("1972", "Year"), ("Class A", "Topology"), ("Marinair", "Transformers"), ("4-Band", "Stepped EQ"), ("VK HOF", "Inductee")],
        "caption": "AMS Neve 1081 — the four-band cousin to the 1073. Found in AIR, Trident, and Olympic studios from the early 1970s onward.",
    },
    "coles-4038-v2.html": {
        "title": "Coles 4038",
        "specs": [("1955", "Year"), ("Ribbon", "Element"), ("Bidirectional", "Pattern"), ("BBC", "Designed for"), ("VK HOF", "Inductee")],
        "caption": "Coles 4038 — designed by the BBC for studio broadcast in 1955. Still hand-built in England to original spec.",
    },
    "tab-telefunken-v72-v76-v2.html": {
        "title": "Telefunken V72 / V76",
        "specs": [("1950s", "Era"), ("Tube", "Topology"), ("Telefunken", "Origin"), ("Broadcast", "Original use"), ("VK HOF", "Inductee")],
        "caption": "TAB / Telefunken V72 and V76 — German broadcast preamps that defined the warmth of European recording from the 1950s on.",
    },
    "telefunken-ela-m-251-v2.html": {
        "title": "Telefunken ELA M 251",
        "specs": [("1959", "Year"), ("Tube", "Topology"), ("CK12", "Capsule"), ("6072a", "Tube"), ("VK HOF", "Inductee")],
        "caption": "Telefunken ELA M 251 — the most coveted vocal microphone ever made. Hand-built reissues to original spec.",
    },
    "universal-audio-175b-v2.html": {
        "title": "Universal Audio 175B",
        "specs": [("1959", "Year"), ("Tube", "Topology"), ("Variable-mu", "Compression"), ("UA", "Origin"), ("VK HOF", "Inductee")],
        "caption": "Universal Audio 175B — Bill Putnam's original tube compressor. The grandfather of every UA compressor since.",
    },
    "universal-audio-apollo-x-v2.html": {
        "title": "Universal Audio Apollo X",
        "specs": [("Modern", "Era"), ("HEXA Core", "DSP"), ("Unison", "Preamp tech"), ("Thunderbolt", "Connection"), ("UAD-2", "Plugin engine")],
        "caption": "Universal Audio Apollo X — the working interface for thousands of pro studios. UAD plugin processing built in.",
    },
    "neve-1073-guide-v2.html": {
        "title": "Neve 1073 Guide",
        "specs": [("1970", "Year"), ("Class A", "Topology"), ("Marinair", "Transformers"), ("3-Band", "Stepped EQ"), ("VK HOF", "Inductee")],
        "caption": "AMS Neve 1073 — the Class A preamp and EQ module that defined modern recording from 1970 to today.",
    },
}

def big_photo_block(caption: str) -> str:
    return (
        '\n<!-- HERO V3 — big contained gear photo -->\n'
        '<section style="background:#fff;padding:64px 0 48px">\n'
        '  <div style="max-width:1160px;margin:0 auto;padding:0 40px">\n'
        '    <div style="min-height:520px;background:#F7F5F2;border:1px solid rgba(26,26,24,0.08);'
        'display:flex;align-items:center;justify-content:center;border-radius:3px">\n'
        '      <div style="text-align:center;font-family:\'DM Sans\',sans-serif">\n'
        '        <div style="font-size:11px;color:rgba(26,26,24,0.32);letter-spacing:0.12em;'
        'text-transform:uppercase;margin-bottom:8px">Hero gear photo \u2014 high resolution</div>\n'
        '        <div style="font-size:12px;color:rgba(26,26,24,0.22)">1160 \u00d7 520 recommended</div>\n'
        '      </div>\n'
        '    </div>\n'
        f'    <p style="margin-top:14px;text-align:center;font-size:12px;color:rgba(26,26,24,0.50);'
        f'font-family:\'DM Sans\',sans-serif;letter-spacing:0.04em">{caption}</p>\n'
        '  </div>\n'
        '</section>\n'
    )

def spec_strip(specs: list[tuple[str, str]]) -> str:
    items_html = ""
    for i, (val, lab) in enumerate(specs):
        if i > 0:
            items_html += '<div style="width:1px;height:24px;background:rgba(26,26,24,0.10)"></div>'
        items_html += (
            '<div style="display:flex;align-items:center;gap:10px">'
            f'<span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:\'DM Sans\',sans-serif">{val}</span>'
            f'<span style="font-size:13px;color:rgba(26,26,24,0.55);font-family:\'DM Sans\',sans-serif">{lab}</span>'
            '</div>'
        )
    return (
        '\n<!-- HERO V3 — spec strip -->\n'
        '<section style="background:#FDFCFB;border-top:1px solid rgba(26,26,24,0.08);'
        'border-bottom:1px solid rgba(26,26,24,0.08);padding:18px 0">\n'
        f'  <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:flex;gap:36px;'
        f'flex-wrap:wrap;align-items:center;justify-content:center">{items_html}</div>\n'
        '</section>\n'
    )

V2_HERO_SLOT_RE = re.compile(r'(\.pg-hero-img-v2\{[^}]*?min-height:)380(px)')

def bump_hero_slot():
    builder = ROOT / "tools" / "build_remaining_pages.py"
    if builder.exists():
        b_orig = builder.read_text(encoding="utf-8")
        b_new = V2_HERO_SLOT_RE.sub(r"\g<1>520\g<2>", b_orig)
        if b_new != b_orig:
            builder.write_text(b_new, encoding="utf-8")
            print("Bumped builder script: tools/build_remaining_pages.py")

    bumped = []
    for path in sorted(ROOT.glob("*-v2.html")):
        original = path.read_text(encoding="utf-8")
        if "pg-hero-img-v2" not in original:
            continue
        new_text = V2_HERO_SLOT_RE.sub(r"\g<1>520\g<2>", original)
        if new_text != original:
            path.write_text(new_text, encoding="utf-8")
            bumped.append(path.name)
    print(f"Bumped hero slot 380->520px on {len(bumped)} v2 page(s)")

V3_MARKER = "HERO V3 \u2014 big contained gear photo"

def append_v3_to_hof():
    added = []
    skipped = []
    trust_strip_marker = '<!-- TRUST STRIP'
    pg_strip_open = '<div class="pg-strip">'
    for name, info in HOF_V2_PAGES.items():
        path = ROOT / name
        if not path.exists():
            skipped.append((name, "missing"))
            continue
        text = path.read_text(encoding="utf-8")
        if V3_MARKER in text:
            skipped.append((name, "already V3"))
            continue
        idx = text.find(pg_strip_open)
        if idx < 0:
            idx = text.find(trust_strip_marker)
            if idx < 0:
                skipped.append((name, "no trust strip"))
                continue
        end_idx = text.find("</div></div>", idx)
        if end_idx < 0:
            end_idx = text.find("</section>", idx)
            if end_idx < 0:
                skipped.append((name, "no strip close"))
                continue
            insert_at = end_idx + len("</section>")
        else:
            insert_at = end_idx + len("</div></div>")
        v3_block = big_photo_block(info["caption"]) + spec_strip(info["specs"])
        new_text = text[:insert_at] + v3_block + text[insert_at:]
        path.write_text(new_text, encoding="utf-8")
        added.append(name)
    print(f"\nAdded V3 stack to {len(added)} HOF v2 page(s):")
    for n in added:
        print(f"  {n}")
    if skipped:
        print(f"\nSkipped {len(skipped)} HOF page(s):")
        for n, w in skipped:
            print(f"  [{w}] {n}")

def main():
    bump_hero_slot()
    append_v3_to_hof()

if __name__ == "__main__":
    main()
