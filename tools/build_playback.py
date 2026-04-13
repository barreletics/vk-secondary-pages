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

  <!-- ── INSIDE THIS ISSUE ── -->
  <section style="background:#1A1A18;padding:64px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:16px;margin-bottom:36px">
        <div style="font-size:12px;letter-spacing:0.22em;text-transform:uppercase;color:var(--amber);font-weight:600">Issue 07 — Now Available</div>
        <div style="flex:1;height:1px;background:rgba(255,255,255,0.1)"></div>
      </div>
      <h2 style="font-family:var(--font-display);font-size:32px;font-weight:500;color:#fff;margin:0 0 16px;line-height:1.2">Inside This Issue</h2>
      <p style="font-size:15px;color:rgba(255,255,255,0.55);line-height:1.7;margin:0 0 16px;max-width:680px">The seventh issue of Vintage King's PLAYBACK celebrates the many paths of today's audio industry. Dive into interviews with Just Blaze, Jett Galindo, Sam Evian, Kris Pooley, and Eva Reistad, plus insights from top producers and engineers in rock and metal.</p>
      <p style="font-size:14px;color:rgba(255,255,255,0.38);line-height:1.6;margin:0 0 44px;max-width:680px">We also spotlight the latest studio essentials, including the Cranborne Audio Brick Lane 500 Series compressor, Focal Utopia Main monitors, and Focusrite RedNet TNX interface.</p>

      <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.4);font-weight:600;margin-bottom:20px">More Features From This Issue</div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">

        <!-- Feature card 1 — Eva Reistad -->
        <div style="background:rgba(255,255,255,0.05);border-radius:4px;overflow:hidden;border:1px solid rgba(255,255,255,0.08)">
          <div style="background:#2A2018;height:280px;display:flex;align-items:center;justify-content:center">
            <div style="font-family:var(--font-display);font-size:40px;font-style:italic;color:rgba(255,255,255,0.12)">ER</div>
          </div>
          <div style="padding:20px">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:var(--amber);font-weight:600;margin-bottom:10px">Interview</div>
            <div style="font-family:var(--font-display);font-size:18px;font-weight:500;color:#fff;line-height:1.3;margin-bottom:10px">Five Sounds With Eva Reistad</div>
            <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.65;margin:0">We sat down with GRAMMY Award-winning mixer, producer, and artist Eva Reistad to discuss her approach to making five of her favorite records.</p>
          </div>
        </div>

        <!-- Feature card 2 — SSL Oracle -->
        <div style="background:rgba(255,255,255,0.05);border-radius:4px;overflow:hidden;border:1px solid rgba(255,255,255,0.08)">
          <div style="background:#181A20;height:280px;display:flex;align-items:center;justify-content:center">
            <div style="font-family:var(--font-display);font-size:40px;font-style:italic;color:rgba(255,255,255,0.12)">SSL</div>
          </div>
          <div style="padding:20px">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.4);font-weight:600;margin-bottom:10px">Buyer's Guide</div>
            <div style="font-family:var(--font-display);font-size:18px;font-weight:500;color:#fff;line-height:1.3;margin-bottom:10px">SSL Oracle Console</div>
            <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.65;margin:0">Learn more about SSL's new Oracle console, combining the brand's iconic analog circuitry with new ActiveAnalogue technology.</p>
          </div>
        </div>

        <!-- Feature card 3 — Allaire Studios -->
        <div style="background:rgba(255,255,255,0.05);border-radius:4px;overflow:hidden;border:1px solid rgba(255,255,255,0.08)">
          <div style="background:#101A12;height:280px;display:flex;align-items:center;justify-content:center">
            <div style="font-family:var(--font-display);font-size:40px;font-style:italic;color:rgba(255,255,255,0.12)">AS</div>
          </div>
          <div style="padding:20px">
            <div style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.4);font-weight:600;margin-bottom:10px">Studio Spotlight</div>
            <div style="font-family:var(--font-display);font-size:18px;font-weight:500;color:#fff;line-height:1.3;margin-bottom:10px">Allaire Studios</div>
            <p style="font-size:13px;color:rgba(255,255,255,0.45);line-height:1.65;margin:0">Meet Randall Wallace, musician, photographer, and owner of Allaire Studios in Woodstock, New York.</p>
          </div>
        </div>

      </div>

      <div style="margin-top:32px;display:flex;align-items:center;gap:24px">
        <a href="#subscribe" style="font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:#fff;text-decoration:none;background:var(--vk-red);padding:11px 22px;border-radius:3px">Get Free Access →</a>
        <a href="https://vintageking.com/playback-magazine" target="_blank" rel="noopener" style="font-size:13px;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;color:rgba(255,255,255,0.45);text-decoration:none">Read Full Issue at VintageKing.com ↗</a>
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
