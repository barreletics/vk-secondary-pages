"""trade-program.html — VK Trade Program page."""
import re

SLUG  = "trade-program"
TITLE = "Trade Program — Same-Day Credit on Your Gear | Vintage King"
META  = "Trade your pro audio gear to Vintage King. Free appraisal, written offer within 24 hours, same-day trade credit toward any purchase. Cash also available."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "name": "Vintage King Trade Program",
      "provider": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com", "telephone": "+18886531184"},
      "description": "Trade your pro audio gear to Vintage King. Free appraisal, written offer within 24 hours, same-day trade credit toward any purchase. Cash, check, or wire also available.",
      "serviceType": "Audio Equipment Trade-In"
    },
    {
      "@type": "HowTo",
      "name": "How to Trade Gear to Vintage King",
      "step": [
        {"@type": "HowToStep", "position": 1, "name": "Submit Your Gear", "text": "Fill out the trade form or call 888.653.1184. Describe your gear and condition."},
        {"@type": "HowToStep", "position": 2, "name": "Get Your Offer", "text": "A VK gear specialist responds within 1 business day with a fair market offer in writing."},
        {"@type": "HowToStep", "position": 3, "name": "Trade Up or Cash Out", "text": "Choose same-day trade credit toward any purchase, or cash via check, wire, or PayPal."}
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
  <a href="studio-professionals.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Studio Professionals</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Trade Program</span>
</nav>
"""

PAGE_BODY = """\
<div id="trade-program" class="page active">
  <div id="nav-trade-program"></div>

  <!-- ── HERO ── -->
  <section style="background:#EDE8E2;padding:96px 0 80px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
        <div>
          <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:20px">Trade &amp; Upgrade</div>
          <h1 style="font-family:var(--font-display);font-size:52px;font-weight:500;line-height:1.05;margin:0 0 24px;color:var(--near-black)">Trade Your Gear.<br>Upgrade Your Studio.</h1>
          <p style="font-size:17px;color:var(--mid-grey);line-height:1.7;margin-bottom:12px">Free appraisal. Written offer within 24 hours. Same-day trade credit toward any purchase — or cash if you prefer.</p>
          <p style="font-size:14px;color:rgba(26,26,24,0.5);line-height:1.65;margin-bottom:40px">High-volume studio accounts receive preferred rates and a dedicated trade contact.</p>
          <div style="display:flex;align-items:center;gap:24px;flex-wrap:wrap">
            <a href="#trade-form" style="background:var(--vk-red);color:#fff;padding:14px 32px;border-radius:3px;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.02em">Get a Trade Quote →</a>
            <a href="#what-we-buy" style="font-size:13px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:rgba(26,26,24,0.45);text-decoration:none">What We Buy ↓</a>
          </div>
        </div>
        <!-- Stats sidebar -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(26,26,24,0.1);border-radius:4px;overflow:hidden">
          <div style="background:#fff;padding:32px 28px;text-align:center">
            <div style="font-family:var(--font-display);font-size:32px;font-weight:500;color:var(--near-black);margin-bottom:6px">24 hr</div>
            <div style="font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.5);font-weight:600">Written Offer</div>
          </div>
          <div style="background:#fff;padding:32px 28px;text-align:center">
            <div style="font-family:var(--font-display);font-size:32px;font-weight:500;color:var(--near-black);margin-bottom:6px">Same Day</div>
            <div style="font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.5);font-weight:600">Trade Credit</div>
          </div>
          <div style="background:#fff;padding:32px 28px;text-align:center">
            <div style="font-family:var(--font-display);font-size:32px;font-weight:500;color:var(--near-black);margin-bottom:6px">Free</div>
            <div style="font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.5);font-weight:600">Appraisal</div>
          </div>
          <div style="background:#fff;padding:32px 28px;text-align:center">
            <div style="font-family:var(--font-display);font-size:32px;font-weight:500;color:var(--near-black);margin-bottom:6px">Cash OK</div>
            <div style="font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.5);font-weight:600">Check · Wire · PayPal</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── 3-STEP PROCESS ── -->
  <section style="background:var(--off-white);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="margin-bottom:48px;text-align:center">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:12px">How It Works</div>
        <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:var(--near-black);margin:0">Submit. Get Credit. Upgrade.</h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:4px;overflow:hidden">

        <div style="background:#fff;padding:44px 40px;position:relative">
          <div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--vk-red)"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:20px">Step 1</div>
          <div style="font-family:var(--font-display);font-size:22px;font-weight:500;color:var(--near-black);margin-bottom:14px;line-height:1.3">Submit Your Gear</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.75;margin:0">Fill out the trade form below or call <a href="tel:8886531184" style="color:var(--near-black);text-decoration:none;font-weight:500">888.653.1184</a>. Describe what you have, its condition, and whether you want credit or cash.</p>
        </div>

        <div style="background:#fff;padding:44px 40px;position:relative">
          <div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--vk-red)"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:20px">Step 2</div>
          <div style="font-family:var(--font-display);font-size:22px;font-weight:500;color:var(--near-black);margin-bottom:14px;line-height:1.3">Get Your Offer</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.75;margin:0">A VK gear specialist reviews your submission and responds within 1 business day with a fair market offer in writing. No obligation to accept.</p>
        </div>

        <div style="background:#fff;padding:44px 40px;position:relative">
          <div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--vk-red)"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:20px">Step 3</div>
          <div style="font-family:var(--font-display);font-size:22px;font-weight:500;color:var(--near-black);margin-bottom:14px;line-height:1.3">Trade Up or Cash Out</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.75;margin:0">Accept your offer and choose: same-day trade credit toward any VK purchase, or cash via check, wire transfer, or PayPal.</p>
        </div>

      </div>

      <!-- Stack tip -->
      <div style="margin-top:24px;background:#fff;border:1px solid rgba(26,26,24,0.08);border-radius:3px;padding:28px 36px;display:flex;align-items:baseline;gap:20px">
        <div style="font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);font-weight:600;flex-shrink:0">Pro Tip</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin:0">Apply trade credit as a down payment, finance the remainder at 0%, then deduct the full purchase under Section 179. First-year out-of-pocket on a major upgrade can approach <strong style="color:var(--near-black)">$0</strong>.</p>
      </div>
    </div>
  </section>

  <!-- ── WHAT WE BUY ── -->
  <section id="what-we-buy" style="background:#fff;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="margin-bottom:48px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:12px">Gear We Want</div>
        <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:var(--near-black);margin:0 0 12px">What We Buy</h2>
        <p style="font-size:15px;color:var(--mid-grey);max-width:540px;line-height:1.7;margin:0">If it's pro audio, we're interested. New, used, or vintage — condition noted, fair market value paid.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(26,26,24,0.08);border-radius:4px;overflow:hidden">

        <div style="background:var(--off-white);padding:32px 28px">
          <div style="font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Microphones</div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px">
            <li style="font-size:13px;color:var(--near-black)">Condenser &amp; Tube</li>
            <li style="font-size:13px;color:var(--near-black)">Dynamic &amp; Ribbon</li>
            <li style="font-size:13px;color:var(--near-black)">Vintage Neumann, AKG, Sony</li>
            <li style="font-size:13px;color:var(--near-black)">Telefunken, Schoeps, Sennheiser</li>
          </ul>
        </div>

        <div style="background:var(--off-white);padding:32px 28px">
          <div style="font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Outboard &amp; Preamps</div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px">
            <li style="font-size:13px;color:var(--near-black)">Compressors &amp; Limiters</li>
            <li style="font-size:13px;color:var(--near-black)">EQs &amp; Channel Strips</li>
            <li style="font-size:13px;color:var(--near-black)">Neve, SSL, API, Focusrite</li>
            <li style="font-size:13px;color:var(--near-black)">Pultec, UA, Manley, Chandler</li>
          </ul>
        </div>

        <div style="background:var(--off-white);padding:32px 28px">
          <div style="font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Consoles &amp; Control</div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px">
            <li style="font-size:13px;color:var(--near-black)">Analog Mixing Consoles</li>
            <li style="font-size:13px;color:var(--near-black)">DAW Control Surfaces</li>
            <li style="font-size:13px;color:var(--near-black)">Neve, SSL, API, Trident</li>
            <li style="font-size:13px;color:var(--near-black)">Avid S6, S1, ICON</li>
          </ul>
        </div>

        <div style="background:var(--off-white);padding:32px 28px">
          <div style="font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Monitors &amp; Interfaces</div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px">
            <li style="font-size:13px;color:var(--near-black)">Studio Monitors</li>
            <li style="font-size:13px;color:var(--near-black)">Audio Interfaces &amp; Converters</li>
            <li style="font-size:13px;color:var(--near-black)">Genelec, ATC, Augspurger</li>
            <li style="font-size:13px;color:var(--near-black)">Prism, Apogee, Antelope</li>
          </ul>
        </div>

      </div>
      <p style="font-size:13px;color:var(--mid-grey);margin-top:20px;text-align:center">Don't see your gear listed? <a href="tel:8886531184" style="color:var(--vk-red);text-decoration:none;font-weight:500">Call us</a> — if it's pro audio, we're likely interested.</p>
    </div>
  </section>

  <!-- ── TRADE FORM ── -->
  <section id="trade-form" style="background:#EDE8E2;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 480px;gap:80px;align-items:start">
      <div>
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Get a Free Quote</div>
        <h2 style="font-family:var(--font-display);font-size:40px;font-weight:500;color:var(--near-black);margin:0 0 20px;line-height:1.1">Tell Us What You Have.</h2>
        <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0 0 32px">Describe your gear below. A VK specialist responds within 1 business day with a written offer. No obligation, no pressure.</p>
        <div style="display:flex;flex-direction:column;gap:16px">
          <div style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;font-size:18px;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6">Written offer within <strong>24 hours</strong></span>
          </div>
          <div style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;font-size:18px;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6">Same-day credit applied toward <strong>any purchase</strong></span>
          </div>
          <div style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;font-size:18px;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6">Cash via check, wire, or PayPal also available</span>
          </div>
          <div style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;font-size:18px;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6">High-volume studios: ask about <strong>preferred trade rates</strong></span>
          </div>
        </div>
      </div>

      <form style="display:flex;flex-direction:column;gap:14px" onsubmit="return false">
        <input type="text" placeholder="Your Name" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(26,26,24,0.15);border-radius:3px;background:#fff;color:var(--near-black);outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(26,26,24,0.15)'">
        <input type="email" placeholder="Email" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(26,26,24,0.15);border-radius:3px;background:#fff;color:var(--near-black);outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(26,26,24,0.15)'">
        <input type="tel" placeholder="Phone (optional)" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(26,26,24,0.15);border-radius:3px;background:#fff;color:var(--near-black);outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(26,26,24,0.15)'">
        <textarea placeholder="Describe your gear — make, model, condition, quantity" rows="4" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(26,26,24,0.15);border-radius:3px;background:#fff;color:var(--near-black);outline:none;resize:vertical" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(26,26,24,0.15)'"></textarea>
        <select style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(26,26,24,0.15);border-radius:3px;background:#fff;color:var(--near-black);outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(26,26,24,0.15)'">
          <option value="" disabled selected>Preferred Payment</option>
          <option>Trade Credit — apply to purchase</option>
          <option>Cash — check or wire</option>
          <option>Cash — PayPal</option>
          <option>Undecided</option>
        </select>
        <button type="submit" style="background:var(--vk-red);color:#fff;border:none;padding:14px 24px;border-radius:3px;font-size:14px;font-weight:600;font-family:var(--font-body);cursor:pointer;letter-spacing:0.02em">Get My Trade Quote →</button>
        <p style="font-size:12px;color:rgba(26,26,24,0.38);margin:0;text-align:center">Or call <a href="tel:8886531184" style="color:var(--near-black);text-decoration:none">888.653.1184</a> · Mon–Sat 9:30AM–9PM ET</p>
      </form>
    </div>
  </section>

  <div id="footer-trade-program"></div>
</div>
"""

INLINE_JS = """\
<script>
  (function() {
    var p = 'trade-program';
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

def build(src_html, head_css, nav_tpl, foot_tpl, js_nav):
    import re
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
