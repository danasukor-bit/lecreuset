import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

# CSS to add - limits dots to 5, styles "+N" badge
EXTRA_CSS = """
    .product-color-dot:nth-child(n+6) { display: none; }
    .color-more { font-size: 11px; font-weight: 700; color: #555; align-self: center; margin-left: 2px; }"""

# JS to add before </script> (the cart.js script tag area) - counts hidden dots and adds "+N"
EXTRA_JS = """
  // Limit color dots to 5 + show "+N" badge
  document.querySelectorAll('.product-colors').forEach(function(wrap) {
    var dots = wrap.querySelectorAll('.product-color-dot');
    if (dots.length > 5) {
      var more = document.createElement('span');
      more.className = 'color-more';
      more.textContent = '+' + (dots.length - 5);
      wrap.appendChild(more);
    }
  });
"""

files = glob.glob('colecao-*.html')
updated = 0

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'product-color-dot' not in html:
        continue
    if 'color-more' in html:
        continue  # already done

    # Add CSS before </style> (first occurrence)
    html = html.replace('</style>', EXTRA_CSS + '\n  </style>', 1)

    # Add JS before </body>
    html = html.replace('</body>', EXTRA_JS + '</body>', 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    updated += 1
    print(f'OK {fname}')

print(f'\nDone: {updated} files updated')
