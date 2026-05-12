import urllib.parse

BASE = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'

PRODUCTS = [
    {
        'file': 'set-4-antiaderente-ceramica.html',
        'title': 'Set 4 Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · 2 Frigideiras + 2 Panelas',
        'price': 'R$ 3.889,00',
        'install': 'ou 10x de R$ 388,90 sem juros',
        'sizes': '20 cm, 24 cm, 26 cm e 28 cm',
        'hash': 'dw81821efe',
        'imgfile': 'New_Set4P%C3%A7s2Frigideiras%2B2PanelasEnsc.png',
        'desc': 'O Set 4 Non-Stick Ceramic Essential Le Creuset reúne 2 frigideiras e 2 panelas com revestimento cerâmico antiaderente de última geração. Ideal para montar uma cozinha completa com praticidade e elegância.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Corpo em alumínio fundido','Cabo ergonômico resistente ao calor','Compatível com indução','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'set-2-frigideiras-rasas-24-28cm-antiaderente.html',
        'title': 'Set 2 Frigideiras Rasas Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · 24 cm e 28 cm',
        'price': 'R$ 1.899,00',
        'install': 'ou 10x de R$ 189,90 sem juros',
        'sizes': '24 cm e 28 cm',
        'hash': 'dw50af4581',
        'imgfile': 'Set2FrigideirasRasascomantiaderentedeCer%C3%A2micaEssential.png',
        'desc': 'O Set com 2 Frigideiras Rasas Non-Stick Ceramic Essential Le Creuset combina dois tamanhos versáteis, perfeitos para o dia a dia. O revestimento cerâmico proporciona cozimento saudável e sem aderência.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Cabo ergonômico resistente ao calor','Compatível com indução','Apto para lavalouças','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'set-2-frigideiras-20-26cm-antiaderente.html',
        'title': 'Set 2 Frigideiras Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · 20 cm e 26 cm',
        'price': 'R$ 1.649,00',
        'install': 'ou 10x de R$ 164,90 sem juros',
        'sizes': '20 cm e 26 cm',
        'hash': 'dw0553ccb0',
        'imgfile': 'Set2FrigideirasRasasantiaderentedeCer%C3%A2micaEssential.png',
        'desc': 'O Set com 2 Frigideiras Non-Stick Ceramic Essential Le Creuset é a dupla ideal para refeições cotidianas. Revestimento cerâmico de alta performance para um cozimento saudável.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Cabo ergonômico resistente ao calor','Compatível com indução','Apto para lavalouças','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'frigideira-funda-alca-antiaderente.html',
        'title': 'Frigideira Funda com Alça Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · Fabricada na França',
        'price': 'R$ 1.639,00 – R$ 1.729,00',
        'install': 'ou 10x de R$ 172,90 sem juros',
        'sizes': '28 cm – 30 cm',
        'hash': 'dw4fd3604f',
        'imgfile': 'FrigideiraRasacomAl%C3%A7aAntiaderentedeCer%C3%A2micaEssential.png',
        'desc': 'A Frigideira Funda com Alça Non-Stick Ceramic Essential é ideal para refogar, fritar e preparar molhos. A profundidade extra permite cozinhar grandes porções sem respingos.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Cabo ergonômico resistente ao calor','Compatível com indução','Apto para lavalouças','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'frigideira-rasa-antiaderente.html',
        'title': 'Frigideira Rasa Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · Fabricada na França',
        'price': 'R$ 799,00 – R$ 1.319,00',
        'install': 'ou 10x de R$ 131,90 sem juros',
        'sizes': '20 cm – 30 cm',
        'hash': 'dwca6c3202',
        'imgfile': 'FrigideiraRasaAntiaderentedeCer%C3%A2micaEssential.png',
        'desc': 'A Frigideira Rasa Non-Stick Ceramic Essential Le Creuset é perfeita para ovos, panquecas, carnes e muito mais. Disponível em vários tamanhos para atender todas as necessidades da cozinha.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Cabo ergonômico resistente ao calor','Compatível com indução','Apto para lavalouças','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'molheira-alca-antiaderente.html',
        'title': 'Molheira com Alça Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · Fabricada na França',
        'price': 'R$ 1.149,00 – R$ 1.859,00',
        'install': 'ou 10x de R$ 185,90 sem juros',
        'sizes': '16 cm – 20 cm',
        'hash': 'dw09944880',
        'imgfile': 'MolheiracomAl%C3%A7aAntiaderentedeCer%C3%A2micaEssential.png',
        'desc': 'A Molheira com Alça Non-Stick Ceramic Essential é perfeita para aquecer leite, preparar molhos e sopas. O revestimento cerâmico facilita a limpeza e garante cozimento uniforme.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Tampa inclusa','Cabo ergonômico resistente ao calor','Compatível com indução','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'panela-saute-alca-antiaderente.html',
        'title': 'Panela Saute com Alça Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · Fabricada na França',
        'price': 'R$ 1.419,00',
        'install': 'ou 10x de R$ 141,90 sem juros',
        'sizes': '26 cm',
        'hash': 'dwb6a70bf6',
        'imgfile': 'PanelaSautecomAl%C3%A7aAntiaderentedeCer%C3%A2micaEssential(1).png',
        'desc': 'A Panela Saute com Alça Non-Stick Ceramic Essential combina a versatilidade de uma frigideira com a profundidade de uma panela. Ideal para refogar, brasear e preparar molhos encorpados.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Tampa de vidro inclusa','Cabo ergonômico resistente ao calor','Compatível com indução','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Capacidade','3,8 L'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'cacarola-funda-antiaderente.html',
        'title': 'Caçarola Funda Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · Fabricada na França',
        'price': 'R$ 1.409,00',
        'install': 'ou 10x de R$ 140,90 sem juros',
        'sizes': '20 cm',
        'hash': 'dw8f427a4e',
        'imgfile': 'cacarola_funda_antiaderente_Cer%C3%A2mica_ensc_03.jpg',
        'desc': 'A Caçarola Funda Non-Stick Ceramic Essential é ideal para sopas, ensopados e preparações que exigem mais volume. O revestimento cerâmico garante fácil limpeza e cozimento saudável.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Tampa de vidro inclusa','Duas alças laterais','Compatível com indução','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Capacidade','2,4 L'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'cacarola-baixa-antiaderente.html',
        'title': 'Caçarola Baixa Non-Stick Ceramic Essential',
        'subtitle': 'Antiaderente de Cerâmica · Fabricada na França',
        'price': 'R$ 1.869,00 – R$ 2.529,00',
        'install': 'ou 10x de R$ 252,90 sem juros',
        'sizes': '26 cm – 30 cm',
        'hash': 'dw555e43b8',
        'imgfile': 'Ca%C3%A7arolaBaixaAntiaderentedeCer%C3%A2micaEssential.png',
        'desc': 'A Caçarola Baixa Non-Stick Ceramic Essential é versátil e elegante. Com formato raso e duas alças, é perfeita para assar no forno, preparar gratinados e servir diretamente à mesa.',
        'features': ['Revestimento cerâmico antiaderente','Livre de PFAS e PTFE','Tampa de vidro inclusa','Duas alças laterais','Compatível com forno até 260°C','Fabricado na França'],
        'specs': [('Material','Alumínio com cerâmica'),('Revestimento','Non-Stick Ceramic Essential'),('Garantia','2 anos'),('Compatibilidade','Gás, Elétrico, Indução, Vitrocerâmica, Forno até 260°C'),('Lavalouças','Sim')],
        'color': 'Satin Black', 'colorbg': '#1c1c1c',
    },
    {
        'file': 'tampa-vidro-tns.html',
        'title': 'Tampa de Vidro TNS',
        'subtitle': 'Acessório Non-Stick · Fabricado na França',
        'price': 'R$ 239,00 – R$ 409,00',
        'install': 'ou 10x de R$ 40,90 sem juros',
        'sizes': '20 cm – 30 cm',
        'hash': 'dwa1904ece',
        'imgfile': '96200824000000.jpg',
        'desc': 'A Tampa de Vidro TNS Le Creuset é o acessório ideal para as panelas e frigideiras da linha Non-Stick Ceramic Essential. O vidro temperado permite monitorar o cozimento sem perder calor.',
        'features': ['Vidro temperado resistente','Aro em aço inox','Puxador ergonômico','Compatível com a linha TNS Non-Stick','Apto para lavalouças'],
        'specs': [('Material','Vidro temperado + aço inox'),('Garantia','2 anos'),('Temperatura máxima','180°C'),('Lavalouças','Sim')],
        'color': 'Transparente', 'colorbg': '#d0e8f0',
    },
]

