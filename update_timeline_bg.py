import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_timeline = '''    <!-- TIMELINE -->
    <section class="section-spacing" style="background: #ffebeb;">'''
new_timeline = '''    <!-- TIMELINE -->
    <section class="section-spacing" style="background: var(--pastel-red);">'''

html = html.replace(old_timeline, new_timeline)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
