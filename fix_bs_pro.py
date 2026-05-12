with open('colecao-best-sellers.html', 'r', encoding='utf-8') as f:
    raw = f.read()

CDN  = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'
CDN2 = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'

# ── 1. Keep only base CSS (before the first BS block) ────────────────────────
style_open  = raw.index('<style>')
bs_css_mark = raw.index('/* ===== BEST SELLERS')          # first BS CSS comment
style_close = raw.index('  </style>\n</head>')

base_css = raw[style_open + len('<style>'):bs_css_mark]   # original site CSS only

# ── 2. Single clean BS CSS ────────────────────────────────────────────────────
bs_css = '''
    /* ═══════ BEST SELLERS ═══════ */
    .bs-hero            { position:relative; width:100%; height:520px; overflow:hidden; }
    .bs-hero img        { width:100%; height:100%; object-fit:cover; object-position:center 25%; display:block; }
    .bs-hero-overlay    { position:absolute; inset:0; background:linear-gradient(120deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.1) 60%); display:flex; align-items:flex-end; padding:0 0 72px 80px; }
    .bs-hero-title      { color:#fff; font-size:56px; font-weight:800; letter-spacing:-1.5px; line-height:1; }

    .bs-intro           { max-width:820px; margin:64px auto 0; padding:0 32px; text-align:center; }
    .bs-intro p         { font-size:15px; color:#555; line-height:1.9; }

    .bs-illustration    { text-align:center; margin:48px auto 0; max-width:520px; padding:0 24px; }
    .bs-illustration img{ width:100%; height:auto; display:block; margin:0 auto; }

    .bs-main-heading    { text-align:center; font-size:36px; font-weight:800; letter-spacing:-.5px; margin:48px auto 72px; padding:0 24px; line-height:1.2; }

    /* section wrapper */
    .bs-cat             { max-width:1280px; margin:0 auto 88px; padding:0 56px; }
    .bs-side-section    { max-width:1280px; margin:0 auto 88px; padding:0 56px; }

    /* orange tag */
    .bs-tag             { display:inline-flex; align-items:center; gap:6px; font-size:11px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:#fe5000; margin-bottom:6px; }
    .bs-tag::before     { content:''; display:inline-block; width:20px; height:2px; background:#fe5000; }

    /* split: circle + text */
    .bs-split           { display:grid; grid-template-columns:1fr 1fr; gap:72px; align-items:center; margin-bottom:40px; }
    .bs-circle-wrap     { width:100%; aspect-ratio:1; border-radius:50%; overflow:hidden; box-shadow:0 12px 48px rgba(0,0,0,.12); }
    .bs-circle-wrap img { width:100%; height:100%; object-fit:cover; display:block; }

    .bs-split-text h2   { font-size:30px; font-weight:800; margin-bottom:14px; line-height:1.15; }
    .bs-split-text p    { font-size:14px; color:#555; line-height:1.75; margin-bottom:12px; }
    .bs-split-text ul   { list-style:none; padding:0; margin:0 0 24px; }
    .bs-split-text li   { font-size:13px; color:#555; line-height:2; padding-left:18px; position:relative; }
    .bs-split-text li::before { content:"✓"; position:absolute; left:0; color:#fe5000; font-weight:800; }
    .bs-ver-todos       { font-size:11px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:#111; border-bottom:2px solid #111; padding-bottom:2px; display:inline-block; transition:color .2s,border-color .2s; }
    .bs-ver-todos:hover { color:#fe5000; border-color:#fe5000; }

    /* overlapping circles (moedores) */
    .bs-circles-wrap        { position:relative; width:100%; min-height:400px; }
    .bs-circle-lg           { position:absolute; width:66%; aspect-ratio:1; border-radius:50%; overflow:hidden; top:0; left:0; box-shadow:0 12px 40px rgba(0,0,0,.12); }
    .bs-circle-sm           { position:absolute; width:48%; aspect-ratio:1; border-radius:50%; overflow:hidden; bottom:0; right:0; border:5px solid #fff; box-shadow:0 8px 24px rgba(0,0,0,.12); }
    .bs-circle-lg img,
    .bs-circle-sm img       { width:100%; height:100%; object-fit:cover; display:block; }

    /* side layout (ceramica) */
    .bs-side-split      { display:grid; grid-template-columns:1fr 1fr; gap:48px; margin-bottom:40px; align-items:start; }
    .bs-side-head       { font-size:28px; font-weight:800; margin-bottom:28px; line-height:1.2; }
    .bs-side-img img    { width:100%; height:320px; object-fit:cover; display:block; }
    .bs-side-text h3    { font-size:17px; font-weight:800; margin-bottom:10px; }
    .bs-side-text p     { font-size:13px; color:#555; line-height:1.75; margin-bottom:10px; }
    .bs-side-text ul    { list-style:none; padding:0; margin:0 0 18px; }
    .bs-side-text li    { font-size:13px; color:#555; line-height:2; padding-left:18px; position:relative; }
    .bs-side-text li::before { content:"✓"; position:absolute; left:0; color:#fe5000; font-weight:800; }

    /* product carousel */
    .bs-products        { display:flex; gap:16px; overflow-x:auto; scroll-snap-type:x mandatory; -webkit-overflow-scrolling:touch; padding-bottom:6px; scrollbar-width:thin; }
    .bs-products::-webkit-scrollbar       { height:3px; }
    .bs-products::-webkit-scrollbar-thumb { background:#ddd; border-radius:2px; }
    .bs-prod-card       { flex:0 0 210px; scroll-snap-align:start; }
    .bs-prod-card > a   { display:block; color:inherit; text-decoration:none; }
    .bs-prod-img        { width:100%; aspect-ratio:1; background:#f7f7f7; overflow:hidden; margin-bottom:10px; }
    .bs-prod-img img    { width:100%; height:100%; object-fit:contain; padding:12px; transition:transform .35s ease; display:block; }
    .bs-prod-card:hover .bs-prod-img img { transform:scale(1.07); }
    .bs-prod-name       { font-size:13px; font-weight:700; line-height:1.3; margin-bottom:4px; color:#111; }
    .bs-prod-price      { font-size:13px; font-weight:800; color:#111; margin-bottom:10px; }
    .bs-prod-btn        { display:block; width:100%; padding:8px; text-align:center; font-size:10px; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; border:1.5px solid #111; color:#111; background:#fff; transition:all .2s; }
    .bs-prod-btn:hover  { background:#111; color:#fff; }

    /* divider between sections */
    .bs-divider         { max-width:1280px; margin:0 auto 88px; padding:0 56px; border-top:1px solid #e8e8e8; }

    /* recipe section */
    .bs-recipes         { max-width:1280px; margin:0 auto 96px; padding:0 56px; }
    .bs-recipe-head     { text-align:center; margin-bottom:40px; }
    .bs-recipe-head h2  { font-size:30px; font-weight:300; color:#333; margin-bottom:6px; font-style:italic; font-family:'Playfair Display',serif; }
    .bs-recipe-head h3  { font-size:30px; font-weight:800; color:#fe5000; }
    .bs-recipe-grid     { display:grid; grid-template-columns:repeat(4,1fr); gap:24px; }
    .bs-recipe-item     { }
    .bs-recipe-img      { width:100%; aspect-ratio:1; overflow:hidden; margin-bottom:14px; }
    .bs-recipe-img img  { width:100%; height:100%; object-fit:cover; transition:transform .35s ease; display:block; }
    .bs-recipe-item:hover .bs-recipe-img img { transform:scale(1.05); }
    .bs-recipe-name     { font-size:14px; font-weight:600; color:#111; margin-bottom:14px; }
    .bs-recipe-btn      { display:inline-block; padding:9px 24px; font-size:10px; font-weight:800; letter-spacing:2px; text-transform:uppercase; border:1.5px solid #111; color:#111; background:#fff; transition:all .2s; }
    .bs-recipe-btn:hover{ background:#111; color:#fff; }

    @media(max-width:1024px) {
      .bs-cat,.bs-side-section,.bs-recipes,.bs-divider { padding:0 24px; }
    }
    @media(max-width:768px) {
      .bs-hero             { height:260px; }
      .bs-hero-overlay     { padding:0 0 32px 24px; }
      .bs-hero-title       { font-size:32px; }
      .bs-main-heading     { font-size:24px; margin-bottom:48px; }
      .bs-split            { grid-template-columns:1fr; gap:32px; }
      .bs-side-split       { grid-template-columns:1fr; gap:24px; }
      .bs-circles-wrap     { min-height:280px; }
      .bs-recipe-grid      { grid-template-columns:repeat(2,1fr); gap:16px; }
      .bs-prod-card        { flex:0 0 155px; }
      .bs-cat,.bs-side-section,.bs-recipes,.bs-divider { margin-bottom:56px; }
    }
'''

