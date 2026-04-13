#!/usr/bin/env python3
"""Build studio-professionals.html — VK Studio Professionals program page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "VK-secondary-pages-source.html"
OUT  = ROOT / "studio-professionals.html"

def slice_lines(path, start, end):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    return "".join(lines[start - 1 : end])

def build():
    head_css   = slice_lines(SRC, 1, 1724)
    nav_tpl    = slice_lines(SRC, 1759, 2480)
    foot_tpl   = slice_lines(SRC, 3869, 3978)
    js_nav_meg = slice_lines(SRC, 3980, 4074)

    head_css = re.sub(
        r"<title>.*?</title>",
        "<title>Studio Professionals — Preferred Pricing &amp; Dedicated Service | Vintage King</title>",
        head_css, count=1, flags=re.S
    )
    head_css += """\
  <meta name="description" content="Vintage King's Studio Professionals program gives recording studios, post houses, educators, and live sound venues a dedicated account manager, preferred pricing, and priority service.">
  <style id="vk-standalone-patch">
    .page { display: block !important; }
  </style>
"""

    json_ld = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Vintage King Studio Professionals Program",
  "description": "Dedicated account management, preferred pricing, trade program access, and priority service for professional recording studios, post production facilities, educational institutions, and live sound venues.",
  "provider": {
    "@type": "Organization",
    "name": "Vintage King Audio",
    "url": "https://vintageking.com",
    "telephone": "+18886531184"
  },
  "areaServed": "Worldwide",
  "audience": {
    "@type": "Audience",
    "audienceType": "Recording studios, post production facilities, educational institutions, live sound venues, broadcast facilities"
  }
}
</script>
"""

    chrome = """\
<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <a href="about.html" style="color:rgba(255,255,255,0.55);text-decoration:none">About VK</a>
  <span style="opacity:0.35">|</span>
  <a href="careers.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Careers</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Studio Professionals</span>
</nav>
"""

    page_body = """\
<div id="studio-professionals" class="page active">
  <div id="nav-studio-professionals"></div>

  <!-- ── HERO T1 DARK ── -->
  <section style="background:#1A1A18;padding:96px 0 80px;position:relative;overflow:hidden">
    <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 50%,rgba(192,57,43,0.08) 0%,transparent 65%);pointer-events:none"></div>
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;position:relative;z-index:1">
      <div style="max-width:660px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:20px">Studio Professionals Program</div>
        <h1 style="font-family:var(--font-display);font-size:56px;font-weight:500;line-height:1.05;margin:0 0 24px;color:#fff">Your Studio Deserves<br>a Pro Partner.</h1>
        <p style="font-size:17px;color:rgba(255,255,255,0.55);line-height:1.7;margin-bottom:12px">Recording studios, post production facilities, educators, and live sound venues work differently than individual buyers. Vintage King's Studio Professionals program is built around that reality.</p>
        <p style="font-size:15px;color:rgba(255,255,255,0.38);line-height:1.65;margin-bottom:40px">Dedicated account manager. Preferred pricing. Priority service. Trade program access. One point of contact for everything.</p>
        <div style="display:flex;align-items:center;gap:24px;flex-wrap:wrap">
          <a href="#apply" style="background:var(--vk-red);color:#fff;padding:14px 32px;border-radius:3px;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.02em">Apply for Pro Access →</a>
          <a href="#benefits" style="font-size:13px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:rgba(255,255,255,0.45);text-decoration:none">See Program Benefits ↓</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── WHO QUALIFIES — segment strip ── -->
  <section style="background:#111;padding:0;border-bottom:1px solid rgba(255,255,255,0.06)">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:flex;align-items:stretch;gap:0;overflow-x:auto">
      <div style="flex:1;min-width:160px;padding:24px 28px;border-right:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;gap:12px">
        <div style="width:6px;height:6px;border-radius:50%;background:var(--vk-red);flex-shrink:0"></div>
        <span style="font-size:13px;color:rgba(255,255,255,0.6);font-weight:500;white-space:nowrap">Recording Studios</span>
      </div>
      <div style="flex:1;min-width:160px;padding:24px 28px;border-right:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;gap:12px">
        <div style="width:6px;height:6px;border-radius:50%;background:var(--vk-red);flex-shrink:0"></div>
        <span style="font-size:13px;color:rgba(255,255,255,0.6);font-weight:500;white-space:nowrap">Post Production</span>
      </div>
      <div style="flex:1;min-width:160px;padding:24px 28px;border-right:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;gap:12px">
        <div style="width:6px;height:6px;border-radius:50%;background:var(--vk-red);flex-shrink:0"></div>
        <span style="font-size:13px;color:rgba(255,255,255,0.6);font-weight:500;white-space:nowrap">EDU &amp; Institutional</span>
      </div>
      <div style="flex:1;min-width:160px;padding:24px 28px;border-right:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;gap:12px">
        <div style="width:6px;height:6px;border-radius:50%;background:var(--vk-red);flex-shrink:0"></div>
        <span style="font-size:13px;color:rgba(255,255,255,0.6);font-weight:500;white-space:nowrap">Live Sound Venues</span>
      </div>
      <div style="flex:1;min-width:160px;padding:24px 28px;border-right:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;gap:12px">
        <div style="width:6px;height:6px;border-radius:50%;background:var(--vk-red);flex-shrink:0"></div>
        <span style="font-size:13px;color:rgba(255,255,255,0.6);font-weight:500;white-space:nowrap">Broadcast &amp; Gaming</span>
      </div>
      <div style="flex:1;min-width:160px;padding:24px 28px;display:flex;align-items:center;gap:12px">
        <div style="width:6px;height:6px;border-radius:50%;background:var(--vk-red);flex-shrink:0"></div>
        <span style="font-size:13px;color:rgba(255,255,255,0.6);font-weight:500;white-space:nowrap">Houses of Worship</span>
      </div>
    </div>
  </section>

  <!-- ── PROGRAM BENEFITS — 6-grid ── -->
  <section id="benefits" style="background:#1A1A18;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="margin-bottom:52px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:12px">Program Benefits</div>
        <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:#fff;margin:0;line-height:1.2">Built for the way facilities buy.</h2>
      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:rgba(255,255,255,0.07);border-radius:4px;overflow:hidden">

        <div style="background:#1A1A18;padding:40px 36px">
          <div style="width:36px;height:2px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;margin-bottom:12px;line-height:1.3">Dedicated Account Manager</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.7;margin:0">One person who knows your facility, your gear, and your budget. No re-explaining every time you call. Priority response guaranteed.</p>
        </div>

        <div style="background:#1A1A18;padding:40px 36px">
          <div style="width:36px;height:2px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;margin-bottom:12px;line-height:1.3">Preferred Pricing</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.7;margin:0">Volume-based preferred rates on gear, bundles, and system builds. High-frequency buyers receive additional savings on recurring orders.</p>
        </div>

        <div style="background:#1A1A18;padding:40px 36px">
          <div style="width:36px;height:2px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;margin-bottom:12px;line-height:1.3">Trade Program Access</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.7;margin:0">Priority trade evaluations with same-day credit toward new purchases. Pro accounts receive preferred trade rates and dedicated trade intake.</p>
        </div>

        <div style="background:#1A1A18;padding:40px 36px">
          <div style="width:36px;height:2px;background:rgba(255,255,255,0.2);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;margin-bottom:12px;line-height:1.3">System Design &amp; Installation</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.7;margin:0">Full-service studio integration from our Design &amp; Integration team. Acoustic planning, gear selection, wiring, patchbay, calibration — turnkey.</p>
        </div>

        <div style="background:#1A1A18;padding:40px 36px">
          <div style="width:36px;height:2px;background:rgba(255,255,255,0.2);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;margin-bottom:12px;line-height:1.3">Financing &amp; Section 179</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.7;margin:0">0% financing up to 48 months. Stack trade credit, finance, and Section 179 to bring first-year out-of-pocket close to zero on major upgrades.</p>
        </div>

        <div style="background:#1A1A18;padding:40px 36px">
          <div style="width:36px;height:2px;background:rgba(255,255,255,0.2);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:#fff;margin-bottom:12px;line-height:1.3">VK Tech Shop Priority</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.7;margin:0">Priority servicing for vintage and outboard gear through the VK Tech Shop. 100+ years of combined experience. All work backed by a 1-year warranty.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ── ELIGIBILITY ── -->
  <section style="background:#fff;padding:80px 0;border-top:1px solid rgba(26,26,24,0.08)">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start">
      <div>
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Who Qualifies</div>
        <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:var(--near-black);margin:0 0 20px;line-height:1.2">Eligibility</h2>
        <div style="width:48px;height:3px;background:var(--vk-red);margin-bottom:28px"></div>
        <p style="font-size:15px;color:var(--mid-grey);line-height:1.75;margin-bottom:24px">The Studio Professionals program is open to any working facility or professional buyer with an active, verifiable audio operation. You don't need to be large — you need to be serious.</p>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px">
          <li style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6"><strong>Recording &amp; Mixing Studios</strong> — commercial or project studios with a gear budget</span>
          </li>
          <li style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6"><strong>Post Production Facilities</strong> — film, TV, gaming, radio, podcast</span>
          </li>
          <li style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6"><strong>Educational Institutions</strong> — music programs, recording schools, university studios</span>
          </li>
          <li style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6"><strong>Live Sound Venues</strong> — clubs, theaters, arenas, touring rigs</span>
          </li>
          <li style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6"><strong>Broadcast &amp; Content</strong> — network studios, streaming facilities, podcasting networks</span>
          </li>
          <li style="display:flex;gap:14px;align-items:baseline">
            <span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span>
            <span style="font-size:14px;color:var(--near-black);line-height:1.6"><strong>Houses of Worship</strong> — church AV teams with ongoing gear needs</span>
          </li>
        </ul>
      </div>

      <!-- Quote + stat block -->
      <div style="display:flex;flex-direction:column;gap:24px">
        <div style="background:var(--off-white);border-radius:4px;padding:36px">
          <div style="font-family:var(--font-display);font-size:20px;font-style:italic;color:var(--near-black);line-height:1.5;margin-bottom:16px">"Vintage King has been fantastic. Chris Bolitho helped me fulfill every dream I had with this studio. He just made everything happen."</div>
          <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--mid-grey);font-weight:600">Jeffery Alan Jones — Alan Audio Works</div>
        </div>
        <div style="background:var(--off-white);border-radius:4px;padding:36px">
          <div style="font-family:var(--font-display);font-size:20px;font-style:italic;color:var(--near-black);line-height:1.5;margin-bottom:16px">"The experience was pretty effortless. They helped me out with the patch bay and all of the cabling. If you buy something big, they take care of everything."</div>
          <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--mid-grey);font-weight:600">Ben Pacheco — Future Perfect Music</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── APPLY CTA ── -->
  <section id="apply" style="background:#1A1A18;padding:80px 0">
    <div style="max-width:760px;margin:0 auto;padding:0 40px;text-align:center">
      <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Get Started</div>
      <h2 style="font-family:var(--font-display);font-size:40px;font-weight:500;color:#fff;margin:0 0 16px;line-height:1.15">Apply for Pro Access</h2>
      <p style="font-size:15px;color:rgba(255,255,255,0.5);line-height:1.75;margin:0 0 40px">Tell us about your facility. An Audio Consultant will follow up within one business day to discuss your program options, preferred pricing, and any active projects.</p>

      <form style="text-align:left;display:flex;flex-direction:column;gap:16px;max-width:560px;margin:0 auto 24px" onsubmit="return false">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
          <input type="text" placeholder="Name" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(255,255,255,0.15);border-radius:3px;background:rgba(255,255,255,0.05);color:#fff;outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(255,255,255,0.15)'">
          <input type="text" placeholder="Facility / Studio Name" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(255,255,255,0.15);border-radius:3px;background:rgba(255,255,255,0.05);color:#fff;outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(255,255,255,0.15)'">
        </div>
        <input type="email" placeholder="Email" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(255,255,255,0.15);border-radius:3px;background:rgba(255,255,255,0.05);color:#fff;outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(255,255,255,0.15)'">
        <select style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(255,255,255,0.15);border-radius:3px;background:#1A1A18;color:rgba(255,255,255,0.6);outline:none" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(255,255,255,0.15)'">
          <option value="" disabled selected>Facility Type</option>
          <option>Recording Studio</option>
          <option>Post Production</option>
          <option>EDU / Institutional</option>
          <option>Live Sound Venue</option>
          <option>Broadcast / Gaming</option>
          <option>House of Worship</option>
          <option>Other</option>
        </select>
        <textarea placeholder="Tell us about your facility and current projects (optional)" rows="3" style="padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(255,255,255,0.15);border-radius:3px;background:rgba(255,255,255,0.05);color:#fff;outline:none;resize:vertical" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(255,255,255,0.15)'"></textarea>
        <button type="submit" style="background:var(--vk-red);color:#fff;border:none;padding:14px 24px;border-radius:3px;font-size:14px;font-weight:600;font-family:var(--font-body);cursor:pointer;letter-spacing:0.02em;text-align:center">Apply for Pro Access →</button>
      </form>
      <p style="font-size:12px;color:rgba(255,255,255,0.25);margin:0">Or call us directly: <a href="tel:8886531184" style="color:rgba(255,255,255,0.4);text-decoration:none">888.653.1184</a> · Mon–Sat 9:30AM–9PM ET</p>
    </div>
  </section>

  <div id="footer-studio-professionals"></div>
</div>
"""

    inline_js = """\
<script>
  (function() {
    var p = 'studio-professionals';
    var navTarget    = document.getElementById('nav-' + p);
    var footerTarget = document.getElementById('footer-' + p);
    var navTpl    = document.getElementById('nav-template');
    var footerTpl = document.getElementById('footer-template');
    if (navTarget && navTpl)    navTarget.innerHTML    = navTpl.innerHTML;
    if (footerTarget && footerTpl) footerTarget.innerHTML = footerTpl.innerHTML;
  })();
  var __vkPageFiles = {
    home:'pages/home.html', category:'pages/category.html', product:'pages/product.html',
    faq:'pages/faq.html', deals:'pages/deals.html', sell:'pages/sell.html',
    studio:'pages/studio.html', techshop:'pages/techshop.html',
    'fin-page':'pages/financing.html', openbox:'pages/openbox.html'
  };
  function injectShared() {}
  function showPage(id) {
    var href = __vkPageFiles[id];
    if (href) window.location.href = href;
  }
  function goToDeals() { window.location.href = 'pages/deals.html'; }
</script>
"""

    html = (
        head_css
        + "\n</head>\n"
        + "<body>\n"
        + chrome
        + nav_tpl
        + foot_tpl
        + json_ld
        + page_body
        + js_nav_meg
        + inline_js
        + "</body>\n</html>\n"
    )

    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    build()