NAV = """    <nav>
      <ul class="nav-list">
        <li>
          <a href="#">Cozinhar</a>
          <div class="dropdown">
            <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
            <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
            <a href="colecao-grelhas.html">Grelhas</a>
            <a href="colecao-antiaderente.html">Antiaderente</a>
            <a href="#">Caçarolas</a>
            <a href="#">Chaleiras</a>
            <a href="#">3-Ply Aço Inox</a>
            <a href="#">Stockpots</a>
          </div>
        </li>
        <li><a href="#">Assar</a></li>
        <li><a href="#">Acessórios</a></li>
        <li><a href="#">Preparar e Servir</a></li>
        <li><a href="#">Coleções</a></li>
        <li class="highlight"><a href="#">Páscoa</a></li>
        <li><a href="#">Ofertas</a></li>
        <li class="blue"><a href="#">Bleu Riviera</a></li>
        <li><a href="#">Lançamentos</a></li>
      </ul>
    </nav>"""

CSS = """    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Nunito Sans', sans-serif; color: #000; background: #fff; }
    a { text-decoration: none; color: inherit; }
    .top-bar { background: #1a1a1a; color: #fff; font-size: 12px; text-align: center; padding: 8px 16px; letter-spacing: 0.5px; }
    header { background: #fff; border-bottom: 1px solid #e5e5e5; position: sticky; top: 0; z-index: 100; }
    .header-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: flex; align-items: center; height: 64px; gap: 24px; }
    .logo { font-size: 22px; font-weight: 800; letter-spacing: -1px; white-space: nowrap; flex-shrink: 0; }
    .logo span { color: #c8102e; }
    nav { flex: 1; }
    .nav-list { display: flex; list-style: none; align-items: center; }
    .nav-list > li { position: relative; }
    .nav-list > li > a { display: block; padding: 22px 14px; font-size: 13px; font-weight: 600; color: #000; white-space: nowrap; border-bottom: 2px solid transparent; transition: border-color 0.2s; }
    .nav-list > li > a:hover { border-bottom-color: #000; }
    .nav-list > li.highlight > a { color: #c8102e; }
    .nav-list > li.blue > a { color: #2563ab; }
    .dropdown { display: none; position: absolute; top: 100%; left: 0; background: #fff; border: 1px solid #e5e5e5; min-width: 200px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); z-index: 200; padding: 12px 0; }
    .nav-list > li:hover .dropdown { display: block; }
    .dropdown a { display: block; padding: 8px 20px; font-size: 13px; color: #333; }
    .dropdown a:hover { background: #f5f5f5; }
    .header-icons { display: flex; align-items: center; gap: 16px; flex-shrink: 0; }
    .header-icons a { font-size: 12px; font-weight: 600; display: flex; flex-direction: column; align-items: center; gap: 2px; color: #000; }
    .header-icons svg { width: 22px; height: 22px; }
    .search-box { display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px; overflow: hidden; height: 36px; }
    .search-box input { border: none; outline: none; padding: 0 12px; font-size: 13px; width: 180px; font-family: inherit; }
    .search-box button { background: #000; border: none; cursor: pointer; padding: 0 12px; height: 100%; display: flex; align-items: center; }
    .search-box button svg { fill: #fff; width: 16px; height: 16px; }
    .breadcrumb { max-width: 1400px; margin: 0 auto; padding: 14px 24px; font-size: 12px; color: #888; display: flex; gap: 6px; align-items: center; }
    .breadcrumb a { color: #888; }
    .breadcrumb a:hover { text-decoration: underline; }
    .breadcrumb span { color: #bbb; }
    .product-wrap { max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; }
    .gallery { position: sticky; top: 80px; }
    .gallery-main { width: 100%; aspect-ratio: 1; background: #f8f8f8; display: flex; align-items: center; justify-content: center; overflow: hidden; cursor: zoom-in; }
    .gallery-main img { width: 100%; height: 100%; object-fit: contain; padding: 24px; transition: transform 0.4s ease; }
    .gallery-main:hover img { transform: scale(1.08); }
    .product-info { padding-top: 4px; }
    .product-badges-top { display: flex; gap: 8px; margin-bottom: 12px; }
    .badge-pill { font-size: 11px; font-weight: 700; padding: 3px 10px; letter-spacing: 0.5px; border: 1px solid #000; }
    .badge-pill.new { background: #000; color: #fff; border-color: #000; }
    .product-title { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; line-height: 1.2; margin-bottom: 6px; }
    .product-subtitle { font-size: 14px; color: #666; margin-bottom: 20px; }
    .product-price-block { margin-bottom: 20px; }
    .price-range { font-size: 22px; font-weight: 700; }
    .price-installment { font-size: 13px; color: #555; margin-top: 4px; }
    .price-pix { font-size: 13px; color: #2a8a2a; margin-top: 3px; font-weight: 600; }
    .color-picker { margin-bottom: 20px; }
    .color-picker-label { font-size: 13px; font-weight: 700; margin-bottom: 10px; display: flex; gap: 6px; align-items: center; }
    .color-picker-label span { font-weight: 400; color: #555; }
    .color-swatches { display: flex; gap: 8px; flex-wrap: wrap; }
    .color-swatch { width: 28px; height: 28px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; transition: transform 0.15s, box-shadow 0.15s; }
    .color-swatch:hover { transform: scale(1.15); }
    .color-swatch.active { box-shadow: 0 0 0 2px #fff, 0 0 0 4px #000; transform: scale(1.1); }
    .qty-row { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
    .qty-label { font-size: 13px; font-weight: 700; }
    .qty-control { display: flex; align-items: center; border: 1px solid #ccc; }
    .qty-btn { width: 36px; height: 36px; background: none; border: none; font-size: 18px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
    .qty-btn:hover { background: #f5f5f5; }
    .qty-input { width: 48px; height: 36px; border: none; border-left: 1px solid #ccc; border-right: 1px solid #ccc; text-align: center; font-size: 14px; font-family: inherit; outline: none; }
    .btn-cart { display: block; width: 100%; background: #000; color: #fff; border: 2px solid #000; padding: 16px; font-size: 14px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer; font-family: inherit; transition: background 0.2s, color 0.2s; margin-bottom: 12px; }
    .btn-cart:hover { background: transparent; color: #000; }
    .btn-wishlist { display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; background: #fff; color: #000; border: 2px solid #000; padding: 14px; font-size: 13px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer; font-family: inherit; transition: background 0.2s; margin-bottom: 24px; }
    .btn-wishlist:hover { background: #f5f5f5; }
    .btn-wishlist svg { width: 18px; height: 18px; }
    .shipping-info { border-top: 1px solid #e5e5e5; padding-top: 20px; margin-bottom: 24px; }
    .shipping-row { display: flex; align-items: center; gap: 10px; font-size: 13px; color: #555; margin-bottom: 8px; }
    .shipping-row svg { width: 18px; height: 18px; flex-shrink: 0; }
    .cep-input { display: flex; margin-top: 10px; }
    .cep-input input { flex: 1; border: 1px solid #ccc; border-right: none; padding: 10px 12px; font-size: 13px; font-family: inherit; outline: none; }
    .cep-input button { background: #000; color: #fff; border: 1px solid #000; padding: 10px 16px; font-size: 12px; font-weight: 700; cursor: pointer; font-family: inherit; }
    .trust-badges-wrap { border-top: 1px solid #e5e5e5; border-bottom: 1px solid #e5e5e5; margin-bottom: 60px; }
    .trust-badges { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: repeat(4, 1fr); }
    .trust-badge { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 32px 20px; border-right: 1px solid #e5e5e5; }
    .trust-badge:last-child { border-right: none; }
    .trust-badge-icon { width: 56px; height: 56px; margin-bottom: 14px; }
    .trust-badge-icon svg { width: 56px; height: 56px; }
    .trust-badge-text { font-size: 14px; font-weight: 700; margin-bottom: 6px; }
    .trust-badge-sub { font-size: 12px; color: #666; line-height: 1.5; max-width: 200px; }
    .product-tabs { max-width: 1400px; margin: 0 auto; padding: 0 24px 60px; }
    .tab { border-top: 1px solid #e5e5e5; }
    .tab:last-child { border-bottom: 1px solid #e5e5e5; }
    .tab-header { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; cursor: pointer; font-size: 15px; font-weight: 700; }
    .tab-header svg { width: 20px; height: 20px; transition: transform 0.3s; flex-shrink: 0; }
    .tab-header.open svg { transform: rotate(180deg); }
    .tab-body { display: none; padding: 0 0 24px; }
    .tab-body.open { display: block; }
    .tab-body p { font-size: 14px; line-height: 1.8; color: #444; margin-bottom: 12px; }
    .tab-body ul { padding-left: 20px; }
    .tab-body ul li { font-size: 14px; line-height: 1.8; color: #444; margin-bottom: 6px; }
    .specs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
    .spec-row { display: flex; padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 13px; }
    .spec-key { font-weight: 700; width: 180px; flex-shrink: 0; color: #555; }
    .spec-val { color: #333; }
    footer { background: #111; color: #fff; padding: 60px 24px 30px; }
    .footer-inner { max-width: 1400px; margin: 0 auto; }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
    .footer-brand .logo { font-size: 20px; margin-bottom: 16px; display: block; }
    .footer-brand p { font-size: 13px; color: #aaa; line-height: 1.7; max-width: 280px; margin-bottom: 20px; }
    .footer-social { display: flex; gap: 12px; }
    .social-btn { width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; }
    .footer-col h4 { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 16px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul li a { font-size: 13px; color: #aaa; }
    .footer-col ul li a:hover { color: #fff; }
    .footer-bottom { border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 12px; color: #666; }
    .payment-icons { display: flex; gap: 8px; }
    .payment-icon { background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }"""

