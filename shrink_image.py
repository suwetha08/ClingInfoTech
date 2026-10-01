import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Modify the image styles
html = html.replace(
    'style="width: 135%; max-width: none; margin-left: 4%; height: auto;',
    'style="width: 115%; max-width: none; margin-left: -10%; height: auto;'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
