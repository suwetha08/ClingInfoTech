import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

akshay_block = '''<div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-8);">
            <img src="akshay.png" alt="Akshay Gupta" style="width: 100%; max-width: 220px; height: auto; object-fit: contain; margin-bottom: var(--space-6);">
            <h3 style="margin-bottom: var(--space-2);">Akshay Gupta</h3>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin: 0;">CEO</p>
          </div>'''

numukeh_block = '''<div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-8);">
            <img src="numukeh.png" alt="Numukeh Tunkara" style="width: 100%; max-width: 220px; height: 220px; object-fit: cover; border-radius: 50%; border: 4px solid var(--color-brand); margin-bottom: var(--space-6);">
            <h3 style="margin-bottom: var(--space-2);">Numukeh Tunkara</h3>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin: 0;">Director</p>
          </div>'''

if akshay_block in html:
    html = html.replace(akshay_block, akshay_block + "\n          " + numukeh_block)
else:
    print("Could not find Akshay block exactly. Attempting regex.")
    import re
    # Try regex fallback
    html = re.sub(
        r'(<div class="bento-card[^>]*>.*?<img src="akshay\.png".*?Akshay Gupta.*?</div>)',
        r'\1\n          ' + numukeh_block,
        html,
        flags=re.DOTALL
    )

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
