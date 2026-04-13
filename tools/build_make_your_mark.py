#!/usr/bin/env python3
"""Build make-your-mark.html — VK Make Your Mark standalone page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC  = ROOT / "VK-secondary-pages-source.html"
OUT  = ROOT / "make-your-mark.html"

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
        "<title>Make Your Mark — Artist &amp; Engineer Stories | Vintage King</title>",
        head_css, count=1, flags=re.S
    )
    head_css += """\
  <style id="vk-standalone-patch">
    .page { display: block !important; }
    .mym-card-thumb { height: 280px !important; }
  </style>
"""

    json_ld = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Make Your Mark — Vintage King Original Series",
  "url": "https://vintageking.com/make-your-mark",
  "description": "Make Your Mark is an original video series from Vintage King featuring the world's top engineers and producers discussing the gear, rooms, and decisions behind the records.",
  "provider": { "@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com" }
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
  <span style="opacity:0.75">Make Your Mark</span>
</nav>
"""

    page_body = """\
<div id="make-your-mark" class="page active">
  <div id="nav-make-your-mark"></div>

  <!-- ── HERO: light split, amber accent ── -->
  <div style="background:var(--warm-white);border-bottom:1px solid var(--pale-grey);padding:80px 0 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center">
      <div style="padding-bottom:80px">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:32px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">VK Original Series</div>
        </div>
        <h1 style="font-family:'Playfair Display',serif;font-size:58px;font-weight:700;color:var(--near-black);line-height:1.04;margin:0 0 24px">Make<br>Your Mark.</h1>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 16px;max-width:460px">The engineers and producers behind the records you know by heart — talking about the rooms, the gear, and the decisions that defined them.</p>
        <p style="font-size:15px;color:var(--mid-grey);line-height:1.70;margin:0 0 40px;max-width:460px">Free to watch. New episodes every month. No signup required.</p>
        <div style="display:flex;gap:14px;flex-wrap:wrap">
          <a href="#mym-episodes" style="display:inline-flex;align-items:center;gap:8px;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Watch Episodes</a>
          <a href="#mym-submit" style="display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(26,26,24,0.22);color:var(--near-black);font-size:13px;font-weight:500;padding:14px 28px;border-radius:3px;text-decoration:none" onmouseover="this.style.borderColor='rgba(26,26,24,0.55)'" onmouseout="this.style.borderColor='rgba(26,26,24,0.22)'">Submit Your Story</a>
        </div>
      </div>
      <div style="align-self:stretch;display:flex;flex-direction:column">
        <div style="flex:1;background:#1A1510;border-radius:3px 3px 0 0;min-height:420px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden">
          <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 60% 40%,rgba(212,134,10,0.20) 0%,transparent 65%)"></div>
          <div style="position:relative;z-index:1;text-align:center;padding:40px">
            <div style="width:72px;height:72px;border-radius:50%;border:1.5px solid rgba(212,134,10,0.40);display:flex;align-items:center;justify-content:center;margin:0 auto 24px">
              <svg width="28" height="28" viewBox="0 0 32 32" fill="none"><polygon points="12,9 25,16 12,23" fill="#D4860A"/></svg>
            </div>
            <div style="font-size:10px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:rgba(212,134,10,0.60);margin-bottom:12px">Latest Episode</div>
            <div style="font-family:'Playfair Display',serif;font-size:20px;font-style:italic;font-weight:400;color:#fff;line-height:1.4;margin-bottom:8px;max-width:280px">"Inside the Neve 8078 — why nothing comes close"</div>
            <div style="font-size:12px;color:rgba(255,255,255,0.40)">12 min · Glyn Johns · Olympic Studios, London</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── SERIES INTRO ── -->
  <div style="background:#fff;border-top:2px solid var(--pale-grey);border-bottom:2px solid var(--pale-grey);padding:56px 0">
    <div style="max-width:860px;margin:0 auto;padding:0 40px;text-align:center">
      <p style="font-family:'Playfair Display',serif;font-size:21px;font-weight:400;font-style:italic;color:var(--near-black);line-height:1.55;margin:0 0 24px">This is not gear review content. Make Your Mark is a documentary series — the engineers and producers who built the sound of recorded music, talking on camera about what they actually use and why.</p>
      <div style="display:flex;justify-content:center;gap:48px;flex-wrap:wrap">
        <div style="text-align:center">
          <div style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#D4860A">7</div>
          <div style="font-size:12px;font-weight:500;color:var(--mid-grey);letter-spacing:0.06em;text-transform:uppercase">Episodes</div>
        </div>
        <div style="text-align:center">
          <div style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#D4860A">6</div>
          <div style="font-size:12px;font-weight:500;color:var(--mid-grey);letter-spacing:0.06em;text-transform:uppercase">Studios</div>
        </div>
        <div style="text-align:center">
          <div style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#D4860A">Free</div>
          <div style="font-size:12px;font-weight:500;color:var(--mid-grey);letter-spacing:0.06em;text-transform:uppercase">Always</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── FEATURED SESSIONS (2 panoramic cards) ── -->
  <div style="background:var(--off-white);padding:80px 0;border-bottom:2px solid var(--pale-grey)">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:32px">
        <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
        <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Featured Sessions</div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">

        <!-- Dave Cobb -->
        <a href="#" style="background:var(--near-black);border-radius:3px;overflow:hidden;text-decoration:none;display:block;position:relative" onmouseover="this.querySelector('.mym-hover').style.opacity='1'" onmouseout="this.querySelector('.mym-hover').style.opacity='0'">
          <div style="height:360px;background:linear-gradient(160deg,#1A1208 0%,#2A1C0A 40%,#1A1208 100%);display:flex;align-items:flex-end;padding:32px;position:relative">
            <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 30% 40%,rgba(212,134,10,0.15) 0%,transparent 60%)"></div>
            <div class="mym-hover" style="position:absolute;inset:0;background:rgba(212,134,10,0.06);opacity:0;transition:opacity 0.25s"></div>
            <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)">
              <div style="width:64px;height:64px;border-radius:50%;border:1.5px solid rgba(212,134,10,0.50);display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.40)">
                <svg width="24" height="24" viewBox="0 0 32 32" fill="none"><polygon points="12,9 25,16 12,23" fill="#D4860A"/></svg>
              </div>
            </div>
            <div style="position:relative;z-index:1">
              <div style="font-size:9px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:rgba(212,134,10,0.70);margin-bottom:8px">Ep. 03 · RCA Studio A, Nashville</div>
              <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.25)">Studio Photo</div>
            </div>
          </div>
          <div style="padding:24px 28px">
            <div style="font-family:'Playfair Display',serif;font-size:22px;font-style:italic;font-weight:400;color:#fff;line-height:1.35;margin-bottom:8px">"How I build a record from the floor up — and why it always starts with the room"</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.45);margin-bottom:16px">18 min · Dave Cobb</div>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
              <span style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A;border:1px solid rgba(212,134,10,0.35);padding:4px 10px;border-radius:2px">Neve 8078</span>
              <span style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:rgba(255,255,255,0.40);border:1px solid rgba(255,255,255,0.12);padding:4px 10px;border-radius:2px">RCA 44-A</span>
              <span style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:rgba(255,255,255,0.40);border:1px solid rgba(255,255,255,0.12);padding:4px 10px;border-radius:2px">Fairchild 670</span>
            </div>
          </div>
        </a>

        <!-- Bob Clearmountain -->
        <a href="#" style="background:var(--near-black);border-radius:3px;overflow:hidden;text-decoration:none;display:block;position:relative" onmouseover="this.querySelector('.mym-hover').style.opacity='1'" onmouseout="this.querySelector('.mym-hover').style.opacity='0'">
          <div style="height:360px;background:linear-gradient(160deg,#0E1218 0%,#161E2A 40%,#0C1018 100%);display:flex;align-items:flex-end;padding:32px;position:relative">
            <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 40%,rgba(192,57,43,0.10) 0%,transparent 60%)"></div>
            <div class="mym-hover" style="position:absolute;inset:0;background:rgba(212,134,10,0.06);opacity:0;transition:opacity 0.25s"></div>
            <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)">
              <div style="width:64px;height:64px;border-radius:50%;border:1.5px solid rgba(212,134,10,0.50);display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.40)">
                <svg width="24" height="24" viewBox="0 0 32 32" fill="none"><polygon points="12,9 25,16 12,23" fill="#D4860A"/></svg>
              </div>
            </div>
            <div style="position:relative;z-index:1">
              <div style="font-size:9px;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;color:rgba(212,134,10,0.70);margin-bottom:8px">Ep. 05 · Right Track Studios, New York</div>
              <div style="font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.25)">Studio Photo</div>
            </div>
          </div>
          <div style="padding:24px 28px">
            <div style="font-family:'Playfair Display',serif;font-size:22px;font-style:italic;font-weight:400;color:#fff;line-height:1.35;margin-bottom:8px">"The SSL bus compressor — what it does that nothing else does, and when to turn it off"</div>
            <div style="font-size:13px;color:rgba(255,255,255,0.45);margin-bottom:16px">14 min · Bob Clearmountain</div>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
              <span style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A;border:1px solid rgba(212,134,10,0.35);padding:4px 10px;border-radius:2px">SSL 4000 G</span>
              <span style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:rgba(255,255,255,0.40);border:1px solid rgba(255,255,255,0.12);padding:4px 10px;border-radius:2px">Neve 1073</span>
              <span style="font-size:10px;font-weight:600;letter-spacing:0.10em;text-transform:uppercase;color:rgba(255,255,255,0.40);border:1px solid rgba(255,255,255,0.12);padding:4px 10px;border-radius:2px">LA-2A</span>
            </div>
          </div>
        </a>

      </div>
    </div>
  </div>

  <!-- ── ALL EPISODES ── -->
  <div id="mym-episodes" style="background:#fff;padding:80px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:40px">
        <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
        <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">All Episodes</div>
      </div>
      <div class="mym-grid" style="grid-template-columns:repeat(3,1fr);gap:24px">

        <a href="#" class="mym-card">
          <div class="mym-card-thumb" style="background:var(--near-black);position:relative">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="rgba(255,255,255,0.15)" fill="none" stroke-width="1"/><polygon points="13,10 23,16 13,22" fill="rgba(192,57,43,0.8)"/></svg>
            <div style="position:absolute;top:10px;left:12px;font-size:9px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.30)">Ep. 01</div>
          </div>
          <div class="mym-card-studio">Capitol Studios · Los Angeles</div>
          <div class="mym-card-title">"How I track vocals at Capitol Studios"</div>
          <div class="mym-card-meta">8 min · Al Schmitt</div>
        </a>

        <a href="#" class="mym-card">
          <div class="mym-card-thumb" style="background:linear-gradient(135deg,#1A1510,#2A1F08);position:relative">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="rgba(212,134,10,0.3)" fill="none" stroke-width="1"/><polygon points="13,10 23,16 13,22" fill="rgba(212,134,10,0.8)"/></svg>
            <div style="position:absolute;top:10px;left:12px;font-size:9px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.50)">Ep. 02</div>
          </div>
          <div class="mym-card-studio">Olympic Studios · London</div>
          <div class="mym-card-title">"The Neve 8078 — why nothing comes close"</div>
          <div class="mym-card-meta">12 min · Glyn Johns</div>
        </a>

        <a href="#" class="mym-card">
          <div class="mym-card-thumb" style="background:linear-gradient(135deg,#1A1208,#2A1C0A);position:relative">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="rgba(212,134,10,0.25)" fill="none" stroke-width="1"/><polygon points="13,10 23,16 13,22" fill="rgba(212,134,10,0.75)"/></svg>
            <div style="position:absolute;top:10px;left:12px;font-size:9px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.50)">Ep. 03</div>
          </div>
          <div class="mym-card-studio">RCA Studio A · Nashville</div>
          <div class="mym-card-title">"How I build a record from the floor up"</div>
          <div class="mym-card-meta">18 min · Dave Cobb</div>
        </a>

        <a href="#" class="mym-card">
          <div class="mym-card-thumb" style="background:var(--near-black);position:relative">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="rgba(255,255,255,0.15)" fill="none" stroke-width="1"/><polygon points="13,10 23,16 13,22" fill="rgba(192,57,43,0.8)"/></svg>
            <div style="position:absolute;top:10px;left:12px;font-size:9px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.30)">Ep. 04</div>
          </div>
          <div class="mym-card-studio">East Side Sound · New York</div>
          <div class="mym-card-title">"Building the mix from scratch"</div>
          <div class="mym-card-meta">10 min · Joe Chiccarelli</div>
        </a>

        <a href="#" class="mym-card">
          <div class="mym-card-thumb" style="background:linear-gradient(135deg,#0E1218,#161E2A);position:relative">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="rgba(255,255,255,0.15)" fill="none" stroke-width="1"/><polygon points="13,10 23,16 13,22" fill="rgba(212,134,10,0.8)"/></svg>
            <div style="position:absolute;top:10px;left:12px;font-size:9px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.30)">Ep. 05</div>
          </div>
          <div class="mym-card-studio">Right Track Studios · New York</div>
          <div class="mym-card-title">"The SSL bus compressor — and when to turn it off"</div>
          <div class="mym-card-meta">14 min · Bob Clearmountain</div>
        </a>

        <a href="#" class="mym-card">
          <div class="mym-card-thumb" style="background:linear-gradient(135deg,#100E08,#1C1A10);position:relative">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="rgba(212,134,10,0.20)" fill="none" stroke-width="1"/><polygon points="13,10 23,16 13,22" fill="rgba(212,134,10,0.70)"/></svg>
            <div style="position:absolute;top:10px;left:12px;font-size:9px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(212,134,10,0.45)">Ep. 06</div>
            <div style="position:absolute;top:10px;right:12px;font-size:9px;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;color:#D4860A;background:rgba(212,134,10,0.15);border:1px solid rgba(212,134,10,0.30);padding:2px 7px;border-radius:2px">New</div>
          </div>
          <div class="mym-card-studio">Gateway Mastering · Portland</div>
          <div class="mym-card-title">"Mastering for vinyl — what actually changes"</div>
          <div class="mym-card-meta">9 min · Bob Ludwig</div>
        </a>

      </div>
    </div>
  </div>

  <!-- ── QUOTE STRIP ── -->
  <div style="background:var(--near-black);padding:56px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:flex;gap:32px;align-items:center">
      <div style="width:4px;background:#D4860A;align-self:stretch;border-radius:2px;flex-shrink:0"></div>
      <div>
        <p style="font-family:'Playfair Display',serif;font-size:24px;font-weight:400;font-style:italic;color:#fff;line-height:1.55;margin:0 0 14px">"The gear you choose is a statement about what you believe sound should be. Make Your Mark is about showing your work — and being accountable to it."</p>
        <div style="font-size:12px;font-weight:600;color:#D4860A;letter-spacing:0.08em;text-transform:uppercase">Al Schmitt — Recording Engineer, 23 Grammy Awards</div>
      </div>
    </div>
  </div>

  <!-- ── SUBMIT YOUR STORY ── -->
  <div id="mym-submit" style="background:#fff;padding:96px 0 80px">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start">
      <div>
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:24px;height:3px;background:#D4860A;border-radius:2px"></div>
          <div style="font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A">Be Featured</div>
        </div>
        <h2 style="font-family:'Playfair Display',serif;font-size:44px;font-weight:700;color:var(--near-black);line-height:1.08;margin:0 0 24px">Your Studio.<br>Your Story.</h2>
        <p style="font-size:17px;color:var(--mid-grey);line-height:1.70;margin:0 0 24px">Make Your Mark features engineers and producers at every level — from career veterans to the engineers recording tomorrow's breakout artists. If you have a story worth telling and the gear to back it up, we want to hear from you.</p>
        <p style="font-size:15px;color:var(--mid-grey);line-height:1.65;margin:0 0 32px">We review every submission. Selected applicants are contacted by our editorial team to schedule a session.</p>
        <div style="display:flex;flex-direction:column;gap:14px">
          <div style="display:flex;align-items:flex-start;gap:12px">
            <div style="width:6px;height:6px;background:#D4860A;border-radius:50%;flex-shrink:0;margin-top:6px"></div>
            <div style="font-size:14px;color:var(--near-black);line-height:1.6">No follower count requirement — we care about the work, not the platform</div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px">
            <div style="width:6px;height:6px;background:#D4860A;border-radius:50%;flex-shrink:0;margin-top:6px"></div>
            <div style="font-size:14px;color:var(--near-black);line-height:1.6">VK covers production costs — no cost to you</div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px">
            <div style="width:6px;height:6px;background:#D4860A;border-radius:50%;flex-shrink:0;margin-top:6px"></div>
            <div style="font-size:14px;color:var(--near-black);line-height:1.6">Distributed across VK's channels and to our customer base</div>
          </div>
        </div>
      </div>
      <div>
        <form onsubmit="event.preventDefault();this.innerHTML='<div style=\\'padding:48px 0;text-align:center\\'><div style=\\'font-family:Playfair Display,serif;font-size:24px;font-weight:700;color:var(--near-black);margin-bottom:12px\\'>Submission received.</div><p style=\\'font-size:15px;color:var(--mid-grey);line-height:1.7\\'>Thank you. Our editorial team reviews all submissions and will reach out if your story is a fit for an upcoming episode.</p></div>'" style="background:var(--off-white);border:1px solid var(--pale-grey);border-radius:3px;padding:40px">
          <div style="font-size:15px;font-weight:600;color:var(--near-black);margin-bottom:24px">Tell us about your work</div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px">
            <div>
              <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">First Name *</label>
              <input type="text" required placeholder="First" style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
            </div>
            <div>
              <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Last Name *</label>
              <input type="text" required placeholder="Last" style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
            </div>
          </div>

          <div style="margin-bottom:14px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Email *</label>
            <input type="email" required placeholder="your@email.com" style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
          </div>

          <div style="margin-bottom:14px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Your Role *</label>
            <select required style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
              <option value="">Select your role</option>
              <option>Recording Engineer</option>
              <option>Mixing Engineer</option>
              <option>Mastering Engineer</option>
              <option>Producer</option>
              <option>Studio Owner</option>
              <option>Artist / Musician</option>
              <option>Other</option>
            </select>
          </div>

          <div style="margin-bottom:14px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Notable Credits (optional)</label>
            <input type="text" placeholder="Artists, albums, or projects you have worked on" style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'">
          </div>

          <div style="margin-bottom:24px">
            <label style="display:block;font-size:12px;font-weight:600;color:var(--near-black);letter-spacing:0.04em;margin-bottom:6px">Your Story *</label>
            <textarea rows="4" required placeholder="Tell us about your studio, your process, and why your story belongs in Make Your Mark..." style="width:100%;padding:10px 12px;border:1px solid var(--pale-grey);border-radius:3px;font-size:14px;font-family:var(--font-body);background:#fff;box-sizing:border-box;resize:vertical;outline:none;color:var(--near-black)" onfocus="this.style.borderColor='#D4860A'" onblur="this.style.borderColor='var(--pale-grey)'"></textarea>
          </div>

          <button type="submit" style="width:100%;background:#D4860A;color:#fff;font-size:13px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;padding:15px 24px;border:none;border-radius:3px;cursor:pointer;font-family:var(--font-body)" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">Submit My Story</button>
        </form>
      </div>
    </div>
  </div>

  <!-- ── CONFIDENCE STRIP ── -->
  <div style="background:var(--off-white);border-top:2px solid var(--pale-grey);padding:56px 0">
    <div style="max-width:1280px;margin:0 auto;padding:0 40px;display:grid;grid-template-columns:repeat(4,1fr);gap:32px">
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Free to Watch</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">No account. No paywall. Every episode available to everyone, always.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Real Studios</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">Filmed on-location at working studios — not a set. Real rooms, real gear, real sessions.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">New Monthly</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">New episodes drop monthly. Subscribe to the VK newsletter and never miss one.</p>
      </div>
      <div style="text-align:center">
        <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:var(--near-black);margin-bottom:8px">Submit Your Story</div>
        <p style="font-size:13px;color:var(--mid-grey);line-height:1.6;margin:0">We feature engineers at every level. If your work is serious, your story belongs here.</p>
      </div>
    </div>
  </div>

  <div id="footer-make-your-mark"></div>
</div>
"""

    inline_js = """\
<script>
  (function() {
    var p = 'make-your-mark';
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
