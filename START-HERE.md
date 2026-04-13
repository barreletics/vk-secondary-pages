# Start here — open the roadmap in your real browser

## Why GitHub feels “broken”

On **github.com**, when you click `navigator.html`, you get GitHub’s **file viewer** (code, blame, “Raw”). That is **not** the same as opening the page **in Chrome or Safari** like a normal website.

- **Repository URL** (`github.com/.../blob/.../navigator.html`) → wrong for preview.  
- **GitHub Pages URL** (`yourname.github.io/your-repo/navigator.html`) → correct **if** Pages is turned on — that serves real HTML in the browser.  
- **Local** (below) → always works on your Mac.

## Open the roadmap on your Mac (do this)

1. Clone or sync this repo so the folder exists on disk (e.g. `vk-secondary-pages`).
2. In **Finder**, open that folder and **double‑click `open-navigator.command`**.  
   It starts a tiny server and should open your default browser.
3. If nothing opens, run in **Terminal**:

```bash
cd /path/to/vk-secondary-pages
python3 -m http.server 8765
```

Then in the browser address bar paste:

**http://127.0.0.1:8765/navigator.html**

(Same URL is in **`ROADMAP-URL.txt`**.)

## Build instructions (what to read)

| What | Where |
|------|--------|
| Page list, filenames, templates T1/T2/T3 | **`HANDOFF.md`** |
| Design tokens, colors, type rules | **`CLAUDE.md`** |
| Roadmap UI | **`navigator.html`** (open locally as above) |

The **main single-file prototype** lives in the **other** project (`vintage-king-redesign`). Use it **only** to compare layouts when building — **do not** copy the big file into this repo. **`HANDOFF.md`** already describes what each secondary page needs.
