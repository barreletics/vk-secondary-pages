# Agency Handoff Brief — Vintage King Shopify Plus Migration

**Prepared by:** AJ / Barreletics Ops (Design and Strategy Lead)
**Date:** April 2026
**For:** Migration agency (Hammer Creative or Domaine)

---

## Purpose of This Document

This brief explains what we built, how it is structured, what the agency can lift directly, what must be rebuilt natively in Shopify, and the recommended phased rollout for layering the new design on top of the stabilized Shopify store.

**Read this document fully before reviewing any code.**

---

## What We Built

Two repositories, one unified design system:

### 1. Core Prototype (`vintage-king-redesign`)

A single monolithic HTML file containing 10 transactional screens, toggled by JS:

| # | Screen | Hash | What it covers |
|---|--------|------|----------------|
| 1 | Homepage | `#home` | Hero, "The Short List" tabbed products, Rare Gear vintage section, co-op brand blocks |
| 2 | Category | `#category` | Filter sidebar, product grid, buyer's guide card, Load More pagination |
| 3 | Product (PDP) | `#product` | Gallery left / details right, add-to-cart, specs panel, co-op blocks |
| 4 | FAQ | `#faq` | Accordion, search, category tabs |
| 5 | Demo Deals | `#deals` | Editorial hero toggle, product grid, condition badges |
| 6 | Sell or Trade | `#sell` | 3-way header toggle, credential bar, multi-step form, quote strips |
| 7 | Studio Installations | `#studio` | Project cards, dark caption overlay, service grid |
| 8 | Tech Shop | `#techshop` | Service tiers, process steps, form CTA |
| 9 | Financing | `#fin-page` | Section 179 calculator, Trade Program tabs, application form |
| 10 | Open Box | `#openbox` | Editorial 2x2 hero, product grid, buyer strip, ghost CTAs |

Plus the **global chrome** that appears on every screen:
- **Utility bar** (top strip with shipping/financing/support quick links)
- **Primary navigation** with mega menu (6 parent categories, hover-open panels)
- **Mobile navigation** (slide-over overlay with accordion sections)
- **Footer** (multi-column links, newsletter, legal)

**Live preview:** https://barreletics.github.io/vintage-king-redesign

### 2. Secondary Pages (`vk-secondary-pages` — this repo)

27 standalone HTML files, one per page:

**Program / Service Pages:**
- `about.html` — company overview
- `audio-consultants.html` — consultant program landing
- `careers.html` — job listings and culture
- `studio-professionals.html` — pro program benefits and application
- `trade-program.html` — trade-in process and gear categories
- `section-179.html` — tax deduction explainer
- `warranty.html` — 3-tier coverage breakdown
- `vk-credit-card.html` — VK credit card program

**Editorial / Content Pages:**
- `playback.html` — PLAYBACK magazine (featured studios, issue archive)
- `make-your-mark.html` — artist features (Dave Cobb, Bob Clearmountain, etc.)
- `hall-of-fame.html` — Hall of Fame landing (13 inducted pieces of gear)
- `classic-studios-gone-modern.html` — editorial feature
- `recording-at-home.html` — editorial/guide
- `live-sound-how.html` — editorial/guide
- `neumann-mic-comparison.html` — product comparison guide

**Hall of Fame Gear Deep-Dives (T3 article template):**
- `neve-1073.html` — Neve 1073 history, specs, EQ comparison, timeline, FAQ
- `neve-1073-guide.html` / `neve-1073-guide-v2.html` — buying guide variants
- `fairchild-660-670.html` — Fairchild compressor deep-dive
- `urei-1176.html` — UREI 1176 deep-dive
- `la-2a.html` — Teletronix LA-2A deep-dive
- `neumann-u47.html` — Neumann U 47 deep-dive
- `neumann-u67.html` — Neumann U 67 deep-dive

**Utility Files:**
- `navigator.html` — interactive dashboard / inventory of all pages (open locally in browser)
- `style-guide.html` — visual design system reference (typography, colors, spacing, components)
- `index.html` — redirects to navigator
- `VK-secondary-pages-source.html` — source file used by build scripts

**Extracted Prototype Slices** (in `pages/` folder):
- `pages/home.html`, `pages/category.html`, `pages/product.html`, `pages/faq.html`, `pages/deals.html`, `pages/sell.html`, `pages/studio.html`, `pages/techshop.html`, `pages/financing.html`, `pages/openbox.html`
- These are standalone extracts of each core prototype screen — useful for inspecting one screen at a time without the page-switcher overhead.

---

## How the Code Is Structured

