import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_ai = '''<!-- AI & 3D -->
<section id="ai" class="container section-spacing reveal">
  <div class="text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-12);">
    <h2>Current Tech Focus</h2>
    <p class="mx-auto">Innovations At Its best, is what we believe in.</p>
  </div>

  <div class="bento-grid">
    <!-- Video Card 1 -->
    <div class="bento-card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <div style="width: 100%; aspect-ratio: 16/9; background: var(--border-light); position: relative; display: flex; align-items: center; justify-content: center;">
         <!-- Placeholder for video -->
         <svg style="width: 48px; height: 48px; color: var(--text-muted);" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
      </div>
      <div style="padding: var(--space-6); text-align: left;">
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-brand); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">3D Animation</div>
        <h3 style="margin-bottom: 0; font-size: 1.25rem;">Cling Logo animation</h3>
      </div>
    </div>

    <!-- Video Card 2 -->
    <div class="bento-card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <div style="width: 100%; aspect-ratio: 16/9; background: var(--border-light); position: relative; display: flex; align-items: center; justify-content: center;">
         <!-- Placeholder for video -->
         <svg style="width: 48px; height: 48px; color: var(--text-muted);" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
      </div>
      <div style="padding: var(--space-6); text-align: left;">
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-brand); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">3D Animation</div>
        <h3 style="margin-bottom: 0; font-size: 1.25rem;">Advertisement video</h3>
      </div>
    </div>

    <!-- Video Card 3 -->
    <div class="bento-card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <div style="width: 100%; aspect-ratio: 16/9; background: var(--border-light); position: relative; display: flex; align-items: center; justify-content: center;">
         <!-- Placeholder for video -->
         <svg style="width: 48px; height: 48px; color: var(--text-muted);" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
      </div>
      <div style="padding: var(--space-6); text-align: left;">
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-brand); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">AI</div>
        <h3 style="margin-bottom: 0.5rem; font-size: 1.25rem;">The Surveillance Model</h3>
        <p style="font-size: 0.95rem; margin: 0; color: var(--text-muted); line-height: 1.4;">Identifies suspicious activity in the video.</p>
      </div>
    </div>
  </div>
</section>
'''

start_idx = html.find('<!-- AI & 3D -->')
end_idx = html.find('<!-- LEADERSHIP TEAM -->', start_idx)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_ai + html[end_idx:]

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
