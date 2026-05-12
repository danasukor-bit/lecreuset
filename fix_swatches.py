import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

# ─── 1. Fix panela-redonda-signature.html: add background-color fallbacks ───
file = Path("panela-redonda-signature.html")
content = file.read_text(encoding='utf-8')

color_map = {
    'Laranja':      '#d46820',
    'Vermelho':     '#c8102e',
    'Bleu Riviera': '#2DBECD',
    'Azure':        '#2060A0',
    'Meringue':     '#F5F0E8',
    'Flint':        '#9EA5AB',
    'Berry':        '#7c3580',
    'Rhône':        '#8b1a1a',
    'Camomille':    '#F5E090',
    'Caribe':       '#0098a8',
    'Artichaut':    '#4d7a3c',
    'Cool Mint':    '#a8d8b8',
}

def add_bg_fallback(match):
    div = match.group(0)
    title_m = re.search(r'title="([^"]+)"', div)
    if not title_m:
        return div
    color_name = title_m.group(1)
    hex_color = color_map.get(color_name)
    if not hex_color:
        return div
    # Only add if has background-image but no solid background color declared
    if 'background-image' in div and f'background:{hex_color}' not in div and 'background:#' not in div.split('background-image')[0]:
        # Insert background-color before background-image in the style
        div = div.replace('background-image:', f'background-color:{hex_color};background-image:', 1)
    return div

# Fix color swatches in the color-swatches section only
# We use a pattern that targets the product color swatches section
content_new = re.sub(
    r'<div class="color-swatch[^"]*"[^>]*title="[^"]*"[^>]*/?>',
    add_bg_fallback,
    content
)

if content_new != content:
    file.write_text(content_new, encoding='utf-8')
    print("OK: panela-redonda-signature.html swatch fallbacks added")
else:
    print("NO CHANGE: panela-redonda-signature.html")

# ─── 2. Fix collection page: add 1 dot to cards missing product-colors ───
file2 = Path("colecao-panelas-de-ferro.html")
content2 = file2.read_text(encoding='utf-8')

CDN = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"

def img(h): return f"{CDN}{h}?sw=650&sh=650&sm=fit"

def dot(color, hex_color, img_hash, active=True, border=False):
    style = f"background:{hex_color};"
    if border: style += "border:1.5px solid #ccc;"
    return f'<div class="product-color-dot active" style="{style}" title="{color}" data-color="{color}" data-img="{img(img_hash)}" onclick="dotColor(this)"></div>'

def add_single_dot(content, price_min, href, name_text, price_text, install_text, color_name, hex_color, img_hash, colors_attr=None, border=False):
    if colors_attr is None:
        colors_attr = color_name
    # Check if this card already has product-colors
    # Find the card block
    card_marker = f'data-price-min="{price_min}" data-reveal'
    if card_marker not in content:
        return content, False

    # Check if product-colors already exists in this card's region
    card_idx = content.find(card_marker)
    next_card_idx = content.find('product-card"', card_idx + 1)
    if next_card_idx == -1:
        next_card_idx = len(content)
    card_block = content[card_idx:next_card_idx]

    if 'product-colors' in card_block:
        return content, False  # Already has colors

    # Build the info end marker
    install_div = f'<div class="product-installment">{install_text}</div>'
    info_end = f'{install_div}\n        </div>\n      </div>'

    if info_end not in content:
        return content, False

    new_info_end = (f'{install_div}\n'
                    f'          <div class="product-colors">\n'
                    f'            {dot(color_name, hex_color, img_hash, border=border)}\n'
                    f'          </div>\n'
                    f'        </div>\n      </div>')

    # Only replace the FIRST occurrence after the card marker
    idx = content.find(card_marker)
    segment_start = content.find(info_end, idx)
    if segment_start == -1:
        return content, False

    content = content[:segment_start] + new_info_end + content[segment_start + len(info_end):]

    # Also add data-colors attribute
    content = content.replace(
        f'data-price-min="{price_min}" data-reveal',
        f'data-price-min="{price_min}" data-colors="{colors_attr}" data-reveal',
        1
    )
    return content, True

