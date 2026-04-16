"""neve-1073-guide.html — Comprehensive guide: Neve 1073 history, legacy, specs. Article + sidebar layout."""
import re

SLUG  = "neve-1073-guide"
TITLE = "The Neve 1073: History, Legacy & Sound — Vintage King Audio"
META  = "The definitive guide to the Neve 1073 — the preamp and EQ module that defined modern recording. Rupert Neve's 1970 design, 80 Series consoles, AIR Studios, Electric Lady, and every version available at Vintage King."

IMG = {
    "vertical_80s": "images/neve-1073/AMS-Neve-1073-80-series-Microphone-Preamp-EQ-vertical-069ce358-237f-4b27-8808-f5930ffd9dc3.png",
    "rack_front":   "images/neve-1073/1073_Rack_FrontHigh-72615813-842a-4121-a8d6-326d02b43c28.png",
    "h_left_lg":    "images/neve-1073/1073-Classic-H-3_4-Left-RT-2048x1198-4a5a8893-ea04-4326-b7b6-e2e5ab2bcb6e.png",
    "h_left_sm":    "images/neve-1073/1073-Classic-H-3_4-Left-RT-1024x599-e1349f25-77a4-4f28-bf3e-5933ccb4c526.png",
    "h_right":      "images/neve-1073/1073-Classic-H-3_4-Right-RT-1024x633-fad3dad8-4075-4ea1-bd34-c17291706280.png",
    "h_rear":       "images/neve-1073/1073-Classic-H-Rear-Raised-RT-1024x674-04ff66a7-26e2-4f34-8159-977a1535f5d7.png",
    "hero_dark":    "images/neve-1073/1073-Classic-H-Main-Black-OP2-scaled-be23d5bf-9721-44e1-a372-3f5d16dd340e.png",
    "rack_front2":  "images/neve-1073/1073_Rack_FrontHigh-a273ef28-c378-4c7e-9537-25d2cc835946.png",
}

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "The Neve 1073: History, Legacy & Sound",
      "description": "The definitive guide to the Neve 1073 — Rupert Neve's 1970 preamp and EQ module that powered the 80 Series consoles at AIR Studios, Electric Lady, and the most important rooms in recording history.",
      "author": {"@type": "Organization", "name": "Vintage King Audio"},
      "publisher": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}
    },
    {
      "@type": "Product",
      "name": "AMS Neve 1073 Mic Preamp & Equaliser",
      "brand": {"@type": "Brand", "name": "AMS Neve"},
      "description": "Class A discrete mic preamp and EQ module. Marinair transformers, hand-built in the UK since 1970.",
      "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com"}}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type":"Question","name":"What is the Neve 1073?","acceptedAnswer":{"@type":"Answer","text":"The Neve 1073 is a microphone preamplifier and three-band equalizer module designed by Rupert Neve around 1970. Class A discrete transistor circuitry, Marinair transformers, hand-built in the UK. Widely regarded as the most influential piece of studio hardware ever made."}},
        {"@type":"Question","name":"What consoles used the Neve 1073?","acceptedAnswer":{"@type":"Answer","text":"The 1073 was used in early Neve 80 Series consoles (8014, 8034). Closely related modules with the same Marinair transformer spec were used in the 8028, 8058, 8068, and 8078. All share the same fundamental sonic character."}},
        {"@type":"Question","name":"How is the Neve 1073 different from clones?","acceptedAnswer":{"@type":"Answer","text":"The original 1073 uses exclusive Marinair specification transformers (models 10468 and 31267) and Rupert Neve's LO1166 output transformer — designs held under lock and key at Neve HQ. Combined with the hand-wired Class A circuit from Rupert Neve's original pencil-on-paper drawings, these cannot be licensed or duplicated by any third party."}},
        {"@type":"Question","name":"What is the Neve 1073 EIN?","acceptedAnswer":{"@type":"Answer","text":"Better than -125dBu at 60dB gain, as specified by AMS Neve. Mic gain ranges from +20dB to +80dB in 5dB steps."}}
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
  <span style="opacity:0.75">Gear Guide</span>
