with open('colecao-nossas-cores.html', 'r', encoding='utf-8') as f:
    html = f.read()

CDN = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-master/default/'

new_css = '''
    /* ═══ NOSSAS CORES PAGE ═══ */
    .nc-hero { position: relative; width: 100%; height: 420px; overflow: hidden; }
    .nc-hero img { width: 100%; height: 100%; object-fit: cover; object-position: center 40%; display: block; }
    .nc-hero-overlay { position: absolute; inset: 0; background: linear-gradient(to right, rgba(0,0,0,.5) 0%, rgba(0,0,0,.05) 65%); display: flex; flex-direction: column; justify-content: center; padding: 0 80px; }
    .nc-hero-title { color: #fff; font-size: 52px; font-weight: 800; letter-spacing: -1px; margin-bottom: 12px; }
    .nc-hero-sub { color: rgba(255,255,255,.85); font-size: 15px; max-width: 480px; line-height: 1.6; }

    .nc-section { max-width: 1400px; margin: 0 auto; padding: 64px 48px 96px; }
    .nc-intro { font-size: 15px; color: #555; line-height: 1.8; max-width: 680px; margin-bottom: 56px; }

    .nc-label { font-size: 11px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #fe5000; margin-bottom: 10px; }
    .nc-heading { font-size: 30px; font-weight: 800; letter-spacing: -.5px; margin-bottom: 8px; }
    .nc-rule { width: 40px; height: 3px; background: #111; margin-bottom: 40px; }

    /* Color grid: rectangular tiles */
    .nc-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 80px; }
    .nc-tile { position: relative; aspect-ratio: 3/4; overflow: hidden; cursor: pointer; display: block; text-decoration: none; }
    .nc-tile-bg { width: 100%; height: 100%; transition: transform .5s ease; }
    .nc-tile:hover .nc-tile-bg { transform: scale(1.06); }
    .nc-tile-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,.55) 0%, rgba(0,0,0,.05) 55%); display: flex; flex-direction: column; justify-content: flex-end; padding: 20px; }
    .nc-tile-name { color: #fff; font-size: 16px; font-weight: 800; line-height: 1.2; margin-bottom: 3px; }
    .nc-tile-sub { color: rgba(255,255,255,.8); font-size: 11px; font-weight: 500; letter-spacing: .5px; }
    .nc-tile-badge { position: absolute; top: 14px; left: 14px; background: #fe5000; color: #fff; font-size: 9px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; padding: 4px 9px; }

    /* Featured color rows */
    .nc-featured { display: flex; flex-direction: column; gap: 40px; }
    .nc-color-row { display: grid; grid-template-columns: 380px 1fr; gap: 32px; align-items: center; border-bottom: 1px solid #ebebeb; padding-bottom: 40px; }
    .nc-color-row:last-child { border-bottom: none; }
    .nc-color-row.reverse { grid-template-columns: 1fr 380px; }
    .nc-color-row.reverse .nc-color-info { order: -1; }
    .nc-color-img { position: relative; aspect-ratio: 1; overflow: hidden; }
    .nc-color-img img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 50%; }
    .nc-color-info { padding: 16px 0; }
    .nc-color-dot { width: 36px; height: 36px; border-radius: 50%; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,.15); }
    .nc-color-info h3 { font-size: 26px; font-weight: 800; margin-bottom: 8px; }
    .nc-color-info p { font-size: 14px; color: #555; line-height: 1.75; margin-bottom: 20px; max-width: 480px; }
    .nc-color-link { font-size: 11px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; color: #111; border-bottom: 2px solid #111; padding-bottom: 2px; transition: color .2s, border-color .2s; display: inline-block; }
    .nc-color-link:hover { color: #fe5000; border-color: #fe5000; }

    @media(max-width: 1024px) { .nc-section { padding: 48px 24px 72px; } }
    @media(max-width: 768px) {
      .nc-hero { height: 240px; }
      .nc-hero-overlay { padding: 0 24px; }
      .nc-hero-title { font-size: 30px; }
      .nc-hero-sub { font-size: 13px; }
      .nc-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
      .nc-color-row, .nc-color-row.reverse { grid-template-columns: 1fr; gap: 20px; }
      .nc-color-row.reverse .nc-color-info { order: 0; }
    }
'''

