"""section-179.html — Section 179 Tax Deduction page."""
import re

INLINE_JS = """\
<script>
  (function() {
    var p = 'section-179';
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

SLUG  = "section-179"
TITLE = "Section 179 Tax Deduction — Write Off Your Studio Gear | Vintage King"
META  = "Deduct the full purchase price of qualifying studio equipment in the year you buy it. Section 179 lets studios, churches, and businesses save thousands on pro audio gear."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "HowTo",
      "name": "How to Use the Section 179 Tax Deduction for Studio Gear",
      "description": "Section 179 of the IRS tax code allows businesses to deduct the full purchase price of qualifying equipment in the year it was purchased, rather than depreciating it over multiple years.",
      "step": [
        {"@type": "HowToStep", "name": "Purchase qualifying equipment", "text": "Buy new or used pro audio, studio, or production equipment from Vintage King before December 31."},
        {"@type": "HowToStep", "name": "Put equipment into service", "text": "Install and begin using the equipment in your business before the end of the tax year."},
        {"@type": "HowToStep", "name": "Claim the deduction", "text": "File IRS Form 4562 with your tax return. Deduct the full cost up to the annual limit. Consult your tax professional for details."}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the Section 179 deduction?",
          "acceptedAnswer": {"@type": "Answer", "text": "Section 179 allows businesses to deduct the full purchase price of qualifying equipment and software in the year of purchase, rather than depreciating it over several years. For 2025, the deduction limit is $1,220,000."}
        },
        {
          "@type": "Question",
          "name": "Does Section 179 apply to used equipment?",
          "acceptedAnswer": {"@type": "Answer", "text": "Yes. Section 179 applies to both new and used equipment, as long as it is new to your business and put into service during the tax year."}
        },
        {
          "@type": "Question",
          "name": "Who qualifies for Section 179?",
          "acceptedAnswer": {"@type": "Answer", "text": "Any business that purchases, finances, or leases qualifying equipment. This includes recording studios, production companies, churches, schools, nonprofits, and freelance engineers operating as a business."}
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
  <a href="trade-program.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Trade Program</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Section 179</span>
</nav>
"""

