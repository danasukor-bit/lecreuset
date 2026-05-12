with open('colecao-best-sellers.html', 'r', encoding='utf-8') as f:
    html = f.read()

CDN  = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'
CDN2 = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'

new_css = '''
    /* ===== BEST SELLERS REBUILD ===== */
    .bs-hero { position: relative; width: 100%; height: 500px; overflow: hidden; }
    .bs-hero img { width: 100%; height: 100%; object-fit: cover; object-position: center 30%; }
    .bs-hero-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.28); display: flex; align-items: flex-end; padding: 0 0 60px 80px; }
    .bs-hero-title { color: #fff; font-size: 52px; font-weight: 800; letter-spacing: -1px; }

    .bs-intro { max-width: 900px; margin: 56px auto 0; padding: 0 24px; text-align: center; }
    .bs-intro p { font-size: 14px; color: #444; line-height: 1.8; }

    .bs-illustration { text-align: center; margin: 48px auto; max-width: 600px; padding: 0 24px; }
    .bs-illustration img { width: 100%; height: auto; }

    .bs-main-heading { text-align: center; font-size: 40px; font-weight: 800; letter-spacing: -0.5px; margin: 0 auto 64px; padding: 0 24px; line-height: 1.2; }

    .bs-cat { max-width: 1400px; margin: 0 auto 72px; padding: 0 24px; }
    .bs-cat-label { font-size: 13px; font-weight: 800; color: #fe5000; letter-spacing: 0.5px; margin-bottom: 6px; }
    .bs-cat-label span { margin-left: 4px; }

    /* Split layout: circular image + text */
    .bs-split { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; margin-bottom: 48px; }
    .bs-split-reverse { direction: rtl; }
    .bs-split-reverse > * { direction: ltr; }
    .bs-circle-wrap { position: relative; width: 100%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; }
    .bs-circle-wrap img { width: 100%; height: 100%; object-fit: cover; }
    .bs-split-text h2 { font-size: 28px; font-weight: 800; margin-bottom: 16px; }
    .bs-split-text p { font-size: 14px; color: #444; line-height: 1.7; margin-bottom: 12px; }
    .bs-split-text ul { list-style: disc; padding-left: 20px; margin: 12px 0 20px; }
    .bs-split-text ul li { font-size: 13px; color: #444; line-height: 1.7; }
    .bs-ver-todos { font-size: 12px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #000; border-bottom: 1.5px solid #000; padding-bottom: 2px; display: inline-flex; align-items: center; gap: 6px; }
    .bs-ver-todos:hover { color: #fe5000; border-color: #fe5000; }

    /* Product carousel */
    .bs-products { display: flex; gap: 16px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; padding-bottom: 8px; }
    .bs-products::-webkit-scrollbar { height: 3px; }
    .bs-products::-webkit-scrollbar-thumb { background: #ccc; border-radius: 2px; }
    .bs-prod-card { flex: 0 0 200px; scroll-snap-align: start; text-align: center; }
    .bs-prod-card a { display: block; color: inherit; text-decoration: none; }
    .bs-prod-img { width: 100%; aspect-ratio: 1; background: #f5f5f5; overflow: hidden; margin-bottom: 10px; }
    .bs-prod-img img { width: 100%; height: 100%; object-fit: contain; padding: 10px; transition: transform 0.3s; }
    .bs-prod-card:hover .bs-prod-img img { transform: scale(1.07); }
    .bs-prod-name { font-size: 13px; font-weight: 600; line-height: 1.3; margin-bottom: 4px; }
    .bs-prod-price { font-size: 12px; font-weight: 800; color: #111; margin-bottom: 2px; }
    .bs-prod-star { color: #fe5000; font-size: 14px; }

    /* Section with side image (moedores/ceramica) */
    .bs-side-section { max-width: 1400px; margin: 0 auto 72px; padding: 0 24px; }
    .bs-side-head { font-size: 26px; font-weight: 800; margin-bottom: 8px; }
    .bs-side-desc { font-size: 14px; color: #444; line-height: 1.7; max-width: 700px; margin-bottom: 32px; }
    .bs-side-split { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-bottom: 40px; align-items: start; }
    .bs-side-img img { width: 100%; height: 300px; object-fit: cover; }
    .bs-side-text h3 { font-size: 18px; font-weight: 700; margin-bottom: 10px; }
    .bs-side-text p { font-size: 13px; color: #555; line-height: 1.7; margin-bottom: 10px; }
    .bs-side-text ul { list-style: disc; padding-left: 18px; }
    .bs-side-text ul li { font-size: 13px; color: #555; line-height: 1.7; }

    /* Recipe section */
    .bs-recipes { max-width: 1400px; margin: 0 auto 80px; padding: 0 24px; }
    .bs-recipe-head { text-align: center; margin-bottom: 36px; }
    .bs-recipe-head h2 { font-size: 26px; font-weight: 600; color: #333; margin-bottom: 4px; }
    .bs-recipe-head h3 { font-size: 26px; font-weight: 600; color: #fe5000; }
    .bs-recipe-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
    .bs-recipe-item { text-align: center; }
    .bs-recipe-img { width: 100%; aspect-ratio: 1; overflow: hidden; margin-bottom: 12px; }
    .bs-recipe-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s; }
    .bs-recipe-item:hover .bs-recipe-img img { transform: scale(1.05); }
    .bs-recipe-name { font-size: 14px; font-weight: 400; color: #333; margin-bottom: 12px; }
    .bs-recipe-btn { display: inline-block; padding: 8px 20px; font-size: 12px; font-weight: 600; letter-spacing: 0.5px; border: 1.5px solid #000; color: #000; background: #fff; cursor: pointer; transition: all 0.2s; }
    .bs-recipe-btn:hover { background: #000; color: #fff; }

    @media (max-width: 768px) {
      .bs-hero { height: 220px; }
      .bs-hero-overlay { padding: 0 0 30px 20px; }
      .bs-hero-title { font-size: 28px; }
      .bs-main-heading { font-size: 24px; margin-bottom: 40px; }
      .bs-split, .bs-side-split { grid-template-columns: 1fr; gap: 24px; }
      .bs-split-reverse { direction: ltr; }
      .bs-recipe-grid { grid-template-columns: repeat(2, 1fr); }
      .bs-prod-card { flex: 0 0 145px; }
      .bs-cat { margin-bottom: 48px; }
    }
'''