new_content = '''<div class="nc-hero">
  <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw494b68f3/images/BestSeller/best_sellers-mais_vendidos-ferro_fundido_esmaltado-le_creuset.jpg" alt="Nossas Cores Le Creuset" />
  <div class="nc-hero-overlay">
    <h1 class="nc-hero-title">Escolha pela Sua Cor</h1>
    <p class="nc-hero-sub">Cada cor Le Creuset conta uma história. Desde o icônico Laranja até o Bleu Riviera da temporada, nossas cores são uma expressão de personalidade à mesa.</p>
  </div>
</div>

<div class="breadcrumb"><a href="index.html">Home</a><span>/</span><span>Nossas Cores</span></div>

<div class="nc-section">
  <div class="nc-label">PALETA EXCLUSIVA</div>
  <h2 class="nc-heading">Todas as Cores</h2>
  <div class="nc-rule"></div>

  <div class="nc-grid">
    <a href="colecao-bleu-riviera.html" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#1aadc0 0%,#2DBECD 60%,#4DD0DE 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-badge">NOVA</div>
        <div class="nc-tile-name">Bleu Riviera</div>
        <div class="nc-tile-sub">A cor da temporada</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#b85c10 0%,#d46820 60%,#e07a30 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Laranja</div>
        <div class="nc-tile-sub">O clássico Le Creuset</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#a00020 0%,#c8102e 60%,#d42040 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Vermelho</div>
        <div class="nc-tile-sub">Força e paixão</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#a03840 0%,#C85250 60%,#d86060 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Cerise</div>
        <div class="nc-tile-sub">Rosa intenso</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#502e16 0%,#6B4226 60%,#7d5030 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Marronnier</div>
        <div class="nc-tile-sub">Elegância terrosa</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#b0a030 0%,#D4C44A 60%,#e0d058 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Nectar</div>
        <div class="nc-tile-sub">Dourado vibrante</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#ddd8cc 0%,#F5F0E8 60%,#faf8f2 100%);"></div>
      <div class="nc-tile-overlay" style="background:linear-gradient(to top,rgba(0,0,0,.4) 0%,rgba(0,0,0,.02) 55%);">
        <div class="nc-tile-name">Meringue</div>
        <div class="nc-tile-sub">Suavidade francesa</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#ddd 0%,#F5F5F5 60%,#fff 100%);"></div>
      <div class="nc-tile-overlay" style="background:linear-gradient(to top,rgba(0,0,0,.4) 0%,rgba(0,0,0,.02) 55%);">
        <div class="nc-tile-name">Branco</div>
        <div class="nc-tile-sub">Pureza clássica</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#8a9098 0%,#B8BEC4 60%,#ccd0d4 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Mist</div>
        <div class="nc-tile-sub">Cinza névoa</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#b85880 0%,#D4779A 60%,#e088aa 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Rose Quartz</div>
        <div class="nc-tile-sub">Rosa delicado</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#7060a0 0%,#9B7EB0 60%,#b090c0 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Bluebell</div>
        <div class="nc-tile-sub">Lilás encantador</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#144080 0%,#2060A0 60%,#3070b0 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Azure</div>
        <div class="nc-tile-sub">Azul profundo</div>
      </div>
    </a>
    <a href="colecao-flamme-doree.html" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#a07800 0%,#D4A017 60%,#e8b828 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-badge">ESPECIAL</div>
        <div class="nc-tile-name">Flamme Dorée</div>
        <div class="nc-tile-sub">100 anos Le Creuset</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#383838 0%,#5A5A5A 60%,#6a6a6a 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Graphite</div>
        <div class="nc-tile-sub">Grafite moderno</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#000 0%,#1C1C1C 60%,#2c2c2c 100%);"></div>
      <div class="nc-tile-overlay">
        <div class="nc-tile-name">Matte Black</div>
        <div class="nc-tile-sub">Preto mate sofisticado</div>
      </div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(135deg,#e0a0b8 0%,#F0B8C8 60%,#faccda 100%);"></div>
      <div class="nc-tile-overlay" style="background:linear-gradient(to top,rgba(0,0,0,.4) 0%,rgba(0,0,0,.02) 55%);">
        <div class="nc-tile-name">Shell Pink</div>
        <div class="nc-tile-sub">Rosa concha suave</div>
      </div>
    </a>
  </div>

  <div class="nc-label">DESTAQUES</div>
  <h2 class="nc-heading">Cores em Foco</h2>
  <div class="nc-rule"></div>

  <div class="nc-featured">
    <div class="nc-color-row">
      <div class="nc-color-img">
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw3dbd40c1/images/BestSeller/lecreuset-ca%C3%A7arola-redonda-azure.png" alt="Bleu Riviera" />
      </div>
      <div class="nc-color-info">
        <div class="nc-color-dot" style="background:#2DBECD;"></div>
        <h3>Bleu Riviera</h3>
        <p>Inspirada nas profundezas cristalinas do Mar Mediterrâneo, o Bleu Riviera é a cor da temporada Le Creuset. Um azul-turquesa vibrante que transforma qualquer cozinha num espaço de alegria e frescor.</p>
        <a href="colecao-bleu-riviera.html" class="nc-color-link">Ver Coleção &rsaquo;</a>
      </div>
    </div>
    <div class="nc-color-row reverse">
      <div class="nc-color-img">
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dwbdcd2587/images/BestSeller/produto-lecreuset-panela-redonda-vermelha.png" alt="Laranja" />
      </div>
      <div class="nc-color-info">
        <div class="nc-color-dot" style="background:#d46820;"></div>
        <h3>Laranja</h3>
        <p>O Laranja é a cor original Le Creuset — criada em 1925 e inspirada no brilho do ferro fundido incandescente. Clássico, poderoso e inconfundível, é o coração da marca.</p>
        <a href="#" class="nc-color-link">Ver Coleção &rsaquo;</a>
      </div>
    </div>
    <div class="nc-color-row">
      <div class="nc-color-img">
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw08061f78/images/BestSeller/panela-de-arroz-berry.png" alt="Flamme Dorée" />
      </div>
      <div class="nc-color-info">
        <div class="nc-color-dot" style="background:#D4A017;"></div>
        <h3>Flamme Dorée</h3>
        <p>Criada para celebrar os 100 anos da Le Creuset, a Flamme Dorée traz um dourado cintilante único, inspirado nas chamas que aqueceram os fornos da fundição em 1925. Edição limitada e exclusiva.</p>
        <a href="colecao-flamme-doree.html" class="nc-color-link">Ver Coleção &rsaquo;</a>
      </div>
    </div>
  </div>
</div>
'''

# Replace old content and CSS
start = html.find('<div class="cat-banner"')
end = html.find('\n<nav class="mobile-nav"')

# Insert CSS before </style>
if '/* ═══ NOSSAS CORES PAGE ═══ */' not in html:
    html = html.replace('  </style>\n</head>', new_css + '  </style>\n</head>')

# Remove old CSS for cores (duplicates from previous runs)
html = html.replace(
    '    /* Nossas Cores specific */\n', ''
)

html = html[:start] + new_content + html[end:]

with open('colecao-nossas-cores.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done')
