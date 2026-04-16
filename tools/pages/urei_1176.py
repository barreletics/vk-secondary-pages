"""urei-1176.html — Hall of Fame editorial guide to the UREI / Universal Audio 1176."""
import re

INLINE_JS = """\
<script>
  (function() {
    var p = 'urei-1176';
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

SLUG  = "urei-1176"
TITLE = "UREI / Universal Audio 1176 — The FET Compressor That Changed Everything | Vintage King Audio"
META  = "The definitive guide to the UREI and Universal Audio 1176 FET compressor-limiter. Every revision from A to H, the engineers who swear by it, and every version available at Vintage King."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "UREI / Universal Audio 1176 — The FET Compressor That Changed Everything",
      "description": "The definitive guide to the 1176 FET compressor-limiter. Every revision from Bluestripe to Silverface, engineering, the studios and engineers who rely on it, and every version at Vintage King.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "UREI / Universal Audio 1176LN Compressor-Limiter",
      "brand": {"@type": "Brand", "name": "Universal Audio"},
      "description": "FET-based peak limiter with attack times as fast as 20 microseconds. The most-used compressor in professional recording.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "29.99",
        "highPrice": "6500",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between 1176 revisions?",
          "acceptedAnswer": {"@type": "Answer", "text": "There are 9 major revisions lettered A through H (including A/B). Bluestripes (A, A/B, B) are edgy with more noise and distortion. Low-Noise Blackfaces (C, D, E) are the most revered — modern reissues are based on these. Rev F added a push-pull output for more gain. Revs G and H replaced the input transformer with an op-amp for a cleaner sound."}
        },
        {
          "@type": "Question",
          "name": "What is 'All Buttons In' mode on the 1176?",
          "acceptedAnswer": {"@type": "Answer", "text": "Pressing all four ratio buttons simultaneously engages a unique compression behavior where the ratio hovers around 12:1 to 20:1 with increased distortion and a distinctive pumping effect. Engineers use it on drums, room mics, and vocals for aggressive, characterful compression."}
        },
        {
          "@type": "Question",
          "name": "Which 1176 revision sounds best?",
          "acceptedAnswer": {"@type": "Answer", "text": "Revisions C, D, and E (the first Low-Noise Blackfaces) are generally considered the most desirable. They have the classic 1176 character with a lower noise floor. The modern Universal Audio reissue is based primarily on these versions."}
        },
        {
          "@type": "Question",
          "name": "How fast is the 1176 attack?",
          "acceptedAnswer": {"@type": "Answer", "text": "The 1176 has an attack time as fast as 20 microseconds — one of the fastest of any compressor ever made. This allows it to catch even the sharpest transients, making it ideal for vocals, drums, bass, and any source that needs tight, controlled dynamics."}
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
  <a href="fairchild-660-670.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Fairchild 660/670</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">UREI 1176</span>
</nav>
"""

