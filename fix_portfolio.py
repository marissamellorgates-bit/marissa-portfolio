import re

with open('public/index.html', 'r') as f:
    html = f.read()

# Fix ALL cdn-cgi email links to mailto
html = re.sub(r'/cdn-cgi/l/email-protection#[a-f0-9]+', 'mailto:marissamellorgates@gmail.com', html)

# Fix nav - change mailto to #contact for the nav link specifically
html = html.replace(
    'href="mailto:marissamellorgates@gmail.com" class="nav-contact">Get in Touch',
    'href="#contact" class="nav-contact">Get in Touch'
)

# Email as visible text (both contact sections)
html = html.replace(
    '<a href="mailto:marissamellorgates@gmail.com" class="contact-link">\u2709 Email</a>',
    '<span class="contact-link" style="cursor:default">\u2709 marissamellorgates@gmail.com</span>'
)

# Remove Cloudflare script
html = html.replace('<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>', '')

# Update LinkedIn
html = html.replace('https://www.linkedin.com/in/marissa-gates-3b38149a', 'https://www.linkedin.com/in/marissa-gates-id')

# Update hero CSS
html = html.replace(
    '.hero{min-height:100vh;display:flex;align-items:center;padding:120px 48px 80px;max-width:1200px;margin:0 auto}.hero-content{max-width:720px}',
    '.hero{min-height:100vh;display:flex;align-items:center;padding:120px 48px 80px}.hero-content{max-width:640px}'
)

# Mobile responsive
html = html.replace(
    '.project-showcase-inner{grid-template-columns:1fr}',
    '.hero-inner{grid-template-columns:1fr!important}.project-showcase-inner{grid-template-columns:1fr}'
)

# New tagline
html = html.replace(
    '<h1 class="fade-in fade-in-delay-1">I design learning that <em>changes behavior</em>, not&nbsp;just checks&nbsp;boxes.</h1>',
    '<h1 class="fade-in fade-in-delay-1">Structured learning, <em>lasting growth.</em></h1>'
)

# Shorten description
html = html.replace(
    'Scenario-based eLearning, compliance simulations, and blended training programs',
    'Scenario-based eLearning, compliance simulations, and blended training'
)
html = html.replace(
    'designed to reduce onboarding time, improve compliance accuracy, and build competency that lasts',
    'designed to build competency that lasts'
)

# Add grid wrapper to hero
html = html.replace(
    '<section class="hero">\n    <div class="hero-content">',
    '<section class="hero">\n    <div class="hero-inner" style="display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;max-width:1200px;margin:0 auto;width:100%">\n      <div class="hero-content">'
)

# Close hero and add highlights
html = html.replace(
    '      </div>\n    </div>\n  </section>\n  <div class="ornament">',
    '''      </div>
      </div>
      <div class="hero-highlights fade-in fade-in-delay-2" style="display:flex;flex-direction:column;gap:28px;padding:40px;background:var(--warm-white);border-radius:12px;border:1px solid var(--sand)">
        <div style="display:flex;align-items:flex-start;gap:16px">
          <span style="font-family:var(--serif);font-size:32px;font-weight:700;color:var(--terracotta);line-height:1">15+</span>
          <div>
            <div style="font-size:14px;font-weight:600;color:var(--espresso)">Years in Learning Design</div>
            <div style="font-size:13px;color:var(--medium);line-height:1.5;margin-top:2px">Corporate, nonprofit, and K\u201312 environments</div>
          </div>
        </div>
        <div style="border-top:1px solid var(--sand)"></div>
        <div style="display:flex;align-items:flex-start;gap:16px">
          <span style="font-family:var(--serif);font-size:32px;font-weight:700;color:var(--terracotta);line-height:1">300+</span>
          <div>
            <div style="font-size:14px;font-weight:600;color:var(--espresso)">Educators Trained</div>
            <div style="font-size:13px;color:var(--medium);line-height:1.5;margin-top:2px">ILT workshops, blended programs, PD institutes</div>
          </div>
        </div>
        <div style="border-top:1px solid var(--sand)"></div>
        <div style="display:flex;align-items:flex-start;gap:16px">
          <span style="font-size:20px;line-height:1.6">\U0001f3af</span>
          <div>
            <div style="font-size:14px;font-weight:600;color:var(--espresso)">Action Mapping & ADDIE</div>
            <div style="font-size:13px;color:var(--medium);line-height:1.5;margin-top:2px">Performance-first design, measurable outcomes</div>
          </div>
        </div>
        <div style="border-top:1px solid var(--sand)"></div>
        <div style="display:flex;align-items:flex-start;gap:16px">
          <span style="font-size:20px;line-height:1.6">\u26a1</span>
          <div>
            <div style="font-size:14px;font-weight:600;color:var(--espresso)">AI-Enhanced Workflow</div>
            <div style="font-size:13px;color:var(--medium);line-height:1.5;margin-top:2px">Claude, ChatGPT, Gemini integrated into development</div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <div class="ornament">''',
    1
)

with open('public/index.html', 'w') as f:
    f.write(html)

print('All fixes applied!')
