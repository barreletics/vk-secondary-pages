"""audio-consultants.html — VK Meet Our Audio Consultants page."""
import re

SLUG  = "audio-consultants"
TITLE = "Meet Our Audio Consultants — Expert Gear Advice | Vintage King"
META  = "Talk to a Vintage King audio consultant — real experts who record, mix, and master. Get honest gear advice by phone, chat, or email. No pressure, ever."

JSON_LD = """\
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "name": "Vintage King Audio Consultation",
      "provider": {"@type": "Organization", "name": "Vintage King Audio", "url": "https://vintageking.com", "telephone": "+18886531184"},
      "description": "One-on-one pro audio gear consultations by phone, chat, or email. VK consultants are working engineers and producers with hands-on studio experience.",
      "serviceType": "Audio Equipment Consulting"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Is the consultation free?",
          "acceptedAnswer": {"@type": "Answer", "text": "Yes — all VK consultations are free. Call 888.653.1184 or start a chat anytime."}
        },
        {
          "@type": "Question",
          "name": "Are VK consultants real engineers?",
          "acceptedAnswer": {"@type": "Answer", "text": "Yes. Every VK consultant is an active or former engineer, producer, or musician with real studio experience — not a sales script."}
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
  <span style="opacity:0.75">Audio Consultants</span>
  <span style="opacity:0.35">|</span>
  <a href="studio-professionals.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Studio Professionals</a>
  <span style="opacity:0.35">|</span>
  <a href="trade-program.html" style="color:rgba(255,255,255,0.55);text-decoration:none">Trade Program</a>
</nav>
"""

