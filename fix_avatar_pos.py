import codecs

with codecs.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS override to position avatar absolutely at top center of card
avatar_fix = """
    .testimonial-card { overflow: visible !important; }
    .testimonial-avatar { position: absolute !important; top: -35px !important; left: 50% !important; transform: translateX(-50%) !important; margin: 0 !important; z-index: 5 !important; box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important; }
"""

# Insert before </style>
html = html.replace('</style>\n  </head>', avatar_fix + '\n  </style>\n  </head>', 1)

with codecs.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
