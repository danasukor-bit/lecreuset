with open('colecao-best-sellers.html', 'r', encoding='utf-8') as f:
    html = f.read()

CDN  = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'
CDN2 = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'

def card(nome, preco, href, img):
    return f'''        <div class="bs-card">
          <a href="{href}">
            <div class="bs-card-img">
              <img src="{img}" alt="{nome}" loading="lazy" />
            </div>
            <p class="bs-card-name">{nome}</p>
            <span class="bs-card-star">&#9733;</span>
            <p class="bs-card-price">R$ {preco}</p>
          </a>
          <a href="{href}" class="bs-btn">Ver Produto</a>
        </div>'''

def section(titulo, link_href, link_label, cards_html):
    return f'''  <div class="bs-section">
    <div class="bs-section-head">
      <h2 class="bs-section-title">{titulo}</h2>
      <a href="{link_href}" class="bs-section-link">{link_label} &rarr;</a>
    </div>
    <div class="bs-carousel">
{cards_html}
    </div>
  </div>'''

ferro = section('Ferro Fundido Esmaltado', 'colecao-ferro-fundido.html', 'Ver Coleção', '\n'.join([
    card('Panela Redonda Signature',  '1.514,25 – R$ 4.399,00', 'panela-redonda-signature.html',
         CDN+'dwbdcd2587/images/BestSeller/produto-lecreuset-panela-redonda-vermelha.png'),
    card('Panela de Arroz Every',     '2.199,00',               'panela-arroz-every.html',
         CDN+'dw08061f78/images/BestSeller/panela-de-arroz-berry.png'),
    card('Caçarola Buffet Signature', '2.069,25 – R$ 3.269,00','cacarola-buffet-signature.html',
         CDN+'dw3dbd40c1/images/BestSeller/lecreuset-ca%C3%A7arola-redonda-azure.png'),
    card('Skillet Redonda Signature', '1.999,00',               'skillet-redonda-signature.html',
         CDN+'dw697b3830/images/BestSeller/produto-lecreuset-skillet-laranja%20(1).png'),
]))

moedores = section('Moedores & Galheteiro', 'colecao-moedores-e-galheteiro.html', 'Ver Coleção', '\n'.join([
    card('Moedor de Sal 21cm',         '369,00', 'moedor-sal-21cm.html',
         CDN+'dw2cc21ce4/images/BestSeller/moedores-azure.png'),
    card('Moedor de Pimenta 21cm',     '369,00', 'moedor-pimenta-21cm.html',
         CDN+'dwd4c4e94a/images/BestSeller/produto-lecreuset-moedores-laranja.png'),
    card('Set Azeite & Vinagre Clássico', '579,00', 'set-azeite-vinagre-classico.html',
         CDN+'dwda943317/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-fundo_brancojpg.jpg'),
    card('Moedor de Pimenta 30cm',     '479,00', 'moedor-pimenta-30cm.html',
         CDN+'dw57e0437f/images/BestSeller/best_sellers-mais_vendidos-Moedor_30_cm-fundo_branco.png'),
]))

ceramica = section('Cerâmica', 'colecao-ceramica.html', 'Ver Coleção', '\n'.join([
    card('Pote para Mel',              '379,00', 'pote-para-mel.html',
         CDN2+'dw3be00d82/images/BestSeller/best-seller%20(21).jpg?sw=768&sfrm=png'),
    card('Pote de Manteiga',           '319,00', 'pote-de-manteiga.html',
         CDN2+'dwae261b1b/images/BestSeller/best-seller%20(29).jpg?sw=768&sfrm=png'),
    card('Pote para Biscoito 2,4L',    '649,00', 'pote-para-biscoito.html',
         CDN2+'dwd940b159/images/BestSeller/best-seller%20(41).jpg?sw=768&sfrm=png'),
    card('Pote de Alho',               '229,00', 'pote-de-alho.html',
         CDN2+'dwaf47ea8d/images/BestSeller/pote-para-alho-vermelho.jpg?sw=768&sfrm=png'),
    card('Travessa Retangular Heritage','689,00', 'travessa-retangular-heritage.html',
         CDN+'dwad6ebcf0/images/BestSeller/travessas-produto-lecreuset-heritage-marseille.png'),
    card('Mini Cocotte',               '167,30 – R$ 239,00', 'mini-cocotte.html',
         CDN+'dw6db25617/images/BestSeller/mini-cocotte-azure.png'),
]))

chaleiras = section('Chaleiras', 'colecao-chaleiras.html', 'Ver Coleção', '\n'.join([
    card('Chaleira Clássica',          '899,00 – R$ 1.299,00', 'chaleira-classica.html',
         CDN+'dw13421845/images/BestSeller/chaleira-cotton-classica.png'),
    card('Chaleira Clássica com Apito','899,00 – R$ 1.299,00', 'chaleira-classica.html',
         CDN+'dw05bada9d/images/BestSeller/chaleira-cl%C3%A1ssica-com-apito-bamboo.png'),
    card('Chaleira Clássica Shell Pink','899,00 – R$ 1.299,00','chaleira-classica.html',
         CDN+'dw265d0f03/images/BestSeller/chaleira-cl%C3%A1ssica-com-apito-shell%20pink.png'),
    card('Chaleira Clássica Azure',    '899,00 – R$ 1.299,00', 'chaleira-classica.html',
         CDN+'dwc412fcee/images/BestSeller/chaleira-tradiconal-azure.png'),
]))

