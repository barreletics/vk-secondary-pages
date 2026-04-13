#!/usr/bin/env python3
"""Build hall-of-fame.html — VK Hall of Fame standalone page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "VK-secondary-pages-source.html"
OUT  = ROOT / "hall-of-fame.html"

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
        "<title>Hall of Fame — The Gear That Defined Recording History | Vintage King</title>",
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
  "@type": "CollectionPage",
  "name": "Vintage King Hall of Fame",
  "url": "https://vintageking.com/hall-of-fame",
  "description": "The VK Hall of Fame honors the compressors, mic preamps, and microphones that have defined the sound of recorded music — curated by the experts at Vintage King Audio.",
  "provider": {
    "@type": "Organization",
    "name": "Vintage King Audio",
    "url": "https://vintageking.com"
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
  <span style="opacity:0.75">Hall of Fame</span>
</nav>
"""

    page_body = """\
<div id="hall-of-fame" class="page active">
  <div id="nav-hall-of-fame"></div>

  <!-- ── HERO: light split, amber prestige ── -->
  <div style="background:var(--warm-white);border-bottom:1px solid var(--pale-grey);padding:80px 0 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center">
      <div style="padding-bottom:80px">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:32px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Vintage King</div>
        </div>
        <h1 style="font-family:'Playfair Display',serif;font-size:58px;font-weight:700;color:var(--near-black);line-height:1.04;margin:0 0 24px">Hall<br>of Fame.</h1>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 16px;max-width:460px">Some pieces of gear do not just get used — they define entire eras of recorded music. The VK Hall of Fame honors the compressors, preamps, and microphones that changed everything.</p>
        <p style="font-size:16px;color:var(--mid-grey);line-height:1.70;margin:0 0 40px;max-width:460px">Curated by the engineers and historians at Vintage King. 19 inductees across 5 categories.</p>
        <div style="display:flex;gap:14px;flex-wrap:wrap">
          <a href="#hof-compressors" style="display:inline-flex;align-items:center;gap:8px;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">See the Inductees</a>
          <a href="#hof-nominate" style="display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(26,26,24,0.22);color:var(--near-black);font-size:13px;font-weight:500;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.borderColor='rgba(26,26,24,0.55)'" onmouseout="this.style.borderColor='rgba(26,26,24,0.22)'">Nominate a Piece</a>
        </div>
      </div>
      <div style="align-self:stretch;display:flex;flex-direction:column">
        <div style="flex:1;background:var(--near-black);border-radius:3px 3px 0 0;min-height:400px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:0;padding:40px;position:relative;overflow:hidden">
          <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 35% 50%,rgba(212,134,10,0.18) 0%,transparent 65%)"></div>
          <div style="position:relative;z-index:1;text-align:center">
            <div style="font-family:'Playfair Display',serif;font-size:80px;font-weight:700;color:rgba(212,134,10,0.15);line-height:1;margin-bottom:16px;letter-spacing:-0.02em">13</div>
            <div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:rgba(212,134,10,0.60);margin-bottom:32px">Inductees</div>
            <div style="display:flex;flex-direction:column;gap:10px;text-align:left;max-width:260px">
              <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 16px;background:rgba(255,255,255,0.04);border:1px solid rgba(212,134,10,0.20);border-radius:2px">
                <span style="font-size:13px;font-weight:500;color:rgba(255,255,255,0.80)">Compressors</span>
                <span style="font-size:11px;font-weight:700;color:#D4860A">4</span>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 16px;background:rgba(255,255,255,0.04);border:1px solid rgba(212,134,10,0.20);border-radius:2px">
                <span style="font-size:13px;font-weight:500;color:rgba(255,255,255,0.80)">Mic Preamps</span>
                <span style="font-size:11px;font-weight:700;color:#D4860A">3</span>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 16px;background:rgba(255,255,255,0.04);border:1px solid rgba(212,134,10,0.20);border-radius:2px">
                <span style="font-size:13px;font-weight:500;color:rgba(255,255,255,0.80)">Microphones</span>
                <span style="font-size:11px;font-weight:700;color:#D4860A">6</span>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 16px;background:rgba(255,255,255,0.04);border:1px solid rgba(212,134,10,0.20);border-radius:2px">
                <span style="font-size:13px;font-weight:500;color:rgba(255,255,255,0.80)">EQs &amp; Filters</span>
                <span style="font-size:11px;font-weight:700;color:#D4860A">3</span>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 16px;background:rgba(255,255,255,0.04);border:1px solid rgba(212,134,10,0.20);border-radius:2px">
                <span style="font-size:13px;font-weight:500;color:rgba(255,255,255,0.80)">Consoles</span>
                <span style="font-size:11px;font-weight:700;color:#D4860A">3</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── INTRO ── -->
  <div style="background:#fff;border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey);padding:56px 0">
    <div style="max-width:860px;margin:0 auto;padding:0 40px;text-align:center">
      <p style="font-family:'Playfair Display',serif;font-size:22px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.55;margin:0">Every piece in the Hall of Fame has appeared on countless records you know by heart. They are not just tools — they are instruments that engineers chose again and again because nothing else sounds quite like them. These are the ones that earned a permanent place in the history of recorded sound.</p>
    </div>
  </div>

  <!-- ══════════════════════════════════════
       CATEGORY 1 — COMPRESSORS
  ══════════════════════════════════════ -->
  <div id="hof-compressors" style="background:var(--near-black);padding:80px 0 64px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <!-- Category header -->
      <div style="display:flex;align-items:baseline;gap:24px;margin-bottom:8px;padding-bottom:20px;border-bottom:1px solid rgba(212,134,10,0.30)">
        <div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A">Category I</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:#fff;margin:0">Compressors</h2>
        <div style="margin-left:auto;font-size:13px;color:rgba(255,255,255,0.35);font-weight:500">4 inductees</div>
      </div>

      <!-- Ledger -->
      <div style="display:flex;flex-direction:column;gap:0;margin-bottom:48px">

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Fairchild 670</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The most sought-after compressor ever made. Variable-mu tube circuit. Used by The Beatles at Abbey Road. Fewer than 1,000 were ever built.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1959</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Teletronix LA-2A</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">Opto-electric leveling amplifier with an unmistakable character. Slow attack, natural release — the standard for vocals, bass, and broadcast. Still in production.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1962</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">UREI 1176LN</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">FET-based limiting amplifier with ultra-fast attack. The "all-buttons-in" mode is one of the most recognizable sounds in rock history. On virtually every major record since 1967.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1967</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">UA 175B</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">Variable-mu tube compressor from Universal Audio's original era. Transparent and musical. A favorite for stereo bus and mastering. Extremely rare in original form.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1960s</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

      </div>

      <!-- Shop cards -->
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#1c1410 0%,#2a1e12 50%,#1a1208 100%);position:relative;display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage · Rare</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Fairchild 670</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Contact for availability</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#14141c 0%,#1e1e28 50%,#121218 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">New and Vintage</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">LA-2A Leveling Amp</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">From $2,199 new · Used available</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#101410 0%,#181e18 50%,#0e1210 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">New and Vintage</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">UREI 1176LN</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">From $1,849 new · Originals from $3,500</div>
          </div>
        </a>
      </div>
    </div>
  </div>

  <!-- Engineer quote strip 1 -->
  <div style="background:var(--off-white);border-left:0;padding:48px 0;border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey)">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:flex;gap:32px;align-items:center">
      <div style="width:4px;background:#D4860A;align-self:stretch;border-radius:2px;flex-shrink:0"></div>
      <div>
        <p style="font-family:'Playfair Display',serif;font-size:22px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.55;margin:0 0 14px">"The 1176 is on every rock record I have ever made. It has a character that no plugin has ever fully captured — and I have tried them all."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Butch Vig — Producer, Nirvana · Smashing Pumpkins</div>
      </div>
    </div>
  </div>

  <!-- ══════════════════════════════════════
       CATEGORY 2 — MIC PREAMPS
  ══════════════════════════════════════ -->
  <div id="hof-preamps" style="background:var(--near-black);padding:80px 0 64px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:24px;margin-bottom:8px;padding-bottom:20px;border-bottom:1px solid rgba(212,134,10,0.30)">
        <div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A">Category II</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:#fff;margin:0">Mic Preamps</h2>
        <div style="margin-left:auto;font-size:13px;color:rgba(255,255,255,0.35);font-weight:500">3 inductees</div>
      </div>

      <div style="display:flex;flex-direction:column;gap:0;margin-bottom:48px">

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Neve 1073</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The benchmark mic preamp and EQ module. Designed by Rupert Neve for the 8000-series console. Transformer-coupled, Class-A. The foundation of more hit records than any other single piece of electronics.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1970</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Neve 1081</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">Four-band EQ with the same Neve transformer character as the 1073, but with more flexible equalization. A favorite for drums, room mics, and full-band tracking sessions.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1972</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Telefunken V72 / V76</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">German broadcast amplifiers developed for the German broadcasting network. The preamps used at Abbey Road during the Beatles sessions. A silky, forward sound unlike anything else.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1950s</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#121010 0%,#1e1c10 50%,#0e1010 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage and New</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Neve 1073</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Originals from $4,500 · New reissues available</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#14100a 0%,#201c12 50%,#100e08 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Neve 1081</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Originals from $3,200 · Contact us</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#140e0a 0%,#221a10 50%,#100c08 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage · Rare</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Telefunken V72 / V76</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Contact for availability</div>
          </div>
        </a>
      </div>
    </div>
  </div>

  <!-- Engineer quote strip 2 -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey);padding:48px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:flex;gap:32px;align-items:center">
      <div style="width:4px;background:#D4860A;align-self:stretch;border-radius:2px;flex-shrink:0"></div>
      <div>
        <p style="font-family:'Playfair Display',serif;font-size:22px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.55;margin:0 0 14px">"If there is one piece of outboard that I would never let leave my studio, it is the 1073. There is nothing else that sounds like it on a vocal — nothing."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Joe Chiccarelli — Producer, The White Stripes · Beck · Morrissey</div>
      </div>
    </div>
  </div>

  <!-- ══════════════════════════════════════
       CATEGORY 3 — MICROPHONES
  ══════════════════════════════════════ -->
  <div id="hof-microphones" style="background:var(--near-black);padding:80px 0 64px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:24px;margin-bottom:8px;padding-bottom:20px;border-bottom:1px solid rgba(212,134,10,0.30)">
        <div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A">Category III</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:#fff;margin:0">Microphones</h2>
        <div style="margin-left:auto;font-size:13px;color:rgba(255,255,255,0.35);font-weight:500">6 inductees</div>
      </div>

      <div style="display:flex;flex-direction:column;gap:0;margin-bottom:48px">

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Neumann U 47 / U 48</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The most iconic vocal microphone ever made. Frank Sinatra refused to record without one. Tube circuit, VF14 capsule, unmistakable warmth. Values exceed $15,000 for clean examples.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1947</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Neumann U 67</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">Multi-pattern tube condenser that bridged the gap between the U 47 and the U 87. Smooth high-end, musical midrange. Used extensively at EMI, Atlantic, and Columbia through the 1960s and 70s.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1960</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Neumann U 47 FET</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">Solid-state large-diaphragm cardioid built for high-SPL sources. The kick drum, snare, and guitar amp mic of choice. John Bonham's bass drum on Led Zeppelin IV. Reissued in 2015 to universal acclaim.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1972</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Telefunken ELA M 251</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The rarest of the classic tube microphones — built by AKG for Telefunken. Three patterns. Extraordinarily detailed and open. Favored by engineers who find the U 47 too dark. Values exceed $20,000.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1959</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Coles 4038</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">BBC ribbon microphone. Figure-8 pattern. Lush, soft top-end that no other ribbon has matched. The standard for room mics, drum overheads, and guitar cabinets in British studios from the 1950s onward.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1954</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">RCA 44-A</div>
          <div style="padding:0 24px">
            <div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The ribbon microphone that defined broadcast and vocal recording in the 1930s and 40s. Figure-8. Warm, round, and completely unlike modern condensers. Bing Crosby. Sinatra. Miles Davis. Still coveted.</div>
          </div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1931</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>

      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#0e1018 0%,#161c24 50%,#0c1018 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage · Rare</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Neumann U 47</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">From $12,000 · Contact us</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#160e0a 0%,#241810 50%,#140c08 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage · Rare</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Telefunken ELA M 251</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">From $18,000 · Contact us</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.14);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.09)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#0a0e14 0%,#12161c 50%,#080c10 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">New</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Neumann U 47 FET</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">$3,499 · In stock</div>
          </div>
        </a>
      </div>
    </div>
  </div>

  <!-- Engineer quote strip 3 -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey);padding:48px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:flex;gap:32px;align-items:center">
      <div style="width:4px;background:#D4860A;align-self:stretch;border-radius:2px;flex-shrink:0"></div>
      <div>
        <p style="font-family:'Playfair Display',serif;font-size:22px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.55;margin:0 0 14px">"When I put a U 47 in front of a great singer, I stop thinking about the microphone. That is the whole point. The best gear disappears into the performance."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Al Schmitt — Recording Engineer, 23 Grammy Awards</div>
      </div>
    </div>
  </div>

  <!-- ══════════════════════════════════════
       CATEGORY 4 — EQs (LIGHT section)
  ══════════════════════════════════════ -->
  <div id="hof-eqs" style="background:var(--off-white);padding:80px 0 64px;border-top:2px solid var(--pale-grey)">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:24px;margin-bottom:8px;padding-bottom:20px;border-bottom:2px solid rgba(26,26,24,0.12)">
        <div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A">Category IV</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:var(--near-black);margin:0">EQs &amp; Filters</h2>
        <div style="margin-left:auto;font-size:13px;color:var(--mid-grey);font-weight:500">3 inductees</div>
      </div>

      <div style="display:flex;flex-direction:column;gap:0;margin-bottom:48px">
        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid var(--pale-grey)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black)">Pultec EQP-1A</div>
          <div style="padding:0 24px"><div style="font-size:13px;color:var(--mid-grey);line-height:1.6">The classic passive tube equalizer. Beloved for the simultaneous boost-and-cut trick on low frequencies that adds weight without muddiness. Found on nearly every major studio rack since the 1950s.</div></div>
          <div style="font-size:12px;font-weight:500;color:#D4860A;letter-spacing:0.06em;text-transform:uppercase">c. 1951</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>
        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid var(--pale-grey)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black)">API 550A</div>
          <div style="padding:0 24px"><div style="font-size:13px;color:var(--mid-grey);line-height:1.6">Three-band discrete solid-state EQ with proportional-Q curves. The foundation of the API sound. On every major rock and soul recording from the late 1960s onward. Still in production. An inductee by consensus.</div></div>
          <div style="font-size:12px;font-weight:500;color:#D4860A;letter-spacing:0.06em;text-transform:uppercase">c. 1967</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>
        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black)">Neve 1084</div>
          <div style="padding:0 24px"><div style="font-size:13px;color:var(--mid-grey);line-height:1.6">Four-band transformer-coupled Class-A EQ module from the Neve 8000 series. Wide, musical curves that add presence and sheen without aggression. A staple at AIR, Abbey Road, and Electric Lady for decades.</div></div>
          <div style="font-size:12px;font-weight:500;color:#D4860A;letter-spacing:0.06em;text-transform:uppercase">c. 1973</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.boxShadow='0 4px 20px rgba(26,26,24,0.10)'" onmouseout="this.style.boxShadow='none'">
          <div style="height:380px;overflow:hidden;background:var(--pale-grey);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.25)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage and New</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:var(--near-black);margin-bottom:6px">Pultec EQP-1A</div>
            <div style="font-size:13px;color:var(--mid-grey)">Originals from $3,500 · Reissues available</div>
          </div>
        </a>
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.boxShadow='0 4px 20px rgba(26,26,24,0.10)'" onmouseout="this.style.boxShadow='none'">
          <div style="height:380px;overflow:hidden;background:var(--pale-grey);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.25)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">New</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:var(--near-black);margin-bottom:6px">API 550A</div>
            <div style="font-size:13px;color:var(--mid-grey)">From $499 · In stock</div>
          </div>
        </a>
        <a href="#" style="background:#fff;border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.boxShadow='0 4px 20px rgba(26,26,24,0.10)'" onmouseout="this.style.boxShadow='none'">
          <div style="height:380px;overflow:hidden;background:var(--pale-grey);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.25)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:var(--near-black);margin-bottom:6px">Neve 1084</div>
            <div style="font-size:13px;color:var(--mid-grey)">Originals from $2,800 · Contact us</div>
          </div>
        </a>
      </div>
    </div>
  </div>

  <!-- Engineer quote strip 4 (dark bg for contrast after light EQ section) -->
  <div style="background:var(--near-black);padding:48px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:flex;gap:32px;align-items:center">
      <div style="width:4px;background:#D4860A;align-self:stretch;border-radius:2px;flex-shrink:0"></div>
      <div>
        <p style="font-family:'Playfair Display',serif;font-size:22px;font-weight:400;font-style:italic;color:#fff;line-height:1.55;margin:0 0 14px">"The Pultec on the low end is not optional. There is no other way to get that weight without making everything heavy. It is the trick every engineer learns and never stops using."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Glyn Johns — Producer, The Rolling Stones · The Who · Eagles</div>
      </div>
    </div>
  </div>

  <!-- ══════════════════════════════════════
       CATEGORY 5 — CONSOLES (warm amber-dark)
  ══════════════════════════════════════ -->
  <div id="hof-consoles" style="background:#1E1A10;padding:80px 0 64px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:baseline;gap:24px;margin-bottom:8px;padding-bottom:20px;border-bottom:1px solid rgba(212,134,10,0.30)">
        <div style="font-size:11px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A">Category V</div>
        <h2 style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:#fff;margin:0">Mixing Consoles</h2>
        <div style="margin-left:auto;font-size:13px;color:rgba(255,255,255,0.35);font-weight:500">3 inductees</div>
      </div>

      <div style="display:flex;flex-direction:column;gap:0;margin-bottom:48px">
        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">SSL 4000 E/G</div>
          <div style="padding:0 24px"><div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The defining console of 1980s and 90s commercial recording. Built-in compressor and gate on every channel. Total recall. Michael Jackson, Phil Collins, Def Leppard — essentially every major record of its era.</div></div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1979</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>
        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0;border-bottom:1px solid rgba(255,255,255,0.07)">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">Neve 8078</div>
          <div style="padding:0 24px"><div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">The large-format Neve console at the heart of the warmest-sounding rock recordings ever made. Led Zeppelin at Headley Grange. The Rolling Stones at Stargroves. Thick, musical, irreplaceable.</div></div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 1972</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>
        <div style="display:grid;grid-template-columns:200px 1fr 160px 120px;gap:0;align-items:center;padding:22px 0">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#fff">API 1608</div>
          <div style="padding:0 24px"><div style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6">Modern API console that brought the classic 2520 op-amp sound into a full-format desk. Sixteen channels of pure API character. The choice of engineers who refuse to track without transformer-coupled hardware.</div></div>
          <div style="font-size:12px;font-weight:500;color:rgba(212,134,10,0.80);letter-spacing:0.06em;text-transform:uppercase">c. 2008</div>
          <div style="text-align:right"><a href="#" style="font-size:12px;font-weight:600;color:#D4860A;text-decoration:none;letter-spacing:0.04em" onmouseover="this.style.opacity='.65'" onmouseout="this.style.opacity='1'">Shop →</a></div>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
        <a href="#" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.12)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#1a180c 0%,#2a2410 50%,#181408 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">SSL 4000 E/G</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Contact for availability</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.12)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#181408 0%,#241e0a 50%,#161208 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Vintage · Rare</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">Neve 8078</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Contact for availability</div>
          </div>
        </a>
        <a href="#" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:3px;text-decoration:none;overflow:hidden;display:block" onmouseover="this.style.borderColor='rgba(212,134,10,0.50)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.12)'">
          <div style="height:380px;overflow:hidden;background:linear-gradient(160deg,#141010 0%,#201c10 50%,#120e0c 100%);display:flex;align-items:center;justify-content:center">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.35)">Product Photo</div>
          </div>
          <div style="padding:18px 20px">
            <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">New</div>
            <div style="font-family:'Playfair Display',serif;font-size:16px;font-weight:700;color:#fff;margin-bottom:6px">API 1608</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.40)">Contact for pricing</div>
          </div>
        </a>
      </div>
    </div>
  </div>

  <!-- Engineer quote strip 5 -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey);padding:48px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:flex;gap:32px;align-items:center">
      <div style="width:4px;background:#D4860A;align-self:stretch;border-radius:2px;flex-shrink:0"></div>
      <div>
        <p style="font-family:'Playfair Display',serif;font-size:22px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.55;margin:0 0 14px">"When I walked into a room with a Neve 8078, I knew the session would sound good before I touched a single fader. The console did half the work."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Bob Ludwig — Mastering Engineer, Rolling Stones · Nirvana · U2</div>
      </div>
    </div>
  </div>

  <!-- ── BY ENGINEER ── -->
  <div id="hof-by-engineer" style="background:#fff;padding:80px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="margin-bottom:48px">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">By Engineer</div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 16px">The Setups Behind<br>the Records.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;max-width:580px;margin:0">Every engineer has a short list of gear they reach for first. These are the Hall of Fame pieces that defined how some of the greatest recordings were made.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">

        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:32px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:4px">Al Schmitt</div>
          <div style="font-size:12px;color:#D4860A;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:20px">23 Grammy Awards</div>
          <div style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin-bottom:20px">Frank Sinatra. Diana Krall. Paul McCartney. Bob Dylan. Al built his sound around a handful of pieces he never let leave the room.</div>
          <div style="border-top:1px solid var(--pale-grey);padding-top:20px">
            <div style="font-size:11px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:var(--near-black);margin-bottom:12px">Signature Gear</div>
            <div style="display:flex;flex-direction:column;gap:8px">
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Neumann U 47 — main vocal mic</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Neve 1073 — mic preamp</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Fairchild 670 — bus compression</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Pultec EQP-1A — low-end shaping</span></div>
            </div>
          </div>
        </div>

        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:32px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:4px">Glyn Johns</div>
          <div style="font-size:12px;color:#D4860A;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:20px">Rolling Stones · The Who · Eagles</div>
          <div style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin-bottom:20px">The Glyn Johns drum miking method is still taught in recording schools worldwide. His gear list was short, deliberate, and always included these.</div>
          <div style="border-top:1px solid var(--pale-grey);padding-top:20px">
            <div style="font-size:11px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:var(--near-black);margin-bottom:12px">Signature Gear</div>
            <div style="display:flex;flex-direction:column;gap:8px">
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Neve 8078 — tracking console</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Telefunken V72 — preamp</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Coles 4038 — room and overheads</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Pultec EQP-1A — mix EQ</span></div>
            </div>
          </div>
        </div>

        <div style="background:var(--off-white);border:1px solid var(--pale-grey);border-top:3px solid #D4860A;border-radius:3px;padding:32px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:4px">Joe Chiccarelli</div>
          <div style="font-size:12px;color:#D4860A;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;margin-bottom:20px">White Stripes · Beck · Morrissey</div>
          <div style="font-size:13px;color:var(--mid-grey);line-height:1.7;margin-bottom:20px">One of the most versatile producers working across rock, indie, and alternative. Known for using vintage gear to bring warmth and character to modern recordings.</div>
          <div style="border-top:1px solid var(--pale-grey);padding-top:20px">
            <div style="font-size:11px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:var(--near-black);margin-bottom:12px">Signature Gear</div>
            <div style="display:flex;flex-direction:column;gap:8px">
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Neve 1073 — every vocal, every session</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">UREI 1176LN — drums and guitars</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">Teletronix LA-2A — bass and vocals</span></div>
              <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:var(--near-black)">API 550A — guitars and drums EQ</span></div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- ── NOMINATE STRIP ── -->
  <div id="hof-nominate" style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
      <div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Nominations Open</div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 24px">Know a Piece<br>That Belongs Here?</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 24px">The Hall of Fame grows through the expertise of engineers, producers, collectors, and musicians who have spent their careers with this gear. If you believe a piece belongs in the next class of inductees, tell us why.</p>
        <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0">Nominations are reviewed by the VK team and a rotating panel of industry veterans. The next induction class is announced annually.</p>
      </div>
      <div>
        <form onsubmit="event.preventDefault();this.innerHTML='<div style=\\'padding:40px 0;text-align:center\\'><div style=\\'font-family:Playfair Display,serif;font-size:22px;font-weight:700;color:var(--near-black);margin-bottom:12px\\'>Nomination received.</div><p style=\\'font-size:15px;color:var(--mid-grey)\\'>Thank you. Our team reviews all nominations ahead of the annual induction announcement.</p></div>'" style="background:var(--off-white);border:1px solid var(--pale-grey);border-radius:3px;padding:40px">
          <div style="font-size:15px;font-weight:600;color:var(--near-black);margin-bottom:20px">Submit a nomination</div>
          <div style="margin-bottom:14px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Piece / Model Name *</label>
            <input type="text" required placeholder="e.g. Pultec EQP-1A" style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
          </div>
          <div style="margin-bottom:14px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Category *</label>
            <select required style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
              <option value="">Select category</option>
              <option>Compressors</option>
              <option>Mic Preamps</option>
              <option>Microphones</option>
              <option>EQs &amp; Filters</option>
              <option>Mixing Consoles</option>
              <option>Other</option>
            </select>
          </div>
          <div style="margin-bottom:14px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Why does it belong? *</label>
            <textarea rows="4" required placeholder="Tell us what makes this piece historically significant..." style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;resize:vertical;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'"></textarea>
          </div>
          <div style="margin-bottom:24px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Your Name and Email</label>
            <input type="text" placeholder="Name and email (optional)" style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
          </div>
          <button type="submit" style="width:100%;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;padding:15px 24px;border:none;border-radius:3px;cursor:pointer;font-family:var(--font-body)" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Submit Nomination</button>
        </form>
      </div>
    </div>
  </div>

  <!-- ── CONFIDENCE STRIP ── -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);padding:56px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:repeat(4,1fr);gap:32px">
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">We Buy Vintage</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Looking to sell a Hall of Fame piece? We offer fair appraisals and fast cash or credit.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">VK Warranty</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Every vintage piece we sell is inspected, serviced, and backed by the VK Warranty.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Expert Sourcing</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Looking for a specific piece? Our vintage specialists actively source rare gear worldwide.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Free Consultation</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Not sure which piece is right for you? Call us — our vintage team lives for this conversation.</p>
      </div>
    </div>
  </div>

  <div id="footer-hall-of-fame"></div>
</div>
"""

    inline_js = """\
<script>
  (function() {
    var p = 'hall-of-fame';
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
