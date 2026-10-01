import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_timeline = '''    <!-- TIMELINE -->
    <section class="section-spacing" style="background: var(--pastel-red);">'''
new_timeline = '''    <!-- TIMELINE -->
    <section class="section-spacing" style="background: #ffebeb;">'''

old_ai = '''<!-- AI & 3D -->
<section id="ai" class="section-spacing reveal" style="background: var(--pastel-red);">'''
new_ai = '''<!-- AI & 3D -->
<section id="ai" class="section-spacing reveal" style="background: #ffebeb;">'''

html = html.replace(old_timeline, new_timeline)
html = html.replace(old_ai, new_ai)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
