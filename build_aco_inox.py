import re

base = open('colecao-formatos-especiais.html', encoding='utf-8').read()

CDN = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'

def img(h, path):
    return CDN + h + '/images/' + path + '?sw=650&sh=650&sm=fit'

def wish():
    return '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

def card(href, img_id, img_url, name, sub, price, badge=None, old_price=None):
    badge_html = ''
    if badge:
        badge_html = f'<div class="product-badge" style="position:absolute;top:10px;left:10px;background:#c8102e;color:#fff;font-size:10px;font-weight:700;padding:3px 8px;letter-spacing:0.5px;">{badge}</div>\n      '
    old_price_html = ''
    if old_price:
        old_price_html = f'<div class="product-card-old" style="font-size:12px;color:#999;text-decoration:line-through;margin-bottom:2px;">{old_price}</div>\n'
    return (
        '<div class="product-card">\n'
        '  <a href="' + href + '">\n'
        '    <div class="product-card-img">\n'
        '      ' + badge_html +
        '      <img id="' + img_id + '" src="' + img_url + '" alt="' + name + '" />\n'
        '      ' + wish() + '\n'
        '    </div>\n'
        '  </a>\n'
        '  <a href="' + href + '">\n'
        '    ' + old_price_html +
        '    <div class="product-card-name">' + name + '</div>\n'
        '    <div class="product-card-sub">' + sub + '</div>\n'
        '    <div class="product-card-price">' + price + '</div>\n'
        '  </a>\n'
        '</div>'
    )

products = [
    # Utensílios Revolution
    card('set-4-utensilios-inox-alpine.html','i1',
         img('dw6d406278','conjunto-alpine-4-pecas-inox.png'),
         'Set 4 Utensilios Inox Alpine','Aco Inox · 4 Pecas','R$ 1.429,00', badge='LANCAMENTO'),
    card('colher-revolution-inox.html','i2',
         img('dwa5ac9575','colher_revolution_aco_inox-41010000010000-img1.jpg'),
         'Colher Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    card('peneira-revolution-inox.html','i3',
         img('dwa0512a82','41006150000000.jpg'),
         'Peneira Revolution Aco Inox','Aco Inox 18/10 · 36cm','R$ 489,00'),
    card('escumadeira-revolution-inox.html','i4',
         img('dw9b2b2108','escumadeira_revolution_aco_inox-41005000010000-img1.jpg'),
         'Escumadeira Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    card('espatula-revolution-inox.html','i5',
         img('dwed80bad0','espatula_vazada_revolution_aco_inox-41001000010000-img1.jpg'),
         'Espatula Vazada Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    card('amassador-batatas-revolution.html','i6',
         img('dw516ea012','amassador_de_batatas_revolution_aco_inox-41002000010000-img1.jpg'),
         'Amassador De Batatas Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    card('espatula-revolution-inox-silicone.html','i7',
         img('dw11afde64','espatula_vazada_revolution_aco_inox_e_silicone-41007350010100-img1.jpg'),
         'Espatula Vazada Revolution Aco Inox e Silicone','Aco Inox + Silicone','R$ 439,00'),
    card('concha-revolution-inox.html','i8',
         img('dw19d55861','concha_revolution_aco_inox-41008000010000-img1.jpg'),
         'Concha Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    card('batedor-revolution-inox.html','i9',
         img('dw03e71561','batedor_revolution_aco_inox-41026000010000-img1.jpg'),
         'Batedor Revolution Aco Inox','Aco Inox 18/10','R$ 329,00'),
    card('pinca-revolution-inox.html','i10',
         img('dw80f46c97','pinca_revolution_de_aco_inox-98401900000000-img01.jpg'),
         'Pinca Revolution Aco Inox','Aco Inox 18/10','R$ 339,00'),
    card('colher-vazada-revolution-inox.html','i11',
         img('dwc82e4186','colher_vazada_revolution_aco_inox-41003000010000-img1.jpg'),
         'Colher Vazada Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    card('pegador-massa-revolution.html','i12',
         img('dw7ed7ea76','pegador_de_massa_revolution_aco_inox-41009000010000-img01.jpg'),
         'Pegador De Massa Revolution Aco Inox','Aco Inox 18/10','R$ 439,00'),
    # Bowls Inox
    card('bowl-inox-19cm.html','i13',
         img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
         'Bowl Inox com Tampa de Vidro 19cm','Aco Inox · 19cm','R$ 399,00', badge='LANCAMENTO'),
    card('frigideira-funda-3ply-signature.html','i14',
         img('dw58a73101','frigideira_sem_anti_aderente_3ply_lecreuset.jpg'),
         'Frigideira Funda 3-Ply Signature','Aco Inox · 24cm','R$ 895,30',
         old_price='R$ 1.279,00'),
    card('bowl-inox-27cm.html','i15',
         img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
         'Bowl Inox com Tampa de Vidro 27cm','Aco Inox · 27cm','R$ 689,00', badge='LANCAMENTO'),
    card('bowl-inox-23cm.html','i16',
         img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
         'Bowl Inox com Tampa de Vidro 23cm','Aco Inox · 23cm','R$ 489,00', badge='LANCAMENTO'),
    card('cacarola-funda-3ply.html','i17',
         img('dwcaff767a','ca%C3%A7arola-funda-3ply-lc.png'),
         'Cacerola Funda 3-Ply Signature','Aco Inox · 3-Ply','R$ 1.799,00 - R$ 2.129,00'),
    card('bowl-inox-com-tampa-de-vidro.html','i18',
         img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
         'Bowl Inox com Tampa de Vidro','Aco Inox · 19cm','R$ 399,00', badge='LANCAMENTO'),
    card('espagueteira-3ply-signature.html','i19',
         img('dw3c93975f','espagueteira_3ply_lecreuset.jpg'),
         'Espagueteira 3-Ply Signature','Aco Inox · 3-Ply','R$ 3.459,00'),
    card('frigideira-saute-3ply-signature.html','i20',
         img('dw45ed6ada','frigideira-saute-com-tampa-3-ply-lc.png'),
         'Frigideira Saute 3-ply Signature','Aco Inox · 3-Ply','R$ 1.829,00'),
    card('panela-molheira-3ply-signature.html','i21',
         img('dw898e26c5','panela-molheira-lecreuset1.png'),
         'Panela Molheira 3-Ply Signature','Aco Inox · 3-Ply · 18cm','R$ 1.282,65',
         old_price='R$ 1.509,00'),
]

