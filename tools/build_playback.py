#!/usr/bin/env python3
"""Build playback.html — VK PLAYBACK Magazine standalone page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "VK-secondary-pages-source.html"
OUT  = ROOT / "playback.html"

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
        "<title>PLAYBACK Magazine — Stories Behind the Gear | Vintage King</title>",
        head_css, count=1, flags=re.S
    )
    head_css += """\
  <style id="vk-standalone-patch">
    .page { display: block !important; }
  </style>
"""

    json_ld = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Periodical",
  "name": "PLAYBACK Magazine",
  "url": "https://vintageking.com/playback-magazine",
  "description": "PLAYBACK is Vintage King's original magazine featuring in-depth interviews with award-winning engineers, gear reviews, and studio spotlights. Free digital subscription.",
  "publisher": {
    "@type": "Organization",
    "name": "Vintage King Audio",
    "url": "https://vintageking.com"
  },
  "issueNumber": "7"
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
  <span style="opacity:0.75">PLAYBACK</span>
</nav>
"""

    page_body = """\
<div id="playback" class="page active">
  <div id="nav-playback"></div>

  <!-- ── HERO — light warm split ── -->
  <section style="background:#EDE8E2;padding:80px 0 60px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">

      <!-- Left: headline + CTAs -->
      <div>
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">VK Original · 7 Issues · Free</div>
        <h1 style="font-family:var(--font-display);font-size:56px;font-weight:500;line-height:1.05;margin:0 0 24px;color:var(--near-black)">PLAYBACK<br>Magazine</h1>
        <p style="font-size:16px;color:#5A5550;line-height:1.75;margin-bottom:10px">The stories behind the gear. In-depth interviews with the engineers and producers who defined recorded music — from Abbey Road to East Side Sound.</p>
        <p style="font-size:14px;color:#7A706A;line-height:1.6;margin-bottom:36px">Al Schmitt. Glyn Johns. Joe Chiccarelli. Bob Ludwig. Eva Reistad. Just Blaze. Free digital subscription.</p>
        <div style="display:flex;align-items:center;gap:24px;flex-wrap:wrap">
          <a href="#subscribe" class="btn-primary" style="background:var(--vk-red);color:#fff;padding:13px 28px;border-radius:3px;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.02em">Get Free Access →</a>
          <a href="#issues" style="font-size:13px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:#5A5550;text-decoration:none">Browse All Issues ↓</a>
        </div>
      </div>

      <!-- Right: staggered 3-col cover mockup -->
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;align-items:end">
        <!-- Issue 05 — raised -->
        <div style="background:#111;border-radius:4px;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:16px;position:relative;overflow:hidden;margin-bottom:40px;box-shadow:0 8px 32px rgba(0,0,0,0.28)">
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(0,0,0,0.88) 100%)"></div>
          <div style="position:absolute;top:14px;left:16px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.4);font-weight:500">PLAYBACK</div>
          <div style="position:relative;z-index:1">
            <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.38);margin-bottom:5px">Issue 05</div>
            <div style="font-family:var(--font-display);font-size:14px;font-style:italic;color:#fff;line-height:1.3">The SSL Sound</div>
          </div>
        </div>
        <!-- Issue 07 — center tall (latest) -->
        <div style="background:#1A1510;border-radius:4px;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:16px;position:relative;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,0.35)">
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(0,0,0,0.88) 100%)"></div>
          <div style="position:absolute;top:14px;left:16px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--amber);font-weight:600">Latest</div>
          <div style="position:relative;z-index:1">
            <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.38);margin-bottom:5px">Issue 07</div>
            <div style="font-family:var(--font-display);font-size:14px;font-style:italic;color:#fff;line-height:1.3">Many Paths</div>
          </div>
        </div>
        <!-- Issue 06 — raised -->
        <div style="background:#0E0E0E;border-radius:4px;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:16px;position:relative;overflow:hidden;margin-bottom:40px;box-shadow:0 8px 32px rgba(0,0,0,0.28)">
          <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 35%,rgba(0,0,0,0.88) 100%)"></div>
          <div style="position:absolute;top:14px;left:16px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.4);font-weight:500">PLAYBACK</div>
          <div style="position:relative;z-index:1">
            <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.38);margin-bottom:5px">Issue 06</div>
            <div style="font-family:var(--font-display);font-size:14px;font-style:italic;color:#fff;line-height:1.3">Mastering for Vinyl</div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ── DIGITAL MAGAZINE VIEWER ── -->
  <section style="background:#111;padding:72px 0 64px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;text-align:center">
      <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--amber);font-weight:600;margin-bottom:12px">Issue 07 — Now Available</div>
      <h2 style="font-family:var(--font-display);font-size:32px;font-weight:500;color:#fff;margin:0 0 8px">Read PLAYBACK — Free</h2>
      <p style="font-size:14px;color:rgba(255,255,255,0.45);margin:0 0 40px">Flip through the latest issue. Subscribe for access to all seven.</p>

      <!-- Flipbook viewer -->
      <div id="pb-flipbook" style="position:relative;display:inline-flex;align-items:stretch;box-shadow:0 20px 80px rgba(0,0,0,0.6);border-radius:2px;max-width:860px;width:100%">

        <!-- Left page -->
        <div id="pb-page-left" style="flex:1;background:#fff;min-height:540px;padding:40px 36px;text-align:left;position:relative;border-right:1px solid rgba(0,0,0,0.12);display:flex;flex-direction:column;justify-content:flex-start;overflow:hidden;transition:opacity 0.3s">
          <!-- Page content injected by JS -->
        </div>

        <!-- Right page -->
        <div id="pb-page-right" style="flex:1;background:#fff;min-height:540px;padding:40px 36px;text-align:left;position:relative;display:flex;flex-direction:column;justify-content:flex-start;overflow:hidden;transition:opacity 0.3s">
          <!-- Page content injected by JS -->
        </div>

        <!-- Spine shadow -->
        <div style="position:absolute;left:50%;top:0;bottom:0;width:6px;transform:translateX(-50%);background:linear-gradient(90deg,rgba(0,0,0,0.18),rgba(0,0,0,0.04),rgba(0,0,0,0.18));pointer-events:none"></div>
      </div>

      <!-- Controls -->
      <div style="display:flex;align-items:center;justify-content:center;gap:20px;margin-top:24px">
        <button id="pb-prev" onclick="pbFlip(-1)" style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);color:#fff;width:40px;height:40px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.15s" aria-label="Previous spread">&#8249;</button>
        <span id="pb-counter" style="font-size:13px;color:rgba(255,255,255,0.45);min-width:80px;text-align:center">Spread 1 of 5</span>
        <button id="pb-next" onclick="pbFlip(1)" style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);color:#fff;width:40px;height:40px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.15s" aria-label="Next spread">&#8250;</button>
      </div>
      <div style="margin-top:16px">
        <a href="https://vintageking.com/playback-magazine" target="_blank" rel="noopener" style="font-size:12px;letter-spacing:0.06em;text-transform:uppercase;color:rgba(255,255,255,0.38);text-decoration:none">Full interactive edition at vintageking.com ↗</a>
      </div>
    </div>
  </section>

  <!-- ── INSIDE THIS ISSUE ── -->
  <section style="background:#fff;padding:72px 0;border-top:1px solid rgba(26,26,24,0.08)">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:16px;margin-bottom:36px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600">Issue 07</div>
        <div style="flex:1;height:1px;background:rgba(26,26,24,0.1)"></div>
      </div>
      <h2 style="font-family:var(--font-display);font-size:32px;font-weight:500;color:var(--near-black);margin:0 0 16px;line-height:1.2">Inside This Issue</h2>
      <p style="font-size:15px;color:var(--mid-grey);line-height:1.7;margin:0 0 12px;max-width:680px">The seventh issue of Vintage King's PLAYBACK celebrates the many paths of today's audio industry. Dive into interviews with Just Blaze, Jett Galindo, Sam Evian, Kris Pooley, and Eva Reistad, plus insights from top producers and engineers in rock and metal.</p>
      <p style="font-size:14px;color:rgba(26,26,24,0.45);line-height:1.6;margin:0 0 44px;max-width:680px">We also spotlight the latest studio essentials, including the Cranborne Audio Brick Lane 500 Series compressor, Focal Utopia Main monitors, and Focusrite RedNet TNX interface.</p>

      <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.4);font-weight:600;margin-bottom:20px">More Features From This Issue</div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">

        <!-- Feature card 1 — Eva Reistad -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,0.09);border:1px solid rgba(26,26,24,0.07)">
          <div style="background:#2A2018;height:280px;display:flex;align-items:center;justify-content:center">
            <div style="font-family:var(--font-display);font-size:40px;font-style:italic;color:rgba(255,255,255,0.15)">ER</div>
          </div>
          <div style="padding:22px">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:var(--amber);font-weight:600;margin-bottom:10px">Interview</div>
            <div style="font-family:var(--font-display);font-size:18px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:10px">Five Sounds With Eva Reistad</div>
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0 0 16px">We sat down with GRAMMY Award-winning mixer, producer, and artist Eva Reistad to discuss her approach to making five of her favorite records.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Feature card 2 — SSL Oracle -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,0.09);border:1px solid rgba(26,26,24,0.07)">
          <div style="background:#181A20;height:280px;display:flex;align-items:center;justify-content:center">
            <div style="font-family:var(--font-display);font-size:40px;font-style:italic;color:rgba(255,255,255,0.15)">SSL</div>
          </div>
          <div style="padding:22px">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.4);font-weight:600;margin-bottom:10px">Buyer's Guide</div>
            <div style="font-family:var(--font-display);font-size:18px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:10px">SSL Oracle Console</div>
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0 0 16px">Learn more about SSL's new Oracle console, combining the brand's iconic analog circuitry with new ActiveAnalogue technology.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Feature card 3 — Allaire Studios -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,0.09);border:1px solid rgba(26,26,24,0.07)">
          <div style="background:#101A12;height:280px;display:flex;align-items:center;justify-content:center">
            <div style="font-family:var(--font-display);font-size:40px;font-style:italic;color:rgba(255,255,255,0.15)">AS</div>
          </div>
          <div style="padding:22px">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.4);font-weight:600;margin-bottom:10px">Studio Spotlight</div>
            <div style="font-family:var(--font-display);font-size:18px;font-weight:500;color:var(--near-black);line-height:1.3;margin-bottom:10px">Allaire Studios</div>
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.65;margin:0 0 16px">Meet Randall Wallace, musician, photographer, and owner of Allaire Studios in Woodstock, New York.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

      </div>

      <div style="margin-top:36px;display:flex;align-items:center;gap:24px">
        <a href="#subscribe" style="font-size:13px;font-weight:600;letter-spacing:0.02em;color:#fff;text-decoration:none;background:var(--vk-red);padding:13px 28px;border-radius:3px">Get Free Access →</a>
        <a href="https://vintageking.com/playback-magazine" target="_blank" rel="noopener" style="font-size:13px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:var(--mid-grey);text-decoration:none">Read at VintageKing.com ↗</a>
      </div>
    </div>
  </section>

  <!-- ── ALL ISSUES GRID ── -->
  <section id="issues" style="background:var(--off-white);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="margin-bottom:48px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:12px">All Issues</div>
        <h2 style="font-family:var(--font-display);font-size:36px;font-weight:500;color:var(--near-black);margin:0 0 12px">Seven Issues. All Free.</h2>
        <p style="font-size:15px;color:var(--mid-grey);line-height:1.7;max-width:520px;margin:0">Subscribe once, access every issue instantly. New issues added as they're published.</p>
      </div>

      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">

        <!-- Issue 01 -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.07);transition:box-shadow 0.2s">
          <div style="background:#1A1510;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,0.9) 100%)"></div>
            <div style="position:absolute;top:16px;left:20px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-weight:500">PLAYBACK</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);margin-bottom:5px">Issue 01</div>
              <div style="font-family:var(--font-display);font-size:15px;font-style:italic;color:#fff;line-height:1.3">The Making of a Classic</div>
            </div>
          </div>
          <div style="padding:16px 18px">
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 14px">Al Schmitt on 50 years at Capitol Studios, plus the gear that never left his rack.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Issue 02 -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.07)">
          <div style="background:#111215;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,0.9) 100%)"></div>
            <div style="position:absolute;top:16px;left:20px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-weight:500">PLAYBACK</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);margin-bottom:5px">Issue 02</div>
              <div style="font-family:var(--font-display);font-size:15px;font-style:italic;color:#fff;line-height:1.3">Analog Signal Chain</div>
            </div>
          </div>
          <div style="padding:16px 18px">
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 14px">Glyn Johns on recording the Stones and Zeppelin with nothing but the right room and the right gear.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Issue 03 -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.07)">
          <div style="background:#150E10;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,0.9) 100%)"></div>
            <div style="position:absolute;top:16px;left:20px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-weight:500">PLAYBACK</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);margin-bottom:5px">Issue 03</div>
              <div style="font-family:var(--font-display);font-size:15px;font-style:italic;color:#fff;line-height:1.3">Room Sound</div>
            </div>
          </div>
          <div style="padding:16px 18px">
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 14px">Joe Chiccarelli on capturing live room acoustics and why the microphone position matters more than the mic itself.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Issue 04 -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.07)">
          <div style="background:#0D1218;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,0.9) 100%)"></div>
            <div style="position:absolute;top:16px;left:20px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-weight:500">PLAYBACK</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);margin-bottom:5px">Issue 04</div>
              <div style="font-family:var(--font-display);font-size:15px;font-style:italic;color:#fff;line-height:1.3">Vintage Mic Techniques</div>
            </div>
          </div>
          <div style="padding:16px 18px">
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 14px">Bob Ludwig on mastering for loudness wars survivors — and the microphones that hold up after 50 years.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Issue 05 -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.07)">
          <div style="background:#111;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,0.9) 100%)"></div>
            <div style="position:absolute;top:16px;left:20px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-weight:500">PLAYBACK</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);margin-bottom:5px">Issue 05</div>
              <div style="font-family:var(--font-display);font-size:15px;font-style:italic;color:#fff;line-height:1.3">The SSL Sound</div>
            </div>
          </div>
          <div style="padding:16px 18px">
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 14px">How the 4000 Series console defined the sound of an entire decade of pop and rock recording.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Issue 06 -->
        <div style="background:#fff;border-radius:4px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,0.07)">
          <div style="background:#0E0E0E;aspect-ratio:2/3;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 40%,rgba(0,0,0,0.9) 100%)"></div>
            <div style="position:absolute;top:16px;left:20px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-weight:500">PLAYBACK</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.35);margin-bottom:5px">Issue 06</div>
              <div style="font-family:var(--font-display);font-size:15px;font-style:italic;color:#fff;line-height:1.3">Mastering for Vinyl</div>
            </div>
          </div>
          <div style="padding:16px 18px">
            <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0 0 14px">Everything that happens between the final mix and the lacquer — and why it changes everything you hear.</p>
            <a href="#subscribe" style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--vk-red);text-decoration:none">Read Free →</a>
          </div>
        </div>

        <!-- Issue 07 — full-width featured -->
        <div style="background:#1A1510;border-radius:4px;overflow:hidden;grid-column:3/5;display:grid;grid-template-columns:1fr 1fr;box-shadow:0 4px 20px rgba(0,0,0,0.18)">
          <div style="aspect-ratio:unset;min-height:300px;background:linear-gradient(135deg,#1A1510 0%,#2A1E0E 100%);display:flex;flex-direction:column;justify-content:flex-end;padding:28px;position:relative;overflow:hidden">
            <div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,0.75) 100%)"></div>
            <div style="position:absolute;top:20px;left:24px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--amber);font-weight:600">Latest Issue</div>
            <div style="position:relative;z-index:1">
              <div style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.38);margin-bottom:6px">Issue 07</div>
              <div style="font-family:var(--font-display);font-size:24px;font-style:italic;color:#fff;line-height:1.2">Many Paths</div>
            </div>
          </div>
          <div style="padding:28px;display:flex;flex-direction:column;justify-content:center">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:var(--amber);font-weight:600;margin-bottom:12px">Now Available</div>
            <p style="font-size:14px;color:rgba(255,255,255,0.65);line-height:1.7;margin:0 0 20px">Featuring Just Blaze, Jett Galindo, Sam Evian, Kris Pooley, and Eva Reistad. Studio spotlight: Allaire Studios. Gear deep-dive: SSL Oracle, Focusrite RedNet TNX.</p>
            <a href="#subscribe" style="display:inline-block;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--amber);text-decoration:none">Read Issue 07 Free →</a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ── SUBSCRIBE FORM ── -->
  <section id="subscribe" style="background:#fff;padding:80px 0">
    <div style="max-width:640px;margin:0 auto;padding:0 40px;text-align:center">
      <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--vk-red);font-weight:600;margin-bottom:16px">Free Digital Subscription</div>
      <h2 style="font-family:var(--font-display);font-size:40px;font-weight:500;color:var(--near-black);margin:0 0 16px;line-height:1.15">Subscribe Today</h2>
      <p style="font-size:15px;color:var(--mid-grey);line-height:1.75;margin:0 0 8px">Get instant access to all seven issues plus bonus content: mastering tips from Jett Galindo, exclusive engineer Q&amp;As, and early access to Issue 08.</p>
      <p style="font-size:13px;color:var(--mid-grey);margin:0 0 40px">No credit card. Cancel anytime.</p>

      <form style="display:flex;gap:12px;max-width:480px;margin:0 auto 16px" onsubmit="return false">
        <input type="email" placeholder="your@email.com" style="flex:1;padding:13px 16px;font-size:14px;font-family:var(--font-body);border:1.5px solid rgba(26,26,24,0.18);border-radius:3px;outline:none;color:var(--near-black);background:#fff" onfocus="this.style.borderColor='var(--vk-red)'" onblur="this.style.borderColor='rgba(26,26,24,0.18)'">
        <button type="submit" style="background:var(--vk-red);color:#fff;border:none;padding:13px 24px;border-radius:3px;font-size:14px;font-weight:600;font-family:var(--font-body);cursor:pointer;white-space:nowrap;letter-spacing:0.02em">Get Access →</button>
      </form>
      <p style="font-size:12px;color:rgba(26,26,24,0.38);margin:0">By subscribing you'll receive Vintage King marketing emails. Opt out any time.</p>

      <!-- Confidence row -->
      <div style="display:flex;justify-content:center;gap:32px;margin-top:40px;flex-wrap:wrap">
        <div style="text-align:center">
          <div style="font-size:24px;font-family:var(--font-display);font-weight:700;color:var(--near-black)">7</div>
          <div style="font-size:12px;color:var(--mid-grey);letter-spacing:0.06em;text-transform:uppercase">Issues</div>
        </div>
        <div style="width:1px;background:rgba(26,26,24,0.1)"></div>
        <div style="text-align:center">
          <div style="font-size:24px;font-family:var(--font-display);font-weight:700;color:var(--near-black)">Free</div>
          <div style="font-size:12px;color:var(--mid-grey);letter-spacing:0.06em;text-transform:uppercase">Always</div>
        </div>
        <div style="width:1px;background:rgba(26,26,24,0.1)"></div>
        <div style="text-align:center">
          <div style="font-size:24px;font-family:var(--font-display);font-weight:700;color:var(--near-black)">New</div>
          <div style="font-size:12px;color:var(--mid-grey);letter-spacing:0.06em;text-transform:uppercase">Quarterly</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── QUOTE RAIL ── -->
  <section style="background:var(--off-white);padding:56px 0;border-top:1px solid rgba(26,26,24,0.08)">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px">
      <div>
        <div style="font-family:var(--font-display);font-size:18px;font-style:italic;color:var(--near-black);line-height:1.5;margin-bottom:14px">"PLAYBACK is the only magazine that actually talks to the engineers who made the records I grew up on."</div>
        <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--mid-grey);font-weight:600">Al Schmitt — Capitol Studios</div>
      </div>
      <div>
        <div style="font-family:var(--font-display);font-size:18px;font-style:italic;color:var(--near-black);line-height:1.5;margin-bottom:14px">"Every issue makes me want to go back to the studio and try something I've never tried before."</div>
        <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--mid-grey);font-weight:600">Joe Chiccarelli — Hollywood, CA</div>
      </div>
      <div>
        <div style="font-family:var(--font-display);font-size:18px;font-style:italic;color:var(--near-black);line-height:1.5;margin-bottom:14px">"Finally — a gear publication that respects the craft as much as the equipment."</div>
        <div style="font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--mid-grey);font-weight:600">Glyn Johns — Surrey, UK</div>
      </div>
    </div>
  </section>

  <div id="footer-playback"></div>
</div>
"""

    inline_js = """\
<script>
  (function() {
    var p = 'playback';
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

  /* ── PLAYBACK magazine flipbook ── */
  (function() {
    var pbSpreads = [
      {
        left: '<div style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;font-weight:600;margin-bottom:32px">PLAYBACK &nbsp;·&nbsp; Issue 07</div>' +
              '<div style="background:#1A1A18;flex:1;margin:-40px -36px 0;display:flex;flex-direction:column;justify-content:flex-end;padding:40px 36px;min-height:320px;position:relative">' +
              '<div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,0.85) 100%)"></div>' +
              '<div style="position:relative;z-index:1"><div style="font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;font-weight:600;margin-bottom:8px">Issue 07</div>' +
              '<div style="font-family:\'Playfair Display\',serif;font-size:32px;font-style:italic;color:#fff;line-height:1.15;margin-bottom:12px">The Many<br>Paths of Audio</div>' +
              '<div style="font-size:12px;color:rgba(255,255,255,0.5)">vintageking.com/playback</div></div></div>',
        right: '<div style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.3);font-weight:600;margin-bottom:28px">Contents</div>' +
               '<div style="display:flex;flex-direction:column;gap:16px">' +
               '<div style="display:flex;gap:16px;align-items:baseline;border-bottom:1px solid rgba(26,26,24,0.07);padding-bottom:14px"><span style="font-size:18px;font-family:\'Playfair Display\',serif;color:rgba(26,26,24,0.2);min-width:28px">01</span><div><div style="font-size:13px;font-weight:600;color:#1A1A18;margin-bottom:2px">Five Sounds With Eva Reistad</div><div style="font-size:12px;color:#888">Interview</div></div></div>' +
               '<div style="display:flex;gap:16px;align-items:baseline;border-bottom:1px solid rgba(26,26,24,0.07);padding-bottom:14px"><span style="font-size:18px;font-family:\'Playfair Display\',serif;color:rgba(26,26,24,0.2);min-width:28px">02</span><div><div style="font-size:13px;font-weight:600;color:#1A1A18;margin-bottom:2px">SSL Oracle Console</div><div style="font-size:12px;color:#888">Buyer\'s Guide</div></div></div>' +
               '<div style="display:flex;gap:16px;align-items:baseline;border-bottom:1px solid rgba(26,26,24,0.07);padding-bottom:14px"><span style="font-size:18px;font-family:\'Playfair Display\',serif;color:rgba(26,26,24,0.2);min-width:28px">03</span><div><div style="font-size:13px;font-weight:600;color:#1A1A18;margin-bottom:2px">Studio Spotlight: Allaire Studios</div><div style="font-size:12px;color:#888">Studio</div></div></div>' +
               '<div style="display:flex;gap:16px;align-items:baseline;border-bottom:1px solid rgba(26,26,24,0.07);padding-bottom:14px"><span style="font-size:18px;font-family:\'Playfair Display\',serif;color:rgba(26,26,24,0.2);min-width:28px">04</span><div><div style="font-size:13px;font-weight:600;color:#1A1A18;margin-bottom:2px">Just Blaze: Beyond the Beat</div><div style="font-size:12px;color:#888">Producer Profile</div></div></div>' +
               '<div style="display:flex;gap:16px;align-items:baseline"><span style="font-size:18px;font-family:\'Playfair Display\',serif;color:rgba(26,26,24,0.2);min-width:28px">05</span><div><div style="font-size:13px;font-weight:600;color:#1A1A18;margin-bottom:2px">Jett Galindo: Mastering Tips</div><div style="font-size:12px;color:#888">Subscriber Bonus</div></div></div>' +
               '</div>'
      },
      {
        left: '<div style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;font-weight:600;margin-bottom:20px">Interview</div>' +
              '<div style="font-family:\'Playfair Display\',serif;font-size:28px;font-style:italic;color:#1A1A18;line-height:1.2;margin-bottom:16px">Five Sounds With<br>Eva Reistad</div>' +
              '<div style="width:40px;height:3px;background:#D4860A;margin-bottom:20px"></div>' +
              '<p style="font-size:13px;color:#555;line-height:1.75;margin-bottom:14px">Eva Reistad is one of the most decorated mixing engineers working today. Her credits span pop, electronic, and singer-songwriter genres, with GRAMMY wins for work with Aurora, Kygo, and Sigrid.</p>' +
              '<p style="font-size:13px;color:#555;line-height:1.75">We sat with her to discuss five records that changed the way she hears sound — and the gear that made them possible.</p>',
        right: '<div style="background:#F5F0E8;border-radius:3px;height:240px;display:flex;align-items:center;justify-content:center;margin-bottom:20px">' +
               '<div style="font-family:\'Playfair Display\',serif;font-size:48px;font-style:italic;color:rgba(26,26,24,0.12)">ER</div></div>' +
               '<p style="font-size:12px;color:#888;line-height:1.6;font-style:italic;margin-bottom:8px">"The room is always the instrument. The gear just decides how much of it you let in."</p>' +
               '<div style="font-size:11px;letter-spacing:0.1em;text-transform:uppercase;color:#C0392B;font-weight:600">Eva Reistad</div>'
      },
      {
        left: '<div style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;font-weight:600;margin-bottom:20px">Buyer\'s Guide</div>' +
              '<div style="font-family:\'Playfair Display\',serif;font-size:28px;font-style:italic;color:#1A1A18;line-height:1.2;margin-bottom:16px">SSL Oracle<br>Console</div>' +
              '<div style="width:40px;height:3px;background:#1A1A18;margin-bottom:20px"></div>' +
              '<p style="font-size:13px;color:#555;line-height:1.75;margin-bottom:14px">SSL\'s Oracle combines the iconic analog circuitry of the 4000 and 9000 series with new ActiveAnalogue technology — a hybrid architecture designed for the modern studio that doesn\'t sacrifice the sound that defined pop and rock recording.</p>' +
              '<p style="font-size:13px;color:#555;line-height:1.75">Our consultants break down every bus, every summing path, and what it means for your sessions.</p>',
        right: '<div style="background:#0D1218;border-radius:3px;height:240px;display:flex;align-items:center;justify-content:center;margin-bottom:20px">' +
               '<div style="font-family:\'Playfair Display\',serif;font-size:40px;font-style:italic;color:rgba(255,255,255,0.15)">SSL</div></div>' +
               '<p style="font-size:12px;color:#888;line-height:1.6;font-style:italic;margin-bottom:8px">"The Oracle is the SSL console for engineers who grew up on SSL consoles."</p>' +
               '<div style="font-size:11px;letter-spacing:0.1em;text-transform:uppercase;color:#C0392B;font-weight:600">VK Audio Consultant</div>'
      },
      {
        left: '<div style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;font-weight:600;margin-bottom:20px">Studio Spotlight</div>' +
              '<div style="font-family:\'Playfair Display\',serif;font-size:28px;font-style:italic;color:#1A1A18;line-height:1.2;margin-bottom:16px">Allaire Studios,<br>Woodstock NY</div>' +
              '<div style="width:40px;height:3px;background:#1A1A18;margin-bottom:20px"></div>' +
              '<p style="font-size:13px;color:#555;line-height:1.75;margin-bottom:14px">Randall Wallace — musician, photographer, owner — built Allaire in the Catskill Mountains with one goal: make a room where artists would stay for weeks, not days.</p>' +
              '<p style="font-size:13px;color:#555;line-height:1.75">The result is one of the most sought-after residential studios in the country, with a live room that sounds as good as it looks.</p>',
        right: '<div style="background:#101A12;border-radius:3px;height:240px;display:flex;align-items:center;justify-content:center;margin-bottom:20px">' +
               '<div style="font-family:\'Playfair Display\',serif;font-size:40px;font-style:italic;color:rgba(255,255,255,0.15)">AS</div></div>' +
               '<p style="font-size:12px;color:#888;line-height:1.6;font-style:italic;margin-bottom:8px">"I wanted guests to forget they were working. If you love where you are, you play better."</p>' +
               '<div style="font-size:11px;letter-spacing:0.1em;text-transform:uppercase;color:#C0392B;font-weight:600">Randall Wallace — Allaire Studios</div>'
      },
      {
        left: '<div style="font-size:10px;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;font-weight:600;margin-bottom:16px">Subscriber Bonus</div>' +
              '<div style="font-family:\'Playfair Display\',serif;font-size:24px;font-style:italic;color:#1A1A18;line-height:1.25;margin-bottom:16px">Mastering Tips from<br>Jett Galindo</div>' +
              '<div style="width:40px;height:3px;background:#D4860A;margin-bottom:20px"></div>' +
              '<p style="font-size:13px;color:#555;line-height:1.75;margin-bottom:16px">GRAMMY-winning mastering engineer Jett Galindo shares her approach to dynamic range, streaming loudness targets, and why she still reaches for analog gear in an all-digital world.</p>' +
              '<div style="background:#F5F0E8;border-radius:3px;padding:16px">' +
              '<div style="font-size:11px;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;font-weight:600;margin-bottom:8px">Exclusive to subscribers</div>' +
              '<p style="font-size:13px;color:#555;line-height:1.6;margin:0">Subscribe to PLAYBACK to unlock this bonus content and access all seven issues instantly.</p></div>',
        right: '<div style="height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px 0">' +
               '<div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(26,26,24,0.35);font-weight:600;margin-bottom:20px">PLAYBACK · Issue 07</div>' +
               '<div style="font-family:\'Playfair Display\',serif;font-size:20px;font-style:italic;color:#1A1A18;margin-bottom:24px">All seven issues.<br>Always free.</div>' +
               '<a href="#subscribe" onclick="document.getElementById(\'subscribe\').scrollIntoView({behavior:\'smooth\'});return false" style="display:inline-block;background:#C0392B;color:#fff;padding:12px 28px;border-radius:3px;font-size:13px;font-weight:600;text-decoration:none;letter-spacing:0.02em">Subscribe Free →</a>' +
               '<div style="margin-top:20px;font-size:11px;color:rgba(26,26,24,0.3)">No credit card required</div></div>'
      }
    ];
    var pbCurrent = 0;
    function pbRender() {
      var s = pbSpreads[pbCurrent];
      var L = document.getElementById('pb-page-left');
      var R = document.getElementById('pb-page-right');
      var C = document.getElementById('pb-counter');
      if (!L || !R) return;
      L.style.opacity = '0';
      R.style.opacity = '0';
      setTimeout(function() {
        L.innerHTML = s.left;
        R.innerHTML = s.right;
        L.style.opacity = '1';
        R.style.opacity = '1';
        C.textContent = 'Spread ' + (pbCurrent + 1) + ' of ' + pbSpreads.length;
        document.getElementById('pb-prev').style.opacity = pbCurrent === 0 ? '0.3' : '1';
        document.getElementById('pb-next').style.opacity = pbCurrent === pbSpreads.length - 1 ? '0.3' : '1';
      }, 180);
    }
    window.pbFlip = function(dir) {
      pbCurrent = Math.max(0, Math.min(pbSpreads.length - 1, pbCurrent + dir));
      pbRender();
    };
    pbRender();
  })();
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
