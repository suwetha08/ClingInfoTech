import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the specific grid for the Leadership team
target_section = 'Leadership Team</h2>\n        <div class="bento-grid" style="margin-top: var(--space-8);">'
replacement = 'Leadership Team</h2>\n        <div class="bento-grid" style="margin-top: var(--space-8); grid-template-columns: repeat(4, 1fr);">'

if target_section in html:
    html = html.replace(target_section, replacement)
else:
    import re
    # Try regex if exact match fails
    html = re.sub(
        r'(Leadership Team</h2>\s*<div class="bento-grid"[^>]*style="[^"]*)(">)',
        r'\1; grid-template-columns: repeat(4, 1fr);\2',
        html
    )

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
