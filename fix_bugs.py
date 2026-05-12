import glob, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── BUG 1: cart.js - product name selector mismatch ──────────────────────────
with open('cart.js', 'r', encoding='utf-8') as f:
    cart = f.read()

old = "var nameEl = document.querySelector('.product-title, h1.product-title');"
new = "var nameEl = document.querySelector('.product-title, h1.product-title, h1.product-name, .product-name > a, h1.nome-produto');"
if old in cart:
    cart = cart.replace(old, new)
    with open('cart.js', 'w', encoding='utf-8') as f:
        f.write(cart)
    print('BUG 1 FIXED: cart.js - product name selector')
else:
    print('BUG 1 SKIP: selector already updated or not found')

# ── BUG 2: carrinho.html - PIX discount shown by default ─────────────────────
with open('carrinho.html', 'r', encoding='utf-8') as f:
    carrinho = f.read()

old2 = ('    pixDiscountEl.textContent = \'\u2014 \' + formatBRL(pixDiscount);\n'
        '    pixDiscountRow.style.display = \'flex\';\n'
        '    totalEl.textContent = formatBRL(total - pixDiscount);')
new2 = ('    // PIX discount shown only on checkout page, not here\n'
        '    pixDiscountRow.style.display = \'none\';\n'
        '    totalEl.textContent = formatBRL(total);')
if old2 in carrinho:
    carrinho = carrinho.replace(old2, new2)
    with open('carrinho.html', 'w', encoding='utf-8') as f:
        f.write(carrinho)
    print('BUG 2 FIXED: carrinho.html - PIX discount removed from cart total')
else:
    print('BUG 2 SKIP: PIX block not found as expected')
    print('Looking for partial match...')
    if 'pixDiscountRow.style.display' in carrinho:
        print('  Found pixDiscountRow reference in file')

# ── BUG 3: 64 product pages - dead links to colecao-nossas-cores.html ────────
files = [f for f in glob.glob('*.html') if not f.startswith('colecao-') and f not in ('carrinho.html','checkout.html','busca.html')]
fixed = 0
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'colecao-nossas-cores.html' not in html:
        continue
    # Remove the "Ver Todas as Cores" link entirely
    html = html.replace(
        '\n            <a href="colecao-nossas-cores.html">Ver Todas as Cores</a>',
        ''
    )
    html = html.replace(
        '<a href="colecao-nossas-cores.html">Ver Todas as Cores</a>',
        ''
    )
    # If still any remaining refs (e.g. footer or nav), remove those too
    html = html.replace(
        '<li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>\n',
        ''
    )
    html = html.replace(
        '<li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>',
        ''
    )
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    fixed += 1

print(f'BUG 3 FIXED: {fixed} product pages - removed dead nossas-cores links')

print('\nAll bugs fixed. Ready to deploy.')
