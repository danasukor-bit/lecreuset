import re, os

files = sorted([f for f in os.listdir('.') if f.startswith('colecao-') and f.endswith('.html')])

css_block = """    /* ─── COLLECTION PAGE TITLE ─── */
    .collection-page-header { text-align: center; padding: 32px 24px 20px; border-bottom: 1px solid #e5e5e5; margin-bottom: 0; }
    .collection-page-title {
      font-size: 36px; font-weight: 800; letter-spacing: -0.5px;
      background: linear-gradient(90deg, #c8102e 0%, #d46820 25%, #2DBECD 55%, #9B7EB0 80%, #2060A0 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text; display: inline-block;
    }
    @media(max-width:768px) { .collection-page-title { font-size: 26px; } .collection-page-header { padding: 20px 16px 16px; } }"""

fixed = 0
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get collection name from <title>
    m = re.search(r'<title>([^|<]+)(?:\|)', content)
    if not m:
        continue
    col_name = m.group(1).strip()

    # Skip if already has collection-page-header
    if 'collection-page-header' in content:
        continue

    # Add CSS before </style>
    if css_block not in content:
        content = content.replace('  </style>', css_block + '\n  </style>', 1)

    # Build title HTML
    title_html = '\n<div class="collection-page-header">\n  <h1 class="collection-page-title">' + col_name + '</h1>\n</div>\n'

    # Insert after </div> that closes cat-banner, before <nav class="breadcrumb"> or <div class="collection-wrap"> or <div class="shop-layout">
    inserted = False
    for marker in ['</div>\n\n<nav class="breadcrumb">', '</div>\n\n<div class="collection-wrap">', '</div>\n\n<div class="shop-layout">']:
        if marker in content:
            content = content.replace(marker, '</div>\n' + title_html + '\n<' + marker.split('<')[1], 1)
            inserted = True
            break

    if not inserted:
        # fallback: after first cat-banner closing div
        idx = content.find('</div>', content.find('cat-banner'))
        if idx > 0:
            content = content[:idx+6] + title_html + content[idx+6:]
            inserted = True

    if inserted:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed += 1
        print(f'OK: {fname} -> {col_name}')
    else:
        print(f'SKIP: {fname}')

print(f'\nTotal: {fixed} paginas atualizadas')
