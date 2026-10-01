import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines 560-563 (0-indexed 559-562):
# 560: <section ...>
# 561:   <h2 style="color: white;">...
# 562:   <p style="...">...
# 563: </div>

new_lines = lines[:560]  # keep everything up to line 560 (0-indexed 559 = the section tag)

# Insert properly centered content
new_lines.append('    <section style="background: var(--color-brand); padding: var(--space-16) 0; margin-top: var(--space-12);">\n')
new_lines.append('      <div class="container text-center mx-auto" style="max-width: 800px; margin-bottom: var(--space-8);">\n')
new_lines.append('        <h2 style="color: white;">Your Voice, Our Pride!</h2>\n')
new_lines.append('        <p style="color: rgba(255,255,255,0.9);">Dive into the heartfelt accounts of our valued patrons. From life-changing experiences to exceptional service, their stories illuminate the essence of our commitment. Your satisfaction is our greatest achievement!</p>\n')
new_lines.append('      </div>\n')
new_lines.append('\n')

# Skip old lines 560-563 (0-indexed 559-562) which are the broken section start + stray h2/p/div
# Continue from line 564 (0-indexed 563) which is the blank line before testimonial-slider
new_lines.extend(lines[564:])

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done!")
