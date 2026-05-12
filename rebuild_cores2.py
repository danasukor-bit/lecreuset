import sys
sys.stdout.reconfigure(encoding='utf-8')

# Use ceramica as a clean structural base
with open('colecao-ceramica.html', 'r', encoding='utf-8') as f:
    base = f.read()

CDN  = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'
CDN2 = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'

# ── Extract head (CSS up to </style>) from ceramica ─────────────────────────
style_end = base.index('  </style>\n</head>')
head_css   = base[:style_end]  # everything up to just before </style>

# ── Extract header/nav (</head> → </header>) from ceramica ──────────────────
head_close  = base.index('</head>\n') + len('</head>\n')
header_end  = base.index('</header>\n') + len('</header>\n')
nav_header  = base[head_close:header_end]

# Fix title for nossas-cores
nav_header = nav_header.replace('<title>Cerâmica | Le Creuset Brasil</title>',
                                '<title>Nossas Cores | Le Creuset Brasil</title>')

# ── Extract mobile nav from ceramica ─────────────────────────────────────────
nav_start = base.index('\n<nav class="mobile-nav"')
nav_end   = base.index('\n<script src="cart.js">', nav_start)
nav_block = base[nav_start:nav_end]
# Fix active link
nav_block = nav_block.replace(
    'colecao-ceramica.html" class="bottom-nav-item active"',
    'colecao-nossas-cores.html" class="bottom-nav-item active"'
)

# ── New CSS for this page ─────────────────────────────────────────────────────
page_css = '''
    /* ═══ NOSSAS CORES ═══ */
    .nc-hero { position:relative; width:100%; height:440px; overflow:hidden; }
    .nc-hero img { width:100%; height:100%; object-fit:cover; object-position:center 40%; display:block; }
    .nc-hero-overlay { position:absolute; inset:0; background:linear-gradient(to right,rgba(0,0,0,.52) 0%,rgba(0,0,0,.05) 65%); display:flex; flex-direction:column; justify-content:center; padding:0 80px; }
    .nc-hero-title { color:#fff; font-size:52px; font-weight:800; letter-spacing:-1px; margin-bottom:12px; }
    .nc-hero-sub { color:rgba(255,255,255,.88); font-size:15px; max-width:480px; line-height:1.65; }

    .nc-wrap { max-width:1400px; margin:0 auto; padding:64px 56px 96px; }
    .nc-label { font-size:11px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:#fe5000; margin-bottom:10px; }
    .nc-heading { font-size:30px; font-weight:800; letter-spacing:-.4px; margin-bottom:8px; }
    .nc-rule { width:40px; height:3px; background:#111; margin-bottom:40px; }

    /* color tiles */
    .nc-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:80px; }
    .nc-tile { position:relative; aspect-ratio:3/4; overflow:hidden; display:block; text-decoration:none; }
    .nc-tile-bg { width:100%; height:100%; transition:transform .5s ease; }
    .nc-tile:hover .nc-tile-bg { transform:scale(1.07); }
    .nc-tile-overlay { position:absolute; inset:0; background:linear-gradient(to top,rgba(0,0,0,.58) 0%,rgba(0,0,0,.04) 55%); display:flex; flex-direction:column; justify-content:flex-end; padding:18px; }
    .nc-tile-name { color:#fff; font-size:15px; font-weight:800; line-height:1.2; margin-bottom:3px; }
    .nc-tile-sub { color:rgba(255,255,255,.78); font-size:11px; }
    .nc-tile-badge { position:absolute; top:14px; left:14px; background:#fe5000; color:#fff; font-size:9px; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; padding:4px 9px; }

    /* featured rows */
    .nc-featured { display:flex; flex-direction:column; gap:0; }
    .nc-row { display:grid; grid-template-columns:1fr 1fr; gap:0; align-items:stretch; margin-bottom:0; border-bottom:1px solid #ebebeb; }
    .nc-row:last-child { border-bottom:none; }
    .nc-row-img { aspect-ratio:1; overflow:hidden; }
    .nc-row-img img { width:100%; height:100%; object-fit:cover; display:block; transition:transform .5s; }
    .nc-row:hover .nc-row-img img { transform:scale(1.04); }
    .nc-row-info { display:flex; flex-direction:column; justify-content:center; padding:56px 64px; }
    .nc-dot { width:32px; height:32px; border-radius:50%; margin-bottom:20px; box-shadow:0 2px 8px rgba(0,0,0,.18); flex-shrink:0; }
    .nc-row-info h3 { font-size:26px; font-weight:800; margin-bottom:10px; }
    .nc-row-info p { font-size:14px; color:#555; line-height:1.8; margin-bottom:24px; max-width:440px; }
    .nc-link { font-size:11px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:#111; border-bottom:2px solid #111; padding-bottom:2px; display:inline-block; transition:color .2s,border-color .2s; }
    .nc-link:hover { color:#fe5000; border-color:#fe5000; }

    @media(max-width:1024px){ .nc-wrap { padding:48px 24px 72px; } }
    @media(max-width:768px){
      .nc-hero { height:240px; }
      .nc-hero-overlay { padding:0 24px; }
      .nc-hero-title { font-size:28px; }
      .nc-hero-sub { font-size:13px; }
      .nc-grid { grid-template-columns:repeat(2,1fr); gap:10px; }
      .nc-row { grid-template-columns:1fr; }
      .nc-row-info { padding:28px 24px; }
    }
'''

