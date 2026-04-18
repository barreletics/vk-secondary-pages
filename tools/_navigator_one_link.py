#!/usr/bin/env python3
"""Merge v1+v2 navigator rows into one link (href -> -v2, label stays canonical). Repo column synced."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAV = ROOT / "navigator.html"

# page-url: first link + v2 chip -> single link
DUAL = re.compile(
    r'<a href="([^"/]+\.html)" target="_blank" rel="noopener" style="color:var\(--vk-red\);text-decoration:none;font-weight:500">'
    r'([^<]+</a>)'
    r'<span style="color:rgba\(255,255,255,0\.25\);margin:0 8px">·</span>'
    r'<a href="([^"]+)" target="_blank" rel="noopener" style="color:#D4860A;text-decoration:none;font-weight:600;font-size:11px;letter-spacing:0\.06em;text-transform:uppercase">v2 ↗</a>'
)


def merge_dual(m: re.Match) -> str:
    v1, inner, v2 = m.group(1), m.group(2), m.group(3)
    if not v2.endswith("-v2.html"):
        return m.group(0)
    return (
        f'<a href="{v2}" target="_blank" rel="noopener" style="color:var(--vk-red);text-decoration:none;font-weight:500">'
        f"{inner}"
    )


# Repo column: point href at v2, keep label as canonical basename
REPO_PAIRS: list[tuple[str, str]] = [
    ("25-years-of-pro-audio.html", "25-years-of-pro-audio-v2.html"),
    ("neve-1081.html", "neve-1081-v2.html"),
    ("telefunken-ela-m-251.html", "telefunken-ela-m-251-v2.html"),
    ("neumann-u47-fet.html", "neumann-u47-fet-v2.html"),
    ("coles-4038.html", "coles-4038-v2.html"),
    ("tab-telefunken-v72-v76.html", "tab-telefunken-v72-v76-v2.html"),
    ("universal-audio-175b.html", "universal-audio-175b-v2.html"),
    ("multi-room-recording-studios.html", "multi-room-recording-studios-v2.html"),
    ("avid-pro-tools-trade-in.html", "avid-pro-tools-trade-in-v2.html"),
    ("avid-s4-control-surface-configurations.html", "avid-s4-control-surface-configurations-v2.html"),
    ("avid-s6-control-surface-configurations.html", "avid-s6-control-surface-configurations-v2.html"),
    ("universal-audio-promotions.html", "universal-audio-promotions-v2.html"),
    ("universal-audio-apollo-x.html", "universal-audio-apollo-x-v2.html"),
    ("black-friday-microphone-deals.html", "black-friday-microphone-deals-v2.html"),
    ("new-at-namm-microphones.html", "new-at-namm-microphones-v2.html"),
    ("back-to-school.html", "back-to-school-v2.html"),
    ("shipping-policy.html", "shipping-policy-v2.html"),
    ("returns.html", "returns-v2.html"),
    ("privacy-policy.html", "privacy-policy-v2.html"),
]


def patch_repo(text: str) -> str:
    for canon, v2 in REPO_PAIRS:
        old = f'Yes — <a href="{canon}" target="_blank" rel="noopener" style="color:#27ae60">{canon} ↗</a>'
        new = f'Yes — <a href="{v2}" target="_blank" rel="noopener" style="color:#27ae60">{canon} ↗</a>'
        if old not in text:
            raise SystemExit(f"Expected repo snippet missing for {canon}")
        text = text.replace(old, new, 1)
    return text


def main() -> None:
    text = NAV.read_text(encoding="utf-8")
    text2, n = DUAL.subn(merge_dual, text)
    print(f"merge_dual replacements: {n}")
    text3 = patch_repo(text2)
    NAV.write_text(text3, encoding="utf-8")
    print(f"Wrote {NAV}")


if __name__ == "__main__":
    main()