def prod_card(nome, preco, href, img):
    return f'''      <div class="bs-prod-card">
        <a href="{href}">
          <div class="bs-prod-img"><img src="{img}" alt="{nome}" loading="lazy" /></div>
          <p class="bs-prod-name">{nome}</p>
          <p class="bs-prod-price">R$ {preco}</p>
          <div class="bs-prod-star">&#9733;</div>
        </a>
      </div>'''

ferro_cards = '\n'.join([
    prod_card('Panela Redonda Signature','1.514,25 – R$ 4.399,00','panela-redonda-signature.html',
              CDN+'dwbdcd2587/images/BestSeller/produto-lecreuset-panela-redonda-vermelha.png'),
    prod_card('Panela de Arroz Every','2.199,00','panela-arroz-every.html',
              CDN+'dw08061f78/images/BestSeller/panela-de-arroz-berry.png'),
    prod_card('Caçarola Buffet Signature','2.069,25 – R$ 3.269,00','cacarola-buffet-signature.html',
              CDN+'dw3dbd40c1/images/BestSeller/lecreuset-ca%C3%A7arola-redonda-azure.png'),
    prod_card('Skillet Redonda Signature','1.999,00','skillet-redonda-signature.html',
              CDN+'dw697b3830/images/BestSeller/produto-lecreuset-skillet-laranja%20(1).png'),
])

