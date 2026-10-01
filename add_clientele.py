import codecs

clients = [
    "Verified Property Intelligence", "MAT Commercial Vehicle Products", "SSCL ERP", 
    "SRS Manpower ERP", "Sunshine", "Jumpie", "Delhi Public International School", 
    "Indian Racing Festival", "Seymour Management", "Omsons India Handicraft", 
    "Kirana Quick Technologies Private Limited", "SOLIDARITY ADVISORS PRIVATE LIMITED", 
    "CP67", "Capital Curve", "FDX Group", "Kalco", "Bhojras", "Wings Rehabilitation Center", 
    "Airdrop JA", "NK Architects", "Vestiary", "Skuad", "Piaah", "Forescribe", "Apptrove", 
    "BeatRoute", "Phonologix Therapy", "Kite Digiceutix", "E-Pay Later", "Astro Reader", 
    "Sagitta", "Viral Hai", "Matrix Solutions", "Parashar", "Vakeel at Home", "Papertio", 
    "MatchMe Global", "Mint HR"
]

chips_html = ""
for client in clients:
    chips_html += f'<div style="background: white; border: 1px solid var(--color-brand-light); color: var(--color-dark); padding: 0.5rem 1.25rem; border-radius: 99px; font-weight: 500; font-size: 0.95rem; box-shadow: 0 4px 6px rgba(237,28,36,0.05); cursor: default; transition: transform 0.2s;" onmouseover="this.style.transform=\'scale(1.05)\'" onmouseout="this.style.transform=\'scale(1)\'">{client}</div>\n        '

section_html = f'''
    <!-- OUR DIVERSE CLIENTELE -->
    <section class="container section-spacing reveal" style="padding-top: var(--space-4); margin-bottom: var(--space-8);">
      <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-8);">
        <h2>Our Diverse Clientele</h2>
        <p class="mx-auto">We are proud to have collaborated with an incredible array of organizations and brands to bring their visions to life.</p>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; justify-content: center; align-items: center; max-width: 1100px; margin: 0 auto;">
        {chips_html}
      </div>
    </section>

    <!-- COMPANY / ABOUT US -->
'''

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert before "<!-- COMPANY / ABOUT US -->" which is just before "Our Core Identity"
# Wait, let's just find '<section id="about"' and insert right before it.
target = '<section id="about"'

if target in html:
    html = html.replace(target, section_html + target)
else:
    # Fallback to without id
    target2 = '<section class="container section-spacing reveal">\n      <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-12);">\n        <h2>Our Core Identity</h2>'
    html = html.replace(target2, section_html + target2)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
