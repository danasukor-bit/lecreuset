import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

# ─── 1. Remove collection page titles ───
colecao_files = sorted(Path('.').glob('colecao-*.html'))
title_removed = 0
for f in colecao_files:
    text = f.read_text(encoding='utf-8')
    orig = text

    # Remove the entire collection-page-header div
    text = re.sub(
        r'\s*<div class="collection-page-header">\s*<h1 class="collection-page-title">[^<]*</h1>\s*</div>\s*',
        '\n',
        text
    )

    if text != orig:
        f.write_text(text, encoding='utf-8')
        title_removed += 1

print(f"Titles removed: {title_removed} collection pages")

# ─── 2. Add cart.js + onclick to all product pages with btn-cart ───
all_html = sorted(Path('.').glob('*.html'))
cart_updated = 0
badge_updated = 0

for f in all_html:
    if f.name in ('carrinho.html', 'checkout.html'):
        continue

    text = f.read_text(encoding='utf-8')
    orig = text
    changed = False

    # Add onclick="addToCart()" to btn-cart if not already present
    if 'class="btn-cart"' in text and 'addToCart' not in text:
        text = text.replace(
            '<button class="btn-cart">Adicionar ao Carrinho</button>',
            '<button class="btn-cart" onclick="addToCart()">Adicionar ao Carrinho</button>'
        )
        changed = True

    # Add cart.js script tag before </body> if not already present
    if 'cart.js' not in text and ('btn-cart' in text or 'header-icons' in text):
        text = text.replace('</body>', '<script src="cart.js"></script>\n</body>', 1)
        changed = True

    if changed and text != orig:
        f.write_text(text, encoding='utf-8')
        cart_updated += 1

print(f"Cart JS added: {cart_updated} pages")
print("Done.")
