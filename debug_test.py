import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check what's actually there
idx = html.find('TESTIMONIALS')
print(repr(html[idx-10:idx+300]))
