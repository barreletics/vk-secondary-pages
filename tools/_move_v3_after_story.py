#!/usr/bin/env python3
"""Move the V3 stack (big gear photo + spec strip) on HOF v2 pages so it sits
between the Story section and the Versions section instead of right after the
trust strip.

Why: better editorial pacing (text -> hero photo -> versions cards), keeps the
SEO-heavy Story copy higher up, and lands the "wow" gear shot mid-scroll where
it primes the Decision Guide.

Idempotent: if the V3 stack already sits after the Story section the script
leaves the file alone.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HOF_V2_PAGES = [
    "neumann-u47-fet-v2.html",
    "neve-1081-v2.html",
    "coles-4038-v2.html",
    "tab-telefunken-v72-v76-v2.html",
    "telefunken-ela-m-251-v2.html",
    "universal-audio-175b-v2.html",
    "universal-audio-apollo-x-v2.html",
    "neve-1073-guide-v2.html",
]

V3_BLOCK_RE = re.compile(
    r"\n*<!-- HERO V3 \u2014 big contained gear photo -->.*?</section>"
    r"\n*<!-- HERO V3 \u2014 spec strip -->.*?</section>\n*",
    re.DOTALL,
)

STORY_EYEBROW = ">The Story<"


def move_v3(text: str) -> tuple[str, str]:
    match = V3_BLOCK_RE.search(text)
    if not match:
        return text, "no V3 block"
    block_start, block_end = match.start(), match.end()

    story_idx = text.find(STORY_EYEBROW)
    if story_idx < 0:
        return text, "no Story eyebrow"

    if story_idx < block_end:
        story_close = text.find("</section>", story_idx)
        if story_close < 0:
            return text, "no Story closing section"
        if story_close > block_start:
            return text, "already after Story"

    block = match.group(0).strip("\n")
    text_without = text[:block_start] + text[block_end:]

    story_idx2 = text_without.find(STORY_EYEBROW)
    if story_idx2 < 0:
        return text, "no Story eyebrow (post-cut)"
    story_close2 = text_without.find("</section>", story_idx2)
    if story_close2 < 0:
        return text, "no Story closing section (post-cut)"
    insert_at = story_close2 + len("</section>")

    new_text = (
        text_without[:insert_at]
        + "\n\n"
        + block
        + "\n"
        + text_without[insert_at:]
    )
    return new_text, "moved"


def main() -> None:
    moved, skipped = [], []
    for name in HOF_V2_PAGES:
        path = ROOT / name
        if not path.exists():
            skipped.append((name, "missing"))
            continue
        text = path.read_text(encoding="utf-8")
        new_text, status = move_v3(text)
        if status == "moved":
            path.write_text(new_text, encoding="utf-8")
            moved.append(name)
        else:
            skipped.append((name, status))
    print(f"Moved V3 stack on {len(moved)} HOF v2 page(s):")
    for n in moved:
        print(f"  {n}")
    if skipped:
        print(f"\nSkipped {len(skipped)} page(s):")
        for n, w in skipped:
            print(f"  [{w}] {n}")


if __name__ == "__main__":
    main()
