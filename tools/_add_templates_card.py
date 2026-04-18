"""Inject Page Templates card into the demo dashboard."""
from pathlib import Path

DASH = Path("/Users/andrewnehra/Alternate-projects/vintage-king-redesign/VK-Prototype-Index.html")

OLD = (
    '      <div class="vk-card">\n'
    '        <div class="vk-card-tag">Secondary pages</div>\n'
    '        <h2>Secondary Pages Navigator</h2>\n'
    '        <p>15 pages built \u00b7 build queue \u00b7 progress tracker \u00b7 links to every secondary page.</p>\n'
    '        <div class="vk-cta-row">\n'
    '          <a class="vk-cta" href="https://barreletics.github.io/vk-secondary-pages/navigator.html" target="_blank" rel="noopener">Open navigator \u2192</a>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="vk-card">\n'
    '        <div class="vk-card-tag">Design system</div>'
)

NEW = (
    '      <div class="vk-card">\n'
    '        <div class="vk-card-tag">Secondary pages</div>\n'
    '        <h2>Secondary Page Navigation</h2>\n'
    '        <p>43 pages built \u00b7 build queue \u00b7 progress tracker \u00b7 links to every secondary page.</p>\n'
    '        <div class="vk-cta-row">\n'
    '          <a class="vk-cta" href="https://barreletics.github.io/vk-secondary-pages/navigator.html" target="_blank" rel="noopener">Open navigation \u2192</a>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="vk-card">\n'
    '        <div class="vk-card-tag">Page templates</div>\n'
    '        <h2>Templates Guide</h2>\n'
    '        <p>3 hero variants \u00b7 2 body modules \u00b7 trust + explore strips \u00b7 agency hand-off spec.</p>\n'
    '        <div class="vk-cta-row">\n'
    '          <a class="vk-cta" href="https://barreletics.github.io/vk-secondary-pages/templates-guide.html" target="_blank" rel="noopener">Open templates \u2192</a>\n'
    '        </div>\n'
    '      </div>\n'
    '      <div class="vk-card">\n'
    '        <div class="vk-card-tag">Design system</div>'
)

OLD_GRID = (
    '    <div class="vk-section-label">Reference &amp; tools</div>\n'
    '    <div class="vk-grid">'
)
NEW_GRID = (
    '    <div class="vk-section-label">Reference &amp; tools</div>\n'
    '    <div class="vk-grid" style="grid-template-columns:repeat(4,1fr)">'
)


def main() -> int:
    text = DASH.read_text(encoding="utf-8")
    if OLD not in text:
        print("ERR: secondary card block not found")
        return 1
    if OLD_GRID not in text:
        print("ERR: reference grid not found")
        return 1
    text = text.replace(OLD, NEW, 1).replace(OLD_GRID, NEW_GRID, 1)
    DASH.write_text(text, encoding="utf-8")
    print(f"OK wrote {len(text)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
