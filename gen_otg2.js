const fs = require('fs');
const path = require('path');
const BASE = String.raw`c:\Users\teste\aa\lecreuset`;
const CDN = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default';

// OTG color palette — shown on all product pages
// real = we have local CDN image; otherwise link to real site
const OTG_COLORS = [
  { name: 'Berry',      hex: '#9B2973', real: true  },
  { name: 'Cotton',     hex: '#EDE8E0', real: true  },
  { name: 'Laranja',    hex: '#d46820', real: false },
  { name: 'Vermelho',   hex: '#c8102e', real: false },
  { name: 'Azure',      hex: '#2060A0', real: false },
  { name: 'Bamboo',     hex: '#8B9A5A', real: false },
  { name: 'Matte Black',hex: '#1a1a1a', real: false },
  { name: 'Nectar',     hex: '#D4C44A', real: false },
  { name: 'Shell Pink', hex: '#E8A8A8', real: false },
];

const PRODUCTS = [
  {
    file: 'garrafa-otg-1l-berry.html',
    title: 'Garrafa Térmica 1L On The Go',
    subtitle: 'Aço Inox · On The Go',
    selectedColor: 'Berry',
    price: 'R$ 379,00',
    installments: '3x R$ 126,33 sem juros',
    pix: 'R$ 360,05 no PIX (5% OFF)',
    desc: 'A Garrafa Térmica On The Go de 1L da Le Creuset combina estética icônica com alto desempenho. Isolamento a vácuo de parede dupla mantém bebidas quentes por até 12 horas ou frias por até 24 horas. Tampa hermética que serve como copo extra, alça dobrável e base antiderrapante de silicone.',
    specs: [['Material','Aço Inox Inoxidável'],['Capacidade','1 L'],['Dimensões','8,8 × 8,8 × 33,1 cm'],['Quente','Até 12 horas'],['Frio','Até 24 horas'],['Lavagem','Lavagem à mão'],['Origem','China'],['Garantia','10 anos']],
    colorImages: {
      Berry:  `${CDN}/dwce47f0e3/images/41066334390001-otg-garrafa-1L-1.png?sw=650&sh=650&sm=fit`,
      Cotton: `${CDN}/dw9cf41b96/images/41066004310001-garrafa-cotton-1.png?sw=650&sh=650&sm=fit`,
    },
    extraImages: {
      Berry: [
        `${CDN}/dwcdee4428/images/41066334390001-otg-garrafa-1L-2.png?sw=650&sh=650&sm=fit`,
        `${CDN}/dw868b4f15/images/41066334390001-otg-garrafa-1L-3.png?sw=650&sh=650&sm=fit`,
        `${CDN}/dw813e38e2/images/41066334390001-otg-garrafa-1L-4.png?sw=650&sh=650&sm=fit`,
        `${CDN}/dw4f4ba7e9/images/41066334390001-otg-garrafa-1L-5.png?sw=650&sh=650&sm=fit`,
      ]
    },
    realUrl: 'https://www.lecreuset.com.br/garrafa-t%C3%A9rmica-1l-otg-berry/41066334390001.html',
  },
  {
    file: 'copo-otg-berry.html',
    title: 'Copo Térmico 350ml On The Go',
    subtitle: 'Aço Inox · On The Go',
    selectedColor: 'Berry',
    price: 'R$ 279,00',
    installments: '2x R$ 139,50 sem juros',
    pix: 'R$ 265,05 no PIX (5% OFF)',
    desc: 'O Copo Térmico On The Go 350ml é compacto e estiloso. Isolamento a vácuo de parede dupla mantém bebidas quentes por até 6 horas ou frias por até 24 horas. Tampa com mecanismo de travamento e base antiderrapante de silicone.',
    specs: [['Material','Aço Inox'],['Capacidade','350 ml'],['Quente','Até 6 horas'],['Frio','Até 24 horas'],['Lavagem','Lavagem à mão'],['Origem','China'],['Garantia','10 anos']],
    colorImages: {
      Berry:  `${CDN}/dw60cf70ff/images/41067194390001-otg-copo-berry.png?sw=650&sh=650&sm=fit`,
      Cotton: `${CDN}/dw94dbfa52/images/41067354310001-copo-cotton-otg.png?sw=650&sh=650&sm=fit`,
    },
    extraImages: {},
    realUrl: 'https://www.lecreuset.com.br/copo-termico-350ml-otg-berry/41067194390001.html',
  },
  {
    file: 'pote-otg-berry.html',
    title: 'Pote Térmico 500ml On The Go',
    subtitle: 'Aço Inox · On The Go',
    selectedColor: 'Berry',
    price: 'R$ 299,00',
    installments: '2x R$ 149,50 sem juros',
    pix: 'R$ 284,05 no PIX (5% OFF)',
    desc: 'O Pote Térmico On The Go 500ml é perfeito para levar refeições ou snacks. Isolamento a vácuo de parede dupla, tampa hermética antiverga e design ergonômico. Perfeito para o trabalho, academia ou viagens.',
    specs: [['Material','Aço Inox'],['Capacidade','500 ml'],['Lavagem','Lavagem à mão'],['Origem','China'],['Garantia','10 anos']],
    colorImages: {
      Berry:  `${CDN}/dw8a6d9177/images/41068124390001-pote-otg-berry.png?sw=650&sh=650&sm=fit`,
      Cotton: `${CDN}/dwff325f96/images/41068504310001-pote-otg-cotton.png?sw=650&sh=650&sm=fit`,
    },
    extraImages: {},
    realUrl: 'https://www.lecreuset.com.br/pote-t%C3%A9rmico-500ml-otg-berry/41068124390001.html',
  },
  {
    file: 'lancheira-otg-berry.html',
    title: 'Lancheira 900ml On The Go',
    subtitle: 'Aço Inox · On The Go',
    selectedColor: 'Berry',
    price: 'R$ 419,00',
    installments: '4x R$ 104,75 sem juros',
    pix: 'R$ 398,05 no PIX (5% OFF)',
    desc: 'A Lancheira On The Go 900ml da Le Creuset foi criada para trazer praticidade e estilo à sua rotina diária. Com formato retangular, tampa hermética antiverga e isolamento que mantém os alimentos na temperatura ideal. Ideal para levar almoço ao trabalho ou lanches em viagens.',
    specs: [['Material','Aço Inox'],['Capacidade','900 ml'],['Lavagem','Lavagem à mão'],['Origem','China'],['Garantia','10 anos']],
    colorImages: {
      Berry:  `${CDN}/dw68d094ec/images/41069224390001-lancheira-otg-berry.png?sw=650&sh=650&sm=fit`,
      Cotton: `${CDN}/dw15a948c3/images/41069904310001-lancheira-otg-cotton.png?sw=650&sh=650&sm=fit`,
    },
    extraImages: {},
    realUrl: 'https://www.lecreuset.com.br/lancheira-900ml-otg/41069224390001.html',
  },
];

