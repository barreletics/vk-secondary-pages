"""Make HOF page labels amber per the Vintage/Used design rule.

For each of the 8 HOF V2 pages:
  - Spec strip (V3 stack): change the small label spans from grey to amber,
    uppercase, with letter-spacing — eyebrow treatment.
  - .pg-stat-label CSS rule: grey -> amber.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGES = [
    "neumann-u47-fet-v2.html",
    "coles-4038-v2.html",
    "neve-1073-guide-v2.html",
    "neve-1081-v2.html",
    "tab-telefunken-v72-v76-v2.html",
    "telefunken-ela-m-251-v2.html",
    "universal-audio-175b-v2.html",
    "universal-audio-apollo-x-v2.html",
]

OLD_LABEL = (
    'font-size:13px;color:rgba(26,26,24,0.55);font-family:\'DM Sans\',sans-serif'
)
NEW_LABEL = (
    "font-size:11px;color:#D4860A;font-family:'DM Sans',sans-serif;"
    "font-weight:700;letter-spacing:0.16em;text-transform:uppercase"
)

OLD_STAT = ".pg-stat-label{font-size:11px;color:rgba(26,26,24,0.55);letter-spacing:0.12em;text-transform:uppercase}"
NEW_STAT = ".pg-stat-label{font-size:11px;color:#D4860A;letter-spacing:0.16em;text-transform:uppercase;font-weight:700}"


def patch(path: Path) -> tuple[bool, dict[str, int]]:
    text = path.read_text(encoding="utf-8")
    counts = {"label": 0, "stat": 0}

    new_text, n = re.subn(re.escape(OLD_LABEL), NEW_LABEL, text)
    counts["label"] = n
    text2 = new_text

    if OLD_STAT in text2:
        text2 = text2.replace(OLD_STAT, NEW_STAT, 1)
        counts["stat"] = 1

    if counts["label"] == 0 and counts["stat"] == 0:
        return False, counts
    path.write_text(text2, encoding="utf-8")
    return True, counts


def main() -> int:
    total = 0
    for fn in PAGES:
        p = ROOT / fn
        if not p.exists():
            print(f"  MISS {fn}")
            continue
        ok, counts = patch(p)
        flag = "OK  " if ok else "--  "
        print(f"  {flag} {fn:42}  labels={counts['label']}  stat={counts['stat']}")
        if ok:
            total += 1
    print(f"Patched {total}/{len(PAGES)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
