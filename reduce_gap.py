import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Clientele section
old_clientele = '<section class="container section-spacing reveal" style="padding-top: var(--space-4); margin-bottom: var(--space-8);">'
new_clientele = '<section class="container reveal" style="padding-top: var(--space-4); padding-bottom: var(--space-8);">'
html = html.replace(old_clientele, new_clientele)

# Fix Core Identity section padding-top
old_about = '<section id="about" class="container section-spacing reveal">'
new_about = '<section id="about" class="container section-spacing reveal" style="padding-top: var(--space-4);">'
html = html.replace(old_about, new_about)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
