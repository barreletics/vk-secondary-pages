"""warranty.html — VK Warranty program page."""
import re

INLINE_JS = """\
<script>
  (function() {
    var p = 'warranty';
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

SLUG  = "warranty"
TITLE = "VK Warranty — World-Class Protection for Every Purchase | Vintage King"
META  = "Vintage King adds one free year to every manufacturer warranty. Plus optional ADH coverage for drops, breaks, and spills. New, used, and vintage gear — all protected."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "name": "VK Warranty — Extended Protection Program",
      "provider": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"},
      "description": "Vintage King adds one free year to every manufacturer warranty on new gear. Used analog rack gear: 1 year. Microphones: 6 months. Digital: 30 days. Optional ADH plans available."
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the VK extended warranty?",
          "acceptedAnswer": {"@type": "Answer", "text": "Vintage King adds one free year to every manufacturer warranty on new gear at no extra cost. If the manufacturer offers 1 year, you get 2. If they offer 5 years, you get 6."}
        },
        {
          "@type": "Question",
          "name": "What does the ADH plan cover?",
          "acceptedAnswer": {"@type": "Answer", "text": "The Accidental Damage and Handling plan covers drops, breaks, and spills — including speaker drivers, mic capsules, and tubes that are not typically covered by standard warranties."}
        },
        {
          "@type": "Question",
          "name": "Does used gear come with a warranty?",
          "acceptedAnswer": {"@type": "Answer", "text": "Yes. Analog rack gear: 1 year warranty. Microphones: 6 months. Digital products: 30 days. All used and vintage items are serviced by Vintage King's in-house tech team before shipping."}
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
  <span style="opacity:0.75">VK Warranty</span>
</nav>
"""

