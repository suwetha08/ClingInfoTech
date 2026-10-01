import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: The section has the red but it's nested inside a .container wrapper 
# from the parent section. We need to check if there's a wrapping container.
# Also fix the margin-top to give space after leadership team.
html = html.replace(
    'class="section-spacing reveal" style="background: var(--color-brand); margin-top: 0;">',
    'style="background: var(--color-brand); padding: var(--space-16) 0; margin-top: var(--space-12);">'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
