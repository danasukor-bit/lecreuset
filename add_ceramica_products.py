import re, os

BASE = r'c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset'

HEART = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

def get_main_img(filename):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        return ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Try to find main product image - look for id="main-img" or first product img
    m = re.search(r'id=["\']main-img["\'][^>]*src=["\']([^"\']+)["\']', html)
    if not m:
        m = re.search(r'src=["\']([^"\']+)["\'][^>]*id=["\']main-img["\']', html)
    if not m:
        # look for first lecreuset CDN image
        m = re.search(r'src=["\'](https://www\.lecreuset\.com\.br/dw/image/[^"\']+)["\']', html)
    if m:
        return m.group(1)
    return ''

def card(nome, sub, preco, href, img, cpid):
    return f'''    <div class="product-card">
      <div class="product-card-img">
        <a href="{href}"><img id="{cpid}" src="{img}" alt="{nome}" /></a>
        {HEART}
      </div>
      <a href="{href}">
        <div class="product-card-name">{nome}</div>
        <div class="product-card-sub">{sub}</div>
        <div class="product-card-price">R$ {preco}</div>
      </a>
    </div>'''

# Missing products: (name, subtitle, price, href)
produtos = [
    ("Set Caneca 100ml Gift Collection", "Cerâmica Esmaltada · 4 peças", "299,00", "set-caneca-100ml-gift-collection.html"),
    ("Açucareiro", "Cerâmica Esmaltada", "229,00", "acucareiro.html"),
    ("Pie Bird", "Cerâmica Esmaltada", "129,00", "pie-bird.html"),
    ("Manteigueira", "Cerâmica Esmaltada", "249,00", "manteigueira.html"),
    ("Bandeja de Servir Oval Jardin", "Cerâmica Esmaltada", "429,00", "bandeja-de-servir-oval-jardin.html"),
    ("Pote de Alho", "Cerâmica Esmaltada", "199,00", "pote-de-alho.html"),
    ("Pote para Biscoito", "Cerâmica Esmaltada", "499,00", "pote-para-biscoito.html"),
    ("Porta Guardanapo 15cm", "Cerâmica Esmaltada", "179,00", "porta-guardanapo-15cm.html"),
    ("Set Cream & Sugar", "Cerâmica Esmaltada · 2 peças", "399,00", "set-creme-e-acucar.html"),
    ("Saleiro Redondo de Madeira Teca", "Madeira · 70ml", "249,00", "saleiro-redondo-madeira-teca.html"),
    ("Travessa Retangular Clássica", "Cerâmica Esmaltada", "559,00", "travessa-retangular-classica.html"),
    ("Descanso Oval para Colher", "Cerâmica Esmaltada", "139,00", "descanso-oval-para-colher.html"),
    ("Bowl Redondo Kobe", "Cerâmica Esmaltada · 16cm", "239,00", "bowl-redondo-kobe.html"),
    ("Suporte para Bolo", "Cerâmica Esmaltada", "699,00", "suporte-para-bolo.html"),
    ("Bandeja Para 6 Ovos", "Cerâmica Esmaltada", "319,00", "bandeja-para-6-ovos.html"),
    ("Travessa Terrine Heritage", "Cerâmica Esmaltada", "789,00", "travessa-terrine-heritage.html"),
    ("Porta Mantimentos", "Cerâmica Esmaltada", "379,00", "porta-mantimentos.html"),
    ("Prato para Aperitivos e Molhos", "Cerâmica Esmaltada", "259,00", "prato-para-aperitivos-e-molhos.html"),
    ("Suporte para Ovo", "Cerâmica Esmaltada", "99,00", "suporte-para-ovo.html"),
    ("Bowl Redondo", "Cerâmica Esmaltada · 16cm", "239,00", "bowl-redondo.html"),
    ("Miniatura Collection", "Cerâmica Esmaltada", "199,00", "miniatura-collection.html"),
    ("Pote Com Tampa de Madeira 220ml", "Cerâmica Esmaltada", "199,00", "pote-tampa-madeira-220ml.html"),
    ("Pilão", "Cerâmica Esmaltada", "349,00", "pilao.html"),
    ("Dispenser para Sabão 580ml", "Cerâmica Esmaltada", "299,00", "dispenser-para-sabao-580ml.html"),
    ("Travessa Redonda Para Torta Heritage", "Cerâmica Esmaltada · 31cm", "429,00", "travessa-redonda-torta-heritage.html"),
    ("Noodle Bowl Kobe", "Cerâmica Esmaltada", "299,00", "noodle-bowl-kobe.html"),
    ("Set 3 Travessas Heritage", "Cerâmica Esmaltada · 3 peças", "1.349,00", "set-3-travessas-heritage.html"),
    ("Set 2 Pratos Gato", "Cerâmica Esmaltada", "299,00", "set-2-pratos-gato.html"),
    ("Set Saleiro & Pimenteiro Coração", "Cerâmica Esmaltada", "249,00", "set-saleiro-pimenteiro-coracao.html"),
    ("Set 2 Pratos Flower 23cm", "Cerâmica Esmaltada · 2 peças", "399,00", "set-2-pratos-flower-23cm.html"),
    ("Porta Óleo 600ml", "Cerâmica Esmaltada", "199,00", "porta-oleo-600ml.html"),
    ("Travessa Abóbora", "Cerâmica Esmaltada", "599,00", "travessa-abobora.html"),
    ("Set 2 Suportes Para Ovo Jardin", "Cerâmica Esmaltada · 2 peças", "219,00", "set-suportes-para-ovo-jardin.html"),
    ("Travessa Retangular com Tampa Signature", "Cerâmica Esmaltada", "999,00", "travessa-retangular-tampa-signature.html"),
    ("Bowl de Servir Ruffle", "Cerâmica Esmaltada · 28cm", "499,00", "bowl-de-servir-ruffle.html"),
    ("Multi Bowl Holly", "Cerâmica Esmaltada", "259,00", "multi-bowl-holly.html"),
    ("Pote Com Tampa de Madeira 1,9L", "Cerâmica Esmaltada", "549,00", "pote-tampa-madeira-19l.html"),
    ("Pote para Geleia", "Cerâmica Esmaltada", "179,00", "pote-para-geleia.html"),
    ("Ramekin 200ml", "Cerâmica Esmaltada · 200ml", "149,00", "ramekin-200ml.html"),
    ("Sopeira Heritage 600ml", "Cerâmica Esmaltada · 600ml", "599,00", "sopeira-heritage-600ml.html"),
    ("Pote Com Tampa de Madeira 1,1L", "Cerâmica Esmaltada", "429,00", "pote-tampa-madeira-11l.html"),
    ("Prato Flor", "Cerâmica Esmaltada · 23cm", "229,00", "prato-flor.html"),
    ("Pote para Mostarda", "Cerâmica Esmaltada", "169,00", "pote-para-mostarda.html"),
    ("Forma de Pão Retangular Canelada", "Cerâmica Esmaltada", "549,00", "forma-pao.html"),
    ("Travessa Retangular Heritage", "Cerâmica Esmaltada", "689,00", "travessa-retangular-heritage.html"),
    ("Set 3 Protetores", "Acessórios · 3 peças", "199,00", "set-3-protetores.html"),
    ("Suporte para Bolo Ruffle 28cm", "Cerâmica Esmaltada · 28cm", "799,00", "suporte-para-bolo-ruffle-28cm.html"),
    ("Pote Com Tampa de Madeira 420ml", "Cerâmica Esmaltada", "279,00", "pote-tampa-madeira-420ml.html"),
    ("Bowl Redondo San Francisco", "Cerâmica Esmaltada", "219,00", "bowl-redondo-san-francisco.html"),
    ("Prato Fundo Kobe", "Cerâmica Esmaltada · 22cm", "259,00", "prato-fundo-kobe.html"),
    ("Bowl Jardin 320ml", "Cerâmica Esmaltada · 320ml", "199,00", "bowl-jardin-320ml.html"),
    ("Travessa Retangular Heritage com Tampa", "Cerâmica Esmaltada", "1.059,00", "travessa-retangular-heritage-com-tampa.html"),
    ("Ramekin Coração", "Cerâmica Esmaltada", "149,00", "ramekin-coracao.html"),
    ("Set 4 Pratos Fundos 22cm", "Cerâmica Esmaltada · 4 peças", "799,00", "set-4-pratos-fundos-22cm.html"),
    ("Set 4 Pratos Rasos 22cm", "Cerâmica Esmaltada · 4 peças", "799,00", "set-4-pratos-rasos-22cm.html"),
    ("Set 4 Pratos Rasos 27cm", "Cerâmica Esmaltada · 4 peças", "899,00", "set-4-pratos-rasos-27cm.html"),
]

