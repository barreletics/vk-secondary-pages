"""neve-1073-guide-v2.html — Full-width editorial version: no sidebar, wider content, studio cards first."""
import re

SLUG  = "neve-1073-guide-v2"
TITLE = "Neve 1073 Guide — The Rooms, The Record, The Sound | Vintage King Audio"
META  = "Full-width editorial guide to the Neve 1073. Three iconic studios, specs, engineer notes, and every version available from Vintage King. The definitive buyer and history resource."

IMG = {
    "vertical_80s": "images/neve-1073/AMS-Neve-1073-80-series-Microphone-Preamp-EQ-vertical-069ce358-237f-4b27-8808-f5930ffd9dc3.png",
    "rack_front":   "images/neve-1073/1073_Rack_FrontHigh-72615813-842a-4121-a8d6-326d02b43c28.png",
    "h_left_lg":    "images/neve-1073/1073-Classic-H-3_4-Left-RT-2048x1198-4a5a8893-ea04-4326-b7b6-e2e5ab2bcb6e.png",
    "h_left_sm":    "images/neve-1073/1073-Classic-H-3_4-Left-RT-1024x599-e1349f25-77a4-4f28-bf3e-5933ccb4c526.png",
    "h_right":      "images/neve-1073/1073-Classic-H-3_4-Right-RT-1024x633-fad3dad8-4075-4ea1-bd34-c17291706280.png",
    "h_rear":       "images/neve-1073/1073-Classic-H-Rear-Raised-RT-1024x674-04ff66a7-26e2-4f34-8159-977a1535f5d7.png",
    "rack_front2":  "images/neve-1073/1073_Rack_FrontHigh-a273ef28-c378-4c7e-9537-25d2cc835946.png",
}

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Neve 1073 Guide — The Rooms, The Record, The Sound",
      "description": "Full-width editorial guide to the AMS Neve 1073. Three iconic 80 Series studio rooms, complete specifications, engineer notes, and every version available from Vintage King.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "AMS Neve 1073 Mic Preamp & Equaliser",
      "brand": {"@type": "Brand", "name": "AMS Neve"},
      "description": "Class A discrete mic preamp and EQ. Marinair transformers, hand-built UK. 1970–present.",
      "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}}
    }
  ]
}
</script>
"""

CHROME = """\
<nav class="vk-secondary-chrome" aria-label="Secondary pages nav" style="position:sticky;top:0;z-index:400;background:#1A1A18;color:#FDFCFB;padding:10px 20px;font-size:12px;font-family:var(--font-body);display:flex;align-items:center;gap:12px;flex-wrap:wrap;border-bottom:1px solid rgba(255,255,255,0.12)">
  <a href="navigator.html" style="color:#FDFCFB;font-weight:600;text-decoration:none">Roadmap</a>
  <span style="opacity:0.35">|</span>
  <a href="hall-of-fame.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Hall of Fame</a>
  <span style="opacity:0.35">|</span>
  <a href="neve-1073.html" style="color:rgba(255,255,255,0.55);text-decoration:none">1073 Overview</a>
  <span style="opacity:0.35">|</span>
  <a href="neve-1073-guide.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Guide v1</a>
  <span style="opacity:0.35">|</span>
  <span style="opacity:0.75">Guide v2 — Editorial</span>
