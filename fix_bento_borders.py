import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the bento-card CSS
old_css = """.bento-card {
      background: var(--pastel-red) !important;
      border: 1px solid rgba(237, 28, 36, 0.08) !important;
      text-align: left !important;
    }"""

new_css = """.bento-card {
      background: white !important;
      border: 1px solid rgba(237, 28, 36, 0.15) !important; /* Red border */
      text-align: left !important;
    }"""

if old_css in html:
    html = html.replace(old_css, new_css)
else:
    # Just in case there's whitespace difference
    import re
    html = re.sub(r'\.bento-card\s*\{[^}]+\}', new_css, html)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
