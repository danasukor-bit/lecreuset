import re, os

BASE = r'c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset'

def get_swatches(href):
    """Extract color-swatch info from product page."""
    path = os.path.join(BASE, href)
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Find all color-swatch elements (span or div), handling any attribute order
    # Extract style, title, and first img url from onclick selectColor
    swatches = []
    for m in re.finditer(
        r'<(?:span|div)\s[^>]*class="color-swatch[^"]*"[^>]*>',
        html
    ):
        tag = m.group(0)
        style_m = re.search(r'style="([^"]*)"', tag)
        title_m = re.search(r'title="([^"]*)"', tag)
        onclick_m = re.search(r"selectColor\(this\s*,\s*'[^']*'\s*,\s*'([^']+)'", tag)
        if not onclick_m:
            onclick_m = re.search(r'selectColor\(this\s*,\s*"[^"]*"\s*,\s*"([^"]+)"', tag)
        if style_m and title_m and onclick_m:
            swatches.append((style_m.group(1), title_m.group(1), onclick_m.group(1)))
    return swatches  # [(style, title, imgurl), ...]

def build_product_colors(cpid, swatches):
    if not swatches:
        return ''
    parts = []
    for i, (style, title, imgurl) in enumerate(swatches):
        active = ' active' if i == 0 else ''
        parts.append(
            f'<span class="swatch{active}" style="{style}" title="{title}" '
            f'onclick="swatchClick(event,this,\'{cpid}\',\'{imgurl}\')"></span>'
        )
    return '        <div class="product-colors">\n          ' + '\n          '.join(parts) + '\n        </div>'

with open(os.path.join(BASE, 'colecao-ceramica.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Find all product-card blocks that have product-card-img but NO product-colors
# Pattern: img id="cpN" in a card without product-colors
# Process card by card
def process_cards(html):
    # Find cards that have img id=cpN but no product-colors nearby
    # Strategy: find each <img id="cpN" pattern, check if product-colors exists before next img
    pattern = re.compile(
        r'(<a href="([^"]+)"><img id="(cp\d+)" src="([^"]+)"[^>]*/></a>\s*)(</div>|<div class="product-wishlist">)',
        re.DOTALL
    )

    def replacer(m):
        full = m.group(0)
        img_part = m.group(1)
        href = m.group(2)
        cpid = m.group(3)
        imgurl = m.group(4)
        after = m.group(5)

        # Check if this card already has product-colors (look backwards)
        start = m.start()
        card_start = html.rfind('<div class="product-card"', 0, start)
        card_chunk = html[card_start:start]
        if 'product-colors' in card_chunk:
            return full  # already has colors

        swatches = get_swatches(href)
        if not swatches:
            return full  # no swatches found

        colors_html = build_product_colors(cpid, swatches)
        return img_part + colors_html + '\n' + after

    return pattern.sub(replacer, html)

new_html = process_cards(html)

with open(os.path.join(BASE, 'colecao-ceramica.html'), 'w', encoding='utf-8') as f:
    f.write(new_html)

# Count how many got colors
added = new_html.count('product-colors') - html.count('product-colors')
print(f'Added product-colors to {added} cards')
