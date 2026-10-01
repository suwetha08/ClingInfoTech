import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = '''<!-- LEADERSHIP TEAM -->
    <section id='team' class='container section-spacing reveal'>
      <div class="reveal delay-300" style="margin-top: var(--space-16);">
        <h2 class="text-center">Leadership Team</h2>
        <div class="bento-grid" style="margin-top: var(--space-8);">
          <div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-8);">
            <img src="ramesh.png" alt="Ramesh Singh" style="width: 100%; max-width: 220px; height: auto; object-fit: contain; margin-bottom: var(--space-6);">
            <h3 style="margin-bottom: var(--space-2);">Ramesh Singh</h3>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin: 0;">Co-founder & Director</p>
          </div>
          <div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-8);">
            <img src="ashi.png" alt="Ashi Gupta" style="width: 100%; max-width: 220px; height: auto; object-fit: contain; margin-bottom: var(--space-6);">
            <h3 style="margin-bottom: var(--space-2);">Ashi Gupta</h3>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin: 0;">Managing Director</p>
          </div>
          <div class="bento-card text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: var(--space-8);">
            <img src="akshay.png" alt="Akshay Gupta" style="width: 100%; max-width: 220px; height: auto; object-fit: contain; margin-bottom: var(--space-6);">
            <h3 style="margin-bottom: var(--space-2);">Akshay Gupta</h3>
            <p style="color: var(--text-muted); font-size: 1.1rem; margin: 0;">CEO</p>
          </div>
        </div>
      </div>\n'''

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines[:534])
    f.write(new_lines)
    f.writelines(lines[553:])
