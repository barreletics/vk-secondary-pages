"""neumann-u67.html — Hall of Fame editorial guide to the Neumann U67."""
import re

INLINE_JS = """\
<script>
  (function() {
    var p = 'neumann-u67';
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

SLUG  = "neumann-u67"
TITLE = "Neumann U67 — The Sound of Tomorrow | Vintage King Audio"
META  = "The definitive guide to the Neumann U67 tube condenser microphone. History, the K67 capsule, EF86 tube, every variant from M269 to SM69, and every version at Vintage King."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Neumann U67 — The Sound of Tomorrow",
      "description": "The definitive guide to the Neumann U67 tube condenser microphone. History, engineering, variants, the studios and records that made it legendary, and every version at Vintage King.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "Neumann U67 Large Diaphragm Tube Condenser Microphone",
      "brand": {"@type": "Brand", "name": "Neumann"},
      "description": "Large-diaphragm tube condenser microphone with K67 capsule, EF86 tube, three polar patterns, -10dB pad, and bass rolloff. The successor to the U47.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "2599",
        "highPrice": "12000",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between the U67 and U87?",
          "acceptedAnswer": {"@type": "Answer", "text": "Both use the K67 capsule, but the U67 is tube-powered (EF86 vacuum tube) while the U87 uses a FET transistor circuit. The U67 has a warmer, richer harmonic character with tube saturation. The U87 is cleaner, more neutral, and does not require a separate power supply. The U67 was made 1960-1971; the U87 from 1967 to present."}
        },
        {
          "@type": "Question",
          "name": "Is the Neumann U67 reissue the same as the original?",
          "acceptedAnswer": {"@type": "Answer", "text": "The 2018 reissue is a historically accurate replica featuring the same K67 capsule and EF86 tube. Modern and vintage parts are interchangeable between the two. The reissue was manufactured to original specifications using many of the same production processes."}
        },
        {
          "@type": "Question",
          "name": "What is the Neumann U67 best for?",
          "acceptedAnswer": {"@type": "Answer", "text": "The U67 is considered one of the most versatile studio microphones ever made. It excels on vocals, drum overheads, acoustic guitar, electric guitar amps, strings, and brass. Its slightly forward midrange and rich texture make it a go-to for any source that benefits from warmth and character."}
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
  <a href="neumann-u47.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Neumann U47</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Neumann U67</span>
</nav>
"""

