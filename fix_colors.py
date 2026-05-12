import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

file_path = Path("colecao-panelas-de-ferro.html")
content = file_path.read_text(encoding='utf-8')

CDN = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"

def img(h): return f"{CDN}{h}?sw=650&sh=650&sm=fit"
def dot(color, hex_color, img_hash, active=False, border=False):
    cls = " active" if active else ""
    style = f"background:{hex_color};"
    if border: style += "border:1.5px solid #ccc;"
    return f'<div class="product-color-dot{cls}" style="{style}" title="{color}" data-color="{color}" data-img="{img(img_hash)}" onclick="dotColor(this)"></div>'

def cdiv(*dots):
    return '\n          <div class="product-colors">\n            ' + '\n            '.join(dots) + '\n          </div>'

results = []

# FIX: Panela Arroz Every - Chambray should be active (matches main image)
old = ('            <div class="product-color-dot active" style="background:#d46820;" title="Laranja" data-color="Laranja"'
       ' data-img="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw854d155d/images/produto-lecreuset-panela-arroz-laranja1.png?sw=650&sh=650&sm=fit"'
       ' onclick="dotColor(this)"></div>\n'
       '            <div class="product-color-dot" style="background:#7098c8;" title="Chambray"')
new = ('            <div class="product-color-dot" style="background:#d46820;" title="Laranja" data-color="Laranja"'
       ' data-img="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw854d155d/images/produto-lecreuset-panela-arroz-laranja1.png?sw=650&sh=650&sm=fit"'
       ' onclick="dotColor(this)"></div>\n'
       '            <div class="product-color-dot active" style="background:#7098c8;" title="Chambray"')
results.append(("Fix Arroz active", old in content))
content = content.replace(old, new, 1)

# ADD: Skillet Redonda Signature
content = content.replace(
    '<div class="product-card" data-price-min="1304.25" data-reveal>\n        <div class="product-card-media">\n          <a href="skillet-redonda-signature.html">',
    '<div class="product-card" data-price-min="1304.25" data-colors="Vermelho,Laranja,Bamboo,Marseille" data-reveal>\n        <div class="product-card-media">\n          <a href="skillet-redonda-signature.html">'
)
marker = ('<div class="product-name"><a href="skillet-redonda-signature.html">Skillet Redonda Signature</a></div>\n'
          '          <div class="product-price">R$ 1.304,25 - R$ 1.999,00</div>\n'
          '          <div class="product-installment">10x R$ 130,43 sem Juros</div>\n'
          '        </div>\n      </div>')
if marker in content:
    repl = marker.replace(
        '          <div class="product-installment">10x R$ 130,43 sem Juros</div>\n        </div>',
        '          <div class="product-installment">10x R$ 130,43 sem Juros</div>' + cdiv(
            dot("Vermelho","#c8102e","dw3a6991b9/images/produto-lecreuset-skillet-vermelho.png",active=True),
            dot("Laranja","#d46820","dw02921f58/images/produto-lecreuset-skillet-laranja.png"),
            dot("Bamboo","#c8b48c","dw32dc5870/images/produto-lecreuset-skillet-bamboo.png"),
            dot("Marseille","#4a7eb5","dwadde9fdc/images/produto-lecreuset-skillet-marseille.png")
        ) + '\n        </div>'
    )
    content = content.replace(marker, repl, 1)
    results.append(("Skillet Redonda", True))
else:
    results.append(("Skillet Redonda", False))

# ADD: Panela Marmita Signature (card 23)
content = content.replace(
    '<div class="product-card" data-price-min="2091.75" data-reveal>\n        <div class="product-card-media">\n          <a href="panela-marmita-holly.html">',
    '<div class="product-card" data-price-min="2091.75" data-colors="Chambray,Laranja,Caribe,Nectar" data-reveal>\n        <div class="product-card-media">\n          <a href="panela-marmita-holly.html">'
)
marker2 = ('<div class="product-name"><a href="panela-marmita-holly.html">Panela Marmita Signature</a></div>\n'
           '          <div class="product-price">R$ 2.091,75 - R$ 3.279,00</div>\n'
           '          <div class="product-installment">10x R$ 209,18 sem Juros</div>\n'
           '        </div>\n      </div>')
