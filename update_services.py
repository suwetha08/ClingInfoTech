import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_services = '''<!-- SERVICES -->
<section id="services" class="container section-spacing reveal">
<div class="text-center mx-auto reveal">
<h2>Our Services</h2>
<p class="mx-auto">Tailored services for all your business needs.</p>
</div>

<div class="bento-grid reveal delay-100" style="margin-top: var(--space-8);">
<div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; padding: var(--space-8);">
<img src="service-app.png" alt="App Development" style="width: 200px; height: 150px; object-fit: contain; margin-bottom: var(--space-6);">
<h3 style="margin-bottom: var(--space-4);">App Development</h3>
<p style="margin: 0;">Need custom app development services? We help you take advantage of the rapidly growing segment of mobile application development.</p>
</div>
<div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; padding: var(--space-8);">
<img src="service-web.png" alt="Web Design" style="width: 200px; height: 150px; object-fit: contain; margin-bottom: var(--space-6);">
<h3 style="margin-bottom: var(--space-4);">Web Design</h3>
<p style="margin: 0;">Don't let your website be just another URL on the web! All design layouts are developed from ground up, meeting the exacting standards you demand.</p>
</div>
<div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; padding: var(--space-8);">
<img src="service-erp.png" alt="Enterprise ERPs" style="width: 200px; height: 150px; object-fit: contain; margin-bottom: var(--space-6);">
<h3 style="margin-bottom: var(--space-4);">Enterprise ERPs</h3>
<p style="margin: 0;">We help you to manage your business activities by integrating your back and front office applications seamlessly.</p>
</div>
</div>
</section>'''

start_idx = html.find('<!-- SERVICES -->')
end_idx = html.find('</section>', start_idx) + len('</section>')

html = html[:start_idx] + new_services + html[end_idx:]

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
