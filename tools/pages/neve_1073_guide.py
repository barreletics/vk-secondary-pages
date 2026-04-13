"""neve-1073-guide.html — Comprehensive buyer's guide: Neve 1073 Mic Preamp & EQ."""
import re

SLUG  = "neve-1073-guide"
TITLE = "Neve 1073 Buyer's Guide — The Definitive Resource | Vintage King"
META  = "The complete guide to the Neve 1073: official specs, Marinair transformer story, 8028/8078 console history, AIR Studios legacy, and every version available new and vintage at Vintage King."

# Image paths (relative to repo root — served alongside HTML)
IMG = {
    "hero_dark":    "images/neve-1073/1073-Classic-H-Main-Black-OP2-scaled-be23d5bf-9721-44e1-a372-3f5d16dd340e.png",
    "rack_front":   "images/neve-1073/1073_Rack_FrontHigh-72615813-842a-4121-a8d6-326d02b43c28.png",
    "rack_front2":  "images/neve-1073/1073_Rack_FrontHigh-a273ef28-c378-4c7e-9537-25d2cc835946.png",
    "h_left_lg":    "images/neve-1073/1073-Classic-H-3_4-Left-RT-2048x1198-4a5a8893-ea04-4326-b7b6-e2e5ab2bcb6e.png",
    "h_left_sm":    "images/neve-1073/1073-Classic-H-3_4-Left-RT-1024x599-e1349f25-77a4-4f28-bf3e-5933ccb4c526.png",
    "h_right":      "images/neve-1073/1073-Classic-H-3_4-Right-RT-1024x633-fad3dad8-4075-4ea1-bd34-c17291706280.png",
    "h_rear":       "images/neve-1073/1073-Classic-H-Rear-Raised-RT-1024x674-04ff66a7-26e2-4f34-8159-977a1535f5d7.png",
    "vertical_80s": "images/neve-1073/AMS-Neve-1073-80-series-Microphone-Preamp-EQ-vertical-069ce358-237f-4b27-8808-f5930ffd9dc3.png",
}

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "name": "AMS Neve 1073 Mic Preamp & Equaliser",
      "brand": {"@type": "Brand", "name": "AMS Neve"},
      "description": "Launched in 1970, the Neve 1073 is the first choice of leading producers and artists, delivering the unique Neve sound on some of the most famous recordings of the past six decades. Class A discrete, Marinair transformers, hand-built in the UK.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com", "telephone": "+18886531184"}
      }
    },
    {
      "@type": "Article",
      "headline": "Neve 1073 Buyer's Guide — The Definitive Resource",
      "description": "Official specs, Marinair transformer story, 8028/8078 console history, AIR Studios legacy, and every version available new and vintage.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What makes the Neve 1073 different from clones?",
          "acceptedAnswer": {"@type": "Answer", "text": "The original 1073 uses the exclusive Marinair specification input transformers (models 10468 and 31267) and the Rupert Neve-designed LO1166 output transformer — both manufactured under Neve's specification and unavailable to any clone manufacturer. Combined with the hand-wired Class A circuit following Rupert Neve's original pencil-on-paper designs, these components produce the specific harmonic character that defines the 1073 sound."}
        },
        {
          "@type": "Question",
          "name": "What is the EIN of the Neve 1073?",
          "acceptedAnswer": {"@type": "Answer", "text": "Better than -125dBu at 60dB gain, as specified by AMS Neve. The mic input gain ranges from +20dB to +80dB in 5dB steps."}
        },
        {
          "@type": "Question",
          "name": "What consoles was the Neve 1073 module used in?",
          "acceptedAnswer": {"@type": "Answer", "text": "The 1073 module was designed for the 1070 Wessex A88 console in 1970 and subsequently used in Neve 8028, 8048, 8056, 8068, 8078, and 8098 large-format consoles throughout the 1970s and 1980s."}
        }
      ]
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
  <span style="opacity:0.75">Buyer's Guide</span>
