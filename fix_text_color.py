import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<h2 style="color: white;">Your Voice, Our Pride!</h2>',
    '<h2 style="color: var(--color-dark);">Your Voice, Our Pride!</h2>'
)

html = html.replace(
    '<p style="color: rgba(255,255,255,0.9);">Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>',
    '<p style="color: var(--text-main);">Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