PAGE_BODY = """\
<div id="neumann-u67" class="page active">
  <div id="nav-neumann-u67"></div>

  <style>
    .n67-wrap { max-width:1160px;margin:0 auto;padding:0 40px }
    .n67-eyebrow { font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;margin-bottom:14px }
    .n67-hero { background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:560px;overflow:hidden }
    .n67-hero-text { padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center }
    .n67-hero-img { display:flex;align-items:center;justify-content:center;padding:32px;background:#fff;position:relative }
    .n67-hero-img img { width:100%;max-height:460px;object-fit:contain;display:block }
    .n67-hero-caption { position:absolute;bottom:12px;right:16px;font-size:11px;color:rgba(26,26,24,0.35);font-family:'DM Sans',sans-serif }
    .n67-stats { display:grid;grid-template-columns:repeat(6,1fr);gap:1px;background:rgba(26,26,24,0.08);border-top:1px solid rgba(26,26,24,0.08);border-bottom:1px solid rgba(26,26,24,0.08) }
    .n67-stat { background:#fff;padding:28px 20px;text-align:center }
    .n67-stat-num { font-family:'DM Sans',sans-serif;font-size:28px;font-weight:700;color:#1A1A18;line-height:1.1 }
    .n67-stat-label { font-family:'DM Sans',sans-serif;font-size:11px;color:rgba(26,26,24,0.5);margin-top:6px;letter-spacing:0.04em }
    .n67-section { padding:64px 0 }
    .n67-section-off { background:var(--off-white,#F7F5F2) }
    .n67-section-white { background:#fff }
    .n67-h2 { font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 8px;line-height:1.15 }
    .n67-sub { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.55);margin:0 0 40px;line-height:1.6;max-width:680px }
    .n67-body { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.7);line-height:1.75;max-width:760px;margin:0 0 24px }
    .n67-quote { border-left:3px solid #D4860A;padding:24px 0 24px 32px;margin:40px 0 }
    .n67-quote p { font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1A1A18;line-height:1.45;margin:0 0 12px }
    .n67-quote cite { font-family:'DM Sans',sans-serif;font-size:13px;font-style:normal;color:#D4860A;font-weight:600 }
    .n67-tl { display:grid;grid-template-columns:140px 1fr;gap:0;margin-bottom:2px }
    .n67-tl-yr { font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;color:#D4860A;padding:4px 12px 4px 0;border-right:2px solid #D4860A;text-align:right;letter-spacing:0.06em }
    .n67-tl-body { padding:0 0 28px 24px }
    .n67-tl-title { font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:4px }
    .n67-tl-body .n67-tl-tag { display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:0;margin-bottom:6px;color:#D4860A }
    .n67-tl-body p { font-size:13px;color:rgba(26,26,24,0.6);line-height:1.65;margin:0 }
    .n67-feat-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;margin-bottom:40px }
    .n67-feat { background:#fff;padding:24px }
    .n67-feat h4 { font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1A1A18;margin:0 0 6px }
    .n67-feat p { font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6;margin:0 }
    .n67-gc-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .n67-gc { background:#fff;padding:24px;display:flex;flex-direction:column }
    .n67-gc-tag { display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:0 0 10px 0;color:#D4860A }
    .n67-gc h4 { font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#1A1A18;margin:0 0 6px }
    .n67-gc-price { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;color:#1A1A18;margin:0 0 8px }
    .n67-gc p { font-size:13px;color:#3A3A38;line-height:1.6;margin:0 0 14px;flex:1 }
    .n67-gc a { font-size:13px;font-weight:600;color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.3);margin-top:auto }
    .n67-gc a:hover { border-bottom-color:#C0392B }
    .n67-ra { font-family:'DM Sans',sans-serif;font-size:13px;color:rgba(26,26,24,0.65);line-height:1.65;margin-bottom:8px }
    .n67-ra a { color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.25) }
    .n67-faq details { margin-bottom:2px }
    .n67-faq summary { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18;padding:18px 24px;background:#fff;cursor:pointer;list-style:none;border-bottom:1px solid rgba(26,26,24,0.06) }
    .n67-faq summary::-webkit-details-marker { display:none }
    .n67-faq summary::after { content:'+';float:right;font-size:18px;font-weight:400;color:rgba(26,26,24,0.3) }
    .n67-faq details[open] summary::after { content:'\\2212' }
    .n67-faq .n67-faq-a { font-family:'DM Sans',sans-serif;font-size:14px;color:rgba(26,26,24,0.65);line-height:1.7;padding:16px 24px 24px;background:#fff }
    .n67-stick { position:fixed;bottom:0;left:0;right:0;z-index:500;background:#1A1A18;color:#FDFCFB;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;font-family:'DM Sans',sans-serif;transform:translateY(100%);transition:transform 0.3s }
    .n67-stick.visible { transform:translateY(0) }
    .n67-stick-title { font-size:15px;font-weight:600 }
    .n67-stick-sub { font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }
    .n67-stick-actions { display:flex;gap:10px;align-items:center }
    .n67-stick-cta { background:#C0392B;color:#fff;padding:10px 22px;font-size:13px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em }
    .n67-stick-ghost { color:rgba(255,255,255,0.7);font-size:13px;font-weight:500;text-decoration:none;padding:10px 16px;border:1px solid rgba(255,255,255,0.2);border-radius:2px }

    /* dark capsule section */
    .n67-dark { background:#1A1A18;padding:56px 64px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center }
    .n67-dark h3 { font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#FDFCFB;margin:0 0 16px }
    .n67-dark p { font-size:15px;color:rgba(253,252,251,0.7);line-height:1.75;margin-bottom:14px }
    .n67-dark p:last-child { margin-bottom:0 }
    .n67-dark-visual { background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:3px;padding:32px;text-align:center }
    .n67-dark-label { font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(253,252,251,0.35);margin-top:16px }
    .n67-dark-spec { display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px;text-align:left }
    .n67-dark-spec dt { font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:rgba(253,252,251,0.4);margin-bottom:2px }
    .n67-dark-spec dd { font-size:14px;font-weight:600;color:#D4860A;margin:0 0 12px }

    /* buyer guide images */
    .n67-gc-img { width:100%;height:160px;object-fit:contain;background:#F7F5F2;border-radius:2px;margin-bottom:12px }
  </style>
  <script>
    (function(){
      var bar=null;
      window.addEventListener('scroll',function(){
        if(!bar)bar=document.getElementById('n67-stick');
        if(!bar)return;
        bar.classList.toggle('visible',window.scrollY>600);
      });
    })();
  </script>

  <!-- ── HERO ── -->
  <section class="n67-hero">
    <div class="n67-hero-text">
      <div class="n67-eyebrow">Pro Audio Hall of Fame</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 20px">The Neumann U67</h1>
      <p style="font-size:17px;color:rgba(26,26,24,0.6);line-height:1.65;max-width:460px;margin:0 0 28px">The "Sound of Tomorrow." Neumann's successor to the U47 — a tube mic so advanced its K67 capsule is still in production over 60 years later.</p>
      <a href="https://vintageking.com/neumann-u67-tube-microphone" target="_blank" style="display:inline-block;background:#C0392B;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em;align-self:flex-start">Shop U67 Models</a>
    </div>
    <div class="n67-hero-img">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Microphone_Neumann_U-67_%281953%29.jpg/500px-Microphone_Neumann_U-67_%281953%29.jpg" alt="Vintage Neumann U67 tube condenser microphone" loading="lazy">
      <span class="n67-hero-caption">Photo: Goldfinger / Wikimedia CC BY-SA 3.0</span>
    </div>
  </section>

  <!-- ── STATS ── -->
  <div class="n67-stats">
    <div class="n67-stat"><div class="n67-stat-num">1960</div><div class="n67-stat-label">First production</div></div>
    <div class="n67-stat"><div class="n67-stat-num">10,000+</div><div class="n67-stat-label">Units built</div></div>
    <div class="n67-stat"><div class="n67-stat-num">3</div><div class="n67-stat-label">Polar patterns</div></div>
    <div class="n67-stat"><div class="n67-stat-num">K67</div><div class="n67-stat-label">Capsule (still made)</div></div>
    <div class="n67-stat"><div class="n67-stat-num">EF86</div><div class="n67-stat-label">Vacuum tube</div></div>
    <div class="n67-stat"><div class="n67-stat-num">60+</div><div class="n67-stat-label">Years of influence</div></div>
  </div>

  <!-- ── HISTORY ── -->
  <section class="n67-section n67-section-white">
    <div class="n67-wrap">
      <div class="n67-eyebrow">History</div>
      <h2 class="n67-h2">The End is the Beginning</h2>
      <p class="n67-body">In 1958, Georg Neumann GmbH received word that Telefunken would no longer manufacture the VF14 steel tube — the heart of the U47. Neumann placed their third and final order for a batch of tubes, and lead engineer Dr.-Ing. Gerhart Bore began to design the successor to a microphone still revered as one of the top vocal mics of all time.</p>
      <p class="n67-body">A new look. A new sound. A new decade. The result was the U60, introduced in 1960 and later renamed the U67 to show continuity with the U47. It was born out of necessity — but it could hardly be improved upon. Its look and sound have been copied endlessly, but the original stands apart as a piece of immortal gear.</p>

      <div class="n67-quote">
        <p>"The U67 is probably the best sounding all-around studio workhorse mic ever made. Super versatile, it sounds amazing on any source. Drum overheads, rock vocals, female vocals, and acoustic guitars are standouts but really there's nothing it can't handle well."</p>
        <cite>Ryan McGuire, President, Vintage King</cite>
      </div>
    </div>
  </section>

  <!-- ── ENGINEERING ADVANCES ── -->
  <section class="n67-section n67-section-off">
    <div class="n67-wrap">
      <div class="n67-eyebrow">Engineering</div>
      <h2 class="n67-h2">Nine Advances in One Microphone</h2>
      <p class="n67-sub">Every element was a synthesis — each improvement relied on and enabled the others.</p>

      <div class="n67-feat-grid">
        <div class="n67-feat"><h4>K67 dual capsule</h4><p>Split backplate replacing single backplate. So advanced it is still produced and used in the U67 and U87 over 60 years later.</p></div>
        <div class="n67-feat"><h4>Mylar diaphragm</h4><p>New material replacing PVC. More consistent, more durable, better frequency response.</p></div>
        <div class="n67-feat"><h4>Three polar patterns</h4><p>Figure-eight added to omni and cardioid. The split backplate made accurate figure-eight possible.</p></div>
        <div class="n67-feat"><h4>EF86 miniature tube</h4><p>Smaller glass vacuum tube replacing the large steel VF14. Allowed the slimmer, tapered body.</p></div>
        <div class="n67-feat"><h4>Tapered body</h4><p>Patented design — tooled on new lathes. Head grille reduced capsule resonance from both directions.</p></div>
        <div class="n67-feat"><h4">-10 dB pad and filter</h4><p>Built-in pad protects the capsule. Internal bass rolloff filter negates proximity effect.</p></div>
        <div class="n67-feat"><h4>Brass tension ring</h4><p>Diaphragm secured mechanically instead of glue. More reliable, more serviceable.</p></div>
        <div class="n67-feat"><h4>Tool-free body</h4><p>Opens without screws for quick servicing during sessions. Same approach used on the ELA-M 251.</p></div>
        <div class="n67-feat"><h4>Angled grille housing</h4><p>Replaced cylindrical grille. Further reduced diffraction and resonance around the capsule.</p></div>
      </div>
    </div>
  </section>

  <!-- ── K67 CAPSULE — DARK SECTION ── -->
  <div class="n67-dark">
    <div>
      <h3>The K67 Capsule — Why the U67 Still Matters</h3>
      <p>The K67 was a dual-capsule, split-backplate design using Mylar diaphragms secured by a brass tension ring instead of glue. This was revolutionary in 1960 — it created an accurate figure-eight polar pattern, improved durability, and allowed the capsule to be serviced without destroying it.</p>
      <p>So advanced was this design that Neumann still produces the K67 today. It powers both the modern U67 reissue and the U87 — the two most important large-diaphragm microphones in professional recording. Numerous manufacturers have tried to replicate the K67's sound; none have fully succeeded.</p>
      <p>The body shape was equally groundbreaking. The tapered head grille reduced capsule resonance from both directions. Neumann patented the design — it remains one of the most recognizable silhouettes in audio.</p>
    </div>
    <div class="n67-dark-visual">
      <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#D4860A;margin-bottom:20px">K67 Capsule</div>
      <dl class="n67-dark-spec">
        <dt>Diaphragm</dt><dd>Dual, split backplate</dd>
        <dt>Material</dt><dd>Mylar (not PVC)</dd>
        <dt>Tensioning</dt><dd>Brass ring (not glue)</dd>
        <dt>Patterns</dt><dd>Omni / Cardioid / Fig-8</dd>
        <dt>Tube</dt><dd>EF86 miniature</dd>
        <dt>Pad</dt><dd>-10 dB built-in</dd>
        <dt>Still in production</dt><dd>Yes — since 1960</dd>
        <dt>Used in</dt><dd>U67, U87, SM69</dd>
      </dl>
      <div class="n67-dark-label">60+ years of continuous production</div>
    </div>
  </div>

  <!-- ── VARIANTS TIMELINE ── -->
  <section class="n67-section n67-section-white">
    <div class="n67-wrap">
      <div class="n67-eyebrow">Variants</div>
      <h2 class="n67-h2">The U67 Family</h2>
      <p class="n67-sub">From the original to its cousins, stereo versions, and the modern reissue.</p>

      <div class="n67-tl">
        <div class="n67-tl-yr">1960–71</div>
        <div class="n67-tl-body">
          <div class="n67-tl-tag">Neumann U67</div>
          <div class="n67-tl-title">The Original</div>
          <p>~10,000 units produced. K67 capsule, EF86 tube, three polar patterns, -10 dB pad, bass rolloff. Tapered patented body. Originally named U60, renamed U67 to show lineage from the U47. Another 400 were made in 1992.</p>
        </div>
      </div>
      <div class="n67-tl">
        <div class="n67-tl-yr">1962–73</div>
        <div class="n67-tl-body">
          <div class="n67-tl-tag">Telefunken M269</div>
          <div class="n67-tl-title">German Broadcast Variant</div>
          <p>Tuchel connector. AC701(k) tube for European broadcast standards. Remotely switchable, continuously variable polar pattern (like the M49). Different tonal character from the U67 due to the Telefunken tube.</p>
        </div>
      </div>
      <div class="n67-tl">
        <div class="n67-tl-yr">1966–76</div>
        <div class="n67-tl-body">
          <div class="n67-tl-tag">Telefunken M367</div>
          <div class="n67-tl-title">French Broadcast Variant</div>
          <p>Sogie connector. AC701(k) tube. Same three-position pattern switch as the U67. Similar to M269 but with fixed pattern selection rather than continuous remote switching.</p>
        </div>
      </div>
      <div class="n67-tl">
        <div class="n67-tl-yr">1964–73</div>
        <div class="n67-tl-body">
          <div class="n67-tl-tag">Neumann SM69</div>
          <div class="n67-tl-title">Stereo Version</div>
          <p>Two K67 capsules in a single body. Top capsule rotates 270 degrees. Nine polar patterns per capsule, selectable on PSU. Pair of AC701(k) tubes. FET version followed in 1970.</p>
        </div>
      </div>
      <div class="n67-tl">
        <div class="n67-tl-yr">2018</div>
        <div class="n67-tl-body">
          <div class="n67-tl-tag">Neumann U67 Reissue</div>
          <div class="n67-tl-title">Historically Accurate Replica</div>
          <p>K67 capsule and EF86 tube, manufactured to original specs. Parts are interchangeable with vintage originals. The legend returns — in continuous production.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── RECORDS ── -->
  <section class="n67-section n67-section-off">
    <div class="n67-wrap">
      <div class="n67-eyebrow">Records It Made</div>
      <h2 class="n67-h2">The U67 on Iconic Recordings</h2>
      <p class="n67-sub">Countless examples, but a few should suffice.</p>

      <div class="n67-feat-grid">
        <div class="n67-feat"><h4>Led Zeppelin I</h4><p>Jimmy Page on acoustic guitar, John Bonham with the Glyn Johns drum technique. The U67 captured both.</p></div>
        <div class="n67-feat"><h4>"My Girl" — The Temptations</h4><p>David Ruffin's vocal through a U67 at Studio A, Hitsville USA. One of Motown's defining sounds.</p></div>
        <div class="n67-feat"><h4>"Hey Jude" — The Beatles</h4><p>Paul McCartney's lead vocal. The U67 was a staple at Abbey Road Studios throughout the 1960s.</p></div>
        <div class="n67-feat"><h4>"Highway Star" — Deep Purple</h4><p>Ian Gillan's scorching vocal performance captured through the U67's three polar patterns.</p></div>
        <div class="n67-feat"><h4>Abbey Road Studios</h4><p>The U67 became EMI's go-to large diaphragm mic after the U47, used across hundreds of sessions through the 1960s and 70s.</p></div>
        <div class="n67-feat"><h4>10,000 Units Built</h4><p>By end of production in 1971, the U67 was the large diaphragm tube mic of choice for audio professionals worldwide.</p></div>
      </div>
    </div>
  </section>

  <!-- ── BUYER GUIDE ── -->
  <section class="n67-section n67-section-white">
    <div class="n67-wrap">
      <div class="n67-eyebrow">Which U67 Is Right for You?</div>
      <h2 class="n67-h2">Every U67 at Vintage King</h2>
      <p class="n67-sub">The original, the reissue, and modern alternatives inspired by the K67 capsule.</p>

      <div class="n67-gc-grid">
        <div class="n67-gc">
          <img class="n67-gc-img" src="https://vintageking.com/media/catalog/product/n/e/neumann-u67_97358_1.jpg" alt="Neumann U67 Reissue" loading="lazy">
          <div class="n67-gc-tag">Official reissue</div>
          <h4>Neumann U67 Reissue</h4>
          <div class="n67-gc-price">$8,299</div>
          <p>Historically accurate replica. K67 capsule, EF86 tube, interchangeable parts with vintage originals. Includes Z 48 suspension, NU 67 V power supply, UC 5 cable, vintage-style case.</p>
          <a href="https://vintageking.com/neumann-u67-microphone-reissue" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
        <div class="n67-gc">
          <img class="n67-gc-img" src="https://vintageking.com/media/catalog/product/w/u/wunder-cm-67-2.jpg" alt="Wunder Audio CM67 S" loading="lazy">
          <div class="n67-gc-tag">Alternative</div>
          <h4>Wunder Audio CM67 S</h4>
          <div class="n67-gc-price">$4,695</div>
          <p>Classic warmth with Phillips EF86 tube and white porcelain ringed K67-style capsule. Upgraded long-term performance. Perfect for drums, acoustic guitar, electric guitar.</p>
          <a href="https://vintageking.com/wunder-audio-cm67-s" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
        <div class="n67-gc">
          <img class="n67-gc-img" src="https://vintageking.com/media/catalog/product/p/e/peluso_p-67_set.jpg" alt="Peluso P-67" loading="lazy">
          <div class="n67-gc-tag">Budget alternative</div>
          <h4>Peluso P-67</h4>
          <div class="n67-gc-price">$2,599</div>
          <p>Based on response charts from a new 1960s U67. Dual 34mm diaphragms, low-frequency rolloff, -10 dB pad, nine polar patterns. Accurate at a sensible price.</p>
          <a href="https://vintageking.com/peluso-microphone-lab-p-67" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── FURTHER READING ── -->
  <section class="n67-section n67-section-off">
    <div class="n67-wrap">
      <div class="n67-eyebrow">Further Reading</div>
      <h2 class="n67-h2">From the Vintage King Blog</h2>
      <div style="margin-top:24px">
        <p class="n67-ra"><a href="https://vintageking.com/blog/2018/05/neumann-u67-reissue/" target="_blank">First Listen: Neumann U67 Reissue &rarr;</a></p>
        <p class="n67-ra"><a href="https://vintageking.com/blog/2018/01/neumann-u67/" target="_blank">The Legend Returns: Neumann Revives the U67 &rarr;</a></p>
        <p class="n67-ra"><a href="https://vintageking.com/blog/2017/12/how-to-get-a-big-vocal-sound/" target="_blank">How to Get a Big Vocal Sound &rarr;</a></p>
        <p class="n67-ra"><a href="https://vintageking.com/blog/2016/02/buying-vintage-mics/" target="_blank">Vintage King's Guide to Buying Vintage Microphones &rarr;</a></p>
      </div>
    </div>
  </section>

  <!-- ── FAQ ── -->
  <section class="n67-section n67-section-white">
    <div class="n67-wrap">
      <div class="n67-eyebrow">Frequently Asked Questions</div>
      <h2 class="n67-h2" style="margin-bottom:32px">U67 FAQ</h2>

      <div class="n67-faq">
        <details><summary>What is the difference between the U67 and U87?</summary><div class="n67-faq-a">Both use the K67 capsule, but the U67 is tube-powered (EF86) while the U87 uses a FET transistor. The U67 has a warmer, richer harmonic character with tube saturation. The U87 is cleaner and more neutral. The U67 requires a separate power supply; the U87 runs on phantom power.</div></details>
        <details><summary>Is the 2018 reissue the same as the original?</summary><div class="n67-faq-a">Yes, to a remarkable degree. The reissue uses the same K67 capsule, the same EF86 tube, and was manufactured to original specifications. Modern and vintage parts are interchangeable. Neumann went to extraordinary lengths to ensure authenticity.</div></details>
        <details><summary>What is the U67 best for?</summary><div class="n67-faq-a">The U67 is considered one of the most versatile studio microphones ever made. It excels on vocals (all types), drum overheads, acoustic guitar, electric guitar amps, strings, brass, and woodwinds. Its slightly forward midrange and rich texture make it outstanding on virtually any source.</div></details>
        <details><summary>U67 vs M269 vs M367 — what is the difference?</summary><div class="n67-faq-a">All three share the same basic design. The M269 (Germany) uses an AC701(k) tube and has continuously variable remote pattern switching like the M49. The M367 (France) also uses the AC701(k) but has the same 3-position switch as the U67. Both have a different tonal character due to the Telefunken tube.</div></details>
        <details><summary>How much is a vintage U67 worth?</summary><div class="n67-faq-a">Vintage U67s in excellent condition typically range from $8,000 to $12,000+ depending on condition, year, and whether all original components are present. The M269 and M367 variants can command similar or higher prices. Contact Vintage King's Audio Consultants for current availability and pricing on vintage units.</div></details>
      </div>
    </div>
  </section>

  <!-- STICKY BAR -->
  <div class="n67-stick" id="n67-stick">
    <div>
      <div class="n67-stick-title">Neumann U67</div>
      <div class="n67-stick-sub">Reissue $8,299 · Alternatives from $2,599 · Vintage by request</div>
    </div>
    <div class="n67-stick-actions">
      <a href="https://vintageking.com/neumann-u67-tube-microphone" target="_blank" class="n67-stick-cta">Shop at Vintage King</a>
      <a href="audio-consultants.html" class="n67-stick-ghost">Ask an Expert</a>
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
    head += '  <style id="vk-standalone-patch">.page{display:block!important}</style>\n'

    return (
        head + "\n</head>\n<body>\n"
        + CHROME + nav_tpl + foot_tpl
        + JSON_LD + PAGE_BODY
        + js_nav + INLINE_JS
        + "</body>\n</html>\n"
    )