PAGE_BODY = """\
<div id="urei-1176" class="page active">
  <div id="nav-urei-1176"></div>

  <style>
    /* ─── UREI 1176 HOF page ─────────────────────────────────────────── */
    .u76-wrap { max-width:1160px;margin:0 auto;padding:0 40px }
    .u76-eyebrow { font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;margin-bottom:14px }

    /* hero */
    .u76-hero { background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:560px;overflow:hidden }
    .u76-hero-text { padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center }
    .u76-hero-img { display:flex;align-items:center;justify-content:center;padding:32px;background:#fff;position:relative }
    .u76-hero-img img { width:100%;max-height:460px;object-fit:contain;display:block }
    .u76-hero-caption { position:absolute;bottom:12px;right:16px;font-size:11px;color:rgba(26,26,24,0.35);font-family:'DM Sans',sans-serif }

    /* stats */
    .u76-stats { display:grid;grid-template-columns:repeat(6,1fr);gap:1px;background:rgba(26,26,24,0.08);border-top:1px solid rgba(26,26,24,0.08);border-bottom:1px solid rgba(26,26,24,0.08) }
    .u76-stat { background:#fff;padding:28px 20px;text-align:center }
    .u76-stat-num { font-family:'DM Sans',sans-serif;font-size:28px;font-weight:700;color:#1A1A18;line-height:1.1 }
    .u76-stat-label { font-family:'DM Sans',sans-serif;font-size:11px;color:rgba(26,26,24,0.5);margin-top:6px;letter-spacing:0.04em }

    /* sections */
    .u76-section { padding:64px 0 }
    .u76-section-off { background:var(--off-white,#F7F5F2) }
    .u76-section-white { background:#fff }
    .u76-section-dark { background:#1A1A18;color:#FDFCFB }

    .u76-h2 { font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 8px;line-height:1.15 }
    .u76-sub { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.55);margin:0 0 40px;line-height:1.6;max-width:680px }
    .u76-body { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.7);line-height:1.75;max-width:760px;margin:0 0 24px }

    /* timeline */
    .u76-tl { display:grid;grid-template-columns:140px 1fr;gap:0;margin-bottom:2px }
    .u76-tl-yr { font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;color:#D4860A;padding:4px 12px 4px 0;border-right:2px solid #D4860A;text-align:right;letter-spacing:0.06em }
    .u76-tl-body { padding:0 0 28px 24px }
    .u76-tl-title { font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:4px }
    .u76-tl-body .u76-tl-tag { display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:0;margin-bottom:6px;color:#D4860A }
    .u76-tl-body p { font-size:13px;color:rgba(26,26,24,0.6);line-height:1.65;margin:0 }

    /* revision cards */
    .u76-rev-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;margin-bottom:40px }
    .u76-rev { background:#fff;padding:28px 24px }
    .u76-rev-name { font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:4px }
    .u76-rev-serial { font-size:11px;color:rgba(26,26,24,0.4);letter-spacing:0.04em;margin-bottom:8px }
    .u76-rev p { font-size:13px;color:rgba(26,26,24,0.6);line-height:1.6;margin:0 }

    /* spec table */
    .u76-spec-table { width:100%;border-collapse:collapse;font-family:'DM Sans',sans-serif;font-size:13px;margin-bottom:32px }
    .u76-spec-table th { text-align:left;padding:12px 16px;background:rgba(26,26,24,0.04);color:rgba(26,26,24,0.5);font-weight:600;letter-spacing:0.04em;font-size:11px;text-transform:uppercase;border-bottom:1px solid rgba(26,26,24,0.08) }
    .u76-spec-table td { padding:12px 16px;border-bottom:1px solid rgba(26,26,24,0.06);color:#1A1A18 }
    .u76-spec-table tr:last-child td { border-bottom:none }

    /* pull quote */
    .u76-quote { border-left:3px solid #D4860A;padding:24px 0 24px 32px;margin:40px 0 }
    .u76-quote p { font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1A1A18;line-height:1.45;margin:0 0 12px }
    .u76-quote cite { font-family:'DM Sans',sans-serif;font-size:13px;font-style:normal;color:#D4860A;font-weight:600 }

    /* buyer guide */
    .u76-gc-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .u76-gc { background:#fff;padding:24px 24px 24px;display:flex;flex-direction:column }
    .u76-gc-tag { display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:0 0 10px 0;color:#D4860A }
    .u76-gc h4 { font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#1A1A18;margin:0 0 6px }
    .u76-gc-price { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;color:#1A1A18;margin:0 0 8px }
    .u76-gc p { font-size:13px;color:#3A3A38;line-height:1.6;margin:0 0 14px;flex:1 }
    .u76-gc a { font-size:13px;font-weight:600;color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.3);margin-top:auto }
    .u76-gc a:hover { border-bottom-color:#C0392B }

    /* reference links */
    .u76-ra { font-family:'DM Sans',sans-serif;font-size:13px;color:rgba(26,26,24,0.65);line-height:1.65;margin-bottom:8px }
    .u76-ra a { color:#C0392B;text-decoration:none;border-bottom:1px solid rgba(192,57,43,0.25) }

    /* FAQ */
    .u76-faq details { margin-bottom:2px }
    .u76-faq summary { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18;padding:18px 24px;background:#fff;cursor:pointer;list-style:none;border-bottom:1px solid rgba(26,26,24,0.06) }
    .u76-faq summary::-webkit-details-marker { display:none }
    .u76-faq summary::after { content:'+';float:right;font-size:18px;font-weight:400;color:rgba(26,26,24,0.3) }
    .u76-faq details[open] summary::after { content:'\\2212' }
    .u76-faq .u76-faq-a { font-family:'DM Sans',sans-serif;font-size:14px;color:rgba(26,26,24,0.65);line-height:1.7;padding:16px 24px 24px;background:#fff }

    /* sticky bar */
    .u76-stick { position:fixed;bottom:0;left:0;right:0;z-index:500;background:#1A1A18;color:#FDFCFB;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;font-family:'DM Sans',sans-serif;transform:translateY(100%);transition:transform 0.3s }
    .u76-stick.visible { transform:translateY(0) }
    .u76-stick-title { font-size:15px;font-weight:600 }
    .u76-stick-sub { font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }
    .u76-stick-actions { display:flex;gap:10px;align-items:center }
    .u76-stick-cta { background:#C0392B;color:#fff;padding:10px 22px;font-size:13px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em }
    .u76-stick-ghost { color:rgba(255,255,255,0.7);font-size:13px;font-weight:500;text-decoration:none;padding:10px 16px;border:1px solid rgba(255,255,255,0.2);border-radius:2px }
  </style>
  <script>
    (function(){
      var bar=null;
      window.addEventListener('scroll',function(){
        if(!bar)bar=document.getElementById('u76-stick');
        if(!bar)return;
        bar.classList.toggle('visible',window.scrollY>600);
      });
    })();
  </script>

  <!-- ── HERO — LIGHT 50/50 ── -->
  <section class="u76-hero">
    <div class="u76-hero-text">
      <div class="u76-eyebrow">Pro Audio Hall of Fame</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 20px">The Universal Audio 1176</h1>
      <p style="font-size:17px;color:rgba(26,26,24,0.6);line-height:1.65;max-width:460px;margin:0 0 28px">The "True Peak Limiter." Bill Putnam's solid-state masterpiece, in continuous production since 1967. The most-used compressor in professional recording history.</p>
      <a href="https://vintageking.com/urei-universal-audio-1176ln-compressor-limiter" target="_blank" style="display:inline-block;background:#C0392B;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em;align-self:flex-start">Shop 1176 Models</a>
    </div>
    <div class="u76-hero-img">
      <img src="https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?w=800&q=80" alt="Universal Audio 1176 compressor-limiter — studio rack" loading="lazy">
      <span class="u76-hero-caption">Placeholder — replace with VK product photo</span>
    </div>
  </section>

  <!-- ── STAT BAR ── -->
  <div class="u76-stats">
    <div class="u76-stat"><div class="u76-stat-num">1967</div><div class="u76-stat-label">First production</div></div>
    <div class="u76-stat"><div class="u76-stat-num">9</div><div class="u76-stat-label">Major revisions</div></div>
    <div class="u76-stat"><div class="u76-stat-num">20 &micro;s</div><div class="u76-stat-label">Fastest attack</div></div>
    <div class="u76-stat"><div class="u76-stat-num">45 dB</div><div class="u76-stat-label">Max gain</div></div>
    <div class="u76-stat"><div class="u76-stat-num">12,000+</div><div class="u76-stat-label">Units produced</div></div>
    <div class="u76-stat"><div class="u76-stat-num">57</div><div class="u76-stat-label">Years in production</div></div>
  </div>

  <!-- ── INTRO ── -->
  <section class="u76-section u76-section-white">
    <div class="u76-wrap">
      <div class="u76-eyebrow">History</div>
      <h2 class="u76-h2">Introducing the "True Peak Limiter"</h2>
      <p class="u76-body">The Universal Audio 1176 Compressor/Limiter was first introduced in 1967, created by Bill Putnam Sr. as the solid-state successor to his tube-based 176 limiting amplifier. The 1176 uses a Field Effect Transistor (FET) as a voltage divider to accomplish compression, combined with I/O transformers and a Class A line-level amplifier. Designed to be a "true peak limiter" with an attack time as fast as 20 microseconds and up to 45 dB of gain, it was unlike anything before it.</p>
      <p class="u76-body">The design went through numerous changes over the decades. The originals were somewhat noisy, prompting Brad Plunkett of UREI to design the Low Noise circuit that gave the unit its "LN" designation. Improvements continued through 9 major revisions — from the original Bluestripe to the final Silverface — each refining the sound that became the backbone of professional recording.</p>

      <div class="u76-quote">
        <p>"What's not to like? This is the workhorse of the industry. The most powerful compressor of them all. You can use it on any instrument and it'll do the job."</p>
        <cite>Michael Brauer, mixing engineer</cite>
      </div>
    </div>
  </section>

  <!-- ── SPEC TABLE ── -->
  <section class="u76-section u76-section-off">
    <div class="u76-wrap">
      <div class="u76-eyebrow">Core Specifications</div>
      <h2 class="u76-h2">Universal Specifications Across All Revisions</h2>
      <p class="u76-sub">Despite many design changes, every 1176 shares these fundamental features.</p>

      <table class="u76-spec-table">
        <thead>
          <tr><th>Parameter</th><th>Value</th></tr>
        </thead>
        <tbody>
          <tr><td>Input level control</td><td>Variable</td></tr>
          <tr><td>Output level control</td><td>Variable</td></tr>
          <tr><td>Attack time</td><td>20 microseconds to 800 microseconds</td></tr>
          <tr><td>Recovery time</td><td>50 milliseconds to 1.1 seconds</td></tr>
          <tr><td>Compression ratios</td><td>4:1, 8:1, 12:1, 20:1, All-In</td></tr>
          <tr><td>Max gain</td><td>45 dB</td></tr>
          <tr><td>VU meter modes</td><td>Off, Gain Reduction, Output (+4 / +8 dBm)</td></tr>
          <tr><td>I/O</td><td>Barrier strip, 1176-SA stereo-link RCA</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- ── REVISIONS TIMELINE ── -->
  <section class="u76-section u76-section-white">
    <div class="u76-wrap">
      <div class="u76-eyebrow">Every Revision</div>
      <h2 class="u76-h2">A Guide to 1176 Revisions: A through H</h2>
      <p class="u76-sub">Four fundamental eras of the 1176, spanning nearly two decades of production.</p>

      <!-- Bluestripes -->
      <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#1A1A18;margin:0 0 24px">The Original Bluestripes</h3>
      <div style="margin-bottom:48px">
        <div class="u76-tl">
          <div class="u76-tl-yr">1967</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision A · Serial 101–125</div>
            <div class="u76-tl-title">The Original</div>
            <p>Bill Putnam's first design. Peerless input transformer, T-pad attenuator, FET voltage divider, 1108 preamp circuit with Darlington pair, Class A output with UA-5002 transformer. Brushed aluminum faceplate with blue paint around the Weston meter — the original "Bluestripe." Two black knobs with silver tops, red power indicator.</p>
          </div>
        </div>
        <div class="u76-tl">
          <div class="u76-tl-yr">1967</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision A/B · Serial 125–216</div>
            <div class="u76-tl-title">First Refinement</div>
            <p>Resistor values changed in signal preamp stages, bypass capacitors added around the FET feed resistor. Improved noise and stability. Same Bluestripe cosmetics.</p>
          </div>
        </div>
        <div class="u76-tl">
          <div class="u76-tl-yr">1968–70</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision B · Serial 217–1078</div>
            <div class="u76-tl-title">Transistor Swap</div>
            <p>FETs replaced by 2N3391A bipolar transistor in the preamp circuit. Feedback tap added from emitter back to the gain reduction FET. Still the Bluestripe faceplate. Some Rev B units were later upgraded by UREI to Low Noise spec with replacement black faceplates.</p>
          </div>
        </div>
      </div>

      <!-- Low-Noise Blackfaces -->
      <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#1A1A18;margin:0 0 24px">The Low-Noise Blackfaces</h3>
      <div style="margin-bottom:48px">
        <div class="u76-tl">
          <div class="u76-tl-yr">1970</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision C · Serial 1079–1238</div>
            <div class="u76-tl-title">The LN Circuit Arrives</div>
            <p>Two major changes: Low Noise circuitry added to reduce drain-to-source voltage of the gain reduction FET, keeping it within its linear range. Circuit sealed in epoxy to protect the pending patent. Q-bias pot added to minimize distortion. Model designation changed from 1176 to 1176LN. New black anodized aluminum faceplate — the "Blackface" era begins. UREI logo placed over the new Modutec meter.</p>
          </div>
        </div>
        <div class="u76-tl">
          <div class="u76-tl-yr">1970–73</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision D · Serial 1239–2140</div>
            <div class="u76-tl-title">Board Integration</div>
            <p>Same circuit as Rev C, but the LN circuit and Q-bias pot are now integrated into a new circuit board instead of being soldered on as afterthoughts.</p>
          </div>
        </div>
        <div class="u76-tl">
          <div class="u76-tl-yr">1973</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision E · Serial 2141–2611</div>
            <div class="u76-tl-title">Voltage Switching</div>
            <p>Addition of a power transformer switch for 110V/220V operation. Virtually identical to C and D in sound. Revisions C, D, and E are generally the most revered — the modern Universal Audio reissue is based on these versions.</p>
          </div>
        </div>
      </div>

      <!-- Push-Pull Blackface -->
      <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#1A1A18;margin:0 0 24px">The Push-Pull Blackface</h3>
      <div style="margin-bottom:48px">
        <div class="u76-tl">
          <div class="u76-tl-yr">1973+</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision F · Serial 2611–7052</div>
            <div class="u76-tl-title">Higher Output, New Amplifier</div>
            <p>Major overhaul. UA's new 1109 preamplifier replaced the Class A output with a Class A/B push-pull configuration, providing significantly more output current. The UA5002A output transformer replaced by the B11148 (from the LA-3A), yielding 12 dB more gain. Meter drive circuit simplified with an operational amplifier. Around unit #6950, UREI moved from North Hollywood to Sun Valley, California.</p>
          </div>
        </div>
      </div>

      <!-- Op-Amp Blackface and Silverface -->
      <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#1A1A18;margin:0 0 24px">The Op-Amp Blackface and Silverface</h3>
      <div style="margin-bottom:48px">
        <div class="u76-tl">
          <div class="u76-tl-yr">~1976</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision G · Serial 7053–7651</div>
            <div class="u76-tl-title">Input Transformer Removed</div>
            <p>The final major circuit change. The input transformer was removed and replaced with a differential input op-amp stage. Produced in the new Sun Valley factory. Cleaner sound character than all previous revisions.</p>
          </div>
        </div>
        <div class="u76-tl">
          <div class="u76-tl-yr">~1978+</div>
          <div class="u76-tl-body">
            <div class="u76-tl-tag">Revision H · Serial 7652–12200+</div>
            <div class="u76-tl-title">The Silverface</div>
            <p>No circuit changes — cosmetics only. Natural brushed aluminum faceplate replaces the black anodized finish. Blue UREI badge replaces silk-screened logo. Modutec "light box" meter. Red Off button. Square fuse holder, IEC cable input replacing the attached power cord. At serial ~10750, Harman Electronics took over UREI. One-third of all vintage 1176 units are Rev G or H.</p>
          </div>
        </div>
      </div>

      <!-- Modern Reissue -->
      <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#1A1A18;margin:0 0 24px">The Modern Reissue</h3>
      <div class="u76-tl">
        <div class="u76-tl-yr">2000</div>
        <div class="u76-tl-body">
          <div class="u76-tl-tag">Universal Audio Reissue · Serial 101–current</div>
          <div class="u76-tl-title">The Putnam Sons Revival</div>
          <p>In 2000, Bill Putnam Jr. and James Putnam resurrected Universal Audio with the 1176LN as their first release — an authentic reissue based primarily on the revered Revisions C, D, and E. The most famous FET compressor in history, back in production.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── REVISION SUMMARY CARDS ── -->
  <section class="u76-section u76-section-off">
    <div class="u76-wrap">
      <div class="u76-eyebrow">At a Glance</div>
      <h2 class="u76-h2">Four Fundamental Versions</h2>
      <p class="u76-sub">In essence, there have been only four basic versions of the 1176.</p>

      <div class="u76-rev-grid">
        <div class="u76-rev">
          <div class="u76-rev-name">Bluestripes</div>
          <div class="u76-rev-serial">Rev A, A/B, B · 1967–1970</div>
          <p>The edgiest versions, with plenty of noise and distortion to provide a distinct color to any signal. The original sound.</p>
        </div>
        <div class="u76-rev">
          <div class="u76-rev-name">LN Blackfaces</div>
          <div class="u76-rev-serial">Rev C, D, E · 1970–1973</div>
          <p>Classic character with a lower noise floor. The heart of the 1176 sound. Modern reissues are based on this era.</p>
        </div>
        <div class="u76-rev">
          <div class="u76-rev-name">Push-Pull Blackface</div>
          <div class="u76-rev-serial">Rev F · 1973 onward</div>
          <p>Continued the classic sound with a new output transformer for considerably higher gain. The workhorse era.</p>
        </div>
      </div>
      <div class="u76-rev-grid" style="grid-template-columns:1fr 1fr">
        <div class="u76-rev">
          <div class="u76-rev-name">Op-Amp / Silverface</div>
          <div class="u76-rev-serial">Rev G, H · 1976–end</div>
          <p>Input transformer replaced with an op-amp for a cleaner sound. One-third of all vintage 1176 units are this type.</p>
        </div>
        <div class="u76-rev">
          <div class="u76-rev-name">UA Reissue</div>
          <div class="u76-rev-serial">2000–present</div>
          <p>Authentic reproduction based on Rev C/D/E. Bill Putnam's sons brought the 1176LN back to continuous production.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── BUYER GUIDE ── -->
  <section class="u76-section u76-section-white">
    <div class="u76-wrap">
      <div class="u76-eyebrow">Which 1176 Is Right for You?</div>
      <h2 class="u76-h2">Every 1176 at Vintage King</h2>
      <p class="u76-sub">Hardware, reissues, alternatives, and plug-ins — from $29.99 to vintage originals by request.</p>

      <div class="u76-gc-grid">
        <div class="u76-gc">
          <div class="u76-gc-tag">Modern reissue</div>
          <h4>Universal Audio 1176LN</h4>
          <div class="u76-gc-price">$2,999</div>
          <p>The official reissue. Based on Rev C/D/E, built at UA's facility. Class A output, hand-matched FET, original Bill Putnam circuit. The benchmark.</p>
          <a href="https://vintageking.com/universal-audio-1176-ln" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
        <div class="u76-gc">
          <div class="u76-gc-tag">Channel strip</div>
          <h4>Universal Audio 6176</h4>
          <div class="u76-gc-price">$2,999</div>
          <p>610 tube preamp paired with the 1176LN compressor in a single 2U chassis. Record-ready signal chain.</p>
          <a href="https://vintageking.com/universal-audio-6176" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
        <div class="u76-gc">
          <div class="u76-gc-tag">Alternative</div>
          <h4>Purple Audio MC77</h4>
          <div class="u76-gc-price">$1,850</div>
          <p>Expanded feature set: stepped I/O, sidechain HPF, and hard/soft recovery. One of the most respected 1176-style units on the market.</p>
          <a href="https://vintageking.com/purple-audio-mc77" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
      </div>
      <div class="u76-gc-grid" style="margin-top:1px">
        <div class="u76-gc">
          <div class="u76-gc-tag">Alternative</div>
          <h4>Retro Instruments 176</h4>
          <div class="u76-gc-price">$3,695</div>
          <p>Tube-based take on the 1176 lineage. Returns to Bill Putnam's original 176 tube limiter concept with modern manufacturing.</p>
          <a href="https://vintageking.com/retro-instruments-176" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
        <div class="u76-gc">
          <div class="u76-gc-tag">Budget hardware</div>
          <h4>UK Sound 176 Mono</h4>
          <div class="u76-gc-price">$749</div>
          <p>Affordable 1176-style compression. FET design with transformer output. Entry point for hardware 1176 tone.</p>
          <a href="https://vintageking.com/uk-sound-176-mono-compressor" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
        <div class="u76-gc">
          <div class="u76-gc-tag">Plug-in</div>
          <h4>Waves CLA-76</h4>
          <div class="u76-gc-price">$29.99</div>
          <p>Chris Lord-Alge's go-to 1176 emulation. Two versions: "Bluey" (Rev A) and "Blacky" (Rev E). Industry standard ITB compression.</p>
          <a href="https://vintageking.com/waves-cla-76-native" target="_blank">Shop at Vintage King &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── FURTHER READING ── -->
  <section class="u76-section u76-section-off">
    <div class="u76-wrap">
      <div class="u76-eyebrow">Further Reading</div>
      <h2 class="u76-h2">From the Vintage King Blog</h2>
      <div style="margin-top:24px">
        <p class="u76-ra"><a href="https://vintageking.com/blog/2017/08/universal-audio-plugins-hardware/" target="_blank">Comparing Universal Audio Plug-Ins to Their Hardware Counterparts &rarr;</a></p>
        <p class="u76-ra"><a href="https://vintageking.com/blog/2015/07/universal-audio/" target="_blank">Vintage King's Inside Look at Universal Audio &rarr;</a></p>
        <p class="u76-ra"><a href="https://vintageking.com/blog/2017/09/compressors-guide/" target="_blank">Vintage King's Guide to Compressors and Using Them in the Studio &rarr;</a></p>
      </div>
    </div>
  </section>

  <!-- ── FAQ ── -->
  <section class="u76-section u76-section-white">
    <div class="u76-wrap">
      <div class="u76-eyebrow">Frequently Asked Questions</div>
      <h2 class="u76-h2" style="margin-bottom:32px">1176 FAQ</h2>

      <div class="u76-faq">
        <details><summary>What is the difference between 1176 revisions?</summary><div class="u76-faq-a">There are 9 major revisions lettered A through H (including A/B). Bluestripes (A, A/B, B) are edgy with more noise and distortion. Low-Noise Blackfaces (C, D, E) are the most revered and the basis for modern reissues. Rev F added a push-pull output for more gain. Revs G and H replaced the input transformer with an op-amp for a cleaner sound.</div></details>
        <details><summary>What is "All Buttons In" mode?</summary><div class="u76-faq-a">Pressing all four ratio buttons simultaneously engages a unique compression behavior where the ratio hovers around 12:1 to 20:1 with increased distortion and a distinctive pumping effect. Engineers use it on drums, room mics, and vocals for aggressive, characterful compression. It was never intended by the designers — it's a happy accident that became a studio standard.</div></details>
        <details><summary>Which 1176 revision sounds best?</summary><div class="u76-faq-a">Revisions C, D, and E (the first Low-Noise Blackfaces) are generally considered the most desirable. They have the classic 1176 character with a lower noise floor than the Bluestripes. The modern Universal Audio reissue is based primarily on these versions. However, many engineers prefer Bluestripes for their raw, colored character — especially on drums and guitars.</div></details>
        <details><summary>How fast is the 1176 attack?</summary><div class="u76-faq-a">The 1176 has an attack time as fast as 20 microseconds — among the fastest of any compressor. Note that the 1176's controls are reversed: turning the Attack knob fully clockwise gives the slowest attack, while fully counter-clockwise gives the fastest 20-microsecond attack. This catches you the first time.</div></details>
        <details><summary>Can I use a vintage 1176 daily?</summary><div class="u76-faq-a">Yes — with proper maintenance. Vintage 1176 units are workhorses built for daily studio use. Vintage King's Tech Shop can recap, recalibrate, and restore any revision to specification. Common service includes recapping electrolytics, replacing the FET if noisy, and recalibrating the meter and threshold.</div></details>
        <details><summary>1176 vs LA-2A — when to use each?</summary><div class="u76-faq-a">The 1176 is a FET compressor with fast attack and aggressive character — ideal for drums, bass, guitars, and vocals that need urgency and punch. The LA-2A is an optical compressor with a slower, smoother response — better for vocals that need transparent leveling, bass that needs to sit evenly, and any source where you want compression to be invisible. Many engineers use both in series: LA-2A for leveling, then 1176 for color and control.</div></details>
      </div>
    </div>
  </section>

  <!-- STICKY SHOP BAR ──────────────────────────────────────────────────── -->
  <div class="u76-stick" id="u76-stick">
    <div>
      <div class="u76-stick-title">Universal Audio 1176</div>
      <div class="u76-stick-sub">Hardware from $749 · Plug-ins from $29.99 · UA reissue in stock</div>
    </div>
    <div class="u76-stick-actions">
      <a href="https://vintageking.com/urei-universal-audio-1176ln-compressor-limiter" target="_blank" class="u76-stick-cta">Shop at Vintage King</a>
      <a href="audio-consultants.html" class="u76-stick-ghost">Ask an Expert</a>
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
