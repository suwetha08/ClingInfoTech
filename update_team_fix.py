import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = '''<!-- LEADERSHIP TEAM -->
    <section id='team' class='container section-spacing reveal'>
      <div class="reveal delay-300" style="margin-top: var(--space-16);">
        <h2 class="text-center">Leadership Team</h2>
        <div class="team-grid">
          <div class="team-card">
            <img class="team-avatar" src="ramesh.png" alt="Ramesh Singh" style="object-fit: cover; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <div><h4>Ramesh Singh</h4><p style="color: var(--text-muted); margin: 0;">Co-founder & Director</p></div>
          </div>
          <div class="team-card">
            <img class="team-avatar" src="ashi.png" alt="Ashi Gupta" style="object-fit: cover; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <div><h4>Ashi Gupta</h4><p style="color: var(--text-muted); margin: 0;">Managing Director</p></div>
          </div>
          <div class="team-card">
            <img class="team-avatar" src="akshay.png" alt="Akshay Gupta" style="object-fit: cover; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <div><h4>Akshay Gupta</h4><p style="color: var(--text-muted); margin: 0;">CEO</p></div>
          </div>
        </div>
      </div>\n'''

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines[:534])
    f.write(new_lines)
    f.writelines(lines[553:])
