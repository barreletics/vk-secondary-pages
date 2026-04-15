"""la-2a.html — Hall of Fame editorial guide to the Teletronix LA-2A."""
import re

SLUG  = "la-2a"
TITLE = "Teletronix LA-2A — The Voice of a Generation | Vintage King Audio"
META  = "The definitive guide to the Teletronix LA-2A leveling amplifier. History, the T4 optical cell, all 7 versions, the records it made, and every alternative at Vintage King. TECnology Hall of Fame, 2004."

IMG = {
    "hero":        "images/la-2a/la-2a-front.jpg",
    "rack_angled": "images/la-2a/la-2a-rack-angled.jpg",
}

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Teletronix LA-2A — The Voice of a Generation",
      "description": "The definitive guide to the Teletronix LA-2A leveling amplifier. History, the T4 optical cell, all 7 versions from Grayface to Universal Audio reissue, the records it made, and every alternative at Vintage King.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "Teletronix LA-2A Leveling Amplifier",
      "brand": {"@type": "Brand", "name": "Teletronix / Universal Audio"},
      "description": "Electro-optical tube compressor/limiter. T4 optical cell, program-dependent compression. TECnology Hall of Fame 2004.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "34.99",
        "highPrice": "4999",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What makes the LA-2A different from other compressors?",
          "acceptedAnswer": {"@type": "Answer", "text": "The LA-2A uses an electro-optical gain reduction element called the T4 cell — an electroluminescent panel paired with a cadmium-sulfide light-dependent resistor. The physical properties of the T4 make the compressor entirely program-dependent: attack, release, and ratio all respond to the nature of the incoming signal rather than fixed settings. No other compressor topology behaves exactly this way, which is why the LA-2A is irreplaceable even after 60 years."}
        },
        {
          "@type": "Question",
          "name": "What is the difference between the Grayface and Silverface LA-2A?",
          "acceptedAnswer": {"@type": "Answer", "text": "Grayface refers to the original Teletronix Engineering Company units (Rev 1, ~SN 001-572, 1962-1965) with a painted battleship-gray faceplate and red Teletronix logo. Silverface refers to all subsequent units (Babcock, Studio Electronics, and UREI versions, ~SN 573-1800, 1965-1969) with brushed aluminum faceplates. Both use the T4A opto cell on most units, though later Silverface units (UREI Rev 2C, from ~SN 1640) switched to the T4B cell and UTC A-10 input transformer."}
        },
        {
          "@type": "Question",
          "name": "What is the LA-2A best used for?",
          "acceptedAnswer": {"@type": "Answer", "text": "Vocals and bass guitar are the LA-2A's most celebrated applications. Its program-dependent optical compression preserves the impression of natural dynamics while handling extreme level variation — the singer sounds like they are controlling their performance, not being controlled by a compressor. It is also widely used on acoustic guitar, piano, room microphones, and as a gentle mix bus processor for 'warmth' rather than loudness."}
        },
        {
          "@type": "Question",
          "name": "Is the Universal Audio LA-2A reissue as good as the original?",
          "acceptedAnswer": {"@type": "Answer", "text": "The Universal Audio reissue uses a custom copy of the original UTC HA-100X input transformer and the T4B opto cell, and is hand-wired to original specifications. Most engineers and owners consider it sonically equivalent to the best-maintained Silverface originals. The UA unit also has the advantage of modern safety features, consistent quality control, and no aging components — unlike vintage units which vary widely depending on condition and service history."}
        }
      ]
    }
  ]
}
</script>
"""

INLINE_JS = """\
<script>
  (function() {
    var p = 'la-2a';
    var navTarget    = document.getElementById('nav-' + p);
    var footerTarget = document.getElementById('footer-' + p);
    var navTpl    = document.getElementById('nav-template');
    var footerTpl = document.getElementById('footer-template');
    if (navTarget && navTpl)        navTarget.innerHTML    = navTpl.innerHTML;
    if (footerTarget && footerTpl)  footerTarget.innerHTML = footerTpl.innerHTML;
  })();
  var __vkPageFiles = {
    home:'pages/home.html', category:'pages/category.html', product:'pages/product.html',
    faq:'pages/faq.html', deals:'pages/deals.html', sell:'pages/sell.html',
    studio:'pages/studio.html', techshop:'pages/techshop.html',
    'fin-page':'pages/financing.html', openbox:'pages/openbox.html'
  };
  function injectShared() {}
  function showPage(id) { var href = __vkPageFiles[id]; if (href) window.location.href = href; }
  function goToDeals() { window.location.href = 'pages/deals.html'; }
</script>
"""

CHROME = """\
<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <a href="hall-of-fame.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Hall of Fame</a>
  <span style="opacity:0.35">|</span>
  <a href="fairchild-660-670.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Fairchild 660/670</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Teletronix LA-2A</span>
