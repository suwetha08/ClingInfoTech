import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    'class="section-spacing reveal" style="background: var(--pastel-red); margin-top: var(--space-12);">',
    'class="section-spacing reveal" style="background: var(--color-brand); margin-top: 0;">'
)

html = html.replace(
    '        <h2>Your Voice, Our Pride!</h2>',
    '        <h2 style="color: white;">Your Voice, Our Pride!</h2>'
)

html = html.replace(
    '        <p>Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>',
    '        <p style="color: rgba(255,255,255,0.9);">Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
