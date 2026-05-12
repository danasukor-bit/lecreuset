import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

OLD_CSS   = '    .product-card { position: relative; }'
NEW_CSS   = '    .product-card { position: relative; text-align: center; transition: transform 0.2s ease; }\n    .product-card:hover { transform: translateY(-4px); }'
OLD_IMG   = '    .product-card-img { position: relative; overflow: hidden; background: #ffffff; aspect-ratio: 1; margin-bottom: 12px; }'
NEW_IMG   = '    .product-card-img { position: relative; overflow: hidden; background: #fff; aspect-ratio: 1; margin-bottom: 14px; }'
OLD_NAME  = '    .product-card-name { font-size: 14px; font-weight: 700; margin-bottom: 4px; }'
NEW_NAME  = '    .product-card-name { font-size: 13px; font-weight: 600; margin-bottom: 4px; color: #111; }'
OLD_PRICE = '    .product-card-price { font-size: 15px; font-weight: 800; }'
NEW_PRICE = '    .product-card-price { font-size: 13px; font-weight: 800; color: #111; margin-bottom: 4px; }'
OLD_SUB   = '    .product-card-sub { font-size: 12px; color: #888; margin-bottom: 6px; }'
NEW_SUB   = '    .product-card-sub { font-size: 11px; color: #999; margin-bottom: 5px; }'

STAR_CSS  = '    .product-card-star { color: #fe5000; font-size: 15px; display: block; margin: 5px 0 8px; }'
BTN_CSS   = ('    .product-card-btn { display: inline-block; padding: 8px 20px; font-size: 10px; font-weight: 800; '
             'letter-spacing: 2px; text-transform: uppercase; border: 1.5px solid #111; color: #111; background: #fff; '
             'transition: all 0.2s; margin-top: 2px; }\n'
             '    .product-card-btn:hover { background: #111; color: #fff; }')

files = [f for f in glob.glob('colecao-*.html') if f != 'colecao-best-sellers.html']
updated = 0

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    if OLD_CSS not in html:
        continue

    # CSS updates
    html = html.replace(OLD_CSS,   NEW_CSS)
    html = html.replace(OLD_IMG,   NEW_IMG)
    html = html.replace(OLD_NAME,  NEW_NAME)
    html = html.replace(OLD_PRICE, NEW_PRICE)
    html = html.replace(OLD_SUB,   NEW_SUB)

    if 'product-card-star' not in html:
        old_sub_price = '    .product-card-price-sub { font-size: 11px; color: #888; }'
        new_sub_price = '    .product-card-price-sub { font-size: 11px; color: #999; }\n' + STAR_CSS + '\n' + BTN_CSS
        html = html.replace(old_sub_price, new_sub_price)

    # Add star after price in HTML (simple string replace, not regex)
    html = html.replace(
        '</div>\n        <div class="product-colors"',
        '\n          <span class="product-card-star">&#9733;</span>\n        </div>\n        <div class="product-colors"'
    )
    # For cards without product-colors
    html = html.replace(
        '<div class="product-card-price">',
        '<div class="product-card-price">'
    )
    # Add star after price where there's no colors div (use marker)
    html = re.sub(
        r'(<div class="product-card-price">[^<]+</div>)\s*\n(\s*</div>\s*\n\s*</div>)',
        lambda m: m.group(1) + '\n          <span class="product-card-star">&#9733;</span>\n' + m.group(2),
        html
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    updated += 1
    print(f'OK {fname}')

print(f'\nDone: {updated}/{len(files)} files updated')