# ── Page content ──────────────────────────────────────────────────────────────
content = f'''<div class="nc-hero">
  <img src="{CDN}dw494b68f3/images/BestSeller/best_sellers-mais_vendidos-ferro_fundido_esmaltado-le_creuset.jpg" alt="Nossas Cores Le Creuset" />
  <div class="nc-hero-overlay">
    <h1 class="nc-hero-title">Escolha pela<br>Sua Cor</h1>
    <p class="nc-hero-sub">Cada cor Le Creuset conta uma história. Desde o icônico Laranja de 1925 até o vibrante Bleu Riviera da temporada, nossas cores são uma expressão de personalidade à mesa.</p>
  </div>
</div>

<div class="nc-wrap">
  <div class="nc-label">PALETA EXCLUSIVA</div>
  <h2 class="nc-heading">Todas as Cores</h2>
  <div class="nc-rule"></div>

  <div class="nc-grid">
    <a href="colecao-bleu-riviera.html" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#18a8c0,#2DBECD,#50d0dc);"></div>
      <div class="nc-tile-overlay"><span class="nc-tile-badge">NOVA</span><div class="nc-tile-name">Bleu Riviera</div><div class="nc-tile-sub">A cor da temporada</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#b05010,#d46820,#e88030);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Laranja</div><div class="nc-tile-sub">O clássico Le Creuset</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#980018,#c8102e,#dc2040);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Vermelho</div><div class="nc-tile-sub">Força e paixão</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#983040,#C85250,#d86860);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Cerise</div><div class="nc-tile-sub">Rosa intenso</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#402010,#6B4226,#7e5230);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Marronnier</div><div class="nc-tile-sub">Elegância terrosa</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#a89828,#D4C44A,#e0d060);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Nectar</div><div class="nc-tile-sub">Dourado vibrante</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#ccc8be,#F5F0E8,#faf6f0);"></div>
      <div class="nc-tile-overlay" style="background:linear-gradient(to top,rgba(0,0,0,.45) 0%,transparent 55%);"><div class="nc-tile-name">Meringue</div><div class="nc-tile-sub">Suavidade francesa</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#c8c8c8,#efefef,#fff);"></div>
      <div class="nc-tile-overlay" style="background:linear-gradient(to top,rgba(0,0,0,.45) 0%,transparent 55%);"><div class="nc-tile-name">Branco</div><div class="nc-tile-sub">Pureza clássica</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#8890a0,#B8BEC4,#ccd2d6);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Mist</div><div class="nc-tile-sub">Cinza névoa</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#b06088,#D4779A,#e088aa);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Rose Quartz</div><div class="nc-tile-sub">Rosa delicado</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#6858a0,#9B7EB0,#b090c4);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Bluebell</div><div class="nc-tile-sub">Lilás encantador</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#103878,#2060A0,#3070b4);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Azure</div><div class="nc-tile-sub">Azul profundo</div></div>
    </a>
    <a href="colecao-flamme-doree.html" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#987000,#D4A017,#e8b830);"></div>
      <div class="nc-tile-overlay"><span class="nc-tile-badge">100 ANOS</span><div class="nc-tile-name">Flamme Dorée</div><div class="nc-tile-sub">Edição especial</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#303030,#5A5A5A,#6a6a6a);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Graphite</div><div class="nc-tile-sub">Grafite moderno</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#000,#1C1C1C,#2a2a2a);"></div>
      <div class="nc-tile-overlay"><div class="nc-tile-name">Matte Black</div><div class="nc-tile-sub">Preto mate sofisticado</div></div>
    </a>
    <a href="#" class="nc-tile">
      <div class="nc-tile-bg" style="background:linear-gradient(160deg,#dca8bc,#F0B8C8,#faccda);"></div>
      <div class="nc-tile-overlay" style="background:linear-gradient(to top,rgba(0,0,0,.45) 0%,transparent 55%);"><div class="nc-tile-name">Shell Pink</div><div class="nc-tile-sub">Rosa concha suave</div></div>
    </a>
  </div>

  <div class="nc-label">DESTAQUES</div>
  <h2 class="nc-heading">Cores em Foco</h2>
  <div class="nc-rule"></div>

  <div class="nc-featured">
    <div class="nc-row">
      <div class="nc-row-img">
        <img src="{CDN}dw3dbd40c1/images/BestSeller/lecreuset-ca%C3%A7arola-redonda-azure.png" alt="Bleu Riviera" />
      </div>
      <div class="nc-row-info">
        <div class="nc-dot" style="background:#2DBECD;"></div>
        <h3>Bleu Riviera</h3>
        <p>Inspirada nas profundezas cristalinas do Mar Mediterrâneo, o Bleu Riviera é a cor da temporada Le Creuset. Um azul-turquesa vibrante que transforma qualquer cozinha em um espaço de alegria e frescor.</p>
        <a href="colecao-bleu-riviera.html" class="nc-link">Ver Coleção &rsaquo;</a>
      </div>
    </div>
    <div class="nc-row">
      <div class="nc-row-info">
        <div class="nc-dot" style="background:#d46820;"></div>
        <h3>Laranja</h3>
        <p>O Laranja é a cor original Le Creuset — criada em 1925 e inspirada no brilho do ferro fundido incandescente. Clássico, poderoso e inconfundível, é o coração da marca há 100 anos.</p>
        <a href="#" class="nc-link">Ver Coleção &rsaquo;</a>
      </div>
      <div class="nc-row-img">
        <img src="{CDN}dwbdcd2587/images/BestSeller/produto-lecreuset-panela-redonda-vermelha.png" alt="Laranja" />
      </div>
    </div>
    <div class="nc-row">
      <div class="nc-row-img">
        <img src="{CDN2}dw807c0f5c/images/BestSeller/bet-seller900.jpg?sw=800&sfrm=png" alt="Flamme Dorée" />
      </div>
      <div class="nc-row-info">
        <div class="nc-dot" style="background:#D4A017;"></div>
        <h3>Flamme Dorée</h3>
        <p>Criada para celebrar os 100 anos da Le Creuset, a Flamme Dorée traz um dourado único e cintilante, inspirado nas chamas dos fornos da fundição original de 1925. Edição limitada e exclusiva.</p>
        <a href="colecao-flamme-doree.html" class="nc-link">Ver Coleção &rsaquo;</a>
      </div>
    </div>
  </div>
</div>
'''

# ── Assemble ──────────────────────────────────────────────────────────────────
result = (
    head_css +
    page_css +
    '  </style>\n</head>\n' +
    nav_header +
    content +
    nav_block +
    '\n<script src="cart.js"></script>\n</body>\n</html>\n'
)

with open('colecao-nossas-cores.html', 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Done. {len(result)} chars, {result.count(chr(10))} lines')