if marker2 in content:
    repl2 = marker2.replace(
        '          <div class="product-installment">10x R$ 209,18 sem Juros</div>\n        </div>',
        '          <div class="product-installment">10x R$ 209,18 sem Juros</div>' + cdiv(
            dot("Chambray","#7098c8","dw2bcdd94c/images/produto-lecreuset-panela-marmita-chambray.png",active=True),
            dot("Laranja","#d46820","dw1a9d0004/images/produto-lecreuset-panela-marmita-laranja.png"),
            dot("Caribe","#00B8D4","dw28f2dcbd/images/produto-lecreuset-panela-marmita-caribe.png"),
            dot("Nectar","#D4C44A","dwad357c4e/images/produto-lecreuset-panela-marmita-nectar.png")
        ) + '\n        </div>'
    )
    content = content.replace(marker2, repl2, 1)
    results.append(("Panela Marmita Sig", True))
else:
    results.append(("Panela Marmita Sig", False))

# ADD: Panela Sauteuse Signature (card 22, white/cotton image)
content = content.replace(
    '<div class="product-card" data-price-min="2769.0" data-reveal>\n        <div class="product-card-media">\n          <a href="panela-sautese-holly.html">',
    '<div class="product-card" data-price-min="2769.0" data-colors="Cotton,Vermelho,Artichaut" data-reveal>\n        <div class="product-card-media">\n          <a href="panela-sautese-holly.html">',
    1
)
marker3 = ('<div class="product-name"><a href="panela-sautese-holly.html">Panela Sauteuse Signature</a></div>\n'
           '          <div class="product-price">R$ 2.769,00</div>\n'
           '          <div class="product-installment">10x R$ 276,90 sem Juros</div>\n'
           '        </div>\n      </div>')
if marker3 in content:
    repl3 = marker3.replace(
        '          <div class="product-installment">10x R$ 276,90 sem Juros</div>\n        </div>',
        '          <div class="product-installment">10x R$ 276,90 sem Juros</div>' + cdiv(
            dot("Cotton","#f0ece0","dwefdf81e4/images/produto-le-creuset-panela-sautese-24cm-signature-branca-pegador-dourado-21198240101441-frente-angulo.jpg",active=True,border=True),
            dot("Vermelho","#c8102e","dw7abd3659/images/panela-sautese-holly-vermelho%20(2).png")
        ) + '\n        </div>'
    )
    content = content.replace(marker3, repl3, 1)
    results.append(("Panela Sauteuse Sig", True))
else:
    results.append(("Panela Sauteuse Sig", False))

# ADD: Panela Oblong Signature - Vermelho + Berry
content = content.replace(
    '<div class="product-card" data-price-min="2759.0" data-reveal>\n        <div class="product-card-media">\n          <a href="panela-oval-signature.html">',
    '<div class="product-card" data-price-min="2759.0" data-colors="Vermelho,Berry" data-reveal>\n        <div class="product-card-media">\n          <a href="panela-oval-signature.html">'
)
marker4 = ('<div class="product-name"><a href="panela-oval-signature.html">Panela Oblong Signature</a></div>\n'
           '          <div class="product-price">R$ 2.759,00 - R$ 3.039,00</div>\n'
           '          <div class="product-installment">10x R$ 275,90 sem Juros</div>\n'
           '        </div>\n      </div>')
if marker4 in content:
    repl4 = marker4.replace(
        '          <div class="product-installment">10x R$ 275,90 sem Juros</div>\n        </div>',
        '          <div class="product-installment">10x R$ 275,90 sem Juros</div>' + cdiv(
            dot("Vermelho","#c8102e","dw48d33705/images/produto-lecreuset-panela-oblong-vermelho.png",active=True),
            dot("Berry","#7c3580","dw30d7f22c/images/berry-oblong.png")
        ) + '\n        </div>'
    )
    content = content.replace(marker4, repl4, 1)
    results.append(("Panela Oblong", True))
else:
    results.append(("Panela Oblong", False))

file_path.write_text(content, encoding='utf-8')

for name, found in results:
    print(f"{'OK' if found else 'NOT FOUND'}: {name}")
print("Done")