receitas_html = f'''  <div class="bs-section">
    <div class="bs-section-head">
      <h2 class="bs-section-title">Receitas</h2>
      <a href="#" class="bs-section-link">Ver Todas &rarr;</a>
    </div>
    <div class="bs-carousel">
      <div class="bs-recipe-card">
        <a href="#">
          <div class="bs-card-img"><img src="{CDN2}dwec7706cf/images/BestSeller/geleia-de-cebola-roxa.jpg?sw=768&sfrm=png" alt="Geleia de Cebola Roxa" /></div>
          <p class="bs-card-name">Geleia de Cebola Roxa</p>
        </a>
        <a href="#" class="bs-btn bs-btn-outline">Ver Receita</a>
      </div>
      <div class="bs-recipe-card">
        <a href="#">
          <div class="bs-card-img"><img src="{CDN2}dw66721f61/images/BestSeller/biscoitos-amanteigados.jpg?sw=768&sfrm=png" alt="Biscoitos Amanteigados" /></div>
          <p class="bs-card-name">Biscoitos Amanteigados</p>
        </a>
        <a href="#" class="bs-btn bs-btn-outline">Ver Receita</a>
      </div>
    </div>
  </div>'''

new_content = f'''<div class="bs-hero">
  <img src="{CDN2}dw807c0f5c/images/BestSeller/bet-seller900.jpg?sw=1440&sfrm=png" alt="Best-sellers Le Creuset" />
  <div class="bs-hero-overlay">
    <h1 class="bs-hero-title">Best-sellers</h1>
    <p class="bs-hero-sub">Alguns produtos conquistam um lugar especial na cozinha</p>
  </div>
</div>
<div class="bs-page">
{ferro}
{moedores}
{ceramica}
{chaleiras}
{receitas_html}
</div>
'''

new_css = '''
    /* ===== BEST SELLERS PAGE ===== */
    .bs-hero { position: relative; width: 100%; height: 420px; overflow: hidden; }
    .bs-hero img { width: 100%; height: 100%; object-fit: cover; object-position: center 40%; display: block; }
    .bs-hero-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(0,0,0,0.15), rgba(0,0,0,0.5)); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0 20px; }
    .bs-hero-title { color: #fff; font-size: 56px; font-weight: 800; letter-spacing: -1px; text-shadow: 0 2px 12px rgba(0,0,0,0.3); }
    .bs-hero-sub { color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 12px; font-weight: 400; }
    .bs-page { max-width: 1400px; margin: 0 auto; padding: 60px 24px 80px; }
    .bs-section { margin-bottom: 64px; }
    .bs-section-head { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 24px; border-bottom: 2px solid #000; padding-bottom: 12px; }
    .bs-section-title { font-size: 22px; font-weight: 800; letter-spacing: -0.3px; }
    .bs-section-link { font-size: 12px; font-weight: 700; letter-spacing: 0.5px; color: #fe5000; text-transform: uppercase; }
    .bs-section-link:hover { text-decoration: underline; }
    .bs-carousel { display: flex; gap: 20px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; padding-bottom: 12px; scrollbar-width: thin; }
    .bs-carousel::-webkit-scrollbar { height: 4px; }
    .bs-carousel::-webkit-scrollbar-thumb { background: #ddd; border-radius: 4px; }
    .bs-card, .bs-recipe-card { flex: 0 0 220px; scroll-snap-align: start; text-align: center; background: #fff; }
    .bs-card-img { width: 100%; aspect-ratio: 1; background: #f8f8f8; overflow: hidden; margin-bottom: 12px; }
    .bs-card-img img { width: 100%; height: 100%; object-fit: contain; padding: 12px; transition: transform 0.35s ease; }
    .bs-card:hover .bs-card-img img, .bs-recipe-card:hover .bs-card-img img { transform: scale(1.06); }
    .bs-card-name { font-size: 13px; font-weight: 700; line-height: 1.35; margin-bottom: 4px; color: #111; }
    .bs-card-star { font-size: 16px; color: #fe5000; display: block; margin-bottom: 4px; }
    .bs-card-price { font-size: 13px; font-weight: 800; color: #111; margin-bottom: 10px; }
    .bs-btn { display: block; margin: 8px auto 0; padding: 8px 16px; font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; background: #000; color: #fff; border: 1.5px solid #000; cursor: pointer; text-align: center; transition: background 0.2s, color 0.2s; }
    .bs-btn:hover { background: #fff; color: #000; }
    .bs-btn-outline { background: #fff; color: #000; }
    .bs-btn-outline:hover { background: #000; color: #fff; }
    @media (max-width: 768px) {
      .bs-hero { height: 220px; }
      .bs-hero-title { font-size: 32px; }
      .bs-hero-sub { font-size: 13px; }
      .bs-page { padding: 32px 14px 80px; }
      .bs-section { margin-bottom: 40px; }
      .bs-section-title { font-size: 17px; }
      .bs-card, .bs-recipe-card { flex: 0 0 155px; }
      .bs-carousel { gap: 12px; }
    }
'''

# Insert CSS before </style>
style_end = html.find('  </style>\n</head>')
html = html[:style_end] + new_css + html[style_end:]

# Replace content area: from <div class="cat-banner"> to </div>\n<footer>
start = html.find('<div class="cat-banner">')
end = html.find('\n<footer>')
html = html[:start] + new_content + html[end:]

with open('colecao-best-sellers.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