</nav>
"""

PAGE_BODY = f"""\
<div id="neve-1073-guide" class="page active">
  <div id="nav-neve-1073-guide"></div>

  <style>
    /* Guide-scoped styles */
    .ng-breadcrumb {{ max-width:1280px;margin:0 auto;padding:14px 48px;font-size:13px;color:rgba(26,26,24,0.45);font-family:'DM Sans',sans-serif }}
    .ng-breadcrumb a {{ color:rgba(26,26,24,0.45);text-decoration:none }}
    .ng-breadcrumb a:hover {{ color:#D4860A }}
    .ng-breadcrumb span {{ margin:0 8px }}

    /* Article + Sidebar layout */
    .ng-outer {{ max-width:1280px;margin:0 auto;padding:64px 48px 96px;display:grid;grid-template-columns:1fr 300px;gap:72px;align-items:start }}
    .ng-article h2 {{ font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#1A1A18;margin:52px 0 16px;line-height:1.2 }}
    .ng-article h2:first-child {{ margin-top:0 }}
    .ng-article p {{ font-size:16px;color:#3A3A38;line-height:1.8;margin-bottom:18px }}
    .ng-article strong {{ color:#1A1A18;font-weight:600 }}
    .ng-article ul {{ margin:14px 0 18px 22px;font-size:16px;color:#3A3A38;line-height:1.85 }}

    /* Pull quote */
    .ng-pullquote {{ border-left:3px solid #D4860A;padding:18px 26px;margin:36px 0;background:rgba(212,134,10,0.05) }}
    .ng-pullquote p {{ font-family:'Playfair Display',serif;font-size:20px;font-style:italic;line-height:1.5;color:#1A1A18;margin:0!important }}
    .ng-pullquote cite {{ display:block;margin-top:10px;font-size:12px;font-style:normal;color:rgba(26,26,24,0.45);letter-spacing:0.08em;text-transform:uppercase }}

    /* Figures */
    .ng-figure {{ margin:40px 0;overflow:hidden }}
    .ng-figure img {{ width:100%;display:block;object-fit:cover;border:1px solid rgba(26,26,24,0.07) }}
    .ng-figure figcaption {{ padding:9px 0 0;font-size:12px;color:rgba(26,26,24,0.48);font-style:italic;border-top:1px solid rgba(26,26,24,0.09) }}
    .ng-figure figcaption strong {{ color:rgba(26,26,24,0.68);font-style:normal }}

    /* Console pair — two dark cards side by side */
    .ng-console-pair {{ display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin:44px 0 }}
    .ng-console-card {{ background:#1A1A18;overflow:hidden }}
    .ng-console-img {{ height:280px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden }}
    .ng-console-label {{ position:absolute;top:14px;left:14px;font-size:10px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#D4860A;background:rgba(0,0,0,0.55);padding:4px 10px }}
    .ng-console-body {{ padding:24px 20px 26px }}
    .ng-console-name {{ font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:#fff;margin-bottom:4px }}
    .ng-console-sub {{ font-size:11px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#D4860A;margin-bottom:12px }}
    .ng-console-desc {{ font-size:13px;color:rgba(255,255,255,0.5);line-height:1.6 }}

    /* Records list */
    .ng-records {{ list-style:none;margin:16px 0 }}
    .ng-records li {{ display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(26,26,24,0.07);font-size:15px;color:#3A3A38;align-items:center }}
    .ng-records li:last-child {{ border-bottom:none }}
    .ng-record-title {{ font-weight:600;color:#1A1A18 }}
    .ng-record-studio {{ font-size:12px;color:rgba(26,26,24,0.45);margin-top:2px }}
    .ng-record-year {{ font-size:12px;color:rgba(26,26,24,0.38);flex-shrink:0;margin-left:16px;font-family:'DM Sans',sans-serif;font-weight:500 }}

    /* Specs table */
    .ng-specs {{ background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.08);overflow:hidden;margin:32px 0 }}
    .ng-specs-header {{ background:#1A1A18;padding:12px 20px;font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.5) }}
    .ng-specs table {{ width:100%;border-collapse:collapse }}
    .ng-specs tr:nth-child(even) {{ background:rgba(26,26,24,0.03) }}
    .ng-specs td {{ padding:10px 20px;font-size:13px }}
    .ng-specs td:first-child {{ color:rgba(26,26,24,0.48);width:46%;font-weight:500 }}
    .ng-specs td:last-child {{ color:#1A1A18;font-weight:500 }}

    /* Timeline */
    .ng-timeline {{ margin:32px 0 }}
    .ng-timeline-item {{ display:grid;grid-template-columns:72px 1fr;gap:20px;padding:16px 0;border-bottom:1px solid rgba(26,26,24,0.07) }}
    .ng-timeline-item:last-child {{ border-bottom:none }}
    .ng-timeline-year {{ font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:#D4860A;line-height:1;padding-top:3px }}
    .ng-timeline-text {{ font-size:14px;color:#3A3A38;line-height:1.65 }}
    .ng-timeline-text strong {{ color:#1A1A18 }}

    /* FAQ */
    .ng-faq-item {{ border-bottom:1px solid rgba(26,26,24,0.08) }}
    .ng-faq-item:first-child {{ border-top:1px solid rgba(26,26,24,0.08) }}
    .ng-faq-q {{ width:100%;text-align:left;background:none;border:none;cursor:pointer;padding:16px 0;display:flex;justify-content:space-between;align-items:center;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:600;color:#1A1A18 }}
    .ng-faq-q::after {{ content:'+';font-size:20px;color:#D4860A;font-weight:300;flex-shrink:0;margin-left:16px }}
    .ng-faq-q.open::after {{ content:'−' }}
    .ng-faq-a {{ display:none;padding:0 0 16px;font-size:14px;color:#3A3A38;line-height:1.7 }}
    .ng-faq-a.open {{ display:block }}

    /* Sidebar */
    .ng-sidebar {{ position:sticky;top:68px }}
    .ng-sb-card {{ background:var(--off-white,#F7F5F2);border:1px solid rgba(26,26,24,0.08);overflow:hidden;margin-bottom:20px }}
    .ng-sb-header {{ background:#1A1A18;padding:12px 18px;font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.45) }}
    .ng-sb-body {{ padding:18px }}
    .ng-sb-body p {{ font-size:13px;color:rgba(26,26,24,0.65);line-height:1.6;margin-bottom:10px }}
    .ng-sb-body p:last-child {{ margin-bottom:0 }}
    .ng-sb-body a {{ color:#D4860A;text-decoration:none }}
    .ng-sb-body a:hover {{ text-decoration:underline }}
    .ng-sb-expert {{ background:#EDE8E2;border:1px solid rgba(212,134,10,0.25);padding:18px;margin-bottom:20px }}
    .ng-sb-expert-label {{ font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#D4860A;margin-bottom:8px }}
    .ng-sb-expert-text {{ font-size:13px;color:rgba(26,26,24,0.68);line-height:1.6;margin-bottom:14px }}
    .ng-sb-cta {{ display:block;background:#1A1A18;color:#fff;text-align:center;padding:11px;font-size:12px;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;text-decoration:none;border-radius:2px }}
    .ng-sb-cta:hover {{ background:#2C2C2A;text-decoration:none!important }}
    .ng-sb-amber-cta {{ background:#D4860A }}
    .ng-sb-amber-cta:hover {{ background:#b8720a!important }}
    .ng-sb-product {{ display:flex;gap:12px;padding:12px 0;border-bottom:1px solid rgba(26,26,24,0.07);align-items:center }}
    .ng-sb-product:last-child {{ border-bottom:none;padding-bottom:0 }}
    .ng-sb-product-img {{ width:56px;height:56px;background:var(--off-white,#F7F5F2);flex-shrink:0;overflow:hidden;border:1px solid rgba(26,26,24,0.08) }}
    .ng-sb-product-img img {{ width:100%;height:100%;object-fit:cover }}
    .ng-sb-product-name {{ font-size:13px;font-weight:600;color:#1A1A18;line-height:1.3;margin-bottom:3px }}
    .ng-sb-product-price {{ font-size:12px;color:#D4860A;font-weight:600 }}
    .vk-stick {{ position:fixed;bottom:0;left:0;right:0;background:#1A1A18;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;border-top:2px solid #D4860A }}
    .vk-stick-title {{ font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB }}
    .vk-stick-sub {{ font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px }}
    .vk-stick-cta {{ background:#D4860A;color:#fff;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em }}
    .vk-stick-ghost {{ color:rgba(255,255,255,0.6);font-size:13px;font-weight:500;text-decoration:none;padding:12px 0 }}
    @media(max-width:700px){{.vk-stick{{padding:12px 20px}}}}
  </style>

  <!-- BREADCRUMB -->
  <div class="ng-breadcrumb">
    <a href="#">Home</a><span>›</span>
    <a href="#">Gear Guides</a><span>›</span>
    <a href="#">Preamps and EQs</a><span>›</span>
    The Neve 1073
  </div>

  <!-- ── HERO — LIGHT 50/50 ── -->
  <section style="background:#EDE8E2;display:grid;grid-template-columns:1fr 1fr;min-height:560px;overflow:hidden">
    <div style="padding:80px 56px 80px 80px;display:flex;flex-direction:column;justify-content:center">
      <p style="font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#D4860A;margin-bottom:16px">Gear Guide · Neve Electronics</p>
      <h1 style="font-family:'Playfair Display',serif;font-size:clamp(40px,4.5vw,62px);font-weight:700;line-height:1.06;color:#1A1A18;margin-bottom:20px">The Neve 1073<br><em style="font-style:italic;color:rgba(26,26,24,0.55)">History, Legacy and Sound</em></h1>
      <p class="speakable" style="font-size:18px;color:rgba(26,26,24,0.65);line-height:1.65;margin-bottom:36px;max-width:520px">The mic preamp and EQ module that defined modern recording — hand-wired in England since 1970, heard on every record that mattered.</p>
      <div style="display:flex;gap:36px">
        <div style="border-left:2px solid #D4860A;padding-left:16px">
          <div style="font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;line-height:1">1970</div>
          <div style="font-size:12px;color:rgba(26,26,24,0.48);margin-top:4px">Year of origin</div>
        </div>
        <div style="border-left:2px solid #D4860A;padding-left:16px">
          <div style="font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;line-height:1">+80dB</div>
          <div style="font-size:12px;color:rgba(26,26,24,0.48);margin-top:4px">Max mic gain</div>
        </div>
        <div style="border-left:2px solid #D4860A;padding-left:16px">
          <div style="font-family:'Playfair Display',serif;font-size:30px;font-weight:700;color:#1A1A18;line-height:1">50+</div>
          <div style="font-size:12px;color:rgba(26,26,24,0.48);margin-top:4px">Years in production</div>
        </div>
      </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;padding:32px;background:#fff;position:relative">
      <img src="{IMG['vertical_80s']}" alt="AMS Neve 1073 80-series module — vertical standing" style="width:100%;height:460px;object-fit:contain;display:block">
      <div style="position:absolute;bottom:14px;right:16px;font-size:10px;letter-spacing:0.08em;text-transform:uppercase;color:rgba(26,26,24,0.35);font-family:'DM Sans',sans-serif">AMS Neve 1073 — 80-series module</div>
    </div>
  </section>

  <!-- ── CONTENT OUTER ── -->
  <div class="ng-outer">

    <!-- LEFT: ARTICLE -->
    <article class="ng-article">

      <h2>Born in a Workshop in Little Shelford</h2>
      <p>In the mid-1960s, Rupert Neve set up shop in Little Shelford, Cambridgeshire, determined to build audio equipment that sounded better than anything on the market. Transistors were new and expensive. Reliable faders didn't exist yet. None of it stopped him.</p>
      <p>By 1968, Neve Electronics had moved to a purpose-built factory in Melbourn, Hertfordshire, and was taking orders from recording and broadcast studios across the world — each console custom, each one entirely hand-wired by Neve technicians to tolerances that production-line manufacturing could not match.</p>
      <p>The <strong>Neve 1073</strong> was finalized around 1970 for the Wessex A88 console. It combined a Class A microphone preamplifier with a three-band program equalizer and high-pass filter into a single module. In the specific way Neve did it — with custom Marinair transformers and discrete transistor circuitry — it became something that recording engineers would spend the next five decades trying to replicate.</p>

      <!-- Rack image — the 8-channel OPX front view -->
      <figure class="ng-figure" style="margin-top:40px">
        <img src="{IMG['rack_front']}" alt="AMS Neve 1073 — 8-channel rack, front high view" style="max-height:320px;object-fit:cover;object-position:center 30%">
        <figcaption><strong>Neve 1073 — 8-channel rack</strong> &mdash; the stepped gain switch, pad, phase reverse, and three-band EQ are unmistakable. Each module is entirely hand-wired and transformer-coupled at both input and output.</figcaption>
      </figure>

      <h2>The 80 Series: A Console Built Around a Module</h2>
      <p>The 1073 did not exist in isolation. It was the heart of Neve's defining product line: the <strong>80 Series mixing consoles</strong>. First introduced with the 8014 model in 1969, the 80 Series grew into the most sought-after recording consoles on earth. Each was assembled to order — custom channel counts, custom routing — and each was entirely hand-wired by Neve technicians.</p>
      <p>The 8014 and 8034 were Class A throughout, populated primarily with 1073 preamps. As the decade progressed the line expanded. The 8028 used the 1073b variant. The <strong>8058 and 8068</strong>, Neve's first in-line monitor consoles introduced in 1976, used the 31102 module — closely related to the 1073 with the same Marinair transformer specification. George Martin had a custom A4792 built for <strong>AIR Studios Montserrat</strong>; Dire Straits recorded <em>Brothers in Arms</em> on it.</p>
      <p>In 1978, Neve introduced the <strong>8078</strong>: the last and largest of the hand-wired 80 Series consoles — available with up to 72 channels, loaded with 31105 preamp modules sharing the same Marinair transformers as the original 1073. Neve ceased 80 Series production in 1979. A limited number were ever made.</p>

      <div class="ng-pullquote">
        <p>"Studios that are lucky enough to own a Neve console of the 80 Series generally have them as the centerpiece of their room — and for good reason."</p>
        <cite>— Vintage King Audio</cite>
      </div>

      <!-- CLASSIC STUDIO LEGACY CARDS — rooms that ran Neve 8068 / 8078 -->
      <div class="ng-console-pair">
        <div class="ng-console-card">
          <div class="ng-console-img" style="background:linear-gradient(160deg,#0d1108 0%,#161c0e 55%,#0d1108 100%)">
            <div class="ng-console-label">Neve 8078</div>
            <svg width="64" height="64" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.14"><rect x="4" y="18" width="48" height="20" rx="1" stroke="#fff" stroke-width="1.2"/><line x1="4" y1="26" x2="52" y2="26" stroke="#fff" stroke-width="0.8" opacity=".4"/><rect x="7" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="15" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="23" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="31" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="39" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><circle cx="44" cy="21" r="2" stroke="#D4860A" stroke-width="0.8"/><circle cx="38" cy="21" r="2" stroke="#fff" stroke-width="0.8" opacity=".3"/></svg>
            <div style="position:absolute;bottom:14px;left:0;right:0;text-align:center;font-size:11px;color:rgba(255,255,255,0.22);letter-spacing:0.06em">Est. 1970 · Greenwich Village, NYC</div>
          </div>
          <div class="ng-console-body">
            <div class="ng-console-name">Electric Lady Studios</div>
            <div class="ng-console-sub">New York, NY · 1970 – Present</div>
            <p class="ng-console-desc">Built by Jimi Hendrix in 1970, Electric Lady ran a Neve 8078 at the heart of Studio A. David Bowie recorded <em>Scary Monsters</em> here. AC/DC tracked <em>Back in Black</em>. Daft Punk returned to this console for <em>Random Access Memories</em>. Still operating today.</p>
          </div>
        </div>
        <div class="ng-console-card">
          <div class="ng-console-img" style="background:linear-gradient(160deg,#080e18 0%,#0e1828 55%,#060e18 100%)">
            <div class="ng-console-label">Custom Neve 8078</div>
            <svg width="64" height="64" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.14"><rect x="4" y="18" width="48" height="20" rx="1" stroke="#fff" stroke-width="1.2"/><line x1="4" y1="26" x2="52" y2="26" stroke="#fff" stroke-width="0.8" opacity=".4"/><rect x="7" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="15" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="23" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="31" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="39" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><circle cx="44" cy="21" r="2" stroke="#D4860A" stroke-width="0.8"/><circle cx="38" cy="21" r="2" stroke="#fff" stroke-width="0.8" opacity=".3"/></svg>
            <div style="position:absolute;bottom:14px;left:0;right:0;text-align:center;font-size:11px;color:rgba(255,255,255,0.22);letter-spacing:0.06em">Est. 1979 · Montserrat, Caribbean</div>
          </div>
          <div class="ng-console-body">
            <div class="ng-console-name">AIR Studios Montserrat</div>
            <div class="ng-console-sub">George Martin · 1979 – 1989</div>
            <p class="ng-console-desc">George Martin built AIR Montserrat around a custom Neve A4792 — the 8078 variant wired to his specification. Dire Straits' <em>Brothers in Arms</em> was recorded here. The Police, Paul McCartney, and Jimmy Buffett all tracked at this desk. Lost to Hurricane Hugo in 1989.</p>
          </div>
        </div>
        <div class="ng-console-card">
          <div class="ng-console-img" style="background:linear-gradient(160deg,#180808 0%,#280e0e 55%,#180808 100%)">
            <div class="ng-console-label">Neve 8078</div>
            <svg width="64" height="64" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:0.14"><rect x="4" y="18" width="48" height="20" rx="1" stroke="#fff" stroke-width="1.2"/><line x1="4" y1="26" x2="52" y2="26" stroke="#fff" stroke-width="0.8" opacity=".4"/><rect x="7" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="15" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="23" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="31" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><rect x="39" y="29" width="5" height="5" rx="0.5" stroke="#fff" stroke-width="0.8" opacity=".35"/><circle cx="44" cy="21" r="2" stroke="#D4860A" stroke-width="0.8"/><circle cx="38" cy="21" r="2" stroke="#fff" stroke-width="0.8" opacity=".3"/></svg>
            <div style="position:absolute;bottom:14px;left:0;right:0;text-align:center;font-size:11px;color:rgba(255,255,255,0.22);letter-spacing:0.06em">Est. 1958 · Miami, FL</div>
          </div>
          <div class="ng-console-body">
            <div class="ng-console-name">Criteria Recording Studios</div>
            <div class="ng-console-sub">Miami, FL · 1958 – Present</div>
            <p class="ng-console-desc">Criteria's Neve 8078 made it the definitive room for the mid-1970s mainstream. The Eagles' <em>Hotel California</em>. Eric Clapton's <em>461 Ocean Boulevard</em>. The Bee Gees' run of disco-era albums. The 8078's extended high-frequency response defined the sound of that era.</p>
          </div>
        </div>
      </div>

      <h2>The Sound: What Makes It Different</h2>
      <p>Engineers reach for the 1073 for a specific reason: <strong>color</strong>. Unlike transparent preamps designed to capture sound neutrally, the 1073 imposes itself on the signal in ways that are consistently musical. Low-end frequencies are tight and authoritative. The upper-midrange has a presence that cuts through a dense mix without harshness.</p>
      <p>The source of this character lives in the transformers. Neve specified custom <strong>Marinair input and output transformers</strong> that introduce gentle second-harmonic saturation at higher signal levels. Combined with Class A discrete transistor circuitry — no op-amps, no integrated circuits — the 1073 has a saturation behavior that modern circuit design can approximate but has never duplicated.</p>
      <p>The three-band EQ uses <strong>handcrafted inductors</strong> manufactured to the original unpublished specification from the Wessex A88 design. Inductor EQ produces an asymmetric curve — slightly tighter on the boost side, extending gently on the cut — which is why 1073 EQ moves rarely sound surgical even at large values.</p>

      <!-- Module detail image -->
      <figure class="ng-figure">
        <img src="{IMG['h_left_lg']}" alt="AMS Neve 1073 Classic H — left 3/4 view showing gain knob" style="max-height:400px;object-fit:cover">
        <figcaption><strong>Neve 1073 Classic H</strong> &mdash; the red gain knob selects both input level and source (mic vs line). No separate mic/line switch. Stepped in 5dB increments from +20 to +80dB mic gain.</figcaption>
      </figure>

      <h2>The Records It Made</h2>
      <p>Through the 1970s, the transformer-balanced Neve preamp was the standard at the highest-level rooms in the world. The studios that ran 80 Series consoles were the rooms where the decade's most enduring records were made.</p>
      <ul class="ng-records">
        <li><div><div class="ng-record-title">Led Zeppelin IV</div><div class="ng-record-studio">Island Studios, London · Headley Grange (Neve mobile)</div></div><div class="ng-record-year">1971</div></li>
        <li><div><div class="ng-record-title">Exile on Main St. — The Rolling Stones</div><div class="ng-record-studio">Olympic Studios, London · Stargroves (Neve mobile)</div></div><div class="ng-record-year">1972</div></li>
        <li><div><div class="ng-record-title">Dark Side of the Moon — Pink Floyd</div><div class="ng-record-studio">Abbey Road Studios, London</div></div><div class="ng-record-year">1973</div></li>
        <li><div><div class="ng-record-title">Rumours — Fleetwood Mac</div><div class="ng-record-studio">Record Plant, Sausalito</div></div><div class="ng-record-year">1977</div></li>
        <li><div><div class="ng-record-title">Brothers in Arms — Dire Straits</div><div class="ng-record-studio">AIR Studios Montserrat (Neve custom A4792)</div></div><div class="ng-record-year">1985</div></li>
        <li><div><div class="ng-record-title">Nevermind — Nirvana</div><div class="ng-record-studio">Sound City, Van Nuys (Neve 8028)</div></div><div class="ng-record-year">1991</div></li>
      </ul>

      <div class="ng-pullquote">
        <p>"When I walked into a room with a Neve 8078, I knew the session would sound good before I touched a single fader. The console did half the work."</p>
        <cite>Bob Ludwig — Mastering Engineer, Rolling Stones &middot; Nirvana &middot; U2</cite>
      </div>

      <h2>Timeline: From Module to Icon</h2>
      <div class="ng-timeline">
        <div class="ng-timeline-item"><div class="ng-timeline-year">1961</div><div class="ng-timeline-text">Rupert Neve founds <strong>Neve Electronics</strong> in the UK, designing custom broadcast and recording equipment.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">1968</div><div class="ng-timeline-text">Neve moves to a purpose-built factory in <strong>Melbourn, Hertfordshire</strong>. The 80 Series console program begins.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">1970</div><div class="ng-timeline-text">The <strong>Neve 1073</strong> is finalized for the Wessex A88 console. Class A preamp, Marinair transformers, 3-band inductor EQ with HPF. It will power the world's most important studios for the next decade.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">1976</div><div class="ng-timeline-text">Neve introduces the <strong>8058 and 8068</strong> in-line monitor consoles with 31102 modules — same Marinair transformer spec as the 1073. Thames Television receives the first UK installation.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">1978</div><div class="ng-timeline-text">The <strong>8078</strong> — last of the hand-wired 80 Series — enters production. Up to 72 channels. George Martin's custom A4792 is built for <strong>AIR Studios Montserrat</strong>.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">1979</div><div class="ng-timeline-text">Neve <strong>ceases 80 Series production</strong>. A limited number were ever built. Surviving consoles begin decades of service that continues today.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">1985</div><div class="ng-timeline-text">Neve merges with AMS to form <strong>AMS Neve</strong>. The 1073 circuit lives on in reissues and 500 Series modules manufactured in the UK to the original spec.</div></div>
        <div class="ng-timeline-item"><div class="ng-timeline-year">Today</div><div class="ng-timeline-text">AMS Neve manufactures the <strong>1073SPX, 1073OPX, and 1073 Classic H</strong> — faithful reproductions using original circuit topology, Marinair transformers, and hand-wired construction.</div></div>
      </div>

      <h2>Official Specifications</h2>
      <div class="ng-specs">
        <div class="ng-specs-header">AMS Neve 1073 — Current Production Specifications</div>
        <table>
          <tr><td>Circuit type</td><td>Class A, fully discrete transistor</td></tr>
          <tr><td>Input transformers</td><td>Marinair spec (10468 mic / 31267 line) — exclusive to Neve</td></tr>
          <tr><td>Output transformer</td><td>LO1166 — designed by Rupert Neve, 1964</td></tr>
          <tr><td>Construction</td><td>Hand-built and hand-wired, UK</td></tr>
          <tr><td>Mic gain range</td><td>+20 to +80 dB in 5dB steps</td></tr>
          <tr><td>Line gain</td><td>−10 to +20 dB in 5dB steps · 10kΩ impedance</td></tr>
          <tr><td>EIN</td><td>&lt; −125 dBu @ 60dB gain</td></tr>
          <tr><td>Max output</td><td>&gt; +26 dBu into 600Ω</td></tr>
          <tr><td>THD</td><td>&lt; 0.07% (50Hz–10kHz at +20dBu into 600Ω)</td></tr>
          <tr><td>Frequency response</td><td>±0.5 dB 20Hz–20kHz · −3dB at 40kHz</td></tr>
          <tr><td>EQ — High shelf</td><td>±16 dB fixed at 12 kHz</td></tr>
          <tr><td>EQ — Mid peak/dip</td><td>±18 dB · 360 / 700 / 1.6k / 3.2k / 4.8k / 7.2k Hz</td></tr>
          <tr><td>EQ — Low shelf</td><td>±16 dB · 35 / 60 / 110 / 220 Hz</td></tr>
          <tr><td>High-pass filter</td><td>18 dB/oct · 50 / 80 / 160 / 300 Hz</td></tr>
          <tr><td>Input impedance options</td><td>1.2kΩ / 300Ω (rear Hi/Lo switch)</td></tr>
          <tr><td>Phantom power</td><td>+48V switchable</td></tr>
          <tr><td>Dimensions (module)</td><td>45mm W × 222mm H × 254mm D · ~2.5kg</td></tr>
        </table>
      </div>

      <h2>Frequently Asked Questions</h2>
      <div>
        <div class="ng-faq-item">
          <button class="ng-faq-q" onclick="ngFaq(this)">What is the Neve 1073?</button>
          <div class="ng-faq-a">The Neve 1073 is a microphone preamplifier and three-band equalizer module designed by Rupert Neve around 1970. Class A discrete transistor circuitry, exclusive Marinair transformers, hand-built in the UK. Widely regarded as the most influential piece of studio hardware ever made — and the only preamp still in continuous production to its original specification after more than fifty years.</div>
        </div>
        <div class="ng-faq-item">
          <button class="ng-faq-q" onclick="ngFaq(this)">What consoles used the Neve 1073?</button>
          <div class="ng-faq-a">The 1073 module was designed for the Wessex A88 console and used in early Neve 80 Series consoles (8014, 8034). Closely related modules (1073b, 31102, 31105) with the same Marinair transformer specification were used in the 8028, 8058, 8068, and 8078. All 80 Series consoles share the same fundamental sonic character.</div>
        </div>
        <div class="ng-faq-item">
          <button class="ng-faq-q" onclick="ngFaq(this)">How is the Neve 1073 different from clones?</button>
          <div class="ng-faq-a">The original 1073 uses the exclusive Marinair specification input transformers (models 10468 and 31267) and Rupert Neve's LO1166 output transformer — both manufactured under Neve's specification and unavailable to any third party. The hand-wired construction follows Rupert Neve's original pencil-on-paper drawings. These elements together produce the specific harmonic character that no licensed clone has fully duplicated.</div>
        </div>
        <div class="ng-faq-item">
          <button class="ng-faq-q" onclick="ngFaq(this)">Can I buy a vintage original Neve 1073?</button>
          <div class="ng-faq-a">Original 1073 modules appear on the used market, though authentic examples have become increasingly rare and expensive. Vintage King regularly sources and inspects vintage Neve modules and consoles — contact our team for current availability and pricing.</div>
        </div>
        <div class="ng-faq-item">
          <button class="ng-faq-q" onclick="ngFaq(this)">What is the difference between the 1073 module and the 1073OPX?</button>
          <div class="ng-faq-a">The 1073OPX is an 8-channel rackmount unit — eight complete 1073 circuits in a 3U chassis with individual phantom, pad, and polarity per channel. The same Marinair transformer specification and Class A discrete circuit as the single module, manufactured by AMS Neve in the UK. Available from $6,499.</div>
        </div>
      </div>

    </article>

    <!-- RIGHT: SIDEBAR -->
    <aside class="ng-sidebar">

      <div class="ng-sb-expert">
        <div class="ng-sb-expert-label">Talk to an Expert</div>
        <p class="ng-sb-expert-text">Not sure which 1073 format fits your setup? Our consultants have run sessions on vintage Neve desks and know this gear from both sides of the glass.</p>
        <a href="audio-consultants.html" class="ng-sb-cta">Call 888.653.1184</a>
      </div>

      <div class="ng-sb-card">
        <div class="ng-sb-header">Shop Neve 1073</div>
        <div class="ng-sb-body">
          <div class="ng-sb-product">
            <div class="ng-sb-product-img"><img src="{IMG['h_left_sm']}" alt="Neve 1073 Classic H"></div>
            <div><div class="ng-sb-product-name">AMS Neve 1073 Classic H</div><div class="ng-sb-product-price">Inquire for pricing</div></div>
          </div>
          <div class="ng-sb-product">
            <div class="ng-sb-product-img" style="display:flex;align-items:center;justify-content:center;background:#1A1A18"><img src="{IMG['vertical_80s']}" alt="1073 vertical module" style="object-fit:contain;padding:4px"></div>
            <div><div class="ng-sb-product-name">AMS Neve 1073 500 Series</div><div class="ng-sb-product-price">From $799</div></div>
          </div>
          <div class="ng-sb-product">
            <div class="ng-sb-product-img" style="display:flex;align-items:center;justify-content:center;background:#1A1A18"><img src="{IMG['rack_front2']}" alt="1073 OPX rack" style="object-fit:cover"></div>
            <div><div class="ng-sb-product-name">AMS Neve 1073OPX (8ch)</div><div class="ng-sb-product-price">From $6,499</div></div>
          </div>
          <a href="#" onclick="return false" class="ng-sb-cta ng-sb-amber-cta" style="display:block;margin-top:16px">Browse All Neve at VK</a>
        </div>
      </div>

      <div class="ng-sb-card">
        <div class="ng-sb-header">About This Guide</div>
        <div class="ng-sb-body">
          <p>Vintage King has been sourcing, restoring, and selling vintage Neve consoles and modules for over 30 years. We completed the full restoration of the Neve 8078 at Electric Lady Studios and dozens of world-class rooms.</p>
          <p>Questions about vintage Neve hardware, console restoration, or module sourcing? Our team is here.</p>
        </div>
      </div>

      <div class="ng-sb-card">
        <div class="ng-sb-header">Related Guides</div>
        <div class="ng-sb-body">
          <p><a href="#">The SSL 4000: History and Legacy</a></p>
          <p><a href="#">API 512 Preamp: What Makes It Different</a></p>
          <p><a href="#">Vintage Console Buying Guide</a></p>
          <p><a href="hall-of-fame.html">VK Hall of Fame →</a></p>
        </div>
      </div>

    </aside>
  </div>

  <div id="footer-neve-1073-guide"></div>

  <div class="vk-stick">
    <div>
      <div class="vk-stick-title">Neve 1073</div>
      <div class="vk-stick-sub">500 Series from $499 · Rackmount from $1,295 · Vintage originals by request</div>
    </div>
    <div style="display:flex;gap:12px;align-items:center">
      <a href="https://vintageking.com/neve-1073" target="_blank" class="vk-stick-cta">Shop at Vintage King</a>
      <a href="audio-consultants.html" class="vk-stick-ghost">Ask an Expert</a>
    </div>
  </div>
  <div style="height:68px"></div>
</div>
"""

INLINE_JS = """\
<script>
  function ngFaq(btn) {
    var a = btn.nextElementSibling;
    var isOpen = a.classList.contains('open');
    document.querySelectorAll('.ng-faq-a.open').forEach(function(el){el.classList.remove('open');});
    document.querySelectorAll('.ng-faq-q.open').forEach(function(el){el.classList.remove('open');});
    if (!isOpen) { a.classList.add('open'); btn.classList.add('open'); }
  }
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
