"""fairchild-660-670.html — Hall of Fame editorial guide to the Fairchild 660/670."""
import re

INLINE_JS = """\
<script>
  (function() {
    var p = 'fairchild-660-670';
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

SLUG  = "fairchild-660-670"
TITLE = "Fairchild 660 and 670 — Holy Grail of Compression | Vintage King Audio"
META  = "The definitive guide to the Fairchild 660 and 670 — history, engineering, the studios that owned them, and every version available at Vintage King. Built with 20 tubes and a legacy that never quit."

IMG = {
    "hero_670":      "images/fairchild/fairchild-670-hero.webp",
    "abbey_rack":    "images/fairchild/fairchild-660-abbey-road.jpg",
}

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Fairchild 660 and 670 — Holy Grail of Compression",
      "description": "The definitive guide to the Fairchild 660 and 670 variable-mu tube compressors. History, engineering, the studios that owned them, the records they made, and every version at Vintage King.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "Fairchild 660 and 670 Tube Compressor-Limiter",
      "brand": {"@type": "Brand", "name": "Fairchild Recording Equipment"},
      "description": "Variable-mu tube compressor-limiter. 20 tubes, 11 transformers, 65 lbs. The most imitated compressor ever built.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "29.99",
        "highPrice": "29500",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between the Fairchild 660 and 670?",
          "acceptedAnswer": {"@type": "Answer", "text": "The 660 is a single-channel mono unit. The 670 is a dual-channel stereo version with an added matrixing network for Left/Right or Mid/Side operation. The 670 contains 20 tubes and 11 transformers versus the 660's 10 tubes. Both share the same variable-mu circuit and RCA 6386 tube topology."}
        },
        {
          "@type": "Question",
          "name": "How many original Fairchild compressors were made?",
          "acceptedAnswer": {"@type": "Answer", "text": "Fewer than 1,000 stereo 670 units were ever produced. Approximately 800 mono 660 units were built, with the first 10 hand-assembled by designer Rein Narma himself. Very few originals survive in working condition today."}
        },
        {
          "@type": "Question",
          "name": "Why does the Fairchild sound so good on vocals?",
          "acceptedAnswer": {"@type": "Answer", "text": "The Fairchild's extremely fast attack time (0.2 milliseconds) catches sibilance and sharp transients before they distort, while its long release (300ms to 25 seconds depending on setting) lets the signal breathe naturally. The variable-mu soft knee adds gain reduction so gradually that the ear never registers it as compression — only as silkiness."}
        },
        {
          "@type": "Question",
          "name": "What is a variable-mu compressor?",
          "acceptedAnswer": {"@type": "Answer", "text": "Variable-mu compressors use vacuum tubes whose amplification factor (mu) decreases as the control voltage increases. Unlike fixed-ratio VCA or optical designs, the Fairchild's ratio rises from about 1:1 on quiet signals to 20:1 on peaks — giving a soft, program-dependent response that sounds extremely natural."}
        }
      ]
    }
  ]
}
</script>
"""

CHROME = """\
<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <a href="hall-of-fame.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Hall of Fame</a>
  <span style="opacity:0.35">|</span>
  <a href="neve-1073-guide-v2.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Neve 1073 Guide</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Fairchild 660 / 670</span>
</nav>
"""

