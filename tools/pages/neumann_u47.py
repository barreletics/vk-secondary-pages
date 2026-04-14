"""neumann-u47.html — Hall of Fame editorial guide to the Neumann U 47."""
import re

SLUG  = "neumann-u47"
TITLE = "Neumann U 47 — The Undisputed King of Vocal Microphones | Vintage King Audio"
META  = "The definitive guide to the Neumann U 47 and U 48. History, the VF14 tube, the M7 capsule, every version, and every alternative at Vintage King. From Frank Sinatra to The Beatles to Adele."

IMG = {
    "hero":  "images/u47/u47-1949.jpg",
    "tube":  "images/u47/u47-tube.jpg",
}

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Neumann U 47 — The Undisputed King of Vocal Microphones",
      "description": "The definitive guide to the Neumann U 47 and U 48 — history, the VF14 tube, the M7 capsule, every variant, the studios and records that defined them, and every alternative at Vintage King.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "Neumann U 47 Large Diaphragm Tube Condenser Microphone",
      "brand": {"@type": "Brand", "name": "Neumann"},
      "description": "Large diaphragm tube condenser microphone. M7/K47 capsule, VF14 tube, custom transformer. First produced 1949, discontinued 1963. Industry standard vocal microphone.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "439",
        "highPrice": "22495",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between the Neumann U 47 and U 48?",
          "acceptedAnswer": {"@type": "Answer", "text": "The U 47 offers cardioid and omnidirectional polar patterns. The U 48, released in 1957, offers cardioid and figure-eight patterns. In cardioid mode both are nearly identical. The U 48 figure-eight mode has a slightly higher noise floor due to the split polarization voltage (52.5V instead of 60V). George Martin famously sent Abbey Road's U 47s back to Neumann in Berlin to be converted to figure-eight — those units became the U 47/48 hybrid designation."}
        },
        {
          "@type": "Question",
          "name": "Why did the Neumann U 47 go out of production?",
          "acceptedAnswer": {"@type": "Answer", "text": "The VF14 tube — a pentode in a steel housing, made only by Telefunken — was discontinued after 1958. Of the 27,548 VF14 tubes manufactured between 1946 and 1958, only about a third passed Neumann's stringent noise tests and were stamped with a white 'M' for microphone use. Approximately 6,700 went into U 47 and U 48 units. When Neumann's final stock of VF14 tubes ran out in 1963, production of the U 47 ceased. No equivalent substitute tube was ever manufactured."}
        },
        {
          "@type": "Question",
          "name": "What is the M7 capsule in the Neumann U 47?",
          "acceptedAnswer": {"@type": "Answer", "text": "The M7 is a dual-diaphragm capsule originally designed in 1932 for the CMV 3 bottle microphone. Early U 47s used PVC diaphragms at 12 microns thick with evaporated gold, mounted on brass backplates with 90 precision-drilled holes per side. By 1960, PVC was replaced with Mylar in the updated K47/K49 capsule. The M7 design is still manufactured today by Microtech Gefell in Germany."}
        },
        {
          "@type": "Question",
          "name": "How much does a vintage Neumann U 47 cost?",
          "acceptedAnswer": {"@type": "Answer", "text": "Vintage U 47 units in working condition typically sell between $18,000 and $35,000 depending on version, capsule condition, transformer revision, and service history. U 48s can sell for similar prices. Vintage King maintains a waitlist and actively sources original units — contact our team for current availability."}
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
    var p = 'neumann-u47';
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
  function showPage(id) {{ var href = __vkPageFiles[id]; if (href) window.location.href = href; }}
  function goToDeals() {{ window.location.href = 'pages/deals.html'; }}
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
  <a href="la-2a.html" style="color:rgba(255,255,255,0.55);text-decoration:none">LA-2A</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Neumann U 47</span>
</nav>
"""

PAGE_BODY = f"""\
<div id="neumann-u47" class="page active">
  <div id="nav-neumann-u47"></div>

  <style>
    /* ─── Neumann U47 HOF page ───────────────────────────────────────── */
    .u47-wrap {{ max-width:860px;margin:0 auto;padding:0 32px }}
    .u47-wide {{ max-width:1280px;margin:0 auto;padding:0 48px }}
    .u47-bread {{ max-width:1280px;margin:0 auto;padding:14px 48px;font-size:13px;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif }}
    .u47-bread a {{ color:rgba(26,26,24,0.42);text-decoration:none }}
    .u47-bread a:hover {{ color:#D4860A }}
    .u47-bread span {{ margin:0 8px }}

    .u47-body h2 {{ font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;margin:56px 0 16px;line-height:1.2 }}
    .u47-body h2:first-child {{ margin-top:0 }}
    .u47-body p {{ font-size:16px;color:#3A3A38;line-height:1.82;margin-bottom:18px }}
    .u47-body strong {{ color:#1A1A18;font-weight:600 }}
    .u47-body ul {{ margin:14px 0 18px 22px;font-size:16px;color:#3A3A38;line-height:1.85 }}

    .u47-pull {{ border-left:3px solid #D4860A;padding:20px 28px;margin:44px 0;background:rgba(212,134,10,0.05) }}
    .u47-pull p {{ font-family:'Playfair Display',serif;font-size:22px;font-style:italic;line-height:1.5;color:#1A1A18;margin:0!important }}
    .u47-pull cite {{ display:block;margin-top:12px;font-size:12px;font-style:normal;color:#D4860A;letter-spacing:0.1em;text-transform:uppercase;font-weight:600 }}

    /* Stat bar */
    .u47-stats {{ background:var(--warm-white,#FDFCFB);border-top:1px solid rgba(26,26,24,0.1);border-bottom:1px solid rgba(26,26,24,0.1) }}
    .u47-si {{ max-width:1280px;margin:0 auto;padding:0 48px;display:flex }}
    .u47-stat {{ flex:1;padding:22px 0;text-align:center;border-right:1px solid rgba(26,26,24,0.08) }}
    .u47-stat:last-child {{ border-right:none }}
    .u47-sn {{ font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;display:block;line-height:1 }}
    .u47-sl {{ font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif;margin-top:5px }}

    /* Anatomy callout — dark section */
    .u47-anatomy {{ background:#1A1A18;padding:72px 0 }}
    .u47-anatomy-inner {{ max-width:1280px;margin:0 auto;padding:0 48px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center }}
    .u47-anatomy h3 {{ font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#FDFCFB;margin:0 0 24px }}
    .u47-anatomy-item {{ margin-bottom:28px }}
    .u47-anatomy-item h4 {{ font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin:0 0 6px }}
    .u47-anatomy-item p {{ font-size:15px;color:rgba(253,252,251,0.65);line-height:1.7;margin:0 }}

    /* Variants timeline */
    .u47-tl {{ border-left:2px solid rgba(26,26,24,0.1);padding-left:32px;margin-top:16px }}
    .u47-tl-item {{ position:relative;margin-bottom:36px }}
    .u47-tl-item::before {{ content:'';position:absolute;left:-40px;top:6px;width:10px;height:10px;border-radius:50%;background:#D4860A;border:2px solid #D4860A }}
    .u47-tl-yr {{ font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;font-family:'DM Sans',sans-serif }}
    .u47-tl-item h4 {{ font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 6px }}
    .u47-tl-item p {{ font-size:14px;color:#3A3A38;line-height:1.65;margin:0 }}

    /* Studio cards */
    .u47-studios {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px }}
    .u47-sc {{ background:#fff;overflow:hidden }}
    .u47-sc-img {{ height:320px;background-size:cover;background-position:center;transition:transform .5s }}
    .u47-sc:hover .u47-sc-img {{ transform:scale(1.03) }}
    .u47-sc-body {{ padding:24px 28px 28px }}
    .u47-sc-yr {{ font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;font-weight:600;margin-bottom:8px;font-family:'DM Sans',sans-serif }}
    .u47-sc-name {{ font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:5px;line-height:1.25 }}
    .u47-sc-loc {{ font-size:13px;color:rgba(26,26,24,0.45);margin-bottom:12px;font-family:'DM Sans',sans-serif }}
    .u47-sc-text {{ font-size:14px;color:#3A3A38;line-height:1.65 }}

    /* Records */
    .u47-records {{ display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(26,26,24,0.08) }}
    .u47-rec {{ background:#fff;padding:18px 24px;display:flex;align-items:baseline;gap:16px }}
    .u47-ry {{ font-size:13px;font-weight:600;color:#D4860A;letter-spacing:0.04em;min-width:38px;padding:2px 10px 2px 0;border-right:2px solid #D4860A;line-height:1;font-family:'DM Sans',sans-serif }}
    .u47-rt {{ font-size:14px;color:#1A1A18;font-weight:500 }}
    .u47-ra {{ font-size:13px;color:rgba(26,26,24,0.48);margin-top:2px }}

    /* Buyer guide */
    .u47-guide {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;background:rgba(26,26,24,0.06) }}
    .u47-gc {{ background:#fff;padding:28px 24px;position:relative }}
    .u47-gc h4 {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#1A1A18;margin:0 0 6px }}
    .u47-gc-price {{ font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;color:#C0392B;margin-bottom:12px }}
    .u47-gc p {{ font-size:13px;color:#3A3A38;line-height:1.6;margin:0 0 14px }}
    .u47-gc a {{ font-size:13px;font-weight:600;color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.3) }}
    .u47-gc-tag {{ position:absolute;top:-1px;right:16px;font-size:10px;font-weight:700;padding:3px 9px;letter-spacing:0.08em;text-transform:uppercase;color:#fff }}

    /* FAQ */
    .u47-faq {{ border-top:1px solid rgba(26,26,24,0.1) }}
    .u47-faq details {{ border-bottom:1px solid rgba(26,26,24,0.1) }}
    .u47-faq summary {{ font-size:16px;font-weight:600;color:#1A1A18;padding:22px 0;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-family:'DM Sans',sans-serif }}
    .u47-faq summary::after {{ content:'＋';font-size:18px;font-weight:300;color:rgba(26,26,24,0.35) }}
    .u47-faq details[open] summary::after {{ content:'－' }}
    .u47-faq details p {{ font-size:15px;color:#3A3A38;line-height:1.75;padding-bottom:24px;margin:0 }}

    /* Explore more */
    .u47-more {{ display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(26,26,24,0.06) }}
    .u47-mc {{ background:#fff;padding:28px 24px }}
    .u47-mc span {{ display:block;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:8px }}
    .u47-mc h4 {{ font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 10px;line-height:1.3 }}
    .u47-mc p {{ font-size:14px;color:rgba(26,26,24,0.55);line-height:1.65;margin:0 0 16px }}
    .u47-mc a {{ font-size:13px;font-weight:600;color:#C0392B;text-decoration:none }}

    /* Sticky bar */
    .u47-stick {{ position:fixed;bottom:0;left:0;right:0;background:#1A1A18;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;border-top:2px solid #C0392B }}
    .u47-stick-title {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB }}
    .u47-stick-sub {{ font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }}
    .u47-stick-cta {{ background:#C0392B;color:#fff;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em }}
    .u47-stick-ghost {{ color:rgba(255,255,255,0.6);font-size:13px;font-weight:500;text-decoration:none;padding:12px 0 }}

    @media(max-width:900px){{
      .u47-hero-split {{ grid-template-columns:1fr!important;min-height:auto!important }}
      .u47-studios,.u47-records,.u47-guide,.u47-more {{ grid-template-columns:1fr }}
      .u47-si {{ flex-wrap:wrap }}
      .u47-stat {{ min-width:50% }}
      .u47-anatomy-inner {{ grid-template-columns:1fr;padding:0 24px }}
      .u47-wide,.u47-bread {{ padding-left:20px;padding-right:20px }}
      .u47-wrap {{ padding:0 20px }}
      .u47-stick {{ padding:12px 20px }}
    }}
  </style>

  <!-- HERO — split full-bleed ────────────────────────────────────────── -->
  <section class="u47-hero-split" style="background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:580px;overflow:hidden">
    <div style="padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:16px">Pro Audio Hall of Fame</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:56px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 24px">Neumann<br>U 47</h1>
      <p style="font-size:18px;color:#3A3A38;line-height:1.7;max-width:520px;margin:0 0 12px;font-family:'DM Sans',sans-serif">Frank Sinatra called it "Telly" and refused to record without one. The Beatles used it from their first session at Abbey Road. Ella Fitzgerald. Adele. Every voice that defined an era passed through a U 47.</p>
      <p style="font-size:15px;color:rgba(26,26,24,0.5);font-family:'DM Sans',sans-serif;margin:0 0 32px">First produced 1949. Discontinued 1963. Irreplaceable ever since.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="https://vintageking.com/neumann-u47-u48-microphone" target="_blank" style="background:#C0392B;color:#fff;padding:14px 32px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em">Shop All U 47</a>
        <a href="#which-u47" style="background:transparent;color:#1A1A18;border:1px solid rgba(26,26,24,0.35);padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;text-decoration:none">Which Version is Right for Me?</a>
      </div>
    </div>
    <div style="position:relative">
      <img src="{IMG['hero']}" alt="Neumann U 47 large diaphragm tube condenser microphone, 1949" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;display:block">
      <div style="position:absolute;bottom:14px;right:16px;font-size:10px;letter-spacing:0.08em;text-transform:uppercase;color:rgba(255,255,255,0.6);font-family:'DM Sans',sans-serif">Neumann U 47 — Original Production, 1949</div>
    </div>
  </section>

  <!-- BREADCRUMB -->
  <div class="u47-bread">
    <a href="https://vintageking.com">Vintage King</a><span>›</span>
    <a href="https://vintageking.com/pro-audio-hall-of-fame">Hall of Fame</a><span>›</span>
    Neumann U 47
  </div>

  <!-- STAT BAR ──────────────────────────────────────────────────────────── -->
  <div class="u47-stats">
    <div class="u47-si">
      <div class="u47-stat">
        <span class="u47-sn" style="font-family:'DM Sans',sans-serif;font-size:26px">1949</span>
        <div class="u47-sl">Production Began</div>
      </div>
      <div class="u47-stat">
        <span class="u47-sn">VF14</span>
        <div class="u47-sl">Tube (Telefunken)</div>
      </div>
      <div class="u47-stat">
        <span class="u47-sn">M7</span>
        <div class="u47-sl">Original Capsule</div>
      </div>
      <div class="u47-stat">
        <span class="u47-sn">6,700</span>
        <div class="u47-sl">Units Made (Est.)</div>
      </div>
      <div class="u47-stat">
        <span class="u47-sn">1963</span>
        <div class="u47-sl">Final Year of Production</div>
      </div>
      <div class="u47-stat">
        <span class="u47-sn">$20K+</span>
        <div class="u47-sl">Vintage Market Value</div>
      </div>
    </div>
  </div>

  <!-- INTRO ────────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="u47-wrap u47-body">
      <h2>The First. The Last. The Only.</h2>
      <p>The Neumann U 47 was the first microphone produced by Georg Neumann GmbH in post-war Berlin. It debuted at the Berlin Radio Show in 1947 — the year encoded in its model number — though production delays pushed manufacture to 1949. In the years that followed, it became <strong>the industry standard vocal microphone</strong>, not because Neumann marketed it that way, but because engineers in studios across the world reached for it first and never stopped.</p>
      <p>Frank Sinatra nicknamed it "Telly" — short for Telefunken, which distributed the microphone under a licensing arrangement. He maintained a consistent distance of about one foot from the capsule to create his signature intimate, close-in sound, and he refused to record without it. Capitol Studios built sessions around his relationship with the U 47. The Beatles used U 47s and U 48s from their first recording at Abbey Road in 1962. Rudy Van Gelder received the second U 47 to arrive in the United States, and it contributed to the sound of hundreds of Blue Note Records masterpieces.</p>
      <p>Production ended in 1963 — not a business decision, but a physics problem. The VF14 tube that gave the U 47 its character was out of stock. <strong>No equivalent was ever manufactured.</strong> The microphones that exist today are the only ones that will ever exist. That is why a working, properly capsulled U 47 commands $20,000 or more, and why the waiting list at Vintage King for a vintage original is always active.</p>

      <div class="u47-pull">
        <p>"The U 47, in my opinion, is the number one vocal mic of choice if I only had one to choose from. Not to mention they're outstanding for one, two and three mic drum recording techniques and on nearly any instrument."</p>
        <cite>Mike Nehra — Co-Founder, Vintage King Audio</cite>
      </div>
    </div>
  </section>

  <!-- ANATOMY — dark section with tube photo ───────────────────────────── -->
  <div class="u47-anatomy">
    <div class="u47-anatomy-inner">
      <div>
        <h3>What Makes the U 47 Sound Like the U 47</h3>
        <div class="u47-anatomy-item">
          <h4>The VF14 Tube</h4>
          <p>A pentode in a steel housing, made only by Telefunken in Berlin and Ulm. Of the 27,548 VF14 tubes produced between 1946 and 1958, approximately one third passed Neumann's stringent noise and performance tests. Those received a white "M" stamp — <em>mikrofon</em> — and about 6,700 of them went into U 47 and U 48 units. No equivalent tube was ever manufactured before or after. When Neumann's final stock ran out in 1963, the U 47 died with it.</p>
        </div>
        <div class="u47-anatomy-item">
          <h4>The M7 Capsule</h4>
          <p>Originally designed in 1932 for the CMV 3 bottle microphone. Early U 47s used PVC diaphragms at 12 microns thick with evaporated gold, mounted on brass backplates with 90 precision-drilled holes per side. By 1960, PVC was replaced by Mylar in the K47/K49 capsule. The M7 design is still manufactured today by Microtech Gefell — and it remains the reference capsule that every large-diaphragm condenser is benchmarked against.</p>
        </div>
        <div class="u47-anatomy-item">
          <h4>The Head Grille and Proximity Effect</h4>
          <p>The special wire-mesh construction of the U 47 grille was not merely protective — it contributed measurably to the microphone's tone and enhanced the proximity effect low-bass boost when a singer worked close to the capsule. Sinatra's one-foot distance was precisely calibrated to use this effect without overwhelming it. The grille was available in chrome (studio) and matte (TV and film broadcast) finishes.</p>
        </div>
        <div class="u47-anatomy-item">
          <h4>The Custom-Wound Transformer</h4>
          <p>The output transformer changed twice during the U 47's production life. Early units used one design; the BV-08B transformer replaced it around serial number 4800. The transformer change also coincided with the capsule upgrade to K47/K49. Units are sometimes designated "U 47a" to distinguish the later capsule/transformer combination — though Neumann was inconsistent with this designation and it is not a reliable indicator.</p>
        </div>
      </div>
      <div>
        <img src="{IMG['tube']}" alt="Neumann U 47 VF14 Telefunken tube and internal components" style="width:100%;height:520px;object-fit:cover;object-position:center;display:block">
        <p style="font-size:11px;color:rgba(255,255,255,0.3);letter-spacing:0.06em;text-transform:uppercase;margin-top:12px;font-family:'DM Sans',sans-serif">U 47 internal components — the VF14 tube and capsule assembly</p>
      </div>
    </div>
  </div>

  <!-- VARIANTS TIMELINE ────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="u47-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">Production History</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 36px">Every U 47 Variant, in Order</h2>
      <div class="u47-tl">
        <div class="u47-tl-item">
          <div class="u47-tl-yr">1949 — SN ~1–3250</div>
          <h4>Long Body — Original U 47</h4>
          <p>Brass body (later aluminum), 240mm long, 60mm diameter. M7 capsule with PVC diaphragms, evaporated gold. Original transformer. Available in chrome (studio) or matte (TV/film) grille finish. Large badge on earliest ~300 units: chrome diamond with Neumann logo and serial number. Replaced by the "small badge" — a metal diamond with black lacquer — on subsequent units. Approximately 3,250 long-body units made through mid-1957.</p>
        </div>
        <div class="u47-tl-item">
          <div class="u47-tl-yr">1950 — Early</div>
          <h4>U 48 — First Examples (Figure-Eight Variant)</h4>
          <p>Some U 48 examples exist from as early as 1950 with the first regular production from 1957. Cardioid and figure-eight patterns — the "8" indicates polar pattern, not the year. Approximately 800 U 48s were produced total. George Martin specifically sent Abbey Road's U 47s back to Neumann in Berlin for figure-eight modification, creating the hybrid "U 47/48" designation used at the studio.</p>
        </div>
        <div class="u47-tl-item">
          <div class="u47-tl-yr">Mid-1957 — SN ~3250+</div>
          <h4>Short Body</h4>
          <p>Smaller components allowed the body to shorten by approximately 1.5 inches (200mm long, 60mm diameter) and the transformer to be mounted horizontally. The U 48 appears only in short-body format. All head grille and capsule assemblies (KK47) from a U 47 can be fitted to a U 48 body, making all three polar patterns (cardioid, omni, figure-eight) possible with the complete U 48 plus a spare KK47 assembly.</p>
        </div>
        <div class="u47-tl-item">
          <div class="u47-tl-yr">~1960 — SN ~4800+</div>
          <h4>U 47a — Mylar Capsule (K47/K49) + BV-08B Transformer</h4>
          <p>Replacement material Mylar (polyester) was introduced for the diaphragm, replacing the aging-prone PVC. The new K47/K49 capsule used a single backplate and held the diaphragm in tension with 12 screws in a brass mounting ring — a design still made today by Microtech Gefell. The BV-08B transformer replaced the earlier design. Microphones with the new capsule were often designated "U 47a," though inconsistently.</p>
        </div>
        <div class="u47-tl-item">
          <div class="u47-tl-yr">1963</div>
          <h4>Production Ends — VF14 Stock Exhausted</h4>
          <p>Neumann placed their third and final VF14 tube order in 1958. When that stock ran out in 1963, production of the U 47 and U 48 ceased permanently. No equivalent replacement tube was manufactured by Telefunken or anyone else. The U 47's successor was the U 67, which used the M7-derived capsule with a new EF86 tube. But the U 67 — excellent as it is — never replaced the U 47 in the esteem of engineers who had worked with both.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- STUDIO CARDS ─────────────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="u47-wide" style="margin-bottom:40px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">The Rooms That Defined It</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0;line-height:1.15">Three Studios.<br>Every Voice That Mattered.</h2>
    </div>
    <div class="u47-studios">

      <!-- Capitol Studios -->
      <div class="u47-sc">
        <div class="u47-sc-img" style="background:linear-gradient(155deg,#12100a 0%,#1e1a0e 50%,#0d0c08 100%);height:320px;display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 320" style="position:absolute;top:0;left:0;opacity:0.18" preserveAspectRatio="xMidYMid slice">
            <defs><radialGradient id="cap-g" cx="50%" cy="45%" r="55%"><stop offset="0%" stop-color="#D4860A" stop-opacity="0.5"/><stop offset="100%" stop-color="#12100a" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="320" fill="url(#cap-g)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <polygon points="45,8 82,78 8,78" fill="none" stroke="rgba(212,134,10,0.3)" stroke-width="1"/>
              <text x="45" y="53" text-anchor="middle" fill="rgba(212,134,10,0.65)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">CAPITOL</text>
              <text x="45" y="66" text-anchor="middle" fill="rgba(212,134,10,0.5)" font-size="8" font-family="DM Sans,sans-serif" letter-spacing="1">STUDIOS</text>
            </svg>
          </div>
        </div>
        <div class="u47-sc-body">
          <div class="u47-sc-yr">Est. 1956</div>
          <div class="u47-sc-name">Capitol Studios</div>
          <div class="u47-sc-loc">Hollywood, California</div>
          <p class="u47-sc-text">Frank Sinatra built his late-career vocal legacy here. His U 47 — "Telly" — was the constant. <em>Songs for Swingin' Lovers</em> (1956), <em>Come Fly With Me</em> (1958), <em>Nice 'N' Easy</em> (1960), <em>Sinatra at the Sands</em> (1966). Dean Martin. Nat King Cole. Ella Fitzgerald. The Capitol sound of the 1950s and 60s is largely the U 47's sound — warm, present, intimate, with a low-end presence that placed the voice unmistakably in the room.</p>
        </div>
      </div>

      <!-- Abbey Road -->
      <div class="u47-sc">
        <div class="u47-sc-img" style="background:linear-gradient(160deg,#0d1b2a 0%,#1a2d40 40%,#0f2030 100%);height:320px;display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 320" style="position:absolute;top:0;left:0;opacity:0.15" preserveAspectRatio="xMidYMid slice">
            <defs><radialGradient id="ab2-g" cx="50%" cy="50%" r="55%"><stop offset="0%" stop-color="#2563EB" stop-opacity="0.4"/><stop offset="100%" stop-color="#0d1b2a" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="320" fill="url(#ab2-g)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <circle cx="45" cy="45" r="38" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
              <text x="45" y="40" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">ABBEY</text>
              <text x="45" y="55" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1.5">ROAD</text>
            </svg>
          </div>
        </div>
        <div class="u47-sc-body">
          <div class="u47-sc-yr">Est. 1931</div>
          <div class="u47-sc-name">Abbey Road Studios</div>
          <div class="u47-sc-loc">St. John's Wood, London, UK</div>
          <p class="u47-sc-text">The Beatles recorded their first EMI session on September 6, 1962, with U 47s and U 48s on vocals. George Martin's U 48 in figure-eight mode let him record two singers facing each other — a technique that defined the sound of early Beatles harmonies. By <em>Revolver</em> (1966), Geoff Emerick began using unconventional close-miking techniques with the U 47, placing it far closer to Lennon's voice than any previous engineer had dared. The "thicker and richer" result defined the second half of the Beatles' studio career.</p>
        </div>
      </div>

      <!-- Van Gelder Studio -->
      <div class="u47-sc">
        <div class="u47-sc-img" style="background:linear-gradient(150deg,#1c110a 0%,#2d1a0e 40%,#1a0f07 100%);height:320px;display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 320" style="position:absolute;top:0;left:0;opacity:0.2" preserveAspectRatio="xMidYMid slice">
            <defs><radialGradient id="vg2-g" cx="50%" cy="50%" r="55%"><stop offset="0%" stop-color="#D4860A" stop-opacity="0.3"/><stop offset="100%" stop-color="#1c110a" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="320" fill="url(#vg2-g)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <circle cx="45" cy="45" r="38" fill="none" stroke="rgba(212,134,10,0.25)" stroke-width="1"/>
              <text x="45" y="40" text-anchor="middle" fill="rgba(212,134,10,0.65)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1">VAN GELDER</text>
              <text x="45" y="55" text-anchor="middle" fill="rgba(212,134,10,0.65)" font-size="9" font-family="DM Sans,sans-serif" letter-spacing="1">STUDIO</text>
            </svg>
          </div>
        </div>
        <div class="u47-sc-body">
          <div class="u47-sc-yr">Est. 1953</div>
          <div class="u47-sc-name">Van Gelder Studio</div>
          <div class="u47-sc-loc">Englewood Cliffs, New Jersey</div>
          <p class="u47-sc-text">Rudy Van Gelder received <strong>the second U 47 to arrive in the United States</strong>. He deployed it immediately on Blue Note Records sessions — and the heightened presence and detail it brought to acoustic jazz instruments and vocals became the defining sonic signature of the Blue Note catalogue. Miles Davis's trumpet. John Coltrane's tenor. Art Blakey's cymbals. The immediacy and three-dimensionality of those recordings owes a direct debt to the U 47 pointed at the source.</p>
        </div>
      </div>

    </div>
  </section>

  <!-- RECORDS LIST ─────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="u47-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">The Discography</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 28px">Voices Captured Through a U 47</h2>
    </div>
    <div class="u47-wrap">
      <div class="u47-records">
        <div class="u47-rec"><div><div class="u47-ry">1950s</div></div><div><div class="u47-rt">Blue Note Records catalog</div><div class="u47-ra">Rudy Van Gelder — second U 47 in the USA</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1956</div></div><div><div class="u47-rt">Songs for Swingin' Lovers — Frank Sinatra</div><div class="u47-ra">Capitol Studios — "Telly" the U 47</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1958</div></div><div><div class="u47-rt">Come Fly With Me — Frank Sinatra</div><div class="u47-ra">Capitol Studios, Hollywood</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1959</div></div><div><div class="u47-rt">Kind of Blue — Miles Davis</div><div class="u47-ra">Van Gelder Studio, Englewood Cliffs</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1962</div></div><div><div class="u47-rt">Please Please Me — The Beatles</div><div class="u47-ra">Abbey Road Studios — first EMI session, U 47 and U 48 on vocals</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1963</div></div><div><div class="u47-rt">With the Beatles / A Hard Day's Night</div><div class="u47-ra">Abbey Road — U 48 in figure-8 for harmony vocals</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1964</div></div><div><div class="u47-rt">A Love Supreme — John Coltrane</div><div class="u47-ra">Van Gelder Studio — U 47 on Coltrane's saxophone</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1966</div></div><div><div class="u47-rt">Revolver — The Beatles</div><div class="u47-ra">Geoff Emerick close-miking on U 47 — "thicker and richer"</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">1969</div></div><div><div class="u47-rt">Abbey Road — The Beatles</div><div class="u47-ra">U 47 / U 48 throughout — last studio album</div></div></div>
        <div class="u47-rec"><div><div class="u47-ry">Ongoing</div></div><div><div class="u47-rt">Every major vocal session where one is available</div><div class="u47-ra">From Adele to Kendrick — engineers request it first</div></div></div>
      </div>
    </div>

    <div class="u47-wrap" style="margin-top:48px">
      <div class="u47-pull">
        <p>"At the studio, we have a bunch of great vocal mic options, but the one that goes up first 95% of the time is our U 47. It works best across the broadest range of vocals for what we do. It sounds the most natural, musical, and 'biggest' — which is what we tend to look for most often."</p>
        <cite>Ryan McGuire — President, Vintage King Audio</cite>
      </div>
    </div>
  </section>

  <!-- WHICH U47? ───────────────────────────────────────────────────────── -->
  <section id="which-u47" style="background:#EDE8E2;padding:80px 0">
    <div class="u47-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">Buyer's Guide</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 8px">Which U 47 Path is Right for You?</h2>
      <p style="font-size:15px;color:rgba(26,26,24,0.55);font-family:'DM Sans',sans-serif;margin:0 0 32px">From $439 capsule-inspired condensers to $9,995 Telefunken reissues. Every U 47-descended option at Vintage King, honestly assessed.</p>
    </div>
    <div class="u47-wide">
      <div class="u47-guide">

        <div class="u47-gc">
          <div class="u47-gc-tag" style="background:#D4860A">Entry Point</div>
          <h4>Roswell Mini K47</h4>
          <div class="u47-gc-price">$439</div>
          <p>Named for the K47 capsule design that replaced the M7 in later U 47s. The Mini K47 delivers surprisingly warm, natural large-diaphragm character for home and project studios entering the U 47 sound world at a price point anyone can access.</p>
          <a href="https://vintageking.com/roswell-pro-audio-mini-k47" target="_blank">Shop Roswell Mini K47 →</a>
        </div>

        <div class="u47-gc">
          <h4>Pearlman TM-1</h4>
          <div class="u47-gc-price">$1,760</div>
          <p>Hand-built in the USA by David Pearlman, who has studied vintage U 47 units extensively. Tube-based, transformer-coupled, with a German tube. Pearlman's designs are widely respected as among the best U 47-inspired builds at their price point.</p>
          <a href="https://vintageking.com/pearlman-tm-1" target="_blank">Shop Pearlman TM-1 →</a>
        </div>

        <div class="u47-gc">
          <h4>Telefunken TF47</h4>
          <div class="u47-gc-price">$1,895</div>
          <p>From the company that originally made the VF14 tube and distributed the U 47. The TF47 uses a modern EF732 tube and new K47-style capsule. Telefunken's direct lineage to the original gives this mic a legitimacy beyond most alternatives at this price.</p>
          <a href="https://vintageking.com/telefunken-elektroakustik-tf47" target="_blank">Shop TF47 →</a>
        </div>

        <div class="u47-gc">
          <h4>Pearlman TM-47</h4>
          <div class="u47-gc-price">$2,280</div>
          <p>Pearlman's dedicated U 47 tribute — cardioid and omni, hand-built, with a K47-style capsule. Step up from the TM-1 with a dedicated U 47 circuit topology. Consistently rated among the best U 47-style mics available under $5,000.</p>
          <a href="https://vintageking.com/pearlman-tm-47-cardioid" target="_blank">Shop TM-47 →</a>
        </div>

        <div class="u47-gc">
          <div class="u47-gc-tag" style="background:#1A1A18">Pro Studio</div>
          <h4>FLEA 47 NEXT</h4>
          <div class="u47-gc-price">$4,409</div>
          <p>FLEA Microphones builds meticulous reproductions of classic tube microphones. The FLEA 47 NEXT uses a genuine vintage capsule option and is widely used in professional tracking rooms alongside vintage originals. Considered the closest modern hardware equivalent to the original U 47 by many engineers who own both.</p>
          <a href="https://vintageking.com/flea-microphones-flea-47-next" target="_blank">Shop FLEA 47 NEXT →</a>
        </div>

        <div class="u47-gc">
          <div class="u47-gc-tag" style="background:#C0392B">Reference</div>
          <h4>Telefunken U47</h4>
          <div class="u47-gc-price">$9,995</div>
          <p>Telefunken Elektroakustik's full reissue — a precision-built tribute to the original from the company that made the VF14 tube and held the original distribution rights. For studios wanting the closest possible new-production equivalent at a level of build quality that belongs in a serious professional environment.</p>
          <a href="https://vintageking.com/telefunken-usa-u47" target="_blank">Shop Telefunken U47 →</a>
        </div>

      </div>
    </div>
  </section>

  <!-- FAQ ──────────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="u47-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">Common Questions</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin:0 0 36px">U 47 FAQ</h2>
      <div class="u47-faq">
        <details>
          <summary>What is the difference between the U 47 and U 48?</summary>
          <p>The U 47 offers cardioid and omnidirectional polar patterns. The U 48 offers cardioid and figure-eight. In cardioid mode they are nearly identical in sound. The U 48 figure-eight mode has a slightly higher noise floor due to how the polarization voltage is split between the two diaphragms (52.5V each instead of the ideal 60V for cardioid), and later U 48 units with the BV-08B transformer have a 4–6 dB output loss versus U 47 equivalents. George Martin converted Abbey Road's U 47s to figure-eight specifically to record Beatles harmony vocals facing each other on one mic — those modified units were designated U 47/48.</p>
        </details>
        <details>
          <summary>Why did the U 47 stop being made?</summary>
          <p>The VF14 pentode tube — made only by Telefunken and used in no other microphone — was discontinued after 1958. Of the 27,548 VF14s produced between 1946 and 1958, only about one third passed Neumann's noise and performance tests and were marked for microphone use. Neumann placed three orders; the third was their last. When that stock ran out in 1963, production of the U 47 and U 48 ended permanently. Telefunken produced many other tubes in the VF family, but none were equivalent in spec. No manufacturer has ever produced a genuine VF14 equivalent.</p>
        </details>
        <details>
          <summary>What is the difference between the M7 and K47 capsule?</summary>
          <p>The M7 is the original dual-diaphragm capsule from 1932, used in all U 47s up to approximately serial number 4800. It uses PVC diaphragms at 12 microns thick with evaporated gold, edge-terminated around dual brass backplates with 90 precision-drilled holes per side. The PVC material tends to degrade over time — shrinking and cracking, affecting frequency response. By 1960, Mylar (polyester) replaced PVC in the K47/K49 capsule, which uses a single backplate and 12 mounting screws. Mylar does not degrade the same way. Early M7 capsules that are in excellent condition are often preferred for their upper-mid character, but well-maintained K47 capsules are their equal and more stable.</p>
        </details>
        <details>
          <summary>What is the long body vs. short body U 47?</summary>
          <p>Long body U 47s (approximately serial numbers 1–3250, produced until mid-1957) are 240mm long. As components shrank, the body was shortened to 200mm — the "short body." Both use the same basic circuit. The long body is often preferred by collectors and commands a premium, but sonically the two are comparable given similar capsule and transformer versions. All U 48s are short bodies. The head grille and capsule assembly (KK47) from any U 47 fits any U 48 body.</p>
        </details>
        <details>
          <summary>Why does the U 47 sound different from every other condenser microphone?</summary>
          <p>Three factors work together in a way that has never been fully replicated. First, the VF14 pentode tube's behavior — pentodes are less common in microphone circuits, and the VF14 specifically was selected by Neumann after rigorous noise testing from a limited population. Second, the M7/K47 capsule's large diaphragm and precise backplate geometry capture low-frequency warmth and transient detail simultaneously. Third, the custom-wound transformer and the interaction between these three components creates a mid-range presence peak and a low-frequency warmth that places voices in three-dimensional space. Engineers describe it as sounding "bigger" than the actual sound source — as though the singer is closer and more present than they physically are.</p>
        </details>
        <details>
          <summary>How do I get the U 47 sound on a realistic budget?</summary>
          <p>Several paths. For under $2,000: the Pearlman TM-1 and Telefunken TF47 are genuinely excellent U 47-inspired designs built with care. For $2,000–$5,000: the Pearlman TM-47 and FLEA 47 NEXT are the current studio references for U 47-character at non-vintage prices. For $10,000: the Telefunken U47 reissue is the closest new-production equivalent. For vintage originals ($20,000+): contact Vintage King's team directly — we actively source original U 47 and U 48 units and maintain a waitlist for buyers who are serious.</p>
        </details>
      </div>
    </div>
  </section>

  <!-- EXPLORE MORE ─────────────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="u47-wide" style="margin-bottom:36px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">More From Vintage King</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;margin:0">Continue Exploring</h2>
    </div>
    <div class="u47-wide">
      <div class="u47-more">
        <div class="u47-mc">
          <span>Hall of Fame</span>
          <h4>Teletronix LA-2A — The Voice of a Generation</h4>
          <p>The U 47 captures the voice. The LA-2A shapes it. Pair them and you have the most documented vocal chain in recording history.</p>
          <a href="la-2a.html">Read the Guide →</a>
        </div>
        <div class="u47-mc">
          <span>Hall of Fame</span>
          <h4>Neve 1073 — The Definitive Guide</h4>
          <p>After the U 47 and the LA-2A, the 1073 preamp is the next piece in the classic vocal chain. Every version, every studio that ran one.</p>
          <a href="neve-1073-guide-v2.html">Read the Guide →</a>
        </div>
        <div class="u47-mc">
          <span>Audio Consulting</span>
          <h4>Talk to a VK Expert</h4>
          <p>Mike Nehra and Ryan McGuire both quoted on this page. Those are the people who answer the phone at Vintage King.</p>
          <a href="audio-consultants.html">Meet the Team →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA ──────────────────────────────────────────────────────────────── -->
  <section style="background:#EDE8E2;padding:80px 48px">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:16px">Vintage King Audio</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 20px;line-height:1.2">Ready to Find Your U 47?</h2>
      <p style="font-size:16px;color:#3A3A38;line-height:1.7;margin:0 0 36px">From K47-inspired condensers to the Telefunken reissue and genuine vintage originals — our team has handled more U 47 transactions than any dealer in the country. We know every unit on the market and will tell you honestly what each one sounds like.</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a href="https://vintageking.com/neumann-u47-u48-microphone" target="_blank" style="background:#C0392B;color:#fff;padding:16px 36px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;text-decoration:none;letter-spacing:0.04em">Shop All U 47</a>
        <a href="audio-consultants.html" style="background:transparent;color:#1A1A18;border:1px solid rgba(26,26,24,0.35);padding:16px 28px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;text-decoration:none">Talk to an Expert</a>
      </div>
    </div>
  </section>

  <!-- STICKY BAR ───────────────────────────────────────────────────────── -->
  <div class="u47-stick">
    <div>
      <div class="u47-stick-title">Neumann U 47</div>
      <div class="u47-stick-sub">K47-inspired from $439 · Telefunken reissue $9,995 · Vintage originals by request</div>
    </div>
    <div style="display:flex;gap:12px;align-items:center">
      <a href="https://vintageking.com/neumann-u47-u48-microphone" target="_blank" class="u47-stick-cta">Shop at Vintage King</a>
      <a href="audio-consultants.html" class="u47-stick-ghost">Ask an Expert</a>
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