moedores_cards = '\n'.join([
    prod_card('Moedor de Sal 21cm','369,00','moedor-sal-21cm.html',
              CDN+'dw2cc21ce4/images/BestSeller/moedores-azure.png'),
    prod_card('Moedor de Pimenta 21cm','369,00','moedor-pimenta-21cm.html',
              CDN+'dwd4c4e94a/images/BestSeller/produto-lecreuset-moedores-laranja.png'),
    prod_card('Set Azeite & Vinagre Clássico','579,00','set-azeite-vinagre-classico.html',
              CDN+'dwda943317/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-fundo_brancojpg.jpg'),
    prod_card('Moedor de Pimenta 30cm','479,00','moedor-pimenta-30cm.html',
              CDN+'dw57e0437f/images/BestSeller/best_sellers-mais_vendidos-Moedor_30_cm-fundo_branco.png'),
])

ceramica_cards = '\n'.join([
    prod_card('Pote para Mel','379,00','pote-para-mel.html',
              CDN2+'dw3be00d82/images/BestSeller/best-seller%20(21).jpg?sw=400&sfrm=png'),
    prod_card('Pote de Manteiga','319,00','pote-de-manteiga.html',
              CDN2+'dwae261b1b/images/BestSeller/best-seller%20(29).jpg?sw=400&sfrm=png'),
    prod_card('Pote para Biscoito 2,4L','649,00','pote-para-biscoito.html',
              CDN2+'dwd940b159/images/BestSeller/best-seller%20(41).jpg?sw=400&sfrm=png'),
    prod_card('Pote de Alho','229,00','pote-de-alho.html',
              CDN2+'dwaf47ea8d/images/BestSeller/pote-para-alho-vermelho.jpg?sw=400&sfrm=png'),
    prod_card('Travessa Retangular Heritage','689,00','travessa-retangular-heritage.html',
              CDN+'dwad6ebcf0/images/BestSeller/travessas-produto-lecreuset-heritage-marseille.png'),
    prod_card('Mini Cocotte','167,30 – R$ 239,00','mini-cocotte.html',
              CDN+'dw6db25617/images/BestSeller/mini-cocotte-azure.png'),
])

chaleiras_cards = '\n'.join([
    prod_card('Chaleira Clássica Azure','899,00','chaleira-classica.html',
              CDN+'dwc412fcee/images/BestSeller/chaleira-tradiconal-azure.png'),
    prod_card('Chaleira Clássica','899,00','chaleira-classica.html',
              CDN+'dw05bada9d/images/BestSeller/chaleira-cl%C3%A1ssica-com-apito-bamboo.png'),
    prod_card('Chaleira Clássica Shell Pink','899,00','chaleira-classica.html',
              CDN+'dw265d0f03/images/BestSeller/chaleira-cl%C3%A1ssica-com-apito-shell%20pink.png'),
    prod_card('Chaleira Clássica Cotton','899,00','chaleira-classica.html',
              CDN+'dw13421845/images/BestSeller/chaleira-cotton-classica.png'),
])

