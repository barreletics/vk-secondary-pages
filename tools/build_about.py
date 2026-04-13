#!/usr/bin/env python3
"""Build about.html — About VK standalone page (T1 dark template)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "VK-secondary-pages-source.html"
OUT  = ROOT / "about.html"

def slice_lines(path, start, end):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    return "".join(lines[start - 1 : end])

def build():
    # --- Extract shared pieces from source ---
    head_css   = slice_lines(SRC, 1, 1724)   # <head> open through </style>
    nav_tpl    = slice_lines(SRC, 1759, 2480) # <template id="nav-template"> ... </template>
    foot_tpl   = slice_lines(SRC, 3869, 3978) # <template id="footer-template"> ... </template>
    js_nav_meg = slice_lines(SRC, 3980, 4074) # mega-menu / nav interaction JS

    # Patch <title>
    head_css = re.sub(
        r"<title>.*?</title>",
        "<title>About Vintage King — Pro Audio Outfitter Since 1993</title>",
        head_css, count=1, flags=re.S
    )

    # Add standalone-patch so .page is visible without .active
    head_css += """\
  <style id="vk-standalone-patch">
    .page { display: block !important; }
  </style>
"""

    json_ld = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About Vintage King Audio",
  "url": "https://vintageking.com/about",
  "description": "Vintage King Audio is the pro audio outfitter for all sonic journeys. Founded in 1993, selling new, used, and vintage professional audio gear with studio installation services worldwide.",
  "provider": {
    "@type": "Organization",
    "name": "Vintage King Audio",
    "url": "https://vintageking.com",
    "foundingDate": "1993",
    "telephone": "+18886531184",
    "sameAs": [
      "https://www.instagram.com/vintagekingaudio",
      "https://www.youtube.com/vintagekingaudio",
      "https://www.facebook.com/vintagekingaudio"
    ]
  }
}
</script>
"""

    chrome = """\
<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">About VK</span>
</nav>
"""

    # amber for secondary page accents (not red)
    AMB = "#D4860A"

    page_body = """\
<div id="about" class="page active">
  <div id="nav-about"></div>

  <!-- T2 light split hero — off-white bg, amber accent rule, photo right -->
  <div style="background:var(--warm-white);border-bottom:1px solid var(--pale-grey);padding:80px 0 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center">
      <div style="padding-bottom:80px">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:32px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">About Vintage King</div>
        </div>
        <h1 style="font-family:'Playfair Display',serif;font-size:58px;font-weight:700;color:var(--near-black);line-height:1.04;margin:0 0 24px">We Are<br>Vintage King.</h1>
        <p style="font-size:18px;color:var(--mid-grey);line-height:1.65;margin:0 0 16px;max-width:480px">The Pro Audio Outfitter for all of your sonic journeys.</p>
        <p style="font-size:16px;color:var(--mid-grey);line-height:1.70;margin:0 0 40px;max-width:480px">For over 30 years, we have been committed to equipping our customers with the very best gear, advice, and personal service — anywhere in the world.</p>
        <div style="display:flex;gap:14px;flex-wrap:wrap">
          <a href="tel:18886531184" style="display:inline-flex;align-items:center;gap:8px;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Call 888.653.1184</a>
          <a href="#about-story" style="display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(26,26,24,0.22);color:var(--near-black);font-size:13px;font-weight:500;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.borderColor='rgba(26,26,24,0.55)'" onmouseout="this.style.borderColor='rgba(26,26,24,0.22)'">Our Story</a>
        </div>
      </div>
      <div style="align-self:stretch;display:flex;flex-direction:column">
        <div style="flex:1;background:#E0DDD6;border-radius:3px 3px 0 0;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;min-height:400px">
          <svg width="72" height="56" viewBox="0 0 72 56" fill="none" style="opacity:0.20"><rect x="4" y="4" width="64" height="48" rx="4" stroke="#1A1A18" stroke-width="1.5" stroke-dasharray="6 3"/><circle cx="22" cy="22" r="8" stroke="#1A1A18" stroke-width="1" opacity=".6"/><path d="M4 40 L20 26 L34 38 L50 20 L68 36" stroke="#1A1A18" stroke-width="1" opacity=".4" fill="none"/></svg>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.30)">Team or Studio Photo — VK Photography</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── CREDENTIAL BAR ── -->
  <div style="background:#fff;border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey)">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:repeat(4,1fr)">
      <div style="padding:36px 0;text-align:center;border-right:1px solid var(--pale-grey)">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">30+</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A">Years in Business</div>
      </div>
      <div style="padding:36px 0;text-align:center;border-right:1px solid var(--pale-grey)">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">50K+</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A">Products Available</div>
      </div>
      <div style="padding:36px 0;text-align:center;border-right:1px solid var(--pale-grey)">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">100s</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A">Studios Built Worldwide</div>
      </div>
      <div style="padding:36px 0;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">1993</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A">Founded</div>
      </div>
    </div>
  </div>

  <!-- ── WHO WE ARE / MISSION — white ── -->
  <div style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
      <div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Who We Are</div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">Built on Relationships.<br>Powered by Passion.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 24px">For over 30 years, we have been committed to equipping our customers with the very best gear, advice, and personal service. We believe that great sound can be achieved at any budget — and that the ambitions of our customers should always come first.</p>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0">For us, it is about building long-lasting relationships, not just selling gear. Those beliefs have turned customers into friends — and friends into family. Whether you are just starting out or a seasoned pro, we are here for you.</p>
      </div>
      <div style="border-left:3px solid #D4860A;padding-left:40px">
        <p style="font-family:'Playfair Display',serif;font-size:28px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.45;margin:0 0 24px">"Our mission has always been to help our customers sound their absolute best."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Mike Nehra — Co-Founder</div>
        <div style="margin-top:40px;padding-top:32px;border-top:1px solid var(--pale-grey)">
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">We understand your passion because we live it ourselves. Our vision is to give every customer the freedom to chase their creativity — whatever that looks like.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ── OUR STORY — off-white ── -->
  <div id="about-story" style="background:var(--off-white);padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
      <div>
        <div style="aspect-ratio:4/3;background:#E0DDD6;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px">
          <svg width="64" height="64" viewBox="0 0 64 64" fill="none" style="opacity:0.22"><rect x="4" y="4" width="56" height="56" rx="4" stroke="#1A1A18" stroke-width="1.5" stroke-dasharray="6 3"/><rect x="14" y="18" width="16" height="28" rx="2" stroke="#1A1A18" stroke-width="1" opacity=".7"/><rect x="34" y="24" width="16" height="16" rx="2" stroke="#1A1A18" stroke-width="1" opacity=".7"/><circle cx="22" cy="42" r="4" stroke="#1A1A18" stroke-width="1" opacity=".5"/></svg>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.30)">Team Photo — VK Photography</div>
        </div>
      </div>
      <div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Our Story</div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">We Are Not<br>Just Vintage Gear.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 24px">In 1993, we started as a small vintage gear refurbishing business. What began with a love of classic analog hardware grew into something much bigger — one of the most trusted names in professional audio.</p>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 24px">Today, we carry everything from vintage classics to cutting-edge digital gear. Bringing together the past, present, and future of recording technology, we have assembled the ultimate selection — so you can capture just about any sound you could imagine.</p>
        <a href="#" style="display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.70'" onmouseout="this.style.opacity='1'">Explore what we carry →</a>
      </div>
    </div>
  </div>

  <!-- ── WHAT WE CARRY — white, cards with amber top border ── -->
  <div style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="text-align:center;max-width:600px;margin:0 auto 56px">
        <div style="display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">What We Carry</div>
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 20px">New. Used. Vintage.<br>All of It.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.65;margin:0">We carry the full spectrum — so you can build any rig, at any budget, for any sound.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px">
        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:28px 24px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:12px">New</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0">Authorized dealer for hundreds of leading pro audio brands worldwide. Full warranty, full support.</p>
        </div>
        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:28px 24px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:12px">Used</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0">Inspected and warranted gear at meaningful discounts off new pricing. Every piece checked.</p>
        </div>
        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:28px 24px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:12px">Vintage</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0">Rare pieces sourced, authenticated, and serviced by our in-house specialists. From Neve to Pultec.</p>
        </div>
        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:28px 24px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:12px">Open Box</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0">Tech-inspected demo gear backed by the VK Warranty at below-retail pricing.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ── EXPERTS — off-white ── -->
  <div style="background:var(--off-white);padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="text-align:center;max-width:680px;margin:0 auto 64px">
        <div style="display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Our Team</div>
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 24px">Experts at Your Service.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0">Our team is made up of studio owners, musicians, award-winning engineers, producers, and industry veterans. Unlike a lot of other headset-jockey sales outfits, our knowledge comes from real-world experience.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
        <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:36px 32px">
          <div style="width:48px;height:48px;background:rgba(212,134,10,0.10);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D4860A" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Audio Consultants</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">From choosing your first quality microphone to building a studio from the ground up — our consultants are here to help, not to push a sale.</p>
        </div>
        <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:36px 32px">
          <div style="width:48px;height:48px;background:rgba(212,134,10,0.10);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D4860A" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Gear Technicians</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">The VK Tech Shop services, repairs, and restores professional audio equipment. Vintage iron, modern circuits, boutique builds — all brands, all eras.</p>
        </div>
        <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:36px 32px">
          <div style="width:48px;height:48px;background:rgba(212,134,10,0.10);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D4860A" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Studio Designers</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">Acoustic design, equipment integration, wiring, and full studio builds from concept to completion. Hundreds of studios built worldwide.</p>
        </div>
      </div>
      <div style="margin-top:24px;background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:36px 32px;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center">
        <div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Have a question? We are ready to answer it.</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">From choosing your first quality microphone to building a studio from the ground up — we can help. Call, chat, or request a callback from a live expert.</p>
        </div>
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <a href="tel:18886531184" style="display:inline-flex;align-items:center;gap:8px;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;padding:14px 24px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Call Now</a>
          <a href="#" style="display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(26,26,24,0.22);color:var(--near-black);font-size:13px;font-weight:500;padding:14px 24px;border-radius:3px;text-decoration:none">Live Chat</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ── WHAT WE DO / SERVICES — white ── -->
  <div style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start">
      <div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Services</div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">Anything You Can<br>Dream Up, We Can<br>Bring to Life.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 40px">We believe great sound can be achieved at any budget. Whatever you can imagine, we can help you build it.</p>
        <div style="display:flex;flex-direction:column">
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:#D4860A;border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Advice and Consultation</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:#D4860A;border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Installation Services</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:#D4860A;border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Studio Integration Help</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:#D4860A;border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Acoustics Design and Installation</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:#D4860A;border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Full Studio Outfitting</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0">
            <div style="width:8px;height:8px;background:#D4860A;border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Gear Restoration and Repair</span>
          </div>
        </div>
      </div>
      <div>
        <!-- Tech Shop callout -->
        <div style="background:var(--near-black);border-radius:3px;padding:40px 36px;margin-bottom:20px">
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:16px">The VK Tech Shop</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:26px;font-weight:700;color:#fff;line-height:1.15;margin:0 0 16px">Sonic archivists dedicated to preservation.</h3>
          <p style="font-size:14px;color:rgba(255,255,255,0.55);line-height:1.65;margin:0 0 24px">Repairs, tune-ups, and full restorations by our in-house technicians. All brands. All eras. Any piece of gear you love.</p>
          <a href="#" style="display:inline-flex;align-items:center;gap:8px;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;padding:13px 22px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Learn About the Tech Shop</a>
        </div>
        <!-- Talk CTA -->
        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-radius:3px;padding:32px 36px">
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:14px">Find Your Sound</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Talk to an Audio Consultant</h3>
          <p style="font-size:14px;color:var(--mid-grey);line-height:1.65;margin:0 0 20px">No pressure. Just honest advice from people who live and breathe pro audio.</p>
          <a href="tel:18886531184" style="display:inline-flex;align-items:center;gap:8px;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;padding:13px 22px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">888.653.1184</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ── DISCOVER MORE — off-white link cards ── -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);padding:80px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="text-align:center;margin-bottom:48px">
        <div style="display:flex;align-items:center;justify-content:center;gap:12px;margin-bottom:16px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Discover More</div>
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:var(--near-black);margin:0">Find out more about what makes us<br>your number one resource for pro audio.</h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px">
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:28px 24px;text-decoration:none;display:block;transition:border-color 0.15s" onmouseover="this.style.borderColor='#D4860A'" onmouseout="this.style.borderColor='var(--pale-grey)'">
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:10px">Trade Your Gear</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 16px">Forget the hassle of selling online. Trade in your old gear for cash or credit with us.</p>
          <span style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.04em">Trade your gear →</span>
        </a>
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:28px 24px;text-decoration:none;display:block;transition:border-color 0.15s" onmouseover="this.style.borderColor='#D4860A'" onmouseout="this.style.borderColor='var(--pale-grey)'">
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:10px">Studio Services</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 16px">From turnkey solutions to full installations, our team can help with anything you need for your space.</p>
          <span style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.04em">Learn more →</span>
        </a>
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:28px 24px;text-decoration:none;display:block;transition:border-color 0.15s" onmouseover="this.style.borderColor='#D4860A'" onmouseout="this.style.borderColor='var(--pale-grey)'">
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:10px">Blog</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 16px">The latest in gear news, pro audio interviews, demo videos, studio tips, and beyond.</p>
          <span style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.04em">Read the blog →</span>
        </a>
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:28px 24px;text-decoration:none;display:block;transition:border-color 0.15s" onmouseover="this.style.borderColor='#D4860A'" onmouseout="this.style.borderColor='var(--pale-grey)'">
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:10px">FAQ</div>
          <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 16px">Got a question? We have answers. Read our FAQ for everything you need to know.</p>
          <span style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.04em">Read the FAQs →</span>
        </a>
      </div>
    </div>
  </div>

  <!-- ── CONFIDENCE STRIP — white ── -->
  <div style="background:#fff;border-top:2px solid var(--pale-grey);padding:56px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:repeat(4,1fr);gap:32px">
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">VK Warranty</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Every piece backed by our warranty and 30-day return policy.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Free Shipping</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">All orders over $99. Same-day shipping on most in-stock items.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">0% Financing</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Up to 48 months through the VK Credit Card. Affirm and PayPal also available.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Expert Advice</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Real engineers and musicians on the line. Call, chat, or video — your choice.</p>
      </div>
    </div>
  </div>

  <div id="footer-about"></div>
</div>
"""

    inline_js = """\
<script>
  // Standalone page — inject nav + footer for the single page id
  (function() {
    var p = 'about';
    var navTarget    = document.getElementById('nav-' + p);
    var footerTarget = document.getElementById('footer-' + p);
    var navTpl    = document.getElementById('nav-template');
    var footerTpl = document.getElementById('footer-template');
    if (navTarget && navTpl)    navTarget.innerHTML    = navTpl.innerHTML;
    if (footerTarget && footerTpl) footerTarget.innerHTML = footerTpl.innerHTML;
  })();

  // Cross-page navigation stubs
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
