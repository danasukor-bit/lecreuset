# -*- coding: utf-8 -*-
import os, glob

BASE_CDN = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NAV = '''<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    <nav>
      <ul class="nav-list">
        <li>
          <a href="#">Cozinhar</a>
          <div class="dropdown">
            <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
            <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
            <a href="colecao-grelhas.html">Grelhas</a>
            <a href="colecao-antiaderente.html">Antiaderente</a>
            <a href="colecao-cacarolas.html">Caçarolas</a>
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
    </nav>
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
</header>'''

FOOTER = '''<footer>
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
</footer>'''

PRODUCT_CSS = '''  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
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
    .badge-pill.sale { background: #c8102e; color: #fff; border-color: #c8102e; }
    .badge-pill.limited { background: #8B6914; color: #fff; border-color: #8B6914; }
    .product-title { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; line-height: 1.2; margin-bottom: 6px; }
    .product-subtitle { font-size: 14px; color: #666; margin-bottom: 20px; }
    .product-price-block { margin-bottom: 20px; }
    .price-range { font-size: 24px; font-weight: 800; color: #000; }
    .price-installment { font-size: 13px; color: #555; margin-top: 4px; }
    .price-pix { font-size: 12px; color: #c8102e; font-weight: 700; margin-top: 4px; }
    .color-picker { margin-bottom: 20px; }
    .color-picker-label { font-size: 13px; font-weight: 600; margin-bottom: 10px; }
    .color-swatches { display: flex; gap: 8px; flex-wrap: wrap; }
    .color-swatch { width: 28px; height: 28px; border-radius: 50%; cursor: pointer; border: 2px solid transparent; transition: transform 0.2s, border-color 0.2s; }
    .color-swatch:hover { transform: scale(1.15); }
    .color-swatch.active { border-color: #000; }
    .size-picker { margin-bottom: 20px; }
    .size-picker-label { font-size: 13px; font-weight: 600; margin-bottom: 10px; }
    .size-buttons { display: flex; gap: 8px; flex-wrap: wrap; }
    .size-btn { border: 1px solid #ccc; padding: 8px 16px; font-size: 13px; font-family: inherit; cursor: pointer; background: #fff; transition: border-color 0.2s, background 0.2s; }
    .size-btn:hover, .size-btn.active { border-color: #000; background: #000; color: #fff; }
    .qty-row { display: flex; align-items: center; gap: 16px; margin-bottom: 16px; }
    .qty-label { font-size: 13px; font-weight: 600; }
    .qty-control { display: flex; align-items: center; border: 1px solid #ccc; }
    .qty-btn { width: 36px; height: 36px; background: none; border: none; cursor: pointer; font-size: 18px; display: flex; align-items: center; justify-content: center; }
    .qty-btn:hover { background: #f5f5f5; }
    .qty-input { width: 48px; height: 36px; border: none; border-left: 1px solid #ccc; border-right: 1px solid #ccc; text-align: center; font-size: 14px; font-family: inherit; outline: none; }
    .btn-cart { width: 100%; background: #000; color: #fff; border: none; padding: 16px; font-size: 14px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer; font-family: inherit; margin-bottom: 12px; transition: background 0.2s; }
    .btn-cart:hover { background: #222; }
    .btn-wishlist { width: 100%; background: #fff; color: #000; border: 1px solid #000; padding: 14px; font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 24px; transition: background 0.2s; }
    .btn-wishlist:hover { background: #f5f5f5; }
    .btn-wishlist svg { width: 18px; height: 18px; }
    .shipping-info { border-top: 1px solid #e5e5e5; padding-top: 20px; }
    .shipping-row { font-size: 13px; color: #555; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
    .shipping-row svg { width: 18px; height: 18px; flex-shrink: 0; }
    .cep-input { display: flex; gap: 8px; }
    .cep-input input { flex: 1; border: 1px solid #ccc; padding: 8px 12px; font-size: 13px; font-family: inherit; outline: none; }
    .cep-input button { background: #000; color: #fff; border: none; padding: 8px 16px; font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; }
    .trust-badges-wrap { background: #f8f8f8; padding: 32px 24px; margin-bottom: 0; }
    .trust-badges { max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
    .trust-badge { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; }
    .trust-badge-icon svg { width: 40px; height: 40px; }
    .trust-badge-text { font-size: 13px; font-weight: 700; }
    .trust-badge-sub { font-size: 11px; color: #666; }
    .product-tabs { max-width: 1400px; margin: 0 auto; padding: 0 24px 60px; }
    .tab { border-bottom: 1px solid #e5e5e5; }
    .tab-header { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; cursor: pointer; font-size: 15px; font-weight: 700; }
    .tab-header svg { width: 20px; height: 20px; transition: transform 0.3s; flex-shrink: 0; }
    .tab-header.open svg { transform: rotate(180deg); }
    .tab-body { display: none; padding: 0 0 24px; }
    .tab-body.open { display: block; }
    .tab-body p { font-size: 14px; line-height: 1.8; color: #444; margin-bottom: 12px; }
    .tab-body ul { padding-left: 20px; }
    .tab-body ul li { font-size: 14px; line-height: 1.8; color: #444; margin-bottom: 6px; }
    .specs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
    .spec-row { display: flex; padding: 10px 0; border-bottom: 1px solid #f0f0f0; gap: 16px; }
    .spec-key { font-size: 13px; color: #888; min-width: 160px; flex-shrink: 0; }
    .spec-val { font-size: 13px; font-weight: 600; }
    footer { background: #111; color: #fff; padding: 60px 24px 30px; }
    .footer-inner { max-width: 1400px; margin: 0 auto; }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
    .footer-brand .logo { font-size: 20px; margin-bottom: 16px; display: block; }
    .footer-brand p { font-size: 13px; color: #aaa; line-height: 1.7; max-width: 280px; margin-bottom: 20px; }
    .footer-social { display: flex; gap: 12px; }
    .social-btn { width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; transition: border-color 0.2s, background 0.2s; }
    .social-btn:hover { border-color: #fff; background: rgba(255,255,255,0.1); }
    .footer-col h4 { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 16px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul li a { font-size: 13px; color: #aaa; transition: color 0.2s; }
    .footer-col ul li a:hover { color: #fff; }
    .footer-bottom { border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 12px; color: #666; }
    .payment-icons { display: flex; gap: 8px; }
    .payment-icon { background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }'''

