# VK Secondary Pages — Handoff Brief
**Project:** Vintage King Audio · Secondary Pages Demo  
**Repo:** `/Users/andrewnehra/vk-secondary-pages/`  
**Date:** April 2026 · Internal

---

## Guardrails (non‑negotiable)

1. **This repo is for standalone secondary `.html` pages** (one file per page when building).
2. **Do not edit** the **core single-file prototype** or other files in the separate **vintage-king-redesign** project **from this repo** (no agent changes, no copying the big file in here).
3. **`navigator.html`** is the **roadmap**. It may use **local `file://` links** and **Open →** to **preview** the demo on your machine. That does not mean we rebuild Section A as standalone HTML — Section A is **done in the prototype** (preview only). **About VK:** confirm on `#about` in the demo; standalone `about.html` is still **TBD**.
4. Cursor agents: **`.cursor/rules/vk-secondary-pages.mdc`** is always on — follow it.

---

## What this repo is

Standalone secondary page demos for the Vintage King redesign. Each page is its own `.html` file. **This repo has zero connection to the core demo** (`VintageKing-Redesign-v2_67-Mar2026.html`). Never import, embed, or edit that file from here.

The core demo lives **outside this repo** (design lead’s machine / separate project). **Do not touch it from here.**

---

## Files in this repo

| File | Status | Notes |
|---|---|---|
| `navigator.html` | ✅ Ready | Secondary pages dashboard — open this first |
| `CLAUDE.md` | ✅ Ready | Design system rules — read before every edit |
| `about.html` | ❌ Needs build | T1 dark, content from vintageking.com/about |
| `hall-of-fame.html` | ❌ Needs build | T1 dark, 3 categories, 13 inductees, quote strips |
| `make-your-mark.html` | ❌ Needs build | T2 light/amber, artist features, Dave Cobb + Bob Clearmountain |
| `playback.html` | ❌ Needs build | T2 light/amber, 2×2 featured studio grid, issue cards |
| `careers.html` | ❌ Needs build | T2 light/amber, job listings, culture strip |
| `studio-professionals.html` | ❌ Needs build | T1 dark, program benefits, apply CTA |
| `trade-program.html` | ❌ Needs build | T1 dark, 3-step process, quote CTA |
| `section-179.html` | ❌ Needs build | T2 light/amber, tax savings, NO gold numbers strip |
| `warranty.html` | ❌ Needs build | T2 light/amber, 3-tier coverage, equipment photo |
| `neve-1073.html` | ❌ Needs build | T3 deep article, light theme, specs, editorial, timeline, FAQ |

---

## Design system

Read `CLAUDE.md` fully before any edit. Key rules:
- **Fonts:** Playfair Display (headings), DM Sans (body)
- **Colors:** `--vk-red: #C0392B` · `--amber: #D4860A` · `--near-black: #1A1A18` · `--off-white: #F7F5F2`
- **Minimum font size: 12px everywhere** — never go below
- **No `&` in headings or body** — always write "and"
- **No pinkish tints** (`#fde8e6` banned) — use neutral greys

---

## Page templates

**T1 — Commerce / Dark**  
Near-black background · Red accent · Large gear visual · Dark hero with gradient overlay

**T2 — Editorial / Light**  
Off-white background · Amber accent · Split hero (text left, photo right) · Eyebrow label + Playfair headline

**T3 — Deep Article**  
White background · Light theme · Product hero · Editorial body · Spec panel · Timeline · FAQ

---

## Each page must include

1. Shared nav (topbar + primary nav — copy structure from core demo)
2. Shared footer (copy from core demo)
3. In-page Dark/Light hero toggle (for T2 pages)
4. `<script type="application/ld+json">` structured data block
5. All font sizes ≥ 12px

---

## Page specs (from navigator)

### About VK
- Template: T1 dark
- Content: fetch from `https://vintageking.com/about`
- Hero: dark full-bleed with overlay
- Sections: mission statement, history timeline, team, locations

### Hall of Fame
- Template: T1 dark
- Hero count: 13 inductees
- 3 categories: Compressors (Fairchild, LA-2A, UREI 1176, UA 175B) · Mic Preamps (Neve 1073, Neve 1081, V72/V76) · Microphones (U47/U48, U67, U47 FET, ELA-M 251, Coles 4038, RCA 44-A)
- Typographic ledger layout per category
- Engineer quote strips between categories (off-white bg, red left border)
- Shop cards per category (3 cards each, dark photo area)
- Intro paragraph + Nominate strip at bottom

### Make Your Mark
- Template: T2 light/amber
- Hero: split layout, amber accent rule
- "Latest Features" cards: Dave Cobb + Bob Clearmountain at 420px height (big studio shots)
- 6-card artist grid below
- Submission form CTA at bottom

### PLAYBACK Magazine
- Template: T2 light/amber
- Featured Studio section: 2×2 grid at 400px card height
- All Issues grid: `minmax(280px,1fr)` columns, 220px image height
- Subscribe form CTA

### Careers
- Template: T2 light/amber
- 4-card culture strip
- Audio Consultant role card (primary listing)
- Open resume / speculative CTA

### Studio Professionals
- Template: T1 dark
- Program benefits: 6-card grid
- Eligibility criteria
- Apply CTA (amber button)
- Big panoramic photo moment (full-width)

### Trade Program
- Template: T1 dark
- 3-step process strip
- What we buy: gear category grid
- Quote/appraisal CTA
- Big panoramic photo moment

### Section 179
- Template: T2 light/amber
- Tax savings explainer
- How it works (3 steps)
- Who qualifies
- Shop CTA
- **NO gold numbers strip** (2.5M / 100% / Dec 31 — removed per design decision)

### VK Warranty
- Template: T2 light/amber
- 3-tier coverage breakdown
- ADH plan callout
- Used gear warranty section
- "Our Tech Shop backs every item" — use equipment/gear photo (not blue abstract)
- Confidence strip

### HOF — Neve 1073
- Template: T3 deep article / light theme
- 2-column hero: headline + lead left, product photo right (`neve-1073-module.png` or Unsplash)
- Spec panel (white bg, light theme)
- Editorial body: history, Neve 8068/8078 consoles, Air Studios, Electric Lady references
- EQ comparison table
- Pull quote strip
- "Records It Made" section
- Timeline
- FAQ (12+ questions)
- All font sizes ≥ 12px

---

## Git workflow (MANDATORY)

Before every edit session:
```bash
cd /Users/andrewnehra/vk-secondary-pages
git add -A && git commit -m "checkpoint before [page name] work"
```

After completing each page:
```bash
git add [filename].html
git commit -m "Build: [page name] — T[1/2/3] complete"
```

This gives a restore point for every page. Never work more than one page without committing.

---

## Hard rules for AI agents working in this repo

- **Never use subagents to modify HTML files** — all edits must be direct, surgical StrReplace calls
- **Never revert completed work**
- **Never touch the core demo** at `../Alternate-projects/vintage-king-redesign/`
- **Commit after every page** — non-negotiable
- **Read CLAUDE.md before every session**
- Work in precision mode: minimal diffs only

---

## Integration with the main prototype (optional — design lead only)

Do **not** edit the core prototype or its index from this repo. If the team later wants a single entry point, that is a **manual, approved** change in the **other** project — not something agents do from `vk-secondary-pages`.