Every HTML file is **self-contained**:
- Inline `<style>` block in `<head>` (thousands of lines of CSS per file)
- Inline `<script>` at the bottom (vanilla JS, no frameworks)
- Google Fonts loaded via `<link>` in `<head>`
- **No shared CSS files, no npm, no build toolchain, no framework**

CSS custom properties (`:root` tokens) are **duplicated identically in every file**. This was intentional for prototype portability — each file opens independently in any browser.

Navigation and footer markup is copy-pasted across files. Some files use a template injection pattern where a `<template>` tag holds the nav/footer and JS clones it into place.

All forms use `onsubmit="return false"` — they are visual demos with no backend.

Most secondary pages include `<script type="application/ld+json">` structured data blocks (Service, HowTo, FAQPage, Article, etc.).

---

## Design System (Locked — Do Not Alter)

### Fonts
| Use | Family | Weight | Notes |
|-----|--------|--------|-------|
| Display / Headings | Playfair Display | 400, 500, 600 | H1 48-56px, H2 32-40px, H3 18-22px |
| Body / UI / Buttons | DM Sans | 300, 400, 500 | 13-17px body text |
| Eyebrows | DM Sans | 500 | 12px, uppercase, 0.18-0.22em letter-spacing |
| **Pricing** | **DM Sans ONLY** | **500** | **NEVER use Playfair on numbers or prices** |
| Minimum size | — | — | **12px everywhere. Nothing below 12px.** |

### Colors
| Token | Hex | Use |
|-------|-----|-----|
| `--vk-red` | `#C0392B` | Primary CTA, eyebrow accents, new gear pages |
| `--near-black` | `#1A1A18` | All body text |
| `--warm-white` | `#FDFCFB` | Primary background |
| `--off-white` | `#F7F5F2` | Section backgrounds |
| `--charcoal` | `#2C2C2A` | Optional dark accent block (max 1 per page, never first section) |
| `--amber` | `#D4860A` | **Vintage/Used content ONLY** — never on new gear pages |
| `--amber-bg` | `#F5E6C8` | Credential bars, info boxes — vintage/used only |
| `--mid-grey` | `#6B6B68` | Secondary text |
| `--light-grey` | `#D8D6D2` | Borders, dividers |
| Blue `#2563EB` / `#EEF4FF` | — | Informational elements only (Open Box badge, buyer guide) |

### Banned Colors
- **`#fde8e6`** — too pinkish on uncalibrated screens. Use `rgba(26,26,24,0.07)` for neutral pill/badge backgrounds.
- **`rgba(192,57,43,0.04-0.08)` as a standalone section background** — looks pinkish. Use `var(--off-white)` instead.

### Section Rhythm (every secondary page follows this order)
1. Hero — `#EDE8E2` warm light background, dark text, red eyebrow, red CTA
2. Strip / credential bar — `var(--warm-white)`, thin border
3. Grid / cards — `var(--off-white)` bg, `#fff` cards, 1px rgba gap
4. Content / body — `#fff` bg, dark text
5. CTA / form — `#EDE8E2` bg, white inputs, red button
6. Values bar — `var(--off-white)` bg, `#fff` tiles
7. Footer

### Design Reference
CB2.com is the foundational design reference: one message per zone, white space as a feature.

---

## What the Agency Can Lift Directly

These assets transfer cleanly from our prototype into a Shopify theme with minimal translation:

| Asset | Where to find it | How to use |
|-------|-------------------|------------|
| **Design tokens** (all CSS custom properties) | `:root` block in any `.html` file | Copy values into theme `base.css` or `settings_schema.json` |
| **Typography scale and rules** | `style-guide.html` + this document | Direct reference for theme typography settings |
| **Section HTML structure** | Each page's `<body>` markup | Reference for Liquid section/block structure — class names, nesting, content zones are the spec |
| **Mega menu markup and CSS** | Any `pages/*.html` — search for `.mega-menu`, `.nav-link`, `.mega` | Adapt into a Liquid section; replace hardcoded links with `{% for link in linklists %}` |
| **JSON-LD structured data patterns** | `<script type="application/ld+json">` blocks in secondary pages | Copy schema structure, swap hardcoded values for Liquid objects (`{{ product.title }}`, etc.) |
| **Section layout patterns** | Every secondary page follows the section rhythm above | Blueprint for Liquid section ordering within templates |
| **Filter / category layout** | `pages/category.html` | Visual reference for collection template; actual filtering will use Shopify Search and Discovery or third-party app |
| **PDP layout and zones** | `pages/product.html` | Gallery placement, details column, specs panel, co-op blocks — adapt into `product.liquid` |
| **Image placeholder sizing** | Defined per template type in the CSS | Maintain aspect ratios and min-heights when swapping in real photography |