PRODUCTS = [
    {
        'file': 'cacarola-buffet-signature.html',
        'title': 'Caçarola Buffet Signature',
        'subtitle': 'Ferro Fundido Esmaltado · 26 cm – 30 cm',
        'price': 'R$ 2.069,25 – R$ 3.269,00',
        'install': 'ou 10x de R$ 326,90 sem juros',
        'sizes_label': '26 cm – 30 cm',
        'hash': 'dwb398291e',
        'imgfile': 'produto-lecreuset-ca%C3%A7arola-redonda-peche.png',
        'badge': '',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido Esmaltado',
        'color_name': 'Pêche',
        'color_bg': '#E8A87C',
        'desc_p': 'A Caçarola Buffet Signature Le Creuset é funcional e elegante — leve-a do forno diretamente para a mesa como uma peça de servir sofisticada ou use-a como acessório decorativo na cozinha. O ferro fundido esmaltado da Le Creuset, o mais leve do mercado, oferece distribuição e retenção de calor superior, mantendo os alimentos na temperatura ideal por mais tempo.',
        'desc_items': [
            'Disponível nos tamanhos 26 cm e 30 cm',
            'Tampa hermética circula o vapor e devolve a umidade aos alimentos',
            'Pegador em aço inox seguro em qualquer temperatura do forno',
            'Interior esmaltado em areia vitrificado — não absorve aromas nem sabores',
            'Exterior esmaltado resistente a manchas, lascas e rachaduras',
        ],
        'features': [
            'Ferro fundido esmaltado — o mais leve do mercado, com distribuição e retenção de calor superior',
            'Pronto para usar — não requer tempero',
            'Tampa hermética projeta o vapor de volta para os alimentos, mantendo suculência',
            'Pegador em aço inox resistente a qualquer temperatura de forno',
            'Esmalte durável, resistente a manchas, lascas e rachaduras',
            'Compatível com lava-louças e utensílios de metal',
            'Disponível em diversas cores exclusivas Le Creuset',
        ],
        'specs': [
            ('Tamanhos disponíveis', '26 cm e 30 cm'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Lavalouças', 'Sim'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro.',
            'Evite mudanças bruscas de temperatura — não leve da geladeira diretamente ao forno.',
            'Use fogo médio — o ferro fundido distribui o calor eficientemente e não requer fogo alto.',
            'Utensílios de madeira, silicone ou nylon preservam o esmalte por mais tempo.',
            'Para limpar, aguarde esfriar e lave com esponja macia e detergente neutro.',
            'Manchas persistentes respondem a imersão em água morna com bicarbonato.',
            'Seque completamente antes de guardar para evitar manchas de oxidação nas bordas.',
        ],
    },
    {
        'file': 'cacarola-buffet-signature-petal.html',
        'title': 'Caçarola Buffet Signature Petal',
        'subtitle': 'Ferro Fundido Esmaltado · 26 cm',
        'price': 'R$ 2.949,00 – R$ 3.079,00',
        'install': 'ou 10x de R$ 307,90 sem juros',
        'sizes_label': '26 cm',
        'hash': 'dwdc236776',
        'imgfile': 'ca%C3%A7arola-buffet-signature-petal-seasalt%20(2).png',
        'badge': '',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido',
        'color_name': 'Sea Salt',
        'color_bg': '#B8D4D0',
        'desc_p': 'A Caçarola Buffet Signature Petal da Le Creuset é funcional e bonita — leve-a do forno para a mesa como uma elegante peça de servir ou use-a como acessório decorativo. O design floral exclusivo Petal combina a lendária performance do ferro fundido esmaltado com uma estética delicada e sofisticada.',
        'desc_items': [
            'Design floral exclusivo Petal em ferro fundido esmaltado',
            'Tampa de excelente vedação promove circulação de calor e umidade',
            'Alças espaçosas acomodam luvas de forno espessas',
            'Pegadores em aço inox resistentes a qualquer temperatura de forno',
            'Interior esmaltado em areia vitrificado — não absorve aromas nem sabores',
            'Dimensões: 26 cm L × 26 cm W × 9,8 cm H',
        ],
        'features': [
            'Design Petal exclusivo com esmalte exterior resistente a lascas e rachaduras',
            'Interior esmaltado em areia vitrificado, não absorve aromas ou sabores',
            'Tampa de excelente vedação promove circulação consistente de calor e umidade',
            'Alças espaçosas para manuseio seguro com luvas espessas',
            'Pegadores em aço inox resistentes a qualquer temperatura de forno',
            'Garantia vitalícia contra defeitos de fabricação',
        ],
        'specs': [
            ('Tamanho', '26 cm'),
            ('Dimensões', '26 cm L × 26 cm W × 9,8 cm H'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Lavalouças', 'Lavagem à mão recomendada'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Lave à mão para preservar o design e o esmalte do Petal.',
            'Evite mudanças bruscas de temperatura.',
            'Use fogo médio — o ferro fundido distribui o calor eficientemente.',
            'Prefira utensílios de madeira ou silicone para preservar o esmalte.',
            'Aguarde esfriar antes de lavar com esponja macia e detergente neutro.',
            'Seque completamente antes de guardar.',
        ],
    },
    {
        'file': 'cacarola-buffet-abobora.html',
        'title': 'Caçarola Buffet Signature Abóbora com Pegador Dourado',
        'subtitle': 'Ferro Fundido Esmaltado · 28 cm · 2,50L',
        'price': 'R$ 4.269,00',
        'install': 'ou 10x de R$ 426,90 sem juros',
        'sizes_label': '28 cm · 2,50L',
        'hash': 'dw37d8acb7',
        'imgfile': 'ca%C3%A7arola-buffet-signature-abobora-pegador-dourado-marronnier-28cm.png',
        'badge': '',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido Esmaltado',
        'color_name': 'Marronnier',
        'color_bg': '#6B4226',
        'desc_p': 'A Caçarola Buffet Signature Abóbora com Pegador Dourado combina sofisticação e funcionalidade em um design icônico inspirado na abóbora. O pegador de aço inox dourado esculpido à mão adiciona um toque de elegância premium. O ferro fundido esmaltado garante distribuição e retenção de calor excepcionais para sopas, refogados e assados.',
        'desc_items': [
            'Design exclusivo inspirado na abóbora em ferro fundido esmaltado',
            'Pegador em aço inox dourado esculpido à mão',
            'Cria crostas douradas marcadas com os três anéis Le Creuset',
            'Capacidade de 2,50L — ideal para sopas e ensopados',
            'Disponível nas cores Marronnier, Meringue e Branco',
            'Resistente a manchas, lascas e rachaduras',
        ],
        'features': [
            'Pegador em aço inox dourado esculpido à mão — elegância premium',
            'Ferro fundido esmaltado lendário com distribuição e retenção de calor excepcionais',
            'Cria crostas douradas e crocantes marcadas com os três anéis Le Creuset',
            'Resistente a manchas, lascas e rachaduras',
            'Lavagem à mão recomendada',
            'Seguro no forno até 250°C',
            'Garantia vitalícia contra defeitos de fabricação',
        ],
        'specs': [
            ('Tamanho', '28 cm'),
            ('Capacidade', '2,50L'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Fontes de calor', 'Gás, elétrico, indução, radiante, grelha, forno'),
            ('Temperatura máxima (forno)', '250°C'),
            ('Lavalouças', 'Lavagem à mão recomendada'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Lave à mão — o pegador dourado e o design especial merecem cuidado delicado.',
            'Evite mudanças bruscas de temperatura.',
            'Não exceda 250°C no forno.',
            'Prefira utensílios de madeira ou silicone.',
            'Aguarde esfriar antes de lavar com esponja macia e detergente neutro.',
            'Seque completamente antes de guardar.',
        ],
    },
    {
        'file': 'cacarola-buffet-flamme-doree.html',
        'title': 'Caçarola Buffet Signature Flamme Dorée',
        'subtitle': 'Edição Limitada Centenário · 30 cm · 3,5L',
        'price': 'R$ 3.449,00',
        'install': 'ou 10x de R$ 344,90 sem juros',
        'sizes_label': '30 cm · 3,5L',
        'hash': 'dwe3d241cf',
        'imgfile': '100%20Anos/Cacarola-redonda-flame-doree.png',
        'badge': 'limited',
        'badge_text': 'Edição Limitada',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido Esmaltado',
        'color_name': 'Flamme Dorée',
        'color_bg': '#D4A017',
        'desc_p': 'A Caçarola Buffet Signature Flamme Dorée é uma edição limitada que celebra o centenário da Le Creuset reinterpretando com sofisticação a clássica cor Flame de 1925. O esmalte incorpora minerais naturais que criam reflexos dourados luminosos, com um pegador em aço inox dourado gravado com os anéis concêntricos da marca — uma peça única que une história e inovação.',
        'desc_items': [
            'Edição limitada Centenário 100 anos Le Creuset',
            'Cor Flamme Dorée reinterpreta o clássico Flame de 1925',
            'Esmalte com minerais naturais para reflexos dourados luminosos',
            'Pegador em aço inox dourado gravado com os anéis concêntricos Le Creuset',
            'Tamanho: 30 cm · Capacidade: 3,5L · Dimensões: 30×30×13,5 cm',
        ],
        'features': [
            'Edição limitada Centenário — cor exclusiva Flamme Dorée',
            'Esmalte vibrante com minerais naturais para reflexos dourados',
            'Interior esmaltado em areia vitrificado — não absorve aromas nem sabores',
            'Alças largas e ergonômicas',
            'Pegador em aço inox dourado resistente ao calor',
            'Construção em ferro fundido para distribuição uniforme de calor',
        ],
        'specs': [
            ('Tamanho', '30 cm'),
            ('Capacidade', '3,5L'),
            ('Dimensões', '30 cm L × 30 cm W × 13,5 cm H'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Lavalouças', 'Lavagem à mão recomendada'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Lave à mão para preservar o esmalte e o pegador dourado.',
            'Evite mudanças bruscas de temperatura.',
            'Use fogo médio — o ferro fundido distribui o calor eficientemente.',
            'Prefira utensílios de madeira ou silicone.',
            'Aguarde esfriar antes de lavar com esponja macia e detergente neutro.',
            'Seque completamente antes de guardar.',
        ],
    },
    {
        'file': 'cacarola-funda-3ply.html',
        'title': 'Caçarola Funda 3-Ply Signature',
        'subtitle': 'Aço Inox 3 Camadas · 20 cm – 24 cm',
        'price': 'R$ 1.799,00 – R$ 2.129,00',
        'install': 'ou 10x de R$ 212,90 sem juros',
        'sizes_label': '20 cm e 24 cm',
        'hash': 'dwcaff767a',
        'imgfile': 'ca%C3%A7arola-funda-3ply-lc.png',
        'badge': '',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'Portugal',
        'material': '3-Ply Aço Inox',
        'color_name': 'Aço Inox',
        'color_bg': '#C0C0C0',
        'desc_p': 'A Caçarola Funda 3-Ply Signature combina construção de três camadas — com núcleo de alumínio da base até a borda — para aquecimento rápido e distribuição uniforme do calor. Ideal para sopas, caldos e ensopados, a construção em aço inox com titânio resiste a queimaduras e corrosão em temperaturas elevadas.',
        'desc_items': [
            'Disponível nos tamanhos 20 cm (R$ 1.799,00) e 24 cm (R$ 2.129,00)',
            'Construção tripla com núcleo de alumínio da base até a borda',
            'Borda sem gotejamento para despejar com precisão',
            'Ventilação integrada na tampa para evitar transbordamento',
            'Alças ergonômicas para manuseio seguro',
        ],
        'features': [
            'Construção 3 camadas com núcleo de alumínio da base até a borda — aquecimento rápido e uniforme',
            'Aço inox com titânio no exterior — resiste a queimaduras e corrosão em altas temperaturas',
            'Tampa icônica com três anéis e botão de fácil preensão — estabilizadores para encaixe perfeito',
            'Ventilação integrada na tampa evita transbordamento',
            'Borda sem gotejamento para despejar com precisão',
            'Compatível com todos os tipos de fogão e lava-louças',
            'Seguro para utensílios de metal',
        ],
        'specs': [
            ('Tamanhos disponíveis', '20 cm e 24 cm'),
            ('Material', '3-Ply Aço Inox'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Lavalouças', 'Sim'),
            ('Origem', 'Portugal'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Compatível com lava-louças, mas a lavagem à mão prolonga o brilho.',
            'Para manchas de alimentos queimados, encha com água e leve ao fogo.',
            'Evite produtos abrasivos que possam arranhar o aço inox.',
            'Seque imediatamente após a lavagem para evitar marcas de água.',
            'Não use palha de aço.',
        ],
    },
    {
        'file': 'set-4-mini-buffet-tampa-gourmand.html',
        'title': 'Set com 4 Mini Buffet com Tampa Gourmand 13cm',
        'subtitle': 'Coleção Gourmand · Ferro Fundido Esmaltado · Matte Black',
        'price': 'R$ 4.199,25',
        'install': 'ou 10x de R$ 419,93 sem juros',
        'sizes_label': '13 cm · Matte Black',
        'hash': 'dw8cdcc97c',
        'imgfile': 'SET-4-BUFFET-C-TAMPA-13CM-GOURMAND10.png',
        'badge': 'sale',
        'badge_text': 'Oferta',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido Esmaltado',
        'color_name': 'Matte Black',
        'color_bg': '#1C1C1C',
        'desc_p': 'A Coleção Gourmand Le Creuset foi desenvolvida para quem domina a arte da hospitalidade. Este conjunto com 4 Mini Buffets com Tampa em ferro fundido esmaltado Matte Black combina funcionalidade e estilo para uma apresentação individual impecável — ideal para pratos principais, acompanhamentos, massas ou sobremesas servidos diretamente do forno à mesa.',
        'desc_items': [
            '4 Mini Buffets com Tampa em ferro fundido esmaltado Matte Black',
            'Design empilhável para economia de espaço',
            'Paredes internas curvas e fundos planos facilitam preparo e limpeza',
            'Alças largas e curvas para manuseio confortável',
            'Suporta temperaturas de até 450°C',
            'Compatível com lava-louças residenciais e industriais',
        ],
        'features': [
            'Design empilhável para armazenamento conveniente',
            'Paredes internas curvas com fundos planos para preparo e limpeza facilitados',
            'Alças largas e curvas para manuseio ergonômico',
            'Esmalte Matte Black resistente a manchas, arranhões, lascas e ferrugem',
            'Distribuição e retenção de calor superiores',
            'Desenvolve pátina natural ao longo do tempo, melhorando a performance',
            'Pronto para usar — não requer tempero',
            'Compatível com lava-louças residenciais e industriais',
        ],
        'specs': [
            ('Conteúdo', '4 Mini Buffets com Tampa'),
            ('Diâmetro', '13 cm (12,7 cm L × 12,7 cm W)'),
            ('Altura', '3,3 cm'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Cor', 'Matte Black'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '450°C'),
            ('Lavalouças', 'Sim (residencial e industrial)'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Compatível com lava-louças — pode ser lavado em lava-louças residenciais e industriais.',
            'Para melhor resultado e maior durabilidade, lave à mão com esponja macia.',
            'Evite quedas e impactos que possam danificar o esmalte.',
            'O esmalte Matte Black desenvolve pátina natural ao longo do tempo — isso é normal e desejável.',
            'Seque completamente antes de guardar.',
        ],
    },
    {
        'file': 'cacarola-aco-esmaltado.html',
        'title': 'Caçarola Aço Esmaltado',
        'subtitle': 'Lançamento · Aço Esmaltado · 20 cm · 3,7L',
        'price': 'R$ 789,00',
        'install': 'ou 10x de R$ 78,90 sem juros',
        'sizes_label': '20 cm · 3,7L',
        'hash': 'dwf6a52a4e',
        'imgfile': 'Ca%C3%A7arola%20Redonda%20A%C3%A7o%20Inox-cool-mint%20(3).png',
        'badge': 'new',
        'badge_text': 'Novo',
        'warranty_label': 'Garantia 5 anos',
        'warranty_sub': 'Garantia de 5 anos contra defeitos de fabricação',
        'warranty_spec': '5 anos',
        'origin': 'Tailândia',
        'material': 'Aço Esmaltado',
        'color_name': 'Cool Mint',
        'color_bg': '#A8D8C8',
        'desc_p': 'Lançamento da Le Creuset, a Caçarola Aço Esmaltado traz o design e a qualidade da marca em um produto de aço esmaltado com fenomenal distribuição de calor. Com formato redondo otimizado para o cozimento do dia a dia, ela é versátil para o fogão e para o forno, com capacidade de 3,7L e botão em fenólico.',
        'desc_items': [
            'Formato redondo otimizado para o cozimento do dia a dia',
            'Capacidade de 3,7L — ideal para refeições em família',
            'Botão em fenólico resistente ao calor',
            'Interior esmaltado de fácil limpeza',
            'Lançamento exclusivo na cor Cool Mint',
            'Dimensões: 20 cm L × 20 cm W × 16,9 cm H',
        ],
        'features': [
            'Aço esmaltado com fenomenal distribuição de calor',
            'Formato redondo otimizado para o cozimento cotidiano',
            'Botão em fenólico resistente ao calor',
            'Interior esmaltado para fácil limpeza',
            'Versátil — fogão e forno',
            'Lavagem à mão recomendada (interior lava-louças)',
        ],
        'specs': [
            ('Tamanho', '20 cm'),
            ('Capacidade', '3,7L'),
            ('Dimensões', '20 cm L × 20 cm W × 16,9 cm H'),
            ('Material', 'Aço Esmaltado'),
            ('Fontes de calor', 'Gás, elétrico, indução, radiante, grelha, forno'),
            ('Botão', 'Fenólico'),
            ('Lavalouças', 'Lavagem à mão recomendada'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos'),
        ],
        'care': [
            'Lavagem à mão recomendada para o exterior — interior pode ir ao lava-louças.',
            'Evite aquecimento excessivo em fogo alto.',
            'Use utensílios de madeira, silicone ou nylon para não riscar o esmalte.',
            'Aguarde esfriar antes de lavar.',
            'Evite esponjas abrasivas.',
        ],
    },
    {
        'file': 'cacarola-buffet-modern-heritage.html',
        'title': 'Caçarola Buffet Modern Heritage',
        'subtitle': 'Ferro Fundido Esmaltado · 28 cm',
        'price': 'R$ 3.819,00',
        'install': 'ou 10x de R$ 381,90 sem juros',
        'sizes_label': '28 cm',
        'hash': 'dw5a6b2fa5',
        'imgfile': 'cacarola-buffet-28Cm-Modern-laranja-Heritage.png',
        'badge': '',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido Esmaltado',
        'color_name': 'Laranja',
        'color_bg': '#d46820',
        'desc_p': 'A Caçarola Buffet Modern Heritage é uma reinterpretação moderna do icônico design Heritage da Le Creuset. Celebrando as origens francesas da marca, esta peça preserva a essência atemporal da Le Creuset com alça arqueada clássica e alças laterais em relevo, unindo nostalgia e inovação culinária.',
        'desc_items': [
            'Reinterpretação moderna do icônico design Heritage Le Creuset',
            'Alça arqueada clássica e alças laterais em relevo',
            'Interior esmaltado em areia vitrificado — não absorve aromas nem sabores',
            'Tampa com excelente vedação para circulação consistente de calor e umidade',
            'Alças espaçosas acomodam luvas de forno espessas',
            'Disponível nas cores Laranja e Meringue',
        ],
        'features': [
            'Design Heritage icônico — alça arqueada clássica e alças laterais em relevo',
            'Esmalte exterior resistente — previne lascas e rachaduras',
            'Interior esmaltado em areia vitrificado, não absorve aromas ou sabores',
            'Tampa de excelente vedação para circulação consistente de calor e umidade',
            'Alças espaçosas para transferência segura com luvas espessas',
            'Pegadores em aço inox resistentes a qualquer temperatura de forno',
        ],
        'specs': [
            ('Tamanho', '28 cm'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Lavalouças', 'Sim'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro.',
            'Evite mudanças bruscas de temperatura.',
            'Use fogo médio — o ferro fundido distribui o calor eficientemente.',
            'Prefira utensílios de madeira ou silicone.',
            'Aguarde esfriar antes de lavar com esponja macia e detergente neutro.',
            'Seque completamente antes de guardar.',
        ],
    },
    {
        'file': 'set-4-mini-buffet-gourmand.html',
        'title': 'Set com 4 Mini Buffet Gourmand 13cm',
        'subtitle': 'Coleção Gourmand · Ferro Fundido Esmaltado · Matte Black',
        'price': 'R$ 2.624,25',
        'install': 'ou 10x de R$ 262,43 sem juros',
        'sizes_label': '13 cm · Matte Black',
        'hash': 'dw8eda217c',
        'imgfile': 'SET-4-BUFFET-13CM-GOURMAND7.png',
        'badge': 'sale',
        'badge_text': 'Oferta',
        'warranty_label': 'Garantia Vitalícia',
        'warranty_sub': 'Garantia vitalícia contra defeitos de fabricação',
        'warranty_spec': 'Vitalícia',
        'origin': 'França',
        'material': 'Ferro Fundido Esmaltado',
        'color_name': 'Matte Black',
        'color_bg': '#1C1C1C',
        'desc_p': 'A Coleção Gourmand Le Creuset foi cuidadosamente desenvolvida para quem domina a arte da hospitalidade. Este conjunto com 4 Mini Buffets em ferro fundido esmaltado Matte Black combina qualidade duradoura e atenção aos mínimos detalhes, com vasilhas redondas individuais projetadas para ir do forno à mesa servindo pratos principais, acompanhamentos, massas ou sobremesas.',
        'desc_items': [
            '4 Mini Buffets (sem tampa) em ferro fundido esmaltado Matte Black',
            'Design empilhável para economia de espaço',
            'Paredes internas curvas e fundos planos facilitam preparo e limpeza',
            'Alças largas e curvas para manuseio confortável',
            'Suporta temperaturas de até 450°C',
            'Compatível com lava-louças residenciais e industriais',
        ],
        'features': [
            'Design empilhável para armazenamento conveniente',
            'Paredes internas curvas com fundos planos para preparo e limpeza facilitados',
            'Alças largas e curvas para manuseio ergonômico',
            'Esmalte Matte Black resistente a manchas, arranhões, lascas e ferrugem',
            'Distribuição e retenção de calor superiores',
            'Desenvolve pátina natural ao longo do tempo, melhorando a performance',
            'Compatível com lava-louças residenciais e industriais',
        ],
        'specs': [
            ('Conteúdo', '4 Mini Buffets sem Tampa'),
            ('Dimensões', '12,7 cm L × 12,7 cm W × 3,3 cm H'),
            ('Material', 'Ferro Fundido Esmaltado'),
            ('Cor', 'Matte Black'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Temperatura máxima', '450°C'),
            ('Lavalouças', 'Sim (residencial e industrial)'),
            ('Origem', 'França'),
            ('Garantia', 'Vitalícia'),
        ],
        'care': [
            'Compatível com lava-louças residenciais e industriais.',
            'Para maior durabilidade, lave à mão com esponja macia e detergente neutro.',
            'O esmalte Matte Black desenvolve pátina natural — isso é normal e desejável.',
            'Evite quedas e impactos que possam danificar o esmalte.',
            'Seque completamente antes de guardar.',
        ],
    },
]


def img_url(p):
    return f'{BASE_CDN}{p["hash"]}/images/{p["imgfile"]}?sw=650&sh=650&sm=fit'


def make_product_page(p):
    url = img_url(p)
    badge_html = ''
    if p.get('badge') == 'new':
        badge_html = f'<span class="badge-pill new">{p.get("badge_text","Novo")}</span>\n      '
    elif p.get('badge') == 'sale':
        badge_html = f'<span class="badge-pill sale">{p.get("badge_text","Oferta")}</span>\n      '
    elif p.get('badge') == 'limited':
        badge_html = f'<span class="badge-pill limited">{p.get("badge_text","Edição Limitada")}</span>\n      '

    feat_li = ''.join(f'\n        <li>{f}</li>' for f in p['features'])
    care_li = ''.join(f'\n        <li>{c}</li>' for c in p['care'])
    desc_li = ''.join(f'\n        <li>{d}</li>' for d in p['desc_items'])
    spec_rows = ''.join(
        f'\n          <div class="spec-row"><span class="spec-key">{k}</span><span class="spec-val">{v}</span></div>'
        for k, v in p['specs']
    )

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["title"]} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>
{PRODUCT_CSS}
  </style>
</head>
<body>

<div class="top-bar">🚚 Frete Grátis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>

{NAV}

<nav class="breadcrumb">
  <a href="index.html">Início</a>
  <span>&rsaquo;</span>
  <a href="colecao-cacarolas.html">Caçarolas</a>
  <span>&rsaquo;</span>
  <strong>{p["title"]}</strong>
</nav>

<div class="product-wrap">
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImgEl" src="{url}" alt="{p["title"]}" />
    </div>
  </div>
  <div class="product-info">
    <div class="product-badges-top">
      {badge_html}<span class="badge-pill">Ferro Fundido</span>
    </div>
    <h1 class="product-title">{p["title"]}</h1>
    <p class="product-subtitle">{p["subtitle"]}</p>
    <div class="product-price-block">
      <div class="price-range">{p["price"]}</div>
      <div class="price-installment">{p["install"]}</div>
      <div class="price-pix">5% OFF no PIX</div>
    </div>
    <div class="color-picker">
      <div class="color-picker-label">Cor: <span id="colorName">{p["color_name"]}</span></div>
      <div class="color-swatches">
        <div class="color-swatch active" style="background:{p["color_bg"]};" title="{p["color_name"]}"
          onclick="selectColor(this,'{p["color_name"]}','{url}')"></div>
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

<div class="trust-badges-wrap">
  <div class="trust-badges">
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M32 6 L54 14 L54 34 C54 48 43 56 32 60 C21 56 10 48 10 34 L10 14 Z"/><polyline points="22 32 29 39 42 26"/></svg></div>
      <div class="trust-badge-text">{p["warranty_label"]}</div>
      <div class="trust-badge-sub">{p["warranty_sub"]}</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="28" r="18"/><path d="M20 52 C20 44 44 44 44 52"/><path d="M26 22 L32 16 L38 22 M32 16 L32 36"/></svg></div>
      <div class="trust-badge-text">Fabricado em {p["origin"]}</div>
      <div class="trust-badge-sub">Qualidade e tradição Le Creuset desde 1925</div>
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
</div>

<div class="product-tabs">
  <div class="tab">
    <div class="tab-header open" onclick="toggleTab(this)">
      Descrição
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body open">
      <p>{p["desc_p"]}</p>
      <ul>{desc_li}
      </ul>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">
      Características
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body">
      <ul>{feat_li}
      </ul>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">
      Especificações Técnicas
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body">
      <div class="specs-grid"><div>{spec_rows}
      </div></div>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">
      Uso e Cuidado
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </div>
    <div class="tab-body">
      <ul>{care_li}
      </ul>
    </div>
  </div>
</div>

{FOOTER}

<script>
  function changeQty(delta) {{
    var inp = document.getElementById('qtyInput');
    var v = parseInt(inp.value) + delta;
    if (v >= 1) inp.value = v;
  }}
  function selectColor(el, name, src) {{
    document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
    el.classList.add('active');
    document.getElementById('colorName').textContent = name;
    document.getElementById('mainImgEl').src = src;
  }}
  function toggleTab(header) {{
    var body = header.nextElementSibling;
    var isOpen = header.classList.contains('open');
    header.classList.toggle('open', !isOpen);
    body.classList.toggle('open', !isOpen);
  }}
</script>
</body>
</html>'''


def make_collection_page(products):
    cards = ''
    for i, p in enumerate(products, 1):
        url = img_url(p)
        badge_html = ''
        if p.get('badge') == 'new':
            badge_html = f'\n          <span class="product-badge badge-new">{p.get("badge_text","Novo")}</span>'
        elif p.get('badge') == 'sale':
            badge_html = f'\n          <span class="product-badge badge-sale">{p.get("badge_text","Oferta")}</span>'
        elif p.get('badge') == 'limited':
            badge_html = f'\n          <span class="product-badge badge-sale" style="background:#8B6914;">{p.get("badge_text","Ed. Limitada")}</span>'

        price2 = p['price'].split(' – ')
        install_val = p['install'].replace('ou ', '')
        cards += f'''
      <!-- {i}. {p["title"]} -->
      <div class="product-card">
        <div class="product-card-media">
          <a href="{p["file"]}">
            <img id="img-cc{i}" src="{url}" alt="{p["title"]}" loading="lazy" />
          </a>{badge_html}
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <button class="product-quick-buy">Compra Rápida</button>
        </div>
        <div class="product-info">
          <div class="product-name"><a href="{p["file"]}">{p["title"]}</a></div>
          <div class="product-sizes">{p["sizes_label"]}</div>
          <div class="product-price">{p["price"]}</div>
          <div class="product-installment">{install_val}</div>
        </div>
      </div>
'''

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Caçarolas | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Nunito Sans', sans-serif; color: #000; background: #fff; }}
    a {{ text-decoration: none; color: inherit; }}
    .top-bar {{ background: #1a1a1a; color: #fff; font-size: 12px; text-align: center; padding: 8px 16px; letter-spacing: 0.5px; }}
    header {{ background: #fff; border-bottom: 1px solid #e5e5e5; position: sticky; top: 0; z-index: 100; }}
    .header-inner {{ max-width: 1400px; margin: 0 auto; padding: 0 24px; display: flex; align-items: center; height: 64px; gap: 24px; }}
    .logo {{ font-size: 22px; font-weight: 800; letter-spacing: -1px; white-space: nowrap; flex-shrink: 0; }}
    .logo span {{ color: #c8102e; }}
    nav {{ flex: 1; }}
    .nav-list {{ display: flex; list-style: none; align-items: center; }}
    .nav-list > li {{ position: relative; }}
    .nav-list > li > a {{ display: block; padding: 22px 14px; font-size: 13px; font-weight: 600; color: #000; white-space: nowrap; border-bottom: 2px solid transparent; transition: border-color 0.2s; }}
    .nav-list > li > a:hover {{ border-bottom-color: #000; }}
    .nav-list > li.highlight > a {{ color: #c8102e; }}
    .nav-list > li.blue > a {{ color: #2563ab; }}
    .dropdown {{ display: none; position: absolute; top: 100%; left: 0; background: #fff; border: 1px solid #e5e5e5; min-width: 200px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); z-index: 200; padding: 12px 0; }}
    .nav-list > li:hover .dropdown {{ display: block; }}
    .dropdown a {{ display: block; padding: 8px 20px; font-size: 13px; color: #333; }}
    .dropdown a:hover {{ background: #f5f5f5; }}
    .header-icons {{ display: flex; align-items: center; gap: 16px; flex-shrink: 0; }}
    .header-icons a {{ font-size: 12px; font-weight: 600; display: flex; flex-direction: column; align-items: center; gap: 2px; color: #000; }}
    .header-icons svg {{ width: 22px; height: 22px; }}
    .search-box {{ display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px; overflow: hidden; height: 36px; }}
    .search-box input {{ border: none; outline: none; padding: 0 12px; font-size: 13px; width: 180px; font-family: inherit; }}
    .search-box button {{ background: #000; border: none; cursor: pointer; padding: 0 12px; height: 100%; display: flex; align-items: center; }}
    .search-box button svg {{ fill: #fff; width: 16px; height: 16px; }}
    .cat-banner {{ width: 100%; aspect-ratio: 1600/500; overflow: hidden; position: relative; }}
    .cat-banner img {{ width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; }}
    .cat-banner-breadcrumb {{ position: absolute; top: 28px; left: 48px; font-size: 12px; color: #333; display: flex; gap: 5px; align-items: center; }}
    .cat-banner-breadcrumb a {{ color: #333; text-decoration: underline; }}
    .cat-banner-breadcrumb a:hover {{ color: #000; }}
    .cat-banner-title {{ position: absolute; bottom: 60px; left: 48px; font-size: 40px; font-weight: 300; color: #1a1a1a; letter-spacing: 0; }}
    .breadcrumb {{ display: none; }}
    .collection-wrap {{ max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; display: grid; grid-template-columns: 240px 1fr; gap: 40px; }}
    .filters {{ padding-top: 8px; }}
    .filter-group {{ border-bottom: 1px solid #e5e5e5; padding: 18px 0; }}
    .filter-group:first-child {{ border-top: 1px solid #e5e5e5; }}
    .filter-title {{ font-size: 13px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; cursor: pointer; letter-spacing: 0.3px; }}
    .filter-title svg {{ width: 16px; height: 16px; transition: transform 0.2s; }}
    .filter-body {{ margin-top: 14px; display: flex; flex-direction: column; gap: 10px; }}
    .filter-option {{ display: flex; align-items: center; gap: 8px; cursor: pointer; font-size: 13px; color: #333; }}
    .filter-option input[type="checkbox"] {{ accent-color: #000; width: 14px; height: 14px; cursor: pointer; }}
    .filter-count {{ color: #aaa; font-size: 11px; margin-left: auto; }}
    .color-filters {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }}
    .color-filter-swatch {{ width: 28px; height: 28px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; transition: transform 0.2s, border-color 0.2s; }}
    .color-filter-swatch:hover {{ border-color: #000; transform: scale(1.15); }}
    .collection-header {{ display: flex; justify-content: space-between; align-items: center; padding: 20px 0 24px; }}
    .results-count {{ font-size: 13px; color: #666; }}
    .results-count strong {{ color: #000; }}
    .sort-select {{ border: 1px solid #ccc; border-radius: 4px; padding: 8px 12px; font-size: 13px; font-family: inherit; outline: none; cursor: pointer; background: #fff; }}
    .product-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px 20px; }}
    .product-card {{ position: relative; }}
    .product-card-media {{ position: relative; overflow: hidden; background: #f8f8f8; aspect-ratio: 1; }}
    .product-card-media img {{ width: 100%; height: 100%; object-fit: contain; display: block; padding: 12px; transition: transform 0.55s cubic-bezier(0.25,0.46,0.45,0.94); }}
    .product-card:hover .product-card-media img {{ transform: scale(1.06); }}
    .product-badge {{ position: absolute; top: 10px; left: 10px; color: #fff; font-size: 10px; font-weight: 700; padding: 3px 8px; letter-spacing: 0.5px; z-index: 1; }}
    .badge-new {{ background: #000; }}
    .badge-sale {{ background: #c8102e; }}
    .product-wishlist {{ position: absolute; top: 10px; right: 10px; width: 32px; height: 32px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.2s; z-index: 1; box-shadow: 0 1px 4px rgba(0,0,0,0.15); cursor: pointer; }}
    .product-card:hover .product-wishlist {{ opacity: 1; }}
    .product-wishlist svg {{ width: 16px; height: 16px; }}
    .product-quick-buy {{ position: absolute; bottom: 0; left: 0; right: 0; background: #000; color: #fff; font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; border: none; padding: 10px; cursor: pointer; font-family: inherit; transform: translateY(100%); transition: transform 0.25s; }}
    .product-card:hover .product-quick-buy {{ transform: translateY(0); }}
    .product-info {{ padding: 12px 0 0; }}
    .product-name {{ font-size: 13px; font-weight: 600; line-height: 1.4; margin-bottom: 4px; }}
    .product-sizes {{ font-size: 11px; color: #888; margin-bottom: 6px; }}
    .product-price {{ font-size: 14px; font-weight: 700; }}
    .product-installment {{ font-size: 11px; color: #666; margin-top: 2px; }}
    footer {{ background: #111; color: #fff; padding: 60px 24px 30px; }}
    .footer-inner {{ max-width: 1400px; margin: 0 auto; }}
    .footer-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }}
    .footer-brand .logo {{ font-size: 20px; margin-bottom: 16px; display: block; }}
    .footer-brand p {{ font-size: 13px; color: #aaa; line-height: 1.7; max-width: 280px; margin-bottom: 20px; }}
    .footer-social {{ display: flex; gap: 12px; }}
    .social-btn {{ width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; transition: border-color 0.2s, background 0.2s; }}
    .social-btn:hover {{ border-color: #fff; background: rgba(255,255,255,0.1); }}
    .footer-col h4 {{ font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 16px; }}
    .footer-col ul {{ list-style: none; }}
    .footer-col ul li {{ margin-bottom: 10px; }}
    .footer-col ul li a {{ font-size: 13px; color: #aaa; transition: color 0.2s; }}
    .footer-col ul li a:hover {{ color: #fff; }}
    .footer-bottom {{ border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }}
    .footer-bottom p {{ font-size: 12px; color: #666; }}
    .payment-icons {{ display: flex; gap: 8px; }}
    .payment-icon {{ background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }}
  </style>
</head>
<body>

<div class="top-bar">🚚 Frete Grátis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>

{NAV}

<div class="cat-banner">
  <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dw6835868d/category/cat_banners/Banner-categoria-cacarola-bleu-riviera-2.png" alt="Caçarolas Le Creuset" />
  <nav class="cat-banner-breadcrumb">
    <a href="index.html">Início</a>
    <span>/</span>
    <a href="#">Cozinhar</a>
    <span>/</span>
    <span>Caçarolas</span>
  </nav>
  <h1 class="cat-banner-title">Caçarolas</h1>
</div>

<div class="collection-wrap">
  <aside class="filters">
    <div class="filter-group">
      <div class="filter-title open">Material <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="filter-body">
        <label class="filter-option"><input type="checkbox" /> Ferro Fundido Esmaltado <span class="filter-count">7</span></label>
        <label class="filter-option"><input type="checkbox" /> Aço Inox 3-Ply <span class="filter-count">1</span></label>
        <label class="filter-option"><input type="checkbox" /> Aço Esmaltado <span class="filter-count">1</span></label>
      </div>
    </div>
    <div class="filter-group">
      <div class="filter-title open">Tamanho <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="filter-body">
        <label class="filter-option"><input type="checkbox" /> 13 cm <span class="filter-count">2</span></label>
        <label class="filter-option"><input type="checkbox" /> 20 cm <span class="filter-count">2</span></label>
        <label class="filter-option"><input type="checkbox" /> 24 cm <span class="filter-count">1</span></label>
        <label class="filter-option"><input type="checkbox" /> 26 cm <span class="filter-count">2</span></label>
        <label class="filter-option"><input type="checkbox" /> 28 cm <span class="filter-count">2</span></label>
        <label class="filter-option"><input type="checkbox" /> 30 cm <span class="filter-count">2</span></label>
      </div>
    </div>
    <div class="filter-group">
      <div class="filter-title open">Cor <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="color-filters">
        <div class="color-filter-swatch" style="background:#d46820;" title="Laranja"></div>
        <div class="color-filter-swatch" style="background:#c8102e;" title="Vermelho"></div>
        <div class="color-filter-swatch" style="background:#2563ab;" title="Bleu Riviera"></div>
        <div class="color-filter-swatch" style="background:#B8D4D0;" title="Sea Salt"></div>
        <div class="color-filter-swatch" style="background:#F5F0E8;" title="Meringue" style="border:1px solid #ddd;"></div>
        <div class="color-filter-swatch" style="background:#A8D8C8;" title="Cool Mint"></div>
        <div class="color-filter-swatch" style="background:#6B4226;" title="Marronnier"></div>
        <div class="color-filter-swatch" style="background:#1C1C1C;" title="Matte Black"></div>
        <div class="color-filter-swatch" style="background:#D4A017;" title="Flamme Dorée"></div>
      </div>
    </div>
    <div class="filter-group">
      <div class="filter-title open">Garantia <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="filter-body">
        <label class="filter-option"><input type="checkbox" /> Vitalícia <span class="filter-count">8</span></label>
        <label class="filter-option"><input type="checkbox" /> 5 anos <span class="filter-count">1</span></label>
      </div>
    </div>
  </aside>

  <div class="main-content">
    <div class="collection-header">
      <p class="results-count"><strong>9</strong> resultados</p>
      <select class="sort-select">
        <option>Mais populares</option>
        <option>Mais Vendido</option>
        <option>Preço menor para maior</option>
        <option>Preço maior para menor</option>
        <option>Nome do Produto A - Z</option>
        <option>Nome do Produto Z - A</option>
      </select>
    </div>

    <div class="product-grid">
{cards}
    </div>
  </div>
</div>

{FOOTER}

</body>
</html>'''


# ── Generate collection page ──────────────────────────────────────────────────
col_path = os.path.join(BASE_DIR, 'colecao-cacarolas.html')
with open(col_path, 'w', encoding='utf-8') as f:
    f.write(make_collection_page(PRODUCTS))
print('Created: colecao-cacarolas.html')

# ── Generate product pages ────────────────────────────────────────────────────
for p in PRODUCTS:
    path = os.path.join(BASE_DIR, p['file'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(make_product_page(p))
    print(f'Created: {p["file"]}')

# ── Update nav in all existing HTML files ─────────────────────────────────────
updated = 0
for fpath in glob.glob(os.path.join(BASE_DIR, '*.html')):
    fname = os.path.basename(fpath)
    # Skip files we just created
    if fname == 'colecao-cacarolas.html' or fname in [p['file'] for p in PRODUCTS]:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if '<a href="#">Caçarolas</a>' in html:
        html = html.replace('<a href="#">Caçarolas</a>', '<a href="colecao-cacarolas.html">Caçarolas</a>')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

print(f'Nav updated in {updated} files')