TRUST = """<div class="trust-badges-wrap">
  <div class="trust-badges">
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M32 6 L54 14 L54 34 C54 48 43 56 32 60 C21 56 10 48 10 34 L10 14 Z"/><polyline points="22 32 29 39 42 26"/></svg></div>
      <div class="trust-badge-text">Livre de PFAS</div>
      <div class="trust-badge-sub">Revestimento cerâmico 100% livre de PFAS e PTFE</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="32" r="24"/><path d="M22 32 L29 39 L42 26"/></svg></div>
      <div class="trust-badge-text">2 Anos de Garantia</div>
      <div class="trust-badge-sub">Garantia de 2 anos contra defeitos de fabricação</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="20" width="36" height="24" rx="2"/><path d="M40 28 L52 28 L60 38 L60 44 L40 44 Z"/><circle cx="16" cy="48" r="5"/><circle cx="50" cy="48" r="5"/></svg></div>
      <div class="trust-badge-text">Frete Grátis*</div>
      <div class="trust-badge-sub">Em compras acima de R$ 1.500,00</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M32 8 L36 20 L50 20 L39 28 L43 42 L32 34 L21 42 L25 28 L14 20 L28 20 Z"/></svg></div>
      <div class="trust-badge-text">30 Dias para Trocar</div>
      <div class="trust-badge-sub">Troca ou devolução sem custo em até 30 dias</div>
    </div>
  </div>
</div>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Le <span>Creuset</span></a>
        <p>Desde 1925, Le Creuset fabrica os melhores utensílios de cozinha do mundo. Tradição, qualidade e design em cada peça.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a><a href="#" class="social-btn">in</a><a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul><li><a href="#">Cozinhar</a></li><li><a href="#">Assar</a></li><li><a href="#">Acessórios</a></li><li><a href="#">Coleções</a></li></ul></div>
      <div class="footer-col"><h4>Explore</h4><ul><li><a href="#">100 anos Le Creuset</a></li><li><a href="#">Receitas</a></li><li><a href="#">Blog</a></li><li><a href="#">Lojas Oficiais</a></li></ul></div>
      <div class="footer-col"><h4>Suporte</h4><ul><li><a href="#">Atendimento ao Cliente</a></li><li><a href="#">Uso e Cuidado</a></li><li><a href="#">Devoluções e Trocas</a></li></ul></div>
      <div class="footer-col"><h4>Minha Conta</h4><ul><li><a href="#">Entrar</a></li><li><a href="#">Meus Pedidos</a></li><li><a href="#">Lista de Desejos</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 Le Creuset Brasil. Todos os direitos reservados.</p>
      <div class="payment-icons">
        <span class="payment-icon">VISA</span><span class="payment-icon">MC</span><span class="payment-icon">PIX</span><span class="payment-icon">AMEX</span><span class="payment-icon">BOLETO</span>
      </div>
    </div>
  </div>
</footer>"""

