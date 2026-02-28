import re

with open('public/index.html', 'r') as f:
    html = f.read()

# 1. Fix ALL cdn-cgi email links to mailto
html = re.sub(r'/cdn-cgi/l/email-protection#[a-f0-9]+', 'mailto:marissamellorgates@gmail.com', html)

# 2. Fix nav Get in Touch - switch to home page then scroll to contact
html = html.replace(
    'href="mailto:marissamellorgates@gmail.com" class="nav-contact">Get in Touch',
    '''href="#" class="nav-contact" onclick="showPage('home');setTimeout(()=>document.getElementById('contact').scrollIntoView({behavior:'smooth'}),100);return false">Get in Touch'''
)

# 3. Replace contact section buttons - email below as highlighted text, no icon
# Home page contact section
html = html.replace(
    '''<a href="mailto:marissamellorgates@gmail.com" class="contact-link">\u2709 Email</a>
        <a href="https://www.linkedin.com/in/marissa-gates-3b38149a" target="_blank" class="contact-link">in LinkedIn</a>
        <a href="Marissa_Gates_Resume.pdf" target="_blank" class="contact-link">Resume (PDF)</a>
      </div>''',
    '''<a href="https://www.linkedin.com/in/marissa-gates-id" target="_blank" class="contact-link">in LinkedIn</a>
        <a href="Marissa_Gates_Resume.pdf" target="_blank" class="contact-link">Resume (PDF)</a>
      </div>
      <div style="margin-top:24px;font-size:18px;font-weight:500;color:var(--terracotta-light);letter-spacing:0.3px;user-select:all;cursor:text">marissamellorgates@gmail.com</div>'''
)

# About page contact section
html = html.replace(
    '''<a href="mailto:marissamellorgates@gmail.com" class="contact-link">\u2709 Email</a>
        <a href="https://www.linkedin.com/in/marissa-gates-3b38149a" target="_blank" class="contact-link">in LinkedIn</a>
        <a href="Marissa_Gates_Resume.pdf" target="_blank" class="contact-link">Resume (PDF)</a>
      </div>''',
    '''<a href="https://www.linkedin.com/in/marissa-gates-id" target="_blank" class="contact-link">in LinkedIn</a>
        <a href="Marissa_Gates_Resume.pdf" target="_blank" class="contact-link">Resume (PDF)</a>
      </div>
      <div style="margin-top:24px;font-size:18px;font-weight:500;color:var(--terracotta-light);letter-spacing:0.3px;user-select:all;cursor:text">marissamellorgates@gmail.com</div>'''
)

# 4. Remove Cloudflare script
html = html.replace('<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>', '')

# 5. Update any remaining old LinkedIn URLs
html = html.replace('https://www.linkedin.com/in/marissa-gates-3b38149a', 'https://www.linkedin.com/in/marissa-gates-id')

# 6. Replace "Let's build something worth learning"
html = html.replace(
    "Let's build something<br>worth learning.",
    "Let's work together."
)

# 7. Update hero CSS
html = html.replace(
    '.hero{min-height:100vh;display:flex;align-items:center;padding:120px 48px 80px;max-width:1200px;margin:0 auto}.hero-content{max-width:720px}',
    '.hero{min-height:100vh;display:flex;align-items:center;padding:120px 48px 80px}.hero-content{max-width:640px}'
)

# 8. Mobile responsive
html = html.replace(
    '.project-showcase-inner{grid-template-columns:1fr}',
    '.hero-inner{grid-template-columns:1fr!important}.hero-highlights{margin-top:32px}.project-showcase-inner{grid-template-columns:1fr}'
)

# 9. New tagline
html = html.replace(
    '<h1 class="fade-in fade-in-delay-1">I design learning that <em>changes behavior</em>, not&nbsp;just checks&nbsp;boxes.</h1>',
    '<h1 class="fade-in fade-in-delay-1">Structured learning, <em>lasting growth.</em></h1>'
)

# 10. Shorten description
html = html.replace(
    'Scenario-based eLearning, compliance simulations, and blended training programs',
    'Scenario-based eLearning, compliance simulations, and blended training'
)
html = html.replace(
    'designed to reduce onboarding time, improve compliance accuracy, and build competency that lasts',
    'designed to build competency that lasts'
)

# 11. Add grid wrapper to hero
html = html.replace(
    '<section class="hero">\n    <div class="hero-content">',
    '<section class="hero">\n    <div class="hero-inner" style="display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;max-width:1200px;margin:0 auto;width:100%">\n      <div class="hero-content">'
)

# 12. Close hero and add philosophy-based value props
html = html.replace(
    '      </div>\n    </div>\n  </section>\n  <div class="ornament">',
    '''      </div>
      </div>
      <div class="hero-highlights fade-in fade-in-delay-2" style="display:flex;flex-direction:column;gap:0;background:var(--warm-white);border-radius:12px;border:1px solid var(--sand);overflow:hidden">
        <div style="padding:32px 36px;border-bottom:1px solid var(--sand)">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#A0522D" stroke-width="2"><path d="M9 18l6-6-6-6"/><path d="M4 12h12"/></svg>
            <div style="font-family:var(--serif);font-size:17px;font-weight:600;color:var(--deep)">Practice Over Presentation</div>
          </div>
          <div style="font-size:14px;color:var(--medium);line-height:1.6">Training that works because learners do the job before they\u2019re on the job.</div>
        </div>
        <div style="padding:32px 36px;border-bottom:1px solid var(--sand)">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#A0522D" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v4m0 12v4M2 12h4m12 0h4"/></svg>
            <div style="font-family:var(--serif);font-size:17px;font-weight:600;color:var(--deep)">Built to Measure</div>
          </div>
          <div style="font-size:14px;color:var(--medium);line-height:1.6">Every design starts with the outcome it needs to prove.</div>
        </div>
        <div style="padding:32px 36px">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#A0522D" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
            <div style="font-family:var(--serif);font-size:17px;font-weight:600;color:var(--deep)">Full Lifecycle, One Designer</div>
          </div>
          <div style="font-size:14px;color:var(--medium);line-height:1.6">Needs analysis through evaluation \u2014 no handoffs, no gaps.</div>
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