# ── 3. Find header end ────────────────────────────────────────────────────────
header_end = raw.index('</header>\n') + len('</header>\n')

# ── 4. Extract body content ───────────────────────────────────────────────────
# Find correct body (from <!-- FERRO FUNDIDO --> to end of recipes </div>)
content_start = raw.index('<!-- FERRO FUNDIDO -->')
# Find the <!-- RECEITAS --> recipes closing div
recipes_close = raw.index('</div>\n', raw.index('<!-- RECEITAS -->'))
# Walk forward to find the outer </div> of recipes section
content_end = raw.index('\n', recipes_close) + 1

# Get clean content
body_content = raw[raw.index('<div class="bs-hero">'):content_end]

# ── 5. Add Ver Produto button to every bs-prod-card ──────────────────────────
import re

def add_btn(m):
    inner = m.group(1)
    href  = re.search(r'href="([^"]+)"', inner).group(1)
    if 'bs-prod-btn' in inner:
        return m.group(0)
    return m.group(0).rstrip() + f'\n      <a href="{href}" class="bs-prod-btn">Ver Produto</a>\n    </div>'

# Replace each bs-prod-card block
body_content = re.sub(
    r'(<div class="bs-prod-card">\s*<a href="[^"]+">.*?</a>\s*)</div>',
    add_btn,
    body_content,
    flags=re.DOTALL
)