</nav>
"""

PAGE_BODY = f"""\
<div id="la-2a" class="page active">
  <div id="nav-la-2a"></div>

  <style>
    /* ─── LA-2A HOF page ─────────────────────────────────────────────── */
    .la2-wrap  {{ max-width:860px;margin:0 auto;padding:0 32px }}
    .la2-wide  {{ max-width:1280px;margin:0 auto;padding:0 48px }}
    .la2-bread {{ max-width:1280px;margin:0 auto;padding:14px 48px;font-size:13px;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif }}
    .la2-bread a {{ color:rgba(26,26,24,0.42);text-decoration:none }}
    .la2-bread a:hover {{ color:#D4860A }}
    .la2-bread span {{ margin:0 8px }}

    .la2-body h2 {{ font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;margin:56px 0 16px;line-height:1.2 }}
    .la2-body h2:first-child {{ margin-top:0 }}
    .la2-body p  {{ font-size:16px;color:#3A3A38;line-height:1.82;margin-bottom:18px }}
    .la2-body strong {{ color:#1A1A18;font-weight:600 }}
    .la2-body ul {{ margin:14px 0 18px 22px;font-size:16px;color:#3A3A38;line-height:1.85 }}

    .la2-pull {{ border-left:3px solid #D4860A;padding:20px 28px;margin:44px 0;background:rgba(212,134,10,0.05) }}
    .la2-pull p {{ font-family:'Playfair Display',serif;font-size:22px;font-style:italic;line-height:1.5;color:#1A1A18;margin:0!important }}
    .la2-pull cite {{ display:block;margin-top:12px;font-size:12px;font-style:normal;color:#D4860A;letter-spacing:0.1em;text-transform:uppercase;font-weight:600 }}

    /* Stat bar */
    .la2-stats {{ background:var(--warm-white,#FDFCFB);border-top:1px solid rgba(26,26,24,0.1);border-bottom:1px solid rgba(26,26,24,0.1) }}
    .la2-si {{ max-width:1280px;margin:0 auto;padding:0 48px;display:flex;align-items:stretch }}
    .la2-stat {{ flex:1;padding:22px 0;text-align:center;border-right:1px solid rgba(26,26,24,0.08) }}
    .la2-stat:last-child {{ border-right:none }}
    .la2-sn {{ font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;display:block;line-height:1 }}
    .la2-sl {{ font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif;margin-top:5px }}

    /* Version timeline */
    .la2-timeline {{ position:relative;padding-left:0 }}
    .la2-tl-item {{ display:grid;grid-template-columns:120px 1fr;gap:24px;margin-bottom:36px;align-items:start }}
    .la2-tl-yr {{ font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;color:#D4860A;padding:4px 12px 4px 0;border-right:2px solid #D4860A;text-align:right;letter-spacing:0.06em }}
    .la2-tl-body h4 {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#1A1A18;margin:0 0 4px }}
    .la2-tl-body .la2-tl-tag {{ display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:0;margin-bottom:6px;color:#D4860A }}
    .la2-tl-body p {{ font-size:14px;color:#3A3A38;line-height:1.65;margin:0 }}

    /* Studio cards */
    .la2-studios {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px }}
    .la2-sc {{ background:#fff;overflow:hidden }}
    .la2-sc-img {{ height:320px;background-size:cover;background-position:center;transition:transform .5s }}
    .la2-sc:hover .la2-sc-img {{ transform:scale(1.03) }}
    .la2-sc-body {{ padding:24px 28px 28px }}
    .la2-sc-yr {{ font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;font-weight:600;margin-bottom:8px;font-family:'DM Sans',sans-serif }}
    .la2-sc-name {{ font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:5px;line-height:1.25 }}
    .la2-sc-loc {{ font-size:13px;color:rgba(26,26,24,0.45);margin-bottom:12px;font-family:'DM Sans',sans-serif }}
    .la2-sc-text {{ font-size:14px;color:#3A3A38;line-height:1.65 }}

    /* Records */
    .la2-records {{ display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(26,26,24,0.08) }}
    .la2-rec {{ background:#fff;padding:18px 24px;display:flex;align-items:baseline;gap:16px }}
    .la2-ry {{ font-size:13px;font-weight:600;color:#D4860A;letter-spacing:0.04em;min-width:38px;padding:2px 10px 2px 0;border-right:2px solid #D4860A;line-height:1;font-family:'DM Sans',sans-serif }}
    .la2-rt {{ font-size:14px;color:#1A1A18;font-weight:500 }}
    .la2-ra {{ font-size:13px;color:rgba(26,26,24,0.65);margin-top:2px }}

    /* T4 explainer */
    .la2-t4 {{ background:#1A1A18;padding:56px 64px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center }}
    .la2-t4 h3 {{ font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#FDFCFB;margin:0 0 16px }}
    .la2-t4 p {{ font-size:15px;color:rgba(253,252,251,0.7);line-height:1.75;margin-bottom:14px }}
    .la2-t4 p:last-child {{ margin-bottom:0 }}
    .la2-t4-diagram {{ background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);padding:32px;text-align:center }}

    /* Guide cards */
    .la2-guide {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;background:rgba(26,26,24,0.06) }}
    .la2-gc {{ background:#fff;padding:28px 24px;position:relative }}
    .la2-gc h4 {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#1A1A18;margin:0 0 6px }}
    .la2-gc-price {{ font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;color:#C0392B;margin-bottom:12px }}
    .la2-gc p {{ font-size:13px;color:#3A3A38;line-height:1.6;margin:0 0 14px }}
    .la2-gc a {{ font-size:13px;font-weight:600;color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.3) }}
    .la2-gc-tag {{ display:inline-block;font-size:10px;font-weight:700;padding:0 0 10px 0;letter-spacing:0.1em;text-transform:uppercase;border-radius:2px }}

    /* FAQ */
    .la2-faq {{ border-top:1px solid rgba(26,26,24,0.1) }}
    .la2-faq details {{ border-bottom:1px solid rgba(26,26,24,0.1) }}
    .la2-faq summary {{ font-size:16px;font-weight:600;color:#1A1A18;padding:22px 0;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-family:'DM Sans',sans-serif }}
    .la2-faq summary::after {{ content:'＋';font-size:18px;font-weight:300;color:rgba(26,26,24,0.35) }}
    .la2-faq details[open] summary::after {{ content:'－' }}
    .la2-faq details p {{ font-size:15px;color:#3A3A38;line-height:1.75;padding-bottom:24px;margin:0 }}

    /* Explore more */
    .la2-more {{ display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(26,26,24,0.06) }}
    .la2-mc {{ background:#fff;padding:28px 24px }}
    .la2-mc span {{ display:block;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:8px }}
    .la2-mc h4 {{ font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 10px;line-height:1.3 }}
    .la2-mc p {{ font-size:14px;color:rgba(26,26,24,0.55);line-height:1.65;margin:0 0 16px }}
    .la2-mc a {{ font-size:13px;font-weight:600;color:#C0392B;text-decoration:none }}

    /* Sticky bar */
    .la2-stick {{ position:fixed;bottom:0;left:0;right:0;background:#1A1A18;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;border-top:2px solid #C0392B }}
    .la2-stick-title {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB }}
    .la2-stick-sub {{ font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }}
    .la2-stick-cta {{ background:#C0392B;color:#fff;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em }}
    .la2-stick-ghost {{ color:rgba(255,255,255,0.6);font-size:13px;font-weight:500;text-decoration:none;padding:12px 0 }}

    @media(max-width:900px){{
      .la2-studios,.la2-records,.la2-guide,.la2-more {{ grid-template-columns:1fr }}
      .la2-si {{ flex-wrap:wrap }}
      .la2-stat {{ min-width:50% }}
      .la2-t4 {{ grid-template-columns:1fr;padding:36px 24px }}
      .la2-wide,.la2-bread {{ padding-left:20px;padding-right:20px }}
      .la2-wrap {{ padding:0 20px }}
      .la2-tl-item {{ grid-template-columns:90px 1fr }}
      .la2-stick {{ padding:12px 20px }}
    }}
  </style>

  <!-- HERO — full-bleed 50/50 split ────────────────────────────────── -->
  <section style="background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:620px;overflow:hidden">
    <div style="padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:16px">Pro Audio Hall of Fame</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:56px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 24px">Teletronix<br>LA-2A</h1>
      <p style="font-size:18px;color:#3A3A38;line-height:1.7;max-width:520px;margin:0 0 12px;font-family:'DM Sans',sans-serif">The most recorded vocals in history passed through an LA-2A. Alanis Morissette. Kurt Cobain. Shakira. Its secret: three controls, one T4 optical cell, and compression that sounds like the singer is doing it themselves.</p>
      <p style="font-size:15px;color:rgba(26,26,24,0.5);font-family:'DM Sans',sans-serif;margin:0 0 32px">Invented 1962. TECnology Hall of Fame 2004. Still the first compressor on every vocal chain.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="https://vintageking.com/teletronix-la-2a-optical-compressor-limiter" target="_blank" style="background:#C0392B;color:#fff;padding:14px 32px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em">Shop All LA-2A</a>
        <a href="#which-la2a" style="background:transparent;color:#1A1A18;border:1px solid rgba(26,26,24,0.35);padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;text-decoration:none">Which Version is Right for Me?</a>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;padding:32px;position:relative;background:#fff">
      <img src="{IMG['hero']}" alt="Teletronix LA-2A leveling amplifier front panel" style="width:100%;height:520px;object-fit:contain;display:block">
    </div>
  </section>

  <!-- BREADCRUMB -->
  <div class="la2-bread">
    <a href="https://vintageking.com">Vintage King</a><span>›</span>
    <a href="https://vintageking.com/pro-audio-hall-of-fame">Hall of Fame</a><span>›</span>
    Teletronix LA-2A
  </div>

  <!-- STAT BAR ──────────────────────────────────────────────────────────── -->
  <div class="la2-stats">
    <div class="la2-si">
      <div class="la2-stat">
        <span class="la2-sn" style="font-family:'DM Sans',sans-serif;font-size:26px">1962</span>
        <div class="la2-sl">First LA-2A Produced</div>
      </div>
      <div class="la2-stat">
        <span class="la2-sn">T4</span>
        <div class="la2-sl">Optical Cell Design</div>
      </div>
      <div class="la2-stat">
        <span class="la2-sn">10 ms</span>
        <div class="la2-sl">Average Attack</div>
      </div>
      <div class="la2-stat">
        <span class="la2-sn">3</span>
        <div class="la2-sl">Controls Total</div>
      </div>
      <div class="la2-stat">
        <span class="la2-sn">7</span>
        <div class="la2-sl">Major Versions</div>
      </div>
      <div class="la2-stat">
        <span class="la2-sn">2004</span>
        <div class="la2-sl">TECnology Hall of Fame</div>
      </div>
    </div>
  </div>

  <!-- INTRO ────────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="la2-wrap la2-body">
      <h2>Three Controls. No Equal.</h2>
      <p>The LA-2A has three controls: Peak Reduction, Gain, and a Limit/Compress switch. There is no attack knob, no release knob, no ratio dial. The compressor decides all of that itself — based on the music. This is the entire point. <strong>Every parameter is program-dependent</strong>, driven by the T4 electro-optical cell, which responds to the nature of the signal rather than fixed settings you dialed in. The result is compression that feels less like processing and more like a performer choosing to hold back.</p>
      <p>In sixty-plus years of compressor design, no one has fully replaced it. Dozens of very good engineers have built very good compressors inspired by the LA-2A. Most of them are worth owning. None of them are the same. The LA-2A remains the first compressor on virtually every professional vocal chain in the world — not because engineers are nostalgic, but because nothing else sounds like it on a voice.</p>

      <div class="la2-pull">
        <p>"LA-2As warm things up. They EQ all the warmth and low mids and bass. When you put bass and drums in them they get fatter and bigger. And unless you hit them way hard and make the tubes sizzle they don't really distort."</p>
        <cite>Jim Scott — Recording Engineer (Tom Petty, Red Hot Chili Peppers, Wilco)</cite>
      </div>

      <h2>From the Titan Missile Program to Abbey Road</h2>
      <p><strong>James F. Lawrence II</strong> was an electrical engineer at Caltech's Jet Propulsion Laboratory in the early 1950s, working on optical sensors for the Titan Missile Program. The physics of electroluminescent panels and photoresistors — light emitted in proportion to voltage, resistance dropping in proportion to light received — gave him an idea. That same physics could control the gain of an audio circuit in a way that no other component could.</p>
      <p>While engineering at radio station KMGM in Los Angeles, Lawrence built his first prototype to solve an everyday broadcast problem: manually riding gain for consistent levels between songs and announcements. He called it the Leveling Amplifier, and the first version, the LA-1, worked immediately. <strong>Gene Autry</strong>, the singing cowboy and one of America's most successful entertainers, was an early user. CBS and RCA adopted the next iteration, the LA-2, for their broadcast chains.</p>
      <p>Lawrence founded <strong>Teletronix Engineering Company</strong> in Pasadena, California in 1958 to build the design properly. By 1962, the third iteration — the first revision of the LA-2 — became the <strong>LA-2A</strong>. In 1965, Lawrence sold Teletronix to Babcock Electronics. In 1967, Babcock's broadcast division was acquired by Bill Putnam's Studio Electronics (later renamed <strong>UREI</strong>), bringing the LA-2A into the world's most important recording studios. In 1999, Putnam's sons re-founded Universal Audio and reissued the LA-2A in 2000 — still in production today, twenty-five years later.</p>
    </div>
  </section>

  <!-- T4 CELL EXPLAINER ────────────────────────────────────────────────── -->
  <div class="la2-t4">
    <div>
      <h3>The T4 Cell — Why the LA-2A Sounds Like Nothing Else</h3>
      <p>The T4 is an electroluminescent panel (a light source whose brightness varies with applied voltage) paired with a cadmium-sulfide photoresistor (a resistor whose resistance drops as light increases). Connect them in a sealed canister and you have an optical attenuator — one that has no memory of the previous signal, but physically responds to the current one in real time.</p>
      <p>The T4's electrical properties are inherently non-linear. The relationship between input voltage, light emission, and resistance change is not a straight line — it curves in a way that varies with frequency, level, and duration. This is why the LA-2A has no fixed attack, release, or ratio: the T4 sets all three simultaneously, and differently, for every signal passing through it.</p>
      <p>There is no software parameter called "program-dependent optical character." You cannot dial it in. The T4 cell either is or isn't in the signal chain. This is why the LA-2A continues to exist in hardware form in 2026, and why the hardware continues to matter.</p>
    </div>
    <div class="la2-t4-diagram">
      <svg width="260" height="220" viewBox="0 0 260 220" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="t4glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#D4860A" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#D4860A" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <!-- Canister outline -->
        <rect x="70" y="30" width="120" height="160" rx="12" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
        <!-- EL Panel glow -->
        <ellipse cx="130" cy="100" rx="38" ry="38" fill="url(#t4glow)"/>
        <ellipse cx="130" cy="100" rx="24" ry="24" fill="rgba(212,134,10,0.25)" stroke="rgba(212,134,10,0.5)" stroke-width="1"/>
        <text x="130" y="96" text-anchor="middle" fill="rgba(212,134,10,0.9)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1">EL PANEL</text>
        <text x="130" y="109" text-anchor="middle" fill="rgba(212,134,10,0.7)" font-size="8" font-family="DM Sans,sans-serif">light source</text>
        <!-- CdS photoresistor label -->
        <text x="130" y="155" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1">CdS PHOTORESISTOR</text>
        <text x="130" y="167" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="8" font-family="DM Sans,sans-serif">gain reduction element</text>
        <!-- T4 label -->
        <text x="130" y="210" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="11" font-family="DM Sans,sans-serif" letter-spacing="3">T4 CELL</text>
        <!-- Input signal arrow -->
        <line x1="20" y1="100" x2="68" y2="100" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" marker-end="url(#arr)"/>
        <text x="10" y="93" fill="rgba(255,255,255,0.35)" font-size="8" font-family="DM Sans,sans-serif">IN</text>
        <!-- Output signal arrow -->
        <line x1="192" y1="100" x2="240" y2="100" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" marker-end="url(#arr)"/>
        <text x="243" y="93" fill="rgba(255,255,255,0.35)" font-size="8" font-family="DM Sans,sans-serif">OUT</text>
        <defs>
          <marker id="arr" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto">
            <path d="M0,0 L0,6 L6,3 z" fill="rgba(255,255,255,0.25)"/>
          </marker>
        </defs>
      </svg>
      <p style="font-size:12px;color:rgba(255,255,255,0.3);margin:16px 0 0;letter-spacing:0.06em;text-transform:uppercase;font-family:'DM Sans',sans-serif">T4 electro-optical cell schematic</p>
    </div>
  </div>

  <!-- VERSION TIMELINE ─────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="la2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:12px">7 Versions, 60+ Years</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 40px">Every LA-2A Ever Made</h2>
      <div class="la2-timeline">
        <div class="la2-tl-item">
          <div class="la2-tl-yr">1962–1965</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Rev 1 — "Grayface"</div>
            <h4>Original Teletronix Engineering Co.</h4>
            <p>Painted battleship-gray faceplate, red Teletronix logo. Serial numbers 001–572 (approx.). Input transformer: UTC HA-100X. T4A opto cell. The first 10 units were hand-assembled by Lawrence himself. The Grayface is the most sought-after vintage LA-2A — rarely available and immediately bought when it surfaces.</p>
          </div>
        </div>
        <div class="la2-tl-item">
          <div class="la2-tl-yr">1965–1967</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Rev 2A — "Silverface" Babcock</div>
            <h4>Teletronix Division of Babcock Electronics</h4>
            <p>Brushed aluminum faceplate with red "Teletronix Div. of Babcock" logo. Lawrence sold the company in 1965. Serial numbers ~573–1000. UTC HA-100X input transformer, T4A cell. Rear panel compress/limit switch added from SN 573. Early units still used original gray faceplate from leftover stock.</p>
          </div>
        </div>
        <div class="la2-tl-item">
          <div class="la2-tl-yr">1967</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Rev 2B — Licensed Version</div>
            <h4>Studio Electronics Corporation (Bill Putnam)</h4>
            <p>Putnam's company licensed the Teletronix patent from Babcock. Serial numbers ~1001–1200. Cosmetically similar to Babcock units — brushed aluminum with "Teletronix" logo, rear metallic sticker noting Studio Electronics manufacture. UTC HA-100X transformer, T4A cell.</p>
          </div>
        </div>
        <div class="la2-tl-item">
          <div class="la2-tl-yr">1967–1969</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Rev 2C — UREI</div>
            <h4>United Recording Electronics Industries</h4>
            <p>Studio Electronics renamed UREI and acquired Babcock's broadcast division outright. Serial numbers ~1201–1800. <strong>Key change from SN ~1640:</strong> input transformer switched to UTC A-10, opto cell upgraded to T4B. Later units have black "UREI" logo on the brushed aluminum faceplate. T4B units are considered slightly smoother in release character than T4A.</p>
          </div>
        </div>
        <div class="la2-tl-item">
          <div class="la2-tl-yr">1979</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Reissue 1 — UREI Limited Edition</div>
            <h4>UREI Limited Edition (~300 units)</h4>
            <p>Demand never stopped. UREI responded with approximately 300 new units — brushed aluminum, T4B cell, UTC A-10 transformer. Added a safety switch that cuts power when the front panel is opened. SN range 101–400 (approx.). These "UREI Reissues" are collectible in their own right.</p>
          </div>
        </div>
        <div class="la2-tl-item">
          <div class="la2-tl-yr">1992</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Reissue 2 — Harman/JBL Limited Edition</div>
            <h4>Harman Electronics (~235 units)</h4>
            <p>UREI was acquired by Harman/JBL around 1985. In 1992, Harman assembled approximately 235 additional units from remaining available parts. SN range ~3000–3235. T4B cell, UTC A-10. The last vintage-parts production units.</p>
          </div>
        </div>
        <div class="la2-tl-item">
          <div class="la2-tl-yr">2000–Now</div>
          <div class="la2-tl-body">
            <div class="la2-tl-tag">Current — Universal Audio</div>
            <h4>Universal Audio Reissue (2000–Present)</h4>
            <p>Bill Putnam's sons re-established Universal Audio in 1999. Their LA-2A reissue was the second product released. Custom copy of the original UTC HA-100X transformer, T4B cell, hand-wired construction, XLR I/O on the rear panel. Compress/limit switch moved to front panel. The front panel is no longer hinged. This is the unit in production today at <strong>$4,999</strong> — and the reference-standard hardware for any working studio.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- STUDIO CARDS ─────────────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="la2-wide" style="margin-bottom:40px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:12px">The Rooms That Use One</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0;line-height:1.15">If Vocals Are Being Tracked,<br>There Is an LA-2A in the Room.</h2>
    </div>
    <div class="la2-studios">

      <!-- Card 1: Sound City -->
      <div class="la2-sc">
        <div class="la2-sc-img" style="background:linear-gradient(155deg,#111825 0%,#1c2535 50%,#0d1520 100%);display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 320" style="position:absolute;top:0;left:0;opacity:0.12" preserveAspectRatio="xMidYMid slice">
            <defs><radialGradient id="sc-g" cx="40%" cy="60%" r="55%"><stop offset="0%" stop-color="#4a8fd4" stop-opacity="0.5"/><stop offset="100%" stop-color="#111825" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="320" fill="url(#sc-g)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <circle cx="45" cy="45" r="38" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
              <text x="45" y="40" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">SOUND</text>
              <text x="45" y="55" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">CITY</text>
            </svg>
          </div>
        </div>
        <div class="la2-sc-body">
          <div class="la2-sc-yr">Est. 1969</div>
          <div class="la2-sc-name">Sound City Studios</div>
          <div class="la2-sc-loc">Van Nuys, California</div>
          <p class="la2-sc-text">Nirvana tracked the foundational sessions for <em>Nevermind</em> (1991) at Sound City on their Neve 8028 console. Kurt Cobain's vocals ran through an LA-2A — which is part of why the vocal takes on "Smells Like Teen Spirit," "Come as You Are," and "Lithium" hit so differently from anything recorded before them. Organic, present, controlled without sounding controlled. Engineers Mike Clink and Butch Vig both kept the LA-2A as a permanent part of their vocal toolkit.</p>
        </div>
      </div>

      <!-- Card 2: PatchWerk -->
      <div class="la2-sc">
        <div class="la2-sc-img" style="background:linear-gradient(150deg,#1a0f20 0%,#2a1535 50%,#140c1a 100%);display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 320" style="position:absolute;top:0;left:0;opacity:0.12" preserveAspectRatio="xMidYMid slice">
            <defs><radialGradient id="pw-g" cx="60%" cy="40%" r="55%"><stop offset="0%" stop-color="#a04dd4" stop-opacity="0.5"/><stop offset="100%" stop-color="#1a0f20" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="320" fill="url(#pw-g)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <rect x="8" y="8" width="74" height="74" fill="none" stroke="rgba(212,134,10,0.3)" stroke-width="1"/>
              <text x="45" y="40" text-anchor="middle" fill="rgba(212,134,10,0.6)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">PATCH</text>
              <text x="45" y="55" text-anchor="middle" fill="rgba(212,134,10,0.6)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">WERK</text>
            </svg>
          </div>
        </div>
        <div class="la2-sc-body">
          <div class="la2-sc-yr">Est. 1997</div>
          <div class="la2-sc-name">PatchWerk Recording Studios</div>
          <div class="la2-sc-loc">Atlanta, Georgia</div>
          <p class="la2-sc-text">PatchWerk is one of the premier recording facilities in the American South, with a client list spanning hip-hop, R&B, and pop. Their outboard racks run multiple LA-2As as permanent fixtures — the units photographed here are working studio tools, not display pieces. Lil Wayne, T.I., Ludacris, and Usher have all recorded vocals in rooms where the LA-2A is the first compressor in the chain. That is not coincidence.</p>
        </div>
      </div>

      <!-- Card 3: Conway Recording -->
      <div class="la2-sc">
        <div class="la2-sc-img" style="background:linear-gradient(155deg,#0f1a10 0%,#182615 50%,#0a1209 100%);display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 320" style="position:absolute;top:0;left:0;opacity:0.12" preserveAspectRatio="xMidYMid slice">
            <defs><radialGradient id="cw-g" cx="50%" cy="50%" r="55%"><stop offset="0%" stop-color="#4a8a4d" stop-opacity="0.4"/><stop offset="100%" stop-color="#0f1a10" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="320" fill="url(#cw-g)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <circle cx="45" cy="45" r="38" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
              <text x="45" y="40" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">CONWAY</text>
              <text x="45" y="55" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">RECORDING</text>
            </svg>
          </div>
        </div>
        <div class="la2-sc-body">
          <div class="la2-sc-yr">Est. 1972</div>
          <div class="la2-sc-name">Conway Recording Studios</div>
          <div class="la2-sc-loc">Hollywood, California</div>
          <p class="la2-sc-text">Conway has been Hollywood's go-to room for major label vocal production for over fifty years. Alanis Morissette, Red Hot Chili Peppers, Kendrick Lamar, and countless others have tracked vocals here. The studio's engineer lineage — including Jim Scott, who gave us the definitive quote on what LA-2As actually do to a signal — is as much a part of the room's reputation as the hardware. Multiple UA LA-2As live permanently in every control room.</p>
        </div>
      </div>

    </div>
  </section>

  <!-- RACK PHOTO ───────────────────────────────────────────────────────── -->
  <figure style="margin:0;background:#fff;padding:0">
    <img src="{IMG['rack_angled']}" alt="Teletronix LA-2A leveling amplifiers in outboard rack at PatchWerk Recording Studios, 2007" style="width:100%;height:480px;object-fit:cover;object-position:center 45%;display:block">
    <figcaption style="text-align:center;font-size:12px;color:rgba(26,26,24,0.44);letter-spacing:0.06em;text-transform:uppercase;padding:14px 0 16px;background:#fff;font-family:'DM Sans',sans-serif">Teletronix LA-2A units in outboard rack — PatchWerk Recording Studios, Atlanta, 2007. Working studio tools, not museum pieces.</figcaption>
  </figure>

  <!-- RECORDS ──────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="la2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:12px">The Discography</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 28px">Vocals You Have Heard Through an LA-2A</h2>
    </div>
    <div class="la2-wrap">
      <div class="la2-records">
        <div class="la2-rec"><div><div class="la2-ry">1967</div></div><div><div class="la2-rt">Early UREI studio sessions</div><div class="la2-ra">LA-2A enters major commercial studios via UREI</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">1991</div></div><div><div class="la2-rt">Nevermind — Nirvana</div><div class="la2-ra">Kurt Cobain vocals — Sound City, Van Nuys / Devonshire Studios</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">1995</div></div><div><div class="la2-rt">Jagged Little Pill — Alanis Morissette</div><div class="la2-ra">Glen Ballard production — 33 million copies sold</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">1999</div></div><div><div class="la2-rt">Californication — Red Hot Chili Peppers</div><div class="la2-ra">Rick Rubin + Jim Scott — Conway Recording Studios</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">2001</div></div><div><div class="la2-rt">Songs in A Minor — Alicia Keys</div><div class="la2-ra">Kerry "Krucial" Brothers production — LA-2A on piano and vocals</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">2006</div></div><div><div class="la2-rt">"Hips Don't Lie" — Shakira</div><div class="la2-ra">Serge Tsai mix — LA-2A on Shakira's lead vocal throughout</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">2007</div></div><div><div class="la2-rt">Icky Thump — The White Stripes</div><div class="la2-ra">Joe Chiccarelli — LA-2A driven into distortion on Jack White's vocals</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">2012</div></div><div><div class="la2-rt">good kid, m.A.A.d city — Kendrick Lamar</div><div class="la2-ra">Multiple sessions — LA-2A as primary vocal compressor</div></div></div>
        <div class="la2-rec"><div><div class="la2-ry">Ongoing</div></div><div><div class="la2-rt">Every major studio, every genre</div><div class="la2-ra">If there is a vocal session, there is an LA-2A</div></div></div>
      </div>
    </div>

    <div class="la2-wrap" style="margin-top:48px">
      <div class="la2-pull">
        <p>"It treats your signal so lovingly. It's inspiring to sing through psychologically. It responds especially well to the human voice in a way that inspires performance."</p>
        <cite>Bill Putnam Jr. — CEO, Universal Audio</cite>
      </div>
      <p style="font-size:15px;color:rgba(26,26,24,0.55);font-style:italic;margin-top:4px">Note: Joe Chiccarelli's use on Icky Thump is one of the most referenced examples of intentional compressor distortion in modern rock. He drove the LA-2A well into clipping on Jack White's vocals, using the tube saturation as an effect. The LA-2A was never designed for this — but it sounds remarkable.</p>
    </div>
  </section>

  <!-- WHICH LA-2A? ─────────────────────────────────────────────────────── -->
  <section id="which-la2a" style="background:#EDE8E2;padding:80px 0">
    <div class="la2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:12px">Buyer's Guide</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 8px">Which LA-2A Path Is Right for You?</h2>
      <p style="font-size:15px;color:rgba(26,26,24,0.55);font-family:'DM Sans',sans-serif;margin:0 0 32px">From $34.99 plug-in to $4,999 hardware reissue. Every option at Vintage King, honest assessment of each.</p>
    </div>
    <div class="la2-wide">
      <div class="la2-guide">

        <div class="la2-gc" style="background:#fff">
          <div class="la2-gc-tag" style="color:#D4860A">In the Box</div>
          <h4>Waves CLA-2A</h4>
          <div class="la2-gc-price">$34.99</div>
          <p>Chris Lord-Alge's personal LA-2A presets baked in. The CLA-2A is a genuine workhorse in-box compressor — used on major label mixes daily. Not the same as hardware, but it's the fastest way to get LA-2A compression behavior into any production at any price point.</p>
          <a href="https://vintageking.com/waves-cla-2a-native-elec-delivery" target="_blank">Shop Waves CLA-2A →</a>
        </div>

        <div class="la2-gc" style="background:#fff">
          <h4>Acme Opticom XLA-500</h4>
          <div class="la2-gc-price">$905</div>
          <p>500 Series optical compressor with a tube in the signal path. Compact format for home and project studios that want hardware optical compression without the full-size commitment. A genuine step up from plug-ins in terms of analog character.</p>
          <a href="https://vintageking.com/acme-audio-opticom-xla-500-series-tube-compressor-limiter" target="_blank">Shop XLA-500 →</a>
        </div>

        <div class="la2-gc" style="background:#fff">
          <h4>IGS Audio One LA</h4>
          <div class="la2-gc-price">$1,812</div>
          <p>A faithful LA-2A-inspired optical design at a price point accessible to serious home studios. The classic Rev A "Grayface" version is also available as the "576 Blue Stripe." Well-regarded for its T4-inspired cell and transformer quality at this price.</p>
          <a href="https://vintageking.com/igs-audio-one-leveling-amplifier-optical-compressor" target="_blank">Shop IGS One LA →</a>
        </div>

        <div class="la2-gc" style="background:#fff">
          <h4>Acme Opticom XLA-3 MKIII</h4>
          <div class="la2-gc-price">$2,599</div>
          <p>Optical limiter combining three separate compression curves into one unit. Combines LA-2A-inspired warmth with more versatile control options. Well-suited for tracking and mixing rooms that want optical compression character without restricting themselves to one compression topology.</p>
          <a href="https://vintageking.com/acme-audio-opticom-xla-3-mkiii-tube-optical-limiter" target="_blank">Shop XLA-3 MKIII →</a>
        </div>

        <div class="la2-gc" style="background:#fff">
          <div class="la2-gc-tag" style="color:#1A1A18">Pro Studio</div>
          <h4>Tube-Tech CL 1B</h4>
          <div class="la2-gc-price">$4,725</div>
          <p>The CL 1B has become its own modern classic — used on hit records across hip-hop, pop, and R&B every single week. Two time controllers, a dedicated gain reduction element, and a tube push-pull amplifier. More controls than the LA-2A with a similar optical warmth. For studios that want to live in the LA-2A's neighborhood with more flexibility.</p>
          <a href="https://vintageking.com/tube-tech-cl1b" target="_blank">Shop Tube-Tech CL 1B →</a>
        </div>

        <div class="la2-gc" style="background:#fff">
          <div class="la2-gc-tag" style="color:#D4860A">Reference</div>
          <h4>Universal Audio LA-2A</h4>
          <div class="la2-gc-price">$4,999</div>
          <p>The reissue. Custom copy of the original UTC HA-100X transformer. T4B opto cell. Hand-wired. Built to original specifications by the company founded by the man who owned the Teletronix patent. This is the standard against which every other LA-2A alternative is measured. If you are building a serious room and want the real thing, this is it.</p>
          <a href="https://vintageking.com/universal-audio-la-2a" target="_blank">Shop UA LA-2A →</a>
        </div>

      </div>
    </div>
  </section>

  <!-- FAQ ──────────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="la2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:12px">Common Questions</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 36px">LA-2A FAQ</h2>
      <div class="la2-faq">
        <details>
          <summary>What makes the LA-2A different from every other compressor?</summary>
          <p>The T4 electro-optical cell. The relationship between input level, light emission, and photoresistor behavior is physically non-linear and cannot be precisely replicated in software or by other hardware topologies. The LA-2A's attack, release, and ratio all change simultaneously based on the incoming signal — frequency, level, duration, and transient character all influence how the T4 responds. You are not setting parameters; the compressor is reading the music and responding to it. This is why engineers describe it as sounding "organic" or like the performer is doing it themselves: because in a very real sense, the compression curve is shaped by the music rather than imposed on it.</p>
        </details>
        <details>
          <summary>What is the difference between the Grayface and Silverface LA-2A?</summary>
          <p>Grayface = original Teletronix Engineering Company units, serial numbers 001–572 (approx.), 1962–1965, painted battleship-gray faceplate, red Teletronix logo, UTC HA-100X transformer, T4A cell. Silverface = all subsequent units from Babcock, Studio Electronics, and UREI, serial numbers ~573–1800, 1965–1969, brushed aluminum faceplate. Both the T4A and later T4B cells are excellent. The primary variable with any vintage LA-2A is the condition and service history — a well-maintained Silverface often outperforms a neglected Grayface. The Grayface commands a collector premium above its sonic premium.</p>
        </details>
        <details>
          <summary>What does the Limit / Compress switch actually do?</summary>
          <p>Switching from Compress to Limit changes the compression ratio. In Compress mode the ratio is approximately 3:1, providing gentle, musical gain reduction. In Limit mode the ratio increases significantly — closer to 10:1 or more — for more aggressive gain control. Both modes remain program-dependent via the T4 cell, so neither sounds "hard" in the way a high-ratio VCA compressor does. The Limit setting is useful for vocals with very wide dynamic range (live recordings, aggressive singers) or for bass guitar where you need more control over peaks.</p>
        </details>
        <details>
          <summary>Is the Universal Audio reissue the same as a vintage original?</summary>
          <p>Sonically, very close. The UA unit uses a custom copy of the original UTC HA-100X input transformer and the T4B opto cell — the same spec as the best-condition Silverface UREI units. The vast majority of blind listening tests between a well-maintained vintage unit and the UA reissue show no consistent preference. The advantages of the UA reissue over a vintage original are practical: consistent manufacturing quality, no aging components, modern XLR connections, safety features, and a warranty. The advantages of a vintage original are primarily collector/historical value and the possibility of finding a T4A cell unit in the Grayface/early Silverface range — which some engineers prefer for its slightly different release character.</p>
        </details>
        <details>
          <summary>What is the LA-2A best used for?</summary>
          <p>Lead vocals. That is the canonical answer, and it is correct. The LA-2A's program-dependent character is almost uniquely suited to the human voice — it rides the dynamics of a performance in a way that preserves the singer's expression while eliminating the level peaks that would otherwise require constant manual gain riding. Beyond vocals: bass guitar (classic application — fatter, warmer, more even), acoustic guitar, piano (adds presence and focus), room microphones, and as a gentle parallel compressor on drum buses. It works particularly poorly on transient-heavy drum overhead or bus applications where a fast, defined attack is needed — that is the 1176's job.</p>
        </details>
        <details>
          <summary>Why does the LA-2A only have three controls?</summary>
          <p>Because the T4 cell handles everything the other controls would set. Attack, release, and ratio are all determined by the physics of the electro-optical circuit — they are not parameters, they are properties. Peak Reduction sets how hard the circuit drives the T4 (and therefore how much compression occurs). Gain is makeup gain after the compression. The Limit/Compress switch gives you two different compression curves. That is genuinely all that is needed, because the T4 adapts to the rest. Adding more controls would mean overriding the circuit's natural character — which is exactly what engineers are trying to avoid.</p>
        </details>
      </div>
    </div>
  </section>

  <!-- EXPLORE MORE ─────────────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="la2-wide" style="margin-bottom:36px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:12px">More From Vintage King</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;margin:0">Continue Exploring</h2>
    </div>
    <div class="la2-wide">
      <div class="la2-more">
        <div class="la2-mc">
          <span>Hall of Fame</span>
          <h4>Fairchild 660/670 — The Holy Grail of Compression</h4>
          <p>The most imitated compressor ever built. Fewer than 1,000 stereo units made. Every version available at VK.</p>
          <a href="fairchild-660-670.html">Read the Guide →</a>
        </div>
        <div class="la2-mc">
          <span>Hall of Fame</span>
          <h4>Neve 1073 — The Definitive Guide</h4>
          <p>How the 1073 mic preamp became the most cloned circuit in recording history. Three iconic studios, full specs, every version.</p>
          <a href="neve-1073-guide-v2.html">Read the Guide →</a>
        </div>
        <div class="la2-mc">
          <span>Audio Consulting</span>
          <h4>Talk to a VK Expert</h4>
          <p>Not sure which LA-2A path makes sense for your room? Our consultants have owned and heard every version discussed here.</p>
          <a href="audio-consultants.html">Meet the Team →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA ──────────────────────────────────────────────────────────────── -->
  <section style="background:#EDE8E2;padding:80px 48px">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;font-family:'DM Sans',sans-serif;margin-bottom:16px">Vintage King Audio</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 20px;line-height:1.2">Ready to Put an LA-2A on Your Vocals?</h2>
      <p style="font-size:16px;color:#3A3A38;line-height:1.7;margin:0 0 36px">From plug-ins to vintage originals, our team knows every version of the LA-2A on the market. We can help you find the right unit for your room, your budget, and the sound you are after.</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a href="https://vintageking.com/teletronix-la-2a-optical-compressor-limiter" target="_blank" style="background:#C0392B;color:#fff;padding:16px 36px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;text-decoration:none;letter-spacing:0.04em">Shop All LA-2A</a>
        <a href="audio-consultants.html" style="background:transparent;color:#1A1A18;border:1px solid rgba(26,26,24,0.35);padding:16px 28px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;text-decoration:none">Talk to an Expert</a>
      </div>
    </div>
  </section>

  <!-- STICKY BAR ───────────────────────────────────────────────────────── -->
  <div class="la2-stick">
    <div>
      <div class="la2-stick-title">Teletronix LA-2A</div>
      <div class="la2-stick-sub">Hardware from $905 · UA reissue $4,999 · Plug-ins from $34.99 · Vintage originals by request</div>
    </div>
    <div style="display:flex;gap:12px;align-items:center">
      <a href="https://vintageking.com/teletronix-la-2a-optical-compressor-limiter" target="_blank" class="la2-stick-cta">Shop at Vintage King</a>
      <a href="audio-consultants.html" class="la2-stick-ghost">Ask an Expert</a>
    </div>
  </div>
  <div style="height:68px"></div>

</div>
"""


def build(src_html, head_css, nav_tpl, foot_tpl, js_nav):
    head = re.sub(
        r"<title>.*?</title>",
        f"<title>{TITLE}</title>",
        head_css, count=1, flags=re.S
    )
    head += f'  <meta name="description" content="{META}">\n'
    head += '  <style id="vk-standalone-patch">.page{{display:block!important}}</style>\n'

    return (
        head + "\n</head>\n<body>\n"
        + CHROME + nav_tpl + foot_tpl
        + JSON_LD + PAGE_BODY
        + js_nav + INLINE_JS
        + "</body>\n</html>\n"
    )
