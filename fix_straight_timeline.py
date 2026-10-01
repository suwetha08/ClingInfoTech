import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_timeline = '''      <!-- TIMELINE -->
      <div class="reveal delay-400">
        <h2 class="text-center" style="margin-bottom: var(--space-12);">A journey as dynamic as us</h2>

        <!-- Straight Timeline -->
        <div style="position: relative; padding: 3rem 0 1rem 0;">

          <!-- Horizontal Line -->
          <div style="position: absolute; top: 3.5rem; left: 0; width: 100%; height: 3px; background: var(--color-brand); z-index: 1;"></div>

          <!-- Items -->
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4);">

            <!-- 2019 -->
            <div style="position: relative; display: flex; flex-direction: column; align-items: center;">
              <!-- Dot -->
              <div style="width: 18px; height: 18px; border-radius: 50%; background: white; border: 3px solid var(--color-brand); z-index: 2; margin-bottom: 1.5rem; flex-shrink: 0;"></div>
              <!-- Card -->
              <div style="background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; text-align: center;">
                <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.4rem; color: white; margin-bottom: 0.5rem;">2019</div>
                <p style="font-size: 0.9rem; margin: 0; color: rgba(255,255,255,0.9);">A year of foundational growth and learning, we focused on building a strong foundation and establishing our identity.</p>
              </div>
            </div>

            <!-- 2020 -->
            <div style="position: relative; display: flex; flex-direction: column; align-items: center;">
              <div style="width: 18px; height: 18px; border-radius: 50%; background: white; border: 3px solid var(--color-brand); z-index: 2; margin-bottom: 1.5rem; flex-shrink: 0;"></div>
              <div style="background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; text-align: center;">
                <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.4rem; color: white; margin-bottom: 0.5rem;">2020</div>
                <p style="font-size: 0.9rem; margin: 0; color: rgba(255,255,255,0.9);">Solidifying our presence, we diversified our services and remained committed to quality and customer satisfaction.</p>
              </div>
            </div>

            <!-- 2021 -->
            <div style="position: relative; display: flex; flex-direction: column; align-items: center;">
              <div style="width: 18px; height: 18px; border-radius: 50%; background: white; border: 3px solid var(--color-brand); z-index: 2; margin-bottom: 1.5rem; flex-shrink: 0;"></div>
              <div style="background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; text-align: center;">
                <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.4rem; color: white; margin-bottom: 0.5rem;">2021</div>
                <p style="font-size: 0.9rem; margin: 0; color: rgba(255,255,255,0.9);">We gained momentum and recognition, expanding our client base and embracing new technologies and methodologies.</p>
              </div>
            </div>

            <!-- 2022 -->
            <div style="position: relative; display: flex; flex-direction: column; align-items: center;">
              <div style="width: 18px; height: 18px; border-radius: 50%; background: white; border: 3px solid var(--color-brand); z-index: 2; margin-bottom: 1.5rem; flex-shrink: 0;"></div>
              <div style="background: var(--color-brand); padding: 1.5rem; border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; text-align: center;">
                <div style="font-family: var(--font-display); font-weight: 800; font-size: 1.4rem; color: white; margin-bottom: 0.5rem;">2022</div>
                <p style="font-size: 0.9rem; margin: 0; color: rgba(255,255,255,0.9);">A milestone year, we grew into a matured organization, taking on ambitious projects and delivering greater value.</p>
              </div>
            </div>

          </div>
        </div>
      </div>

'''

new_lines = lines[:415]
new_lines.append(new_timeline)
new_lines.extend(lines[459:])

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done!")
