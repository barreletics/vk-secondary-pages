"""style-guide.html — VK Secondary Pages Design System Reference."""
import re

SLUG  = "style-guide"
TITLE = "Style Guide — VK Secondary Pages Design System | Vintage King"
META  = "Design system reference for Vintage King secondary pages. Color rules, typography scale, badge system, component patterns, and page type classification."

INLINE_JS = """\
<script>
(function(){
  document.querySelectorAll('.sg-copy').forEach(function(btn){
    btn.addEventListener('click',function(){
      var code = btn.previousElementSibling.textContent;
      navigator.clipboard.writeText(code.trim());
      btn.textContent='Copied';
      setTimeout(function(){btn.textContent='Copy';},1200);
    });
  });
})();
</script>
"""

PAGE_BODY = """\
<div id="page-style-guide">
<style>
  #page-style-guide { font-family:'DM Sans',sans-serif;color:#1A1A18 }
  .sg-wrap { max-width:1160px;margin:0 auto;padding:0 40px }
  .sg-section { padding:64px 0;border-bottom:1px solid rgba(26,26,24,0.08) }
  .sg-section:last-of-type { border-bottom:none }
  .sg-eyebrow { font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;margin-bottom:12px }
  .sg-h2 { font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin:0 0 8px;line-height:1.2 }
  .sg-sub { font-size:15px;color:rgba(26,26,24,0.55);margin:0 0 48px;line-height:1.6 }
  .sg-rule { background:#fff;border:1px solid rgba(26,26,24,0.1);border-radius:3px;padding:28px 32px;margin-bottom:12px }
  .sg-rule-label { font-size:10px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:rgba(26,26,24,0.4);margin-bottom:8px }
  .sg-rule-value { font-size:15px;font-weight:500;color:#1A1A18;line-height:1.5 }
  .sg-rule-note { font-size:13px;color:rgba(26,26,24,0.5);margin-top:4px;line-height:1.5 }
  .sg-grid-2 { display:grid;grid-template-columns:1fr 1fr;gap:12px }
  .sg-grid-3 { display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px }
  .sg-swatch { height:72px;border-radius:3px;display:flex;align-items:flex-end;padding:10px 14px }
  .sg-swatch-label { font-size:11px;font-weight:600;letter-spacing:0.06em;color:#fff }
  .sg-swatch-dark .sg-swatch-label { color:#1A1A18 }
  .sg-type-row { display:grid;grid-template-columns:180px 1fr;gap:24px;align-items:baseline;padding:20px 0;border-bottom:1px solid rgba(26,26,24,0.06) }
  .sg-type-row:last-child { border-bottom:none }
  .sg-type-meta { font-size:11px;color:rgba(26,26,24,0.45);line-height:1.5 }
  .sg-badge-row { display:flex;gap:12px;flex-wrap:wrap;align-items:center;padding:20px 0;border-bottom:1px solid rgba(26,26,24,0.06) }
  .sg-badge-row:last-child { border-bottom:none }
  .sg-badge-label { font-size:11px;color:rgba(26,26,24,0.45);width:140px;flex-shrink:0 }
  .sg-page-type { background:#fff;border:1px solid rgba(26,26,24,0.1);border-radius:3px;padding:24px 28px }
  .sg-page-type-tag { display:inline-block;font-size:10px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:3px 10px;border-radius:2px;margin-bottom:12px }
  .sg-page-type h4 { font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#1A1A18;margin:0 0 8px }
  .sg-page-type p { font-size:13px;color:rgba(26,26,24,0.55);line-height:1.6;margin:0 0 14px }
  .sg-page-type ul { font-size:13px;color:rgba(26,26,24,0.55);margin:0;padding-left:18px;line-height:1.8 }
  .sg-code { background:rgba(26,26,24,0.04);border:1px solid rgba(26,26,24,0.08);border-radius:3px;padding:16px 20px;font-family:monospace;font-size:13px;color:#1A1A18;line-height:1.6;margin-top:12px;position:relative }
  .sg-copy { position:absolute;top:10px;right:12px;font-size:11px;font-weight:600;letter-spacing:0.06em;background:#1A1A18;color:#fff;border:none;cursor:pointer;padding:4px 10px;border-radius:2px;font-family:'DM Sans',sans-serif }
  .sg-do-dont { display:grid;grid-template-columns:1fr 1fr;gap:2px;background:rgba(26,26,24,0.08);border-radius:3px;overflow:hidden;margin-top:24px }
  .sg-do { background:#fff;padding:24px 28px }
  .sg-dont { background:#fff;padding:24px 28px }
  .sg-do-label { font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#22863a;margin-bottom:14px }
  .sg-dont-label { font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#C0392B;margin-bottom:14px }
  .sg-do-item,.sg-dont-item { font-size:13px;color:rgba(26,26,24,0.7);line-height:1.7;padding:3px 0 }
</style>

<div id="nav-style-guide"></div>

<!-- ── HERO ── -->
<section style="background:#EDE8E2;padding:80px 0 64px">
  <div class="sg-wrap">
    <div style="font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A;margin-bottom:14px">Design System</div>
    <h1 style="font-family:'Playfair Display',serif;font-size:56px;font-weight:700;color:#1A1A18;line-height:1.06;margin:0 0 20px">VK Style Guide</h1>
    <p style="font-size:18px;color:rgba(26,26,24,0.6);line-height:1.65;max-width:560px;margin:0 0 32px">Color rules, typography scale, badge system, hero patterns, and page type classification for all secondary pages.</p>
    <div style="display:flex;gap:24px;flex-wrap:wrap">
      <a href="#colors" style="font-size:13px;font-weight:600;color:#1A1A18;text-decoration:none;border-bottom:2px solid #D4860A;padding-bottom:2px">Colors</a>
      <a href="#typography" style="font-size:13px;font-weight:600;color:#1A1A18;text-decoration:none;border-bottom:2px solid rgba(26,26,24,0.2);padding-bottom:2px">Typography</a>
      <a href="#badges" style="font-size:13px;font-weight:600;color:#1A1A18;text-decoration:none;border-bottom:2px solid rgba(26,26,24,0.2);padding-bottom:2px">Badges</a>
      <a href="#heroes" style="font-size:13px;font-weight:600;color:#1A1A18;text-decoration:none;border-bottom:2px solid rgba(26,26,24,0.2);padding-bottom:2px">Hero Patterns</a>
      <a href="#pages" style="font-size:13px;font-weight:600;color:#1A1A18;text-decoration:none;border-bottom:2px solid rgba(26,26,24,0.2);padding-bottom:2px">Page Types</a>
    </div>
  </div>
</section>

<!-- ── COLORS ── -->
<section id="colors" class="sg-section" style="background:#fff">
  <div class="sg-wrap">
    <div class="sg-eyebrow">01 — Color System</div>
    <h2 class="sg-h2">Two-Accent Rule</h2>
    <p class="sg-sub">The entire secondary page system runs on two accents. The choice is determined by page type — not personal preference.</p>

    <div class="sg-do-dont">
      <div class="sg-do">
        <div class="sg-do-label">✓ Amber — Informational / Editorial</div>
        <div class="sg-do-item">Hall of Fame gear guides (Fairchild, LA-2A, U47)</div>
        <div class="sg-do-item">Gear Guide articles (Neve 1073 Guide)</div>
        <div class="sg-do-item">Magazine / editorial (Playback)</div>
        <div class="sg-do-item">About, careers, historical content</div>
        <div class="sg-do-item">Section eyebrows, year markers, timeline dots, badges</div>
      </div>
      <div class="sg-dont">
        <div class="sg-dont-label">✓ Red — Transactional / Program</div>
        <div class="sg-do-item">Trade Program, Audio Consultants</div>
        <div class="sg-do-item">Studio Professionals, Financing</div>
        <div class="sg-do-item">Any page where the primary goal is a form submission or purchase</div>
        <div class="sg-do-item">Section eyebrows, form accents, program badges</div>
      </div>
    </div>

    <div style="margin-top:12px;background:rgba(26,26,24,0.04);border-left:3px solid #1A1A18;padding:14px 20px;font-size:13px;color:rgba(26,26,24,0.65);line-height:1.6">
      <strong>Universal rule:</strong> CTAs and Shop buttons are always Red <code>#C0392B</code> regardless of page type. Amber never appears on a buy/CTA button.
    </div>

    <div style="margin-top:40px;margin-bottom:20px;font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:rgba(26,26,24,0.4)">Full Palette</div>
    <div class="sg-grid-3" style="margin-bottom:16px">
      <div>
        <div class="sg-swatch" style="background:#D4860A"><span class="sg-swatch-label">#D4860A — Amber</span></div>
        <div style="font-size:12px;color:rgba(26,26,24,0.5);margin-top:6px">Editorial accent · Vintage/Used pricing · HOF eyebrows</div>
      </div>
      <div>
        <div class="sg-swatch" style="background:#C0392B"><span class="sg-swatch-label">#C0392B — VK Red</span></div>
        <div style="font-size:12px;color:rgba(26,26,24,0.5);margin-top:6px">All CTAs · Transactional page accent · Form focus borders</div>
      </div>
      <div>
        <div class="sg-swatch" style="background:#1A1A18"><span class="sg-swatch-label">#1A1A18 — Near-Black</span></div>
        <div style="font-size:12px;color:rgba(26,26,24,0.5);margin-top:6px">All body text · Headings · Dark section backgrounds</div>
      </div>
    </div>
    <div class="sg-grid-3">
      <div>
        <div class="sg-swatch sg-swatch-dark" style="background:#EDE8E2;border:1px solid rgba(26,26,24,0.1)"><span class="sg-swatch-label">#EDE8E2 — Hero Bg</span></div>
        <div style="font-size:12px;color:rgba(26,26,24,0.5);margin-top:6px">Hero sections · CTA sections on all secondary pages</div>
      </div>
      <div>
        <div class="sg-swatch sg-swatch-dark" style="background:#F7F5F2;border:1px solid rgba(26,26,24,0.1)"><span class="sg-swatch-label">#F7F5F2 — Off-White</span></div>
        <div style="font-size:12px;color:rgba(26,26,24,0.5);margin-top:6px">Grid/card section backgrounds · var(--off-white)</div>
      </div>
      <div>
        <div class="sg-swatch sg-swatch-dark" style="background:#FDFCFB;border:1px solid rgba(26,26,24,0.1)"><span class="sg-swatch-label">#FDFCFB — Warm White</span></div>
        <div style="font-size:12px;color:rgba(26,26,24,0.5);margin-top:6px">Credential strips · Stat bars · var(--warm-white)</div>
      </div>
    </div>

    <div style="margin-top:24px;background:rgba(192,57,43,0.06);border:1px solid rgba(192,57,43,0.15);border-radius:3px;padding:16px 20px">
      <div style="font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#C0392B;margin-bottom:8px">Banned</div>
      <div style="font-size:13px;color:rgba(26,26,24,0.7);line-height:1.7">
        <code>#fde8e6</code> — too pinkish. Use <code>rgba(26,26,24,0.07)</code> for neutral badge/pill backgrounds.<br>
        <code>rgba(192,57,43,0.04–0.08)</code> as standalone section background — looks pinkish. Use <code>var(--off-white)</code>.<br>
        Amber on CTAs, shop buttons, or any actionable element.
      </div>
    </div>
  </div>
</section>

<!-- ── TYPOGRAPHY ── -->
<section id="typography" class="sg-section" style="background:var(--off-white,#F7F5F2)">
  <div class="sg-wrap">
    <div class="sg-eyebrow">02 — Typography</div>
    <h2 class="sg-h2">Type Scale</h2>
    <p class="sg-sub">Two fonts only. Playfair Display for display/headings. DM Sans for everything else. Never mix on the same element type.</p>

    <div style="background:#fff;border:1px solid rgba(26,26,24,0.1);border-radius:3px;overflow:hidden">
      <div class="sg-type-row" style="padding:20px 28px">
        <div class="sg-type-meta">Display H1<br>Playfair Display<br>48–56px / weight 700<br>line-height 1.05</div>
        <div style="font-family:'Playfair Display',serif;font-size:52px;font-weight:700;color:#1A1A18;line-height:1.05">Hero Headline</div>
      </div>
      <div class="sg-type-row" style="padding:20px 28px">
        <div class="sg-type-meta">H2 Section<br>Playfair Display<br>32–40px / weight 700<br>line-height 1.2</div>
        <div style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;line-height:1.2">Section Heading</div>
      </div>
      <div class="sg-type-row" style="padding:20px 28px">
        <div class="sg-type-meta">H3 Card<br>Playfair Display<br>18–22px / weight 700<br>line-height 1.3</div>
        <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:#1A1A18;line-height:1.3">Card or Sub-heading</div>
      </div>
      <div class="sg-type-row" style="padding:20px 28px">
        <div class="sg-type-meta">Eyebrow<br>DM Sans<br>11–12px / weight 700<br>uppercase / 0.18–0.22em tracking</div>
        <div style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#D4860A">Section Eyebrow Label</div>
      </div>
      <div class="sg-type-row" style="padding:20px 28px">
        <div class="sg-type-meta">Body<br>DM Sans<br>15–17px / weight 400<br>line-height 1.65–1.75</div>
        <div style="font-family:'DM Sans',sans-serif;font-size:16px;color:rgba(26,26,24,0.7);line-height:1.7">Body copy. Readable at arm's length. Never below 12px anywhere on the page including captions, labels, and footnotes.</div>
      </div>
      <div class="sg-type-row" style="padding:20px 28px">
        <div class="sg-type-meta">Pricing<br>DM Sans ONLY<br>weight 500<br>color: near-black</div>
        <div style="font-family:'DM Sans',sans-serif;font-size:18px;font-weight:500;color:#1A1A18">$4,999 · From $34.99</div>
      </div>
      <div class="sg-type-row" style="padding:20px 28px;border-bottom:none">
        <div class="sg-type-meta">Stat Number<br>Playfair Display<br>28–40px / weight 700<br>color: near-black</div>
        <div style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;line-height:1">30+</div>
      </div>
    </div>

    <div style="margin-top:24px;background:rgba(26,26,24,0.04);border-left:3px solid #1A1A18;padding:14px 20px;font-size:13px;color:rgba(26,26,24,0.65);line-height:1.6">
      <strong>Pricing rule:</strong> DM Sans only on all numbers and prices. Never Playfair Display on pricing. Font-weight 500, color near-black.
    </div>
  </div>
</section>

<!-- ── BADGES ── -->
<section id="badges" class="sg-section" style="background:#fff">
  <div class="sg-wrap">
    <div class="sg-eyebrow">03 — Badge System</div>
    <h2 class="sg-h2">Labels &amp; Badges</h2>
    <p class="sg-sub">Text-only. No filled pill backgrounds on editorial pages. Inline display, flowing with card content.</p>

    <div style="background:var(--off-white,#F7F5F2);border-radius:3px;overflow:hidden">

      <div class="sg-badge-row" style="padding:20px 28px">
        <div class="sg-badge-label">Version tag<br><span style="color:#D4860A">Amber — editorial</span></div>
        <div style="font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#D4860A">Rev 1 — "Grayface"</div>
        <div style="font-size:13px;color:rgba(26,26,24,0.5);margin-left:24px">Used in HOF timelines. Text only, no fill.</div>
      </div>

      <div class="sg-badge-row" style="padding:20px 28px">
        <div class="sg-badge-label">Buyer guide tag<br><span style="color:#D4860A">Amber — editorial</span></div>
        <div style="font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#D4860A">In the Box</div>
        <div style="font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#D4860A;margin-left:16px">Reference</div>
        <div style="font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#D4860A;margin-left:16px">Pro Studio</div>
        <div style="font-size:13px;color:rgba(26,26,24,0.5);margin-left:24px">Top of card, inline block, bottom padding 10px.</div>
      </div>

      <div class="sg-badge-row" style="padding:20px 28px">
        <div class="sg-badge-label">Program badge<br><span style="color:#C0392B">Red — transactional</span></div>
        <div style="font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#C0392B">VK Exclusive</div>
        <div style="font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#C0392B;margin-left:16px">Trade Credit</div>
        <div style="font-size:13px;color:rgba(26,26,24,0.5);margin-left:24px">Used on program/transactional pages only.</div>
      </div>

      <div class="sg-badge-row" style="padding:20px 28px;border-bottom:none">
        <div class="sg-badge-label">Vintage price<br><span style="color:#D4860A">Amber always</span></div>
        <div style="font-family:'DM Sans',sans-serif;font-size:13px;font-weight:500;color:#D4860A">Used — $4,800</div>
        <div style="font-size:13px;color:rgba(26,26,24,0.5);margin-left:24px">Vintage/used pricing labels only. DM Sans, weight 500.</div>
      </div>
    </div>

    <div class="sg-do-dont" style="margin-top:24px">
      <div class="sg-do">
        <div class="sg-do-label">Do</div>
        <div class="sg-do-item">Text-only badges, no fill background</div>
        <div class="sg-do-item">Inline flow at top of card content</div>
        <div class="sg-do-item">10px, 700 weight, 0.1em tracking, uppercase</div>
        <div class="sg-do-item">Amber on editorial badges, red on program badges</div>
        <div class="sg-do-item">Only use badges if factually accurate</div>
      </div>
      <div class="sg-dont">
        <div class="sg-dont-label">Don't</div>
        <div class="sg-do-item">Filled pill/chip background on badges</div>
        <div class="sg-do-item">position:absolute on badge — causes clip/overlap issues</div>
        <div class="sg-do-item">Invent badges that aren't factually accurate</div>
        <div class="sg-do-item">Mix amber and red badges on the same page</div>
        <div class="sg-do-item">White text on colored fill badges</div>
      </div>
    </div>
  </div>
</section>

<!-- ── HEROES ── -->
<section id="heroes" class="sg-section" style="background:var(--off-white,#F7F5F2)">
  <div class="sg-wrap">
    <div class="sg-eyebrow">04 — Hero Patterns</div>
    <h2 class="sg-h2">Hero Types</h2>
    <p class="sg-sub">Two hero patterns. Choice is determined by whether you have a product photo.</p>

    <div class="sg-grid-2">
      <div class="sg-rule">
        <div class="sg-rule-label">Type A — Photo Hero (HOF / Gear Guide)</div>
        <div class="sg-rule-value">50/50 full-bleed grid</div>
        <div class="sg-rule-note">
          Left panel: <code>background:#EDE8E2</code> · text, eyebrow, CTAs<br>
          Right panel: <code>background:#fff</code> · product photo<br>
          Image: <code>object-fit:contain</code> · height:460–520px<br>
          Section: <code>grid-template-columns:1fr 1fr;min-height:560px</code><br>
          Used on: Fairchild, LA-2A, U47, Neve guides
        </div>
      </div>
      <div class="sg-rule">
        <div class="sg-rule-label">Type B — Stats Hero (Program / No photo)</div>
        <div class="sg-rule-value">50/50 full-bleed grid</div>
        <div class="sg-rule-note">
          Left panel: <code>background:#EDE8E2</code> · text, eyebrow, CTAs<br>
          Right panel: <code>background:#fff</code> · 2×2 stats grid<br>
          Stats grid: <code>grid-template-columns:1fr 1fr;gap:1px;background:rgba(26,26,24,0.08)</code><br>
          Stat number: Playfair Display 32px · label: 11px uppercase<br>
          Used on: Trade Program, Studio Professionals
        </div>
      </div>
    </div>

    <div style="margin-top:12px" class="sg-rule">
      <div class="sg-rule-label">Never</div>
      <div class="sg-rule-note">
        Dark hero backgrounds on secondary pages — always light <code>#EDE8E2</code> left panel.<br>
        <code>object-fit:cover</code> on product shots with white backgrounds — use <code>contain</code>.<br>
        Captions referencing specific studios/clients unless VK-verified.
      </div>
    </div>
  </div>
</section>

<!-- ── PAGE TYPES ── -->
<section id="pages" class="sg-section" style="background:#fff">
  <div class="sg-wrap">
    <div class="sg-eyebrow">05 — Page Classification</div>
    <h2 class="sg-h2">Page Types</h2>
    <p class="sg-sub">Every page belongs to one of two types. This determines accent color, badge color, and hero treatment.</p>

    <div class="sg-grid-2">
      <div class="sg-page-type">
        <div class="sg-page-type-tag" style="background:#FEF3E2;color:#D4860A">Editorial / Informational</div>
        <h4>HOF &amp; Gear Guides</h4>
        <p>Content-first pages. Goal is to educate and build trust. The purchase happens at Vintage King but the decision is made here.</p>
        <ul>
          <li>Fairchild 660/670</li>
          <li>Teletronix LA-2A</li>
          <li>Neumann U 47 / U 48</li>
          <li>Neve 1073 (all versions)</li>
          <li>PLAYBACK Magazine</li>
          <li>Hall of Fame index</li>
          <li>About, Careers</li>
        </ul>
        <div style="margin-top:16px;font-size:12px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A">Accent: Amber #D4860A</div>
      </div>
      <div class="sg-page-type">
        <div class="sg-page-type-tag" style="background:rgba(192,57,43,0.08);color:#C0392B">Transactional / Program</div>
        <h4>Program &amp; Conversion Pages</h4>
        <p>Action-first pages. Goal is form submission, quote request, or direct purchase. Every element drives toward one CTA.</p>
        <ul>
          <li>Trade Program</li>
          <li>Audio Consultants</li>
          <li>Studio Professionals</li>
          <li>Financing / Section 179</li>
          <li>Make Your Mark (careers form)</li>
        </ul>
        <div style="margin-top:16px;font-size:12px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#C0392B">Accent: Red #C0392B</div>
      </div>
    </div>

    <div style="margin-top:24px;background:rgba(26,26,24,0.04);border-radius:3px;padding:24px 28px">
      <div style="font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:rgba(26,26,24,0.4);margin-bottom:12px">Universal — applies to both types</div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;font-size:13px;color:rgba(26,26,24,0.65);line-height:1.7">
        <div><strong style="display:block;color:#1A1A18;margin-bottom:4px">CTAs &amp; Shop Buttons</strong>Always Red #C0392B. No exceptions.</div>
        <div><strong style="display:block;color:#1A1A18;margin-bottom:4px">Sticky Bar</strong>Dark (#1A1A18) bar, Red CTA, ghost link. Every page.</div>
        <div><strong style="display:block;color:#1A1A18;margin-bottom:4px">Form Focus</strong>Always var(--vk-red) border regardless of page type.</div>
        <div><strong style="display:block;color:#1A1A18;margin-bottom:4px">Min Font Size</strong>12px everywhere. Nothing below 12px.</div>
        <div><strong style="display:block;color:#1A1A18;margin-bottom:4px">Pricing</strong>DM Sans only, weight 500, near-black. Never Playfair on numbers.</div>
        <div><strong style="display:block;color:#1A1A18;margin-bottom:4px">JSON-LD</strong>Every page needs at least one structured data block.</div>
      </div>
    </div>
  </div>
</section>

<!-- ── STICKY BAR ── -->
<section class="sg-section" style="background:var(--off-white,#F7F5F2)">
  <div class="sg-wrap">
    <div class="sg-eyebrow">06 — Sticky Bar</div>
    <h2 class="sg-h2">Bottom Sticky Bar</h2>
    <p class="sg-sub">Required on every page. Fixed to the bottom of the viewport. Dark background, red CTA, ghost secondary link.</p>

    <div style="background:#1A1A18;border-top:2px solid #C0392B;padding:14px 40px;display:flex;align-items:center;justify-content:space-between;border-radius:3px">
      <div>
        <div style="font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB">Page Title or Product Name</div>
        <div style="font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px">Supporting context — price range or program benefit</div>
      </div>
      <div style="display:flex;gap:12px;align-items:center">
        <span style="background:#C0392B;color:#fff;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;letter-spacing:0.04em;cursor:default">Primary CTA</span>
        <span style="color:rgba(255,255,255,0.6);font-size:13px;font-weight:500;cursor:default;padding:12px 0">Secondary Link</span>
      </div>
    </div>
    <div style="margin-top:16px;font-size:13px;color:rgba(26,26,24,0.5);line-height:1.6">
      CSS: <code>position:fixed;bottom:0;left:0;right:0;z-index:500</code> · Add <code>height:68px</code> spacer div before closing wrapper to prevent content overlap.
    </div>
  </div>
</section>

<div id="footer-style-guide"></div>

  <style>.vk-stick{position:fixed;bottom:0;left:0;right:0;background:#1A1A18;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;border-top:2px solid #C0392B}.vk-stick-title{font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB}.vk-stick-sub{font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px}.vk-stick-cta{background:#C0392B;color:#fff;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em}.vk-stick-ghost{color:rgba(255,255,255,0.6);font-size:13px;font-weight:500;text-decoration:none;padding:12px 0}@media(max-width:700px){.vk-stick{padding:12px 20px}}</style>
  <div class="vk-stick">
    <div>
      <div class="vk-stick-title">VK Style Guide</div>
      <div class="vk-stick-sub">Color · Typography · Badges · Heroes · Page Types</div>
    </div>
    <div style="display:flex;gap:12px;align-items:center">
      <a href="navigator.html" class="vk-stick-cta">View Navigator</a>
      <a href="hall-of-fame.html" class="vk-stick-ghost">Hall of Fame ↑</a>
    </div>
  </div>
  <div style="height:68px"></div>
</div>
"""

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "VK Secondary Pages Style Guide",
  "description": "Design system reference for Vintage King secondary pages.",
  "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
}
</script>
"""

def build(src_html, head_css, nav_tpl, foot_tpl, js_nav):
    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head_css, flags=re.DOTALL)
    head = re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{META}">', head)
    head += '  <style id="vk-standalone-patch">.page{{display:block!important}}</style>\n'
    return (
        head + "\n</head>\n<body>\n"
        + nav_tpl + foot_tpl
        + JSON_LD + PAGE_BODY
        + js_nav + INLINE_JS
        + "</body>\n</html>\n"
    )