function buildPage(p) {
  const borderStyle = 'style="box-sizing:border-box;border:2px solid transparent;width:100%;height:100%;display:flex;align-items:center;justify-content:center;overflow:hidden;"';

  // Build color swatches HTML
  const swatches = OTG_COLORS.map(c => {
    const isActive = c.name === p.selectedColor ? 'active' : '';
    const hasImg = p.colorImages[c.name];
    const imgUrl = hasImg || p.colorImages['Berry'];
    if (c.real && hasImg) {
      return `<div class="color-swatch ${isActive}" style="background:${c.hex};" title="${c.name}"
        onclick="selectColorOTG(this,'${c.name}','${hasImg}')"></div>`;
    } else {
      // No local image — link to real site
      return `<div class="color-swatch ${isActive}" style="background:${c.hex};opacity:0.7;" title="${c.name} — ver no site oficial"
        onclick="selectColorOTGExternal(this,'${c.name}','${p.realUrl}')"></div>`;
    }
  }).join('\n');

  // Build thumbs (Berry images)
  const berryImgs = [p.colorImages['Berry'], ...(p.extraImages['Berry'] || [])];
  const thumbsHtml = berryImgs.length > 1 ? `<div class="gallery-thumbs" id="galleryThumbs">
    ${berryImgs.map((u,i) => `<div class="thumb${i===0?' active':''}" onclick="setImg(this,'${u}')"><img src="${u}" alt="" /></div>`).join('\n')}
  </div>` : '';

  const specs = p.specs.map(([k,v]) => `<tr><td class="spec-key">${k}</td><td class="spec-val">${v}</td></tr>`).join('');

  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>${p.title} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:'Nunito Sans',sans-serif;color:#000;background:#fff;}
    a{text-decoration:none;color:inherit;}
    .top-bar{background:#1a1a1a;color:#fff;font-size:12px;text-align:center;padding:8px 16px;}
    header{background:#fff;border-bottom:1px solid #e5e5e5;position:sticky;top:0;z-index:100;}
    .header-inner{max-width:1400px;margin:0 auto;padding:0 24px;display:flex;align-items:center;height:64px;gap:24px;}
    .logo img{height:45px;width:auto;}
    nav{flex:1;}
    .nav-list{display:flex;list-style:none;align-items:center;}
    .nav-list>li>a{display:block;padding:22px 14px;font-size:13px;font-weight:600;color:#000;white-space:nowrap;border-bottom:2px solid transparent;transition:border-color .2s;}
    .nav-list>li>a:hover{border-bottom-color:#000;}
    .header-icons{display:flex;align-items:center;gap:16px;flex-shrink:0;}
    .header-icons a{font-size:12px;font-weight:600;display:flex;flex-direction:column;align-items:center;gap:2px;color:#000;}
    .header-icons svg{width:22px;height:22px;}
    .search-box{display:flex;align-items:center;border:1px solid #ccc;border-radius:4px;overflow:hidden;height:36px;}
    .search-box input{border:none;outline:none;padding:0 12px;font-size:13px;width:180px;font-family:inherit;}
    .search-box button{background:#000;border:none;cursor:pointer;padding:0 12px;height:100%;display:flex;align-items:center;}
    .search-box button svg{fill:#fff;width:16px;height:16px;}
    /* Breadcrumb */
    .breadcrumb{max-width:1400px;margin:0 auto;padding:14px 24px;font-size:12px;color:#888;display:flex;gap:6px;align-items:center;}
    .breadcrumb a{color:#888;} .breadcrumb a:hover{text-decoration:underline;}
    /* Product layout */
    .product-wrap{max-width:1400px;margin:0 auto;padding:0 24px 80px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start;}
    .gallery{position:sticky;top:80px;}
    .gallery-main{width:100%;aspect-ratio:1;background:#f7f7f4;display:flex;align-items:center;justify-content:center;overflow:hidden;cursor:zoom-in;border-radius:4px;}
    .gallery-main img{width:100%;height:100%;object-fit:contain;padding:24px;transition:transform .4s;}
    .gallery-main:hover img{transform:scale(1.07);}
    .gallery-thumbs{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap;}
    .thumb{width:80px;height:80px;background:#f7f7f4;border:2px solid transparent;cursor:pointer;border-radius:3px;overflow:hidden;transition:border-color .2s;}
    .thumb.active{border-color:#9B2973;}
    .thumb img{width:100%;height:100%;object-fit:contain;padding:6px;}
    /* Product info */
    .product-info{padding-top:4px;}
    .badge-otg{display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;letter-spacing:.5px;background:#9B2973;color:#fff;margin-bottom:12px;}
    .product-title{font-size:28px;font-weight:800;letter-spacing:-.5px;line-height:1.2;margin-bottom:6px;}
    .product-subtitle{font-size:13px;color:#888;margin-bottom:20px;}
    .product-pix{font-size:13px;color:#2a8a2a;font-weight:700;margin-bottom:4px;}
    .product-price{font-size:32px;font-weight:800;margin-bottom:4px;}
    .product-installments{font-size:13px;color:#666;margin-bottom:24px;}
    /* Color picker */
    .color-label{font-size:13px;font-weight:700;margin-bottom:10px;display:flex;gap:8px;align-items:center;}
    .color-name-display{font-weight:400;color:#555;}
    .color-swatches{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px;}
    .color-swatch{width:28px;height:28px;border-radius:50%;border:2px solid transparent;cursor:pointer;transition:transform .15s,box-shadow .15s;}
    .color-swatch:hover{transform:scale(1.15);}
    .color-swatch.active{box-shadow:0 0 0 2px #fff,0 0 0 4px #000;transform:scale(1.1);}
    .color-note{font-size:12px;color:#888;margin-top:-16px;margin-bottom:20px;display:none;}
    .color-note.visible{display:block;}
    /* Buttons */
    .btn-buy{display:block;width:100%;background:#000;color:#fff;border:none;padding:16px;font-size:14px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;cursor:pointer;font-family:inherit;transition:background .2s;margin-bottom:10px;border-radius:2px;text-align:center;}
    .btn-buy:hover{background:#333;}
    .btn-cart{display:block;width:100%;background:#fff;color:#000;border:2px solid #000;padding:14px;font-size:14px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;cursor:pointer;font-family:inherit;transition:background .2s,color .2s;margin-bottom:24px;border-radius:2px;text-align:center;}
    .btn-cart:hover{background:#000;color:#fff;}
    /* Description & specs */
    .product-desc{font-size:14px;color:#444;line-height:1.75;margin-bottom:28px;padding-bottom:28px;border-bottom:1px solid #eee;}
    .specs-title{font-size:13px;font-weight:800;letter-spacing:1px;text-transform:uppercase;margin-bottom:16px;}
    .spec-table{width:100%;border-collapse:collapse;font-size:13px;}
    .spec-table tr{border-bottom:1px solid #f0f0f0;}
    .spec-key{padding:10px 0;color:#888;width:42%;font-weight:600;}
    .spec-val{padding:10px 0;color:#111;font-weight:600;}
    /* OTG strip */
    .otg-strip{background:#1a1a1a;color:#fff;padding:48px 24px;text-align:center;margin-top:60px;}
    .otg-strip h2{font-size:28px;font-weight:800;margin-bottom:10px;}
    .otg-strip p{font-size:14px;color:rgba(255,255,255,.8);max-width:600px;margin:0 auto 20px;}
    .otg-strip a{display:inline-block;background:#fff;color:#000;padding:12px 28px;font-size:13px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;text-decoration:none;}
    /* Footer */
    footer{background:#111;color:#fff;padding:48px 24px 28px;}
    .footer-inner{max-width:1400px;margin:0 auto;}
    .footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;margin-bottom:40px;}
    .footer-brand p{font-size:13px;color:#aaa;line-height:1.7;max-width:260px;margin-top:14px;}
    .footer-col h4{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:14px;}
    .footer-col ul{list-style:none;}
    .footer-col ul li{margin-bottom:9px;}
    .footer-col ul li a{font-size:13px;color:#aaa;} .footer-col ul li a:hover{color:#fff;}
    .footer-bottom{border-top:1px solid #333;padding-top:20px;font-size:12px;color:#666;}
    /* Mobile */
    .mobile-menu-btn{display:none;background:none;border:none;cursor:pointer;padding:8px;flex-direction:column;justify-content:center;gap:5px;flex-shrink:0;}
    .mobile-menu-btn span{display:block;width:22px;height:2px;background:#000;border-radius:2px;}
    .mobile-nav{display:block;position:fixed;top:0;left:0;width:82%;max-width:300px;height:100%;background:#fff;z-index:999;overflow-y:auto;transform:translateX(-100%);transition:transform .3s;box-shadow:4px 0 24px rgba(0,0,0,.18);}
    .mobile-nav.open{transform:translateX(0);}
    .mobile-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:996;}
    .mobile-overlay.open{display:block;}
    .mobile-nav-header{display:flex;align-items:center;justify-content:flex-end;padding:14px 16px;}
    .mobile-nav-close{background:none;border:none;cursor:pointer;font-size:28px;color:#000;line-height:1;}
    .mnav-links{list-style:none;padding:8px 0;}
    .mnav-links li>a{display:block;padding:14px 18px;font-size:15px;color:#333;}
    .bottom-nav{display:none;}
    @media(max-width:768px){
      nav{display:none;} .search-box{display:none;}
      .mobile-menu-btn{display:flex;}
      .logo img{height:32px;} .header-inner{padding:0 12px;height:56px;}
      .header-icons a span{display:none;}
      .product-wrap{grid-template-columns:1fr;gap:24px;padding:0 14px 80px;}
      .gallery{position:static;}
      .product-title{font-size:22px;}
      .product-price{font-size:26px;}
      .thumb{width:64px;height:64px;}
      .footer-grid{grid-template-columns:1fr;gap:24px;}
      footer{padding:36px 14px 80px;}
      .otg-strip{padding:36px 16px;}
      .bottom-nav{display:flex;position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #e5e5e5;z-index:500;height:56px;}
      .bottom-nav-item{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:10px;font-weight:600;color:#666;text-decoration:none;}
      .bottom-nav-item svg{width:22px;height:22px;}
    }
  </style>
</head>
<body>
<div class="top-bar">&#x1F69A; Frete Grátis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>
<header>
  <div class="header-inner">
    <button class="mobile-menu-btn" onclick="document.getElementById('mNav').classList.add('open');document.getElementById('mOvl').classList.add('open');">
      <span></span><span></span><span></span>
    </button>
    <a href="index.html" class="logo"><img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites/default/dwd459bb3e/images/logo.svg" alt="Le Creuset"/></a>
    <nav>
      <ul class="nav-list">
        <li><a href="#">Comprar</a></li>
        <li><a href="colecao-foret.html">Forêt</a></li>
        <li><a href="colecao-lancamentos.html">Lançamentos</a></li>
        <li><a href="colecao-ofertas.html">Ofertas</a></li>
        <li><a href="colecao-best-sellers.html">Best-Sellers</a></li>
      </ul>
    </nav>
    <div class="header-icons">
      <div class="search-box">
        <input type="text" placeholder="Buscar..."/>
        <button><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
      </div>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-linecap="round"/></svg><span>Entrar</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round"/></svg><span>Sacola</span></a>
    </div>
  </div>
</header>

<div class="breadcrumb">
  <a href="index.html">Home</a><span>/</span>
  <a href="colecao-lancamentos.html">Lançamentos</a><span>/</span>
  <span>${p.title}</span>
</div>

<div class="product-wrap">
  <div class="gallery">
    <div class="gallery-main"><img src="${p.colorImages['Berry']}" alt="${p.title}" id="mainImgEl"/></div>
    ${thumbsHtml}
  </div>
  <div class="product-info">
    <div class="badge-otg">LANÇAMENTO</div>
    <h1 class="product-title">${p.title}</h1>
    <div class="product-subtitle">${p.subtitle}</div>
    <div class="product-pix">${p.pix}</div>
    <div class="product-price" id="prodPrice">${p.price}</div>
    <div class="product-installments" id="prodInstall">${p.installments}</div>
    <div class="color-label">Cor: <span class="color-name-display" id="colorDisplay">${p.selectedColor}</span></div>
    <div class="color-swatches">${swatches}</div>
    <div class="color-note" id="colorNote">Esta cor está disponível no <a href="${p.realUrl}" target="_blank" style="color:#9B2973;font-weight:700;">site oficial Le Creuset</a></div>
    <a href="#" class="btn-buy">Comprar Agora</a>
    <a href="#" class="btn-cart">Adicionar à Sacola</a>
    <div class="product-desc">${p.desc}</div>
    <div class="specs-title">Especificações</div>
    <table class="spec-table">${specs}</table>
    <div style="margin-top:32px;">
      <a href="colecao-lancamentos.html" style="display:inline-flex;align-items:center;gap:6px;font-size:13px;color:#9B2973;font-weight:700;text-decoration:none;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><polyline points="15 18 9 12 15 6"/></svg>
        Voltar para Lançamentos
      </a>
    </div>
  </div>
</div>

<div class="otg-strip">
  <h2>Coleção On The Go</h2>
  <p>Praticidade e estilo Le Creuset para o seu dia a dia. Disponível em 9 cores vibrantes.</p>
  <a href="colecao-lancamentos.html">Ver Todos os Lançamentos</a>
</div>

<nav class="mobile-nav" id="mNav">
  <div class="mobile-nav-header">
    <button class="mobile-nav-close" onclick="document.getElementById('mNav').classList.remove('open');document.getElementById('mOvl').classList.remove('open');">&times;</button>
  </div>
  <ul class="mnav-links">
    <li><a href="colecao-lancamentos.html">Lançamentos</a></li>
    <li><a href="colecao-foret.html">Forêt</a></li>
    <li><a href="index.html">Home</a></li>
  </ul>
</nav>
<div class="mobile-overlay" id="mOvl" onclick="document.getElementById('mNav').classList.remove('open');this.classList.remove('open');"></div>

<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html"><img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites/default/dwd459bb3e/images/logo.svg" alt="Le Creuset" style="height:28px;filter:brightness(0) invert(1);"/></a>
        <p>Desde 1925, Le Creuset cria peças excepcionais que combinam funcionalidade e beleza.</p>
      </div>
      <div class="footer-col"><h4>Ajuda</h4><ul><li><a href="#">Fale Conosco</a></li><li><a href="#">Trocas e Devoluções</a></li><li><a href="#">Garantia</a></li></ul></div>
      <div class="footer-col"><h4>Legal</h4><ul><li><a href="#">Privacidade</a></li><li><a href="#">Termos de Uso</a></li></ul></div>
    </div>
    <div class="footer-bottom">&copy; 2026 Le Creuset Brasil. Todos os direitos reservados.</div>
  </div>
</footer>

<nav class="bottom-nav">
  <a href="index.html" class="bottom-nav-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" stroke-linecap="round"/></svg>Home</a>
  <a href="colecao-lancamentos.html" class="bottom-nav-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" stroke-linecap="round"/></svg>Novidades</a>
  <a href="#" class="bottom-nav-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round"/></svg>Sacola</a>
</nav>

<script>
var colorImages = ${JSON.stringify(p.colorImages)};

function setImg(el, url) {
  document.getElementById('mainImgEl').src = url;
  document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
}

function selectColorOTG(el, colorName, imgUrl) {
  document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('colorDisplay').textContent = colorName;
  document.getElementById('mainImgEl').src = imgUrl;
  document.getElementById('colorNote').classList.remove('visible');
}

function selectColorOTGExternal(el, colorName, realUrl) {
  document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('colorDisplay').textContent = colorName;
  document.getElementById('colorNote').classList.add('visible');
  document.querySelector('#colorNote a').href = realUrl;
}
</script>
</body>
</html>`;
}

let count = 0;
for (const p of PRODUCTS) {
  const html = buildPage(p);
  fs.writeFileSync(path.join(BASE, p.file), html, 'utf8');
  console.log('OK:', p.file);
  count++;
}
console.log(`\nTotal: ${count} páginas atualizadas`);
