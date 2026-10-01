import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navigation Links
old_nav = '''      <ul class="nav-links">
        <li><a href="https://clinginfotech.com/">Home</a></li>
        <li><a href="#about">About Us</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#solutions">Solutions</a></li>
        <li><a href="#resources">Resources</a></li>
        <li><a href="https://clinginfotech.com/clients">Clients</a></li>
      </ul>'''

new_nav = '''      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About Us</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#solutions">Solutions</a></li>
        <li><a href="#resources">Resources</a></li>
        <li><a href="#clients">Clients</a></li>
      </ul>'''
html = html.replace(old_nav, new_nav)


# 2. Add id="home" to Hero
html = html.replace('<section class="container hero reveal">', '<section id="home" class="container hero reveal">')


# 3. Add id="about" to Core Identity
# The HTML is `<section class="container section-spacing reveal">` just before `<h2>Our Core Identity</h2>`
html = html.replace(
    '<section class="container section-spacing reveal">\n      <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-12);">\n        <h2>Our Core Identity</h2>',
    '<section id="about" class="container section-spacing reveal">\n      <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-12);">\n        <h2>Our Core Identity</h2>'
)

# Services already has id="services" (<section id="services" class="container reveal")


# 4. Add id="solutions" to Tech Focus
# The HTML has `<section style="background: #ffebeb;">` just before `<div class="container">...<h2>Current Tech Focus</h2>`
html = html.replace(
    '<section style="background: #ffebeb;">\n  <div class="container">\n  <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-12);">\n    <h2>Current Tech Focus</h2>',
    '<section id="solutions" style="background: #ffebeb;">\n  <div class="container">\n  <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-12);">\n    <h2>Current Tech Focus</h2>'
)


# 5. Add id="clients" to Testimonials
# The HTML is `<section style="background: #ffebeb; padding: var(--space-16) 0; margin-top: var(--space-12);">` before `<h2>Your Voice, Our Pride!</h2>`
html = html.replace(
    '<section style="background: #ffebeb; padding: var(--space-16) 0; margin-top: var(--space-12);">\n      <div class="container text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-8);">\n        <h2 style="color: var(--color-dark);">Your Voice, Our Pride!</h2>',
    '<section id="clients" style="background: #ffebeb; padding: var(--space-16) 0; margin-top: var(--space-12);">\n      <div class="container text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-8);">\n        <h2 style="color: var(--color-dark);">Your Voice, Our Pride!</h2>'
)


with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