PAGE_BODY = """\
<div id="warranty" class="page active">
  <div id="nav-warranty"></div>

  <style>
    .wr-wrap { max-width:1160px;margin:0 auto;padding:0 40px }
    .wr-eyebrow { font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;margin-bottom:14px }
    .wr-hero { background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:520px;overflow:hidden }
    .wr-hero-text { padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center }
    .wr-hero-stats { background:#fff;display:grid;grid-template-columns:1fr 1fr;gap:1px;padding:0 }
    .wr-hero-stat { display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px 24px;text-align:center }
    .wr-hero-stat-num { font-family:'DM Sans',sans-serif;font-size:36px;font-weight:700;color:#1A1A18;line-height:1.1 }
    .wr-hero-stat-label { font-family:'DM Sans',sans-serif;font-size:12px;color:rgba(26,26,24,0.5);margin-top:8px;letter-spacing:0.04em }
    .wr-section { padding:64px 0 }
    .wr-section-off { background:var(--off-white,#F7F5F2) }
    .wr-section-white { background:#fff }
    .wr-section-cta { background:#EDE8E2 }
    .wr-h2 { font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 8px;line-height:1.15 }
    .wr-sub { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.55);margin:0 0 40px;line-height:1.6;max-width:680px }
    .wr-body { font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.7);line-height:1.75;max-width:760px;margin:0 0 24px }
    .wr-tier-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .wr-tier { background:#fff;padding:36px 28px;display:flex;flex-direction:column }
    .wr-tier-tag { font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:12px }
    .wr-tier h3 { font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1A1A18;margin:0 0 8px }
    .wr-tier-period { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18;margin-bottom:16px }
    .wr-tier p { font-size:13px;color:rgba(26,26,24,0.6);line-height:1.65;margin:0 0 8px }
    .wr-tier ul { font-size:13px;color:rgba(26,26,24,0.6);line-height:1.8;margin:0;padding-left:16px }
    .wr-adh { display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;margin-top:40px }
    .wr-adh-text h3 { font-family:'Playfair Display',serif;font-size:24px;font-weight:700;color:#1A1A18;margin:0 0 12px }
    .wr-adh-text p { font-size:14px;color:rgba(26,26,24,0.65);line-height:1.7;margin:0 0 16px }
    .wr-adh-covers { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .wr-adh-item { background:#fff;padding:20px;text-align:center }
    .wr-adh-item h4 { font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1A1A18;margin:0 0 4px }
    .wr-adh-item p { font-size:12px;color:rgba(26,26,24,0.5);margin:0;line-height:1.5 }
    .wr-used-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden }
    .wr-used { background:#fff;padding:28px 24px }
    .wr-used h4 { font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1A1A18;margin:0 0 4px }
    .wr-used-period { font-size:22px;font-family:'DM Sans',sans-serif;font-weight:700;color:#D4860A;margin:8px 0 }
    .wr-used p { font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6;margin:0 }
    .wr-faq details { margin-bottom:2px }
    .wr-faq summary { font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18;padding:18px 24px;background:#fff;cursor:pointer;list-style:none;border-bottom:1px solid rgba(26,26,24,0.06) }
    .wr-faq summary::-webkit-details-marker { display:none }
    .wr-faq summary::after { content:'+';float:right;font-size:18px;font-weight:400;color:rgba(26,26,24,0.3) }
    .wr-faq details[open] summary::after { content:'\\2212' }
    .wr-faq .wr-faq-a { font-family:'DM Sans',sans-serif;font-size:14px;color:rgba(26,26,24,0.65);line-height:1.7;padding:16px 24px 24px;background:#fff }
    /* dark promise section */
    .wr-dark { background:#1A1A18;padding:56px 64px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center }
    .wr-dark h3 { font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#FDFCFB;margin:0 0 16px }
    .wr-dark p { font-size:15px;color:rgba(253,252,251,0.7);line-height:1.75;margin-bottom:14px }
    .wr-dark p:last-child { margin-bottom:0 }
    .wr-dark-stats { display:grid;grid-template-columns:1fr 1fr;gap:20px }
    .wr-dark-stat-num { font-family:'DM Sans',sans-serif;font-size:32px;font-weight:700;color:#D4860A;line-height:1.1 }
    .wr-dark-stat-label { font-size:12px;color:rgba(253,252,251,0.4);margin-top:6px }

    /* console tiers */
    .wr-console-grid { display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;margin-top:32px }
    .wr-console { background:#fff;padding:24px }
    .wr-console h4 { font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1A1A18;margin:0 0 4px }
    .wr-console-tag { font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#D4860A;margin-bottom:8px;display:block }
    .wr-console p { font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6;margin:0 }

    .wr-stick { position:fixed;bottom:0;left:0;right:0;z-index:500;background:#1A1A18;color:#FDFCFB;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;font-family:'DM Sans',sans-serif;transform:translateY(100%);transition:transform 0.3s }
    .wr-stick.visible { transform:translateY(0) }
    .wr-stick-title { font-size:15px;font-weight:600 }
    .wr-stick-sub { font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }
    .wr-stick-cta { background:#C0392B;color:#fff;padding:10px 22px;font-size:13px;font-weight:600;text-decoration:none;border-radius:2px }
    .wr-stick-ghost { color:rgba(255,255,255,0.7);font-size:13px;font-weight:500;text-decoration:none;padding:10px 16px;border:1px solid rgba(255,255,255,0.2);border-radius:2px }
  </style>
  <script>
    (function(){
      var bar=null;
      window.addEventListener('scroll',function(){
        if(!bar)bar=document.getElementById('wr-stick');
        if(!bar)return;
        bar.classList.toggle('visible',window.scrollY>500);
      });
    })();
  </script>

  <!-- ── HERO ── -->
  <section class="wr-hero">
    <div class="wr-hero-text">
      <div class="wr-eyebrow">Buyer Protection</div>
      <h1 style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 20px">VK Warranty</h1>
      <p style="font-size:17px;color:rgba(26,26,24,0.6);line-height:1.65;max-width:460px;margin:0 0 28px">We add one free year to every manufacturer warranty. No registration required. Plus optional ADH coverage for drops, breaks, and spills.</p>
      <a href="https://vintageking.com/warranty" target="_blank" style="display:inline-block;background:#C0392B;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;letter-spacing:0.02em;align-self:flex-start">Learn More</a>
    </div>
    <div class="wr-hero-stats">
      <div class="wr-hero-stat"><div class="wr-hero-stat-num">+1 Year</div><div class="wr-hero-stat-label">Free on every new purchase</div></div>
      <div class="wr-hero-stat"><div class="wr-hero-stat-num">$0</div><div class="wr-hero-stat-label">No cost, no registration</div></div>
      <div class="wr-hero-stat"><div class="wr-hero-stat-num">30+</div><div class="wr-hero-stat-label">Years backing every sale</div></div>
      <div class="wr-hero-stat"><div class="wr-hero-stat-num">ADH</div><div class="wr-hero-stat-label">Optional accidental damage plans</div></div>
    </div>
  </section>

  <!-- ── NEW GEAR WARRANTY ── -->
  <section class="wr-section wr-section-white">
    <div class="wr-wrap">
      <div class="wr-eyebrow">New Gear</div>
      <h2 class="wr-h2">World-Class Warranty on Every New Purchase</h2>
      <p class="wr-body">Most new items at Vintage King include a FREE extended warranty. If the manufacturer offers one year, you get two. If they offer five, you get six. We add one year to the standard manufacturer warranty at no charge, no registration required.</p>
      <p class="wr-body">This isn't a gimmick — it's a commitment Mike and Andrew Nehra made when they started Vintage King. They'd bought broken, incomplete junk for their own studio and swore they'd never let that happen to a customer.</p>
    </div>
  </section>

  <!-- ── THE VK PROMISE — DARK SECTION ── -->
  <div class="wr-dark">
    <div>
      <h3>The Vintage King Promise</h3>
      <p>In the early days of Vintage King, owners Mike and Andrew Nehra would buy vintage gear for their recording studio and often receive broken and incomplete junk in need of repair.</p>
      <p>When Vintage King became a retailer, they made a pledge to never let that happen to any of their customers. Not once. That's why Vintage King offers an industry-leading level of technical service and warranty support — the likes of which has never been surpassed.</p>
      <p>Every used and vintage item is serviced by our in-house tech team before it ships. Every new item gets an extra year of warranty coverage at no cost. This isn't a marketing claim — it's the founding principle of the company.</p>
    </div>
    <div class="wr-dark-stats">
      <div><div class="wr-dark-stat-num">30+</div><div class="wr-dark-stat-label">Years in business</div></div>
      <div><div class="wr-dark-stat-num">+1 Year</div><div class="wr-dark-stat-label">Free on every new item</div></div>
      <div><div class="wr-dark-stat-num">In-House</div><div class="wr-dark-stat-label">Tech Shop service</div></div>
      <div><div class="wr-dark-stat-num">$0</div><div class="wr-dark-stat-label">No registration needed</div></div>
    </div>
  </div>

  <!-- ── THREE TIERS ── -->
  <section class="wr-section wr-section-off">
    <div class="wr-wrap">
      <div class="wr-eyebrow">Coverage Tiers</div>
      <h2 class="wr-h2">Three Levels of Protection</h2>
      <p class="wr-sub">Every tier starts automatically at the time of purchase.</p>

      <div class="wr-tier-grid">
        <div class="wr-tier">
          <div class="wr-tier-tag">Included free</div>
          <h3>Manufacturer Warranty</h3>
          <div class="wr-tier-period">Standard term</div>
          <p>Full manufacturer coverage against defects in materials and workmanship. Term varies by brand — typically 1 to 5 years.</p>
          <ul>
            <li>Original defects covered</li>
            <li>Parts and labor included</li>
            <li>Authorized service centers</li>
          </ul>
        </div>
        <div class="wr-tier">
          <div class="wr-tier-tag">Included free</div>
          <h3>VK Extended Warranty</h3>
          <div class="wr-tier-period">+1 year beyond manufacturer</div>
          <p>Vintage King adds one free year on top of the manufacturer term. Same coverage, same protection, zero extra cost.</p>
          <ul>
            <li>Automatic — no registration</li>
            <li>Same terms as manufacturer</li>
            <li>VK Tech Shop backs every claim</li>
          </ul>
        </div>
        <div class="wr-tier">
          <div class="wr-tier-tag">Optional add-on</div>
          <h3>ADH Protection Plan</h3>
          <div class="wr-tier-period">Up to 5 years</div>
          <p>Accidental Damage and Handling coverage from Extend. No-deductible protection against drops, breaks, and spills.</p>
          <ul>
            <li>Speaker drivers, mic capsules, tubes</li>
            <li>Drops, breaks, and spills</li>
            <li>Extends to cover mechanical failure after manufacturer warranty expires</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ── ADH DETAIL ── -->
  <section class="wr-section wr-section-white">
    <div class="wr-wrap">
      <div class="wr-eyebrow">Accidental Damage</div>
      <h2 class="wr-h2">ADH Plans by Extend</h2>
      <p class="wr-body">Available on most new and VK-serviced used items for a low cost proportional to the price of the equipment. Plans start at the time of delivery and last the full purchased term.</p>

      <div class="wr-adh-covers">
        <div class="wr-adh-item"><h4>Drops</h4><p>Accidental falls and impacts</p></div>
        <div class="wr-adh-item"><h4>Breaks</h4><p>Physical damage to enclosures and components</p></div>
        <div class="wr-adh-item"><h4>Spills</h4><p>Liquid damage to electronics</p></div>
        <div class="wr-adh-item"><h4>Speaker Drivers</h4><p>Blown drivers from accidental overload</p></div>
        <div class="wr-adh-item"><h4>Mic Capsules</h4><p>Capsule damage not covered by standard warranty</p></div>
        <div class="wr-adh-item"><h4>Tubes</h4><p>Vacuum tube failure from handling</p></div>
      </div>

      <p class="wr-body" style="margin-top:32px">If your ADH plan lasts longer than the manufacturer warranty, it also covers mechanical and electrical failure once the manufacturer term expires — functioning as a true extended warranty.</p>
    </div>
  </section>

  <!-- ── USED GEAR WARRANTY ── -->
  <section class="wr-section wr-section-off">
    <div class="wr-wrap">
      <div class="wr-eyebrow">Used and Vintage</div>
      <h2 class="wr-h2">Used Gear Warranty Coverage</h2>
      <p class="wr-sub">Every used and vintage item is serviced by our in-house tech team before shipping. Industry-leading warranty included.</p>

      <div class="wr-used-grid">
        <div class="wr-used">
          <h4>Analog Rack Gear</h4>
          <div class="wr-used-period">1 Year</div>
          <p>Compressors, preamps, EQs, and analog processors. Full parts and labor warranty from the VK Tech Shop.</p>
        </div>
        <div class="wr-used">
          <h4>Microphones</h4>
          <div class="wr-used-period">6 Months</div>
          <p>Large and small diaphragm condensers, ribbons, dynamics. Capsule, tube, and electronics tested before sale.</p>
        </div>
        <div class="wr-used">
          <h4>Digital Products</h4>
          <div class="wr-used-period">30 Days</div>
          <p>Interfaces, converters, digital processors. Fully tested and verified operational before shipping.</p>
        </div>
      </div>

      <p class="wr-body" style="margin-top:32px">ADH plans from Extend are also available on VK-serviced used items.</p>

      <div class="wr-eyebrow" style="margin-top:48px">Console Warranty Tiers</div>
      <h2 class="wr-h2" style="font-size:28px">Recording Consoles</h2>
      <p class="wr-sub">Due to the size and complexity of recording consoles, warranty coverage varies by servicing level.</p>

      <div class="wr-console-grid">
        <div class="wr-console">
          <span class="wr-console-tag">Brokered</span>
          <h4>As-Is with Tech Report</h4>
          <p>VK represents the sale on behalf of the owner. Detailed third-party tech report when possible. No warranty included. VK handles decommissioning, freight, and payment.</p>
        </div>
        <div class="wr-console">
          <span class="wr-console-tag">Tested with fault report</span>
          <h4>Fair Market Value</h4>
          <p>Owned by VK, priced to reflect needed work. Cleaned, tested, guaranteed to power up on delivery. Tech report details all flaws. No warranty included.</p>
        </div>
        <div class="wr-console">
          <span class="wr-console-tag">Serviced</span>
          <h4>30-Day Module Warranty</h4>
          <p>Fully functioning, thorough cleaning and testing by VK techs. Faults repaired to factory spec. 30-day warranty on removable modules and power supplies.</p>
        </div>
        <div class="wr-console">
          <span class="wr-console-tag">Premium restoration</span>
          <h4>1-Year Module Warranty</h4>
          <p>Serviced to order upon deposit. Craftsmanship that exceeds expectations. One-year warranty on all removable modules and power supplies.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── FAQ ── -->
  <section class="wr-section wr-section-white">
    <div class="wr-wrap">
      <div class="wr-eyebrow">Frequently Asked Questions</div>
      <h2 class="wr-h2" style="margin-bottom:32px">Warranty FAQ</h2>

      <div class="wr-faq">
        <details><summary>Do I need to register for the VK extended warranty?</summary><div class="wr-faq-a">No. The +1 year extended warranty is automatic on all new purchases. No registration, no extra cost.</div></details>
        <details><summary>What does the ADH plan cover that the regular warranty doesn't?</summary><div class="wr-faq-a">The ADH plan covers accidental damage — drops, breaks, spills — plus components like speaker drivers, mic capsules, and tubes that are typically excluded from standard warranties.</div></details>
        <details><summary>Does used gear come with a warranty?</summary><div class="wr-faq-a">Yes. Analog rack gear: 1 year. Microphones: 6 months. Digital: 30 days. All items are serviced by VK's in-house tech team before shipping.</div></details>
        <details><summary>How do I file a warranty claim?</summary><div class="wr-faq-a">Contact Customer Service at 1.888.653.1184 (press 2) or email customerservice@vintageking.com. If covered, we'll create a Return Authorization and handle the process from there.</div></details>
        <details><summary>Who pays for shipping on warranty repairs?</summary><div class="wr-faq-a">You are responsible for shipping costs to and from VK for warranty repairs, unless the manufacturer's specific warranty policy covers shipping. International customers should contact VK before arranging any warranty repair.</div></details>
        <details><summary>What about consoles?</summary><div class="wr-faq-a">Consoles have separate warranty tiers: brokered consoles are sold as-is with a tech report. "Tested with Fault Report" consoles are priced to reflect needed work. Serviced consoles include a 30-day warranty on modules and power supplies. Premium Restoration consoles include a 1-year warranty on all removable modules and power supplies.</div></details>
      </div>
    </div>
  </section>

  <!-- ── CTA ── -->
  <section class="wr-section wr-section-cta">
    <div class="wr-wrap" style="text-align:center">
      <div class="wr-eyebrow">Need Help?</div>
      <h2 class="wr-h2" style="margin:0 auto 16px">Not Sure if You're Covered?</h2>
      <p style="font-family:'DM Sans',sans-serif;font-size:15px;color:rgba(26,26,24,0.6);max-width:520px;margin:0 auto 32px;line-height:1.6">Contact our Customer Service team to check your warranty status, learn about ADH coverage, or start a claim. We're here Monday through Friday, 10 AM to 6 PM ET.</p>
      <a href="https://vintageking.com/contact" target="_blank" style="display:inline-block;background:#C0392B;color:#fff;padding:14px 32px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border-radius:2px;margin-right:12px">Contact Us</a>
      <a href="tel:18886531184" style="display:inline-block;background:transparent;color:#1A1A18;padding:13px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;border:1px solid rgba(26,26,24,0.25);border-radius:2px">Call 888.653.1184</a>
    </div>
  </section>

  <!-- STICKY BAR -->
  <div class="wr-stick" id="wr-stick">
    <div>
      <div class="wr-stick-title">VK Warranty</div>
      <div class="wr-stick-sub">Free +1 year on every new purchase · ADH plans available</div>
    </div>
    <div style="display:flex;gap:10px;align-items:center">
      <a href="https://vintageking.com/warranty" target="_blank" class="wr-stick-cta">Learn More</a>
      <a href="audio-consultants.html" class="wr-stick-ghost">Ask an Expert</a>
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
