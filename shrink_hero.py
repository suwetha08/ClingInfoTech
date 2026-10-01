import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the wrapper div's margin-left from -2rem to -4rem to move it further left
html = html.replace(
    '<div style="margin-top: -2rem; margin-left: -2rem; padding-right: 2rem;">',
    '<div style="margin-top: -2rem; margin-left: -4rem; padding-right: 2rem; max-width: 95%;">'
)

# 2. Reduce the size of the H1 heading
html = html.replace(
    '<h1 class="reveal delay-100">Making Your Ideas Happen!</h1>',
    '<h1 class="reveal delay-100" style="font-size: clamp(2.5rem, 4.5vw, 4rem); margin-bottom: 1rem;">Making Your Ideas Happen!</h1>'
)

# 3. Slightly reduce the paragraph size and line height so it matches the smaller heading nicely
html = html.replace(
    '<p class="reveal delay-200">We are an end-to-end IT Solutions providing major services such as website development, mobile application development, digital marketing, custom web portal, IT team for your next idea, ERP development, for all your business needs.</p>',
    '<p class="reveal delay-200" style="font-size: 1.05rem; line-height: 1.6; max-width: 90%;">We are an end-to-end IT Solutions providing major services such as website development, mobile application development, digital marketing, custom web portal, IT team for your next idea, ERP development, for all your business needs.</p>'
)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