</nav>
"""

PAGE_BODY = f"""\
<div id="neve-1073-guide-v2" class="page active">
  <div id="nav-neve-1073-guide-v2"></div>

  <style>
    /* v2 — full-width editorial, no sidebar */
    .nv2-wrap {{ max-width:860px;margin:0 auto;padding:0 32px }}
    .nv2-wide {{ max-width:1280px;margin:0 auto;padding:0 48px }}

    .nv2-bread {{ max-width:1280px;margin:0 auto;padding:14px 48px;font-size:13px;color:rgba(26,26,24,0.42);font-family:'DM Sans',sans-serif }}
    .nv2-bread a {{ color:rgba(26,26,24,0.42);text-decoration:none }}
    .nv2-bread a:hover {{ color:#D4860A }}
    .nv2-bread span {{ margin:0 8px }}

    .nv2-body h2 {{ font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;margin:56px 0 16px;line-height:1.2 }}
    .nv2-body h2:first-child {{ margin-top:0 }}
    .nv2-body p {{ font-size:16px;color:#3A3A38;line-height:1.82;margin-bottom:18px }}
    .nv2-body strong {{ color:#1A1A18;font-weight:600 }}
    .nv2-body ul {{ margin:14px 0 18px 22px;font-size:16px;color:#3A3A38;line-height:1.85 }}

    /* Pull quote — amber accent */
    .nv2-pull {{ border-left:3px solid #D4860A;padding:20px 28px;margin:44px 0;background:rgba(212,134,10,0.05) }}
    .nv2-pull p {{ font-family:'Playfair Display',serif;font-size:22px;font-style:italic;line-height:1.5;color:#1A1A18;margin:0!important }}
    .nv2-pull cite {{ display:block;margin-top:10px;font-size:12px;font-style:normal;color:rgba(26,26,24,0.42);letter-spacing:0.08em;text-transform:uppercase }}

    /* Full-width gear photo strip */
    .nv2-strip {{ margin:52px 0;background:#fff;padding:48px }}
    .nv2-strip img {{ display:block;max-width:100%;max-height:400px;margin:0 auto;object-fit:contain }}
    .nv2-strip-cap {{ max-width:860px;margin:12px auto 0;padding:9px 0 0;font-size:12px;color:rgba(26,26,24,0.48);font-style:italic;border-top:1px solid rgba(26,26,24,0.09) }}
    .nv2-strip-cap strong {{ color:rgba(26,26,24,0.65);font-style:normal }}

    /* Studio grid — 3 col, full-width */
    .nv2-studios {{ max-width:1280px;margin:52px auto;padding:0 48px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px }}
    .nv2-sc {{ background:#1A1A18;overflow:hidden }}
    .nv2-sc-img {{ height:220px;position:relative;display:flex;align-items:center;justify-content:center }}
    .nv2-sc-badge {{ position:absolute;top:12px;left:12px;font-size:10px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;background:rgba(0,0,0,0.6);padding:3px 9px }}
    .nv2-sc-loc {{ position:absolute;bottom:12px;left:0;right:0;text-align:center;font-size:11px;color:rgba(255,255,255,0.22);letter-spacing:0.06em }}
    .nv2-sc-body {{ padding:22px 18px 24px }}
    .nv2-sc-name {{ font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#fff;margin-bottom:3px }}
    .nv2-sc-sub {{ font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#D4860A;margin-bottom:10px }}
    .nv2-sc-desc {{ font-size:13px;color:rgba(255,255,255,0.48);line-height:1.6 }}

    /* Specs table */
    .nv2-specs {{ background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.08);overflow:hidden;margin:32px 0 }}
    .nv2-specs-hd {{ background:#1A1A18;padding:12px 20px;font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.45) }}
    .nv2-specs table {{ width:100%;border-collapse:collapse }}
    .nv2-specs tr:nth-child(even) {{ background:rgba(26,26,24,0.03) }}
    .nv2-specs td {{ padding:10px 20px;font-size:13px }}
    .nv2-specs td:first-child {{ color:rgba(26,26,24,0.48);width:46%;font-weight:500 }}
    .nv2-specs td:last-child {{ color:#1A1A18;font-weight:500 }}

    /* Records */
    .nv2-records {{ list-style:none;margin:16px 0 }}
    .nv2-records li {{ display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(26,26,24,0.07);font-size:15px;align-items:center }}
    .nv2-records li:last-child {{ border-bottom:none }}
    .nv2-rt {{ font-weight:600;color:#1A1A18 }}
    .nv2-rs {{ font-size:12px;color:rgba(26,26,24,0.42);margin-top:2px }}
    .nv2-ry {{ font-size:12px;color:rgba(26,26,24,0.35);flex-shrink:0;margin-left:16px }}

    /* Timeline */
    .nv2-tl {{ margin:32px 0 }}
    .nv2-tl-item {{ display:grid;grid-template-columns:68px 1fr;gap:20px;padding:16px 0;border-bottom:1px solid rgba(26,26,24,0.07) }}
    .nv2-tl-item:last-child {{ border-bottom:none }}
    .nv2-tl-yr {{ font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:#D4860A;padding-top:3px }}
    .nv2-tl-txt {{ font-size:14px;color:#3A3A38;line-height:1.65 }}
    .nv2-tl-txt strong {{ color:#1A1A18 }}

    /* FAQ */
    .nv2-faq-item {{ border-bottom:1px solid rgba(26,26,24,0.08) }}
    .nv2-faq-item:first-child {{ border-top:1px solid rgba(26,26,24,0.08) }}
    .nv2-faq-q {{ width:100%;text-align:left;background:none;border:none;cursor:pointer;padding:16px 0;display:flex;justify-content:space-between;align-items:center;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18 }}
    .nv2-faq-q::after {{ content:'+';font-size:20px;color:#D4860A;font-weight:300;flex-shrink:0;margin-left:16px }}
    .nv2-faq-q.open::after {{ content:'−' }}
    .nv2-faq-a {{ display:none;padding:0 0 16px;font-size:14px;color:#3A3A38;line-height:1.7 }}
    .nv2-faq-a.open {{ display:block }}

    /* Inline product cards */
    .nv2-versions {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin:32px 0 }}
    .nv2-ver {{ background:#fff;border:1px solid rgba(26,26,24,0.08);overflow:hidden }}
    .nv2-ver-img {{ height:160px;overflow:hidden;background:var(--off-white,#F7F5F2);display:flex;align-items:center;justify-content:center }}
    .nv2-ver-img img {{ max-height:100%;width:auto;max-width:100%;object-fit:contain;padding:12px }}
    .nv2-ver-body {{ padding:16px }}
    .nv2-ver-name {{ font-weight:600;color:#1A1A18;font-size:14px;margin-bottom:4px }}
    .nv2-ver-price {{ font-size:13px;color:#D4860A;font-weight:600 }}
    .nv2-ver-desc {{ font-size:12px;color:rgba(26,26,24,0.55);margin-top:6px;line-height:1.5 }}

    /* Sticky shop bar */
    .nv2-shopbar {{ position:fixed;bottom:0;left:0;right:0;background:#1A1A18;border-top:1px solid rgba(255,255,255,0.1);padding:14px 48px;display:flex;align-items:center;justify-content:space-between;z-index:300;font-family:'DM Sans',sans-serif }}
    .nv2-shopbar-text {{ font-size:13px;color:rgba(255,255,255,0.55) }}
    .nv2-shopbar-text strong {{ color:#fff }}
    .nv2-shopbar-actions {{ display:flex;gap:12px }}
    .nv2-shopbar-btn {{ padding:9px 20px;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px;cursor:pointer }}
    .nv2-shopbar-primary {{ background:#D4860A;color:#fff }}
    .nv2-shopbar-secondary {{ background:rgba(255,255,255,0.1);color:#fff }}
    .nv2-shopbar-close {{ background:none;border:none;cursor:pointer;color:rgba(255,255,255,0.3);font-size:20px;padding:0 0 0 8px;line-height:1 }}
  </style>

  <!-- BREADCRUMB -->
  <div class="nv2-bread">
    <a href="#">Home</a><span>›</span>
    <a href="#">Gear Guides</a><span>›</span>
    <a href="#">Preamps and EQs</a><span>›</span>
    The Neve 1073 — Editorial
  </div>

  <!-- ── HERO — LIGHT ── -->
  <section style="background:#EDE8E2;padding:72px 0 48px;overflow:visible">
    <div class="nv2-wide" style="display:grid;grid-template-columns:1fr 340px;gap:72px;align-items:end">
      <div style="padding-bottom:64px">
        <p style="font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A;margin-bottom:14px">Gear Guide · AMS Neve</p>
        <h1 style="font-family:'Playfair Display',serif;font-size:clamp(40px,5vw,68px);font-weight:700;line-height:1.04;color:#1A1A18;margin-bottom:22px">The Neve 1073<br><span style="font-style:italic;color:rgba(26,26,24,0.48);font-size:0.82em">The Rooms. The Record. The Sound.</span></h1>
        <p class="speakable" style="font-size:17px;color:rgba(26,26,24,0.62);line-height:1.7;max-width:560px;margin-bottom:0">Rupert Neve finalized the 1073 in 1970. Electric Lady. AIR Montserrat. Criteria Miami. Every room that mattered ran this circuit — and you can own it today in the same configuration.</p>
      </div>
      <div style="align-self:end;display:flex;align-items:flex-end;justify-content:center">
        <img src="{IMG['vertical_80s']}" alt="AMS Neve 1073 80-series module vertical" style="max-height:340px;width:auto;display:block;filter:drop-shadow(0 10px 36px rgba(26,26,24,0.16))">
      </div>
    </div>
  </section>

  <!-- STAT BAR -->
  <div style="background:var(--warm-white,#FDFCFB);border-bottom:1px solid rgba(26,26,24,0.07)">
    <div class="nv2-wide" style="display:flex;gap:0;padding-top:0;padding-bottom:0">
      <div style="flex:1;padding:22px 32px 22px 0;border-right:1px solid rgba(26,26,24,0.07)">
        <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#1A1A18">1970</div>
        <div style="font-size:12px;color:rgba(26,26,24,0.45);margin-top:3px">Year of origin</div>
      </div>
      <div style="flex:1;padding:22px 32px;border-right:1px solid rgba(26,26,24,0.07)">
        <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#1A1A18">+80dB</div>
        <div style="font-size:12px;color:rgba(26,26,24,0.45);margin-top:3px">Max mic gain</div>
      </div>
      <div style="flex:1;padding:22px 32px;border-right:1px solid rgba(26,26,24,0.07)">
        <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#1A1A18">50+</div>
        <div style="font-size:12px;color:rgba(26,26,24,0.45);margin-top:3px">Years in production</div>
      </div>
      <div style="flex:1;padding:22px 0 22px 32px">
        <div style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#1A1A18">3</div>
        <div style="font-size:12px;color:rgba(26,26,24,0.45);margin-top:3px">Iconic 8078 rooms</div>
      </div>
    </div>
  </div>

  <!-- ARTICLE — FULL WIDTH -->
  <div style="padding:72px 0 0;background:#fff">

    <!-- INTRO -->
    <div class="nv2-wrap nv2-body">
      <h2 style="margin-top:0">Born in a Workshop in Little Shelford</h2>
      <p>In the mid-1960s, Rupert Neve set up shop in Little Shelford, Cambridgeshire, determined to build audio equipment that sounded better than anything on the market. Transistors were new. Reliable faders didn't exist. None of it stopped him.</p>
      <p>By 1968, Neve Electronics had moved to a purpose-built factory in Melbourn, Hertfordshire. The <strong>Neve 1073</strong> was finalized around 1970 — a Class A microphone preamplifier with a three-band program equalizer and high-pass filter in a single module. Custom Marinair transformers and discrete transistor circuitry produced a saturation character that modern circuit design has never duplicated.</p>
    </div>

    <!-- FULL-WIDTH RACK PHOTO -->
    <div class="nv2-strip">
      <img src="{IMG['rack_front']}" alt="AMS Neve 1073 — 8-channel rack, front high view" style="object-position:center 25%">
      <div class="nv2-strip-cap"><strong>Neve 1073 — 8-channel rack.</strong> Stepped gain switch, pad, phase reverse, and three-band inductor EQ. Every module hand-wired and transformer-coupled at both input and output.</div>
    </div>

  </div>

  <!-- STUDIO LEGACY — FULL WIDTH SECTION -->
  <div style="background:var(--off-white,#F7F5F2);padding:72px 0">
    <div class="nv2-wide">
      <p style="font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A;margin-bottom:10px">The 80 Series in the Wild</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:clamp(28px,3vw,42px);font-weight:700;color:#1A1A18;margin:0 0 8px">Three Rooms That Ran the Neve 8078</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.55);max-width:600px;margin:0 0 40px">The 8078 was the last and largest of the hand-wired 80 Series consoles. Studios that had one built careers around it.</p>
    </div>
    <div class="nv2-studios">
      <!-- Electric Lady -->
      <div class="nv2-sc">
        <div class="nv2-sc-img" style="background:linear-gradient(160deg,#0d1108 0%,#161c0e 55%,#0d1108 100%)">
          <div class="nv2-sc-badge">Neve 8078</div>
          <svg width="60" height="60" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.14"><rect x="4" y="18" width="48" height="20" rx="1" stroke="#fff" stroke-width="1.2"/><line x1="4" y1="26" x2="52" y2="26" stroke="#fff" stroke-width="0.8" opacity=".4"/><rect x="7" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="15" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="23" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="31" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="39" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/></svg>
          <div class="nv2-sc-loc">Est. 1970 · Greenwich Village, NYC</div>
        </div>
        <div class="nv2-sc-body">
          <div class="nv2-sc-name">Electric Lady Studios</div>
          <div class="nv2-sc-sub">New York, NY · 1970 – Present</div>
          <p class="nv2-sc-desc">Built by Jimi Hendrix. Studio A's Neve 8078 has since recorded David Bowie (<em>Scary Monsters</em>), AC/DC (<em>Back in Black</em>), and Daft Punk (<em>Random Access Memories</em>). Still operating.</p>
        </div>
      </div>
      <!-- AIR Montserrat -->
      <div class="nv2-sc">
        <div class="nv2-sc-img" style="background:linear-gradient(160deg,#080e18 0%,#0e1828 55%,#060e18 100%)">
          <div class="nv2-sc-badge">Custom Neve 8078</div>
          <svg width="60" height="60" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.14"><rect x="4" y="18" width="48" height="20" rx="1" stroke="#fff" stroke-width="1.2"/><line x1="4" y1="26" x2="52" y2="26" stroke="#fff" stroke-width="0.8" opacity=".4"/><rect x="7" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="15" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="23" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="31" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="39" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/></svg>
          <div class="nv2-sc-loc">Est. 1979 · Montserrat, Caribbean</div>
        </div>
        <div class="nv2-sc-body">
          <div class="nv2-sc-name">AIR Studios Montserrat</div>
          <div class="nv2-sc-sub">George Martin · 1979 – 1989</div>
          <p class="nv2-sc-desc">George Martin built AIR Montserrat around a custom Neve A4792. Dire Straits' <em>Brothers in Arms</em>, The Police, Paul McCartney. Destroyed by Hurricane Hugo, 1989.</p>
        </div>
      </div>
      <!-- Criteria -->
      <div class="nv2-sc">
        <div class="nv2-sc-img" style="background:linear-gradient(160deg,#180808 0%,#280e0e 55%,#180808 100%)">
          <div class="nv2-sc-badge">Neve 8078</div>
          <svg width="60" height="60" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.14"><rect x="4" y="18" width="48" height="20" rx="1" stroke="#fff" stroke-width="1.2"/><line x1="4" y1="26" x2="52" y2="26" stroke="#fff" stroke-width="0.8" opacity=".4"/><rect x="7" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="15" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="23" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="31" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="39" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/></svg>
          <div class="nv2-sc-loc">Est. 1958 · Miami, FL</div>
        </div>
        <div class="nv2-sc-body">
          <div class="nv2-sc-name">Criteria Recording Studios</div>
          <div class="nv2-sc-sub">Miami, FL · 1958 – Present</div>
          <p class="nv2-sc-desc">The Eagles' <em>Hotel California</em>. Eric Clapton's <em>461 Ocean Boulevard</em>. The Bee Gees' disco-era run. The 8078's extended high-frequency response defined the sound of an era.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- CONT ARTICLE -->
  <div style="padding:72px 0;background:#fff">
    <div class="nv2-wrap nv2-body">

      <h2>The Sound: Why Engineers Still Reach for It</h2>
      <p>The 1073 imposes itself on the signal. Low-end is tight and authoritative. Upper-mid presence cuts through a dense mix without harshness. The source of this character is the <strong>Marinair input and output transformers</strong> — custom designs exclusive to Neve that introduce gentle second-harmonic saturation at higher signal levels, combined with Class A discrete transistor circuitry and hand-crafted inductor EQ coils.</p>
      <p>No third party has ever licensed or duplicated the Marinair specification. Every 1073 sold by AMS Neve today uses the same transformer models — 10468 mic input, 31267 line input, LO1166 output — as Rupert Neve's original 1970 drawings.</p>

      <div class="nv2-pull">
        <p>"When I walked into a room with a Neve 8078, I knew the session would sound good before I touched a single fader."</p>
        <cite>Bob Ludwig — Mastering Engineer · Stones · Nirvana · U2</cite>
      </div>

      <h2>The Records It Made</h2>
      <ul class="nv2-records">
        <li><div><div class="nv2-rt">Led Zeppelin IV</div><div class="nv2-rs">Island Studios / Headley Grange (Neve mobile)</div></div><div class="nv2-ry">1971</div></li>
        <li><div><div class="nv2-rt">Exile on Main St. — The Rolling Stones</div><div class="nv2-rs">Olympic Studios / Stargroves (Neve mobile)</div></div><div class="nv2-ry">1972</div></li>
        <li><div><div class="nv2-rt">Dark Side of the Moon — Pink Floyd</div><div class="nv2-rs">Abbey Road Studios, London</div></div><div class="nv2-ry">1973</div></li>
        <li><div><div class="nv2-rt">Rumours — Fleetwood Mac</div><div class="nv2-rs">Record Plant, Sausalito</div></div><div class="nv2-ry">1977</div></li>
        <li><div><div class="nv2-rt">Brothers in Arms — Dire Straits</div><div class="nv2-rs">AIR Studios Montserrat (Custom Neve)</div></div><div class="nv2-ry">1985</div></li>
        <li><div><div class="nv2-rt">Nevermind — Nirvana</div><div class="nv2-rs">Sound City, Van Nuys (Neve 8028)</div></div><div class="nv2-ry">1991</div></li>
      </ul>

    </div>

    <!-- Full-width module photo -->
    <div class="nv2-strip" style="margin:56px 0">
      <img src="{IMG['h_left_lg']}" alt="AMS Neve 1073 Classic H — left 3/4 detail" style="object-position:center 40%">
      <div class="nv2-strip-cap"><strong>Neve 1073 Classic H</strong> — the stepped red gain knob selects both level and source. Mic gain +20 to +80dB in 5dB steps. No separate mic/line switch.</div>
    </div>

    <div class="nv2-wrap nv2-body">
      <h2>Official Specifications</h2>
      <div class="nv2-specs">
        <div class="nv2-specs-hd">AMS Neve 1073 — Current Production</div>
        <table>
          <tr><td>Circuit type</td><td>Class A, fully discrete transistor</td></tr>
          <tr><td>Input transformers</td><td>Marinair spec (10468 mic / 31267 line) — exclusive to Neve</td></tr>
          <tr><td>Output transformer</td><td>LO1166 — designed by Rupert Neve, 1964</td></tr>
          <tr><td>Construction</td><td>Hand-built and hand-wired, UK</td></tr>
          <tr><td>Mic gain range</td><td>+20 to +80 dB in 5dB steps</td></tr>
          <tr><td>Line gain</td><td>−10 to +20 dB · 10kΩ impedance</td></tr>
          <tr><td>EIN</td><td>&lt; −125 dBu @ 60dB gain</td></tr>
          <tr><td>Max output</td><td>&gt; +26 dBu into 600Ω</td></tr>
          <tr><td>THD</td><td>&lt; 0.07% (50Hz–10kHz @ +20dBu into 600Ω)</td></tr>
          <tr><td>EQ — High shelf</td><td>±16 dB fixed at 12 kHz</td></tr>
          <tr><td>EQ — Mid peak/dip</td><td>±18 dB · 360 / 700 / 1.6k / 3.2k / 4.8k / 7.2k Hz</td></tr>
          <tr><td>EQ — Low shelf</td><td>±16 dB · 35 / 60 / 110 / 220 Hz</td></tr>
          <tr><td>High-pass filter</td><td>18 dB/oct · 50 / 80 / 160 / 300 Hz</td></tr>
          <tr><td>Phantom power</td><td>+48V switchable</td></tr>
          <tr><td>Dimensions (module)</td><td>45mm W × 222mm H × 254mm D · ~2.5kg</td></tr>
        </table>
      </div>

      <h2>Available Formats</h2>
      <div class="nv2-versions">
        <div class="nv2-ver">
          <div class="nv2-ver-img"><img src="{IMG['h_left_sm']}" alt="Neve 1073 Classic H"></div>
          <div class="nv2-ver-body">
            <div class="nv2-ver-name">1073 Classic H</div>
            <div class="nv2-ver-price">Inquire for pricing</div>
            <div class="nv2-ver-desc">Single module. Original transformer spec. Hand-wired UK. The purest expression of the 1073 circuit.</div>
          </div>
        </div>
        <div class="nv2-ver">
          <div class="nv2-ver-img" style="background:#1A1A18"><img src="{IMG['vertical_80s']}" alt="Neve 1073 500 Series module"></div>
          <div class="nv2-ver-body">
            <div class="nv2-ver-name">1073 SPX / 500 Series</div>
            <div class="nv2-ver-price">From $799</div>
            <div class="nv2-ver-desc">500 Series format. Marinair transformer topology. Compatible with any 500 Series lunchbox.</div>
          </div>
        </div>
        <div class="nv2-ver">
          <div class="nv2-ver-img" style="background:#1A1A18"><img src="{IMG['rack_front2']}" alt="Neve 1073 OPX 8-channel rack"></div>
          <div class="nv2-ver-body">
            <div class="nv2-ver-name">1073OPX — 8 Channel</div>
            <div class="nv2-ver-price">From $6,499</div>
            <div class="nv2-ver-desc">Eight 1073 circuits in 3U. Individual phantom, pad, polarity per channel. Same transformer spec throughout.</div>
          </div>
        </div>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div>
        <div class="nv2-faq-item">
          <button class="nv2-faq-q" onclick="nv2Faq(this)">What is the Neve 1073?</button>
          <div class="nv2-faq-a">A microphone preamplifier and three-band equalizer module designed by Rupert Neve around 1970. Class A discrete transistor circuitry, exclusive Marinair transformers, hand-built in the UK. The only preamp still in continuous production to its original specification after more than fifty years.</div>
        </div>
        <div class="nv2-faq-item">
          <button class="nv2-faq-q" onclick="nv2Faq(this)">What consoles used the Neve 1073?</button>
          <div class="nv2-faq-a">The 1073 was designed for the Wessex A88 and used in early Neve 80 Series consoles (8014, 8034). Related modules (1073b, 31102, 31105) with the same Marinair transformer spec were used in the 8028, 8058, 8068, and 8078. All share the same fundamental sonic character.</div>
        </div>
        <div class="nv2-faq-item">
          <button class="nv2-faq-q" onclick="nv2Faq(this)">How is the Neve 1073 different from clones?</button>
          <div class="nv2-faq-a">The original uses exclusive Marinair specification input transformers (10468 and 31267) and Rupert Neve's LO1166 output transformer — both unavailable to any third party. Hand-wired construction follows Rupert Neve's original 1970 drawings. The specific harmonic character this combination produces has never been duplicated.</div>
        </div>
        <div class="nv2-faq-item">
          <button class="nv2-faq-q" onclick="nv2Faq(this)">Can I buy a vintage original Neve 1073?</button>
          <div class="nv2-faq-a">Authentic examples have become increasingly rare. Vintage King regularly sources and inspects vintage Neve modules and consoles — contact our team for current availability.</div>
        </div>
      </div>

    </div>
  </div>

  <!-- EXPLORE OTHER PAGES -->
  <div style="background:var(--off-white,#F7F5F2);padding:64px 48px;border-top:1px solid rgba(26,26,24,0.07)">
    <div style="max-width:1280px;margin:0 auto">
      <p style="font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:rgba(26,26,24,0.38);margin-bottom:10px">Explore Vintage King</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:26px;font-weight:700;color:#1A1A18;margin:0 0 32px">More From VK</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">
        <a href="hall-of-fame.html" style="background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;text-decoration:none;display:block">
          <div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:10px">Hall of Fame</div>
          <div style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:8px">Legendary Gear and Rooms</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.5);line-height:1.6">The consoles, microphones, and outboard that defined recording history — sourced and documented by VK.</div>
          <div style="margin-top:16px;font-size:12px;font-weight:700;color:#D4860A;letter-spacing:0.06em">Explore →</div>
        </a>
        <a href="audio-consultants.html" style="background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;text-decoration:none;display:block">
          <div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:10px">Expert Consulting</div>
          <div style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:8px">Talk to an Audio Consultant</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.5);line-height:1.6">Our team has tracked sessions on vintage Neve desks. Call, chat, or email — we know this gear from both sides of the glass.</div>
          <div style="margin-top:16px;font-size:12px;font-weight:700;color:#D4860A;letter-spacing:0.06em">Call 888.653.1184 →</div>
        </a>
        <a href="neve-1073.html" style="background:#fff;border:1px solid rgba(26,26,24,0.08);padding:28px;text-decoration:none;display:block">
          <div style="font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:10px">Gear Overview</div>
          <div style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:8px">Neve 1073 — All Formats</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.5);line-height:1.6">Compare every current version — Classic H, 500 Series SPX, OPX 8-channel rack — with specs and pricing side by side.</div>
          <div style="margin-top:16px;font-size:12px;font-weight:700;color:#D4860A;letter-spacing:0.06em">See All Formats →</div>
        </a>
      </div>
    </div>
  </div>

  <!-- CTA SECTION -->
  <section style="background:#EDE8E2;padding:72px 48px">
    <div style="max-width:680px;margin:0 auto;text-align:center">
      <p style="font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A;margin-bottom:14px">Talk to a Neve Expert</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin-bottom:16px">We've Serviced, Sold and Restored More Neve Than Anyone</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.6);margin-bottom:36px">Our consultants have run sessions on vintage 80 Series desks and know this gear from both sides of the glass. Call us or browse the full inventory.</p>
      <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
        <a href="audio-consultants.html" style="background:#1A1A18;color:#fff;padding:14px 32px;font-size:13px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">Call 888.653.1184</a>
        <a href="#" onclick="return false" style="background:#D4860A;color:#fff;padding:14px 32px;font-size:13px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">Shop Neve at VK</a>
      </div>
    </div>
  </section>

  <!-- STICKY SHOP BAR -->
  <div class="nv2-shopbar" id="nv2-shopbar">
    <div class="nv2-shopbar-text"><strong>AMS Neve 1073</strong> — Available now from Vintage King. Free shipping on orders over $49.</div>
    <div class="nv2-shopbar-actions">
      <a href="audio-consultants.html" class="nv2-shopbar-btn nv2-shopbar-secondary">Talk to an Expert</a>
      <a href="#" onclick="return false" class="nv2-shopbar-btn nv2-shopbar-primary">Shop Neve 1073</a>
      <button class="nv2-shopbar-close" onclick="document.getElementById('nv2-shopbar').style.display='none'">&times;</button>
    </div>
  </div>

  <div id="footer-neve-1073-guide-v2"></div>
</div>
"""

INLINE_JS = """\
<script>
  function nv2Faq(btn) {
    var a = btn.nextElementSibling;
    var isOpen = a.classList.contains('open');
    document.querySelectorAll('.nv2-faq-a.open').forEach(function(el){el.classList.remove('open');});
    document.querySelectorAll('.nv2-faq-q.open').forEach(function(el){el.classList.remove('open');});
    if (!isOpen) { a.classList.add('open'); btn.classList.add('open'); }
  }
  (function() {
    var p = 'neve-1073-guide-v2';
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
    head = re.sub(
        r"<title>.*?</title>",
        f"<title>{TITLE}</title>",
        head_css, count=1, flags=re.S
    )
    head += f'  <meta name="description" content="{META}">\n'
    head += '  <style id="vk-standalone-patch">.page{{display:block!important}}</style>\n'

    return (
        head + "\n</head>\n<body>\n"
        + CHROME + nav_tpl + foot_tpl
        + JSON_LD + PAGE_BODY
        + js_nav + INLINE_JS
        + "</body>\n</html>\n"
    )
