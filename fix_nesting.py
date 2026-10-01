import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The team section ends at line 556 (index 555) with </div>
# and then line 557 is blank \r\n
# Testimonials starts at line 558 with <!-- TESTIMONIALS -->
# We need to insert </section> after line 556 to close the team section

# Insert closing </section> for team after line 556 (0-indexed: 555)
# and remove the extra </div> that was the team's closing

# Current structure around 555-558:
# 555: </div>  <-- closes .reveal delay-300
# 556: </div>  <-- (wait, need to recheck)

# From the view: line 556 is "      </div>" and line 557 is blank \r\n
# The team section opened at line 536: <section id='team' ...>
# It needs a </section> to close

# Insert </section> after line 556
new_lines = lines[:556]
new_lines.append('    </section>\n')  # close team section
new_lines.append('\n')
new_lines.append('    <!-- TESTIMONIALS -->\n')
new_lines.append('    <section style="background: var(--color-brand); padding: var(--space-16) 0; margin-top: var(--space-12);">\n')

# Skip original lines 557 (blank \r\n) and 558 (<!-- TESTIMONIALS -->) and 559 (<section ...>)
# Continue from line 560 (the div inside testimonials)
new_lines.extend(lines[560:])

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done!")