# ── 6. Get nav/mobile block from ceramica ────────────────────────────────────
with open('colecao-ceramica.html', 'r', encoding='utf-8') as f:
    ceramica = f.read()

nav_start = ceramica.index('\n<nav class="mobile-nav"')
nav_end   = ceramica.index('\n<script src="cart.js">', nav_start)
nav_block = ceramica[nav_start:nav_end]

# ── 7. Get head part (base styles only, no duplicate BS blocks) ───────────────
head_raw = raw[:header_end]
# Keep up to just before the first BS CSS comment, then close style
head_clean_end = head_raw.index('/* ===== BEST SELLERS')
head_part = head_raw[:style_open + len('<style>')] + base_css.rstrip() + '\n' + bs_css + '  </style>\n</head>\n'
# Append everything from </head> to </header>
head_close_pos = head_raw.index('</head>\n') + len('</head>\n')
nav_header = head_raw[head_close_pos:]  # <body>...<header>...</header>\n

# ── 8. Assemble ───────────────────────────────────────────────────────────────
hero_img  = f'{CDN2}dw1b33812b/images/BestSeller/4K-TIF-20231123_BAKINGACTI2024_044.jpg?sw=1440&sfrm=png'

# Rebuild just the page content (hero + sections)
page_content = f'''<div class="bs-hero">
  <img src="{hero_img}" alt="Best-sellers Le Creuset" />
  <div class="bs-hero-overlay">
    <h1 class="bs-hero-title">Best-sellers</h1>
  </div>
</div>

<div class="bs-intro">
  <p>Alguns produtos conquistam um lugar especial na cozinha — e no coração de quem ama cozinhar. Nesta seleção reunimos os <strong>Best-sellers</strong> da Le Creuset: as panelas de ferro fundido mais desejadas, moedores que elevam os sabores, além de cerâmica, chaleiras e acessórios que unem charme e funcionalidade.</p>
</div>

<div class="bs-illustration">
  <img src="{CDN2}dwb4230871/images/BestSeller/lp-best-seller.jpg?sw=1440&sfrm=png" alt="Le Creuset" />
</div>

<h2 class="bs-main-heading">Cozinhar com os melhores<br>faz toda a diferença!</h2>

<!-- FERRO FUNDIDO -->
<div class="bs-cat">
  <div class="bs-tag">BEST-SELLER</div>
  <div class="bs-split">
    <div class="bs-split-text">
      <h2>Ferro Fundido Esmaltado</h2>
      <p>Um clássico atemporal projetado para cozimento uniforme, retenção de calor excepcional e durabilidade incomparável. Cada peça é fundida individualmente e esmaltada à mão.</p>
      <ul>
        <li>Compatível com todas as fontes de calor</li>
        <li>Esmalte interior de fácil limpeza</li>
        <li>O ferro mais leve do mercado</li>
        <li>Cores incomparáveis</li>
        <li>Garantia Vitalícia</li>
      </ul>
      <a href="colecao-ferro-fundido.html" class="bs-ver-todos">Ver Coleção &rsaquo;</a>
    </div>
    <div class="bs-circle-wrap">
      <img src="{CDN}dweba6c0c9/images/BestSeller/best-seller(51).png" alt="Ferro Fundido Le Creuset" />
    </div>
  </div>
  <div class="bs-products">
    <div class="bs-prod-card">
      <a href="panela-redonda-signature.html">
        <div class="bs-prod-img"><img src="{CDN}dwbdcd2587/images/BestSeller/produto-lecreuset-panela-redonda-vermelha.png" alt="Panela Redonda Signature" loading="lazy" /></div>
        <p class="bs-prod-name">Panela Redonda Signature</p>
        <p class="bs-prod-price">R$ 1.514,25 – R$ 4.399,00</p>
      </a>
      <a href="panela-redonda-signature.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="panela-arroz-every.html">
        <div class="bs-prod-img"><img src="{CDN}dw08061f78/images/BestSeller/panela-de-arroz-berry.png" alt="Panela de Arroz Every" loading="lazy" /></div>
        <p class="bs-prod-name">Panela de Arroz Every</p>
        <p class="bs-prod-price">R$ 2.199,00</p>
      </a>
      <a href="panela-arroz-every.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="cacarola-buffet-signature.html">
        <div class="bs-prod-img"><img src="{CDN}dw3dbd40c1/images/BestSeller/lecreuset-ca%C3%A7arola-redonda-azure.png" alt="Caçarola Buffet Signature" loading="lazy" /></div>
        <p class="bs-prod-name">Caçarola Buffet Signature</p>
        <p class="bs-prod-price">R$ 2.069,25 – R$ 3.269,00</p>
      </a>
      <a href="cacarola-buffet-signature.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="skillet-redonda-signature.html">
        <div class="bs-prod-img"><img src="{CDN}dw697b3830/images/BestSeller/produto-lecreuset-skillet-laranja%20(1).png" alt="Skillet Redonda Signature" loading="lazy" /></div>
        <p class="bs-prod-name">Skillet Redonda Signature</p>
        <p class="bs-prod-price">R$ 1.999,00</p>
      </a>
      <a href="skillet-redonda-signature.html" class="bs-prod-btn">Ver Produto</a>
    </div>
  </div>
</div>

<div class="bs-divider"></div>

<!-- MOEDORES & GALHETEIROS -->
<div class="bs-cat">
  <div class="bs-split">
    <div class="bs-circles-wrap">
      <div class="bs-circle-lg">
        <img src="{CDN}dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-moedor_de_sal_e_pimenta-le_creuset.jpg" alt="Moedores Le Creuset" />
      </div>
      <div class="bs-circle-sm">
        <img src="{CDN}dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-le_creuset.jpg" alt="Galheteiros Le Creuset" />
      </div>
    </div>
    <div class="bs-split-text">
      <h2>A Le Creuset trouxe cor à cozinha.</h2>
      <h3 style="font-size:16px;font-weight:800;margin-bottom:8px;margin-top:4px;">Moedores</h3>
      <p>Mecanismo em cerâmica que não oxida, resina ABS altamente resistente e cores vibrantes que transformam qualquer bancada.</p>
      <ul>
        <li>Mecanismo cerâmico anti-corrosão</li>
        <li>Ajuste preciso de granulometria</li>
        <li>Resina ABS muito resistente</li>
        <li>Cores incomparáveis</li>
      </ul>
      <h3 style="font-size:16px;font-weight:800;margin:16px 0 8px;">Galheteiros</h3>
      <p>O Set de Azeite e Vinagre em cerâmica traz conveniência e personalidade à mesa.</p>
      <ul>
        <li>Perfeitos para azeite e vinagre</li>
        <li>Cerâmica projetada para uso diário</li>
        <li>10 anos de garantia</li>
      </ul>
      <a href="colecao-moedores-e-galheteiro.html" class="bs-ver-todos">Ver Coleção &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
    <div class="bs-prod-card">
      <a href="moedor-sal-21cm.html">
        <div class="bs-prod-img"><img src="{CDN}dw2cc21ce4/images/BestSeller/moedores-azure.png" alt="Moedor de Sal 21cm" loading="lazy" /></div>
        <p class="bs-prod-name">Moedor de Sal 21cm</p>
        <p class="bs-prod-price">R$ 369,00</p>
      </a>
      <a href="moedor-sal-21cm.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="moedor-pimenta-21cm.html">
        <div class="bs-prod-img"><img src="{CDN}dwd4c4e94a/images/BestSeller/produto-lecreuset-moedores-laranja.png" alt="Moedor de Pimenta 21cm" loading="lazy" /></div>
        <p class="bs-prod-name">Moedor de Pimenta 21cm</p>
        <p class="bs-prod-price">R$ 369,00</p>
      </a>
      <a href="moedor-pimenta-21cm.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="set-azeite-vinagre-classico.html">
        <div class="bs-prod-img"><img src="{CDN}dwda943317/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-fundo_brancojpg.jpg" alt="Set Azeite & Vinagre" loading="lazy" /></div>
        <p class="bs-prod-name">Set Azeite &amp; Vinagre Clássico</p>
        <p class="bs-prod-price">R$ 579,00</p>
      </a>
      <a href="set-azeite-vinagre-classico.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="moedor-pimenta-30cm.html">
        <div class="bs-prod-img"><img src="{CDN}dw57e0437f/images/BestSeller/best_sellers-mais_vendidos-Moedor_30_cm-fundo_branco.png" alt="Moedor de Pimenta 30cm" loading="lazy" /></div>
        <p class="bs-prod-name">Moedor de Pimenta 30cm</p>
        <p class="bs-prod-price">R$ 479,00</p>
      </a>
      <a href="moedor-pimenta-30cm.html" class="bs-prod-btn">Ver Produto</a>
    </div>
  </div>
</div>

<div class="bs-divider"></div>

<!-- CERÂMICA -->
<div class="bs-side-section">
  <h2 class="bs-side-head">Beleza e desempenho<br>em cada detalhe.</h2>
  <div class="bs-side-split">
    <div class="bs-side-img">
      <img src="{CDN}dw507b1eac/images/BestSeller/best_sellers-mais_vendidos-canecas_de_ceramica_esmaltada-le_creuset.jpg" alt="Cerâmica Le Creuset" />
    </div>
    <div class="bs-side-text">
      <h3>Cerâmica</h3>
      <p>A cerâmica premium da Le Creuset é sinônimo de resistência, versatilidade e elegância. Seu esmalte vitrificado evita a absorção de aromas e facilita a limpeza.</p>
      <ul>
        <li>Retenção de temperatura</li>
        <li>Segura para lava-louças</li>
        <li>Resistente a arranhões</li>
        <li>Cores incomparáveis</li>
        <li>Garantia de 10 anos</li>
      </ul>
      <a href="colecao-ceramica.html" class="bs-ver-todos">Ver Coleção &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
    <div class="bs-prod-card">
      <a href="pote-para-mel.html">
        <div class="bs-prod-img"><img src="{CDN2}dw3be00d82/images/BestSeller/best-seller%20(21).jpg?sw=400&sfrm=png" alt="Pote para Mel" loading="lazy" /></div>
        <p class="bs-prod-name">Pote para Mel</p>
        <p class="bs-prod-price">R$ 379,00</p>
      </a>
      <a href="pote-para-mel.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="pote-de-manteiga.html">
        <div class="bs-prod-img"><img src="{CDN2}dwae261b1b/images/BestSeller/best-seller%20(29).jpg?sw=400&sfrm=png" alt="Pote de Manteiga" loading="lazy" /></div>
        <p class="bs-prod-name">Pote de Manteiga</p>
        <p class="bs-prod-price">R$ 319,00</p>
      </a>
      <a href="pote-de-manteiga.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="pote-para-biscoito.html">
        <div class="bs-prod-img"><img src="{CDN2}dwd940b159/images/BestSeller/best-seller%20(41).jpg?sw=400&sfrm=png" alt="Pote para Biscoito 2,4L" loading="lazy" /></div>
        <p class="bs-prod-name">Pote para Biscoito 2,4L</p>
        <p class="bs-prod-price">R$ 649,00</p>
      </a>
      <a href="pote-para-biscoito.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="pote-de-alho.html">
        <div class="bs-prod-img"><img src="{CDN2}dwaf47ea8d/images/BestSeller/pote-para-alho-vermelho.jpg?sw=400&sfrm=png" alt="Pote de Alho" loading="lazy" /></div>
        <p class="bs-prod-name">Pote de Alho</p>
        <p class="bs-prod-price">R$ 229,00</p>
      </a>
      <a href="pote-de-alho.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="travessa-retangular-heritage.html">
        <div class="bs-prod-img"><img src="{CDN}dwad6ebcf0/images/BestSeller/travessas-produto-lecreuset-heritage-marseille.png" alt="Travessa Retangular Heritage" loading="lazy" /></div>
        <p class="bs-prod-name">Travessa Retangular Heritage</p>
        <p class="bs-prod-price">R$ 689,00</p>
      </a>
      <a href="travessa-retangular-heritage.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="mini-cocotte.html">
        <div class="bs-prod-img"><img src="{CDN}dw6db25617/images/BestSeller/mini-cocotte-azure.png" alt="Mini Cocotte" loading="lazy" /></div>
        <p class="bs-prod-name">Mini Cocotte</p>
        <p class="bs-prod-price">R$ 167,30 – R$ 239,00</p>
      </a>
      <a href="mini-cocotte.html" class="bs-prod-btn">Ver Produto</a>
    </div>
  </div>
</div>

<div class="bs-divider"></div>

<!-- CHALEIRAS -->
<div class="bs-cat">
  <div class="bs-tag">BEST-SELLER</div>
  <div class="bs-split">
    <div class="bs-circle-wrap">
      <img src="{CDN2}dw807c0f5c/images/BestSeller/bet-seller900.jpg?sw=900&sfrm=png" alt="Chaleiras Le Creuset" />
    </div>
    <div class="bs-split-text">
      <h2>Chaleiras</h2>
      <p>Fabricada em aço carbono esmaltado, a Chaleira Clássica oferece aquecimento rápido e distribuição uniforme do calor. O apito sonoro avisa quando a água atinge o ponto de fervura.</p>
      <ul>
        <li>Aquecimento rápido e uniforme</li>
        <li>Apito sonoro de segurança</li>
        <li>Esmalte vitrificado anti-corrosão</li>
        <li>Cores incomparáveis</li>
        <li>Garantia de 5 anos</li>
      </ul>
      <a href="colecao-chaleiras.html" class="bs-ver-todos">Ver Coleção &rsaquo;</a>
    </div>
  </div>
  <div class="bs-products">
    <div class="bs-prod-card">
      <a href="chaleira-classica.html">
        <div class="bs-prod-img"><img src="{CDN}dwc412fcee/images/BestSeller/chaleira-tradiconal-azure.png" alt="Chaleira Clássica Azure" loading="lazy" /></div>
        <p class="bs-prod-name">Chaleira Clássica Azure</p>
        <p class="bs-prod-price">R$ 899,00 – R$ 1.299,00</p>
      </a>
      <a href="chaleira-classica.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="chaleira-classica.html">
        <div class="bs-prod-img"><img src="{CDN}dw05bada9d/images/BestSeller/chaleira-cl%C3%A1ssica-com-apito-bamboo.png" alt="Chaleira Clássica Bamboo" loading="lazy" /></div>
        <p class="bs-prod-name">Chaleira Clássica Bamboo</p>
        <p class="bs-prod-price">R$ 899,00 – R$ 1.299,00</p>
      </a>
      <a href="chaleira-classica.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="chaleira-classica.html">
        <div class="bs-prod-img"><img src="{CDN}dw265d0f03/images/BestSeller/chaleira-cl%C3%A1ssica-com-apito-shell%20pink.png" alt="Chaleira Shell Pink" loading="lazy" /></div>
        <p class="bs-prod-name">Chaleira Clássica Shell Pink</p>
        <p class="bs-prod-price">R$ 899,00 – R$ 1.299,00</p>
      </a>
      <a href="chaleira-classica.html" class="bs-prod-btn">Ver Produto</a>
    </div>
    <div class="bs-prod-card">
      <a href="chaleira-classica.html">
        <div class="bs-prod-img"><img src="{CDN}dw13421845/images/BestSeller/chaleira-cotton-classica.png" alt="Chaleira Clássica Cotton" loading="lazy" /></div>
        <p class="bs-prod-name">Chaleira Clássica Cotton</p>
        <p class="bs-prod-price">R$ 899,00 – R$ 1.299,00</p>
      </a>
      <a href="chaleira-classica.html" class="bs-prod-btn">Ver Produto</a>
    </div>
  </div>
</div>

<!-- RECEITAS -->
<div class="bs-recipes">
  <div class="bs-recipe-head">
    <h2>Já garantiu o seu favorito?</h2>
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

result = head_part + nav_header + page_content + nav_block + '\n<script src="cart.js"></script>\n</body>\n</html>\n'

with open('colecao-best-sellers.html', 'w', encoding='utf-8') as f:
    f.write(result)

lines = result.count('\n')
styles = result.count('/* ═')
print(f'Done. {len(result)} chars, {lines} lines, {styles} CSS block(s)')
