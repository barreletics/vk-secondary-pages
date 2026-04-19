#!/usr/bin/env python3
"""
Phase 6 ampersand sweep.

Replaces &amp; with the word "and" in visible UI text across all *.html files.

Skips:
  - style-guide.html (already manually corrected; contains intentional <code> examples)
  - Anything inside an <a href="..."> URL attribute (no &amp; appears in attrs in scope, but be safe)
  - Inside <code>...</code> blocks (so the No-Go example survives)
"""
import os
import re
import sys

ROOT = "/Users/andrewnehra/vk-secondary-pages"
SKIP_FILES = {"style-guide.html"}

# Mass replacement map for compound product/category labels where "and" reads correctly.
# Default: replace standalone &amp; with "and".

def fix_file(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    original = src

    # Protect <code>...</code> spans so the style-guide-style example tokens stay literal.
    placeholders = []
    def stash(m):
        placeholders.append(m.group(0))
        return f"\x00CODE{len(placeholders)-1}\x00"
    src = re.sub(r"<code\b[^>]*>.*?</code>", stash, src, flags=re.DOTALL)

    # Protect href URL params (rare here) so we don't fold real query strings.
    href_stash = []
    def stash_href(m):
        href_stash.append(m.group(0))
        return f"\x00HREF{len(href_stash)-1}\x00"
    src = re.sub(r'href="[^"]*"', stash_href, src)

    src = src.replace("&amp;", "and")

    # Restore hrefs and code spans.
    for i, val in enumerate(href_stash):
        src = src.replace(f"\x00HREF{i}\x00", val)
    for i, val in enumerate(placeholders):
        src = src.replace(f"\x00CODE{i}\x00", val)

    if src != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
        return 1
    return 0


def main() -> int:
    changed = 0
    files = []
    for entry in os.listdir(ROOT):
        if entry.endswith(".html") and entry not in SKIP_FILES:
            files.append(os.path.join(ROOT, entry))

    for path in sorted(files):
        if fix_file(path):
            print(f"fixed: {os.path.basename(path)}")
            changed += 1

    print(f"\nTotal files changed: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
