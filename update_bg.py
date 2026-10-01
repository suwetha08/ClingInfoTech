import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_timeline_start = '''      </div>

      <!-- TIMELINE -->
      <div class="reveal delay-400">'''
new_timeline_start = '''      </div>
    </section>

    <!-- TIMELINE -->
    <section class="section-spacing" style="background: var(--pastel-red);">
      <div class="container reveal delay-400">'''

old_timeline_end = '''</section>
<!-- SERVICES -->'''
new_timeline_end = '''</div>
</section>
<!-- SERVICES -->'''

html = html.replace(old_timeline_start, new_timeline_start)
html = html.replace(old_timeline_end, new_timeline_end)

old_ai_start = '''<!-- AI & 3D -->
<section id="ai" class="container section-spacing reveal">'''
new_ai_start = '''<!-- AI & 3D -->
<section id="ai" class="section-spacing reveal" style="background: var(--pastel-red);">
  <div class="container">'''

old_ai_end = '''</section>
<!-- LEADERSHIP TEAM -->'''
new_ai_end = '''  </div>
</section>
<!-- LEADERSHIP TEAM -->'''

html = html.replace(old_ai_start, new_ai_start)
html = html.replace(old_ai_end, new_ai_end)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
