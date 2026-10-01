with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2019 (Red Box)
old_1 = '''            <div style="margin-bottom: auto; padding-bottom: 20px;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2019</div>
              <p style="font-size: 0.95rem; margin: 0 auto; max-width: 250px;">A year of foundational growth and learning, we focused on building a strong foundation and establishing our identity.</p>
            </div>'''
new_1 = '''            <div style="margin-bottom: auto; background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: white; margin-bottom: 0.5rem;">2019</div>
              <p style="font-size: 0.95rem; margin: 0 auto; color: rgba(255,255,255,0.9);">A year of foundational growth and learning, we focused on building a strong foundation and establishing our identity.</p>
            </div>'''

# 2020 (White Box)
old_2 = '''            <div style="margin-top: auto; padding-top: 20px;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2020</div>
              <p style="font-size: 0.95rem; margin: 0 auto; max-width: 250px;">Solidifying our presence, we diversified our services and remained committed to quality and customer satisfaction.</p>
            </div>'''
new_2 = '''            <div style="margin-top: auto; background: var(--bg-surface); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-light); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2020</div>
              <p style="font-size: 0.95rem; margin: 0 auto; color: var(--text-muted);">Solidifying our presence, we diversified our services and remained committed to quality and customer satisfaction.</p>
            </div>'''

# 2021 (Red Box)
old_3 = '''            <div style="margin-bottom: auto; padding-bottom: 20px;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2021</div>
              <p style="font-size: 0.95rem; margin: 0 auto; max-width: 250px;">We gained momentum and recognition, expanding our client base and embracing new technologies and methodologies.</p>
            </div>'''
new_3 = '''            <div style="margin-bottom: auto; background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: white; margin-bottom: 0.5rem;">2021</div>
              <p style="font-size: 0.95rem; margin: 0 auto; color: rgba(255,255,255,0.9);">We gained momentum and recognition, expanding our client base and embracing new technologies and methodologies.</p>
            </div>'''

# 2022 (White Box)
old_4 = '''            <div style="margin-top: auto; padding-top: 20px;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2022</div>
              <p style="font-size: 0.95rem; margin: 0 auto; max-width: 250px;">A milestone year, we grew into a matured organization, taking on ambitious projects and delivering greater value.</p>
            </div>'''
new_4 = '''            <div style="margin-top: auto; background: var(--bg-surface); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-light); z-index: 2; margin-left: 1rem; margin-right: 1rem; position: relative;">
              <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.5rem; color: var(--color-dark); margin-bottom: 0.5rem;">2022</div>
              <p style="font-size: 0.95rem; margin: 0 auto; color: var(--text-muted);">A milestone year, we grew into a matured organization, taking on ambitious projects and delivering greater value.</p>
            </div>'''

html = html.replace(old_1, new_1)
html = html.replace(old_2, new_2)
html = html.replace(old_3, new_3)
html = html.replace(old_4, new_4)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
