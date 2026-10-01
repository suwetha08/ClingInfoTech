import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add margin to the div wrapping the hero text and card
html = html.replace(
    '<section class="container hero reveal">\n      <div>',
    '<section class="container hero reveal">\n      <div style="margin-top: -2rem; margin-left: -2rem; padding-right: 2rem;">'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
