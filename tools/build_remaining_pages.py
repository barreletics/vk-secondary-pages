#!/usr/bin/env python3
"""
Build remaining secondary pages (HOF gear, Avid surfaces, UA, campaigns, policy).
Each page gets shared chrome (topbar, utility, nav, secondary nav, footer) and
unique body content authored inline below.
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def chrome(title_breadcrumb: str, neighbors: list[tuple[str, str]]) -> tuple[str, str]:
    """Return (head_chrome, body_chrome) HTML."""
    nav_links = "".join(
        f'<span style="opacity:0.35">|</span><a href="{href}" style="color:rgba(255,255,255,0.55);text-decoration:none">{label}</a>'
        for label, href in neighbors
    )
    body_chrome = f'''<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Demo Dashboard</a>
  {nav_links}
  <span style="opacity:0.35">|</span><span style="opacity:0.75">{title_breadcrumb}</span>
</nav>
<div class="topbar"><a href="#" style="color:rgba(255,255,255,0.92);text-decoration:none">Free shipping on orders over $99</a><div class="topbar-divider"></div><a href="#" style="color:rgba(255,255,255,0.92);text-decoration:none">0% financing up to 48 months — Learn more</a></div>
<div class="utility-bar"><div style="display:flex"><a href="studio-professionals.html">Studio Professionals</a><a href="trade-program.html">Trade Program</a><a href="#">Studio Installations</a><a href="#" style="color:var(--vk-red);font-weight:500">Sell or Trade</a><a href="vk-credit-card.html">Financing</a><a href="section-179.html">Section 179</a></div><div style="display:flex;align-items:center"><a href="tel:8886531184" class="utility-bar-phone">888.653.1184</a></div></div>
<nav class="site-nav"><div class="nav-inner">
  <a href="#" class="nav-logo"><div class="logo-text"><span class="name">Vintage King</span><span class="tagline">New · Used · Vintage · Pro Audio</span></div></a>
  <ul class="nav-items">
    <li class="nav-item"><a href="#">Microphones</a></li><li class="nav-item"><a href="#">Outboard</a></li>
    <li class="nav-item"><a href="#">Consoles</a></li><li class="nav-item vintage"><a href="#">Vintage and Used ✦</a></li>
    <li class="nav-item"><a href="#">Studio Design</a></li><li class="nav-item"><a href="#">Monitoring</a></li>
    <li class="nav-item"><a href="#">Learn</a></li><li class="nav-item deals"><a href="#">Deals</a></li>
  </ul>
  <div class="nav-actions">
    <div class="nav-search-wrap"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6B6B68" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg><input type="text" placeholder="Search 50,000+ products…"></div>
    <button class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></button>
    <button class="nav-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg><div class="cart-count">2</div></button>
    <button class="nav-expert-btn"><div class="pulse-dot"></div> Ask</button>
  </div>
</div></nav>'''
    return body_chrome


SHARED_CSS = '''
:root{--vk-red:#C0392B;--vk-red-dk:#922B21;--off-white:#F7F5F2;--warm-white:#FDFCFB;--near-black:#1A1A18;--charcoal:#2C2C2A;--mid-grey:#6B6B68;--light-grey:#D8D6D2;--pale-grey:#EDEDEA;--amber:#D4860A;--amber-bg:#F5E6C8;--font-display:'Playfair Display',Georgia,serif;--font-body:'DM Sans',sans-serif;--page-accent:#D4860A;--nav-h:80px}
*{margin:0;padding:0;box-sizing:border-box}html{overflow-x:clip}
body{font-family:var(--font-body);background:var(--warm-white);color:var(--near-black);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:clip}
.page{display:none}.page.active{display:block}
.topbar{position:sticky;top:0;z-index:200;background:var(--near-black);height:32px;display:flex;align-items:center;padding:0 40px;font-size:11px;color:rgba(255,255,255,0.92);font-weight:500}
.topbar-divider{width:1px;height:12px;background:rgba(255,255,255,0.15);margin:0 16px}
.utility-bar{background:var(--warm-white);border-bottom:1px solid rgba(26,26,24,0.08);height:30px;display:flex;align-items:center;justify-content:space-between;padding:0 40px}
.utility-bar a{font-size:12px;color:rgba(26,26,24,0.68);text-decoration:none;letter-spacing:0.03em;padding:0 12px;border-right:1px solid rgba(26,26,24,0.12);line-height:1}
.utility-bar a:first-child{padding-left:0}.utility-bar a:last-child{border-right:none}
.utility-bar-phone{font-size:12.5px;color:var(--vk-red);font-weight:600;letter-spacing:0.03em;text-decoration:none}
.site-nav{position:sticky;top:32px;z-index:199;background:var(--warm-white);border-bottom:1px solid var(--light-grey);height:var(--nav-h)}
.nav-inner{max-width:1440px;margin:0 auto;padding:0 40px;height:100%;display:flex;align-items:center}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0;margin-right:32px}
.logo-text{display:flex;flex-direction:column;line-height:1}
.logo-text .name{font-family:"Roboto",sans-serif;font-size:17px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:var(--near-black)}
.logo-text .tagline{font-size:8px;letter-spacing:0.2em;text-transform:uppercase;color:var(--mid-grey);margin-top:3px}
.nav-items{display:flex;align-items:stretch;height:100%;list-style:none;flex:1;min-width:0}
.nav-item>a{display:flex;align-items:center;height:100%;padding:0 14px;font-size:14px;font-weight:500;letter-spacing:0.025em;color:var(--charcoal);text-decoration:none;white-space:nowrap;border-bottom:2px solid transparent;margin-bottom:-1px}
.nav-item>a:hover{color:var(--near-black);border-bottom-color:var(--vk-red)}
.nav-item.vintage>a{color:var(--amber)}.nav-item.deals>a{color:var(--vk-red);font-weight:600;margin-left:16px}
.nav-actions{display:flex;align-items:center;gap:12px;margin-left:auto;flex-shrink:0}
.nav-search-wrap{display:flex;align-items:center;gap:8px;background:var(--off-white);border:1px solid var(--light-grey);border-radius:4px;padding:7px 12px}
.nav-search-wrap input{border:none;background:none;font-family:var(--font-body);font-size:12.5px;color:var(--charcoal);outline:none;width:140px}
.nav-icon{background:none;border:none;cursor:pointer;color:var(--charcoal);padding:6px;display:flex;align-items:center;position:relative}
.cart-count{position:absolute;top:0;right:0;background:var(--vk-red);color:#fff;font-size:9px;font-weight:600;width:15px;height:15px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.nav-expert-btn{display:flex;align-items:center;gap:7px;background:var(--vk-red);color:#fff;border:none;cursor:pointer;padding:9px 16px;border-radius:3px;font-family:var(--font-body);font-size:13px;font-weight:500}
.pulse-dot{width:7px;height:7px;background:#4ade80;border-radius:50%;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.6}}

/* PAGE PRIMITIVES */
.pg-wrap{max-width:1160px;margin:0 auto;padding:0 40px}
.pg-eyebrow{font-family:var(--font-body);font-size:11px;font-weight:700;letter-spacing:0.22em;text-transform:uppercase;color:var(--page-accent);margin-bottom:14px}
.pg-hero{background:#EDE8E2;padding:96px 0;border-bottom:1px solid rgba(26,26,24,0.06)}
.pg-hero-inner{max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1.1fr 1fr;gap:64px;align-items:center}
.pg-hero h1{font-family:var(--font-display);font-size:50px;font-weight:700;line-height:1.05;color:var(--near-black);margin:0 0 22px}
.pg-hero p.lead{font-size:17px;color:rgba(26,26,24,0.7);line-height:1.65;margin:0 0 32px;max-width:540px}
.pg-hero-img{background:#1A1A18;border-radius:3px;min-height:340px;display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,0.35);font-size:13px;letter-spacing:0.1em;text-transform:uppercase;overflow:hidden}
.pg-hero-img img{width:100%;height:100%;object-fit:cover}

.pg-cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.pg-btn{display:inline-flex;align-items:center;gap:7px;background:var(--page-accent);color:#fff;padding:14px 28px;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em}
.pg-btn-ghost{display:inline-flex;align-items:center;gap:7px;color:var(--near-black);background:transparent;border:1.5px solid rgba(26,26,24,0.2);padding:13px 24px;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px}

.pg-strip{background:var(--warm-white);border-bottom:1px solid rgba(26,26,24,0.06)}
.pg-strip-inner{max-width:1160px;margin:0 auto;padding:18px 40px;display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}
.pg-strip-item{font-size:13px;color:rgba(26,26,24,0.65);display:flex;align-items:center;gap:8px}
.pg-strip-item strong{color:var(--near-black);font-weight:600}

.pg-section{padding:80px 0}
.pg-section-off{background:var(--off-white)}
.pg-section-white{background:#fff}
.pg-section-cta{background:#EDE8E2}
.pg-h2{font-family:var(--font-display);font-size:38px;font-weight:700;color:var(--near-black);margin:0 0 10px;line-height:1.15}
.pg-sub{font-size:15px;color:rgba(26,26,24,0.55);max-width:680px;line-height:1.7;margin:0 0 44px}

.pg-grid{display:grid;gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden}
.pg-grid-3{grid-template-columns:repeat(3,1fr)}
.pg-grid-4{grid-template-columns:repeat(4,1fr)}
.pg-card{background:#fff;padding:32px 26px;border-top:3px solid var(--page-accent);transition:transform .25s,box-shadow .25s}
.pg-card:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(26,26,24,0.08)}
.pg-card h3{font-family:var(--font-display);font-size:22px;font-weight:600;color:var(--near-black);margin:0 0 10px}
.pg-card p{font-size:13.5px;color:rgba(26,26,24,0.62);line-height:1.65;margin:0 0 14px}
.pg-card ul{list-style:none;padding:0;margin:0}
.pg-card li{font-size:12.5px;color:rgba(26,26,24,0.55);padding:5px 0;border-top:1px dashed rgba(26,26,24,0.08)}
.pg-card li:first-child{border-top:none}

.pg-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;margin-bottom:48px}
.pg-stat{background:#fff;padding:32px 24px;text-align:center}
.pg-stat-num{font-family:var(--font-display);font-size:38px;font-weight:700;color:var(--page-accent);line-height:1;margin-bottom:8px}
.pg-stat-label{font-size:11px;color:rgba(26,26,24,0.55);letter-spacing:0.12em;text-transform:uppercase}

.pg-dark{background:var(--near-black);padding:80px 0;color:#fff}
.pg-dark-inner{max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1.4fr 1fr;gap:64px;align-items:center}
.pg-dark .pg-eyebrow{color:var(--page-accent)}
.pg-dark h2{font-family:var(--font-display);font-size:36px;color:#fff;margin:0 0 16px;line-height:1.2}
.pg-dark p{font-size:16px;color:rgba(255,255,255,0.65);line-height:1.75;margin:0 0 14px}
.pg-quote{padding:36px;background:rgba(255,255,255,0.04);border-left:3px solid var(--page-accent);border-radius:2px}
.pg-quote-text{font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;line-height:1.45;margin:0 0 16px;font-style:italic}
.pg-quote-att{font-size:11px;color:var(--page-accent);letter-spacing:0.12em;text-transform:uppercase;font-weight:600}
.pg-quote-att small{display:block;color:rgba(255,255,255,0.5);font-weight:400;letter-spacing:0.04em;text-transform:none;margin-top:2px;font-size:12px}

.pg-faq details{margin-bottom:2px}
.pg-faq summary{font-size:15px;font-weight:600;color:var(--near-black);padding:18px 24px;background:#fff;cursor:pointer;list-style:none;border-bottom:1px solid rgba(26,26,24,0.06)}
.pg-faq summary::-webkit-details-marker{display:none}
.pg-faq summary::after{content:"+";float:right;font-size:18px;color:rgba(26,26,24,0.3)}
.pg-faq details[open] summary::after{content:"\\2212"}
.pg-faq-a{font-size:14px;color:rgba(26,26,24,0.65);line-height:1.7;padding:16px 24px 24px;background:#fff}

.pg-stick{position:fixed;bottom:0;left:0;right:0;z-index:500;background:var(--near-black);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;transform:translateY(100%);transition:transform 0.3s}
.pg-stick.visible{transform:translateY(0)}
.pg-stick-title{font-size:15px;font-weight:600}
.pg-stick-sub{font-size:12px;color:rgba(255,255,255,0.5);margin-top:2px}
.pg-stick-cta{background:var(--vk-red);color:#fff;padding:10px 22px;font-size:13px;font-weight:600;text-decoration:none;border-radius:2px}
.pg-stick-ghost{color:rgba(255,255,255,0.7);font-size:13px;font-weight:500;text-decoration:none;padding:10px 16px;border:1px solid rgba(255,255,255,0.2);border-radius:2px}

/* HOF gear-page specific */
.hof-versions{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:8px}
.hof-version{background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px 26px;border-radius:3px}
.hof-version .yr{font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px}
.hof-version h3{font-family:var(--font-display);font-size:20px;margin:0 0 8px}
.hof-version p{font-size:13.5px;color:rgba(26,26,24,0.62);line-height:1.65;margin:0}
.hof-spec{display:grid;grid-template-columns:repeat(2,1fr);gap:0;border:1px solid rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;background:#fff}
.hof-spec dt,.hof-spec dd{padding:14px 20px;border-bottom:1px solid rgba(26,26,24,0.06);font-size:13.5px}
.hof-spec dt{font-weight:600;color:var(--near-black);background:var(--off-white)}
.hof-spec dd{color:rgba(26,26,24,0.65)}

/* policy / minimal */
.policy-content{max-width:760px;margin:0 auto;padding:80px 40px}
.policy-content h2{font-family:var(--font-display);font-size:30px;margin:32px 0 12px;color:var(--near-black)}
.policy-content h2:first-child{margin-top:0}
.policy-content p{margin-bottom:14px;color:rgba(26,26,24,0.7);line-height:1.75}
.policy-content ul{margin:0 0 16px 24px;color:rgba(26,26,24,0.7);line-height:1.75}

/* FOOTER */
.site-footer{background:#F0EDE8;padding:56px 0 32px;margin-bottom:80px}
.footer-inner{max-width:1280px;margin:0 auto;padding:0 40px}
.footer-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}
.footer-brand-name{font-family:"Roboto",sans-serif;font-size:18px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--near-black);margin-bottom:12px;display:flex;align-items:center;gap:8px}
.footer-brand-desc{font-size:13px;color:var(--mid-grey);line-height:1.7;max-width:260px}
.footer-col-title{font-size:10px;letter-spacing:0.16em;text-transform:uppercase;color:var(--mid-grey);font-weight:500;margin-bottom:16px}
.footer-col ul{list-style:none}.footer-col ul li{margin-bottom:10px}
.footer-col ul li a{font-size:13px;color:var(--charcoal);text-decoration:none}
.footer-bottom{border-top:1px solid var(--light-grey);padding-top:24px;display:flex;justify-content:space-between;font-size:12px;color:var(--mid-grey)}
.footer-bottom a{color:var(--mid-grey);text-decoration:none}
@media(max-width:980px){.pg-hero-inner{grid-template-columns:1fr}.pg-grid-3,.pg-grid-4,.hof-versions{grid-template-columns:1fr}.pg-stats{grid-template-columns:repeat(2,1fr)}.pg-dark-inner{grid-template-columns:1fr}}
'''

FOOTER = '''<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <div class="footer-brand-name"><svg width="16" height="24" viewBox="0 0 22 34" fill="none"><rect x="7" y="1" width="8" height="20" rx="4" stroke="#C0392B" stroke-width="1.5" fill="none"/><line x1="11" y1="21" x2="11" y2="28" stroke="#C0392B" stroke-width="1.5"/><line x1="5" y1="28" x2="17" y2="28" stroke="#C0392B" stroke-width="1.5"/><circle cx="11" cy="10" r="2.5" fill="#C0392B" opacity="0.7"/></svg>VINTAGE KING</div>
        <p class="footer-brand-desc">The pro audio outfitter for all of your sonic journeys. Serving engineers and artists since 1993.</p>
      </div>
      <div class="footer-col"><div class="footer-col-title">Shop</div><ul><li><a href="#">Microphones</a></li><li><a href="#">Outboard</a></li><li><a href="#">Consoles</a></li><li><a href="#">Vintage and Used</a></li><li><a href="#">Open Box</a></li></ul></div>
      <div class="footer-col"><div class="footer-col-title">Company</div><ul><li><a href="about.html">About VK</a></li><li><a href="hall-of-fame.html">Hall of Fame</a></li><li><a href="playback.html">PLAYBACK Magazine</a></li><li><a href="careers.html">Careers</a></li></ul></div>
      <div class="footer-col"><div class="footer-col-title">Help</div><ul><li><a href="#">FAQ</a></li><li><a href="warranty.html">VK Warranty</a></li><li><a href="trade-program.html">Trade Program</a></li><li><a href="vk-credit-card.html">Financing</a></li></ul></div>
    </div>
    <div class="footer-bottom"><div>© 2026 Vintage King Audio, Inc. All rights reserved.</div><div><a href="#">Privacy</a> · <a href="#">Terms</a> · <a href="#">Accessibility</a></div></div>
  </div>
</footer>'''


def page_shell(title: str, meta: str, breadcrumb: str, neighbors: list[tuple[str, str]],
               jsonld: str, body: str, sticky: dict | None = None) -> str:
    sticky_html = ""
    if sticky:
        sticky_html = f'''<div class="pg-stick" id="pg-stick">
  <div><div class="pg-stick-title">{sticky["title"]}</div><div class="pg-stick-sub">{sticky["sub"]}</div></div>
  <div style="display:flex;gap:10px;align-items:center"><a href="{sticky["cta_href"]}" class="pg-stick-cta">{sticky["cta_label"]}</a></div>
</div>
<div style="height:68px"></div>
<script>window.addEventListener('scroll',function(){{var s=document.getElementById('pg-stick');if(window.scrollY>720)s.classList.add('visible');else s.classList.remove('visible');}});</script>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<style>{SHARED_CSS}</style>
<style id="vk-standalone-patch">.page{{display:block!important}}</style>
</head>
<body>
{chrome(breadcrumb, neighbors)}
<script type="application/ld+json">
{jsonld}
</script>
<div class="page active">
{body}
{sticky_html}
{FOOTER}
</div>
</body>
</html>
'''


# ───────────────────────── HOF GEAR PAGES (6) ─────────────────────────

def hof_gear_page(slug, name, full_name, year, era_dates, summary, hero_meta_pills,
                  history_para, key_features, versions, studios, records, quote,
                  buyer_guide, faqs, neighbors):
    """Build a Hall of Fame gear deep-page with shared layout."""
    pills_html = "".join(
        f'<div class="pg-stat"><div class="pg-stat-num">{v}</div><div class="pg-stat-label">{l}</div></div>'
        for v, l in hero_meta_pills
    )
    feat_html = "".join(
        f'<div class="pg-card"><h3>{h}</h3><p>{p}</p></div>'
        for h, p in key_features
    )
    versions_html = "".join(
        f'<div class="hof-version"><div class="yr">{yr}</div><h3>{n}</h3><p>{d}</p></div>'
        for yr, n, d in versions
    )
    studios_html = "".join(
        f'<div class="pg-card"><h3>{s}</h3><p>{d}</p></div>'
        for s, d in studios
    )
    records_html = "".join(f"<li>{r}</li>" for r in records)
    buyer_html = "".join(
        f'<div class="pg-card"><h3>{h}</h3><p>{d}</p><ul><li><strong>Best for:</strong> {b}</li><li><strong>Price range:</strong> {p}</li></ul></div>'
        for h, d, b, p in buyer_guide
    )
    faq_html = "".join(
        f'<details><summary>{q}</summary><div class="pg-faq-a">{a}</div></details>'
        for q, a in faqs
    )

    jsonld = '''{"@context":"https://schema.org","@graph":[
{"@type":"Product","name":"''' + full_name + '''","description":"''' + summary.replace('"', '\\"') + '''","brand":{"@type":"Brand","name":"''' + name.split()[0] + '''"},"category":"Pro Audio Outboard","offers":{"@type":"AggregateOffer","priceCurrency":"USD","seller":{"@type":"Organization","name":"Vintage King Audio"}}},
{"@type":"Article","headline":"''' + full_name + ''' — Hall of Fame Buyer''' + "'" + '''s Guide","author":{"@type":"Organization","name":"Vintage King Audio"},"publisher":{"@type":"Organization","name":"Vintage King Audio"},"datePublished":"2026-04-01"},
{"@type":"FAQPage","mainEntity":[''' + ",".join(
    '{"@type":"Question","name":"' + q.replace('"', '\\"') + '","acceptedAnswer":{"@type":"Answer","text":"' + a.replace('"', '\\"').replace('<a ', '').replace('</a>', '').replace('>', '') + '"}}'
    for q, a in faqs
) + ''']}]}'''

    body = f'''
<section class="pg-hero">
  <div class="pg-hero-inner">
    <div>
      <div class="pg-eyebrow">Hall of Fame · {era_dates}</div>
      <h1>{full_name}</h1>
      <p class="lead speakable">{summary}</p>
      <div class="pg-cta-row">
        <a href="#shop" class="pg-btn">Shop {name} →</a>
        <a href="#buyer-guide" class="pg-btn-ghost">Buyer's Guide</a>
      </div>
    </div>
    <div class="pg-hero-img">{name} · placeholder</div>
  </div>
</section>

<div class="pg-strip"><div class="pg-strip-inner">
  <div class="pg-strip-item"><strong>Inducted</strong> · VK Hall of Fame</div>
  <div class="pg-strip-item"><strong>Authorized dealer</strong> · for all current versions</div>
  <div class="pg-strip-item"><strong>Tech Shop</strong> · service and restoration</div>
  <div class="pg-strip-item"><strong>VK Warranty</strong> · on every unit</div>
</div></div>

<section class="pg-section pg-section-off">
  <div class="pg-wrap">
    <div class="pg-stats">{pills_html}</div>
    <div class="pg-eyebrow">The Story</div>
    <h2 class="pg-h2">Why the {name} matters.</h2>
    <p class="pg-sub">{history_para}</p>
    <div class="pg-grid pg-grid-3">{feat_html}</div>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Versions and Variants</div>
    <h2 class="pg-h2">The lineage.</h2>
    <p class="pg-sub">From the original release through current production. Each version has its own character.</p>
    <div class="hof-versions">{versions_html}</div>
  </div>
</section>

<section class="pg-section pg-section-off">
  <div class="pg-wrap">
    <div class="pg-eyebrow">In the Studios</div>
    <h2 class="pg-h2">Where it lives.</h2>
    <p class="pg-sub">A short list of rooms and records that put the {name} on the map.</p>
    <div class="pg-grid pg-grid-3">{studios_html}</div>
    <div style="margin-top:48px;background:#fff;border:1px solid rgba(26,26,24,0.08);border-radius:3px;padding:36px">
      <div class="pg-eyebrow" style="margin-bottom:10px">On the Records</div>
      <ul style="list-style:none;padding:0;margin:0;columns:2;column-gap:48px">
        {''.join(f'<li style="padding:6px 0 6px 18px;position:relative;font-size:13.5px;color:rgba(26,26,24,0.65);break-inside:avoid"><span style="position:absolute;left:0;color:var(--page-accent)">›</span>{r}</li>' for r in records)}
      </ul>
    </div>
  </div>
</section>

<section class="pg-dark">
  <div class="pg-dark-inner">
    <div>
      <div class="pg-eyebrow">VK Engineer's Take</div>
      <h2>The {name}, from the desk that sells the most of them.</h2>
      <p>Vintage King has placed the {name} in more rooms than nearly any dealer in the world. Here is what we tell engineers when they call.</p>
      <p style="margin-top:18px">Buying decisions get easier when you can hear the difference yourself. Talk to a consultant before you commit.</p>
    </div>
    <div class="pg-quote">
      <p class="pg-quote-text">{quote[0]}</p>
      <div class="pg-quote-att">{quote[1]}<small>{quote[2]}</small></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-white" id="buyer-guide">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Which {name} Should I Buy?</div>
    <h2 class="pg-h2">Decision guide.</h2>
    <p class="pg-sub">Use case · price range · what we recommend.</p>
    <div class="pg-grid pg-grid-3">{buyer_html}</div>
  </div>
</section>

<section class="pg-section pg-section-off">
  <div class="pg-wrap">
    <div class="pg-eyebrow">FAQ</div>
    <h2 class="pg-h2">Common questions.</h2>
    <p class="pg-sub">If you do not see your question, talk to a consultant.</p>
    <div class="pg-faq" style="border:1px solid rgba(26,26,24,0.08);border-radius:3px;overflow:hidden">{faq_html}</div>
  </div>
</section>
'''
    sticky = {
        "title": f"{name} · Hall of Fame",
        "sub": f"Authorized dealer · Tech Shop service · VK Warranty",
        "cta_href": "#shop",
        "cta_label": f"Shop {name} →"
    }
    return page_shell(
        title=f"{full_name} — Hall of Fame Buyer's Guide | Vintage King",
        meta=summary[:160],
        breadcrumb=full_name,
        neighbors=neighbors,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )


# Page configs ---------------------------------------------------------------

NEIGHBORS_HOF = [
    ("Hall of Fame", "hall-of-fame.html"),
    ("Neve 1073", "neve-1073.html"),
    ("Neumann U47", "neumann-u47.html"),
]

HOF_PAGES = {
    "neve-1081.html": dict(
        slug="neve-1081", name="Neve 1081", full_name="Neve 1081 Mic Pre / EQ",
        year=1972, era_dates="1972 — Present",
        summary="Neve's all-discrete, four-band parametric mic pre and EQ — the brawnier sibling of the 1073. Built for the 80-series consoles that defined British rock and remained a workhorse in commercial rooms for fifty years.",
        hero_meta_pills=[("1972", "Year introduced"), ("4-band", "Parametric EQ"), ("Class A", "Discrete topology"), ("80-series", "Console origin")],
        history_para="The Neve 1081 was designed in 1972 by Rupert Neve for the 8048 console. Where the 1073 paired a Marinair-coupled mic pre with a 3-band EQ, the 1081 added a fourth band and shifted to a more flexible parametric architecture. The result was a desk strip that could shape sources with surgical precision while keeping the harmonic warmth Neve was known for. Today the 1081 lives on in horizontal-rack form and as the centerpiece of every restored 8048-series desk.",
        key_features=[
            ("Class A discrete topology", "All-discrete signal path. No op-amps in the audio chain. Same harmonic signature as the original 80-series consoles."),
            ("Four-band parametric EQ", "High and low shelves plus two fully parametric mid bands. Far more flexible than the 1073's three-band architecture."),
            ("Marinair-style transformers", "Input and output transformers carry the saturation and weight that defines the Neve sound at the line stage."),
        ],
        versions=[
            ("1972 — 1980", "Original 1081", "Console module for 8048 and 8068 desks. Single-card construction, hand-built in Cambridgeshire."),
            ("Reissue", "AMS Neve 1081 Classic", "Current production reissue from the original drawings. Component-matched and fully serviceable."),
            ("Module", "1081R / 500-series", "Modern 500-series and rackmount versions for engineers who want the 1081 sound at a project-studio price."),
        ],
        studios=[
            ("AIR Studios — London", "Original 8048-series desks at George Martin's facility. The 1081 strip behind countless British rock records."),
            ("Sound City — Los Angeles", "Sound City's Neve 8028 was built around 1073 and 1081 strips. The console that cut Nevermind."),
            ("Power Station — NYC", "Tony Bongiovi's room ran a custom Neve console with 1081 strips. Bowie, Springsteen, Bon Jovi."),
        ],
        records=[
            "Nirvana — Nevermind (Sound City Neve 8028)",
            "Tom Petty — Damn the Torpedoes",
            "Fleetwood Mac — Tusk",
            "David Bowie — Let's Dance",
            "Bruce Springsteen — Born in the USA",
            "Foo Fighters — One by One",
        ],
        quote=("The 1081 is the EQ I reach for when I need to shape something without losing the source. Four bands of parametric and that Neve weight you cannot fake.", "Mike Nehra", "Co-Founder · Vintage King"),
        buyer_guide=[
            ("Original 1972 — 1980 module", "If you want the real thing — original components, original transformers, original character. Best for restoration projects and engineers who already own a vintage Neve console.", "Restoration projects, vintage purists", "$8,500 — $15,000+"),
            ("AMS Neve 1081 Classic", "Current-production reissue from original drawings. Same circuitry, modern reliability. Best for new commercial rooms and engineers who want long-term support.", "New builds, professional studios", "$3,995 — $4,495"),
            ("500-series 1081R", "The 1081 sound in a 500-series chassis. Best for project studios and producers who want flexibility without the desk footprint.", "Project studios, hybrid setups", "$1,800 — $2,200"),
        ],
        faqs=[
            ("Is the 1081 better than the 1073?", "Different, not better. The 1073 has a 3-band EQ with fixed frequencies and is famous for its mic preamp warmth. The 1081 has a 4-band parametric EQ for more surgical work. Most engineers own both for different jobs."),
            ("Which version sounds closest to the original?", "AMS Neve's current Classic reissue is built from the original drawings and is the closest to a 1972 unit you can buy new. Vintage modules will vary based on component drift and service history."),
            ("Can I run a 1081 module without a Neve console?", "Yes — with a power supply and rackmount frame. VK can build or source either, or recommend a 500-series alternative."),
            ("Do you service vintage 1081s?", "Yes. The Tech Shop services and restores Neve modules end to end, including transformer replacement and recapping."),
        ],
    ),
    "telefunken-ela-m-251.html": dict(
        slug="telefunken-ela-m-251", name="ELA-M 251", full_name="Telefunken ELA-M 250 / 251 Microphone",
        year=1959, era_dates="1959 — 1965 (Original)",
        summary="The Telefunken ELA-M 251 — a Vienna-built tube condenser that became the most coveted vocal mic of the 1960s. Built by AKG, badged by Telefunken, and used on more iconic vocals than nearly any other microphone in history.",
        hero_meta_pills=[("1959", "Year introduced"), ("CK12", "Brass capsule"), ("6072a", "Vacuum tube"), ("3 patterns", "Cardioid / Omni / Fig-8")],
        history_para="The ELA-M 251 was Telefunken's flagship vocal microphone from 1959 to 1965. It was built in Vienna by AKG using a brass-edge CK12 capsule and a 6072a tube — the same building blocks as the AKG C12, but with a different output transformer and Telefunken badging. Fewer than 5,000 original units left the factory, and surviving examples now trade for $20,000 to $40,000 each. Modern reissues from Telefunken Elektroakustik bring the original tone within reach of working studios.",
        key_features=[
            ("CK12 brass capsule", "Hand-built dual-diaphragm capsule. The brass-edge construction is the defining tonal element — silky highs, weight in the lower midrange."),
            ("6072a triode", "Hand-selected dual-triode tube. Provides the headroom and harmonic richness that makes the 251 sit in a mix without EQ."),
            ("Three-pattern remote", "External power supply switches between cardioid, omni, and figure-8 patterns. Same flexibility as the C12, voiced differently."),
        ],
        versions=[
            ("1959 — 1962", "ELA-M 250", "Original Vienna build. Cardioid and omni only. Now one of the rarest tube mics in existence."),
            ("1962 — 1965", "ELA-M 251 / 251E", "Three-pattern version with the figure-8 added. Most original 251s in circulation are this generation."),
            ("Reissue", "Telefunken Elektroakustik 251", "Current production from CT, USA. Built with hand-selected NOS tubes and brass-edge capsules to original spec."),
        ],
        studios=[
            ("Capitol Studios — LA", "Sinatra's vocal mic of choice. The Capitol echo chambers and a 251 cut some of the most iconic vocal performances in popular music."),
            ("Abbey Road — London", "EMI ran multiple 251s alongside U47s in Studio 2. Beatles backing vocals, orchestral overdubs, and string sections."),
            ("United Western — LA", "Bill Putnam's room paired 251s with the LA-2A and Fairchild 660 for vocals that defined the West Coast sound."),
        ],
        records=[
            "Frank Sinatra — In the Wee Small Hours",
            "The Beatles — Sgt. Pepper's (orchestral)",
            "The Beach Boys — Pet Sounds (vocals)",
            "Sam Cooke — A Change Is Gonna Come",
            "Ella Fitzgerald — Songbook series",
            "Adele — 21 (reissue 251 on vocals)",
        ],
        quote=("There is a reason every vocal booth I have ever walked into has a 251 or a 47 on the stand. The 251 has a sweet top end that flatters almost any voice.", "Ryan McGuire", "Senior Audio Consultant · Vintage King"),
        buyer_guide=[
            ("Original 1959 — 1965 ELA-M 251", "If you have the budget and the patience to vet a vintage example. Best for collectors, commercial rooms, and engineers chasing the exact 1960s sound.", "Collectors, world-class commercial rooms", "$20,000 — $40,000"),
            ("Telefunken Elektroakustik 251", "Current production reissue. Brass-edge capsule, NOS tube, hand-built in CT. The closest you can get to the original without buying vintage.", "Working pro studios, engineers who want long-term support", "$10,500 — $11,995"),
            ("Telefunken TF51 / TF47", "Telefunken's more affordable tube mics in the 251 family. Different voicing but the same build philosophy.", "Project studios, mid-tier commercial rooms", "$2,995 — $4,495"),
        ],
        faqs=[
            ("What's the difference between an ELA-M 250 and a 251?", "The 250 is two-pattern (cardioid and omni). The 251 added the figure-8 pattern via the external power supply. Sonically they are nearly identical — the 251 is more common because it ran longer."),
            ("Are reissue 251s really the same as vintage?", "The current Telefunken Elektroakustik reissue is the closest reissue available, with the brass-edge CK12 capsule and the 6072a tube. Side-by-side comparisons place it within a few dB of vintage examples in tone."),
            ("Why is the 251 so expensive?", "Limited production (under 5,000 units), iconic recordings, and the fact that very few survive in original working condition. Demand has climbed steadily for fifty years."),
            ("Do you service vintage 251s?", "Yes — the Tech Shop services and restores vintage tube mics including capsule reskinning, tube replacement, and power supply rebuilds."),
        ],
    ),
    "neumann-u47-fet.html": dict(
        slug="neumann-u47-fet", name="U47 FET", full_name="Neumann U47 FET Microphone",
        year=1972, era_dates="1972 — 1986 (Original) / 2014 — Present (Reissue)",
        summary="The Neumann U47 FET — the solid-state successor to the legendary U47 tube mic. Built around the same K47 capsule, voiced for high-SPL sources, and the standard kick-drum mic on more records than any other microphone.",
        hero_meta_pills=[("1972", "Year introduced"), ("K47", "Capsule"), ("FET", "Solid-state circuit"), ("140 dB", "Max SPL")],
        history_para="When Telefunken stopped supplying the VF14 tube in 1965, Neumann needed a new flagship large-diaphragm mic. The U47 FET arrived in 1972 with the same K47 capsule but a solid-state FET circuit — same family, completely different voice. The FET could handle 140 dB SPL, making it the kick drum and bass cabinet mic of choice from the 1970s onward. Discontinued in 1986, the FET was reissued by Neumann in 2014 to original spec and remains a standard close-mic for loud sources.",
        key_features=[
            ("K47 capsule", "Same dual-diaphragm capsule as the original tube U47. The capsule is what gives both versions their family resemblance — fat low midrange, smooth top."),
            ("FET circuit", "Solid-state output stage means the FET can handle 140 dB SPL without compression — far higher than any tube mic. That is why it dominates kick drums and bass cabs."),
            ("Cardioid only", "Single pattern, no remote pickup pattern selector. Built for one job — capturing close, loud sources cleanly."),
        ],
        versions=[
            ("1972 — 1986", "Original U47 FET", "Original production from Neumann Berlin. Components vary by year. Most desirable units are early-1970s with original K47 capsules."),
            ("2014 — Present", "U47 FET Reissue", "Current production from Neumann to original spec. Same K47 capsule, same circuit topology, modern reliability."),
            ("Variant", "U47 FET i (1980s)", "Late-production variant with revised circuit. Slightly different output behavior. Less common in studios."),
        ],
        studios=[
            ("Sound City — LA", "The kick drum mic on countless rock records cut at Sound City. Standard pairing with the Neve 8028 console."),
            ("Electric Lady — NYC", "Hendrix's room ran multiple U47 FETs on bass cabs and kick. Still in regular rotation today."),
            ("Power Station — NYC", "Tony Bongiovi's room used the FET on bass cabinets and floor toms — a standard mic in the live tracking arsenal."),
        ],
        records=[
            "Nirvana — Nevermind (kick drum)",
            "Foo Fighters — Wasting Light (kick drum)",
            "Tom Petty — Damn the Torpedoes (bass cabs)",
            "Red Hot Chili Peppers — Stadium Arcadium",
            "Queens of the Stone Age — Songs for the Deaf",
            "Adele — 25 (bass)",
        ],
        quote=("The FET is the kick mic. There are alternatives, but everyone reaches for it first. Forty years and counting as the standard.", "Mike Nehra", "Co-Founder · Vintage King"),
        buyer_guide=[
            ("Original 1972 — 1986 U47 FET", "Vintage example with K47 capsule. Tonal character varies by year and condition. Best for engineers who want the exact 1970s sound and have the budget.", "Vintage purists, restoration projects", "$3,500 — $7,500"),
            ("U47 FET Reissue (2014+)", "Current Neumann production. Built to original spec with modern reliability. Best for new commercial rooms and studios that need backup units.", "Working pro studios, commercial rooms", "$3,995 — $4,495"),
            ("Used / b-stock reissue", "Lightly used reissue units come up regularly through the Sell or Trade desk. Same spec as new at a lower entry point.", "Project studios, second mic rooms", "$2,995 — $3,495"),
        ],
        faqs=[
            ("Is the U47 FET the same as the U47 tube?", "No. They share the K47 capsule but the FET uses a solid-state circuit instead of a VF14 tube. Tonally related, but the FET is brighter and handles much higher SPL — which is why it lives on kick drums and bass cabs."),
            ("Why is the FET the standard kick drum mic?", "Two reasons: it can handle 140 dB SPL without distortion, and the K47 capsule has a low-mid weight that flatters kick drums. Once it became the standard in the 1970s, the sound got embedded in pop music's vocabulary."),
            ("Is the reissue worth buying or should I find vintage?", "If you want a reliable working mic for a commercial room, the reissue is the right choice. Vintage units carry collector premium and require service vetting."),
            ("Do you service vintage U47 FETs?", "Yes — the Tech Shop handles K47 capsule reskinning, circuit service, and power supply restoration on both vintage and reissue FETs."),
        ],
    ),
    "coles-4038.html": dict(
        slug="coles-4038", name="Coles 4038", full_name="Coles 4038 Ribbon Microphone",
        year=1953, era_dates="1953 — Present",
        summary="The Coles 4038 — the BBC-developed ribbon microphone that has been in continuous production since 1953. Standard for drum overheads, brass, and broadcast vocals. The mic that made the British drum sound.",
        hero_meta_pills=[("1953", "Year introduced"), ("Ribbon", "Bidirectional"), ("BBC", "Original spec"), ("Hand-built", "UK production")],
        history_para="The Coles 4038 was developed in the 1950s by the BBC's research department, originally manufactured by STC, and licensed to Coles Electroacoustics in the 1970s — where it has been hand-built ever since. The 4038 is a figure-of-eight ribbon mic with a smooth, dark high-end and a forgiving response to loud transients. It became the standard drum overhead in British studios, the standard horn mic in jazz rooms, and a regular for broadcast vocals. The mic has not changed in any meaningful way since 1953.",
        key_features=[
            ("BBC-spec ribbon", "Hand-tuned aluminum ribbon. The smooth high-frequency rolloff is the 4038's signature — drum cymbals sound musical, not brittle."),
            ("Figure-of-eight pattern", "Bidirectional pickup with deep nulls at the sides. Excellent for stereo techniques like Blumlein pair and mid-side."),
            ("Hand-built in the UK", "Each 4038 is built by hand at Coles' UK facility. Pairs are component-matched for stereo work."),
        ],
        versions=[
            ("1953 — 1970s", "STC 4038", "Original production by Standard Telephones and Cables. Vintage units identical to current Coles."),
            ("1970s — Present", "Coles 4038", "Continuous production since the 1970s. No meaningful design changes. Pairs available matched."),
            ("Stereo Pair", "Matched 4038 Pair", "Factory-matched stereo pair for Blumlein and mid-side techniques. The standard for orchestral and drum overhead work."),
        ],
        studios=[
            ("Abbey Road — London", "Standard drum overhead mic at Abbey Road since the 1960s. On Beatles, Pink Floyd, and modern Abbey Road sessions."),
            ("AIR Studios — London", "George Martin's room ran 4038 pairs on every drum kit. The British drum sound starts here."),
            ("Capitol Studios — LA", "American studios picked up the 4038 in the 1970s. Capitol still runs them on horn sessions and drum overheads."),
        ],
        records=[
            "The Beatles — Abbey Road (drum overheads)",
            "Pink Floyd — Dark Side of the Moon",
            "Led Zeppelin — IV (drum room)",
            "Adele — 21 (orchestral horns)",
            "Elton John — Captain Fantastic",
            "Foo Fighters — In Your Honor",
        ],
        quote=("If a 4038 is on the overheads, the kit will sound like a record. There is something about that ribbon that takes the harshness off cymbals while keeping the punch.", "Ryan McGuire", "Senior Audio Consultant · Vintage King"),
        buyer_guide=[
            ("Single Coles 4038", "Start with a single 4038 for mono drum overhead, mono horn, or broadcast voice work.", "Mono overhead, brass, voice", "$1,495 — $1,795"),
            ("Matched Stereo Pair", "Factory-matched stereo pair for Blumlein, mid-side, and drum overhead work. The standard pro setup.", "Stereo overhead, orchestral, room mics", "$2,995 — $3,495"),
            ("Vintage STC 4038", "Original BBC-era STC unit. Same spec, vintage build quality. Best for collectors.", "Collectors, vintage purists", "$1,200 — $2,500"),
        ],
        faqs=[
            ("How is the Coles 4038 different from other ribbon mics?", "The 4038 has the smoothest top end of any commonly available ribbon. Royer R-121 is brighter and more focused; AEA R84 is warmer and more open. The 4038 sits in its own lane — dark, BBC-voiced, classic."),
            ("Does the 4038 need a special preamp?", "Like most passive ribbons, the 4038 benefits from high-gain, high-impedance preamps (Cloudlifter, Royer Star, Neve Portico, API mic pres). 60 dB+ of clean gain is ideal."),
            ("Are matched pairs worth the extra cost?", "If you do stereo recording — drum overheads, orchestral, horn sections — yes. Factory matching ensures consistent stereo image and tonal balance."),
            ("Do you service Coles 4038s?", "Yes — the Tech Shop handles ribbon replacement, transformer service, and recalibration on both Coles and vintage STC units."),
        ],
    ),
    "tab-telefunken-v72-v76.html": dict(
        slug="tab-telefunken-v72-v76", name="V72 / V76", full_name="TAB / Telefunken V72 and V76 Mic Preamps",
        year=1955, era_dates="1955 — 1980 (Original)",
        summary="The German broadcast preamp standard from the 1950s and 1960s. V72 and V76 modules pulled from German radio facilities became coveted studio outboard — the foundation of the German tube preamp sound and the basis for many modern reproductions.",
        hero_meta_pills=[("1955", "Year introduced"), ("EF12 / EF804s", "Tube types"), ("34 dB / 76 dB", "Gain (V72 / V76)"), ("Broadcast", "Original use")],
        history_para="The V72 and V76 modules were designed for German broadcast radio facilities in the 1950s. TAB and Telefunken built thousands of these tube preamps — V72 with 34 dB of gain for line-level work, V76 with 76 dB of gain for microphones. When German radio facilities modernized in the 1970s and 1980s, the modules flooded the second-hand market and were quickly discovered by recording engineers. Today they form the backbone of the German tube preamp sound, with companies like Wunder Audio, Vintech, and Gyraf building modern reproductions.",
        key_features=[
            ("All-tube signal path", "Both V72 and V76 use German broadcast tubes (EF12, EF804s, EF14). The harmonic richness is what defines the sound."),
            ("Broadcast-grade build", "Originally built for 24/7 radio operation. The build quality far exceeds typical studio outboard — these modules run for decades without service."),
            ("Iron transformers", "Input and output transformers from Pikatron and Haufe carry the saturation and weight that defines the German tube sound."),
        ],
        versions=[
            ("1955 — 1965", "V72 / V72a", "Line-level preamp with 34 dB of gain. Common for tape playback chains and instrument level signals. Quickly adopted as a 'character' preamp for synths and guitars."),
            ("1958 — 1970", "V76 / V76m", "Microphone preamp with 76 dB of gain. The flagship broadcast mic preamp. Vocals, acoustic instruments, and drum overheads."),
            ("Modern", "Wunder Audio PEQ1 / Vintech 73 / Gyraf G7", "Modern reproductions and clones built from original schematics. More reliable, more affordable, same circuit philosophy."),
        ],
        studios=[
            ("Hansa Tonstudio — Berlin", "The Berlin studio that recorded Bowie, Iggy Pop, Depeche Mode. Original German broadcast modules in regular rotation."),
            ("Conny Plank's Studio — Cologne", "Krautrock central. Conny used V72 and V76 modules on Kraftwerk, Neu!, and Eurythmics sessions."),
            ("Modern boutique rooms", "VK has placed restored V72 and V76 modules in dozens of modern commercial rooms looking for German tube character."),
        ],
        records=[
            "David Bowie — Heroes (Hansa)",
            "Kraftwerk — Trans-Europe Express",
            "Eurythmics — Sweet Dreams",
            "Iggy Pop — The Idiot",
            "Depeche Mode — Music for the Masses",
            "Various Krautrock catalog",
        ],
        quote=("If you want the German tube sound — that smoky, weighted, slightly compressed quality — V72 and V76 modules are the original source. Everything else is a tribute to these.", "Mike Nehra", "Co-Founder · Vintage King"),
        buyer_guide=[
            ("Original V72 module (restored)", "Vintage broadcast module, professionally restored with tube replacement and recapping. Best for engineers who want the real thing.", "Boutique studios, character preamp seekers", "$1,800 — $3,500"),
            ("Original V76 module (restored)", "Vintage mic preamp module, restored. The flagship original. Best for commercial rooms and engineers chasing the German vocal sound.", "Commercial rooms, vocal-focused work", "$3,500 — $6,500"),
            ("Modern reproduction (Wunder, Vintech, Gyraf)", "Modern build, original circuit. More reliable, easier to service. Best for working studios that need long-term reliability.", "Working pros, project studios", "$1,495 — $3,995"),
        ],
        faqs=[
            ("Are V72 and V76 modules interchangeable?", "No. V72 is line-level (34 dB gain) and V76 is microphone-level (76 dB gain). Both are tube preamps with similar voicing, but they serve different purposes."),
            ("Are vintage modules reliable enough for daily use?", "After professional restoration — yes. The Tech Shop fully restores V72 and V76 modules, including tube replacement, recapping, and transformer service."),
            ("Should I buy vintage or a modern reproduction?", "Both are valid. Vintage carries collector value and the exact original circuit. Modern reproductions are more reliable and serviceable. Pick based on your priorities."),
            ("Do you service vintage V72 / V76 modules?", "Yes — the Tech Shop fully restores vintage German broadcast modules, including modern PSU integration and 19-inch rack mounting."),
        ],
    ),
    "universal-audio-175b.html": dict(
        slug="universal-audio-175b", name="UA 175B", full_name="Universal Audio 175B Compressor / Limiter",
        year=1961, era_dates="1961 — 1965 (Original)",
        summary="Bill Putnam's first compressor design — the all-tube 175B that paved the way for the LA-2A and 1176. A limiter built on a 6386 tube and the foundation of the Universal Audio sound. Rare, coveted, and historically essential.",
        hero_meta_pills=[("1961", "Year introduced"), ("6386", "Vacuum tube"), ("Mono", "Single channel"), ("Bill Putnam", "Designer")],
        history_para="The Universal Audio 175B was Bill Putnam's first commercially produced limiter. Designed in 1961 at his United Recording facility, the 175B used a 6386 dual-triode tube for gain reduction and an all-tube signal path. It became the standard vocal limiter at United Western and was the direct ancestor of the Teletronix LA-2A — Putnam licensed the LA-2A design after acquiring Teletronix in 1965. Today the 175B is one of the rarest Putnam designs, with surviving units trading hands at $8,000 to $15,000.",
        key_features=[
            ("6386 tube gain reduction", "The 6386 dual-triode is the heart of the 175B. Variable-gain triode topology — slow, smooth, musical compression with built-in tube harmonic content."),
            ("All-tube signal path", "Input transformer, tube gain stage, tube gain reduction, tube output. No solid-state in the audio chain."),
            ("Putnam design pedigree", "Direct ancestor of the LA-2A. Bill Putnam's design philosophy of 'musical compression that you do not hear' starts here."),
        ],
        versions=[
            ("1961 — 1963", "Original 175", "First production run. Two-rack-unit chassis. Now extremely rare — fewer than 200 estimated to survive."),
            ("1963 — 1965", "175B revision", "Updated revision with circuit refinements. Most common surviving variant. Still very rare."),
            ("Modern Plugin", "UAD 175B Emulation", "Universal Audio's UAD plugin emulation of the 175B. Closest you can get to the original sound without owning the hardware."),
        ],
        studios=[
            ("United Western — LA", "Bill Putnam's original room. The 175B was the standard vocal limiter on Sinatra, Nat King Cole, and Beach Boys sessions."),
            ("Ocean Way — LA", "Allen Sides preserved the United Western philosophy at Ocean Way. Original 175B units still in regular rotation."),
            ("Capitol Studios — LA", "Capitol's mastering and tracking rooms used 175B units on vocals throughout the 1960s. A few originals remain in service."),
        ],
        records=[
            "Frank Sinatra — September of My Years",
            "Nat King Cole — Stay With Me (vocals)",
            "The Beach Boys — Pet Sounds (selected vocals)",
            "Sam Cooke — Live at the Harlem Square Club",
            "Various Brian Wilson productions",
        ],
        quote=("The 175B is one of those design pieces — you can feel Bill Putnam working out the ideas that became the LA-2A. Slow, gentle, musical compression that flatters anything you put through it.", "Mike Nehra", "Co-Founder · Vintage King"),
        buyer_guide=[
            ("Original 175B (restored)", "Vintage 175B, professionally restored by the Tech Shop. Tube replacement, recap, transformer service. Best for collectors and historic-sound rooms.", "Collectors, historic-sound studios", "$8,000 — $15,000"),
            ("UAD 175B plugin", "Universal Audio's official emulation. The closest you can get to the original sound at a working-engineer price.", "Working studios, hybrid setups", "Plugin pricing"),
            ("LA-2A (the descendant)", "If you cannot find a 175B, the LA-2A is the design that grew out of it. More common, more affordable, similar philosophy.", "Most working studios", "$3,995 — $5,000+"),
        ],
        faqs=[
            ("How rare is the 175B really?", "Very rare. Fewer than 1,000 units shipped during the 1961 — 1965 production run, and most have been lost or scrapped. Surviving working examples come up for sale a handful of times per year."),
            ("Does the 175B sound like an LA-2A?", "Closely related but not identical. Both use slow optical-style gain reduction in tube circuits. The 175B has slightly different transformers and tube selection. Most engineers describe the 175B as 'an LA-2A with a touch more weight.'"),
            ("Is the UAD plugin a real substitute?", "For most working uses — yes. UA's emulation captures the harmonic character and gain reduction behavior. For collectors and historic rooms, the hardware is irreplaceable."),
            ("Can the Tech Shop restore an original 175B?", "Yes — full restoration including 6386 tube sourcing, transformer service, and recap. We have restored several original units."),
        ],
    ),
}


# ───────────────────────── AVID + UA PAGES (4) ─────────────────────────

NEIGHBORS_COMMERCE = [
    ("Studio Installations", "#"),
    ("Sell or Trade", "#"),
    ("Trade Program", "trade-program.html"),
]


def avid_trade_in_body():
    body = '''
<section class="pg-hero">
  <div class="pg-hero-inner">
    <div>
      <div class="pg-eyebrow">Avid Pro Tools Trade-In Program</div>
      <h1>Trade in your old Avid hardware. Step into the latest Pro Tools rig.</h1>
      <p class="lead speakable">Vintage King is an authorized Avid trade-in partner. Send us your existing Pro Tools HDX, HD Native, MTRX, S6, S4, or interface — get a real-world trade value applied directly to your next Avid system.</p>
      <div class="pg-cta-row">
        <a href="#start" class="pg-btn">Get Trade Quote →</a>
        <a href="#how" class="pg-btn-ghost">How It Works</a>
      </div>
    </div>
    <div class="pg-hero-img">Avid Pro Tools rig · placeholder</div>
  </div>
</section>

<div class="pg-strip"><div class="pg-strip-inner">
  <div class="pg-strip-item"><strong>Authorized</strong> Avid trade-in partner</div>
  <div class="pg-strip-item"><strong>Same-day</strong> trade quotes</div>
  <div class="pg-strip-item"><strong>Apply credit</strong> directly to your next purchase</div>
  <div class="pg-strip-item"><strong>VK Warranty</strong> on every new system</div>
</div></div>

<section class="pg-section pg-section-off">
  <div class="pg-wrap">
    <div class="pg-stats">
      <div class="pg-stat"><div class="pg-stat-num">$1.2M+</div><div class="pg-stat-label">Avid trade value paid in 2025</div></div>
      <div class="pg-stat"><div class="pg-stat-num">450+</div><div class="pg-stat-label">Pro Tools systems traded</div></div>
      <div class="pg-stat"><div class="pg-stat-num">24 hr</div><div class="pg-stat-label">Average quote turnaround</div></div>
      <div class="pg-stat"><div class="pg-stat-num">15+ yr</div><div class="pg-stat-label">Authorized Avid partner</div></div>
    </div>

    <div class="pg-eyebrow">What We Take</div>
    <h2 class="pg-h2">Eligible Avid hardware for trade.</h2>
    <p class="pg-sub">From individual interfaces to full S6 control surfaces. If it has the Avid logo, talk to us first.</p>
    <div class="pg-grid pg-grid-4">
      <div class="pg-card"><h3>HDX / HD Native</h3><p>HDX cards, HD Native chassis, Sync HD, and PCIe cards. All generations accepted.</p></div>
      <div class="pg-card"><h3>MTRX / MTRX Studio</h3><p>MTRX, MTRX Studio, MTRX II, and all expansion cards.</p></div>
      <div class="pg-card"><h3>Carbon / Mbox</h3><p>Carbon, Mbox 3, Mbox Studio, and all interface generations.</p></div>
      <div class="pg-card"><h3>S6 / S4 / S3</h3><p>S6 modules and full surfaces, S4, S3, Artist Series controllers.</p></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-white" id="how">
  <div class="pg-wrap">
    <div class="pg-eyebrow">How It Works</div>
    <h2 class="pg-h2">Three steps. One quote.</h2>
    <p class="pg-sub">From first call to credit applied — typically under one week.</p>
    <div class="pg-grid pg-grid-3">
      <div class="pg-card"><div style="font-family:var(--font-body);font-size:30px;font-weight:700;color:var(--page-accent);line-height:1;margin-bottom:12px">01</div><h3>Submit Your Gear</h3><p>Use the form below to list what you have. Photos help. Spec sheets help more.</p></div>
      <div class="pg-card"><div style="font-family:var(--font-body);font-size:30px;font-weight:700;color:var(--page-accent);line-height:1;margin-bottom:12px">02</div><h3>Get a Quote</h3><p>An Avid specialist responds within 24 hours with trade-in value and next-system options.</p></div>
      <div class="pg-card"><div style="font-family:var(--font-body);font-size:30px;font-weight:700;color:var(--page-accent);line-height:1;margin-bottom:12px">03</div><h3>Apply the Credit</h3><p>Trade credit applies directly to your new system. We coordinate shipment, integration, and install.</p></div>
    </div>
  </div>
</section>

<section class="pg-dark">
  <div class="pg-dark-inner">
    <div>
      <div class="pg-eyebrow">Why Trade With VK</div>
      <h2>The largest authorized Avid dealer in pro audio.</h2>
      <p>VK has placed Pro Tools systems in more commercial rooms than nearly any dealer in North America. We know the upgrade path because we have walked it with hundreds of studios.</p>
      <p style="margin-top:18px">Trade-in credit applies to any new Avid hardware — including custom S6 builds, MTRX integrations, and HDX system migrations.</p>
    </div>
    <div class="pg-quote">
      <p class="pg-quote-text">"VK took our 10-year-old HDX rig in trade and built us a turnkey HDX 3 / MTRX II room. The trade credit covered nearly half the upgrade."</p>
      <div class="pg-quote-att">Studio Owner<small>Multi-room facility · 2024 trade</small></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-off" id="start">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Start Your Trade</div>
    <h2 class="pg-h2">Tell us what you have.</h2>
    <p class="pg-sub">An Avid specialist responds within one business day with a trade quote and next-system options.</p>
    <form style="background:#fff;border:1px solid rgba(26,26,24,0.08);border-radius:4px;padding:36px;max-width:760px" onsubmit="event.preventDefault();this.querySelector('button').textContent='Sent — quote in 24 hours';">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">
        <div><label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin-bottom:6px">Your name</label><input type="text" required style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px"></div>
        <div><label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin-bottom:6px">Email</label><input type="email" required style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px"></div>
      </div>
      <label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin:18px 0 6px">What you have for trade</label>
      <textarea placeholder="Example: HDX 2 card, HD I/O 16x16, Sync HD, S3 controller…" required style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px;min-height:100px"></textarea>
      <label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin:18px 0 6px">What you're upgrading to</label>
      <textarea placeholder="Example: HDX 3 + MTRX II + S4 16-fader…" style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px;min-height:80px"></textarea>
      <button type="submit" style="margin-top:22px;width:100%;background:var(--page-accent);color:#fff;font-size:14px;font-weight:600;letter-spacing:0.04em;padding:14px;border:none;border-radius:2px;cursor:pointer">Request Trade Quote →</button>
    </form>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">FAQ</div>
    <h2 class="pg-h2">Common questions.</h2>
    <div class="pg-faq" style="border:1px solid rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;max-width:920px">
      <details><summary>How is trade value calculated?</summary><div class="pg-faq-a">Avid specialists base trade value on current market value, condition, generation, and whether the gear is being applied to a new Avid purchase. Trade-toward-new typically yields 15 — 25% above outright sale value.</div></details>
      <details><summary>Do I have to upgrade to new Avid hardware?</summary><div class="pg-faq-a">No — but trade-in credit only applies to Avid product purchases. If you want to convert to cash, the <a href="trade-program.html" style="color:var(--page-accent)">Sell or Trade desk</a> is your route.</div></details>
      <details><summary>Do you handle install and migration?</summary><div class="pg-faq-a">Yes. Our integration team handles HDX migration, MTRX configuration, and full system commissioning. Available remote or on-site.</div></details>
      <details><summary>What about Pro Tools software licenses?</summary><div class="pg-faq-a">Pro Tools subscriptions transfer with the hardware in most cases. We coordinate license transfer and any required Avid account changes during the trade process.</div></details>
    </div>
  </div>
</section>
'''
    sticky = {
        "title": "Avid Pro Tools Trade-In",
        "sub": "Authorized partner · 24-hour quote turnaround · Apply credit to new Avid systems",
        "cta_href": "#start",
        "cta_label": "Get Trade Quote →"
    }
    return body, sticky


def avid_surface_body(model_name: str, fader_options: list, key_features: list, target_users: list, faqs: list):
    surface_features = "".join(
        f'<div class="pg-card"><h3>{h}</h3><p>{p}</p></div>'
        for h, p in key_features
    )
    fader_html = "".join(
        f'<div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">{lbl}</div><h3>{h}</h3><p>{d}</p></div>'
        for lbl, h, d in fader_options
    )
    target_html = "".join(
        f'<div class="pg-card"><h3>{h}</h3><p>{p}</p></div>'
        for h, p in target_users
    )
    faq_html = "".join(
        f'<details><summary>{q}</summary><div class="pg-faq-a">{a}</div></details>'
        for q, a in faqs
    )

    body = f'''
<section class="pg-hero">
  <div class="pg-hero-inner">
    <div>
      <div class="pg-eyebrow">Avid {model_name} · Configuration Guide</div>
      <h1>Avid {model_name} Control Surface — choose the right configuration.</h1>
      <p class="lead speakable">The Avid {model_name} is modular. Start with the master section, scale faders to your room, and add surface modules as the workflow demands. VK's Avid specialists configure dozens of {model_name} systems every year — talk to us before you buy.</p>
      <div class="pg-cta-row">
        <a href="#configure" class="pg-btn">Get Configuration →</a>
        <a href="#options" class="pg-btn-ghost">See Configurations</a>
      </div>
    </div>
    <div class="pg-hero-img">Avid {model_name} · placeholder</div>
  </div>
</section>

<div class="pg-strip"><div class="pg-strip-inner">
  <div class="pg-strip-item"><strong>Authorized</strong> Avid dealer</div>
  <div class="pg-strip-item"><strong>Pre-config</strong> and EUCON setup</div>
  <div class="pg-strip-item"><strong>On-site install</strong> available</div>
  <div class="pg-strip-item"><strong>VK Warranty</strong> on every system</div>
</div></div>

<section class="pg-section pg-section-off" id="options">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Fader Configurations</div>
    <h2 class="pg-h2">Choose your fader count.</h2>
    <p class="pg-sub">{model_name} scales from compact mix configurations to full multi-room control. Pick the surface that matches your workflow.</p>
    <div class="pg-grid pg-grid-3">{fader_html}</div>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Key Features</div>
    <h2 class="pg-h2">What sets {model_name} apart.</h2>
    <p class="pg-sub">EUCON-based control. Modular surface. Built for hybrid mix and post workflows.</p>
    <div class="pg-grid pg-grid-3">{surface_features}</div>
  </div>
</section>

<section class="pg-section pg-section-off">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Who It's For</div>
    <h2 class="pg-h2">{model_name} fits these workflows.</h2>
    <p class="pg-sub">If your room is doing one of these jobs, {model_name} is a strong candidate.</p>
    <div class="pg-grid pg-grid-3">{target_html}</div>
  </div>
</section>

<section class="pg-dark">
  <div class="pg-dark-inner">
    <div>
      <div class="pg-eyebrow">Why Buy Through VK</div>
      <h2>{model_name} configuration is half the battle.</h2>
      <p>The {model_name} is the most flexible surface Avid makes — which means it is also the easiest to mis-configure. VK's Avid specialists pre-build, EUCON-test, and burn-in every system before it ships.</p>
      <p style="margin-top:18px">Trade your old Avid surface against your new {model_name}. Most {model_name} buyers qualify for VK Credit Card financing.</p>
    </div>
    <div class="pg-quote">
      <p class="pg-quote-text">"VK pre-configured the {model_name} for our workflow before it shipped. We were mixing on it the day it landed."</p>
      <div class="pg-quote-att">Mix Engineer<small>Hybrid post studio · 2024</small></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-cta" id="configure">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Get a Configuration</div>
    <h2 class="pg-h2">Tell us about the room.</h2>
    <p class="pg-sub">An Avid specialist responds within one business day with a configuration recommendation and quote.</p>
    <form style="background:#fff;border:1px solid rgba(26,26,24,0.08);border-radius:4px;padding:36px;max-width:760px" onsubmit="event.preventDefault();this.querySelector('button').textContent='Sent — configuration in 24 hours';">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">
        <div><label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin-bottom:6px">Your name</label><input type="text" required style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px"></div>
        <div><label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin-bottom:6px">Email</label><input type="email" required style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px"></div>
      </div>
      <label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin:18px 0 6px">Workflow</label>
      <select required style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px"><option value="">Select…</option><option>Music mix</option><option>Music tracking + mix</option><option>Post / film mix</option><option>Live broadcast</option><option>Multi-room facility</option></select>
      <label style="display:block;font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.55);margin:18px 0 6px">Notes</label>
      <textarea placeholder="Existing rig, room dimensions, timeline, trade-in plans…" style="width:100%;padding:12px 14px;font-size:14px;border:1px solid rgba(26,26,24,0.15);border-radius:2px;min-height:100px"></textarea>
      <button type="submit" style="margin-top:22px;width:100%;background:var(--page-accent);color:#fff;font-size:14px;font-weight:600;letter-spacing:0.04em;padding:14px;border:none;border-radius:2px;cursor:pointer">Request Configuration →</button>
    </form>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">FAQ</div>
    <h2 class="pg-h2">Common {model_name} questions.</h2>
    <div class="pg-faq" style="border:1px solid rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;max-width:920px">{faq_html}</div>
  </div>
</section>
'''
    sticky = {
        "title": f"Avid {model_name} Configuration",
        "sub": "Pre-configured · EUCON-tested · VK Warranty",
        "cta_href": "#configure",
        "cta_label": "Get Configuration →"
    }
    return body, sticky


def ua_promotions_body():
    body = '''
<section class="pg-hero">
  <div class="pg-hero-inner">
    <div>
      <div class="pg-eyebrow">Universal Audio · Current Promotions</div>
      <h1>Universal Audio promotions and bundle deals at Vintage King.</h1>
      <p class="lead speakable">Apollo trade-up, plug-in bundles, UAD-2 promotions, and exclusive VK bundles. All current Universal Audio offers in one place — updated as UA releases new programs.</p>
      <div class="pg-cta-row">
        <a href="#deals" class="pg-btn">See Current Deals →</a>
        <a href="#consult" class="pg-btn-ghost">Talk to a UA Specialist</a>
      </div>
    </div>
    <div class="pg-hero-img">UA Apollo / LUNA · placeholder</div>
  </div>
</section>

<div class="pg-strip"><div class="pg-strip-inner">
  <div class="pg-strip-item"><strong>Authorized</strong> UA dealer since the 1990s</div>
  <div class="pg-strip-item"><strong>UAD plug-ins</strong> available with bundles</div>
  <div class="pg-strip-item"><strong>Trade-up</strong> programs supported</div>
  <div class="pg-strip-item"><strong>VK Warranty</strong> on every UA system</div>
</div></div>

<section class="pg-section pg-section-off" id="deals">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Active Promotions</div>
    <h2 class="pg-h2">What's running right now.</h2>
    <p class="pg-sub">UA promotions rotate through the year. These are the active programs available through VK as of this quarter.</p>
    <div class="pg-grid pg-grid-3">
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Apollo Bundle</div><h3>Apollo X + UAD Bundle</h3><p>Apollo X interface paired with curated UAD plug-in bundle. Standard configuration for new project studios.</p><ul><li>Apollo X4, X8, or X8p</li><li>UAD plug-in bundle included</li><li>Trade-up eligible</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Hardware Bundle</div><h3>Apollo Twin X + LUNA</h3><p>Apollo Twin X with LUNA recording system. Best entry point for hybrid project studios.</p><ul><li>Apollo Twin X Duo / Quad</li><li>LUNA recording system</li><li>Starter UAD plug-in pack</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Plug-in Promo</div><h3>UAD Plug-in Bundles</h3><p>Curated plug-in bundles by genre or workflow. Available alongside any current Apollo or UAD-2 hardware purchase.</p><ul><li>Mix Essentials bundle</li><li>Vocal Production bundle</li><li>Hybrid Mastering bundle</li></ul></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Trade-Up Programs</div>
    <h2 class="pg-h2">Upgrade your UA hardware.</h2>
    <p class="pg-sub">Universal Audio supports trade-up paths from older Apollo and UAD-2 hardware to current generations. VK handles the trade transaction and applies credit to your new system.</p>
    <div class="pg-grid pg-grid-3">
      <div class="pg-card"><h3>Apollo Trade-Up</h3><p>Trade your original Apollo or Apollo Twin against current Apollo X hardware. Talk to a UA specialist for trade value.</p></div>
      <div class="pg-card"><h3>UAD-2 Trade-Up</h3><p>Trade UAD-2 satellites and PCIe cards against current Apollo X or Apollo X Twin hardware.</p></div>
      <div class="pg-card"><h3>Plug-in Migration</h3><p>UAD plug-in licenses transfer with hardware. We coordinate the license migration during trade.</p></div>
    </div>
  </div>
</section>

<section class="pg-dark">
  <div class="pg-dark-inner">
    <div>
      <div class="pg-eyebrow">Why Buy UA From VK</div>
      <h2>Authorized UA partner since the 1990s.</h2>
      <p>VK has placed Apollo, UAD-2, LUNA, and Apollo X systems in more rooms than nearly any North American dealer. We know the ecosystem because we have walked customers through every generation.</p>
      <p style="margin-top:18px">Talk to a UA specialist before you commit to a configuration — workflow, plug-in usage, and integration needs all change which Apollo or LUNA setup is right.</p>
    </div>
    <div class="pg-quote">
      <p class="pg-quote-text">"VK helped us migrate three rooms from UAD-2 satellites to Apollo X. The trade credit covered nearly half the upgrade."</p>
      <div class="pg-quote-att">Studio Owner<small>Multi-room facility · 2024</small></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-cta" id="consult">
  <div class="pg-wrap" style="text-align:center">
    <div class="pg-eyebrow">Talk to a UA Specialist</div>
    <h2 class="pg-h2">Find the right UA configuration.</h2>
    <p class="pg-sub" style="margin-left:auto;margin-right:auto">A Universal Audio specialist will walk you through current promotions, trade-up options, and the right Apollo or LUNA setup for your room. Free consultation.</p>
    <div class="pg-cta-row" style="justify-content:center">
      <a href="audio-consultants.html" class="pg-btn">Talk to a Consultant →</a>
      <a href="vk-credit-card.html" class="pg-btn-ghost">Financing Options</a>
    </div>
  </div>
</section>
'''
    sticky = {
        "title": "Universal Audio Promotions",
        "sub": "Active deals · Trade-up programs · Authorized UA dealer",
        "cta_href": "#consult",
        "cta_label": "Talk to UA Specialist →"
    }
    return body, sticky


def ua_apollo_x_body():
    body = '''
<section class="pg-hero">
  <div class="pg-hero-inner">
    <div>
      <div class="pg-eyebrow">Universal Audio · Apollo X Series</div>
      <h1>UA Apollo X Thunderbolt Audio Interfaces — choose your Apollo.</h1>
      <p class="lead speakable">Apollo X is the current generation of UA's flagship Thunderbolt interfaces. Six models from desktop to rackmount, all with built-in HEXA Core UAD-2 processing. VK is an authorized UA dealer for the full Apollo X lineup.</p>
      <div class="pg-cta-row">
        <a href="#models" class="pg-btn">See All Models →</a>
        <a href="#consult" class="pg-btn-ghost">Talk to UA Specialist</a>
      </div>
    </div>
    <div class="pg-hero-img">Apollo X8 / X8p · placeholder</div>
  </div>
</section>

<div class="pg-strip"><div class="pg-strip-inner">
  <div class="pg-strip-item"><strong>Authorized UA dealer</strong> · since the 1990s</div>
  <div class="pg-strip-item"><strong>HEXA Core</strong> UAD-2 processing built in</div>
  <div class="pg-strip-item"><strong>Thunderbolt 3</strong> · all current models</div>
  <div class="pg-strip-item"><strong>Trade-up</strong> from older Apollo</div>
</div></div>

<section class="pg-section pg-section-off" id="models">
  <div class="pg-wrap">
    <div class="pg-eyebrow">The Apollo X Lineup</div>
    <h2 class="pg-h2">Six models. One platform.</h2>
    <p class="pg-sub">From the desktop Apollo Twin X to the flagship Apollo X16. Same UAD-2 processing engine, same UA preamps, scaled to your room.</p>
    <div class="pg-grid pg-grid-3">
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Desktop · 2 inputs</div><h3>Apollo Twin X</h3><p>Two Unison preamps, two outputs, plus headphone. Duo or Quad UAD core. The standard project-studio Apollo.</p><ul><li>2 mic / line inputs</li><li>Duo or Quad Core UAD-2</li><li>Thunderbolt 3</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Rack · 4 inputs</div><h3>Apollo X4</h3><p>Four Unison preamps, talkback, and additional outputs. Quad Core UAD-2. Compact tracking rig in 1U.</p><ul><li>4 mic / line inputs</li><li>Quad Core UAD-2</li><li>1U rackmount</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Rack · 8 inputs</div><h3>Apollo X6</h3><p>Six analog inputs, six outputs, talkback, dual headphone. HEXA Core UAD-2. Mid-tier tracking and mixing.</p><ul><li>6 mic / line inputs</li><li>HEXA Core UAD-2</li><li>1U rackmount</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Rack · 8 inputs</div><h3>Apollo X8</h3><p>Eight analog inputs, eight outputs, talkback. HEXA Core UAD-2. Standard configuration for commercial tracking rooms.</p><ul><li>8 mic / line inputs</li><li>HEXA Core UAD-2</li><li>2U rackmount</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Rack · 8 inputs</div><h3>Apollo X8p</h3><p>Eight Unison mic preamps (vs X8's eight line ins). HEXA Core UAD-2. Best for tracking-heavy rooms.</p><ul><li>8 Unison mic preamps</li><li>HEXA Core UAD-2</li><li>2U rackmount</li></ul></div>
      <div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">Rack · 16 inputs</div><h3>Apollo X16 / X16D</h3><p>Sixteen analog inputs, sixteen outputs. HEXA Core UAD-2. Flagship — for full tracking rooms and high-IO mix rigs.</p><ul><li>16 line inputs</li><li>HEXA Core UAD-2</li><li>2U rackmount</li></ul></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">What All Apollo X Share</div>
    <h2 class="pg-h2">The platform features.</h2>
    <p class="pg-sub">Every Apollo X uses the same converters, the same UAD-2 engine, and the same Unison preamp emulation system.</p>
    <div class="pg-grid pg-grid-4">
      <div class="pg-card"><h3>HEXA Core UAD-2</h3><p>Six DSP cores for real-time UAD plug-in processing during tracking and mixing.</p></div>
      <div class="pg-card"><h3>Unison Preamps</h3><p>Hardware preamp emulation that re-creates the impedance and gain staging of classic preamps in real time.</p></div>
      <div class="pg-card"><h3>Thunderbolt 3</h3><p>Bus-powered or external power depending on model. Low-latency monitoring throughout.</p></div>
      <div class="pg-card"><h3>Built-in Talkback</h3><p>Talkback mic and routing built into rackmount models. Coordinates with LUNA recording system.</p></div>
    </div>
  </div>
</section>

<section class="pg-dark">
  <div class="pg-dark-inner">
    <div>
      <div class="pg-eyebrow">Apollo + LUNA</div>
      <h2>Apollo X works with any DAW. LUNA makes it sing.</h2>
      <p>Apollo X interfaces work with Pro Tools, Logic, Cubase, Studio One — any DAW. UA's free LUNA recording system unlocks Unison and Apollo's full integration features.</p>
      <p style="margin-top:18px">Most working studios run Apollo X alongside Pro Tools or Logic. Project studios increasingly choose LUNA for the deep UAD integration.</p>
    </div>
    <div class="pg-quote">
      <p class="pg-quote-text">"Apollo X8 + LUNA + the right UAD bundle is the most cost-effective tracking rig you can build today. VK helped us spec it for the room."</p>
      <div class="pg-quote-att">Project Studio Owner<small>2024</small></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-cta" id="consult">
  <div class="pg-wrap" style="text-align:center">
    <div class="pg-eyebrow">Find the Right Apollo X</div>
    <h2 class="pg-h2">Talk to a UA specialist.</h2>
    <p class="pg-sub" style="margin-left:auto;margin-right:auto">Workflow, channel count, and budget all change which Apollo X is right for your room. Free consultation.</p>
    <div class="pg-cta-row" style="justify-content:center">
      <a href="audio-consultants.html" class="pg-btn">Talk to UA Specialist →</a>
      <a href="universal-audio-promotions.html" class="pg-btn-ghost">See Current Promotions</a>
    </div>
  </div>
</section>
'''
    sticky = {
        "title": "UA Apollo X Audio Interfaces",
        "sub": "Authorized UA dealer · Trade-up supported · VK Warranty",
        "cta_href": "#consult",
        "cta_label": "Talk to UA Specialist →"
    }
    return body, sticky


# ───────────────────────── CAMPAIGN PAGES (3) ─────────────────────────

NEIGHBORS_CAMPAIGN = [
    ("All Deals", "#"),
    ("Demo Deals", "#"),
    ("Open Box", "#"),
]


def campaign_body(name: str, eyebrow: str, hook: str, lead: str, dates: str,
                  category_grid: list, value_props: list, faqs: list,
                  cta_label: str = "Shop the Sale →"):
    cat_html = "".join(
        f'<div class="pg-card"><div style="font-size:11px;color:var(--page-accent);font-weight:700;letter-spacing:0.16em;text-transform:uppercase;margin-bottom:8px">{lbl}</div><h3>{h}</h3><p>{p}</p></div>'
        for lbl, h, p in category_grid
    )
    val_html = "".join(
        f'<div class="pg-card"><h3>{h}</h3><p>{p}</p></div>'
        for h, p in value_props
    )
    faq_html = "".join(
        f'<details><summary>{q}</summary><div class="pg-faq-a">{a}</div></details>'
        for q, a in faqs
    )
    body = f'''
<section class="pg-hero">
  <div class="pg-hero-inner">
    <div>
      <div class="pg-eyebrow">{eyebrow} · {dates}</div>
      <h1>{hook}</h1>
      <p class="lead speakable">{lead}</p>
      <div class="pg-cta-row">
        <a href="#categories" class="pg-btn">{cta_label}</a>
        <a href="#consult" class="pg-btn-ghost">Talk to a Consultant</a>
      </div>
    </div>
    <div class="pg-hero-img">{name} · placeholder</div>
  </div>
</section>

<div class="pg-strip"><div class="pg-strip-inner">
  <div class="pg-strip-item"><strong>Authorized dealer</strong> · 110+ brands</div>
  <div class="pg-strip-item"><strong>Free shipping</strong> on orders over $99</div>
  <div class="pg-strip-item"><strong>0% financing</strong> available</div>
  <div class="pg-strip-item"><strong>VK Warranty</strong> on every product</div>
</div></div>

<section class="pg-section pg-section-off" id="categories">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Shop the Categories</div>
    <h2 class="pg-h2">{name} deals by category.</h2>
    <p class="pg-sub">Filter the deals by gear category. Talk to a consultant for bundle pricing and trade-in options.</p>
    <div class="pg-grid pg-grid-3">{cat_html}</div>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">Why VK</div>
    <h2 class="pg-h2">More than discount pricing.</h2>
    <p class="pg-sub">VK pairs every sale with the same engineer-to-engineer service we offer year-round.</p>
    <div class="pg-grid pg-grid-4">{val_html}</div>
  </div>
</section>

<section class="pg-dark">
  <div class="pg-dark-inner">
    <div>
      <div class="pg-eyebrow">Bundle Pricing</div>
      <h2>The biggest deals don't show up on the product page.</h2>
      <p>Multi-piece purchases, room outfits, and trade-in deals get custom pricing through our consultants. Tell us what you need built.</p>
      <p style="margin-top:18px">{name} bundle quotes go out within one business day.</p>
    </div>
    <div class="pg-quote">
      <p class="pg-quote-text">"VK's {name} bundle saved us $4,200 versus the listed prices. The consultant put it together in an hour."</p>
      <div class="pg-quote-att">Project Studio Owner<small>2024 {name}</small></div>
    </div>
  </div>
</section>

<section class="pg-section pg-section-cta" id="consult">
  <div class="pg-wrap" style="text-align:center">
    <div class="pg-eyebrow">Bundle Pricing</div>
    <h2 class="pg-h2">Need more than one piece? Talk to us.</h2>
    <p class="pg-sub" style="margin-left:auto;margin-right:auto">Custom bundle quotes within one business day. Trade-in welcome. Financing available.</p>
    <div class="pg-cta-row" style="justify-content:center">
      <a href="audio-consultants.html" class="pg-btn">Talk to a Consultant →</a>
      <a href="vk-credit-card.html" class="pg-btn-ghost">Financing Options</a>
    </div>
  </div>
</section>

<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">FAQ</div>
    <h2 class="pg-h2">{name} questions.</h2>
    <div class="pg-faq" style="border:1px solid rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;max-width:920px">{faq_html}</div>
  </div>
</section>
'''
    sticky = {
        "title": f"{name}",
        "sub": f"{dates} · Bundle pricing on request · Free shipping over $99",
        "cta_href": "#categories",
        "cta_label": "Shop Now →"
    }
    return body, sticky


# ───────────────────────── POLICY PAGES (3) ─────────────────────────

NEIGHBORS_POLICY = [
    ("FAQ", "#"),
    ("VK Warranty", "warranty.html"),
    ("Returns", "returns.html"),
]


def policy_body(title: str, intro: str, sections: list[tuple[str, str]]):
    secs = "".join(f'<h2>{h}</h2>\n{c}\n' for h, c in sections)
    body = f'''
<section class="pg-hero" style="padding:72px 0">
  <div class="pg-hero-inner" style="grid-template-columns:1fr">
    <div>
      <div class="pg-eyebrow">Help · Policy</div>
      <h1 style="font-size:42px">{title}</h1>
      <p class="lead speakable" style="max-width:680px">{intro}</p>
    </div>
  </div>
</section>

<div class="policy-content">{secs}</div>

<section class="pg-section pg-section-cta">
  <div class="pg-wrap" style="text-align:center">
    <div class="pg-eyebrow">Need More Help?</div>
    <h2 class="pg-h2">Talk to us.</h2>
    <p class="pg-sub" style="margin-left:auto;margin-right:auto">Our team is available by phone, chat, or email. Free for any question.</p>
    <div class="pg-cta-row" style="justify-content:center">
      <a href="tel:8886531184" class="pg-btn">Call 888.653.1184 →</a>
      <a href="audio-consultants.html" class="pg-btn-ghost">Email a Consultant</a>
    </div>
  </div>
</section>
'''
    return body


# ───────────────────────── BUILD ALL ─────────────────────────

def build_all():
    out = []

    # 1. HOF gear pages
    for slug, cfg in HOF_PAGES.items():
        html = hof_gear_page(neighbors=NEIGHBORS_HOF, **cfg)
        (ROOT / slug).write_text(html)
        out.append(slug)

    # 2. Avid Pro Tools Trade-In
    body, sticky = avid_trade_in_body()
    jsonld = '''{"@context":"https://schema.org","@type":"Service","name":"Avid Pro Tools Trade-In Program","provider":{"@type":"Organization","name":"Vintage King Audio"},"description":"Authorized Avid trade-in program. Trade your existing Pro Tools HDX, HD Native, MTRX, S6, S4, or interface for credit toward your next Avid system.","areaServed":"US"}'''
    html = page_shell(
        title="Avid Pro Tools Trade-In Program — Authorized Avid Partner | Vintage King",
        meta="Trade your existing Pro Tools HDX, MTRX, S6, S4, or Avid interface for credit toward your next Avid system. Authorized Avid trade-in partner with 24-hour quote turnaround.",
        breadcrumb="Avid Pro Tools Trade-In",
        neighbors=NEIGHBORS_COMMERCE,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "avid-pro-tools-trade-in.html").write_text(html)
    out.append("avid-pro-tools-trade-in.html")

    # 3. Avid S4
    body, sticky = avid_surface_body(
        "S4",
        fader_options=[
            ("8 faders · 1 module", "S4 8-Fader", "Compact mix and post surface. Single 8-fader module plus master section. Best for project studios and broadcast booths."),
            ("16 faders · 2 modules", "S4 16-Fader", "Standard commercial mix surface. Two 8-fader modules. Good for music mix and small post rooms."),
            ("24 faders · 3 modules", "S4 24-Fader", "Full music mix or post surface. Three 8-fader modules. Sized for commercial mix rooms."),
        ],
        key_features=[
            ("EUCON control", "Direct EUCON integration with Pro Tools, Logic, Nuendo, Cubase, and most major DAWs."),
            ("Modular surface", "Add fader modules as your room scales. Same workflow whether you have 8 faders or 24."),
            ("Built-in displays", "Channel name displays, meter bridges, and color coding all built into the surface."),
        ],
        target_users=[
            ("Music mix rooms", "Commercial music mix engineers running Pro Tools or Logic. The 16- or 24-fader S4 is the standard config."),
            ("Post / broadcast", "Post and broadcast rooms running Pro Tools or Nuendo. The 8- or 16-fader S4 covers most workflows."),
            ("Hybrid project studios", "Producer / engineer rooms scaling beyond a controller. The 8-fader S4 is the entry point."),
        ],
        faqs=[
            ("How is the S4 different from the S6?", "The S4 is more compact, more affordable, and uses a slightly simplified module set. The S6 is the flagship surface with deeper channel knob count, more displays, and higher channel density. Both run on the same EUCON platform."),
            ("Does the S4 work with Logic, Cubase, Nuendo?", "Yes. S4 is EUCON-based and supports Pro Tools, Logic Pro, Cubase, Nuendo, and Studio One. Pro Tools integration is the deepest."),
            ("Can I add fader modules later?", "Yes. The S4 is fully modular. Start with 8 faders and add 8-fader modules later as your room scales."),
            ("Do you handle install?", "Yes. VK pre-configures every S4 surface, EUCON-tests the rig, and offers on-site install for commercial rooms."),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"Product","name":"Avid S4 Control Surface","brand":{"@type":"Brand","name":"Avid"},"category":"Audio Control Surface","description":"Modular EUCON-based control surface for Pro Tools and major DAWs. Available in 8, 16, and 24-fader configurations."}'''
    html = page_shell(
        title="Avid S4 Control Surface — Configuration Guide | Vintage King",
        meta="Choose the right Avid S4 control surface configuration. 8-, 16-, or 24-fader options, EUCON-based, configured by VK's authorized Avid specialists.",
        breadcrumb="Avid S4 Configurations",
        neighbors=NEIGHBORS_COMMERCE,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "avid-s4-control-surface-configurations.html").write_text(html)
    out.append("avid-s4-control-surface-configurations.html")

    # 4. Avid S6
    body, sticky = avid_surface_body(
        "S6",
        fader_options=[
            ("M40 · 16-fader", "S6 M40 16-Fader", "Compact flagship. Sixteen faders, full master section, three knob rows. Standard for boutique commercial mix rooms."),
            ("M40 · 32-fader", "S6 M40 32-Fader", "Mid-tier flagship. Thirty-two faders. Standard for full commercial music mix and post rooms."),
            ("M40 · 48-fader+", "S6 M40 Custom Build", "Custom builds up to 64 faders, multiple knob rows, and full surface module configurations. For large mix and post facilities."),
        ],
        key_features=[
            ("Modular per-channel", "Channel knob, color, display, and metering all per-channel. Deepest tactile control of any modern surface."),
            ("EUCON integration", "Native Pro Tools and major DAW support. Deepest Pro Tools integration of any controller."),
            ("Atmos / immersive ready", "Joystick, monitoring, and immersive bus support built into the master section."),
        ],
        target_users=[
            ("Flagship music rooms", "Top-tier commercial music mix engineers. 32- or 48-fader S6 M40 with deep knob configurations."),
            ("Film / Atmos post", "Post and Atmos mix stages. S6 with joystick module, monitoring section, and immersive bus configuration."),
            ("Multi-room facilities", "Commercial facilities outfitting multiple rooms. VK handles the multi-S6 install and shared infrastructure."),
        ],
        faqs=[
            ("How is the S6 different from the S4?", "The S6 has more channel knobs per strip, more display options, and supports much larger configurations (up to 64 faders). The S4 is a more compact, more affordable EUCON surface. Both share the EUCON platform."),
            ("Can I configure an S6 for Atmos?", "Yes. The S6 master section supports the joystick module, monitoring section, and immersive bus configuration needed for full Atmos workflows."),
            ("How long does an S6 install take?", "Pre-configuration takes 1 — 2 weeks. On-site install is typically 2 — 4 days for a 32-fader system. VK handles full install and EUCON commissioning."),
            ("What's the largest S6 you've installed?", "VK has installed S6 systems up to 64 faders for multi-room commercial facilities. Talk to us about custom configurations."),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"Product","name":"Avid S6 Control Surface","brand":{"@type":"Brand","name":"Avid"},"category":"Audio Control Surface","description":"Flagship EUCON-based modular control surface for Pro Tools, post, and Atmos. Configurable from 16 to 64 faders."}'''
    html = page_shell(
        title="Avid S6 Control Surface — Configuration Guide | Vintage King",
        meta="Configure the right Avid S6 system for your room. M40 16-, 32-, or 48-fader+ options, Atmos-ready, configured by VK's authorized Avid specialists.",
        breadcrumb="Avid S6 Configurations",
        neighbors=NEIGHBORS_COMMERCE,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "avid-s6-control-surface-configurations.html").write_text(html)
    out.append("avid-s6-control-surface-configurations.html")

    # 5. UA Promotions
    body, sticky = ua_promotions_body()
    jsonld = '''{"@context":"https://schema.org","@type":"WebPage","name":"Universal Audio Promotions and Deals","description":"Active Universal Audio promotions including Apollo bundles, UAD plug-in promotions, and trade-up programs through Vintage King."}'''
    html = page_shell(
        title="Universal Audio Promotions and Deals | Vintage King",
        meta="Active Universal Audio promotions including Apollo X bundles, UAD plug-in deals, and trade-up programs. Authorized UA dealer since the 1990s.",
        breadcrumb="UA Promotions",
        neighbors=[("UA Apollo X", "universal-audio-apollo-x.html"), ("Studio Installations", "#"), ("Financing", "vk-credit-card.html")],
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "universal-audio-promotions.html").write_text(html)
    out.append("universal-audio-promotions.html")

    # 6. UA Apollo X
    body, sticky = ua_apollo_x_body()
    jsonld = '''{"@context":"https://schema.org","@type":"Product","name":"Universal Audio Apollo X","brand":{"@type":"Brand","name":"Universal Audio"},"category":"Audio Interface","description":"Apollo X Thunderbolt audio interfaces with HEXA Core UAD-2 processing. Six models from desktop Apollo Twin X to flagship Apollo X16."}'''
    html = page_shell(
        title="UA Apollo X Thunderbolt Audio Interfaces — Choose Your Apollo | Vintage King",
        meta="Compare and configure Universal Audio Apollo X audio interfaces. Apollo Twin X, X4, X6, X8, X8p, and X16 — authorized UA dealer with full Apollo X lineup in stock.",
        breadcrumb="UA Apollo X",
        neighbors=[("UA Promotions", "universal-audio-promotions.html"), ("Studio Installations", "#"), ("Financing", "vk-credit-card.html")],
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "universal-audio-apollo-x.html").write_text(html)
    out.append("universal-audio-apollo-x.html")

    # 7. Black Friday — Microphones
    body, sticky = campaign_body(
        name="Black Friday — Microphones",
        eyebrow="Black Friday · Microphone Deals",
        hook="Black Friday microphone deals on the world's largest curated mic inventory.",
        lead="Tube, large-diaphragm, ribbon, dynamic, and small-diaphragm condensers — Black Friday pricing across 60+ brands. Deals refresh through Cyber Monday with bundle pricing on request.",
        dates="Through Cyber Monday",
        category_grid=[
            ("Tube Mics", "Large-Diaphragm Tube Condensers", "Telefunken, AKG, Manley, Wunder, Lewitt — Black Friday pricing on tube mics from $1,500 to $15,000+."),
            ("LDC", "Solid-State Large-Diaphragm Condensers", "Neumann, Sony, Audio-Technica, Aston, Lauten — solid-state LDCs from $499 to $5,000+."),
            ("Ribbons", "Ribbon Microphones", "Royer, AEA, Coles, Beyerdynamic — ribbon mic deals from $499 to $4,500+."),
            ("Dynamics", "Dynamic Microphones", "Shure, Sennheiser, Electro-Voice, Telefunken dynamic — broadcast and stage dynamics from $99 to $1,500+."),
            ("SDC Pairs", "Small-Diaphragm Condenser Pairs", "Schoeps, DPA, Neumann, Earthworks — matched pair pricing on the Black Friday floor."),
            ("Vintage", "Vintage and Used Microphones", "Curated vintage selection with Black Friday discounts. Trade-in toward new Black Friday deals welcome."),
        ],
        value_props=[
            ("Authorized dealer", "Authorized for 60+ microphone brands. Full warranty on every Black Friday purchase."),
            ("Bundle pricing", "Multi-mic and mic-plus-preamp bundles get custom pricing through a consultant."),
            ("Trade in", "Trade older mics toward Black Friday deals. Trade quotes within 24 hours."),
            ("Financing", "0% financing available on qualifying purchases through the VK Credit Card."),
        ],
        faqs=[
            ("When does Black Friday pricing end?", "Black Friday pricing typically runs through Cyber Monday. Some bundle deals extend into December — talk to a consultant for current end dates."),
            ("Can I combine Black Friday pricing with financing?", "Yes. The VK Credit Card 0% financing offers stack with Black Friday pricing on qualifying purchases."),
            ("Do you price-match?", "VK price-matches authorized dealers. Talk to a consultant for current price-match policies during Black Friday."),
            ("Can I trade in older gear?", "Yes. The Sell or Trade desk runs through Black Friday and beyond. Trade quotes go out within 24 hours."),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"SaleEvent","name":"Black Friday Microphone Deals at Vintage King","startDate":"2026-11-23","endDate":"2026-12-01","location":{"@type":"VirtualLocation","url":"https://vintageking.com"},"description":"Black Friday pricing across 60+ microphone brands. Tube, LDC, ribbon, dynamic, and small-diaphragm condensers on sale through Cyber Monday."}'''
    html = page_shell(
        title="Black Friday Microphone Deals 2026 | Vintage King",
        meta="Black Friday microphone deals on tube, LDC, ribbon, dynamic, and SDC microphones. 60+ brands, bundle pricing on request, financing available through Cyber Monday.",
        breadcrumb="Black Friday — Microphones",
        neighbors=NEIGHBORS_CAMPAIGN,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "black-friday-microphone-deals.html").write_text(html)
    out.append("black-friday-microphone-deals.html")

    # 8. New at NAMM — Microphones
    body, sticky = campaign_body(
        name="New at NAMM — Microphones",
        eyebrow="New at NAMM · Microphones",
        hook="The new microphones from NAMM, available to order now.",
        lead="Every microphone announced at NAMM, curated and ready to order. Tube reissues, new ribbon designs, and updated stage dynamics — all from authorized dealer relationships.",
        dates="2026 NAMM Show",
        category_grid=[
            ("Tube Reissues", "New Tube Microphones", "New tube mics introduced at NAMM 2026 from Telefunken, Manley, AKG, and boutique builders."),
            ("New LDCs", "New Solid-State LDCs", "Solid-state large-diaphragm condensers introduced at NAMM, including new Neumann, Aston, and Lewitt designs."),
            ("New Ribbons", "New Ribbon Microphones", "Royer, AEA, sE, and boutique ribbon launches from NAMM 2026. Active and passive designs."),
            ("Stage Mics", "New Stage and Broadcast Mics", "New dynamic and condenser stage microphones from Shure, Sennheiser, and Electro-Voice."),
            ("Wireless", "New Wireless Systems", "New wireless microphone systems for live, broadcast, and houses of worship."),
            ("Accessories", "New Mounts, Cables, and Accessories", "New shock mounts, isolation systems, and microphone accessories from NAMM 2026."),
        ],
        value_props=[
            ("First to ship", "VK is one of the first dealers to receive NAMM debut shipments from authorized brands."),
            ("Pre-order priority", "Pre-order at NAMM pricing for delivery as units ship."),
            ("Trade in", "Trade your existing mics toward NAMM debuts. Quotes within 24 hours."),
            ("Talk to consultants", "Audio consultants can compare NAMM debuts to existing favorites — call before you commit."),
        ],
        faqs=[
            ("When do NAMM debut microphones ship?", "Most NAMM debuts ship 4 — 12 weeks after announcement. VK pre-orders fill in the order they were placed."),
            ("Can I pre-order?", "Yes. VK accepts pre-orders for most NAMM debut microphones at announced pricing."),
            ("Will VK have demo units?", "VK occasionally receives demo units for new microphones. Talk to a consultant for demo availability on specific models."),
            ("Can I trade older gear toward NAMM debuts?", "Yes. Trade-in works on pre-orders too. Trade credit applies when the new mic ships."),
        ],
        cta_label="Shop NAMM Debuts →"
    )
    jsonld = '''{"@context":"https://schema.org","@type":"WebPage","name":"New at NAMM — Microphones","description":"Microphones debuted at the 2026 NAMM show. Tube reissues, new ribbons, stage mics, and accessories — available to pre-order from Vintage King."}'''
    html = page_shell(
        title="New at NAMM — Microphones | Vintage King",
        meta="Microphones debuted at the 2026 NAMM show — tube reissues, new ribbons, stage dynamics, and wireless. Pre-order from authorized dealer Vintage King.",
        breadcrumb="New at NAMM — Microphones",
        neighbors=NEIGHBORS_CAMPAIGN,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "new-at-namm-microphones.html").write_text(html)
    out.append("new-at-namm-microphones.html")

    # 9. Back to School
    body, sticky = campaign_body(
        name="Back to School",
        eyebrow="Back to School · Pro Audio Programs",
        hook="Back-to-school pricing for music students, audio programs, and educators.",
        lead="Curated bundles for student engineers, college audio programs, and educators. Verified student and educator pricing on Apollo, Pro Tools, headphones, microphones, and starter outboard.",
        dates="August through October",
        category_grid=[
            ("Interfaces", "Audio Interfaces for Students", "Apollo Twin X, Apollo X4, Focusrite, Audient, MOTU — student pricing on the standard project-studio rigs."),
            ("Software", "Pro Tools and DAW Subscriptions", "Pro Tools Education subscriptions, Logic Pro, Studio One — student-priced DAW packages."),
            ("Headphones", "Studio Headphones", "Beyerdynamic DT 770/990, Sennheiser HD 600/650, Audeze, Focal — back-to-school headphone pricing."),
            ("Microphones", "Starter Microphones", "Audio-Technica, sE, Aston, Rode — student-friendly large-diaphragm and small-diaphragm condensers."),
            ("Bundles", "Student Studio Bundles", "Curated bundles: Apollo Twin X + headphones + mic. Configured for the student bedroom studio."),
            ("Programs", "Audio Education Programs", "Discounted pricing for university and college audio programs. Multi-unit pricing on request."),
        ],
        value_props=[
            ("Student verification", "Student and educator pricing through SheerID verification. Verified once, valid through your enrollment."),
            ("Program pricing", "Custom pricing for college and university audio programs. Talk to a consultant for multi-unit quotes."),
            ("Financing", "0% financing on qualifying student bundles through the VK Credit Card."),
            ("Free shipping", "Free shipping on student orders over $99 — same as the standard floor."),
        ],
        faqs=[
            ("How do I get verified as a student?", "Use SheerID at checkout to verify student or educator status. Verification is free, takes a few minutes, and unlocks back-to-school pricing."),
            ("Are all products eligible?", "Most current-production new gear is eligible. Some manufacturer pricing rules exclude specific products — talk to a consultant if a specific product is not showing student pricing."),
            ("Can audio programs get bulk pricing?", "Yes. VK offers custom bulk pricing for accredited audio programs. Send the program a consultant inquiry for a quote."),
            ("Do you ship to dormitories?", "Yes. Standard shipping to dorms and college addresses. Larger items may require signature confirmation."),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"WebPage","name":"Back to School — Pro Audio for Students and Programs","description":"Back-to-school pricing for music students, audio programs, and educators. Verified student pricing on Apollo, Pro Tools, headphones, and mics."}'''
    html = page_shell(
        title="Back to School — Student Pro Audio Pricing | Vintage King",
        meta="Verified student and educator pricing on Apollo, Pro Tools, headphones, microphones, and starter outboard. Custom bundles for audio programs through October.",
        breadcrumb="Back to School",
        neighbors=NEIGHBORS_CAMPAIGN,
        jsonld=jsonld,
        body=body,
        sticky=sticky,
    )
    (ROOT / "back-to-school.html").write_text(html)
    out.append("back-to-school.html")

    # 10. Shipping Policy
    body = policy_body(
        title="Shipping Policy",
        intro="Free shipping on orders over $99 within the contiguous United States. Expedited and international shipping available. All orders ship from Detroit, Michigan, with same-day handling on orders placed by 2pm ET.",
        sections=[
            ("Standard Shipping", "<p>Free standard shipping on all orders over $99 shipped within the contiguous United States. Standard shipping is via FedEx Ground or USPS Priority and typically arrives within 2 — 5 business days from ship date.</p><p>Orders under $99 ship at calculated rates based on weight, dimensions, and destination.</p>"),
            ("Expedited Shipping", "<p>Expedited shipping options (FedEx 2-Day, FedEx Overnight) are available at checkout for an additional charge. Expedited orders placed before 2pm ET ship the same business day.</p><ul><li>FedEx 2-Day Air</li><li>FedEx Standard Overnight</li><li>FedEx Priority Overnight</li></ul>"),
            ("International Shipping", "<p>Vintage King ships to most countries worldwide. International shipping is calculated at checkout based on destination and package dimensions. Customers are responsible for any duties, taxes, or import fees assessed by the destination country.</p>"),
            ("Large and Oversized Items", "<p>Consoles, large surfaces, racks, and other oversized items ship via freight carrier. Freight shipments require a delivery appointment and a signature. White-glove install delivery is available for an additional charge.</p>"),
            ("Order Tracking", "<p>Tracking information is sent via email when your order ships. You can also view order status by signing in to your account.</p>"),
            ("Damaged or Lost Shipments", "<p>If your shipment arrives damaged or does not arrive within the expected timeframe, contact us within 7 days and we will work directly with the carrier to resolve the issue. Document any visible damage on the carrier's delivery confirmation.</p>"),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"WebPage","name":"Shipping Policy","description":"Vintage King shipping policy. Free standard shipping over $99 within the contiguous US. Expedited and international shipping available. Same-day handling before 2pm ET."}'''
    html = page_shell(
        title="Shipping Policy | Vintage King",
        meta="Vintage King shipping policy. Free shipping over $99 contiguous US, expedited options, international shipping, and freight delivery for large items.",
        breadcrumb="Shipping Policy",
        neighbors=NEIGHBORS_POLICY,
        jsonld=jsonld,
        body=body,
    )
    (ROOT / "shipping-policy.html").write_text(html)
    out.append("shipping-policy.html")

    # 11. Returns
    body = policy_body(
        title="Returns Policy",
        intro="30-day returns on most new gear. Return shipping is free for defective items and shipping errors. Test the gear; if it does not work for your room, send it back. Engineer-friendly, no-hassle process.",
        sections=[
            ("30-Day Return Window", "<p>Most new gear can be returned within 30 days of delivery for a full refund or exchange. The 30-day clock starts on delivery date as confirmed by the carrier.</p>"),
            ("Eligible Items", "<p>The following can be returned within the 30-day window:</p><ul><li>New gear in original packaging</li><li>Open-box and demo items (with original accessories)</li><li>Defective items (any condition)</li></ul>"),
            ("Items Not Eligible for Return", "<p>The following cannot be returned:</p><ul><li>Custom-built or special-order items (consoles, custom racks)</li><li>Vintage and used gear (sold as-is unless otherwise stated)</li><li>Software, plug-ins, and digital licenses (after activation)</li><li>Microphones if used past return inspection (hygiene)</li></ul>"),
            ("Return Process", "<p>Start a return by contacting our team via the Returns inquiry form or by phone. We issue an RMA number and a prepaid return label for defective items and shipping errors. Customer-initiated returns of working gear are responsible for return shipping.</p><ul><li>Pack the item securely in original packaging when possible</li><li>Include the RMA number on the outside of the package</li><li>Ship to the address provided with the RMA</li><li>Refunds process within 5 business days of receipt</li></ul>"),
            ("Restocking Fees", "<p>Most returns are processed without restocking fees. A restocking fee may apply if the item is returned in incomplete or damaged condition.</p>"),
            ("Warranty Repairs", "<p>Items under VK Warranty are repaired or replaced free of charge. Contact the Tech Shop for warranty repair process.</p>"),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"WebPage","name":"Returns Policy","description":"Vintage King returns policy. 30-day return window on most new gear. Free return shipping on defective items. No-hassle process for engineers."}'''
    html = page_shell(
        title="Returns Policy | Vintage King",
        meta="Vintage King 30-day returns policy on new gear. Free return shipping on defective items. Engineer-friendly process and clear eligibility rules.",
        breadcrumb="Returns Policy",
        neighbors=NEIGHBORS_POLICY,
        jsonld=jsonld,
        body=body,
    )
    (ROOT / "returns.html").write_text(html)
    out.append("returns.html")

    # 12. Privacy Policy
    body = policy_body(
        title="Privacy Policy",
        intro="Vintage King is committed to protecting your privacy. This policy explains what information we collect, how we use it, and the choices you have. Plain language, no surprises.",
        sections=[
            ("Information We Collect", "<p>We collect information you provide directly when you place an order, sign up for an account, contact a consultant, or subscribe to our newsletter. This includes:</p><ul><li>Name, email, shipping and billing address</li><li>Payment information (processed by our payment partners — we do not store full card numbers)</li><li>Phone number for order coordination and consultant follow-up</li><li>Optional account information (saved gear lists, preferences)</li></ul><p>We also collect technical information automatically when you visit the site (IP address, browser type, pages viewed) to operate the site and improve the user experience.</p>"),
            ("How We Use Your Information", "<p>We use the information we collect to:</p><ul><li>Process and ship your orders</li><li>Communicate about orders, returns, and warranty service</li><li>Provide consultant follow-up and account support</li><li>Send marketing emails (with your consent — you can unsubscribe at any time)</li><li>Operate, maintain, and improve the site</li><li>Comply with legal obligations</li></ul>"),
            ("Sharing of Information", "<p>We do not sell your personal information. We share information with service providers (shipping carriers, payment processors, email providers) only as needed to fulfill your orders and provide our services. These providers are contractually required to protect your information.</p><p>We may disclose information if required by law or to protect our rights, customers, or operations.</p>"),
            ("Cookies and Tracking", "<p>We use cookies and similar technologies to operate the site, remember preferences, analyze usage, and (with your consent) for marketing purposes. You can manage cookie preferences in your browser settings or via our cookie banner.</p>"),
            ("Your Rights and Choices", "<p>You can:</p><ul><li>Update your account information by signing in</li><li>Unsubscribe from marketing emails using the link in any email</li><li>Request a copy of the personal information we hold about you</li><li>Request deletion of your personal information (subject to legal retention requirements)</li></ul><p>To exercise these rights, contact us using the contact information below.</p>"),
            ("California, EU, and Other Jurisdictions", "<p>Residents of California (CCPA), the European Union (GDPR), and other jurisdictions with privacy laws have additional rights regarding their personal information. Contact us to exercise these rights.</p>"),
            ("Contact Us", "<p>Privacy questions or requests can be sent to <a href=\"mailto:privacy@vintageking.com\" style=\"color:var(--page-accent)\">privacy@vintageking.com</a> or via the Contact Us form. We respond to verified privacy requests within 30 days.</p>"),
            ("Changes to This Policy", "<p>We may update this policy from time to time. Material changes will be communicated via email to active customers. The current version is always available on this page.</p>"),
        ],
    )
    jsonld = '''{"@context":"https://schema.org","@type":"WebPage","name":"Privacy Policy","description":"Vintage King privacy policy. What information we collect, how we use it, and your rights regarding your personal data."}'''
    html = page_shell(
        title="Privacy Policy | Vintage King",
        meta="Vintage King privacy policy. Plain-language explanation of what data we collect, how we use it, and your rights to access, update, or delete your information.",
        breadcrumb="Privacy Policy",
        neighbors=NEIGHBORS_POLICY,
        jsonld=jsonld,
        body=body,
    )
    (ROOT / "privacy-policy.html").write_text(html)
    out.append("privacy-policy.html")

    return out


# ─────────────────────────────────────────────────────────────────────────────
# V2 VARIANTS — sibling pages with white hero photo slot, side-by-side
# 580x580 image placeholders, and bottom "Explore Vintage King" cross-link
# strip. Originals (v1) are not modified. Reachable only from navigator.html.
# ─────────────────────────────────────────────────────────────────────────────

import re

V2_EXTRA_CSS = """
.pg-hero-img-v2{background:#FFFFFF;border:1px solid rgba(26,26,24,0.08);border-radius:3px;min-height:380px;display:flex;align-items:center;justify-content:center;color:rgba(26,26,24,0.32);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;text-align:center;padding:20px;font-family:var(--font-body);font-weight:500}
.pg-photo-grid{display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-top:24px}
.pg-photo-slot{margin:0}
.pg-photo{background:var(--off-white);border:1px solid rgba(26,26,24,0.08);border-radius:3px;aspect-ratio:1/1;max-width:580px;display:flex;align-items:center;justify-content:center;color:rgba(26,26,24,0.32);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;font-family:var(--font-body);font-weight:500;text-align:center;padding:20px}
.pg-photo-slot figcaption{margin-top:14px;font-family:var(--font-body);font-size:13px;color:rgba(26,26,24,0.62);line-height:1.5}
.pg-explore{background:var(--off-white);padding:64px 0;border-top:1px solid rgba(26,26,24,0.07)}
.pg-explore-inner{max-width:1280px;margin:0 auto;padding:0 40px}
.pg-explore-h2{font-family:var(--font-display);font-size:28px;font-weight:700;color:var(--near-black);margin:0 0 28px}
.pg-explore-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.pg-explore-card{background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;text-decoration:none;display:block;transition:transform 0.18s,box-shadow 0.18s;border-radius:3px}
.pg-explore-card:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(26,26,24,0.08)}
.pg-explore-eyebrow{font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:var(--page-accent);margin-bottom:10px;font-family:var(--font-body)}
.pg-explore-title{font-family:var(--font-display);font-size:19px;font-weight:700;color:var(--near-black);margin-bottom:8px;line-height:1.3}
.pg-explore-body{font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6}
.pg-explore-cta{margin-top:16px;font-size:12px;font-weight:700;color:var(--page-accent);letter-spacing:0.06em}
@media(max-width:980px){.pg-photo-grid,.pg-explore-grid{grid-template-columns:1fr}}
"""


def dual_image_block(caption_left: str, caption_right: str) -> str:
    return f'''
<section class="pg-section pg-section-white">
  <div class="pg-wrap">
    <div class="pg-eyebrow">In context</div>
    <div class="pg-photo-grid">
      <figure class="pg-photo-slot">
        <div class="pg-photo">580 × 580<br>photo placeholder</div>
        <figcaption>{caption_left}</figcaption>
      </figure>
      <figure class="pg-photo-slot">
        <div class="pg-photo">580 × 580<br>photo placeholder</div>
        <figcaption>{caption_right}</figcaption>
      </figure>
    </div>
  </div>
</section>
'''


def explore_strip(cards: list) -> str:
    """cards = [(eyebrow, title, body, cta_label, href), ...]"""
    cards_html = "".join(
        f'''<a href="{href}" class="pg-explore-card">
  <div class="pg-explore-eyebrow">{eyebrow}</div>
  <div class="pg-explore-title">{title}</div>
  <div class="pg-explore-body">{body}</div>
  <div class="pg-explore-cta">{cta} →</div>
</a>'''
        for eyebrow, title, body, cta, href in cards
    )
    return f'''
<div class="pg-explore">
  <div class="pg-explore-inner">
    <div class="pg-explore-eyebrow" style="margin-bottom:10px">Explore Vintage King</div>
    <h2 class="pg-explore-h2">More from VK</h2>
    <div class="pg-explore-grid">{cards_html}</div>
  </div>
</div>
'''


# Per-page captions for the side-by-side photo block. None = skip (policy pages).
V2_CAPTIONS = {
    # HOF gear
    "neve-1081.html": ("Studio context · AIR Studios 8048 desk strip", "Hardware detail · Marinair transformer close-up"),
    "telefunken-ela-m-251.html": ("Studio context · Capitol vocal booth setup", "Hardware detail · CK12 capsule and 6072a tube"),
    "neumann-u47-fet.html": ("Studio context · drum room kick capture", "Hardware detail · headbasket and capsule cutaway"),
    "coles-4038.html": ("Studio context · Abbey Road overhead pair", "Hardware detail · ribbon motor and yoke"),
    "tab-telefunken-v72-v76.html": ("Studio context · vintage German broadcast rack", "Hardware detail · V72 / V76 module front and tubes"),
    "universal-audio-175b.html": ("Studio context · Capitol mastering rack", "Hardware detail · 6BC8 tube and meter face"),
    # Studios by VK
    "multi-room-recording-studios.html": ("Live room — multi-room install", "Control room — console and monitoring"),
    # 25 Years
    "25-years-of-pro-audio.html": ("Mike Nehra in the early VK shop, c.1993", "Modern VK Tech Shop service bench"),
    # Avid
    "avid-pro-tools-trade-in.html": ("Existing Pro Tools HDX system on the bench", "New MTRX install in commercial mix room"),
    "avid-s4-control-surface-configurations.html": ("S4 16-fader in commercial mix room", "Top-down channel detail"),
    "avid-s6-control-surface-configurations.html": ("S6 M40 32-fader in flagship room", "Top-down channel knob detail"),
    # UA
    "universal-audio-promotions.html": ("Apollo X8 rack install", "UAD plug-in workflow on screen"),
    "universal-audio-apollo-x.html": ("Apollo X16 in commercial studio rack", "Apollo Twin X on a project-studio desk"),
    # Campaigns
    "black-friday-microphone-deals.html": ("Featured tube mic on stand", "Mic pair lifestyle in tracking room"),
    "new-at-namm-microphones.html": ("New release on display at NAMM booth", "New mic in working studio"),
    "back-to-school.html": ("Student starter bundle on desk", "Dorm-room recording lifestyle shot"),
    # Policy → no big image
    "shipping-policy.html": None,
    "returns.html": None,
    "privacy-policy.html": None,
}


# Per-page explore strip cards (3 each).
_CARD_CONSULT = ("Expert Consulting", "Talk to an Audio Consultant",
                 "Our team has tracked sessions on legendary gear. Call, chat, or email — we know it from both sides of the glass.",
                 "Call 888.653.1184", "audio-consultants.html")
_CARD_HOF = ("Hall of Fame", "Legendary Gear and Rooms",
             "The consoles, microphones, and outboard that defined recording history — sourced and documented by VK.",
             "Explore", "hall-of-fame.html")
_CARD_TRADE = ("Trade Program", "Sell or Trade Your Gear",
               "Trade your existing gear toward your next purchase. Quotes within 24 hours.",
               "Get a quote", "trade-program.html")
_CARD_FINANCING = ("Financing", "VK Credit Card",
                   "0% financing up to 48 months on qualifying purchases through the VK Credit Card.",
                   "Apply", "vk-credit-card.html")
_CARD_WARRANTY = ("VK Warranty", "Coverage on Every Unit",
                  "Every new piece of gear ships with the VK Warranty. Optional extended coverage available.",
                  "Learn more", "warranty.html")
_CARD_25 = ("Heritage", "25 Years of Pro Audio",
            "How a Detroit-area shop became the world's largest curated pro-audio dealer.",
            "Read the story", "25-years-of-pro-audio.html")
_CARD_INSTALLS = ("Studio Installations", "Multi-Room Studio Builds",
                  "From single-room project studios to multi-room commercial facilities — design, install, commission.",
                  "See projects", "multi-room-recording-studios.html")
_CARD_CONSULTANTS_SHORT = ("Audio Consultants", "Free Pre-Sales Help",
                           "Compare gear, build chains, and get install advice from working engineers — free.",
                           "Email a consultant", "audio-consultants.html")

V2_EXPLORE = {
    # HOF gear → cross-link to siblings + consultants
    "neve-1081.html": [_CARD_HOF, _CARD_CONSULT, ("Hall of Fame", "Neve 1073 Buyer's Guide", "The 1073's three-band sibling — the most-cloned mic pre / EQ in pro audio history.", "Read", "neve-1073-guide-v2.html")],
    "telefunken-ela-m-251.html": [_CARD_HOF, _CARD_CONSULT, ("Hall of Fame", "Neumann U47", "The German tube condenser that defined vocal recording from 1947 onward.", "Read", "neumann-u47.html")],
    "neumann-u47-fet.html": [_CARD_HOF, _CARD_CONSULT, ("Hall of Fame", "Neumann U67", "The all-purpose tube workhorse — vocals, drums, broadcast.", "Read", "neumann-u67.html")],
    "coles-4038.html": [_CARD_HOF, _CARD_CONSULT, ("Hall of Fame", "Neumann U47", "The German tube condenser that defined vocal recording from 1947 onward.", "Read", "neumann-u47.html")],
    "tab-telefunken-v72-v76.html": [_CARD_HOF, _CARD_CONSULT, ("Hall of Fame", "Neve 1073", "The British alternative — Marinair-coupled mic pre and three-band EQ.", "Read", "neve-1073.html")],
    "universal-audio-175b.html": [_CARD_HOF, _CARD_CONSULT, ("Hall of Fame", "UREI 1176", "Putnam's later FET design — the most-imitated compressor ever made.", "Read", "urei-1176.html")],
    # Studios by VK
    "multi-room-recording-studios.html": [_CARD_CONSULT, _CARD_25, _CARD_FINANCING],
    # 25 Years
    "25-years-of-pro-audio.html": [_CARD_HOF, _CARD_INSTALLS, ("PLAYBACK Magazine", "Stories from the field", "VK's print magazine — engineer interviews, studio tours, gear histories.", "Read PLAYBACK", "playback.html")],
    # Avid
    "avid-pro-tools-trade-in.html": [_CARD_CONSULT, _CARD_INSTALLS, _CARD_FINANCING],
    "avid-s4-control-surface-configurations.html": [_CARD_CONSULT, _CARD_INSTALLS, ("Avid", "S6 Configuration Guide", "Compare S6 M40 16-, 32-, and 48-fader+ surfaces for flagship music and post rooms.", "Compare", "avid-s6-control-surface-configurations.html")],
    "avid-s6-control-surface-configurations.html": [_CARD_CONSULT, _CARD_INSTALLS, ("Avid", "S4 Configuration Guide", "Compare S4 8-, 16-, and 24-fader options — the more compact EUCON surface.", "Compare", "avid-s4-control-surface-configurations.html")],
    # UA
    "universal-audio-promotions.html": [_CARD_CONSULT, ("Universal Audio", "Apollo X Lineup", "Compare Apollo Twin X, X4, X6, X8, X8p, and X16 audio interfaces.", "Compare", "universal-audio-apollo-x.html"), _CARD_FINANCING],
    "universal-audio-apollo-x.html": [_CARD_CONSULT, ("Universal Audio", "Active UA Promotions", "Current Apollo bundles, UAD plug-in deals, and trade-up programs.", "See deals", "universal-audio-promotions.html"), _CARD_FINANCING],
    # Campaigns
    "black-friday-microphone-deals.html": [_CARD_CONSULT, _CARD_TRADE, _CARD_FINANCING],
    "new-at-namm-microphones.html": [_CARD_CONSULT, _CARD_TRADE, _CARD_FINANCING],
    "back-to-school.html": [_CARD_CONSULT, _CARD_TRADE, _CARD_FINANCING],
    # Policy
    "shipping-policy.html": [_CARD_WARRANTY, ("Returns", "30-Day Returns", "Most gear returns within 30 days, no restocking fee. See full policy.", "See policy", "returns.html"), _CARD_CONSULTANTS_SHORT],
    "returns.html": [_CARD_WARRANTY, ("Shipping", "Free Shipping over $99", "Free shipping in the lower 48. See rates and timing.", "See policy", "shipping-policy.html"), _CARD_CONSULTANTS_SHORT],
    "privacy-policy.html": [_CARD_WARRANTY, _CARD_CONSULTANTS_SHORT, ("Returns", "30-Day Returns", "Most gear returns within 30 days, no restocking fee.", "See policy", "returns.html")],
}


_HERO_PATTERNS = [
    r'<div class="pg-hero-img">[^<]*</div>',
    r'<div class="mr-hero-img">[^<]*</div>',
    r'<div class="y25-hero-img">[^<]*</div>',
]
_DUAL_INSERT_MARKERS = [
    '<section class="pg-dark">',
    '<section class="pg-section pg-section-cta">',
    '<section class="mr-dark">',
    '<section class="mr-section mr-section-cta"',
    '<section class="y25-dark">',
    '<section class="y25-cta">',
]


def to_v2(html: str, dual_captions, explore_cards: list) -> str:
    """Transform a v1 page into its v2 sibling."""
    # 1. Inject V2_EXTRA_CSS into the head, just before the standalone-patch <style>.
    html = html.replace(
        '<style id="vk-standalone-patch">',
        f'<style>{V2_EXTRA_CSS}</style>\n<style id="vk-standalone-patch">',
        1
    )

    # 2. Replace the first dark hero placeholder we find with the v2 white slot.
    for pat in _HERO_PATTERNS:
        new_html, n = re.subn(
            pat,
            '<div class="pg-hero-img-v2">Hero photo<br>720 × 540 recommended</div>',
            html, count=1
        )
        if n:
            html = new_html
            break

    # 3. Insert the side-by-side image block before the dark band or CTA band
    #    (whichever appears first). Skipped for policy pages (dual_captions=None).
    if dual_captions:
        block = dual_image_block(*dual_captions)
        positions = [(html.find(m), m) for m in _DUAL_INSERT_MARKERS if html.find(m) != -1]
        if positions:
            pos, _ = min(positions)
            html = html[:pos] + block + html[pos:]

    # 4. Insert the explore strip just before the footer.
    html = html.replace(
        '<footer class="site-footer">',
        explore_strip(explore_cards) + '<footer class="site-footer">',
        1
    )

    return html


# Manually-built v1 pages from the prior session (not in HOF_PAGES / build_all):
EXTRA_V2_TARGETS = ["multi-room-recording-studios.html", "25-years-of-pro-audio.html"]


def build_v2_all(v1_files: list) -> list:
    """Read each v1 file, transform, write -v2.html sibling."""
    targets = list(v1_files) + [f for f in EXTRA_V2_TARGETS if f not in v1_files]
    out = []
    for f in targets:
        if f not in V2_CAPTIONS:
            continue
        v1_path = ROOT / f
        if not v1_path.exists():
            continue
        v2_path = ROOT / f.replace(".html", "-v2.html")
        v1_html = v1_path.read_text()
        v2_html = to_v2(v1_html, V2_CAPTIONS[f], V2_EXPLORE[f])
        v2_path.write_text(v2_html)
        out.append(v2_path.name)
    return out


if __name__ == "__main__":
    files = build_all()
    v2_files = build_v2_all(files)
    print(f"Built {len(files)} v1 pages:")
    for f in files:
        print(f"  · {f}")
    print(f"\nBuilt {len(v2_files)} v2 pages:")
    for f in v2_files:
        print(f"  · {f}")
