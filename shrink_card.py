import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Scale down the picker card as well to match the reduced text size
html = html.replace(
    '<div class="picker-card reveal delay-300">',
    '<div class="picker-card reveal delay-300" style="transform: scale(0.95); transform-origin: left top; margin-top: 1rem;">'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
