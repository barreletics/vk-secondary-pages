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

    page_body = """\
<div id="about" class="page active">
  <div id="nav-about"></div>

  <!-- ── HERO: dark full-bleed ── -->
  <div style="position:relative;min-height:520px;display:flex;align-items:flex-end;overflow:hidden;background:var(--near-black)">
    <div style="position:absolute;inset:0;background:linear-gradient(135deg,#0e1014 0%,#1c2028 60%,#111318 100%)">
      <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0.055">
        <svg width="420" height="280" viewBox="0 0 420 280" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="400" height="260" rx="4" stroke="#fff" stroke-width="1.5" stroke-dasharray="8 4"/><rect x="30" y="40" width="100" height="180" rx="2" stroke="#fff" stroke-width="1" opacity=".5"/><rect x="150" y="70" width="240" height="120" rx="2" stroke="#fff" stroke-width="1" opacity=".5"/><circle cx="80" cy="160" r="22" stroke="#fff" stroke-width="1" opacity=".4"/><text x="210" y="220" font-family="sans-serif" font-size="12" fill="#fff" opacity=".2" text-anchor="middle">STUDIO PHOTO — VK PHOTOGRAPHY</text></svg>
      </div>
    </div>
    <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(8,10,12,0.92) 0%,rgba(8,10,12,0.50) 55%,rgba(8,10,12,0.18) 100%)"></div>
    <div style="position:relative;z-index:2;max-width:1280px;margin:0 auto;padding:0 40px 72px;width:100%">
      <div style="display:flex;align-items:flex-start;gap:20px;max-width:720px">
        <div style="width:4px;background:var(--vk-red);align-self:stretch;border-radius:2px;flex-shrink:0;min-height:120px"></div>
        <div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:16px">About Vintage King</div>
          <h1 style="font-family:'Playfair Display',serif;font-size:60px;font-weight:700;color:#fff;line-height:1.02;margin:0 0 24px">We Are<br>Vintage King.</h1>
          <p style="font-size:18px;color:rgba(255,255,255,0.60);line-height:1.65;margin:0 0 36px;max-width:560px">The Pro Audio Outfitter for all of your sonic journeys. Since 1993, we have been committed to equipping our customers with the very best gear, advice, and personal service anywhere.</p>
          <div style="display:flex;gap:14px;flex-wrap:wrap">
            <a href="tel:18886531184" style="display:inline-flex;align-items:center;gap:8px;background:var(--vk-red);color:#fff;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Call 888.653.1184</a>
            <a href="#about-story" style="display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(255,255,255,0.22);color:rgba(255,255,255,0.80);font-size:13px;font-weight:500;letter-spacing:0.04em;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.borderColor='rgba(255,255,255,0.55)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.22)'">Our Story</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── CREDENTIAL BAR ── -->
  <div style="background:#fff;border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey)">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:repeat(4,1fr)">
      <div style="padding:36px 0;text-align:center;border-right:1px solid var(--pale-grey)">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">30+</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:var(--vk-red)">Years in Business</div>
      </div>
      <div style="padding:36px 0;text-align:center;border-right:1px solid var(--pale-grey)">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">50K+</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:var(--vk-red)">Products Available</div>
      </div>
      <div style="padding:36px 0;text-align:center;border-right:1px solid var(--pale-grey)">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">100s</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:var(--vk-red)">Studios Built Worldwide</div>
      </div>
      <div style="padding:36px 0;text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:48px;font-weight:700;color:var(--near-black);line-height:1;padding-bottom:14px;border-bottom:1px solid var(--pale-grey);margin-bottom:14px">1993</div>
        <div style="font-size:11px;font-weight:500;letter-spacing:0.10em;text-transform:uppercase;color:var(--vk-red)">Founded</div>
      </div>
    </div>
  </div>

  <!-- ── MISSION STATEMENT — amber bg ── -->
  <div style="background:#F5E6C8;padding:80px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
      <div>
        <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:16px">Who We Are</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">Built on Relationships.<br>Powered by Passion.</h2>
        <p style="font-size:17px;color:var(--near-black);line-height:1.70;margin:0 0 24px;opacity:.75">For over 30 years, we have been committed to equipping our customers with the very best gear, advice, and personal service. We believe that great sound can be achieved at any budget — and that the ambitions of our customers should always come first.</p>
        <p style="font-size:17px;color:var(--near-black);line-height:1.70;margin:0;opacity:.75">For us, it is about building long-lasting relationships, not just selling gear. Those beliefs have turned customers into friends — and friends into family.</p>
      </div>
      <div style="border-left:4px solid var(--vk-red);padding-left:40px">
        <p style="font-family:'Playfair Display',serif;font-size:28px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.45;margin:0 0 20px">"Our mission has always been to help our customers sound their absolute best."</p>
        <div style="font-size:12px;font-weight:600;color:var(--vk-red);letter-spacing:0.08em;text-transform:uppercase">Mike Nehra — Co-Founder</div>
      </div>
    </div>
  </div>

  <!-- ── OUR STORY — white ── -->
  <div id="about-story" style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
      <div>
        <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:16px">Our Story</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">We Are Not<br>Just Vintage Gear.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 24px">In 1993, we started as a small vintage gear refurbishing business. What began with a love of classic analog hardware grew into something much bigger — one of the most trusted names in professional audio, period.</p>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0">Today, we bring together the past, present, and future of recording technology under one roof. Vintage classics. Cutting-edge digital. Everything in between. If you can imagine the sound, we can help you build it.</p>
      </div>
      <div>
        <div style="aspect-ratio:4/3;background:#E8E4DE;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px">
          <svg width="64" height="64" viewBox="0 0 64 64" fill="none" style="opacity:0.22"><rect x="4" y="4" width="56" height="56" rx="4" stroke="#1A1A18" stroke-width="1.5" stroke-dasharray="6 3"/><rect x="14" y="18" width="16" height="28" rx="2" stroke="#1A1A18" stroke-width="1" opacity=".7"/><rect x="34" y="24" width="16" height="16" rx="2" stroke="#1A1A18" stroke-width="1" opacity=".7"/><circle cx="22" cy="42" r="4" stroke="#1A1A18" stroke-width="1" opacity=".5"/></svg>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.30)">Team Photo — VK Photography</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── WHAT WE CARRY — off-white with light cards ── -->
  <div style="background:var(--off-white);padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
        <div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:16px">What We Carry</div>
          <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">New. Used.<br>Vintage. All of It.</h2>
          <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 40px">We carry the full spectrum — from rare vintage classics to the latest digital tools — so you can build any rig, at any budget, for any sound you can imagine.</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
            <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:24px;border-top:3px solid var(--vk-red)">
              <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--near-black);margin-bottom:10px">Vintage</div>
              <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Rare pieces sourced, authenticated, and serviced by our in-house specialists.</p>
            </div>
            <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:24px;border-top:3px solid var(--vk-red)">
              <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--near-black);margin-bottom:10px">Used</div>
              <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Inspected and warranted gear at meaningful discounts off new pricing.</p>
            </div>
            <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:24px;border-top:3px solid var(--vk-red)">
              <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--near-black);margin-bottom:10px">New</div>
              <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Authorized dealer for hundreds of leading pro audio brands worldwide.</p>
            </div>
            <div style="background:#fff;border:1px solid var(--pale-grey);border-radius:3px;padding:24px;border-top:3px solid var(--vk-red)">
              <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--near-black);margin-bottom:10px">Open Box</div>
              <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Tech-inspected demo gear backed by the VK Warranty.</p>
            </div>
          </div>
        </div>
        <div>
          <div style="aspect-ratio:4/3;background:#E0DDD8;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px">
            <svg width="72" height="72" viewBox="0 0 72 72" fill="none" style="opacity:0.18"><rect x="5" y="22" width="62" height="34" rx="3" stroke="#1A1A18" stroke-width="1.5"/><line x1="5" y1="34" x2="67" y2="34" stroke="#1A1A18" stroke-width="1" opacity=".5"/><circle cx="17" cy="28" r="2" stroke="#1A1A18" stroke-width="1" opacity=".6"/><circle cx="27" cy="28" r="2" stroke="#1A1A18" stroke-width="1" opacity=".6"/><rect x="17" y="40" width="10" height="10" rx="1" stroke="#1A1A18" stroke-width="1" opacity=".4"/><rect x="31" y="40" width="10" height="10" rx="1" stroke="#1A1A18" stroke-width="1" opacity=".4"/><rect x="45" y="40" width="10" height="10" rx="1" stroke="#1A1A18" stroke-width="1" opacity=".4"/></svg>
            <div style="font-size:11px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.30)">Gear Photo — VK Photography</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── EXPERTS — amber bg ── -->
  <div style="background:#F5E6C8;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="text-align:center;max-width:680px;margin:0 auto 64px">
        <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:16px">Our Team</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 24px">Experts at Your Service.</h2>
        <p style="font-size:17px;color:var(--near-black);line-height:1.70;margin:0;opacity:.70">Our team is made up of studio owners, musicians, award-winning engineers, producers, and industry veterans. Our knowledge comes from real-world experience — not a headset-jockey sales pitch.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
        <div style="background:#fff;border:1px solid rgba(212,134,10,0.20);border-radius:3px;padding:36px 32px">
          <div style="width:48px;height:48px;background:rgba(192,57,43,0.08);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--vk-red)" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Audio Consultants</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">From choosing your first quality microphone to building a studio from the ground up — our consultants are here to help, not to push a sale.</p>
        </div>
        <div style="background:#fff;border:1px solid rgba(212,134,10,0.20);border-radius:3px;padding:36px 32px">
          <div style="width:48px;height:48px;background:rgba(192,57,43,0.08);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--vk-red)" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Gear Technicians</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">The VK Tech Shop services, repairs, and restores professional audio equipment. Vintage iron, modern circuits, boutique builds — all brands, all eras.</p>
        </div>
        <div style="background:#fff;border:1px solid rgba(212,134,10,0.20);border-radius:3px;padding:36px 32px">
          <div style="width:48px;height:48px;background:rgba(192,57,43,0.08);border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--vk-red)" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
          </div>
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin:0 0 12px">Studio Designers</h3>
          <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">Acoustic design, equipment integration, wiring, and full studio builds from concept to completion. Hundreds of studios built worldwide.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ── WHAT WE DO — white ── -->
  <div style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start">
      <div>
        <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:16px">Services</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 28px">Anything You Can<br>Dream Up.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 40px">We believe great sound can be achieved at any budget. Whatever you can imagine, we can help you build it — from a single mic to a world-class facility.</p>
        <div style="display:flex;flex-direction:column">
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:var(--vk-red);border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Advice and Consultation</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:var(--vk-red);border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Studio Installation Services</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:var(--vk-red);border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Studio Integration Help</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:var(--vk-red);border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Acoustics Design and Installation</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--pale-grey)">
            <div style="width:8px;height:8px;background:var(--vk-red);border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Full Studio Outfitting</span>
          </div>
          <div style="display:flex;align-items:center;gap:16px;padding:18px 0">
            <div style="width:8px;height:8px;background:var(--vk-red);border-radius:50%;flex-shrink:0"></div>
            <span style="font-size:15px;font-weight:500;color:var(--near-black)">Gear Restoration and Repair</span>
          </div>
        </div>
      </div>
      <div style="padding-top:32px">
        <div style="background:var(--near-black);border-radius:3px;padding:48px 40px">
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--vk-red);margin-bottom:20px">Find Your Sound</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#fff;line-height:1.15;margin:0 0 20px">Talk to an Audio Consultant</h3>
          <p style="font-size:15px;color:rgba(255,255,255,0.55);line-height:1.65;margin:0 0 32px">Whether you are just starting out or a seasoned pro, we are here for you. No pressure — just honest advice from people who live and breathe this stuff.</p>
          <div style="display:flex;flex-direction:column;gap:12px">
            <a href="tel:18886531184" style="display:flex;align-items:center;gap:12px;background:var(--vk-red);color:#fff;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;padding:15px 24px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.4 19.79 19.79 0 0 1 1.61 4.83 2 2 0 0 1 3.58 2.63h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.91 10.1a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21.73 17z"/></svg>
              888.653.1184
            </a>
            <a href="#" style="display:flex;align-items:center;gap:12px;border:1px solid rgba(255,255,255,0.18);color:rgba(255,255,255,0.75);font-size:13px;font-weight:500;padding:15px 24px;border-radius:3px;text-decoration:none" onmouseover="this.style.borderColor='rgba(255,255,255,0.45)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.18)'">Live Chat</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── CONFIDENCE STRIP — off-white ── -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);padding:56px 0">
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
