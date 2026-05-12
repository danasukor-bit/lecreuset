with open('colecao-best-sellers.html', 'r', encoding='utf-8') as f:
    html = f.read()

CDN = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'
CDN2 = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'

# ── 1. Add CSS for overlapping circles ───────────────────────────────────────
extra_css = '''
    /* Overlapping circles (moedores) */
    .bs-circles-wrap { position: relative; width: 100%; min-height: 380px; }
    .bs-circle-lg { position: absolute; width: 68%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; top: 0; left: 0; }
    .bs-circle-sm { position: absolute; width: 50%; aspect-ratio: 1; border-radius: 50%; overflow: hidden; bottom: 0; right: 0; border: 4px solid #fff; }
    .bs-circle-lg img, .bs-circle-sm img { width: 100%; height: 100%; object-fit: cover; display: block; }
'''

# Insert before </style>
html = html.replace('  </style>\n</head>', extra_css + '  </style>\n</head>')

# ── 2. Fix Ferro Fundido: texto LEFT, círculo RIGHT ───────────────────────────
# Remove the extra bs-side-split I added previously (dw494b68f3)
old_extra = '''  <div class="bs-side-split" style="margin-bottom:32px;">
    <div class="bs-side-img">
      <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw494b68f3/images/BestSeller/best_sellers-mais_vendidos-ferro_fundido_esmaltado-le_creuset.jpg" alt="Ferro Fundido Le Creuset" />
    </div>
    <div class="bs-side-text">
      <h3>Por que escolher o Ferro Fundido Le Creuset?</h3>
      <p>Cada peça é fundida individualmente e esmaltada à mão, garantindo qualidade única. O esmalte vitrificado colorido é resistente a riscos e absorção de odores.</p>
      <ul>
        <li>Cozimento uniforme e preciso</li>
        <li>Compatível com todas as fontes de calor</li>
        <li>Fácil limpeza, dishwasher safe</li>
        <li>Garantia Vitalícia</li>
      </ul>
    </div>
  </div>
  <div class="bs-products">'''
html = html.replace(old_extra, '  <div class="bs-products">')

# Flip ferro fundido: put text FIRST (left), then circle (right) using bs-split-reverse
old_ff_split = '''  <div class="bs-split">
    <div class="bs-circle-wrap">
      <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dweba6c0c9/images/BestSeller/best-seller(51).png" alt="Ferro Fundido Le Creuset" />
    </div>
    <div class="bs-split-text">
      <h2>Ferro Fundido Esmaltado</h2>
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
  </div>'''

new_ff_split = '''  <div class="bs-split">
    <div class="bs-split-text">
      <h2>Ferro Fundido Esmaltado</h2>
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
    <div class="bs-circle-wrap">
      <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dweba6c0c9/images/BestSeller/best-seller(51).png" alt="Ferro Fundido Le Creuset" />
    </div>
  </div>'''

html = html.replace(old_ff_split, new_ff_split)

# ── 3. Fix Moedores: dois círculos sobrepostos ESQUERDA, texto DIREITA ────────
old_moedores = '''<!-- MOEDORES & GALHETEIROS -->
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
      <p>O Set de Azeite e vinagre de cerâmica da Le Creuset, também conhecido como Galheteiros, trazem conveniência e personalidade à bancada ou mesa.</p>
      <ul>
        <li>Perfeitos para uso e armazenagem de azeite e vinagre</li>
        <li>Cerâmica projetada para uso diário</li>
        <li>10 anos de garantia</li>
      </ul>
      <a href="colecao-moedores-e-galheteiro.html" class="bs-ver-todos">VER TODOS &rsaquo;</a>
    </div>
  </div>'''

new_moedores = '''<!-- MOEDORES & GALHETEIROS -->
<div class="bs-cat">
  <div class="bs-split">
    <div class="bs-circles-wrap">
      <div class="bs-circle-lg">
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-moedor_de_sal_e_pimenta-le_creuset.jpg" alt="Moedores Le Creuset" />
      </div>
      <div class="bs-circle-sm">
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-le_creuset.jpg" alt="Galheteiros Le Creuset" />
      </div>
    </div>
    <div class="bs-split-text">
      <h2>A Le Creuset trouxe cor à cozinha.</h2>
      <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">Moedores</h3>
      <p>Feito com resina acrílica (ABS) altamente resistente, tecnologia moderna e proteção contra corrosão, o moedor da Le Creuset possui um mecanismo de moagem em cerâmica que não oxida.</p>
      <ul>
        <li>Recomendamos o uso de pimentas de grãos secos</li>
        <li>Resina Acrílica (ABS) muito resistente</li>
        <li>Resistente a corrosão</li>
        <li>Cores incomparáveis</li>
        <li>Tecnologia Moderna</li>
      </ul>
      <h3 style="font-size:16px;font-weight:700;margin:16px 0 8px;">Galheteiros</h3>
      <p>O Set de Azeite e vinagre de cerâmica da Le Creuset, também conhecido como Galheteiros, trazem conveniência e personalidade à bancada ou mesa.</p>
      <ul>
        <li>Perfeitos para uso e armazenagem de azeite e vinagre</li>
        <li>Cerâmica projetada para uso diário</li>
        <li>10 anos de garantia</li>
      </ul>
      <a href="colecao-moedores-e-galheteiro.html" class="bs-ver-todos">VER TODOS &rsaquo;</a>
    </div>
  </div>'''

html = html.replace(old_moedores, new_moedores)

# Fix closing tag: bs-side-section → bs-cat for moedores
# The moedores </div> closes bs-side-section, need to keep that closing </div>
# (already handled since we replaced the opening, and the closing </div> before <!-- CERÂMICA --> stays)

# ── 4. Fix Chaleiras: círculo ESQUERDA, texto DIREITA (remove bs-split-reverse) ─
html = html.replace(
    '<div class="bs-split bs-split-reverse">\n    <div class="bs-circle-wrap">',
    '<div class="bs-split">\n    <div class="bs-circle-wrap">'
)

with open('colecao-best-sellers.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done')
