# Content Audit — Secondary Pages

Status of every secondary page in this repo against live `vintageking.com` content.
Updated as part of the v3 strip-and-hero rollout (commit series `v2-pre-rollout` → `v3-strip-and-hero-locked`).

## Status Legend

- **`live-verified`** — matching live VK URL exists; hero copy derived from real VK content (may need verbatim swap of body)
- **`live-derived`** — matching live VK URL exists; current copy is grounded but paraphrased; needs verbatim refresh of hero + body
- **`source-derived`** — copy pulled from `VK-secondary-pages-source.html` (AJ-provided); treat as approved
- **`generated`** — no live VK equivalent; copy is original prototype content; needs AJ approval before launch
- **`policy`** — legal / policy page; reuse existing VK policy text verbatim before launch

## Live URLs Confirmed (probed during audit)

| Live URL | Status | Notes |
| --- | --- | --- |
| `/about-us` | 200 | Real H1 = "We Are Vintage King" |
| `/trade` | 200 | Real H1 = "Sell & Trade Your Gear" |
| `/credit-card` | 200 | Real H1 = "Fuel Your Passion" |
| `/studio-services` | 200 | Real H1 = "System Design & Installation Services" |
| `/careers` | 200 | Real H1 = "Careers" / "Make Your Mark" |
| `/playback` | 200 | Real H1 = "PLAYBACK Magazine" |
| `/hall-of-fame` | 200 | Real H1 = "The Vintage King Pro Audio Hall Of Fame" |
| `/warranty` | 200 (redirect to FAQ) | No standalone page; warranty info under `/faq` |
| `/sell-your-gear` | 404 | Use `/trade` instead |
| `/audio-consulting` | 404 | No equivalent VK URL |

## Page-by-Page Audit

### Service / Program Pages

| Repo file | Live VK URL | Status | Action |
| --- | --- | --- | --- |
| `about.html` | `/about-us` | live-derived | Replace mission paragraph + co-founder quote with verbatim VK copy. H1 already verbatim. |
| `trade-program.html` | `/trade` | live-derived | H1 should be "Sell & Trade Your Gear" (verbatim). Subhead: "Your Trusted Trade Resource For Easy Gear Upgrades". 3-step process verbatim from VK. |
| `vk-credit-card.html` | `/credit-card` | live-derived | H1: "Fuel Your Passion". Subhead: "Financing Options to Help You Make Your Mark". 6/12/24/36/48 month tiers — match VK's exact disclaimer text. |
| `studio-professionals.html` | `/studio-services` | live-derived | Refresh "Why Partner" 5 cards with verbatim VK headers. |
| `multi-room-recording-studios.html` (+v2) | `/studio-services` | live-derived | Same source as above. |
| `careers.html` | `/careers` | live-derived | H1 should be "Careers" with eyebrow/subhead "Make Your Mark". Replace "Why Work" 4 cards verbatim. |
| `audio-consultants.html` | none | generated | No matching URL. Approve copy before launch — currently positions VK consultants similarly to live "Experts At Your Service" sidebar. |
| `section-179.html` | none (linked from `/faq#section-179`) | source-derived | Tax content — verify 2026 figures with AJ before launch. |

### Hall of Fame Pages (live VK has matching pages for all 13)

All HOF gear pages have a live VK equivalent — refresh hero blurb verbatim from the linked page on `/hall-of-fame`.

| Repo file | Live VK URL | Status |
| --- | --- | --- |
| `hall-of-fame.html` | `/hall-of-fame` | live-derived |
| `fairchild-660-670.html` | `/fairchild-660-670-compressor-limiter` | live-derived |
| `la-2a.html` | `/teletronix-la-2a-optical-compressor-limiter` | live-derived |
| `urei-1176.html` | `/urei-universal-audio-1176ln-compressor-limiter` | live-derived |
| `universal-audio-175b.html` (+v2) | `/universal-audio-175b-compressor-limiter` | live-derived |
| `neve-1073.html` | `/neve-1073-mic-pre` | live-derived |
| `neve-1073-guide.html` (+v2) | `/neve-1073-mic-pre` | live-derived |
| `neve-1081.html` (+v2) | `/neve-1081-mic-pre-eq` | live-derived |
| `tab-telefunken-v72-v76.html` (+v2) | `/tab-telefunken-v72-v76-mic-pre` | live-derived |
| `neumann-u47.html` | `/neumann-u47-u48-microphone` | live-derived |
| `neumann-u67.html` | `/neumann-u67-tube-microphone` | live-derived |
| `neumann-u47-fet.html` (+v2) | `/neumann-u47-fet-microphone` | live-derived |
| `telefunken-ela-m-251.html` (+v2) | `/telefunken-ela-m-250-microphone` | live-derived |
| `coles-4038.html` (+v2) | `/coles-4038-ribbon-microphone` | live-derived |