# Read current ceramica html
with open(os.path.join(BASE, 'colecao-ceramica.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Find end of product grid (closing </div> before </div>\n  </div>)
# The grid ends with the last product-card </div> then </div> for the grid itself
end_marker = '    </div>\n  </div>\n</div>\n<footer'
grid_end = html.find(end_marker)
if grid_end == -1:
    end_marker = '    </div>\n  </div>\n</div>\n<script'
    grid_end = html.find(end_marker)
if grid_end == -1:
    # fallback: find </div> before </div>  </div>
    end_marker = '\n    </div>\n  </div>'
    grid_end = html.rfind(end_marker, 0, html.find('<footer'))

print(f'grid_end position: {grid_end}')
print(f'Context: {repr(html[grid_end-50:grid_end+80])}')

# Build new cards
new_cards = ''
# find current max cpN id
existing_ids = re.findall(r'id="cp(\d+)"', html)
next_id = max(int(x) for x in existing_ids) + 1 if existing_ids else 13

for nome, sub, preco, href in produtos:
    img = get_main_img(href)
    if not img:
        img = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc027de66/images/produto-lecreuset-minicocotte-laranja-vermelho.png?sw=650&sh=650&sm=fit'
    cpid = f'cp{next_id}'
    next_id += 1
    new_cards += '\n' + card(nome, sub, preco, href, img, cpid)

# Insert new cards before the closing </div> of product-grid
# Find the product grid closing tag
insert_pos = grid_end
html_new = html[:insert_pos] + new_cards + '\n' + html[insert_pos:]

with open(os.path.join(BASE, 'colecao-ceramica.html'), 'w', encoding='utf-8') as f:
    f.write(html_new)

print(f'Added {len(produtos)} products. Total cp IDs now go up to cp{next_id-1}')