# Products missing color dots — add at least 1
single_color_products = [
    # (price_min, install_text, color_name, hex_color, img_hash, border)
    ("3899.0",  "10x R$ 389,90 sem Juros", "Flamme Dorée", "#D4A017", "dw36947ba2/images/100%20Anos/panela-oval-flame-doree.png", False),
    ("3819.0",  "10x R$ 381,90 sem Juros", "Laranja",      "#d46820",  "dw5a6b2fa5/images/cacarola-buffet-28Cm-Modern-laranja-Heritage.png", False),
    ("3699.0",  "10x R$ 369,90 sem Juros", "Meringue",     "#F5F0E8",  "dwfdb403b0/images/panela-redonda-26Cm-Modern-Heritage-meringue.png", True),
    ("3399.0",  "10x R$ 339,90 sem Juros", "Rosa",         "#f4b8c8",  "dw99d3d451/images/panela-redonda-colecao-wicked-glinda%20(2).png", True),
    ("4379.0",  "10x R$ 437,90 sem Juros", "Flamme Dorée", "#D4A017",  "dwa57c56ea/images/100%20Anos/panela-abobora-flame-doree.png", False),
    ("3809.0",  "10x R$ 380,90 sem Juros", "Laranja",      "#d46820",  "dw8894e17f/images/produto-lecreuset-panela-abobora-laranja%20(3).png", False),
    ("4269.0",  "10x R$ 426,90 sem Juros", "Laranja",      "#d46820",  "dw56ae8f89/images/caccarola-buffet-signature-abobora28cm.png", False),
    ("2369.0",  "10x R$ 236,90 sem Juros", "Berry",        "#7c3580",  "dw15c3c264/images/panela-flor-tradition-20cm-berry.png", False),
    ("1449.0",  "10x R$ 144,90 sem Juros", "Vermelho",     "#c8102e",  "dwfc8e3a97/images/skillet-coracao-lecreuset-vermelho.png", False),
    ("2199.0",  "10x R$ 219,90 sem Juros", "Graphite",     "#5A5A5A",  "dwaf467702/images/produto-lecreuset-panela-arroz-graphite%20(2).png", False),
    ("439.0",   "10x R$ 43,90 sem Juros",  "Graphite",     "#5A5A5A",  "dwc38f378c/images/tampa-interna-panela-dearroz.png", False),
    ("2469.0",  "10x R$ 246,90 sem Juros", "Rhône",        "#8b1a1a",  "dw19a1bf1a/images/lecreuset-panela-everyday-rhone.png", False),
    ("2949.0",  "10x R$ 294,90 sem Juros", "Laranja",      "#d46820",  "dw2032c303/images/produto-lecreuset-wok-laranja-vidro.png", False),
    ("2191.2",  "10x R$ 219,12 sem Juros", "Vermelho",     "#c8102e",  "dwc58f4908/images/produto-lecreuset-tagine-vermelho.png", False),
    ("2279.0",  "10x R$ 227,90 sem Juros", "Vermelho",     "#c8102e",  "dw8af30b99/images/frigideira-cabo-de-madeira-vermelho-signature-lecreuset1.jpg", False),
    ("2489.0",  "10x R$ 248,90 sem Juros", "Matte Black",  "#1C1C1C",  "dw246f331d/images/Grelha-Retangular-com-Alcas-alpine-40cm-matte-black.png", False),
    ("1669.0",  "10x R$ 166,90 sem Juros", "Matte Black",  "#1C1C1C",  "dwf36c5adf/images/cesta-perfurada-quadrada-alpine-30cm-matte-black.png", False),
    ("1429.0",  "10x R$ 142,90 sem Juros", "Vermelho",     "#c8102e",  "dw0a51a20c/images/grelha-retangular-lecreuset-vermelha.png", False),
    ("1799.0",  "10x R$ 179,90 sem Juros", "Vermelho",     "#c8102e",  "dwcaff767a/images/cacarola-funda-3ply-lc.png", False),
    ("1769.0",  "10x R$ 176,90 sem Juros", "Matte Black",  "#1C1C1C",  "dwd8aeb9fc/images/grelha-quadrada-alpine-26cm-matte-black.png", False),
    ("1509.0",  "10x R$ 150,90 sem Juros", "Matte Black",  "#1C1C1C",  "dwe64a51e1/images/grelha-redonda-alpine-35cm-matte-black.png", False),
    ("2999.0",  "10x R$ 299,90 sem Juros", "Matte Black",  "#1C1C1C",  "dwd34a7285/images/skillet-redonda-alpine-25cm-matte-black.png", False),
    ("1359.0",  "10x R$ 135,90 sem Juros", "Vermelho",     "#c8102e",  "dw8894e17f/images/produto-lecreuset-panela-abobora-laranja%20(3).png", False),
    ("3219.0",  "10x R$ 321,90 sem Juros", "Vermelho",     "#c8102e",  "dw5b5fae0f/images/produto-lecreuset-grelha-redonda-lisa1.png", False),
    ("4199.25", "10x R$ 419,93 sem Juros", "Vermelho",     "#c8102e",  "dw4a4e9c71/images/set-mini-buffet-com-tampa-gourmand.png", False),
    ("2624.25", "10x R$ 262,43 sem Juros", "Vermelho",     "#c8102e",  "dw4a4e9c71/images/set-mini-buffet-gourmand.png", False),
    ("3149.25", "10x R$ 314,93 sem Juros", "Vermelho",     "#c8102e",  "dw4a4e9c71/images/set-mini-skillets-gourmand.png", False),
    ("3299.0",  "10x R$ 329,90 sem Juros", "Artichaut",    "#4d7a3c",  "dw2c627260/images/panela-redonda-signature-pegador-estrela-artichaut20.png", False),
    ("1579.0",  "10x R$ 157,90 sem Juros", "Vermelho",     "#c8102e",  "dw7656b11c/images/grelha-retangular-rasa-vermelha.jpg", False),
    ("1299.0",  "10x R$ 129,90 sem Juros", "Vermelho",     "#c8102e",  "dw5a5c1ca9/images/crepeira-lecreuset-preta.jpg", False),
    ("1519.0",  "10x R$ 151,90 sem Juros", "Vermelho",     "#c8102e",  "dw9fa69e17/images/20210720_GS_20205240600460_200_002.png", False),
]

count = 0
for item in single_color_products:
    price_min, install_text, color_name, hex_color, img_hash, border = item
    content2, changed = add_single_dot(
        content2, price_min, None, None, None, install_text,
        color_name, hex_color, img_hash, border=border
    )
    if changed:
        count += 1
        print(f"  Added dot to price={price_min}: {color_name}")

file2.write_text(content2, encoding='utf-8')
print(f"OK: {count} products updated in collection page")