PAGE_BODY = f"""\
<div id="fairchild-660-670" class="page active">
  <div id="nav-fairchild-660-670"></div>

  <style>
    /* ─── Fairchild HOF page ─────────────────────────────────────────── */
    .fc2-wrap   {{ max-width:860px;margin:0 auto;padding:0 32px }}
    .fc2-wide   {{ max-width:1280px;margin:0 auto;padding:0 48px }}

    .fc2-bread  {{ max-width:1280px;margin:0 auto;padding:14px 48px;font-size:13px;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif }}
    .fc2-bread a {{ color:rgba(26,26,24,0.42);text-decoration:none }}
    .fc2-bread a:hover {{ color:#D4860A }}
    .fc2-bread span {{ margin:0 8px }}

    .fc2-body h2 {{ font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;margin:56px 0 16px;line-height:1.2 }}
    .fc2-body h2:first-child {{ margin-top:0 }}
    .fc2-body p  {{ font-size:16px;color:#3A3A38;line-height:1.82;margin-bottom:18px }}
    .fc2-body strong {{ color:#1A1A18;font-weight:600 }}
    .fc2-body ul {{ margin:14px 0 18px 22px;font-size:16px;color:#3A3A38;line-height:1.85 }}

    /* Pull quotes */
    .fc2-pull {{ border-left:3px solid #D4860A;padding:20px 28px;margin:44px 0;background:rgba(212,134,10,0.05) }}
    .fc2-pull p {{ font-family:'Playfair Display',serif;font-size:22px;font-style:italic;line-height:1.5;color:#1A1A18;margin:0!important }}
    .fc2-pull cite {{ display:block;margin-top:12px;font-size:12px;font-style:normal;color:#D4860A;letter-spacing:0.1em;text-transform:uppercase;font-weight:600 }}

    /* Full-width strip */
    .fc2-strip {{ background:#fff;padding:56px 0;margin:0 }}
    .fc2-strip img {{ width:100%;height:520px;object-fit:cover;object-position:center 40%;display:block }}
    .fc2-strip figcaption {{ text-align:center;font-size:12px;color:rgba(26,26,24,0.44);letter-spacing:0.06em;text-transform:uppercase;margin-top:14px;font-family:'DM Sans',sans-serif }}

    /* Stat bar */
    .fc2-stats {{ background:var(--warm-white,#FDFCFB);border-top:1px solid rgba(26,26,24,0.1);border-bottom:1px solid rgba(26,26,24,0.1);padding:0 }}
    .fc2-stats-inner {{ max-width:1280px;margin:0 auto;padding:0 48px;display:flex;align-items:stretch }}
    .fc2-stat {{ flex:1;padding:22px 0;text-align:center;border-right:1px solid rgba(26,26,24,0.08) }}
    .fc2-stat:last-child {{ border-right:none }}
    .fc2-stat-n {{ font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;display:block;line-height:1 }}
    .fc2-stat-l {{ font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif;margin-top:5px }}

    /* Studio cards — 3-column */
    .fc2-studios {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:2px;margin:0 }}
    .fc2-sc {{ position:relative;overflow:hidden;cursor:default }}
    .fc2-sc-img {{ height:340px;background-size:cover;background-position:center;transition:transform .6s ease }}
    .fc2-sc:hover .fc2-sc-img {{ transform:scale(1.03) }}
    .fc2-sc-body {{ padding:24px 28px 28px }}
    .fc2-sc-year {{ font-family:'DM Sans',sans-serif;font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;font-weight:600;margin-bottom:8px }}
    .fc2-sc-name {{ font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:#1A1A18;line-height:1.25;margin-bottom:6px }}
    .fc2-sc-loc  {{ font-size:13px;color:rgba(26,26,24,0.48);margin-bottom:12px;font-family:'DM Sans',sans-serif }}
    .fc2-sc-text {{ font-size:14px;color:#3A3A38;line-height:1.65 }}

    /* Records list */
    .fc2-records {{ display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(26,26,24,0.08) }}
    .fc2-rec {{ background:#fff;padding:18px 24px;display:flex;align-items:baseline;gap:16px }}
    .fc2-ry  {{ font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;color:#D4860A;letter-spacing:0.04em;min-width:38px;padding:2px 10px 2px 0;border-right:2px solid #D4860A;line-height:1 }}
    .fc2-rt  {{ font-size:14px;color:#1A1A18;font-weight:500 }}
    .fc2-ra  {{ font-size:13px;color:rgba(26,26,24,0.48);margin-top:2px }}

    /* Time-constant table */
    .fc2-tc-table {{ width:100%;border-collapse:collapse;font-family:'DM Sans',sans-serif;font-size:14px;margin:24px 0 }}
    .fc2-tc-table th {{ background:#1A1A18;color:#FDFCFB;padding:10px 16px;text-align:left;font-weight:500;font-size:12px;letter-spacing:0.1em;text-transform:uppercase }}
    .fc2-tc-table td {{ padding:11px 16px;border-bottom:1px solid rgba(26,26,24,0.08);color:#3A3A38 }}
    .fc2-tc-table tr:last-child td {{ border-bottom:none }}
    .fc2-tc-table td:first-child {{ font-weight:600;color:#1A1A18;width:90px }}
    .fc2-tc-table tr:hover td {{ background:rgba(212,134,10,0.04) }}
    .fc2-tc-badge {{ display:inline-block;background:#D4860A;color:#fff;font-size:10px;font-weight:600;padding:2px 7px;border-radius:2px;letter-spacing:0.06em;text-transform:uppercase;margin-left:8px;vertical-align:middle }}

    /* Which Fairchild? decision guide */
    .fc2-guide {{ display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:32px }}
    .fc2-guide-card {{ background:#fff;border:1px solid rgba(26,26,24,0.1);padding:28px;position:relative }}
    .fc2-guide-card h4 {{ font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 8px }}
    .fc2-guide-card .fc2-gc-price {{ font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;color:#C0392B;margin-bottom:14px }}
    .fc2-guide-card p {{ font-size:14px;color:#3A3A38;line-height:1.6;margin:0 0 16px }}
    .fc2-guide-card a {{ display:inline-block;font-size:13px;font-weight:600;color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.3) }}
    .fc2-guide-card a:hover {{ border-bottom-color:#C0392B }}
    .fc2-gc-tag {{ position:absolute;top:-1px;right:20px;background:#D4860A;color:#fff;font-size:10px;font-weight:700;padding:4px 10px;letter-spacing:0.08em;text-transform:uppercase }}

    /* Product alt cards */
    .fc2-alts {{ display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(26,26,24,0.06) }}
    .fc2-alt {{ background:#fff;padding:28px 24px;text-align:center }}
    .fc2-alt-name {{ font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#1A1A18;margin-bottom:6px }}
    .fc2-alt-price {{ font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;color:#C0392B;margin-bottom:12px }}
    .fc2-alt-desc {{ font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6;margin-bottom:16px }}
    .fc2-alt a {{ font-size:13px;font-weight:600;color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.3) }}

    /* FAQ */
    .fc2-faq {{ border-top:1px solid rgba(26,26,24,0.1) }}
    .fc2-faq details {{ border-bottom:1px solid rgba(26,26,24,0.1);padding:0 }}
    .fc2-faq summary {{ font-family:'DM Sans',sans-serif;font-size:16px;font-weight:600;color:#1A1A18;padding:22px 0;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center }}
    .fc2-faq summary::after {{ content:'＋';font-size:18px;font-weight:300;color:rgba(26,26,24,0.35);transition:transform .2s }}
    .fc2-faq details[open] summary::after {{ content:'－' }}
    .fc2-faq details p {{ font-size:15px;color:#3A3A38;line-height:1.75;padding-bottom:24px;margin:0 }}

    /* Explore more */
    .fc2-more {{ display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(26,26,24,0.06) }}
    .fc2-more-card {{ background:#fff;padding:28px 24px }}
    .fc2-more-card span {{ display:block;font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:8px }}
    .fc2-more-card h4 {{ font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 10px;line-height:1.3 }}
    .fc2-more-card p {{ font-size:14px;color:rgba(26,26,24,0.55);line-height:1.65;margin:0 0 16px }}
    .fc2-more-card a {{ font-size:13px;font-weight:600;color:#C0392B;text-decoration:none }}

    /* Sticky bar */
    .fc2-stick {{ position:fixed;bottom:0;left:0;right:0;background:#1A1A18;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;border-top:2px solid #C0392B }}
    .fc2-stick-title {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB }}
    .fc2-stick-sub {{ font-size:12px;color:rgba(255,255,255,0.48);margin-top:2px }}
    .fc2-stick-actions {{ display:flex;gap:12px;align-items:center }}
    .fc2-stick-cta {{ background:#C0392B;color:#fff;border:none;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;cursor:pointer;letter-spacing:0.04em;text-decoration:none;display:inline-block }}
    .fc2-stick-cta:hover {{ background:#a93226 }}
    .fc2-stick-ghost {{ color:rgba(255,255,255,0.65);font-size:13px;font-weight:500;text-decoration:none;padding:12px 0 }}
    .fc2-stick-ghost:hover {{ color:#fff }}

    @media(max-width:900px){{
      .fc2-hero-split {{ grid-template-columns:1fr!important;min-height:auto!important }}
      .fc2-hero-img {{ height:260px!important;width:100%!important }}
      .fc2-studios,.fc2-records,.fc2-guide,.fc2-alts,.fc2-more {{ grid-template-columns:1fr }}
      .fc2-stats-inner {{ flex-wrap:wrap }}
      .fc2-stat {{ min-width:50% }}
      .fc2-stick {{ padding:12px 20px }}
      .fc2-wide,.fc2-bread {{ padding-left:20px;padding-right:20px }}
      .fc2-wrap {{ padding:0 20px }}
    }}
  </style>

  <!-- HERO — full-bleed split ───────────────────────────────────────── -->
  <section style="background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:620px;overflow:hidden">
    <div style="padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:16px">Pro Audio Hall of Fame</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:56px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 24px">Fairchild<br>660 / 670</h1>
      <p style="font-size:18px;color:#3A3A38;line-height:1.7;max-width:520px;margin:0 0 12px;font-family:'DM Sans',sans-serif">The most imitated compressor ever built. Fewer than 1,000 stereo units were ever made. Records through one and you're in the company of the Beatles, Miles Davis, Led Zeppelin, and Jimi Hendrix.</p>
      <p style="font-size:15px;color:rgba(26,26,24,0.5);font-family:'DM Sans',sans-serif;margin:0 0 32px">Designed 1955. Still irreplaceable in 2026.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="https://vintageking.com/fairchild-660-670-compressor-limiter" target="_blank" style="background:#C0392B;color:#fff;padding:14px 32px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em">Shop All Fairchild</a>
        <a href="#which-fairchild" style="background:transparent;color:#1A1A18;border:1px solid rgba(26,26,24,0.35);padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;text-decoration:none">Which One is Right for Me?</a>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;padding:32px;position:relative">
      <img src="{IMG['hero_670']}" alt="Fairchild Model 670 front panel — dual VU meters and time constant controls" style="width:100%;height:520px;object-fit:cover;object-position:center 50%;display:block">
      <div style="position:absolute;bottom:14px;right:16px;font-size:10px;letter-spacing:0.08em;text-transform:uppercase;color:rgba(255,255,255,0.55);font-family:'DM Sans',sans-serif">Fairchild Model 670 — Original Production Unit</div>
    </div>
  </section>

  <!-- BREADCRUMB -->
  <div class="fc2-bread">
    <a href="https://vintageking.com">Vintage King</a><span>›</span>
    <a href="https://vintageking.com/pro-audio-hall-of-fame">Hall of Fame</a><span>›</span>
    Fairchild 660 / 670
  </div>

  <!-- STAT BAR ──────────────────────────────────────────────────────────── -->
  <div class="fc2-stats">
    <div class="fc2-stats-inner">
      <div class="fc2-stat">
        <span class="fc2-stat-n" style="font-family:'DM Sans',sans-serif;font-size:28px">1959</span>
        <div class="fc2-stat-l">Year Introduced</div>
      </div>
      <div class="fc2-stat">
        <span class="fc2-stat-n">&lt;1,000</span>
        <div class="fc2-stat-l">Stereo Units Made</div>
      </div>
      <div class="fc2-stat">
        <span class="fc2-stat-n">20</span>
        <div class="fc2-stat-l">Vacuum Tubes (670)</div>
      </div>
      <div class="fc2-stat">
        <span class="fc2-stat-n">11</span>
        <div class="fc2-stat-l">Transformers (670)</div>
      </div>
      <div class="fc2-stat">
        <span class="fc2-stat-n">65 lbs</span>
        <div class="fc2-stat-l">Unit Weight</div>
      </div>
      <div class="fc2-stat">
        <span class="fc2-stat-n">0.2 ms</span>
        <div class="fc2-stat-l">Fastest Attack</div>
      </div>
    </div>
  </div>

  <!-- INTRO BODY ────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="fc2-wrap fc2-body">
      <h2>The Holy Grail — and Why It Earned That Name</h2>
      <p>There are compressors that engineers reach for, and then there is the Fairchild 670. For over sixty years it has sat at the apex of the compression world — not because of marketing, not because of scarcity alone, but because no one has completely explained why it sounds the way it does and managed to fully replicate it. That mystery is the point. A well-maintained Fairchild does something to audio that no other device quite matches: it makes everything sound more <strong>present, three-dimensional, and alive</strong>, often while barely moving the gain-reduction meter.</p>
      <p>Fewer than 1,000 stereo 670 units were ever manufactured. Very few of those survive in working condition. The ones that do command prices above $30,000 — when they can be found at all. And every year, a new wave of engineers builds studios with the singular goal of eventually owning one. That is not nostalgia. That is a compressor that has outlasted decades of "better" technology and still wins the shootout.</p>

      <div class="fc2-pull">
        <p>"Right the way through my studio career the Fairchild 670 was a staple in any commercial studio... They were rolled out like secret weapons to bring an electric guitar to life or add punch to a snare drum or bass drum, or to squash an entire mix."</p>
        <cite>Pete Townshend — The Who</cite>
      </div>

      <h2>From a Basement in New Jersey to Every Major Studio on Earth</h2>
      <p>The Fairchild story begins with <strong>Rein Narma</strong>, an Estonian-born engineer who had fled World War II and arrived in the United States working for the United Nations. By the early 1950s, Narma was one of the most sought-after audio technicians in the New York area. His clients were not small: he built custom mixing consoles for <strong>Rudy Van Gelder</strong>, the engineer behind hundreds of Blue Note Records masterpieces, and for guitar inventor and recording pioneer <strong>Les Paul</strong> — including Les Paul's legendary "Monster" desk paired with his "Octopus" 8-track Ampex recorder.</p>
      <p>Narma was frustrated by the limitations of available dynamics processors and began developing a better compressor-limiter under Gotham Audio Development, a company he co-founded in 1954. When Gotham folded, he took his compressor designs with him.</p>
      <p>Enter <strong>Sherman Fairchild</strong> — heir to the fortune of his father, one of the founders of IBM, and a prolific inventor himself with passions for photography and professional audio. Sherman had founded Fairchild Recording Equipment Company in 1931. Through a mutual connection, he heard about Narma's new limiter design, licensed it, and brought Narma on as Chief Engineer. Narma's creation became the Fairchild 660 and, in 1959, the stereo 670.</p>
      <p>The first production 660 went to <strong>Rudy Van Gelder</strong> at his Hackensack, New Jersey studio — where he was cutting lacquer masters for Blue Note Records. The second unit shipped to <strong>Olmsted Sound Studios</strong> in New York City, where a decade later Jimi Hendrix would record. The third went to <strong>Les Paul</strong> himself. Narma made custom consoles for all three. These were not random sales. These were the three most important recording rooms in America, and they all wanted Narma's compressor first.</p>
    </div>
  </section>

  <!-- FULL-WIDTH GEAR PHOTO ─────────────────────────────────────────────── -->
  <figure class="fc2-strip" style="padding:0;margin:0">
    <img src="{IMG['hero_670']}" alt="Fairchild Model 670 stereo tube compressor-limiter, original production unit" style="width:100%;height:520px;object-fit:cover;object-position:center 40%;display:block">
    <figcaption style="text-align:center;font-size:12px;color:rgba(26,26,24,0.44);letter-spacing:0.06em;text-transform:uppercase;padding:14px 0 16px;background:#fff;font-family:'DM Sans',sans-serif">Fairchild Model 670 — 20 tubes, 11 transformers, 65 lbs. Circa 1959–1962.</figcaption>
  </figure>

  <!-- TECHNICAL DEEP DIVE ──────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0 0">
    <div class="fc2-wrap fc2-body">
      <h2>Inside the Machine — Why 20 Tubes and 11 Transformers</h2>
      <p>The Fairchild 670's size and weight are not gratuitous. The 65-pound, 6U enclosure is packed with hardware for a reason: <strong>most of the components never touch the audio signal</strong>. The actual signal path is elegantly simple — an input transformer, a single variable push-pull amplifier stage, and an output transformer. Everything else — those 20 tubes, those 11 transformers, the inductors, the control circuitry — exists solely to generate and manage the side-chain control voltage with enough precision and power to drive the gain cells cleanly.</p>
      <p>At the heart of the design are <strong>RCA 6386 dual-triode tubes</strong>. Each channel uses four of them, wired in parallel, in a push-pull configuration. This parallel topology dramatically lowers impedance and minimizes noise and distortion — essential in an era when engineers were genuinely trying to make things sound as clean as possible. The high control voltages generated by the side-chain circuitry (far higher than comparable designs) give the Fairchild its characteristic grip and authority.</p>
      <p>The compression principle is <strong>variable-mu</strong>: as the control voltage rises, the amplification factor (mu) of the gain-cell tubes falls. Unlike VCA or optical compressors with a fixed ratio, the Fairchild's ratio is program-dependent — starting around 1:1 on quiet signals and rising to as high as 20:1 on loud peaks. The transition is a soft knee so gradual the ear perceives it not as compression but as a kind of tonal focus.</p>
    </div>
  </section>

  <!-- TIME CONSTANTS TABLE ─────────────────────────────────────────────── -->
  <section style="background:#fff;padding:0 0 80px">
    <div class="fc2-wrap">
      <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#1A1A18;margin:40px 0 8px">The Six Time Constants — What Every Switch Position Actually Does</h3>
      <p style="font-size:15px;color:rgba(26,26,24,0.55);margin-bottom:20px;font-family:'DM Sans',sans-serif">One rotary switch. Six distinct personalities. Most engineers never leave position 1 on vocal sources — and most originals show decades of wear on that exact position.</p>
      <table class="fc2-tc-table">
        <thead>
          <tr>
            <th>Position</th>
            <th>Attack</th>
            <th>Release</th>
            <th>Best for</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1 <span class="fc2-tc-badge">Most Used</span></td>
            <td>0.2 ms</td>
            <td>0.3 sec</td>
            <td>Vocals, vocal bus, pop productions</td>
          </tr>
          <tr>
            <td>2</td>
            <td>0.2 ms</td>
            <td>0.8 sec</td>
            <td>Vocals with more sustain, acoustic instruments</td>
          </tr>
          <tr>
            <td>3</td>
            <td>0.4 ms</td>
            <td>2 sec</td>
            <td>Strings, woodwinds, classical</td>
          </tr>
          <tr>
            <td>4</td>
            <td>0.8 ms</td>
            <td>5 sec</td>
            <td>Classical, orchestral bus</td>
          </tr>
          <tr>
            <td>5</td>
            <td>0.4 ms</td>
            <td>Program-adaptive: 2 sec (peaks) / 10 sec (sustained)</td>
            <td>Full mixes, broadcast leveling</td>
          </tr>
          <tr>
            <td>6</td>
            <td>0.2 ms</td>
            <td>Program-adaptive: 0.3 sec (peaks) / up to 25 sec (programme)</td>
            <td>Mastering, disc cutting, long-form level control</td>
          </tr>
        </tbody>
      </table>
      <p style="font-size:14px;color:rgba(26,26,24,0.5);font-family:'DM Sans',sans-serif;margin-top:14px">The user manual originally recommended positions 1 and 2 for pop music, positions 3 and 4 for classical. Position 6 was designed for vinyl disc cutting — where consistent average levels over a full side were critical.</p>
    </div>
  </section>

  <!-- STUDIO CARDS ─────────────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="fc2-wide" style="margin-bottom:40px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">The Rooms That Owned One</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#1A1A18;margin:0;line-height:1.15">Three Studios. Three Legends.<br>One Compressor.</h2>
    </div>
    <div class="fc2-studios">
      <!-- Card 1: Abbey Road -->
      <div class="fc2-sc" style="background:#fff">
        <div class="fc2-sc-img" style="background:linear-gradient(160deg,#0d1b2a 0%,#1a2d40 40%,#0f2030 100%);height:340px;display:flex;align-items:flex-end;padding:0">
          <svg width="100%" height="100%" viewBox="0 0 440 340" preserveAspectRatio="xMidYMid slice" style="position:absolute;top:0;left:0;opacity:0.18">
            <rect width="440" height="340" fill="url(#ab-grad)"/>
            <defs><linearGradient id="ab-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2563EB"/><stop offset="100%" stop-color="#0d1b2a"/></linearGradient></defs>
            <!-- Stylized console silhouette -->
            <rect x="40" y="180" width="360" height="80" rx="4" fill="rgba(255,255,255,0.06)"/>
            <rect x="60" y="160" width="12" height="24" rx="2" fill="rgba(255,255,255,0.12)"/>
            <rect x="80" y="155" width="12" height="29" rx="2" fill="rgba(255,255,255,0.08)"/>
            <rect x="100" y="162" width="12" height="22" rx="2" fill="rgba(255,255,255,0.14)"/>
            <rect x="120" y="158" width="12" height="26" rx="2" fill="rgba(255,255,255,0.10)"/>
            <rect x="140" y="163" width="12" height="21" rx="2" fill="rgba(255,255,255,0.12)"/>
            <circle cx="68" cy="140" r="6" fill="rgba(212,134,10,0.6)"/>
            <circle cx="88" cy="136" r="5" fill="rgba(212,134,10,0.4)"/>
            <circle cx="108" cy="142" r="6" fill="rgba(212,134,10,0.5)"/>
          </svg>
          <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)">
            <svg width="90" height="90" viewBox="0 0 90 90">
              <circle cx="45" cy="45" r="40" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
              <text x="45" y="38" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="11" font-family="DM Sans,sans-serif" letter-spacing="2">ABBEY</text>
              <text x="45" y="54" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-size="11" font-family="DM Sans,sans-serif" letter-spacing="2">ROAD</text>
            </svg>
          </div>
        </div>
        <div class="fc2-sc-body" style="background:#fff">
          <div class="fc2-sc-year">Est. 1931</div>
          <div class="fc2-sc-name">Abbey Road Studios</div>
          <div class="fc2-sc-loc">St. John's Wood, London, UK</div>
          <p class="fc2-sc-text">From A Hard Day's Night (1964) onward, Abbey Road ran Fairchild 660 units on virtually every Beatles session. Geoff Emerick used them on John Lennon's and Paul McCartney's vocals from <em>Revolver</em> through <em>Abbey Road</em>. The 660's 0.2ms attack removed sibilance without dulling; the slow release added what engineers called "silk." It also gave Ringo's kick and snare that locked, focused transient that defined a generation of drum sound.</p>
        </div>
      </div>

      <!-- Card 2: Van Gelder Studio -->
      <div class="fc2-sc" style="background:#fff">
        <div class="fc2-sc-img" style="background:linear-gradient(150deg,#1c110a 0%,#2d1a0e 40%,#1a0f07 100%);height:340px;display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 340" preserveAspectRatio="xMidYMid slice" style="position:absolute;top:0;left:0;opacity:0.22">
            <defs><radialGradient id="vg-grad" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#D4860A" stop-opacity="0.3"/><stop offset="100%" stop-color="#1c110a" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="340" fill="url(#vg-grad)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="100" height="100" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="44" fill="none" stroke="rgba(212,134,10,0.3)" stroke-width="1"/>
              <text x="50" y="44" text-anchor="middle" fill="rgba(212,134,10,0.7)" font-size="10" font-family="DM Sans,sans-serif" letter-spacing="1.5">VAN GELDER</text>
              <text x="50" y="60" text-anchor="middle" fill="rgba(212,134,10,0.7)" font-size="10" font-family="DM Sans,sans-serif" letter-spacing="1.5">STUDIO</text>
            </svg>
          </div>
        </div>
        <div class="fc2-sc-body" style="background:#fff">
          <div class="fc2-sc-year">Est. 1953</div>
          <div class="fc2-sc-name">Van Gelder Studio</div>
          <div class="fc2-sc-loc">Englewood Cliffs, New Jersey</div>
          <p class="fc2-sc-text">Rudy Van Gelder received <strong>the very first Fairchild 660 ever sold</strong>. He used it cutting lacquer masters for Blue Note Records — which means it is on <em>Kind of Blue</em>, <em>A Love Supreme</em>, <em>Somethin' Else</em>, and hundreds more. When mastering engineers talk about the depth and presence in those Blue Note recordings, the Fairchild 660 is part of that answer. The same unit that caught John Coltrane's breath, Miles Davis's trumpet bell, and Art Blakey's rim shots at the source.</p>
        </div>
      </div>

      <!-- Card 3: Olmsted Sound Studios -->
      <div class="fc2-sc" style="background:#fff">
        <div class="fc2-sc-img" style="background:linear-gradient(155deg,#0e1a0e 0%,#162416 45%,#0a130a 100%);height:340px;display:flex;align-items:center;justify-content:center;position:relative">
          <svg width="100%" height="100%" viewBox="0 0 440 340" preserveAspectRatio="xMidYMid slice" style="position:absolute;top:0;left:0;opacity:0.2">
            <defs><radialGradient id="os-grad" cx="50%" cy="50%" r="60%"><stop offset="0%" stop-color="#4a7c4e" stop-opacity="0.4"/><stop offset="100%" stop-color="#0e1a0e" stop-opacity="0"/></radialGradient></defs>
            <rect width="440" height="340" fill="url(#os-grad)"/>
          </svg>
          <div style="position:relative;text-align:center">
            <svg width="100" height="100" viewBox="0 0 100 100">
              <rect x="8" y="8" width="84" height="84" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
              <text x="50" y="44" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10" font-family="DM Sans,sans-serif" letter-spacing="1.5">OLMSTED</text>
              <text x="50" y="60" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="10" font-family="DM Sans,sans-serif" letter-spacing="1.5">SOUND</text>
            </svg>
          </div>
        </div>
        <div class="fc2-sc-body" style="background:#fff">
          <div class="fc2-sc-year">Est. 1957</div>
          <div class="fc2-sc-name">Olmsted Sound Studios</div>
          <div class="fc2-sc-loc">New York City, New York</div>
          <p class="fc2-sc-text">The second Fairchild 660 ever sold went to Olmsted Sound Studios in Manhattan. A decade later, <strong>Jimi Hendrix</strong> would record there — and the Fairchild was part of the signal chain that captured his sessions. Olmsted was one of the most active commercial studios in New York through the 1960s, and having the second unit off the production line gave it a technical advantage that most studios would not catch up to for years.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ABBEY ROAD RACK PHOTO ────────────────────────────────────────────── -->
  <figure style="margin:0;background:#fff;padding:0">
    <img src="{IMG['abbey_rack']}" alt="Fairchild 660 limiter rack at Abbey Road Studios with EMI Presence Box and Altec RS124, 1960s" style="width:100%;height:480px;object-fit:cover;object-position:center 55%;display:block">
    <figcaption style="text-align:center;font-size:12px;color:rgba(26,26,24,0.44);letter-spacing:0.06em;text-transform:uppercase;padding:14px 0 16px;background:#fff;font-family:'DM Sans',sans-serif">Fairchild 660 (left) alongside the EMI Presence Box and Altec RS124 in Abbey Road Studios rack — original 1960s equipment, still intact</figcaption>
  </figure>

  <!-- RECORDS LIST ─────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="fc2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">The Discography</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 32px;line-height:1.2">Records Made Through a Fairchild</h2>
    </div>
    <div class="fc2-wrap">
      <div class="fc2-records">
        <div class="fc2-rec"><div><div class="fc2-ry">1955</div></div><div><div class="fc2-rt">Early Blue Note Sessions</div><div class="fc2-ra">Rudy Van Gelder — Van Gelder Studio</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1959</div></div><div><div class="fc2-rt">Kind of Blue — Miles Davis</div><div class="fc2-ra">Van Gelder Studio, Englewood Cliffs</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1960</div></div><div><div class="fc2-rt">A Love Supreme — John Coltrane</div><div class="fc2-ra">Van Gelder Studio, Englewood Cliffs</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1964</div></div><div><div class="fc2-rt">A Hard Day's Night — The Beatles</div><div class="fc2-ra">Abbey Road Studios, London — first Beatles album with Fairchild</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1965</div></div><div><div class="fc2-rt">Help! / Rubber Soul — The Beatles</div><div class="fc2-ra">Abbey Road Studios — Fairchild on all vocals</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1966</div></div><div><div class="fc2-rt">Revolver — The Beatles</div><div class="fc2-ra">Geoff Emerick, Abbey Road — defining use on Lennon and McCartney vocals</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1967</div></div><div><div class="fc2-rt">Sgt. Pepper's Lonely Hearts Club Band</div><div class="fc2-ra">Abbey Road Studios — Fairchild on drums, vocals, piano</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1968</div></div><div><div class="fc2-rt">The White Album — The Beatles</div><div class="fc2-ra">Abbey Road Studios — including "Octopus's Garden" LFO vocal trick</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1969</div></div><div><div class="fc2-rt">Abbey Road — The Beatles</div><div class="fc2-ra">Abbey Road Studios — final studio album, Fairchild throughout</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1969</div></div><div><div class="fc2-rt">Jimi Hendrix sessions</div><div class="fc2-ra">Olmsted Sound Studios, New York City</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">1970s</div></div><div><div class="fc2-rt">Pete Townshend solo albums (multiple)</div><div class="fc2-ra">Produced by Chris Thomas — 670 rented in as "secret weapon"</div></div></div>
        <div class="fc2-rec"><div><div class="fc2-ry">Ongoing</div></div><div><div class="fc2-rt">Major label sessions worldwide</div><div class="fc2-ra">Wherever a working unit exists, it is used</div></div></div>
      </div>
    </div>

    <div class="fc2-wrap" style="margin-top:48px">
      <div class="fc2-pull">
        <p>"The Fairchild 670 is my favorite piece of gear. Everything sounds great through it — especially vocals, piano, and drums. I like it on my master bus too, even without compressing at all, just for color."</p>
        <cite>Armando Avila — Producer (Thalia, Luis Fonsi, Gloria Trevi)</cite>
      </div>
      <p style="font-size:15px;color:rgba(26,26,24,0.55);font-style:italic;margin-top:12px">Note: The wobbly background vocals in the Beatles' <strong>"Octopus's Garden"</strong> (Abbey Road, 1969) were created by feeding the Fairchild 660's side-chain with a pulsing LFO. Geoff Emerick's deliberate "abuse" of the unit is now one of the most referenced creative compression effects in recording history.</p>
    </div>
  </section>

  <!-- WHICH FAIRCHILD? ─────────────────────────────────────────────────── -->
  <section id="which-fairchild" style="background:#EDE8E2;padding:80px 0">
    <div class="fc2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">Buyer's Guide</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 10px">Which Fairchild Is Right for You?</h2>
      <p style="font-size:15px;color:rgba(26,26,24,0.55);font-family:'DM Sans',sans-serif;margin:0 0 8px">From $29 plug-in to $29,500 reissue. Every option reviewed honestly.</p>
    </div>
    <div class="fc2-wrap">
      <div class="fc2-guide">

        <div class="fc2-guide-card" style="background:#fff">
          <div class="fc2-gc-tag">In the Box</div>
          <h4>Plug-in Emulation</h4>
          <div class="fc2-gc-price">From $29.99 — UAD, Waves, Acustica</div>
          <p>If your studio is primarily in-the-box, the UAD Fairchild Tube Limiter Collection and Waves PuigChild are genuinely excellent starting points. The UAD emulation in particular is considered the reference-standard plug-in clone — used on major label records daily. Best choice for home studios, bedroom producers, or anyone testing Fairchild compression before investing in hardware.</p>
          <a href="https://vintageking.com/universal-audio-fairchild-tube-limiter-collection" target="_blank">Shop UAD Fairchild →</a>
        </div>

        <div class="fc2-guide-card" style="background:#fff">
          <h4>500 Series Entry Point</h4>
          <div class="fc2-gc-price">Heritage Grandchild 670 — $2,299</div>
          <p>Heritage Audio's 500 Series take on the 670 circuit. Stereo operation in two 500 Series slots, true vari-mu topology, and build quality that takes the Heritage name seriously. Ideal for engineers who want hardware Fairchild compression in a modular, portable format without committing to a full-size unit. Remarkable value at this price point.</p>
          <a href="https://vintageking.com/heritage-audio-grandchild-670-500-series-stereo-compressor" target="_blank">Shop Grandchild 670 →</a>
        </div>

        <div class="fc2-guide-card" style="background:#fff">
          <h4>Full-Size Stereo Hardware</h4>
          <div class="fc2-gc-price">Heritage Herchild 670 — $5,995</div>
          <p>The full stereo 670 format from Heritage Audio — 2U rack, same vari-mu compression principle, DC Threshold Control, sidechain filter, and the kind of build quality that belongs in a professional room. A significant step up from the 500 Series in headroom, transformers, and that full-rack presence. The go-to hardware Fairchild for studios that want the real thing without the vintage maintenance costs.</p>
          <a href="https://vintageking.com/heritage-audio-herchild-670-tube-compressor" target="_blank">Shop Herchild 670 →</a>
        </div>

        <div class="fc2-guide-card" style="background:#fff">
          <div class="fc2-gc-tag" style="background:#1A1A18">Studio Reference</div>
          <h4>UnFairchild 670M II</h4>
          <div class="fc2-gc-price">UnderTone Audio — $9,995</div>
          <p>UnderTone Audio built the UnFairchild from the original schematics with one goal: the most accurate modern reproduction of the 670 circuit possible, built for working studios. Hand-wired, point-to-point construction. Can be specced with NOS 6386 valves. Revered in mastering rooms and high-end mix suites worldwide. This is for engineers who want to own a Fairchild reference and use it in serious production daily.</p>
          <a href="https://vintageking.com/undertone-audio-unfairchild-670m-ii" target="_blank">Shop UnFairchild →</a>
        </div>

        <div class="fc2-guide-card" style="background:#fff">
          <h4>Authentic Reissue — New Production</h4>
          <div class="fc2-gc-price">Fairchild 660: $19,500 / 670: $29,500</div>
          <p>Fairchild Recording Equipment has resumed production of the 660 and 670 built to the original specifications. Not a clone — a reissue. Same circuit topology, same transformer specifications, same control layout as units sold in 1959. For studios and collectors who want the Fairchild name on a unit they can actually own and maintain without worrying about NOS tube scarcity in a 65-year-old chassis.</p>
          <a href="https://vintageking.com/fairchild" target="_blank">Shop New Fairchild →</a>
        </div>

        <div class="fc2-guide-card" style="background:#fff">
          <div class="fc2-gc-tag" style="background:#D4860A">Contact VK</div>
          <h4>Vintage Original</h4>
          <div class="fc2-gc-price">$30,000+ — When Available</div>
          <p>Vintage originals appear rarely and sell immediately. When a working, serviced 660 or 670 comes through Vintage King, it goes to the waitlist first. If owning an original is your goal, the best move is to contact our team now — we know every legitimate original Fairchild that surfaces on the market, and we can advise on condition, servicing costs, and realistic expectations for the 6386 tube situation.</p>
          <a href="https://vintageking.com/fairchild-660-670-compressor-limiter" target="_blank">Join the Waitlist →</a>
        </div>

      </div>
    </div>
  </section>

  <!-- ALTERNATIVES AT VK ───────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="fc2-wide" style="margin-bottom:40px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">Available at Vintage King</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0;line-height:1.2">Every Fairchild Format — One Place</h2>
    </div>
    <div class="fc2-wide">
      <div class="fc2-alts">
        <div class="fc2-alt">
          <div class="fc2-alt-name">Heritage Grandchild 670</div>
          <div class="fc2-alt-price">$2,299</div>
          <div class="fc2-alt-desc">500 Series stereo vari-mu. Two-slot format, true 670-topology, DC threshold control. Best entry into hardware Fairchild compression.</div>
          <a href="https://vintageking.com/heritage-audio-grandchild-670-500-series-stereo-compressor" target="_blank">View at VK →</a>
        </div>
        <div class="fc2-alt">
          <div class="fc2-alt-name">Heritage Herchild 660</div>
          <div class="fc2-alt-price">$2,995</div>
          <div class="fc2-alt-desc">Full 2U mono 660 format. DC Threshold, sidechain filter, premium iron. The Heritage standard in a single-channel rack unit.</div>
          <a href="https://vintageking.com/heritage-audio-herchild-660-tube-compressor" target="_blank">View at VK →</a>
        </div>
        <div class="fc2-alt">
          <div class="fc2-alt-name">Chandler RS660</div>
          <div class="fc2-alt-price">$3,985</div>
          <div class="fc2-alt-desc">Chandler Limited's hybrid of the Fairchild 660 and the EMI RS124 — merging the two compressors used at Abbey Road in the 1960s into one unit.</div>
          <a href="https://vintageking.com/chandler-limited-rs660-compressor-with-stepped-i-o-switches" target="_blank">View at VK →</a>
        </div>
        <div class="fc2-alt">
          <div class="fc2-alt-name">Heritage Herchild 670</div>
          <div class="fc2-alt-price">$5,995</div>
          <div class="fc2-alt-desc">Full stereo 670 in 2U rack format. Step up to full-size hardware — wider headroom, more iron, proper stereo linking. The professional studio choice.</div>
          <a href="https://vintageking.com/heritage-audio-herchild-670-tube-compressor" target="_blank">View at VK →</a>
        </div>
        <div class="fc2-alt">
          <div class="fc2-alt-name">UnFairchild 670M II</div>
          <div class="fc2-alt-price">$9,995</div>
          <div class="fc2-alt-desc">Hand-wired point-to-point. Built to original schematics by UnderTone Audio. The mastering-room standard for modern Fairchild hardware. Available with NOS 6386 valves.</div>
          <a href="https://vintageking.com/undertone-audio-unfairchild-670m-ii" target="_blank">View at VK →</a>
        </div>
        <div class="fc2-alt">
          <div class="fc2-alt-name">Fairchild 660 (New Production)</div>
          <div class="fc2-alt-price">$19,500</div>
          <div class="fc2-alt-desc">Restarted production of the original mono unit. Built to 1959 specifications by Fairchild Recording Equipment. The real name, the real circuit, new construction.</div>
          <a href="https://vintageking.com/fairchild-recording-equipment-660-compressor-limiter" target="_blank">View at VK →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ ──────────────────────────────────────────────────────────────── -->
  <section style="background:#fff;padding:80px 0">
    <div class="fc2-wrap">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">Common Questions</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 40px">Fairchild FAQ</h2>
      <div class="fc2-faq">
        <details>
          <summary>What is the difference between the Fairchild 660 and 670?</summary>
          <p>The 660 is a single-channel mono unit. The 670 is the stereo version — built by literally doubling the entire 660 circuit and adding a matrixing network between the two channels. The 670 contains 20 tubes and 11 transformers vs. the 660's 10 tubes. Critically, the 670 can operate in Left/Right stereo mode or in Mid/Side matrix mode — the latter being why it was designed in the first place, for stereo vinyl disc cutting. Both share the same variable-mu RCA 6386 tube topology and the same six time-constant switch positions.</p>
        </details>
        <details>
          <summary>How many original Fairchilds survive today?</summary>
          <p>Fewer than 1,000 stereo 670 units were ever made, and fewer than 800 mono 660s. Of those, a significant number no longer function or have been cannibalized for parts — especially as the NOS RCA 6386 tubes have become increasingly scarce and expensive. Working, properly serviced originals are rare enough that most studios never encounter one. When one comes to market in good condition, it sells immediately and at premium prices — often $30,000 to $50,000 or more for a verified, serviced 670.</p>
        </details>
        <details>
          <summary>Why does the Fairchild sound so good on vocals?</summary>
          <p>Three reasons work together. First, the 0.2ms attack time (position 1) catches sibilant consonants and harsh transients before they distort or fatigue the ear — but so quickly the ear never registers the reduction as clamping. Second, the variable-mu soft knee means the ratio rises gradually from near-unity, so the compression sounds like tonal focus rather than control. Third, the signal path is an exceptionally clean transformer-coupled tube stage — one that adds a subtle three-dimensionality that engineers describe as "silk" or "presence." Run a vocal through a working Fairchild and the comparison is immediate.</p>
        </details>
        <details>
          <summary>What is a variable-mu compressor and why does it matter?</summary>
          <p>Variable-mu compressors use vacuum tubes whose amplification factor (mu) decreases as the control voltage increases. Unlike a VCA compressor (which uses a voltage-controlled amplifier with a defined ratio) or an optical compressor (which uses a light element), the Fairchild's tubes physically change their behavior based on the signal hitting them. The result is a compression curve that starts near 1:1 for quiet passages and rises to 20:1 for loud peaks — entirely program-dependent. This is why it sounds "musical" rather than mechanical: the compressor responds to the music rather than applying a fixed rule to it.</p>
        </details>
        <details>
          <summary>What is the 6386 tube and why is it getting scarce?</summary>
          <p>The RCA 6386 is a remote-cutoff dual-triode tube used as the gain cell in the Fairchild. RCA discontinued production decades ago. The new-old-stock (NOS) supply has been shrinking for years as Fairchild owners, cloners, and servicing engineers work through the remaining stock. JJ Electronic now makes a modern 6386 substitute, but the debate over whether it sounds identical to NOS continues. High-quality NOS 6386 tubes now fetch serious prices individually. For anyone buying a vintage Fairchild, the tube supply question is a real part of the ownership conversation — and one of the reasons new production reissues like the Fairchild RE units are attractive despite the price.</p>
        </details>
        <details>
          <summary>Can the Fairchild be used as a mix bus compressor?</summary>
          <p>Yes, but carefully. The Fairchild was designed for peak control and mastering, not the kind of mix-bus punch shaping that 1176s and SSL G-bus compressors are used for. Its 0.2ms minimum attack is extremely fast — which means on a full mix with heavy bass transients, it can reduce punch if you're not careful. Where it excels on the mix bus is as a "glue" processor: subtle leveling with no audible compression, just the transformer-tube signal path adding coherence and focus. Many engineers run minimal or no gain reduction (watching the meter idle near zero) and use it purely for the color. Position 1 is still usually the right starting point.</p>
        </details>
      </div>
    </div>
  </section>

  <!-- EXPLORE MORE ─────────────────────────────────────────────────────── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div class="fc2-wide" style="margin-bottom:36px">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:12px">More From Vintage King</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;margin:0">Continue Exploring</h2>
    </div>
    <div class="fc2-wide">
      <div class="fc2-more">
        <div class="fc2-more-card">
          <span>Hall of Fame</span>
          <h4>Neve 1073 — The Definitive Guide</h4>
          <p>How the 1073 mic preamp became the most cloned circuit in recording history, and every version available at VK.</p>
          <a href="neve-1073-guide-v2.html">Read the Guide →</a>
        </div>
        <div class="fc2-more-card">
          <span>Audio Consulting</span>
          <h4>Talk to a VK Expert</h4>
          <p>Not sure which Fairchild path makes sense for your room? Our consultants know every unit in stock and can help you make the right call.</p>
          <a href="audio-consultants.html">Meet the Team →</a>
        </div>
        <div class="fc2-more-card">
          <span>Pro Audio Hall of Fame</span>
          <h4>More Hall of Fame Gear</h4>
          <p>The LA-2A, Neumann U47, UREI 1176, Telefunken 251 — each one a legend. Each one with its own deep history at Vintage King.</p>
          <a href="https://vintageking.com/pro-audio-hall-of-fame" target="_blank">View Hall of Fame →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA SECTION ──────────────────────────────────────────────────────── -->
  <section style="background:#EDE8E2;padding:80px 48px">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <div style="font-size:12px;letter-spacing:0.2em;text-transform:uppercase;color:#C0392B;font-family:'DM Sans',sans-serif;margin-bottom:16px">Vintage King Audio</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#1A1A18;margin:0 0 20px;line-height:1.2">Ready to Find Your Fairchild?</h2>
      <p style="font-size:16px;color:#3A3A38;line-height:1.7;margin:0 0 36px">Whether you want the UAD plug-in or a vintage original, our team has handled more Fairchild transactions than anyone else in the business. We know the market, we know the units, and we know exactly which one fits your room.</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a href="https://vintageking.com/fairchild-660-670-compressor-limiter" target="_blank" style="background:#C0392B;color:#fff;padding:16px 36px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;text-decoration:none;letter-spacing:0.04em">Shop All Fairchild</a>
        <a href="audio-consultants.html" style="background:transparent;color:#1A1A18;border:1px solid rgba(26,26,24,0.35);padding:16px 28px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;text-decoration:none">Talk to an Expert</a>
      </div>
    </div>
  </section>

  <!-- STICKY SHOP BAR ──────────────────────────────────────────────────── -->
  <div class="fc2-stick" id="fc2-stick">
    <div>
      <div class="fc2-stick-title">Fairchild 660 / 670</div>
      <div class="fc2-stick-sub">Hardware from $2,299 · Plug-ins from $29.99 · New production reissues in stock</div>
    </div>
    <div class="fc2-stick-actions">
      <a href="https://vintageking.com/fairchild-660-670-compressor-limiter" target="_blank" class="fc2-stick-cta">Shop at Vintage King</a>
      <a href="audio-consultants.html" class="fc2-stick-ghost">Ask an Expert</a>
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