</nav>
"""

PAGE_BODY = f"""\
<div id="neve-1073-guide" class="page active">
  <div id="nav-neve-1073-guide"></div>

  <!-- ── HERO ── -->
  <section style="background:#EDE8E2;padding:80px 0 0;overflow:hidden">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 440px;gap:64px;align-items:end">
        <div style="padding-bottom:64px">
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Hall of Fame · Mic Preamp &amp; EQ</p>
          <h1 style="font-family:'Playfair Display',serif;font-size:68px;font-weight:800;color:#1A1A18;line-height:0.97;margin-bottom:16px;letter-spacing:-0.02em">Neve<br>1073</h1>
          <p class="speakable" style="font-family:'Playfair Display',serif;font-size:21px;font-style:italic;color:rgba(26,26,24,0.58);margin-bottom:24px;line-height:1.4">Launched in 1970. Still the first choice.</p>
          <p class="speakable" style="font-size:17px;color:rgba(26,26,24,0.68);max-width:480px;line-height:1.65;margin-bottom:36px">Class A discrete. Marinair transformers. Hand-built in the UK to Rupert Neve's original pencil-on-paper design. Copied hundreds of times. Never equaled.</p>
          <div style="display:flex;gap:12px;flex-wrap:wrap">
            <a href="#shop" style="display:inline-block;background:#D4860A;color:#fff;padding:13px 26px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Shop Neve 1073</a>
            <a href="#specs" style="display:inline-block;border:1.5px solid rgba(26,26,24,0.3);color:#1A1A18;padding:13px 26px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">View Specs</a>
          </div>
        </div>
        <!-- Hero image — dark dramatic shot, sits at bottom of hero -->
        <div style="align-self:end">
          <img src="{IMG['hero_dark']}" alt="AMS Neve 1073 Classic H — dramatic studio angle" style="width:100%;display:block;border-radius:2px 2px 0 0;box-shadow:0 -8px 40px rgba(26,26,24,0.12)">
        </div>
      </div>
    </div>
  </section>

  <!-- ── CREDENTIAL STRIP ── -->
  <section style="background:var(--warm-white,#FDFCFB);border-top:1px solid rgba(26,26,24,0.08);border-bottom:1px solid rgba(26,26,24,0.08);padding:20px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:flex;gap:0;flex-wrap:wrap">
      <div style="display:flex;align-items:center;gap:10px;padding:0 36px 0 0;border-right:1px solid rgba(26,26,24,0.09)">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">1970</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.52)">Original Year</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:0 36px;border-right:1px solid rgba(26,26,24,0.09)">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">Class A</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.52)">Discrete Circuit</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:0 36px;border-right:1px solid rgba(26,26,24,0.09)">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">Marinair</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.52)">Transformers</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:0 36px;border-right:1px solid rgba(26,26,24,0.09)">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">−125 dBu</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.52)">EIN @ 60dB</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:0 0 0 36px">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">UK</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.52)">Hand-Built</span>
      </div>
    </div>
  </section>

  <!-- ── FULL-BLEED RACK ── -->
  <section style="background:#1A1A18;padding:0;overflow:hidden">
    <img src="{IMG['rack_front']}" alt="AMS Neve 1073 8-channel rack — front view" style="width:100%;display:block;max-height:420px;object-fit:cover;object-position:center 30%">
  </section>

  <!-- ── WHAT MAKES IT ── -->
  <section style="background:#fff;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Why It Sounds the Way It Sounds</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#1A1A18;margin-bottom:48px;line-height:1.12">Four Things No Clone Can Copy</h2>

      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid rgba(26,26,24,0.08)">

        <div style="padding:32px 28px;border-right:1px solid rgba(26,26,24,0.08)">
          <div style="font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:16px">01</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:12px;line-height:1.2">Marinair Input Transformers</h3>
          <p style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.6">A collaboration between Neve Electronics and the Marinair Radar Company, late 1960s. The 10468 mic input and 31267 line input specifications are exclusive to Neve — manufactured in the UK for every 1073 built. This is where the harmonic saturation originates.</p>
        </div>

        <div style="padding:32px 28px;border-right:1px solid rgba(26,26,24,0.08)">
          <div style="font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:16px">02</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:12px;line-height:1.2">LO1166 Output Transformer</h3>
          <p style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.6">Designed by Rupert Neve in 1964 for his first transistorised console, built for Phillips Records. The design has been held under lock and key at Neve HQ for six decades. This output stage is unique to Neve — it cannot be licensed, purchased, or reproduced by any third party.</p>
        </div>

        <div style="padding:32px 28px;border-right:1px solid rgba(26,26,24,0.08)">
          <div style="font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:16px">03</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:12px;line-height:1.2">Class A Discrete Throughout</h3>
          <p style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.6">Not the most power-efficient topology — but entirely free from crossover distortion. The Class A design runs warm because it has to. That thermal activity is part of what produces the subtle, musical analog hue that distinguishes the 1073 from solid-state alternatives.</p>
        </div>

        <div style="padding:32px 28px">
          <div style="font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:16px">04</div>
          <h3 style="font-family:'Playfair Display',serif;font-size:19px;font-weight:700;color:#1A1A18;margin-bottom:12px;line-height:1.2">Hand-Built to Original Designs</h3>
          <p style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.6">Every unit built today follows Rupert Neve's original pencil-on-paper drawings. Point-to-point wiring. Fiberglass tracking. Original component specifications. Assembled by hand in the UK by Neve engineers — not a factory. This construction takes time and it is the reason no two 1073s sound exactly alike.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ── PREAMP SECTION + IMAGE ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center">
        <div>
          <img src="{IMG['h_left_lg']}" alt="AMS Neve 1073 Classic H — left 3/4 view showing gain knob and input selector" style="width:100%;display:block;border:1px solid rgba(26,26,24,0.07)">
        </div>
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Preamp Section</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin-bottom:20px;line-height:1.15">Up to 80 dB of Mic Gain. No Mic/Line Switch Needed.</h2>
          <p style="font-size:16px;color:rgba(26,26,24,0.68);line-height:1.65;margin-bottom:20px">The classic 5dB stepped Elma switch does double duty — it selects both gain level and input source (mic vs. line), eliminating the need for a separate switch. At the bottom of its range, it engages the line input. At the top, the two independent transistor-based preamplifiers work in combination to deliver up to 80dB of microphone gain.</p>
          <p style="font-size:16px;color:rgba(26,26,24,0.68);line-height:1.65;margin-bottom:28px">It's this gain staging that drives the harmonic character. Set the input gain high and trim the output to compensate — that's the move that every engineer learns on their first 1073 session.</p>
          <div style="border:1px solid rgba(26,26,24,0.09);background:#fff">
            <div style="display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid rgba(26,26,24,0.07)">
              <div style="padding:14px 16px;border-right:1px solid rgba(26,26,24,0.07)">
                <div style="font-size:11px;color:rgba(26,26,24,0.42);margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em">Mic Gain</div>
                <div style="font-size:14px;font-weight:600;color:#1A1A18">+20 to +80 dB, 5dB steps</div>
              </div>
              <div style="padding:14px 16px">
                <div style="font-size:11px;color:rgba(26,26,24,0.42);margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em">Line Gain</div>
                <div style="font-size:14px;font-weight:600;color:#1A1A18">−10 to +20 dB, 5dB steps</div>
              </div>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr">
              <div style="padding:14px 16px;border-right:1px solid rgba(26,26,24,0.07)">
                <div style="font-size:11px;color:rgba(26,26,24,0.42);margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em">EIN</div>
                <div style="font-size:14px;font-weight:600;color:#1A1A18">&lt; −125 dBu @ 60dB</div>
              </div>
              <div style="padding:14px 16px">
                <div style="font-size:11px;color:rgba(26,26,24,0.42);margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em">Line Impedance</div>
                <div style="font-size:14px;font-weight:600;color:#1A1A18">10 kΩ</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── EQ SECTION + IMAGE ── -->
  <section style="background:#fff;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center">
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">EQ Section</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin-bottom:20px;line-height:1.15">Handcrafted Inductors. Original 1070 Wessex Specification.</h2>
          <p style="font-size:16px;color:rgba(26,26,24,0.68);line-height:1.65;margin-bottom:20px">The 1073 EQ section uses inductor-based equalization — not op-amps or gyrators. These inductors are handcrafted to the original unpublished specification laid out in the 1073 module design for the Wessex A88 console, where the EQ had to perform across a wide range of signal sources.</p>
          <p style="font-size:16px;color:rgba(26,26,24,0.68);line-height:1.65;margin-bottom:28px">Inductor EQ produces an asymmetric curve — slightly tighter on the boost side, with a gentle extension on the cut side. This is why 1073 EQ moves rarely sound surgical. A 3dB boost at 12kHz adds air, not harshness. A 3dB cut at 220Hz thins the low-mid without sounding hollow.</p>

          <div style="display:flex;flex-direction:column;gap:0;border:1px solid rgba(26,26,24,0.09);background:#fff">
            <div style="padding:13px 16px;border-bottom:1px solid rgba(26,26,24,0.07);display:flex;justify-content:space-between;align-items:center">
              <span style="font-size:13px;font-weight:600;color:#1A1A18">High Shelf</span>
              <span style="font-size:13px;color:rgba(26,26,24,0.6)">±16 dB fixed at 12 kHz</span>
            </div>
            <div style="padding:13px 16px;border-bottom:1px solid rgba(26,26,24,0.07);display:flex;justify-content:space-between;align-items:center">
              <span style="font-size:13px;font-weight:600;color:#1A1A18">Low Shelf</span>
              <span style="font-size:13px;color:rgba(26,26,24,0.6)">±16 dB · 35 / 60 / 110 / 220 Hz</span>
            </div>
            <div style="padding:13px 16px;border-bottom:1px solid rgba(26,26,24,0.07);display:flex;justify-content:space-between;align-items:center">
              <span style="font-size:13px;font-weight:600;color:#1A1A18">Mid Peak</span>
              <span style="font-size:13px;color:rgba(26,26,24,0.6)">±18 dB · 360 / 700 / 1.6k / 3.2k / 4.8k / 7.2k Hz</span>
            </div>
            <div style="padding:13px 16px;display:flex;justify-content:space-between;align-items:center">
              <span style="font-size:13px;font-weight:600;color:#1A1A18">High-Pass Filter</span>
              <span style="font-size:13px;color:rgba(26,26,24,0.6)">18 dB/oct · 50 / 80 / 160 / 300 Hz</span>
            </div>
          </div>
        </div>
        <div>
          <img src="{IMG['h_right']}" alt="AMS Neve 1073 Classic H — right 3/4 view showing EQ section" style="width:100%;display:block;border:1px solid rgba(26,26,24,0.07)">
        </div>
      </div>
    </div>
  </section>

  <!-- ── ENGINEER QUOTE ── -->
  <section style="background:#2C2C2A;padding:64px 0">
    <div style="max-width:800px;margin:0 auto;padding:0 40px;text-align:center">
      <div style="font-size:48px;color:rgba(212,134,10,0.2);font-family:'Playfair Display',serif;line-height:1;margin-bottom:20px">&ldquo;</div>
      <blockquote style="font-family:'Playfair Display',serif;font-size:23px;font-style:italic;color:rgba(255,255,255,0.88);line-height:1.5;margin-bottom:24px">If there is one piece of outboard that I would never let leave my studio, it is the 1073. There is nothing else that sounds like it on a vocal — nothing.</blockquote>
      <cite style="font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A;font-style:normal;font-weight:600">Joe Chiccarelli &mdash; Producer, The White Stripes &middot; Beck &middot; Morrissey</cite>
    </div>
  </section>

  <!-- ── FULL SPECS TABLE ── id="specs" -->
  <section id="specs" style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start">
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Official Specifications</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin-bottom:32px">Complete Technical Spec</h2>

          <div style="margin-bottom:28px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.45);padding-bottom:8px;border-bottom:2px solid rgba(26,26,24,0.1);margin-bottom:12px">General</div>
            <table style="width:100%;border-collapse:collapse;font-size:14px">
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5);width:48%">Topology</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">Class A discrete</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Input transformers</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">Marinair spec (10468 mic / 31267 line)</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Output transformer</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">LO1166 (Rupert Neve, 1964)</td></tr>
              <tr><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Construction</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">Hand-built and hand-wired, UK</td></tr>
            </table>
          </div>

          <div style="margin-bottom:28px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.45);padding-bottom:8px;border-bottom:2px solid rgba(26,26,24,0.1);margin-bottom:12px">Preamp</div>
            <table style="width:100%;border-collapse:collapse;font-size:14px">
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5);width:48%">Mic gain</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">+20 to +80 dB, 5dB steps</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Line impedance</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">10 kΩ</td></tr>
              <tr><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Line gain</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">−10 to +20 dB, 5dB steps</td></tr>
            </table>
          </div>

          <div style="margin-bottom:28px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.45);padding-bottom:8px;border-bottom:2px solid rgba(26,26,24,0.1);margin-bottom:12px">EQ</div>
            <table style="width:100%;border-collapse:collapse;font-size:14px">
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5);width:48%">High shelf</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">±16 dB fixed at 12 kHz</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Low shelf</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">±16 dB, 35/60/110/220 Hz</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Mid peak</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">±18 dB, 0.36/0.7/1.6/3.2/4.8/7.2 kHz</td></tr>
              <tr><td style="padding:10px 0;color:rgba(26,26,24,0.5)">High-pass filter</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">18 dB/oct, 50/80/160/300 Hz</td></tr>
            </table>
          </div>

          <div>
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.45);padding-bottom:8px;border-bottom:2px solid rgba(26,26,24,0.1);margin-bottom:12px">Audio Performance</div>
            <table style="width:100%;border-collapse:collapse;font-size:14px">
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5);width:48%">Max output</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">&gt;+26 dBu into 600 Ω</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">THD</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">&lt;0.07% (50Hz–10kHz at +20dBu)</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Freq response</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">±0.5 dB, 20Hz–20kHz; −3dB at 40kHz</td></tr>
              <tr style="border-bottom:1px solid rgba(26,26,24,0.07)"><td style="padding:10px 0;color:rgba(26,26,24,0.5)">Noise</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">−83 dBu at all line gain settings</td></tr>
              <tr><td style="padding:10px 0;color:rgba(26,26,24,0.5)">EIN</td><td style="padding:10px 0;color:#1A1A18;font-weight:500">&lt;−125 dBu @ 60dB gain</td></tr>
            </table>
          </div>
        </div>

        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Physical</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#1A1A18;margin-bottom:20px">Dimensions &amp; Rack Options</h2>
          <p style="font-size:15px;color:rgba(26,26,24,0.62);line-height:1.65;margin-bottom:28px">The 1073 is available in vertical and horizontal orientations. Vertical modules install into an 80-series console channel strip or an 8-module 5U rack. Horizontal (Classic H) modules mount in a 3U stereo pair rack, two per unit.</p>

          <div style="border:1px solid rgba(26,26,24,0.09);background:#fff;margin-bottom:28px">
            <div style="padding:13px 16px;border-bottom:1px solid rgba(26,26,24,0.07);display:flex;justify-content:space-between">
              <span style="font-size:13px;color:rgba(26,26,24,0.5)">Width</span>
              <span style="font-size:13px;font-weight:600;color:#1A1A18">45 mm (1.8")</span>
            </div>
            <div style="padding:13px 16px;border-bottom:1px solid rgba(26,26,24,0.07);display:flex;justify-content:space-between">
              <span style="font-size:13px;color:rgba(26,26,24,0.5)">Height</span>
              <span style="font-size:13px;font-weight:600;color:#1A1A18">222 mm (8.75")</span>
            </div>
            <div style="padding:13px 16px;border-bottom:1px solid rgba(26,26,24,0.07);display:flex;justify-content:space-between">
              <span style="font-size:13px;color:rgba(26,26,24,0.5)">Depth</span>
              <span style="font-size:13px;font-weight:600;color:#1A1A18">254 mm (10")</span>
            </div>
            <div style="padding:13px 16px;display:flex;justify-content:space-between">
              <span style="font-size:13px;color:rgba(26,26,24,0.5)">Weight</span>
              <span style="font-size:13px;font-weight:600;color:#1A1A18">~2.5 kg (5.5 lbs)</span>
            </div>
          </div>

          <!-- Rear image -->
          <img src="{IMG['h_rear']}" alt="AMS Neve 1073 Classic H — rear panel showing PL31073-CH connector" style="width:100%;display:block;border:1px solid rgba(26,26,24,0.07)">
          <p style="font-size:11px;color:rgba(26,26,24,0.38);margin-top:8px;line-height:1.5">Rear panel showing the proprietary PL31073-CH connector, serial number plate (hand-stamped with test date and initials), and Hi/Lo impedance switch (1.2kΩ / 300Ω).</p>

          <div style="margin-top:24px;padding:20px;border:1px solid rgba(26,26,24,0.09);background:#fff">
            <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:8px">Impedance Matching</div>
            <p style="font-size:13px;color:rgba(26,26,24,0.62);line-height:1.55">The rear-mounted Hi/Lo switch selects between 1.2kΩ and 300Ω input impedance — optimized for modern and vintage microphones respectively. Lower impedance with ribbon mics affects the mic's low-frequency response and perceived character.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── STUDIO LEGACY ── -->
  <section style="background:#1A1A18;padding:80px 0 64px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Console History</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#fff;margin-bottom:12px">The Consoles That Carried the 1073</h2>
      <p style="font-size:16px;color:rgba(255,255,255,0.5);max-width:580px;margin-bottom:48px;line-height:1.6">The 1073 module appeared in every major Neve large-format console from 1970 onward. The studios that installed them defined the sound of recorded music for a decade.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1px;background:rgba(255,255,255,0.06)">

        <div style="background:#1A1A18;padding:28px 24px">
          <div style="font-size:11px;color:rgba(212,134,10,0.7);font-weight:600;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">1970 · Wessex Sound Studios</div>
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:8px">Neve A88 — First Installation</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.48);line-height:1.55">The 1073 was designed specifically for the Wessex A88 console. This was the module's commercial debut — and the beginning of its studio legacy.</p>
        </div>

        <div style="background:#1A1A18;padding:28px 24px">
          <div style="font-size:11px;color:rgba(212,134,10,0.7);font-weight:600;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">1971–1975 · Olympic Studios, London</div>
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:8px">Neve 8028</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.48);line-height:1.55">Led Zeppelin tracked IV in Olympic's Room 1 — and at Headley Grange using the Neve mobile truck. The Rolling Stones used the Olympic 8028 extensively through this period.</p>
        </div>

        <div style="background:#1A1A18;padding:28px 24px">
          <div style="font-size:11px;color:rgba(212,134,10,0.7);font-weight:600;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">1972–1980 · Various Studios</div>
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:8px">Neve 8078</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.48);line-height:1.55">The large-format console at the heart of the warmest-sounding rock recordings ever made. Headley Grange. Stargroves. Thick, musical, irreplaceable. VK has serviced several of these consoles.</p>
        </div>

        <div style="background:#1A1A18;padding:28px 24px">
          <div style="font-size:11px;color:rgba(212,134,10,0.7);font-weight:600;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">1972–Present · AIR Studios, London</div>
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:8px">Neve 8068</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.48);line-height:1.55">George Martin's AIR Studios in Oxford Street, and later Lyndhurst Hall, ran Neve 8068 consoles. The 1073-derived mic channels contributed to the smooth, open character that defined AIR's output through the 1970s and 80s.</p>
        </div>

        <div style="background:#1A1A18;padding:28px 24px">
          <div style="font-size:11px;color:rgba(212,134,10,0.7);font-weight:600;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">1972–Present · Electric Lady, New York</div>
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:8px">Neve 8078</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.48);line-height:1.55">Jimi Hendrix built Electric Lady with a Neve 8078 as the centerpiece. VK completed a full premium restoration of Electric Lady's 8078 — one of the most significant console restorations in VK's history.</p>
        </div>

        <div style="background:#1A1A18;padding:28px 24px">
          <div style="font-size:11px;color:rgba(212,134,10,0.7);font-weight:600;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">1969–1983 · Olympic Studios, London</div>
          <div style="font-family:'Playfair Display',serif;font-size:18px;font-weight:700;color:#fff;margin-bottom:8px">The Helios Connection</div>
          <p style="font-size:13px;color:rgba(255,255,255,0.48);line-height:1.55">Olympic also installed one of the rarest British consoles: the Helios, commissioned in 1969. VK sources original Helios components. The Neve and Helios lineage represent the twin peaks of 1970s British studio design.</p>
        </div>

      </div>
    </div>
  </section>

  <!-- ── ENGINEER RIGS ── -->
  <section style="background:#fff;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Engineer Signal Chains</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#1A1A18;margin-bottom:48px;line-height:1.12">The 1073 in the Wild</h2>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">

        <div style="background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.07);border-top:3px solid #D4860A;padding:32px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1A1A18;margin-bottom:4px">Al Schmitt</div>
          <div style="font-size:12px;color:#D4860A;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:16px">23 Grammy Awards</div>
          <p style="font-size:13px;color:rgba(26,26,24,0.58);line-height:1.65;margin-bottom:20px">Frank Sinatra. Diana Krall. Paul McCartney. Bob Dylan. Al built his sound around a handful of pieces he reached for on every session.</p>
          <div style="border-top:1px solid rgba(26,26,24,0.08);padding-top:16px;display:flex;flex-direction:column;gap:8px">
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Neumann U 47 — main vocal</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18;font-weight:600">Neve 1073 — mic preamp</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Fairchild 670 — bus compression</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Pultec EQP-1A — low-end shaping</span></div>
          </div>
        </div>

        <div style="background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.07);border-top:3px solid #D4860A;padding:32px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1A1A18;margin-bottom:4px">Glyn Johns</div>
          <div style="font-size:12px;color:#D4860A;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:16px">The Rolling Stones &middot; The Who &middot; Eagles</div>
          <p style="font-size:13px;color:rgba(26,26,24,0.58);line-height:1.65;margin-bottom:20px">The Glyn Johns drum miking method is still taught in recording schools worldwide. His signal chain was deliberate and short — and centered on the 8078.</p>
          <div style="border-top:1px solid rgba(26,26,24,0.08);padding-top:16px;display:flex;flex-direction:column;gap:8px">
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18;font-weight:600">Neve 8078 — tracking console</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Telefunken V72 — preamp</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Coles 4038 — room / overheads</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Pultec EQP-1A — mix EQ</span></div>
          </div>
        </div>

        <div style="background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.07);border-top:3px solid #D4860A;padding:32px">
          <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:700;color:#1A1A18;margin-bottom:4px">Joe Chiccarelli</div>
          <div style="font-size:12px;color:#D4860A;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:16px">White Stripes &middot; Beck &middot; Morrissey</div>
          <p style="font-size:13px;color:rgba(26,26,24,0.58);line-height:1.65;margin-bottom:20px">One of the most versatile producers in modern recording. The 1073 appears on his credit list as far back as his sessions go — never replaced, never questioned.</p>
          <div style="border-top:1px solid rgba(26,26,24,0.08);padding-top:16px;display:flex;flex-direction:column;gap:8px">
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18;font-weight:600">Neve 1073 — every vocal, every session</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">UREI 1176LN — drums and guitars</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">Teletronix LA-2A — bass and vocals</span></div>
            <div style="display:flex;align-items:center;gap:8px"><div style="width:5px;height:5px;background:#D4860A;border-radius:50%;flex-shrink:0"></div><span style="font-size:13px;color:#1A1A18">API 550A — guitars and drums EQ</span></div>
          </div>
        </div>

      </div>

      <!-- Second quote -->
      <div style="margin-top:48px;border-left:4px solid #D4860A;padding:24px 32px;background:rgba(212,134,10,0.04)">
        <p style="font-family:'Playfair Display',serif;font-size:20px;font-style:italic;color:#1A1A18;line-height:1.5;margin-bottom:10px">"When I walked into a room with a Neve 8078, I knew the session would sound good before I touched a single fader. The console did half the work."</p>
        <cite style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.45);font-style:normal">Bob Ludwig &mdash; Mastering Engineer, Rolling Stones &middot; Nirvana &middot; U2</cite>
      </div>
    </div>
  </section>

  <!-- ── VERSIONS ── id="shop" -->
  <section id="shop" style="background:#EDE8E2;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Which 1073 Is Right for You?</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#1A1A18;margin-bottom:12px">Shop Neve 1073 at Vintage King</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.62);max-width:580px;margin-bottom:48px;line-height:1.6">New current production, certified used, and original vintage modules when available. All tested by VK's gear team. Trade-in credit available on any purchase.</p>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:36px">

        <!-- Vertical 80-series module -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="background:#1A1A18;padding:32px;display:flex;align-items:center;justify-content:center;min-height:280px">
            <img src="{IMG['vertical_80s']}" alt="AMS Neve 1073 80-series vertical module" style="max-height:240px;width:auto;display:block;margin:0 auto">
          </div>
          <div style="padding:24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Current Production</div>
            <h3 style="font-size:17px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">1073 Vertical Module</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:16px">Classic 80-series format. Retrofits directly into original Neve consoles. Can be installed in the 5U 8-module rack. The format Rupert Neve designed first.</p>
            <a href="#" onclick="return false" style="display:block;text-align:center;background:#D4860A;color:#fff;padding:11px;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">View &amp; Buy</a>
          </div>
        </div>

        <!-- Classic H horizontal -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="background:#F0EDE8;padding:24px;display:flex;align-items:center;justify-content:center;min-height:280px">
            <img src="{IMG['h_left_sm']}" alt="AMS Neve 1073 Classic H horizontal module" style="width:100%;display:block">
          </div>
          <div style="padding:24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Current Production</div>
            <h3 style="font-size:17px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">1073 Classic H</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:16px">Horizontal format — two units fit in the 3U stereo pair rack. Popular for home and project studios that need the 1073 character without a console. Same circuit, different orientation.</p>
            <a href="#" onclick="return false" style="display:block;text-align:center;background:#D4860A;color:#fff;padding:11px;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">View &amp; Buy</a>
          </div>
        </div>

        <!-- 8-channel OPX rack -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="background:#1A1A18;padding:16px 0;display:flex;align-items:center;justify-content:center;min-height:280px;overflow:hidden">
            <img src="{IMG['rack_front2']}" alt="AMS Neve 1073 8-channel OPX rack — front view" style="width:100%;display:block">
          </div>
          <div style="padding:24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Current Production</div>
            <h3 style="font-size:17px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">1073OPX — 8 Channels</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:16px">Eight 1073 channels in 3U. The professional studio workhorse. Individual phantom, pad, and polarity per channel. From $6,499 — the most cost-effective way to run full 1073 tracking sessions.</p>
            <a href="#" onclick="return false" style="display:block;text-align:center;background:#D4860A;color:#fff;padding:11px;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">View &amp; Buy</a>
          </div>
        </div>

      </div>

      <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;padding-top:8px">
        <a href="#" onclick="return false" style="display:inline-block;background:#D4860A;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Browse All Neve at VK</a>
        <a href="audio-consultants.html" style="display:inline-block;border:1.5px solid rgba(26,26,24,0.3);color:#1A1A18;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Talk to a Consultant</a>
        <span style="font-size:13px;color:rgba(26,26,24,0.45)">Trade-in credit available · Vintage modules by inquiry · 888.653.1184</span>
      </div>
    </div>
  </section>

  <!-- ── VALUES BAR ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:48px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Vintage Specialist</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">VK has moved more original Neve modules than any other dealer in North America.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Trade-In Credit</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Written offer within 24 hours. Same-day trade credit toward any 1073 or other gear.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Gear Expert Consultation</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Not sure which 1073 version fits your setup? Call us — we'll give you a straight answer.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">VK Warranty</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">All current-production units backed by full VK Warranty. Certified used units inspected.</div>
        </div>
      </div>
    </div>
  </section>

  <div id="footer-neve-1073-guide"></div>
</div>
"""

INLINE_JS = """\
<script>
  (function() {
    var p = 'neve-1073-guide';
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