PAGE_BODY = """\
<div id="audio-consultants" class="page active">
  <div id="nav-audio-consultants"></div>

  <!-- ── HERO ── -->
  <section style="background:#EDE8E2;padding:96px 0 80px">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p class="speakable" style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:16px">Expert Gear Advice</p>
      <h1 style="font-family:'Playfair Display',serif;font-size:52px;font-weight:700;color:#1A1A18;line-height:1.08;margin-bottom:24px;max-width:640px">Talk to Someone<br>Who Actually Records</h1>
      <p class="speakable" style="font-size:18px;color:rgba(26,26,24,0.7);max-width:520px;line-height:1.6;margin-bottom:36px">Every VK consultant is an active or former engineer, producer, or musician. Real studio experience. No scripts. No pressure.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">
        <a href="tel:8886531184" style="display:inline-flex;align-items:center;gap:8px;background:#C0392B;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 01.07 2.18 2 2 0 012.06 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
          888.653.1184
        </a>
        <a href="#" onclick="return false" style="display:inline-flex;align-items:center;gap:8px;border:1.5px solid rgba(26,26,24,0.35);color:#1A1A18;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">
          Start Live Chat
        </a>
      </div>
      <p style="font-size:12px;color:rgba(26,26,24,0.42);margin-top:16px">Mon–Sat 9:30AM–9PM ET &nbsp;·&nbsp; Response within 1 business day by email</p>
    </div>
  </section>

  <!-- ── CREDENTIAL STRIP ── -->
  <section style="background:var(--warm-white,#FDFCFB);border-top:1px solid rgba(26,26,24,0.08);border-bottom:1px solid rgba(26,26,24,0.08);padding:20px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px;display:flex;gap:40px;flex-wrap:wrap;align-items:center">
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:22px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">30+</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Years in Pro Audio</span>
      </div>
      <div style="width:1px;height:28px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:22px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">1000s</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">of Clients Worldwide</span>
      </div>
      <div style="width:1px;height:28px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:22px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">Free</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Consultations Always</span>
      </div>
      <div style="width:1px;height:28px;background:rgba(26,26,24,0.1)"></div>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="font-size:22px;font-weight:700;color:#1A1A18;font-family:'DM Sans',sans-serif">Grammy</span>
        <span style="font-size:13px;color:rgba(26,26,24,0.55)">Winning Clients</span>
      </div>
    </div>
  </section>

  <!-- ── CONSULTANT PROFILES ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:12px">The Team</p>
      <h2 style="font-family:'Playfair Display',serif;font-size:38px;font-weight:700;color:#1A1A18;margin-bottom:12px">Your Experts</h2>
      <p style="font-size:16px;color:rgba(26,26,24,0.6);max-width:520px;margin-bottom:48px;line-height:1.6">These aren't salespeople. They track sessions, mix records, and design studios. When they recommend gear, it's because they've used it.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:24px">

        <!-- Consultant 1 -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:260px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Photo Placeholder]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:16px;font-weight:700;color:#1A1A18;margin-bottom:2px;font-family:'DM Sans',sans-serif">Scott Adamson</div>
            <div style="font-size:12px;color:#C0392B;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:10px">Senior Audio Consultant</div>
            <p style="font-size:13px;color:rgba(26,26,24,0.62);line-height:1.5;margin-bottom:14px">Recording engineer &amp; gear specialist. 15+ years tracking sessions across Nashville and beyond. Deep analog and vintage mic expertise.</p>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Analog Consoles</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Vintage Mics</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Pro Tools</span>
            </div>
          </div>
        </div>

        <!-- Consultant 2 -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:260px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Photo Placeholder]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:16px;font-weight:700;color:#1A1A18;margin-bottom:2px;font-family:'DM Sans',sans-serif">Matt Seidel</div>
            <div style="font-size:12px;color:#C0392B;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:10px">Audio Consultant</div>
            <p style="font-size:13px;color:rgba(26,26,24,0.62);line-height:1.5;margin-bottom:14px">Producer, mixer, and DAW specialist. Fluent across Logic, Ableton, and Studio One. Guides home studio builders from first interface to mastering chain.</p>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">DAW &amp; Monitoring</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Home Studio</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Plug-ins</span>
            </div>
          </div>
        </div>

        <!-- Consultant 3 -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:260px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Photo Placeholder]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:16px;font-weight:700;color:#1A1A18;margin-bottom:2px;font-family:'DM Sans',sans-serif">Blake Eisele</div>
            <div style="font-size:12px;color:#C0392B;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:10px">Studio Systems Specialist</div>
            <p style="font-size:13px;color:rgba(26,26,24,0.62);line-height:1.5;margin-bottom:14px">Systems integrator and acoustic designer. Specializes in monitor calibration, summing systems, and outboard signal chains for commercial studios.</p>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Monitors</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Summing</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Signal Path</span>
            </div>
          </div>
        </div>

        <!-- Consultant 4 -->
        <div style="background:#fff;border:1px solid rgba(26,26,24,0.07);overflow:hidden">
          <div style="min-height:260px;background:var(--off-white,#F7F5F2);border-bottom:1px solid rgba(26,26,24,0.08);display:flex;align-items:center;justify-content:center">
            <span style="font-size:11px;font-family:'DM Sans',sans-serif;color:rgba(26,26,24,0.3);letter-spacing:0.1em;text-transform:uppercase">[Photo Placeholder]</span>
          </div>
          <div style="padding:22px 20px 24px">
            <div style="font-size:16px;font-weight:700;color:#1A1A18;margin-bottom:2px;font-family:'DM Sans',sans-serif">Chris Thayer</div>
            <div style="font-size:12px;color:#C0392B;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:10px">Vintage Gear Specialist</div>
            <p style="font-size:13px;color:rgba(26,26,24,0.62);line-height:1.5;margin-bottom:14px">Certified tech and vintage gear historian. Deep knowledge of classic transformers, tubes, and circuit topologies — the go-to for outboard and hardware EQ/comp questions.</p>
            <div style="display:flex;gap:8px;flex-wrap:wrap">
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Outboard</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Tube Gear</span>
              <span style="font-size:11px;background:rgba(26,26,24,0.06);color:rgba(26,26,24,0.55);padding:4px 9px;border-radius:2px">Repairs</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ── HOW IT WORKS ── -->
  <section style="background:#fff;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:12px">What to Expect</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;line-height:1.12;margin-bottom:24px">No Pressure.<br>Real Answers.</h2>
          <p style="font-size:16px;color:rgba(26,26,24,0.65);line-height:1.65;margin-bottom:24px">A VK consultation isn't a sales call — it's a conversation between engineers. Tell us your room, your workflow, your budget. We'll give you an honest recommendation, even if it means spending less.</p>
          <p style="font-size:16px;color:rgba(26,26,24,0.65);line-height:1.65;margin-bottom:32px">We don't push brands we don't believe in, and we'll tell you when a used unit beats new at half the price.</p>
          <a href="tel:8886531184" style="display:inline-flex;align-items:center;gap:8px;background:#C0392B;color:#fff;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;text-decoration:none;border-radius:2px">Call 888.653.1184</a>
        </div>
        <div style="display:flex;flex-direction:column;gap:24px">
          <div style="display:flex;gap:20px;align-items:flex-start;padding:24px;border:1px solid rgba(26,26,24,0.07)">
            <div style="min-width:36px;height:36px;background:#C0392B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;font-family:'DM Sans',sans-serif;border-radius:2px;flex-shrink:0">1</div>
            <div>
              <div style="font-size:15px;font-weight:700;color:#1A1A18;margin-bottom:4px">Tell us what you're working on</div>
              <div style="font-size:14px;color:rgba(26,26,24,0.58);line-height:1.5">Your room, your DAW, your genre, your current gear — the more context you give, the more precise we can be.</div>
            </div>
          </div>
          <div style="display:flex;gap:20px;align-items:flex-start;padding:24px;border:1px solid rgba(26,26,24,0.07)">
            <div style="min-width:36px;height:36px;background:#C0392B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;font-family:'DM Sans',sans-serif;border-radius:2px;flex-shrink:0">2</div>
            <div>
              <div style="font-size:15px;font-weight:700;color:#1A1A18;margin-bottom:4px">Get honest options at every price point</div>
              <div style="font-size:14px;color:rgba(26,26,24,0.58);line-height:1.5">New, demo, used, vintage — we'll show you what fits your workflow and budget, not just what's in stock.</div>
            </div>
          </div>
          <div style="display:flex;gap:20px;align-items:flex-start;padding:24px;border:1px solid rgba(26,26,24,0.07)">
            <div style="min-width:36px;height:36px;background:#C0392B;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;font-family:'DM Sans',sans-serif;border-radius:2px;flex-shrink:0">3</div>
            <div>
              <div style="font-size:15px;font-weight:700;color:#1A1A18;margin-bottom:4px">Buy when you're ready — or don't</div>
              <div style="font-size:14px;color:rgba(26,26,24,0.58);line-height:1.5">No follow-up pressure. We want to earn your trust on every purchase, not just the first one.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── QUOTE RAIL ── -->
  <section style="background:#2C2C2A;padding:64px 0">
    <div style="max-width:800px;margin:0 auto;padding:0 40px;text-align:center">
      <div style="font-size:36px;color:rgba(255,255,255,0.12);font-family:'Playfair Display',serif;line-height:1;margin-bottom:16px">&ldquo;</div>
      <blockquote style="font-family:'Playfair Display',serif;font-size:22px;font-style:italic;color:rgba(255,255,255,0.88);line-height:1.5;margin-bottom:20px">I've been a customer for twelve years. The consultants at VK know gear the way other people know music theory. It's not a store — it's a resource.</blockquote>
      <cite style="font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.35);font-style:normal">Working Engineer — Nashville, TN</cite>
    </div>
  </section>

  <!-- ── CONTACT CTA ── -->
  <section style="background:#EDE8E2;padding:80px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start">
        <div>
          <p style="font-size:12px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#C0392B;margin-bottom:12px">Get in Touch</p>
          <h2 style="font-family:'Playfair Display',serif;font-size:36px;font-weight:700;color:#1A1A18;margin-bottom:16px">Start the Conversation</h2>
          <p style="font-size:16px;color:rgba(26,26,24,0.65);line-height:1.6;margin-bottom:32px">Call, chat, or email. We respond to every inquiry personally — usually within a few hours during business hours.</p>
          <div style="display:flex;flex-direction:column;gap:14px">
            <div style="display:flex;align-items:center;gap:14px">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#C0392B" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 01.07 2.18 2 2 0 012.06 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
              <span style="font-size:15px;color:#1A1A18;font-weight:600">888.653.1184</span>
              <span style="font-size:13px;color:rgba(26,26,24,0.45)">Mon–Sat 9:30AM–9PM ET</span>
            </div>
            <div style="display:flex;align-items:center;gap:14px">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#C0392B" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              <span style="font-size:15px;color:#1A1A18;font-weight:600">sales@vintageking.com</span>
            </div>
            <div style="display:flex;align-items:center;gap:14px">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#C0392B" stroke-width="2.5"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
              <span style="font-size:15px;color:#1A1A18;font-weight:600">Live Chat</span>
              <span style="font-size:13px;color:rgba(26,26,24,0.45)">on vintageking.com</span>
            </div>
          </div>
        </div>
        <form onsubmit="return false" style="background:#fff;padding:32px;border:1px solid rgba(26,26,24,0.08)">
          <h3 style="font-family:'Playfair Display',serif;font-size:20px;color:#1A1A18;margin-bottom:20px">Send a Quick Note</h3>
          <div style="display:flex;flex-direction:column;gap:14px">
            <input type="text" placeholder="Your name" style="width:100%;padding:12px 14px;border:1px solid rgba(26,26,24,0.18);background:#fff;font-family:'DM Sans',sans-serif;font-size:14px;color:#1A1A18;outline:none;border-radius:1px">
            <input type="email" placeholder="Email address" style="width:100%;padding:12px 14px;border:1px solid rgba(26,26,24,0.18);background:#fff;font-family:'DM Sans',sans-serif;font-size:14px;color:#1A1A18;outline:none;border-radius:1px">
            <input type="text" placeholder="Gear or topic (e.g. &quot;preamp for vocals under $2k&quot;)" style="width:100%;padding:12px 14px;border:1px solid rgba(26,26,24,0.18);background:#fff;font-family:'DM Sans',sans-serif;font-size:14px;color:#1A1A18;outline:none;border-radius:1px">
            <textarea rows="3" placeholder="Tell us about your setup and what you're trying to achieve..." style="width:100%;padding:12px 14px;border:1px solid rgba(26,26,24,0.18);background:#fff;font-family:'DM Sans',sans-serif;font-size:14px;color:#1A1A18;outline:none;resize:vertical;border-radius:1px"></textarea>
            <button type="submit" style="width:100%;padding:14px;background:#C0392B;color:#fff;border:none;font-family:'DM Sans',sans-serif;font-size:13px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;cursor:pointer;border-radius:2px">Send My Question</button>
          </div>
          <p style="font-size:12px;color:rgba(26,26,24,0.38);margin-top:12px;text-align:center">We respond personally — usually within a few hours.</p>
        </form>
      </div>
    </div>
  </section>

  <!-- ── VALUES BAR ── -->
  <section style="background:var(--off-white,#F7F5F2);padding:48px 0">
    <div style="max-width:1160px;margin:0 auto;padding:0 40px">
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Engineer-Level Advice</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Consultants who have tracked sessions and designed studios themselves.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">No Pressure, Ever</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Buy when you're ready. We earn repeat customers through trust, not tactics.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">New, Demo &amp; Vintage</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">We'll show you every tier — including when a used unit beats new at half the price.</div>
        </div>
        <div style="background:#fff;padding:24px 20px;border:1px solid rgba(26,26,24,0.07)">
          <div style="font-size:13px;font-weight:700;color:#1A1A18;margin-bottom:6px">Same Consultant, Long Term</div>
          <div style="font-size:13px;color:rgba(26,26,24,0.55);line-height:1.5">Studio Pro members get a dedicated contact who knows your setup.</div>
        </div>
      </div>
    </div>
  </section>

  <div id="footer-audio-consultants"></div>

  <style>.vk-stick{position:fixed;bottom:0;left:0;right:0;background:#1A1A18;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 40px;border-top:2px solid #C0392B}.vk-stick-title{font-family:'Playfair Display',serif;font-size:17px;font-weight:700;color:#FDFCFB}.vk-stick-sub{font-size:12px;color:rgba(255,255,255,0.45);margin-top:2px}.vk-stick-cta{background:#C0392B;color:#fff;padding:12px 28px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;text-decoration:none;letter-spacing:0.04em}.vk-stick-ghost{color:rgba(255,255,255,0.6);font-size:13px;font-weight:500;text-decoration:none;padding:12px 0}@media(max-width:700px){.vk-stick{padding:12px 20px}}</style>
  <div class="vk-stick">
    <div>
      <div class="vk-stick-title">Talk to an Expert</div>
      <div class="vk-stick-sub">Free consultation · No sales pressure · 888-653-1184</div>
    </div>
    <div style="display:flex;gap:12px;align-items:center">
      <a href="#book" class="vk-stick-cta">Book a Consultation</a>
      <a href="tel:+18886531184" class="vk-stick-ghost">Call Now</a>
    </div>
  </div>
  <div style="height:68px"></div>
</div>
"""

INLINE_JS = """\
<script>
  (function() {
    var p = 'audio-consultants';
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
