import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 2020 box - white to red
html = html.replace(
    'margin-top: auto; background: var(--bg-surface); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-light); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">',
    'margin-top: auto; background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">'
)

# Fix 2020 year text color
html = html.replace(
    'font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2020',
    'font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: white; margin-bottom: 0.5rem;">2020'
)
html = html.replace(
    'font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2022',
    'font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: white; margin-bottom: 0.5rem;">2022'
)

# Fix 2020 and 2022 paragraph text color
html = html.replace(
    'font-size: 0.95rem; margin: 0 auto; color: var(--text-muted);">Solidifying',
    'font-size: 0.95rem; margin: 0 auto; color: rgba(255,255,255,0.9);">Solidifying'
)
html = html.replace(
    'font-size: 0.95rem; margin: 0 auto; color: var(--text-muted);">A milestone',
    'font-size: 0.95rem; margin: 0 auto; color: rgba(255,255,255,0.9);">A milestone'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
