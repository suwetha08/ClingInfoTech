import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix background: solid red -> light red
html = html.replace(
    'style="background: var(--color-brand); padding: var(--space-16) 0; margin-top: var(--space-12);"',
    'style="background: #ffebeb; padding: var(--space-16) 0; margin-top: var(--space-12);"'
)

# 2. Fix testimonial card CSS - add padding-top so avatar isn't clipped, make card smaller
html = html.replace(
    '.testimonial-card { flex: 0 0 450px; scroll-snap-align: center; background: var(--bg-surface); padding: var(--space-8) var(--space-6) var(--space-6); border: 1px solid var(--border-light); border-radius: 24px; box-shadow: var(--shadow-md); position: relative; text-align: center; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.3s; }',
    '.testimonial-card { flex: 0 0 350px; scroll-snap-align: center; background: var(--bg-surface); padding: 60px var(--space-5) var(--space-5); border: 1px solid var(--border-light); border-radius: 20px; box-shadow: var(--shadow-md); position: relative; text-align: center; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.3s; overflow: visible; }'
)

# 3. Fix avatar - position it centered at the top of the card
html = html.replace(
    '.testimonial-avatar { width: 80px; height: 80px; background: var(--color-brand); color: white; border-radius: 50%; display: flex; align-items: center; jus',
    '.testimonial-avatar { width: 70px; height: 70px; background: var(--color-brand); color: white; border-radius: 50%; display: flex; align-items: center; jus'
)

# Also make the slide wrapper overflow visible so avatar shows above card
html = html.replace(
    'class="testimonial-carousel-wrapper" style="position: relative; overflow: hidden;',
    'class="testimonial-carousel-wrapper" style="position: relative; overflow: hidden; padding-top: 40px;'
)

# Fix each card in the carousel - add margin-top to make space for avatar above card
html = html.replace(
    'class="testimonial-slide" style="min-width: 100%; display: flex; gap: 2rem; padding: 0 5%;"',
    'class="testimonial-slide" style="min-width: 100%; display: flex; gap: 1.5rem; padding: 40px 5% 0 5%; align-items: flex-start;"'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
