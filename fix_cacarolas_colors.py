# -*- coding: utf-8 -*-
import os, re

BASE = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'
DIR = os.path.dirname(os.path.abspath(__file__))

def img(h, f):
    return f'{BASE}{h}/images/{f}?sw=650&sh=650&sm=fit'

# ── Color data per product ──────────────────────────────────────────────────
COLORS = {
    'cacarola-buffet-signature.html': [
        ('Laranja',      '#d46820', img('dw8283d435', 'produto-lecreuset-ca%C3%A7arola-redonda-laranja.png')),
        ('Vermelho',     '#c8102e', img('dwffc12c88',  'produto-lecreuset-ca%C3%A7arola-redonda-vermelho.png')),
        ('Bleu Riviera', '#2563ab', img('dwe61a242b',  '21180300994450-cacarola-buffet-bleu.jpg')),
        ('Azure',        '#7EB3D8', img('dw2295f57e',  'lecreuset-ca%C3%A7arola-redonda-azure.png')),
        ('Meringue',     '#F5F0E8', img('dwd198c7aa',  'produto-lecreuset-ca%C3%A7arola-redonda-meringue.png')),
        ('Branco',       '#EFEFEF', img('dw8ac659d0',  'cacarola-pegador-dourado-white.png')),
        ('Cool Mint',    '#A8D8C8', img('dwa26cebcf',  'tardes%20de%20verao/ca%C3%A7arola-buffet-signature-30cm-coolmint.png')),
        ('Pêche',        '#E8A87C', img('dwb398291e',  'produto-lecreuset-ca%C3%A7arola-redonda-peche.png')),
        ('Cotton',       '#E8E0D8', img('dwff6c498d',  'produto-lecreuset-ca%C3%A7arola-redonda-cotton.png')),
        ('Bluebell',     '#9B7EB0', img('dwff69be8c',  'cacarola-buffet-signature-bluebell.png')),
    ],
    'cacarola-buffet-signature-petal.html': [
        ('Sea Salt', '#B8D4D0', img('dwdc236776', 'ca%C3%A7arola-buffet-signature-petal-seasalt%20(2).png')),
        ('Honey',    '#C49A44', img('dw567dc9cc',  'ca%C3%A7arola-buffet-signature-petal-honey.png')),
    ],
    'cacarola-buffet-abobora.html': [
        ('Marronnier', '#6B4226', img('dw37d8acb7', 'ca%C3%A7arola-buffet-signature-abobora-pegador-dourado-marronnier-28cm.png')),
        ('Meringue',   '#F5F0E8', img('dwca6362ac', 'ca%C3%A7arola-buffet-signature-abobora-pegador-dourado-meringue-28cm.png')),
        ('Branco',     '#EFEFEF', img('dw149ec2b5', 'ca%C3%A7arola-buffet-signature-abobora-pegador-dourado-white-28cm.png')),
    ],
    'cacarola-buffet-modern-heritage.html': [
        ('Laranja',  '#d46820', img('dw5a6b2fa5', 'cacarola-buffet-28Cm-Modern-laranja-Heritage.png')),
        ('Meringue', '#F5F0E8', img('dw2ae07ee9', 'cacarola-buffet-28Cm-Modern-meringue-Heritage.png')),
    ],
}

# ── 1. Update product detail pages ─────────────────────────────────────────
for fname, colors in COLORS.items():
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Build new color-picker block
    first_name, first_bg, first_src = colors[0]
    swatches = ''
    for name, bg, src in colors:
        active = ' active' if name == first_name else ''
        border = ' border:1px solid #ccc;' if bg in ('#EFEFEF','#F5F0E8','#E8E0D8') else ''
        swatches += f'\n        <div class="color-swatch{active}" style="background:{bg};{border}" title="{name}"\n          onclick="selectColor(this,\'{name}\',\'{src}\')"></div>'

    new_picker = f'''<div class="color-picker">
      <div class="color-picker-label">Cor: <span id="colorName">{first_name}</span></div>
      <div class="color-swatches">{swatches}
      </div>
    </div>'''

    # Also update main image src to first color
    html = re.sub(
        r'(<img id="mainImgEl" src=")[^"]+(")',
        r'\g<1>' + first_src + r'\g<2>',
        html
    )

    # Replace color-picker block
    html = re.sub(
        r'<div class="color-picker">.*?</div>\s*</div>',
        new_picker,
        html, flags=re.DOTALL, count=1
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated product page: {fname} ({len(colors)} cores)')


# ── 2. Update collection page cards ────────────────────────────────────────
col_path = os.path.join(DIR, 'colecao-cacarolas.html')
with open(col_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add swatch CSS if not already there
SWATCH_CSS = '''    .product-colors { position: absolute; bottom: 48px; left: 10px; display: flex; gap: 4px; z-index: 2; flex-wrap: wrap; max-width: 90%; }
    .swatch { width: 18px; height: 18px; border-radius: 50%; cursor: pointer; border: 1.5px solid rgba(255,255,255,0.8); display: inline-block; transition: transform 0.2s, border-color 0.2s; }
    .swatch:hover, .swatch.active { border-color: #000; transform: scale(1.15); }'''

if '.product-colors' not in html:
    html = html.replace('    footer {', SWATCH_CSS + '\n    footer {')

# Map img IDs to color data (in collection page order: cc1..cc9)
CARD_COLORS = {
    'img-cc1': COLORS['cacarola-buffet-signature.html'],
    'img-cc2': COLORS['cacarola-buffet-signature-petal.html'],
    'img-cc3': COLORS['cacarola-buffet-abobora.html'],
    # cc4 Flamme Dorée - single color, skip
    # cc5 3-Ply - single color, skip
    # cc6 Mini Buffet Tampa - single color, skip
    # cc7 Aço Esmaltado - single color, skip
    'img-cc8': COLORS['cacarola-buffet-modern-heritage.html'],
    # cc9 Mini Buffet - single color, skip
}

for img_id, colors in CARD_COLORS.items():
    # Build swatch spans
    spans = ''
    for name, bg, src in colors:
        active = ' active' if name == colors[0][0] else ''
        border = ' border:1px solid #ccc;' if bg in ('#EFEFEF','#F5F0E8','#E8E0D8') else ''
        spans += f'\n            <span class="swatch{active}" style="background:{bg};{border}" title="{name}" onclick="swatchClick(this,\'{img_id}\',\'{src}\')"></span>'

    swatch_div = f'\n          <div class="product-colors">{spans}\n          </div>'

    # Insert swatch div before the wishlist div (after the img closing tag)
    # Pattern: the img tag with this id, followed by </a> then wishlist
    html = re.sub(
        r'(<img id="' + img_id + r'"[^/]*/>\s*</a>)(\s*\n\s*<div class="product-wishlist">)',
        r'\1' + swatch_div + r'\2',
        html
    )

    # Also update the img src to first color
    first_src = colors[0][2]
    html = re.sub(
        r'(<img id="' + img_id + r'" src=")[^"]+(")',
        r'\g<1>' + first_src + r'\g<2>',
        html
    )

# Add swatchClick JS before </body>
SWATCH_JS = '''<script>
function swatchClick(swatch, imgId, newSrc) {
  var colors = swatch.parentElement;
  var swatches = colors.querySelectorAll('.swatch');
  for (var i = 0; i < swatches.length; i++) {
    swatches[i].classList.remove('active');
  }
  swatch.classList.add('active');
  var img = document.getElementById(imgId);
  if (img) img.src = newSrc;
}
</script>'''

if 'swatchClick' not in html:
    html = html.replace('</body>', SWATCH_JS + '\n</body>')

with open(col_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated collection page with color swatches')