### Editorial Pages

| Repo file | Live VK URL | Status | Action |
| --- | --- | --- | --- |
| `playback.html` | `/playback` | live-derived | H1 verbatim. Add subhead "Recording History In Real Time". Issue copy verbatim from current PLAYBACK issue 7. |
| `make-your-mark.html` | `/blog/tag/make-your-mark` (likely) | source-derived | Editorial series. Verify episode list with AJ. |
| `25-years-of-pro-audio.html` (+v2) | none | generated | Anniversary editorial — content created for prototype. AJ to approve. |
| `classic-studios-gone-modern.html` | none / blog | generated | Long-form editorial — needs editorial review. |
| `recording-at-home.html` | none / blog | generated | Long-form editorial — needs editorial review. |
| `live-sound-how.html` | none | generated | How-to article — needs editorial review. |
| `neumann-mic-comparison.html` | none / blog | generated | Comparison article — verify spec data with AJ. |

### Campaign Pages

| Repo file | Live VK URL | Status | Action |
| --- | --- | --- | --- |
| `black-friday-microphone-deals.html` (+v2) | rotating | source-derived | Refresh deal data per Black Friday cycle. |
| `back-to-school.html` (+v2) | rotating | source-derived | Refresh per back-to-school cycle. |
| `new-at-namm-microphones.html` (+v2) | rotating | source-derived | Refresh per NAMM cycle. |
| `universal-audio-promotions.html` (+v2) | brand promo | source-derived | Refresh per UA promo cycle. |
| `avid-pro-tools-trade-in.html` (+v2) | brand promo | source-derived | Refresh per Avid promo cycle. |
| `avid-s4-control-surface-configurations.html` (+v2) | product family | source-derived | Verify current S4 SKUs. |
| `avid-s6-control-surface-configurations.html` (+v2) | product family | source-derived | Verify current S6 SKUs. |

### Policy Pages

| Repo file | Live VK URL | Status | Action |
| --- | --- | --- | --- |
| `warranty.html` | `/faq` (no standalone) | policy | Warranty content lives under FAQ on live. Either lift verbatim into this page or redirect. AJ to decide. |
| `returns.html` (+v2) | `/faq#easy-returns` | policy | Lift verbatim from FAQ. |
| `shipping-policy.html` (+v2) | `/faq#shipping-methods` | policy | Lift verbatim from FAQ. |
| `privacy-policy.html` (+v2) | `/privacy-policy` | policy | Lift verbatim — legal text must match exactly. |

## Recommended Refresh Order (by content value)

1. **`hall-of-fame.html`** — top GEO target, verbatim hero from `/hall-of-fame`.
2. **`trade-program.html`** — high-conversion service page, verbatim H1 + 3-step process from `/trade`.
3. **`about.html`** — top brand SEO page, verbatim mission + Mike Nehra quote from `/about-us`.
4. **`vk-credit-card.html`** — high-conversion finance page, verbatim 6/12/24/36/48 month tiers + disclaimers.
5. **`studio-professionals.html`** — high-value service page, verbatim 5 "Why Partner" cards from `/studio-services`.
6. **HOF gear pages (13 pages)** — verbatim blurbs from `/hall-of-fame` cards (already pulled in this audit).
7. **`careers.html`** — verbatim 4 "Why Work" cards from `/careers`.
8. **Policy pages (4 pages)** — verbatim from FAQ + privacy-policy.
9. **Editorial pages (7 pages)** — AJ to approve original copy or commission new editorial.
10. **Campaign pages (7 pages)** — refresh per cycle (Black Friday, NAMM, etc.).

## Notes

- The `VK-secondary-pages-source.html` file (provided by AJ, 6,250 lines) was the primary source for hero copy on most pages built so far. Any "source-derived" content above came from there.
- Page H1 + meta titles are already SEO-optimized. Body copy refresh should preserve existing JSON-LD blocks.
- All pages now have a trust strip (top) and Explore Vintage King strip (above footer) — these don't need content refresh.