products_html = '\n'.join(products)

sidebar = '''<aside class="sidebar">
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Capacidade
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Utensilios</label>
        <label class="filter-option"><input type="checkbox"> Bowls</label>
        <label class="filter-option"><input type="checkbox"> Panelas 3-Ply</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Cor
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <div style="display:flex;gap:8px;padding:4px 0;">
          <span style="width:28px;height:28px;border-radius:50%;background:#C8A882;border:2px solid #ccc;display:inline-block;cursor:pointer;" title="Inox"></span>
        </div>
      </div>
    </div>
  </aside>'''

new = base

new = new.replace('<title>Formatos Especiais | Le Creuset Brasil</title>',
                  '<title>Aco Inox | Le Creuset Brasil</title>')

new = new.replace(
    '<div class="breadcrumb">\n  <a href="index.html">In\u00edcio</a><span>/</span>\n  <a href="#">Cozinhar</a><span>/</span>\n  <span>Formatos Especiais</span>\n</div>',
    '<div class="breadcrumb">\n  <a href="index.html">In\u00edcio</a><span>/</span>\n  <a href="#">Cozinhar</a><span>/</span>\n  <span>A\u00e7o Inox</span>\n</div>'
)

new = new.replace(
    'src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwec30f170/category/Formatos-Especiais2.png" alt="Formatos Especiais Le Creuset"',
    'src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dw257b4fc0/category/cat_banners/banner-categoria-aco-inox.jpg" alt="A\u00e7o Inox Le Creuset"'
)

new = new.replace('<h1>Formatos Especiais</h1>', '<h1>A\u00e7o Inox</h1>')
new = new.replace('<a href="#">A\u00e7o Inox</a>', '<a href="colecao-aco-inox.html">A\u00e7o Inox</a>')

new = re.sub(r'<aside class="sidebar">.*?</aside>', sidebar, new, flags=re.DOTALL)

def replace_grid(m):
    return m.group(1) + '\n' + products_html + '\n    </div>\n  </div>\n</div>\n<div class="mobile-overlay"'

new = re.sub(
    r'(<div class="product-grid">).*?(</div>\s*</div>\s*</div>\s*<div class="mobile-overlay")',
    replace_grid, new, flags=re.DOTALL
)

new = new.replace('<strong>12</strong> resultados', '<strong>22</strong> resultados')
new = new.replace('12 produtos', '22 produtos')

open('colecao-aco-inox.html', 'w', encoding='utf-8').write(new)
print('OK - produtos:', len(products), '- chars:', len(new))