def page(p):
    img_url = f"{BASE}{p['hash']}/images/{p['imgfile']}?sw=650&sh=650&sm=fit"
    feats = '\n'.join(f'        <li>{f}</li>' for f in p['features'])
    specs = '\n'.join(f'          <div class="spec-row"><span class="spec-key">{k}</span><span class="spec-val">{v}</span></div>' for k,v in p['specs'])
    border = ' border-color:#ccc;' if p['colorbg'] in ('#f5f5f0','#fff','#d0e8f0') else ''
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["title"]} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>
{CSS}
  </style>
</head>
<body>

<div class="top-bar">&#x1F69A; Frete Grátis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>

<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
{NAV}
    <div class="header-icons">
      <div class="search-box">
        <input type="text" placeholder="Buscar..." />
        <button><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
      </div>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Entrar</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Lista</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Sacola</span></a>
    </div>
  </div>
</header>

<nav class="breadcrumb">
  <a href="index.html">Início</a>
  <span>&rsaquo;</span>
  <a href="colecao-antiaderente.html">Antiaderente</a>
  <span>&rsaquo;</span>
  <strong>{p["title"]}</strong>
</nav>

<div class="product-wrap">
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImgEl" src="{img_url}" alt="{p["title"]}" />
    </div>
  </div>
  <div class="product-info">
    <div class="product-badges-top">
      <span class="badge-pill new">Novo</span>
      <span class="badge-pill">Livre de PFAS</span>
    </div>
    <h1 class="product-title">{p["title"]}</h1>
    <p class="product-subtitle">{p["subtitle"]}</p>
    <div class="product-price-block">
      <div class="price-range">{p["price"]}</div>
      <div class="price-installment">{p["install"]}</div>
      <div class="price-pix">5% OFF no PIX</div>
    </div>
    <div class="color-picker">
      <div class="color-picker-label">Cor: <span id="colorName">{p["color"]}</span></div>
      <div class="color-swatches">
        <div class="color-swatch active" style="background:{p["colorbg"]};{border}" title="{p["color"]}"
          onclick="selectColor(this,'{p["color"]}','{img_url}')"></div>
      </div>
    </div>
    <div class="qty-row">
      <span class="qty-label">Quantidade</span>
      <div class="qty-control">
        <button class="qty-btn" onclick="changeQty(-1)">&#8722;</button>
        <input class="qty-input" type="number" id="qtyInput" value="1" min="1" />
        <button class="qty-btn" onclick="changeQty(1)">+</button>
      </div>
    </div>
    <button class="btn-cart">Adicionar ao Carrinho</button>
    <button class="btn-wishlist">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Adicionar à Lista de Desejos
    </button>
    <div class="shipping-info">
      <div class="shipping-row">
        <svg viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="1.5"><path d="M1 3h15v13H1zM16 8h4l3 3v5h-7V8zM5.5 21a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM18.5 21a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Calcular frete e prazo de entrega:
      </div>
      <div class="cep-input">
        <input type="text" placeholder="Digite seu CEP" maxlength="9" />
        <button>Calcular</button>
      </div>
    </div>
  </div>
