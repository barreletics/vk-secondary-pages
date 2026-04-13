"""neve-1073.html — VK Hall of Fame: Neve 1073 deep article page."""
import re

SLUG  = "neve-1073"
TITLE = "Neve 1073 — The Preamp That Defined Modern Recording | Vintage King"
META  = "The definitive guide to the Neve 1073 mic preamp and EQ. History, versions, circuit topology, and why this 1970s module still commands every major studio — new and vintage at Vintage King."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "name": "Neve 1073",
      "brand": {"@type": "Brand", "name": "AMS Neve"},
      "description": "The Neve 1073 is a Class A transformer-balanced mic preamp and three-band EQ module first introduced in 1970. Widely regarded as the gold standard of analog recording.",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
      }
    },
    {
      "@type": "Article",
      "headline": "Neve 1073 — The Preamp That Defined Modern Recording",
      "description": "History, circuit design, versions, and studio legacy of the Neve 1073 mic preamp and EQ.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
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
  <span style="opacity:0.75">Neve 1073</span>
</nav>
"""

PAGE_BODY = """\
<div id="neve-1073" class="page active">
  <div id="nav-neve-1073"></div>

  <!-- ── HERO ── -->
  <section style="background:#EDE8E2;padding:80px 0 64px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Hall of Fame — Mic Preamp &amp; EQ</p>
      <h1 style="font-family:'Playfair Display',serif;font-size:64px;font-weight:800;color:#1A1A18;line-height:1.0;margin-bottom:8px;letter-spacing:-0.01em">Neve 1073</h1>
      <p class="speakable" style="font-family:'Playfair Display',serif;font-size:22px;font-style:italic;color:rgba(26,26,24,0.6);margin-bottom:28px;line-height:1.4">The Preamp That Defined Modern Recording</p>
      <p class="speakable" style="font-size:17px;color:rgba(26,26,24,0.65);max-width:600px;line-height:1.65;margin-bottom:36px">Introduced in 1970. Found on records by Led Zeppelin, David Bowie, The Rolling Stones, and virtually every major album of the 1970s and beyond. Copied hundreds of times. Never surpassed.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="#shop" style="display:inline-block;background:#D4860A;color:#fff;padding:13px 26px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Shop Neve 1073</a>
        <a href="hall-of-fame.html" style="display:inline-block;border:1.5px solid rgba(26,26,24,0.3);color:#1A1A18;padding:13px 26px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Hall of Fame ↑</a>
      </div>
    </div>
  </section>

  <!-- ── CREDENTIAL STRIP ── -->
  <section style="background:var(--warm-white,#FDFCFB);border-top:1px solid rgba(26,26,24,0.08);border-bottom:1px solid rgba(26,26,24,0.08);padding:18px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:flex;gap:36px;flex-wrap:wrap;align-items:center">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">1970</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Original Year</span>
      </div>
      <div style="width:1px;height:24px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">Class A</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Topology</span>
      </div>
      <div style="width:1px;height:24px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">Marinair</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Transformers</span>
      </div>
      <div style="width:1px;height:24px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">3-Band</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Stepped EQ</span>
      </div>
      <div style="width:1px;height:24px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:20px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">VK HOF</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Inductee</span>
      </div>
    </div>
  </section>

  <!-- ── HERO GEAR IMAGE ── -->
  <section style="background:#fff;padding:64px 0 48px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="min-height:520px;background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center;position:relative">
        <div style="text-align:center">
          <p style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">[Neve 1073 Product Photo — High Resolution]</p>
          <p style="font-size:12px;color:rgba(26,26,24,0.22)">Full rack unit or module — dark background preferred</p>
        </div>
        <div style="position:absolute;bottom:20px;right:24px;font-size:11px;color:rgba(26,26,24,0.3);font-style:italic">AMS Neve 1073 / 1073N</div>
      </div>
    </div>
  </section>

  <!-- ── EDITORIAL ── -->
  <section style="background:#fff;padding:0 0 80px">
    <div style="max-width:760px;margin:0 auto;padding:0 40px">
      <h2 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;margin-bottom:20px;line-height:1.2">Where It Came From</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.72);line-height:1.7;margin-bottom:20px">In 1968, Rupert Neve was commissioned to design the 8014 console for London's Wessex Sound Studios. The preamp module at its heart — which would evolve into the 1073 — was unlike anything else available at the time. Where competitors offered clean, colorless amplification, Neve built in a specific harmonic character rooted in the behavior of his custom transformers and discrete Class A circuitry.</p>
      <p style="font-size:16px;color:rgba(26,26,24,0.72);line-height:1.7;margin-bottom:20px">The 1073 designation appeared formally in 1970 as part of the A88 console. Studios across the UK began installing them immediately. Trident, AIR, Olympic, Metropolis — the major London studios of the early 1970s were all running Neve. The records that came out of those rooms defined the sonic character of a decade.</p>
      <p style="font-size:16px;color:rgba(26,26,24,0.72);line-height:1.7;margin-bottom:36px">What made the 1073 so widely copied, and so rarely equaled, was the interaction between three elements: the input transformer (originally a Marinair, later St. Ives), the Class A discrete amplifier stage, and the inductor-based EQ section. Each contributes to a specific "weight" in the low end, a presence in the upper midrange, and an air at the top that engineers still chase today.</p>

      <h2 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;margin-bottom:20px;line-height:1.2">The Sound, Technically Speaking</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.72);line-height:1.7;margin-bottom:20px">The 1073's character comes largely from harmonic distortion that is pleasant and musical rather than harsh. At moderate gain settings, the unit introduces second-order harmonics that add body and density to signals without sounding "saturated" in the modern plugin sense. Push the input gain further and the color increases — this is why engineers often ride the input trim to taste.</p>
      <p style="font-size:16px;color:rgba(26,26,24,0.72);line-height:1.7;margin-bottom:36px">The EQ section offers three bands: a high-pass filter (50/80/160Hz), a fixed high shelf (at 10kHz), and a peaking mid with switchable frequencies at 360Hz, 700Hz, 1.6kHz, 3.2kHz, 4.8kHz, 8kHz, and 12kHz. The inductor-based topology gives each boost a slightly asymmetric curve — tighter on the low side, with a gentle extension on the high side — which is why 1073 EQ moves rarely sound surgical or brittle.</p>

      <blockquote style="border-left:3px solid #D4860A;padding:20px 24px;margin:0 0 36px;background:rgba(212,134,10,0.04)">
        <p style="font-family:'Playfair Display',serif;font-size:19px;font-style:italic;color:#1A1A18;line-height:1.5;margin-bottom:10px">"I've never heard a vocal that didn't benefit from a 1073. The transformer input alone adds something you can't replicate."</p>
        <cite style="font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(26,26,24,0.45);font-style:normal">Working Mix Engineer — VK Client</cite>
      </blockquote>
    </div>
  </section>

  <!-- ── VERSIONS GRID ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Versions &amp; Variants</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin-bottom:12px">Which 1073 Is Right for You?</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.6);max-width:560px;margin-bottom:48px;line-height:1.6">From original vintage modules to current AMS Neve production units — every version has a specific character and use case.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px">

        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:320px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Vintage Module Photo]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Original Vintage</div>
            <h3 style="font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">1970s Neve 1073 Module</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:14px">Original production modules from Neve consoles of the 1970s. Marinair or St. Ives transformers. The benchmark. Prices vary widely by condition and console provenance.</p>
            <div style="font-size:13px;font-weight:600;color:#1A1A18">Vintage market · Inquire for pricing</div>
          </div>
        </div>

        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:320px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[1073N Photo]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#C0392B;margin-bottom:6px">Current Production</div>
            <h3 style="font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">AMS Neve 1073N</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:14px">500-series version of the original 1073 circuit. Neve-wound transformers. Closest current-production equivalent to the vintage module. Stacks in any standard 500 rack.</p>
            <div style="font-size:13px;font-weight:600;color:#1A1A18">From $799 · In Stock</div>
          </div>
        </div>

        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:320px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[1073OPX Photo]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#C0392B;margin-bottom:6px">Current Production</div>
            <h3 style="font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">AMS Neve 1073OPX</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:14px">8-channel rackmount version. Same 1073 circuit in every channel, with individual phantom, pad, and polarity controls per strip. The professional studio workhorse.</p>
            <div style="font-size:13px;font-weight:600;color:#1A1A18">From $6,499 · In Stock</div>
          </div>
        </div>

        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:320px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Demo / Used Photo]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;margin-bottom:6px">Demo &amp; Used</div>
            <h3 style="font-size:18px;font-weight:700;color:#1A1A18;margin-bottom:8px;font-family:'Playfair Display',serif">Neve 1073 — Certified Used</h3>
            <p style="font-size:13px;color:rgba(26,26,24,0.6);line-height:1.55;margin-bottom:14px">Inspected and tested by VK's tech team. Significant savings on current-production units. Always a smart option for the 1073 — it's a robust piece of hardware.</p>
            <div style="font-size:13px;font-weight:600;color:#1A1A18">Availability varies · Check stock</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ── STUDIO TIMELINE ── -->
  <section style="background:#fff;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Studio Legacy</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin-bottom:48px">Records Made on the 1073</h2>

      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px">

        <div style="border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:360px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Studio Photo]</span>
          </div>
          <div style="padding:20px">
            <div style="font-size:11px;color:rgba(26,26,24,0.4);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px">1971 — Olympic Studios, London</div>
            <div style="font-size:15px;font-weight:700;color:#1A1A18;margin-bottom:6px;font-family:'Playfair Display',serif">Led Zeppelin, IV</div>
            <div style="font-size:13px;color:rgba(26,26,24,0.58);line-height:1.5">Tracked through a Neve 8036 console. The drum sound on "When the Levee Breaks" — recorded in the stairwell at Headley Grange — has become one of the most sampled and studied recordings in rock history.</div>
          </div>
        </div>

        <div style="border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:360px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Studio Photo]</span>
          </div>
          <div style="padding:20px">
            <div style="font-size:11px;color:rgba(26,26,24,0.4);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px">1972 — Trident Studios, London</div>
            <div style="font-size:15px;font-weight:700;color:#1A1A18;margin-bottom:6px;font-family:'Playfair Display',serif">David Bowie, Ziggy Stardust</div>
            <div style="font-size:13px;color:rgba(26,26,24,0.58);line-height:1.5">Recorded and mixed on the Trident A-range console, a direct descendant of Neve's design philosophy. Bowie's vocal on "Starman" remains one of the most studied examples of Neve preamp character on voice.</div>
          </div>
        </div>

        <div style="border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:360px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Studio Photo]</span>
          </div>
          <div style="padding:20px">
            <div style="font-size:11px;color:rgba(26,26,24,0.4);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px">1971 — Island Studios, London</div>
            <div style="font-size:15px;font-weight:700;color:#1A1A18;margin-bottom:6px;font-family:'Playfair Display',serif">Traffic, The Low Spark of High-Heeled Boys</div>
            <div style="font-size:13px;color:rgba(26,26,24,0.58);line-height:1.5">Island's Room 1 was equipped with a Neve 8028 console. Engineers of the period cite Island's 1073 channels as having a particularly warm character attributed to their specific transformer spec.</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ── SPECS TABLE ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start">
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Specifications</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;margin-bottom:28px">Neve 1073 — Key Specs</h2>
          <table style="width:100%;border-collapse:collapse;font-size:14px">
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5);width:45%">Topology</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">Class A discrete</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">Input transformer</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">Marinair / St. Ives (vintage); Neve-wound (current)</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">Gain range</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">+20 to +80 dB (mic) / 0 to +20 dB (line)</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">EQ high shelf</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">10 kHz, ±16 dB</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">EQ mid frequencies</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">360 / 700 / 1.6k / 3.2k / 4.8k / 8k / 12k Hz</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">EQ mid range</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">±18 dB</td>
            </tr>
            <tr style="border-bottom:1px solid rgba(26,26,24,0.08)">
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">High-pass filter</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">50 / 80 / 160 Hz, 18 dB/oct</td>
            </tr>
            <tr>
              <td style="padding:12px 0;color:rgba(26,26,24,0.5)">Phantom power</td>
              <td style="padding:12px 0;color:#1A1A18;font-weight:500">+48V switchable</td>
            </tr>
          </table>
        </div>
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">What to Know</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:32px;font-weight:700;color:#1A1A18;margin-bottom:20px">Before You Buy</h2>
          <div style="display:flex;flex-direction:column;gap:16px">
            <div style="padding:20px;border:1px solid rgba(26,26,24,0.07);background:#fff">
              <div style="font-size:14px;font-weight:700;color:#1A1A18;margin-bottom:6px">Vintage vs. current production</div>
              <div style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.55">Original modules have the Marinair or St. Ives transformer, which many engineers prefer. Current AMS Neve units use Neve-wound transformers and sound excellent — different, not lesser. Call us and we'll walk you through the difference on your application.</div>
            </div>
            <div style="padding:20px;border:1px solid rgba(26,26,24,0.07);background:#fff">
              <div style="font-size:14px;font-weight:700;color:#1A1A18;margin-bottom:6px">500-series vs. full rack</div>
              <div style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.55">The 1073N (500-series) is the most accessible entry point. The 1073OPX gives you eight identical channels in 3U. For a single-purpose desktop unit, the 1073SPX is worth investigating.</div>
            </div>
            <div style="padding:20px;border:1px solid rgba(26,26,24,0.07);background:#fff">
              <div style="font-size:14px;font-weight:700;color:#1A1A18;margin-bottom:6px">The clones question</div>
              <div style="font-size:14px;color:rgba(26,26,24,0.62);line-height:1.55">There are dozens of 1073-style clones at every price point. Some are excellent for the money. None are identical to a Neve-wound unit. If you want the original character, VK's position is clear: buy Neve or buy vintage.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── SHOP CTA ── id="shop" -->
  <section id="shop" style="background:#EDE8E2;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#D4860A;margin-bottom:12px">Shop Neve 1073</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin-bottom:12px">New, Demo &amp; Vintage — In Stock at VK</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.65);max-width:540px;margin-bottom:40px;line-height:1.6">Current AMS Neve production units, certified used, and original vintage modules when available. Every unit tested by VK's gear team. Trade-in pricing available.</p>

      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:36px">
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:300px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Product Image]</span>
          </div>
          <div style="padding:20px">
            <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:4px">AMS Neve 1073N</div>
            <div style="font-size:13px;font-weight:500;color:#1A1A18;margin-bottom:10px;font-family:'DM Sans',sans-serif">From $799</div>
            <a href="#" onclick="return false" style="display:block;text-align:center;background:#D4860A;color:#fff;padding:11px;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">View &amp; Buy</a>
          </div>
        </div>
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:300px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Product Image]</span>
          </div>
          <div style="padding:20px">
            <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:4px">AMS Neve 1073OPX</div>
            <div style="font-size:13px;font-weight:500;color:#1A1A18;margin-bottom:10px;font-family:'DM Sans',sans-serif">From $6,499</div>
            <a href="#" onclick="return false" style="display:block;text-align:center;background:#D4860A;color:#fff;padding:11px;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">View &amp; Buy</a>
          </div>
        </div>
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:300px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Vintage Module Image]</span>
          </div>
          <div style="padding:20px">
            <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:4px">Vintage 1073 Modules</div>
            <div style="font-size:13px;font-weight:500;color:#1A1A18;margin-bottom:10px;font-family:'DM Sans',sans-serif">Inquire for Pricing</div>
            <a href="tel:8886531184" style="display:block;text-align:center;background:#1A1A18;color:#fff;padding:11px;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px">Call to Inquire</a>
          </div>
        </div>
      </div>

      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="#" onclick="return false" style="display:inline-block;background:#D4860A;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Browse All Neve at VK</a>
        <a href="audio-consultants.html" style="display:inline-block;border:1.5px solid rgba(26,26,24,0.3);color:#1A1A18;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Talk to a Consultant</a>
      </div>
    </div>
  </section>

  <!-- ── VALUES BAR ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:48px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Vintage Specialist</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">We've sold more original Neve modules than any dealer in North America.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Gear Expert Consultation</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Not sure which 1073 version is right for your setup? Call us — we'll give you a straight answer.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Trade-In Credit</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Trade your current gear toward a 1073. Written offer within 24 hours, same-day credit.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">VK Warranty</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">All current-production units backed by full VK Warranty. Used units inspected and certified.</div>
        </div>
      </div>
    </div>
  </section>

  <div id="footer-neve-1073"></div>
</div>
"""

INLINE_JS = """\
<script>
  (function() {
    var p = 'neve-1073';
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
    head += '  <style id="vk-standalone-patch">.page{display:block!important}</style>\n'

    return (
        head + "\n</head>\n<body>\n"
        + CHROME + nav_tpl + foot_tpl
        + JSON_LD + PAGE_BODY
        + js_nav + INLINE_JS
        + "</body>\n</html>\n"
    )