new_content = f'''<div class="bs-hero">
  <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw1b33812b/images/BestSeller/4K-TIF-20231123_BAKINGACTI2024_044.jpg?sw=1440&sfrm=png" alt="Best-sellers Le Creuset" />
  <div class="bs-hero-overlay">
    <h1 class="bs-hero-title">Best-sellers</h1>
  </div>
</div>

<div class="bs-intro">
  <p>Alguns produtos conquistam um lugar especial na cozinha &ndash; e no coração de quem ama cozinhar. Nesta seleção, reunimos os <strong>Best-sellers</strong> da Le Creuset, aqueles que fazem sucesso pela qualidade, durabilidade e design inconfundível. Descubra as panelas de ferro fundido mais desejadas, os antiaderentes perfeitos para o dia a dia, moedores que elevam os sabores das receitas, além de canecas, chaleiras e acessórios que unem charme e funcionalidade. Pronto para encontrar seu próximo favorito?</p>
</div>

<div class="bs-illustration">
  <img src="{CDN2}dwb4230871/images/BestSeller/lp-best-seller.jpg?sw=768&sfrm=png" alt="Le Creuset Best-sellers" />
</div>

<h2 class="bs-main-heading">Cozinhar com os melhores faz toda a diferença!</h2>

<!-- FERRO FUNDIDO -->
<div class="bs-cat">
  <div class="bs-cat-label">BEST-SELLER <span>&#9733;</span></div>
  <div class="bs-split">
    <div class="bs-circle-wrap">
      <img src="{CDN2}dweba6c0c9/images/BestSeller/best-seller(51).jpg?sw=768&sfrm=png" alt="Ferro Fundido Le Creuset" />
    </div>
    <div class="bs-split-text">
      <h2>Ferro Fundido Esmaltado!</h2>
      <p>O ferro fundido esmaltado da Le Creuset é um clássico atemporal, projetado para oferecer cozimento uniforme, retenção de calor excepcional e durabilidade incomparável.</p>
      <ul>
        <li>Desenvolvida para garantir conforto e segurança</li>
        <li>Compatibilidade com todas as fontes de calor</li>
        <li>Pegadores e tampas projetados</li>
        <li>Esmalte interior de fácil limpeza</li>
        <li>Ferro mais leve do mercado</li>
        <li>Cores incomparáveis</li>
        <li>Garantia Vitalícia</li>
      </ul>
      <a href="colecao-ferro-fundido.html" class="bs-ver-todos">VER TODOS &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
{ferro_cards}
  </div>
</div>

<!-- MOEDORES & GALHETEIROS -->
<div class="bs-side-section">
  <h2 class="bs-side-head">A Le Creuset trouxe cor à cozinha.</h2>
  <div class="bs-side-split">
    <div class="bs-side-img">
      <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-moedor_de_sal_e_pimenta-le_creuset.jpg" alt="Moedores Le Creuset" />
    </div>
    <div class="bs-side-text">
      <h3>Moedores</h3>
      <p>Feito com resina acrílica (ABS) altamente resistente, tecnologia moderna e proteção contra corrosão, o moedor da Le Creuset possui um mecanismo de moagem em cerâmica que não oxida.</p>
      <ul>
        <li>Recomendamos o uso de pimentas de grãos secos</li>
        <li>Resina Acrílica (ABS) muito resistente</li>
        <li>Resistente a corrosão</li>
        <li>Cores incomparáveis</li>
        <li>Tecnologia Moderna</li>
      </ul>
    </div>
  </div>
  <div class="bs-side-split">
    <div class="bs-side-img">
      <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-le_creuset.jpg" alt="Galheteiros Le Creuset" />
    </div>
    <div class="bs-side-text">
      <h3>Galheteiros</h3>
      <p>O Set de Azeite e vinagre de cerâmica da Le Creuset, também conhecido como Galheteiros trazem conveniência e personalidade à bancada ou mesa.</p>
      <ul>
        <li>Perfeitos para uso e armazenagem de azeite e vinagre</li>
        <li>Cerâmica projetada para uso diário</li>
        <li>10 anos de garantia</li>
      </ul>
      <br><a href="colecao-moedores-e-galheteiro.html" class="bs-ver-todos">VER TODOS &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
{moedores_cards}
  </div>
</div>

<!-- CERÂMICA -->
<div class="bs-side-section">
  <h2 class="bs-side-head">Beleza e desempenho em cada detalhe!</h2>
  <div class="bs-side-split">
    <div class="bs-side-img">
      <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-canecas_de_ceramica_esmaltada-le_creuset.jpg" alt="Cerâmica Le Creuset" />
    </div>
    <div class="bs-side-text">
      <h3>Cerâmica</h3>
      <p>A cerâmica premium da Le Creuset é sinônimo de resistência, versatilidade e elegância. Seu esmalte vitrificado evita a absorção de aromas, sabores e umidade, facilitando a limpeza.</p>
      <ul>
        <li>Retenção de temperatura</li>
        <li>Segura para Lava-louças</li>
        <li>Resistente a arranhões</li>
        <li>Cores incomparáveis</li>
        <li>Garantia de 10 anos</li>
        <li>Fácil limpeza</li>
      </ul>
      <br><a href="colecao-ceramica.html" class="bs-ver-todos">VER TODOS &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
{ceramica_cards}
  </div>
</div>

<!-- CHALEIRAS -->
<div class="bs-cat">
  <div class="bs-cat-label">BEST-SELLER <span>&#9733;</span></div>
  <div class="bs-split bs-split-reverse">
    <div class="bs-circle-wrap">
      <img src="{CDN2}dw807c0f5c/images/BestSeller/bet-seller900.jpg?sw=768&sfrm=png" alt="Chaleiras Le Creuset" />
    </div>
    <div class="bs-split-text">
      <h2>Chaleiras</h2>
      <p>Com design de alta performance, a Chaleira Clássica fabricada em aço carbono esmaltado, oferece aquecimento rápido e distribuição uniforme do calor, garantindo eficiência no preparo de bebidas quentes.</p>
      <p>O pegador e o bico são resistentes ao calor, trazendo mais segurança no manuseio. Além disso, o apito sonoro avisa quando a água atinge o ponto de fervura, tornando o uso ainda mais prático.</p>
      <ul>
        <li>Aquecimento rápido</li>
        <li>Cores incomparáveis</li>
        <li>Garantia de 5 anos</li>
        <li>Segurança Máxima</li>
        <li>Esmalte Vitrificado</li>
        <li>Fácil limpeza</li>
      </ul>
      <br><a href="colecao-chaleiras.html" class="bs-ver-todos">VER TODOS &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
{chaleiras_cards}
  </div>
</div>

<!-- RECEITAS -->
<div class="bs-recipes">
  <div class="bs-recipe-head">
    <h2>Já garantiu o seu Favorito?</h2>
    <h3>Hora de cozinhar!</h3>
  </div>
  <div class="bs-recipe-grid">
    <div class="bs-recipe-item">
      <div class="bs-recipe-img"><img src="{CDN2}dwec7706cf/images/BestSeller/geleia-de-cebola-roxa.jpg?sw=600&sfrm=png" alt="Geleia de Cebola Roxa" loading="lazy" /></div>
      <p class="bs-recipe-name">Geleia de Cebola Roxa</p>
      <a href="#" class="bs-recipe-btn">Ver Receita</a>
    </div>
    <div class="bs-recipe-item">
      <div class="bs-recipe-img"><img src="{CDN2}dw184d5662/images/BestSeller/banner_best_seller-espatula_le_creuset-desenho.jpg?sw=600&sfrm=png" alt="Galette de Maçã" loading="lazy" /></div>
      <p class="bs-recipe-name">Galette de Maçã</p>
      <a href="#" class="bs-recipe-btn">Ver Receita</a>
    </div>
    <div class="bs-recipe-item">
      <div class="bs-recipe-img"><img src="{CDN2}dw1b33812b/images/BestSeller/4K-TIF-20231123_BAKINGACTI2024_044.jpg?sw=600&sfrm=png" alt="Bolo de Mel com Milho" loading="lazy" /></div>
      <p class="bs-recipe-name">Bolo de Mel com Milho</p>
      <a href="#" class="bs-recipe-btn">Ver Receita</a>
    </div>
    <div class="bs-recipe-item">
      <div class="bs-recipe-img"><img src="{CDN2}dw66721f61/images/BestSeller/biscoitos-amanteigados.jpg?sw=600&sfrm=png" alt="Biscoitos Amanteigados" loading="lazy" /></div>
      <p class="bs-recipe-name">Biscoitos Amanteigados</p>
      <a href="#" class="bs-recipe-btn">Ver Receita</a>
    </div>
  </div>
</div>
'''

# Add CSS before </style>
style_end = html.find('  </style>\n</head>')
html = html[:style_end] + new_css + html[style_end:]

# Replace content: from <div class="cat-banner"> to \n<footer>
start = html.find('<div class="cat-banner">')
end   = html.find('\n<footer>')
html  = html[:start] + new_content + html[end:]

with open('colecao-best-sellers.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