</div>

{TRUST}

<div class="product-tabs">
  <div class="tab">
    <div class="tab-header open" onclick="toggleTab(this)">
      Descrição
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body open">
      <p>{p["desc"]}</p>
      <ul>
{feats}
      </ul>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">
      Especificações Técnicas
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body">
      <div class="specs-grid"><div>
{specs}
      </div></div>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">
      Uso e Cuidado
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body">
      <ul>
        <li>Use fogo médio ou baixo — o revestimento cerâmico distribui calor eficientemente.</li>
        <li>Evite utensílios de metal; prefira silicone, madeira ou nylon.</li>
        <li>Aguarde esfriar antes de lavar para preservar o revestimento.</li>
        <li>Lave com esponja macia e detergente neutro.</li>
        <li>Evite choques térmicos bruscos.</li>
      </ul>
    </div>
  </div>
</div>

{FOOTER}

<script>
  function changeQty(delta) {{
    const input = document.getElementById('qtyInput');
    input.value = Math.max(1, parseInt(input.value) + delta);
  }}
  function toggleTab(header) {{
    const body = header.nextElementSibling;
    const isOpen = body.classList.contains('open');
    header.classList.toggle('open', !isOpen);
    body.classList.toggle('open', !isOpen);
  }}
  function selectColor(el, name, src) {{
    document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
    el.classList.add('active');
    document.getElementById('colorName').textContent = name;
    document.getElementById('mainImgEl').src = src;
  }}
</script>
</body>
</html>'''

for p in PRODUCTS:
    with open(p['file'], 'w', encoding='utf-8') as f:
        f.write(page(p))
    print(f"Created: {p['file']}")
