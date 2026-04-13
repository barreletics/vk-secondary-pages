#!/usr/bin/env python3
"""Build careers.html — VK Careers standalone page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "VK-secondary-pages-source.html"
OUT  = ROOT / "careers.html"

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
        "<title>Careers at Vintage King — Join the Pro Audio Outfitter | Vintage King</title>",
        head_css, count=1, flags=re.S
    )
    head_css += """\
  <meta name="description" content="Join Vintage King Audio — the world's most respected pro audio dealer. We're hiring Audio Consultants and studio experts. Work with fellow creatives. Do what you love.">
  <style id="vk-standalone-patch">
    .page { display: block !important; }
  </style>
"""

    json_ld = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "Audio Consultant",
  "description": "Vintage King Audio Consultants engage directly with clients daily, providing hands-on service from initial consultations to follow-up after fulfillment. Applicants should have four or more years of experience in pro audio retail.",
  "hiringOrganization": {
    "@type": "Organization",
    "name": "Vintage King Audio",
    "sameAs": "https://vintageking.com",
    "logo": "https://vintageking.com/images/vk-logo.png"
  },
  "jobLocation": [
    {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Detroit", "addressRegion": "MI", "addressCountry": "US"}},
    {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Los Angeles", "addressRegion": "CA", "addressCountry": "US"}},
    {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Nashville", "addressRegion": "TN", "addressCountry": "US"}}
  ],
  "jobLocationType": "TELECOMMUTE",
  "employmentType": "FULL_TIME",
  "url": "https://vintageking.com/careers"
}
</script>
"""

    chrome = """\
<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <a href="about.html" style="color:rgba(255,255,255,0.55);text-decoration:none">About VK</a>
  <span style="opacity:0.35">|</span>
  <a href="hall-of-fame.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Hall of Fame</a>
  <span style="opacity:0.35">|</span>
  <a href="make-your-mark.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Make Your Mark</a>
  <span style="opacity:0.35">|</span>
  <a href="playback.html" style="color:rgba(255,255,255,0.55);text-decoration:none">PLAYBACK</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Careers</span>
</nav>
"""

    page_body = """\
<div id="careers" class="page active">
  <div id="nav-careers"></div>

  <!-- ── HERO ── -->
  <section style="background:#EDE8E2;padding:88px 0 72px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
      <div>
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Now Hiring · Full-Time &amp; Remote</div>
        <h1 style="font-family:var(--font-display);font-size:54px;font-weight:500;line-height:1.05;margin:0 0 24px;color:var(--near-black)">Join the Team<br>at Vintage King</h1>
        <p style="font-size:16px;color:#5A5550;line-height:1.75;margin-bottom:10px">The world's most respected pro audio dealer is growing. We're looking for studio experts, audio consultants, and passionate creatives to join a team of 100+ people who live and breathe this craft.</p>
        <p style="font-size:14px;color:#7A706A;line-height:1.6;margin-bottom:36px">Musicians. Engineers. Producers. Techs. If great sound is your life's work, this is your next chapter.</p>
        <div style="display:flex;align-items:center;gap:24px;flex-wrap:wrap">
          <a href="#openings" style="background:var(--vk-red);color:#fff;padding:13px 28px;border-radius:3px;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.02em">See Open Roles →</a>
          <a href="#open-resume" style="font-size:13px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:#5A5550;text-decoration:none">Send Your Resume ↓</a>
        </div>
      </div>
      <!-- Stats block -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:rgba(26,26,24,0.12);border-radius:4px;overflow:hidden">
        <div style="background:#EDE8E2;padding:36px 28px">
          <div style="font-family:var(--font-display);font-size:44px;font-weight:700;color:var(--near-black);line-height:1">30+</div>
          <div style="font-size:13px;color:#7A706A;margin-top:6px;letter-spacing:0.04em">Years in Business</div>
        </div>
        <div style="background:#EDE8E2;padding:36px 28px">
          <div style="font-family:var(--font-display);font-size:44px;font-weight:700;color:var(--near-black);line-height:1">100+</div>
          <div style="font-size:13px;color:#7A706A;margin-top:6px;letter-spacing:0.04em">Team Members</div>
        </div>
        <div style="background:#EDE8E2;padding:36px 28px">
          <div style="font-family:var(--font-display);font-size:44px;font-weight:700;color:var(--near-black);line-height:1">∞</div>
          <div style="font-size:13px;color:#7A706A;margin-top:6px;letter-spacing:0.04em">Remote Friendly</div>
        </div>
        <div style="background:#EDE8E2;padding:36px 28px">
          <div style="font-family:var(--font-display);font-size:44px;font-weight:700;color:var(--near-black);line-height:1">1993</div>
          <div style="font-size:13px;color:#7A706A;margin-top:6px;letter-spacing:0.04em">Founded</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── WHY VK — 4-card culture strip ── -->
  <section style="background:var(--off-white);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="margin-bottom:48px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:12px">Why Vintage King</div>
        <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:var(--near-black);margin:0">A career worth showing up for.</h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">

        <div style="background:#fff;border-radius:4px;padding:32px 28px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
          <div style="width:40px;height:3px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:14px">Work With Fellow Creatives</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin:0">Musicians, producers, engineers, and techs — 100+ people who all share one thing: a real passion for making music. Creative, collaborative, and unlike anywhere else.</p>
        </div>

        <div style="background:#fff;border-radius:4px;padding:32px 28px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
          <div style="width:40px;height:3px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:14px">Do What You Love</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin:0">Stop squeezing your passion into free time. At VK, your dedication to audio isn't a hobby — it's exactly what the job requires. You'll be celebrated for it.</p>
        </div>

        <div style="background:#fff;border-radius:4px;padding:32px 28px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
          <div style="width:40px;height:3px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:14px">Opportunity for Growth</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin:0">Many of our team members have held multiple impactful roles here over decades — some since the original VK warehouse. Careers, not jobs.</p>
        </div>

        <div style="background:#fff;border-radius:4px;padding:32px 28px;box-shadow:0 2px 12px rgba(0,0,0,0.06)">
          <div style="width:40px;height:3px;background:var(--vk-red);margin-bottom:24px"></div>
          <div style="font-family:var(--font-display);font-size:20px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:14px">Stellar Benefits &amp; Perks</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin:0">Medical, dental, and vision options. Gear discounts. Training on the latest tech. On-site amenities. Company events. The full picture.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ── CURRENT OPENINGS ── -->
  <section id="openings" style="background:#fff;padding:80px 0;border-top:1px solid rgba(26,26,24,0.08)">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:16px;margin-bottom:48px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600">Current Openings</div>
        <div style="flex:1;height:1px;background:rgba(26,26,24,0.1)"></div>
      </div>

      <!-- Audio Consultant role card -->
      <div style="display:grid;grid-template-columns:1fr 420px;gap:56px;align-items:start">
        <div>
          <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.4);font-weight:600;margin-bottom:12px">Full-Time · Remote Available</div>
          <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:var(--near-black);margin:0 0 20px;line-height:1.15">Audio Consultant</h2>
          <div style="width:48px;height:3px;background:var(--vk-red);margin-bottom:28px"></div>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.75;margin-bottom:16px">For over 30 years, Vintage King has been synonymous with the best in pro audio. We're looking for Audio Consultants who engage directly with clients — from initial consultations to post-sale follow-up — ensuring every customer's needs are met with expertise and care.</p>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.75;margin-bottom:32px">Whether working from our Michigan headquarters, our LA or Nashville showrooms, or remotely, you'll be on the frontlines of the audio industry — working with recording studios, post-production facilities, live sound venues, houses of worship, and educational institutions.</p>

          <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:var(--near-black);font-weight:600;margin-bottom:16px">Responsibilities &amp; Requirements</div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px">
            <li style="display:flex;gap:12px;align-items:baseline"><span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span><span style="font-size:14px;color:var(--mid-grey);line-height:1.6">Responsible for achieving annual profitability targets</span></li>
            <li style="display:flex;gap:12px;align-items:baseline"><span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span><span style="font-size:14px;color:var(--mid-grey);line-height:1.6">Strong knowledge and genuine passion for audio gear</span></li>
            <li style="display:flex;gap:12px;align-items:baseline"><span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span><span style="font-size:14px;color:var(--mid-grey);line-height:1.6">Ability to build long-term client relationships</span></li>
            <li style="display:flex;gap:12px;align-items:baseline"><span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span><span style="font-size:14px;color:var(--mid-grey);line-height:1.6">4+ years selling pro audio or musical instruments</span></li>
            <li style="display:flex;gap:12px;align-items:baseline"><span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span><span style="font-size:14px;color:var(--mid-grey);line-height:1.6">Experience outfitting studios from inception to completion</span></li>
            <li style="display:flex;gap:12px;align-items:baseline"><span style="color:var(--vk-red);font-weight:700;flex-shrink:0">—</span><span style="font-size:14px;color:var(--mid-grey);line-height:1.6">CRM experience a plus</span></li>
          </ul>
        </div>

        <!-- Apply sidebar -->
        <div style="background:var(--off-white);border-radius:4px;padding:36px;position:sticky;top:80px">
          <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Apply Now</div>
          <div style="font-family:var(--font-display);font-size:22px;font-weight:500;color:var(--near-black);margin-bottom:12px;line-height:1.3">Audio Consultant</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin-bottom:24px">If you're the go-to expert in your network — the one people rely on for studio gear decisions — we want to hear from you.</p>
          <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px">
            <div style="display:flex;align-items:center;gap:10px;font-size:13px;color:var(--mid-grey)">
              <span style="color:var(--vk-red);font-weight:700">✓</span> Remote or on-site
            </div>
            <div style="display:flex;align-items:center;gap:10px;font-size:13px;color:var(--mid-grey)">
              <span style="color:var(--vk-red);font-weight:700">✓</span> Gear discounts
            </div>
            <div style="display:flex;align-items:center;gap:10px;font-size:13px;color:var(--mid-grey)">
              <span style="color:var(--vk-red);font-weight:700">✓</span> Medical, dental, vision
            </div>
            <div style="display:flex;align-items:center;gap:10px;font-size:13px;color:var(--mid-grey)">
              <span style="color:var(--vk-red);font-weight:700">✓</span> Growth from within
            </div>
          </div>
          <a href="mailto:careers@vintageking.com" style="display:block;background:var(--vk-red);color:#fff;padding:14px 20px;border-radius:3px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.02em">Apply for This Role →</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── OPEN RESUME CTA ── -->
  <section id="open-resume" style="background:#1A1A18;padding:72px 0">
    <div style="max-width:760px;margin:0 auto;padding:0 40px;text-align:center">
      <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:rgba(255,255,255,0.4);font-weight:600;margin-bottom:16px">Don't See the Right Role?</div>
      <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:#fff;margin:0 0 16px;line-height:1.2">Send Your Resume Anyway</h2>
      <p style="font-size:15px;color:rgba(255,255,255,0.55);line-height:1.75;margin:0 0 36px">If you don't see a position that fits right now, send us your resume and a note about yourself. We'll keep it on file — and reach out when the right role opens up.</p>
      <a href="mailto:careers@vintageking.com" style="display:inline-block;background:var(--vk-red);color:#fff;padding:14px 32px;border-radius:3px;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.02em">Send Your Resume →</a>
      <div style="margin-top:16px;font-size:13px;color:rgba(255,255,255,0.3)">careers@vintageking.com</div>
    </div>
  </section>

  <div id="footer-careers"></div>
</div>
"""

    inline_js = """\
<script>
  (function() {
    var p = 'careers';
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