PAGE_BODY = """\
<div id="section-179" class="page active">
  <div id="nav-section-179"></div>

  <style>
    .s179-wrap { max-width:1160px;margin:0 auto;padding:0 40px }
    .s179-eyebrow { font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;margin-bottom:14px }
    .s179-hero { background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:600px;overflow:hidden }
    .s179-hero-text { padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center }
    .s179-hero-img { position:relative;overflow:hidden }
    .s179-hero-img img { width:100%;height:100%;object-fit:cover;display:block }
    .s179-hero-caption { position:absolute;bottom:12px;right:16px;font-size:11px;color:rgba(255,255,255,0.55);font-family:'DM Sans',sans-serif }
    .s179-hero-stats-inline { display:flex;gap:24px;margin-top:24px }
    .s179-hero-stat-num { font-family:'DM Sans',sans-serif;font-size:22px;font-weight:700;color:#D4860A;line-height:1.1 }
    .s179-hero-stat-label { font-family:'DM Sans',sans-serif;font-size:11px;color:rgba(26,26,24,0.45);margin-top:3px }
    .s179-section { padding:64px 0 }
    .s179-section-off { background:var(--off-white,#F7F5F2) }
    .s179-section-white { background:#fff }
    .s179-section-cta { background:#EDE8E2 }
    .s179-h2 { font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 8px;line-height:1.15 }
    .s179-sub { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.55);margin:0 0 40px;line-height:1.6;max-width:680px }
    .s179-body { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.7);line-height:1.75;max-width:760px;margin:0 0 24px }
    .s179-steps { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .s179-step { background:#fff;padding:36px 28px;transition:box-shadow .3s ease,transform .3s ease }
    .s179-step:hover { transform:translateY(-3px);box-shadow:0 8px 24px rgba(26,26,24,0.08) }
    .s179-step-num { font-family:'DM Sans',sans-serif;font-size:32px;font-weight:700;color:#D4860A;line-height:1;margin-bottom:16px }
    .s179-step h3 { font-family:'DM Sans',sans-serif;font-size:16px;font-weight:700;color:#1A1A18;margin:0 0 8px }
    .s179-step p { font-size:13px;color:rgba(26,26,24,0.6);line-height:1.65;margin:0 }
    .s179-who-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .s179-who { background:#fff;padding:28px 24px;text-align:center;transition:box-shadow .3s ease,transform .3s ease }
    .s179-who:hover { transform:translateY(-3px);box-shadow:0 8px 24px rgba(26,26,24,0.08) }
    .s179-who h4 { font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1A1A18;margin:0 0 6px }
    .s179-who p { font-size:13px;color:rgba(26,26,24,0.5);margin:0;line-height:1.5 }
    .s179-what-grid { display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .s179-what { background:#fff;padding:24px;text-align:center }
    .s179-what h4 { font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1A1A18;margin:0 0 4px }
    .s179-what p { font-size:12px;color:rgba(26,26,24,0.5);margin:0;line-height:1.5 }
    .s179-faq details { margin-bottom:2px }
    .s179-faq summary { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18;padding:18px 24px;background:#fff;cursor:pointer;list-style:none;border-bottom:1px solid rgba(26,26,24,0.06) }
    .s179-faq summary::-webkit-details-marker { display:none }
    .s179-faq summary::after { content:'+';float:right;font-size:18px;font-weight:400;color:rgba(26,26,24,0.3) }
    .s179-faq details[open] summary::after { content:'\\2212' }
    .s179-faq .s179-faq-a { font-family:'DM Sans',sans-serif;font-size:14px;color:rgba(26,26,24,0.65);line-height:1.7;padding:16px 24px 24px;background:#fff }
    /* dark savings example section */
    .s179-dark { background:#1A1A18;padding:56px 64px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center }
    .s179-dark h3 { font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#FDFCFB;margin:0 0 16px }
    .s179-dark p { font-size:15px;color:rgba(253,252,251,0.7);line-height:1.75;margin-bottom:14px }
    .s179-dark p:last-child { margin-bottom:0 }
    .s179-dark-example { background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:3px;padding:32px }
    .s179-dark-row { display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.06);font-size:14px }
    .s179-dark-row:last-child { border-bottom:none }
    .s179-dark-label { color:rgba(253,252,251,0.5) }
    .s179-dark-value { color:#FDFCFB;font-weight:600 }
    .s179-dark-total { color:#D4860A;font-size:18px;font-weight:700 }

    .s179-stick { position:fixed;bottom:0;left:0;right:0;z-index:500;background:#1A1A18;color:#FDFCFB;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;font-family:'DM Sans',sans-serif;transform:translateY(100%);transition:transform 0.3s }
    .s179-stick.visible { transform:translateY(0) }
    .s179-stick-title { font-size:15px;font-weight:600 }
    .s179-stick-sub { font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }
    .s179-stick-cta { background:#C0392B;color:#fff;padding:10px 22px;font-size:13px;font-weight:600;text-decoration:none;border-radius:2px }
    .s179-stick-ghost { color:rgba(255,255,255,0.7);font-size:13px;font-weight:500;text-decoration:none;padding:10px 16px;border:1px solid rgba(255,255,255,0.2);border-radius:2px }

    /* explore strip */
    .s179-explore { background:#EDE8E2;padding:64px 0 }
    .s179-explore-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:20px }
    .s179-explore-card { background:#fff;border-radius:3px;overflow:hidden;text-decoration:none;transition:box-shadow .3s ease,transform .3s ease }
    .s179-explore-card:hover { transform:translateY(-4px);box-shadow:0 12px 32px rgba(26,26,24,0.1) }
    .s179-explore-img { height:180px;background:#F7F5F2;overflow:hidden }
    .s179-explore-img img { width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s ease }
    .s179-explore-card:hover .s179-explore-img img { transform:scale(1.06) }
    .s179-explore-body { padding:20px 24px }
    .s179-explore-tag { font-family:'DM Sans',sans-serif;font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:6px }
    .s179-explore-title { font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 6px }
    .s179-explore-desc { font-family:'DM Sans',sans-serif;font-size:13px;color:rgba(26,26,24,0.55);line-height:1.55;margin:0 }
  </style>
  <script>
    (function(){
      var bar=null;
      window.addEventListener('scroll',function(){
        if(!bar)bar=document.getElementById('s179-stick');
        if(!bar)return;
        bar.classList.toggle('visible',window.scrollY>500);
      });
    })();
  </script>

  <!-- ── HERO ── -->
  <section class="s179-hero">
    <div class="s179-hero-text">
      <div class="s179-eyebrow">Tax Savings</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 20px">Section 179 Tax Deduction</h1>
      <p style="font-size:17px;color:rgba(26,26,24,0.6);line-height:1.65;max-width:460px;margin:0 0 28px">Write off the full cost of qualifying studio equipment in the year you buy it. New or used. Purchased, financed, or leased.</p>
      <a href="https://vintageking.com/audio-consultants" target="_blank" style="display:inline-block;background:#C0392B;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em;align-self:flex-start">Talk to an Expert</a>
      <div class="s179-hero-stats-inline">
        <div><div class="s179-hero-stat-num">$1.22M</div><div class="s179-hero-stat-label">2025 limit</div></div>
        <div><div class="s179-hero-stat-num">100%</div><div class="s179-hero-stat-label">Year-one write-off</div></div>
        <div><div class="s179-hero-stat-num">Dec 31</div><div class="s179-hero-stat-label">Annual deadline</div></div>
      </div>
    </div>
    <div class="s179-hero-img">
      <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Rack_Outboard_Location_Recording.jpg" alt="Professional outboard gear rack" loading="lazy">
      <span class="s179-hero-caption">Photo: Milkstudios / Wikimedia CC BY-SA 3.0</span>
    </div>
  </section>

  <!-- ── WHAT IS IT ── -->
  <section class="s179-section s179-section-white">
    <div class="s179-wrap">
      <div class="s179-eyebrow">Overview</div>
      <h2 class="s179-h2">What Is the Section 179 Deduction?</h2>
      <p class="s179-body">Section 179 of the IRS tax code allows businesses to deduct the full purchase price of qualifying equipment in the year it was purchased, rather than depreciating it over several years. For studios, production companies, churches, and any business buying pro audio gear, this means significant tax savings — potentially thousands of dollars on a single purchase.</p>
      <p class="s179-body">The deduction applies to tangible business equipment that is purchased, financed, or leased and put into service during the tax year. Both new and used equipment qualify, as long as the equipment is new to your business.</p>
    </div>
  </section>

  <!-- ── HOW IT WORKS ── -->
  <section class="s179-section s179-section-off">
    <div class="s179-wrap">
      <div class="s179-eyebrow">How It Works</div>
      <h2 class="s179-h2">Three Steps to Your Deduction</h2>
      <p class="s179-sub">Equipment must be purchased and put into service before December 31 of the tax year.</p>

      <div class="s179-steps">
        <div class="s179-step">
          <div class="s179-step-num">1</div>
          <h3>Purchase Qualifying Equipment</h3>
          <p>Buy new or used pro audio, studio, recording, or production equipment from Vintage King. Financed and leased equipment also qualifies.</p>
        </div>
        <div class="s179-step">
          <div class="s179-step-num">2</div>
          <h3>Put It Into Service</h3>
          <p>Install and begin using the equipment in your business before December 31. It must be actively used for business purposes — not just purchased and stored.</p>
        </div>
        <div class="s179-step">
          <div class="s179-step-num">3</div>
          <h3>Claim the Deduction</h3>
          <p>File IRS Form 4562 with your annual tax return. Deduct the full purchase price up to the annual Section 179 limit. Consult your tax professional for specific guidance.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── WHO QUALIFIES ── -->
  <section class="s179-section s179-section-white">
    <div class="s179-wrap">
      <div class="s179-eyebrow">Eligibility</div>
      <h2 class="s179-h2">Who Qualifies?</h2>
      <p class="s179-sub">Any business entity that purchases qualifying equipment for business use.</p>

      <div class="s179-who-grid">
        <div class="s179-who"><h4>Recording Studios</h4><p>Commercial and project studios</p></div>
        <div class="s179-who"><h4>Production Companies</h4><p>Film, TV, podcast, broadcast</p></div>
        <div class="s179-who"><h4>Churches and Nonprofits</h4><p>Houses of worship, 501(c)(3)</p></div>
        <div class="s179-who"><h4>Schools and Universities</h4><p>Music programs, media labs</p></div>
        <div class="s179-who"><h4>Freelance Engineers</h4><p>Operating as a business entity</p></div>
        <div class="s179-who"><h4>Live Sound Companies</h4><p>Touring, installed, rental</p></div>
      </div>
    </div>
  </section>

  <!-- ── WHAT QUALIFIES ── -->
  <section class="s179-section s179-section-off">
    <div class="s179-wrap">
      <div class="s179-eyebrow">Qualifying Equipment</div>
      <h2 class="s179-h2">What Can You Deduct?</h2>
      <p class="s179-sub">Tangible equipment purchased for business use. Both new and used qualify.</p>

      <div class="s179-what-grid">
        <div class="s179-what"><h4>Microphones</h4><p>Condensers, ribbons, dynamics</p></div>
        <div class="s179-what"><h4>Preamps and EQs</h4><p>Channel strips, outboard</p></div>
        <div class="s179-what"><h4>Compressors</h4><p>Hardware dynamics processors</p></div>
        <div class="s179-what"><h4>Interfaces and Converters</h4><p>AD/DA, USB, Thunderbolt</p></div>
        <div class="s179-what"><h4>Monitors and Speakers</h4><p>Studio monitors, subs</p></div>
        <div class="s179-what"><h4>Consoles and Mixers</h4><p>Analog, digital, control surfaces</p></div>
        <div class="s179-what"><h4>Recording Furniture</h4><p>Desks, racks, acoustic treatment</p></div>
        <div class="s179-what"><h4>Installed Systems</h4><p>Studio wiring, patchbays, infrastructure</p></div>
      </div>
    </div>
  </section>

  <!-- ── SAVINGS EXAMPLE — DARK SECTION ── -->
  <div class="s179-dark">
    <div>
      <h3>See How Much You Could Save</h3>
      <p>Here's a simplified example of how Section 179 works for a studio purchasing $50,000 in equipment. The actual tax benefit depends on your tax bracket, business structure, and state laws.</p>
      <p>Equipment purchased, financed, or leased before December 31 qualifies. The gear must be put into service in the same tax year — simply ordering before the deadline is not sufficient.</p>
      <p style="font-size:13px;color:rgba(253,252,251,0.4)">This is a simplified illustration. Consult a qualified tax professional for your specific situation. Vintage King is not a tax advisory firm.</p>
    </div>
    <div class="s179-dark-example">
      <div class="s179-dark-row"><span class="s179-dark-label">Equipment purchased</span><span class="s179-dark-value">$50,000</span></div>
      <div class="s179-dark-row"><span class="s179-dark-label">Section 179 deduction</span><span class="s179-dark-value">$50,000</span></div>
      <div class="s179-dark-row"><span class="s179-dark-label">Assumed tax bracket</span><span class="s179-dark-value">35%</span></div>
      <div class="s179-dark-row"><span class="s179-dark-label">Estimated tax savings</span><span class="s179-dark-total">$17,500</span></div>
      <div class="s179-dark-row"><span class="s179-dark-label">Net equipment cost</span><span class="s179-dark-value">$32,500</span></div>
      <div style="margin-top:16px;font-size:11px;color:rgba(253,252,251,0.3);text-align:center;letter-spacing:0.04em">2025 DEDUCTION LIMIT: $1,220,000 · PHASE-OUT BEGINS AT $3,050,000</div>
    </div>
  </div>

  <!-- ── FAQ ── -->
  <section class="s179-section s179-section-white">
    <div class="s179-wrap">
      <div class="s179-eyebrow">Frequently Asked Questions</div>
      <h2 class="s179-h2" style="margin-bottom:32px">Section 179 FAQ</h2>

      <div class="s179-faq">
        <details><summary>What is the 2025 Section 179 deduction limit?</summary><div class="s179-faq-a">For 2025, the Section 179 deduction limit is $1,220,000. The total equipment purchase limit is $3,050,000, after which the deduction begins to phase out dollar-for-dollar. These figures are adjusted annually for inflation.</div></details>
        <details><summary>Does financed or leased equipment qualify?</summary><div class="s179-faq-a">Yes. Equipment that is purchased, financed, or leased qualifies for Section 179 — you can deduct the full cost in the year it is put into service, even if you are making monthly payments.</div></details>
        <details><summary>Can I deduct used equipment?</summary><div class="s179-faq-a">Yes. Both new and used equipment qualify, as long as the equipment is new to your business and purchased and put into service during the tax year.</div></details>
        <details><summary>When is the deadline?</summary><div class="s179-faq-a">Equipment must be purchased AND put into service before December 31 of the tax year. Simply ordering before December 31 is not sufficient — the equipment must be installed and in use.</div></details>
        <details><summary>Do I need a tax professional?</summary><div class="s179-faq-a">This information is provided for general awareness. Section 179 rules can be complex. We strongly recommend consulting a qualified tax professional to determine your specific eligibility and deduction amount. Vintage King is not a tax advisory firm.</div></details>
        <details><summary>Can Vintage King help me plan a Section 179 purchase?</summary><div class="s179-faq-a">Yes. Our Audio Consultants can help you select qualifying equipment, arrange financing through our leasing partners, and coordinate delivery timelines to ensure your gear is in service before the December 31 deadline. Call 888.653.1184 to get started.</div></details>
      </div>
    </div>
  </section>

  <!-- ── CTA ── -->
  <section class="s179-section s179-section-cta">
    <div class="s179-wrap" style="text-align:center">
      <div class="s179-eyebrow">Ready to Save?</div>
      <h2 class="s179-h2" style="margin:0 auto 16px">Plan Your Section 179 Purchase</h2>
      <p style="font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.6);max-width:520px;margin:0 auto 32px;line-height:1.6">Talk to an Audio Consultant about qualifying equipment, financing options, and delivery timelines. Start saving before December 31.</p>
      <a href="audio-consultants.html" style="display:inline-block;background:#C0392B;color:#fff;padding:14px 32px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;margin-right:12px">Talk to an Expert</a>
      <a href="https://vintageking.com" target="_blank" style="display:inline-block;background:transparent;color:#1A1A18;padding:13px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border:1px solid rgba(26,26,24,0.25);border-radius:2px">Shop Now</a>
    </div>
  </section>

  <!-- ── CONTINUE EXPLORING ── -->
  <section class="s179-explore">
    <div class="s179-wrap">
      <div class="s179-eyebrow">Continue Exploring</div>
      <h2 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;margin:0 0 32px">More from Vintage King</h2>
      <div class="s179-explore-grid">
        <a href="urei-1176.html" class="s179-explore-card">
          <div class="s179-explore-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/UREI_1176LN_%28Silver%29_x6.jpg/600px-UREI_1176LN_%28Silver%29_x6.jpg" alt="UREI 1176" loading="lazy"></div>
          <div class="s179-explore-body">
            <div class="s179-explore-tag">Hall of Fame</div>
            <div class="s179-explore-title">The Universal Audio 1176</div>
            <p class="s179-explore-desc">The most-used compressor in recording history. FET design since 1967.</p>
          </div>
        </a>
        <a href="neumann-u67.html" class="s179-explore-card">
          <div class="s179-explore-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Microphone_Neumann_U-67_%281953%29.jpg/500px-Microphone_Neumann_U-67_%281953%29.jpg" alt="Neumann U67" loading="lazy"></div>
          <div class="s179-explore-body">
            <div class="s179-explore-tag">Hall of Fame</div>
            <div class="s179-explore-title">The Neumann U67</div>
            <p class="s179-explore-desc">Neumann's legendary tube condenser — K67 capsule that shaped modern recording.</p>
          </div>
        </a>
        <a href="warranty.html" class="s179-explore-card">
          <div class="s179-explore-img"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Outboard_racks_1-2%2C_PatchWerk_Recording_Studios%2C_2007.jpg/960px-Outboard_racks_1-2%2C_PatchWerk_Recording_Studios%2C_2007.jpg" alt="Studio gear" loading="lazy"></div>
          <div class="s179-explore-body">
            <div class="s179-explore-tag">Buyer Protection</div>
            <div class="s179-explore-title">VK Warranty</div>
            <p class="s179-explore-desc">+1 free year on every purchase. No registration. Optional ADH coverage.</p>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- STICKY BAR -->
  <div class="s179-stick" id="s179-stick">
    <div>
      <div class="s179-stick-title">Section 179</div>
      <div class="s179-stick-sub">Deduct the full cost of studio gear · Deadline Dec 31</div>
    </div>
    <div style="display:flex;gap:10px;align-items:center">
      <a href="audio-consultants.html" class="s179-stick-cta">Talk to an Expert</a>
      <a href="https://vintageking.com" target="_blank" class="s179-stick-ghost">Shop Now</a>
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
