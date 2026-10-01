import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update 2020 Box
old_2020 = '''<div style="margin-top: auto; background: var(--bg-surface); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-light); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
<div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2020</div>
<p style="font-size: 0.95rem; margin: 0 auto; color: var(--text-muted);">Solidifying our presence, we diversified our services and remained committed to quality and customer satisfaction.</p>
</div>'''

new_2020 = '''<div style="margin-top: auto; background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
<div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: white; margin-bottom: 0.5rem;">2020</div>
<p style="font-size: 0.95rem; margin: 0 auto; color: rgba(255,255,255,0.9);">Solidifying our presence, we diversified our services and remained committed to quality and customer satisfaction.</p>
</div>'''

html = html.replace(old_2020, new_2020)

# 2. Update 2022 Box
old_2022 = '''<div style="margin-top: auto; background: var(--bg-surface); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-light); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
<div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2022</div>
<p style="font-size: 0.95rem; margin: 0 auto; color: var(--text-muted);">A milestone year, we grew into a matured organization, taking on ambitious projects and delivering greater value.</p>
</div>'''

new_2022 = '''<div style="margin-top: auto; background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
<div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: white; margin-bottom: 0.5rem;">2022</div>
<p style="font-size: 0.95rem; margin: 0 auto; color: rgba(255,255,255,0.9);">A milestone year, we grew into a matured organization, taking on ambitious projects and delivering greater value.</p>
</div>'''

html = html.replace(old_2022, new_2022)


# 3. Update Testimonials
old_test = '''    <!-- TESTIMONIALS -->
    <section class="section-spacing reveal" style="background: var(--pastel-red); margin-top: var(--space-12);">
      <div class="container text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-4);">
        <h2>Your Voice, Our Pride!</h2>
        <p>Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>
      </div>'''

new_test = '''    <!-- TESTIMONIALS -->
    <section class="section-spacing reveal" style="background: var(--color-brand); margin-top: var(--space-12);">
      <div class="container text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-4);">
        <h2 style="color: white;">Your Voice, Our Pride!</h2>
        <p style="color: rgba(255,255,255,0.9);">Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>
      </div>'''

html = html.replace(old_test, new_test)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
