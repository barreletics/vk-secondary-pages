# VK Secondary Pages

Standalone **secondary** HTML pages + **`navigator.html`** (roadmap). Rules: **`HANDOFF.md`**.

---

## You want the roadmap in your browser — not inside GitHub’s site

**github.com/.../navigator.html** = GitHub’s UI around the file. **Not** a full preview.

**Do this on your Mac:**

1. Double‑click **`open-navigator.command`** in this folder, **or** run:

```bash
cd /Users/andrewnehra/vk-secondary-pages && python3 -m http.server 8765
```

2. In Chrome or Safari, open:

### **http://127.0.0.1:8765/navigator.html**

Copy that line manually if needed. See **`ROADMAP-URL.txt`** or **`START-HERE.md`** for the same steps.

---

## Optional: preview via GitHub Pages (real browser, not the repo viewer)

If the repo is on GitHub with **Pages** enabled (Settings → Pages → branch `main`, folder `/root`), use:

**`https://YOUR_USERNAME.github.io/YOUR_REPO/navigator.html`**

That is a **website** URL, not the blob page on github.com.

---

## What to read to build each page

| Doc | Purpose |
|-----|--------|
| **`HANDOFF.md`** | One row per page: `about.html`, `hall-of-fame.html`, templates, specs |
| **`CLAUDE.md`** | Fonts, colors, banned tints, copy rules |
| **Other repo** (`vintage-king-redesign`) | Visual reference only — compare in the browser; do not import that HTML file here |