---

## What Must Be Rebuilt Natively in Shopify

These components require Shopify-native implementation. Our code is the visual and behavioral spec only:

### Mega Menu
Our JS is vanilla DOM manipulation (hover open/close, click-outside dismiss, dynamic positioning). On Shopify this needs to be a **Liquid section** pulling from Shopify `linklists` with proper menu management in the admin. Our code defines exactly how it should look and behave — the agency builds the Liquid/JS to match.

### Product Detail Page (PDP)
Our `pages/product.html` defines the full layout: gallery left, details right, variant selectors, add-to-cart, specs panel, co-op brand blocks. On Shopify, this becomes a `product.liquid` template using `{{ product.media }}`, `{{ product.variants }}`, cart AJAX, and Shopify's native variant/inventory system. Our code shows exactly what it should look like.

### Collection Filters
Our category page has a visual filter sidebar with collapsed/expanded states, pill badges, and count indicators. On Shopify, filtering is powered by the **Search and Discovery** app or a third-party like Searchspring. Our code shows the UI treatment; the data layer is Shopify-native.

### Cart and Checkout
Not in our prototype. Pure Shopify territory. Shopify Plus checkout extensibility (checkout UI extensions) applies here.

### Forms
Sell or Trade, Studio Professionals, Careers, and other pages have demo forms (`onsubmit="return false"`). These need real Shopify form handling: Shopify Forms app, custom metaobject + webhook flows, or a third-party form service.

### Mobile
We have not done a mobile responsive pass. The agency builds mobile from scratch using our desktop layouts as the design starting point. Desktop-first was intentional — mobile is the agency's responsibility.

### Search
No search prototype exists. The agency implements using Shopify native search or a third-party provider (Searchspring, Algolia, etc.).

---

## Recommended Phased Rollout

### Phase 1: Magento to Shopify Stabilization (existing design)

No new design work yet. Agency focuses on:
- Set up Horizon base theme on Shopify Plus
- Migrate products, customers, orders, historical data from Magento
- Implement 70,000+ URL redirects (manageable in native Shopify)
- Verify all Magento integrations have Shopify equivalents
- Stabilize and QA the existing site experience on Shopify

**From our repo during Phase 1:** Install our design tokens (`:root` CSS custom properties) into the theme even before visual changes begin. This future-proofs Phase 2 and avoids a massive find-and-replace later.

### Phase 2a: Global Chrome

Implement the elements that appear on every page:
- Utility bar (top strip)
- Primary navigation with mega menu
- Mobile navigation
- Footer

These touch every page, so doing them first means all subsequent template work inherits the new chrome automatically.

**Reference files:** Any `pages/*.html` file for the full nav/footer markup and CSS.

### Phase 2b: Core Transactional Pages

Revenue-driving pages, in priority order:
1. **Homepage** — `pages/home.html`
2. **Category / Collection** (with filters) — `pages/category.html`
3. **PDP / Product** — `pages/product.html`
4. **Cart** — agency builds from scratch (not in prototype)
5. **FAQ** — `pages/faq.html`

PDP and Category are the highest-value pages. Get these right first.

### Phase 2c: Service and Program Pages

Pages with moderate Shopify data dependencies (forms, conditional content):
- Sell or Trade — `pages/sell.html`
- Tech Shop — `pages/techshop.html`
- Studio Installations — `pages/studio.html`
- Financing — `pages/financing.html`
- Open Box — `pages/openbox.html`
- Demo Deals — `pages/deals.html`

### Phase 2d: Secondary and Editorial Pages

The standalone pages from this repo. These are the **easiest to implement** — mostly static content with minimal Shopify data dependencies:

- **Program pages:** `about.html`, `audio-consultants.html`, `careers.html`, `studio-professionals.html`, `trade-program.html`, `section-179.html`, `warranty.html`, `vk-credit-card.html`
- **Editorial pages:** `playback.html`, `make-your-mark.html`, `hall-of-fame.html`, `classic-studios-gone-modern.html`, `recording-at-home.html`, `live-sound-how.html`, `neumann-mic-comparison.html`
- **Gear deep-dives:** `neve-1073.html`, `fairchild-660-670.html`, `urei-1176.html`, `la-2a.html`, `neumann-u47.html`, `neumann-u67.html`

Most of these can be built as Shopify **custom page templates** with Liquid sections, or as **metaobject-driven content** if the agency wants CMS editability.

---

## Shopify Template Mapping

How our pages map to Shopify template types:

| Our Page | Shopify Template Type | Notes |
|----------|-----------------------|-------|
| Homepage | `templates/index.json` | Sections-based homepage |
| Category | `templates/collection.json` | Collection template with filter sidebar |
| PDP | `templates/product.json` | Product template with gallery, variants, cart |
| FAQ | `templates/page.faq.json` | Custom page template |
| Demo Deals | `templates/collection.demo-deals.json` | Alternate collection template with editorial hero |
| Sell or Trade | `templates/page.sell.json` | Custom page template with form |
| Open Box | `templates/collection.open-box.json` | Alternate collection template |
| Tech Shop / Studio / Financing | `templates/page.[name].json` | Custom page templates |
| About / Careers / Warranty / etc. | `templates/page.[name].json` | Custom page templates |
| Hall of Fame / PLAYBACK | `templates/page.[name].json` or blog template | Could be blog-driven if CMS editing needed |
| Gear deep-dives (Neve 1073, etc.) | `templates/article.gear.json` or `templates/page.[name].json` | Article template if blog-driven; custom page if static |

---

## Key Decisions (Locked)

These decisions are final. Do not revisit them during implementation:

| Decision | Detail |
|----------|--------|
| **Headed Shopify, not headless** | Horizon base theme. Liquid templates. No Hydrogen, no React storefront. |
| **70,000 redirects** | Manageable in native Shopify. Agency needs a redirect migration plan and testing strategy. |
| **Load More pagination** | Not infinite scroll. Must have static paginated URLs (`?page=2`, `?page=3`) for crawler indexing. |
| **No physical locations** | VK has no showrooms, retail stores, or city offices. Never reference Detroit, LA, Nashville as VK locations. Never use "showroom", "visit us", "in-store", "demo room" language. |
| **Red vs Amber accent** | New gear / commerce pages use `--vk-red` (#C0392B). Vintage/used/editorial pages use `--amber` (#D4860A). Each template gets one accent; our pages have a dev toggle for reference. |
| **Pricing typography** | DM Sans only, font-weight 500, `var(--near-black)`. Never Playfair Display on numbers or prices. |
| **12px minimum font** | Nothing below 12px anywhere on the site. |
| **"Pro Audio Outfitter" tagline** | Locked in the nav. Never remove. |
| **"VK Warranty" wording** | Always "VK Warranty" — never "Full Warranty". |
| **Navigation = conversion tool** | Six parent categories max. Not a sitemap. |
| **Open Box excluded from mega menu** | Follows Sweetwater / B&H benchmark. |
| **"The Short List"** | Tabbed product section name on homepage. Locked. |
| **"Rare Gear"** | Visible H2 on homepage vintage section. Locked. |

---

## Files to Review First

The agency should review these files in this order:

1. **This document** (`AGENCY-BRIEF.md`) — you are here
2. **`style-guide.html`** — open in browser; visual reference for the full design system
3. **`navigator.html`** — open locally (run `python3 -m http.server 8765` and visit `http://127.0.0.1:8765/navigator.html`); interactive dashboard of all pages with status, links, and template types
4. **`CLAUDE.md`** — detailed design system rules and decision log
5. **`HANDOFF.md`** — page inventory with template types and build specs
6. **Core prototype** (separate repo) — open in browser for the full 10-screen transactional experience
7. **Individual `.html` files** — inspect in browser and dev tools as you build each corresponding Liquid template

---

## How to Run the Prototype Locally

```bash
cd vk-secondary-pages
python3 -m http.server 8765
```

Then open: `http://127.0.0.1:8765/navigator.html`

From the navigator, you can open any page. Each `.html` file also works standalone — just open it directly in a browser.

The core prototype is hosted at: https://barreletics.github.io/vintage-king-redesign

---

## SEO and Structured Data

Every secondary page includes at least one JSON-LD block. The agency should:

- Preserve the schema types we chose (Service, HowTo, FAQPage, Article, JobPosting, Product)
- Replace hardcoded values with Liquid objects where applicable
- Maintain meta descriptions (140-160 chars, action-oriented) and title format: `[Page Name] — [Benefit Hook] | Vintage King`
- Keep `.speakable` class on hero paragraphs for Google SGE / AI agent discoverability
- Add `Organization`, `WebSite`, and `BreadcrumbList` schemas at the theme level (not in our prototype but expected for production)

---

## What Is NOT in Our Prototype

The agency will build these from scratch:
- Cart and checkout flow
- Customer account pages (login, order history, addresses)
- Search results page
- 404 page
- Blog index and article templates (unless gear deep-dives become blog posts)
- Mobile responsive design (we are desktop-only)
- Email templates (order confirmation, shipping, etc.)
- Shopify app integrations (reviews, loyalty, email marketing, etc.)

---

## Contact

Design and strategy questions: AJ / Barreletics Ops
