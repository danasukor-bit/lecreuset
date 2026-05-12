# -*- coding: utf-8 -*-
import os, re, glob

DIR = os.path.dirname(os.path.abspath(__file__))
BASE_IMG = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'
BANNER_BASE = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/'

def img(h, f, q='sw=650&sh=650&sm=fit'):
    return f'{BASE_IMG}{h}/images/{f}?{q}'

TOP_BAR = '<div class="top-bar">\U0001f69a Frete Grátis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>'

NAV = '''<nav>
      <ul class="nav-list">
        <li>
          <a href="#">Comprar</a>
          <div class="mega-menu">
            <div class="mega-inner">
              <div class="mega-col">
                <div class="mega-col-title">Cozinhar</div>
                <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
                <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
                <a href="colecao-grelhas.html">Grelhas</a>
                <a href="colecao-antiaderente.html">Antiaderente</a>
                <a href="colecao-cacarolas.html">Caçarolas</a>
                <a href="#">Chaleiras de Aço Esmaltado</a>
                <a href="#">3-Ply Aço Inox</a>
                <a href="#">Aço Inox</a>
                <a href="#">Formatos Especiais</a>
                <a href="#">Acessórios</a>
                <a href="#">Minha Primeira Le Creuset</a>
                <a href="#">Stockpots</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Assar</div>
                <a href="#">Mini Cocotte e Ramekins</a>
                <a href="#">Formas Metal Bakeware</a>
                <a href="#">Assadeiras e Travessas</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Acessórios</div>
                <a href="#">Moedores e Galheteiro</a>
                <a href="#">Utensílios</a>
                <a href="#">Utensílios de Madeira</a>
                <a href="#">Suportes e Descansos</a>
                <a href="#">Potes e Porta-Mantimentos</a>
                <a href="#">Acessórios de Vinhos</a>
                <a href="#">Sets</a>
                <a href="#">Decoração</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Preparar e Servir</div>
                <a href="colecao-ceramica.html">Bowls</a>
                <a href="colecao-ceramica.html">Pratos</a>
                <a href="colecao-ceramica.html">Canecas e Xícaras</a>
                <a href="#">Bules e Jarras</a>
                <a href="#">Chaleiras</a>
                <a href="colecao-ceramica.html">Travessas</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Coleções</div>
                <a href="#">Flamme Dorée</a>
                <a href="#">Gift Collection</a>
                <a href="#">Churrasco</a>
                <a href="#">Coleção Alpine</a>
                <a href="colecao-cacarolas.html">Modern Heritage</a>
                <a href="#">Coleção Jardim</a>
                <a href="#">Culinária Oriental</a>
                <a href="#">Coleção Gourmand</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Nossas Cores</div>
                <div class="mega-colors">
                  <div class="mega-color-dot" style="background:#2DBECD;" title="Bleu Riviera"></div>
                  <div class="mega-color-dot" style="background:#d46820;" title="Laranja"></div>
                  <div class="mega-color-dot" style="background:#c8102e;" title="Vermelho"></div>
                  <div class="mega-color-dot" style="background:#C85250;" title="Cerise"></div>
                  <div class="mega-color-dot" style="background:#6B4226;" title="Marronnier"></div>
                  <div class="mega-color-dot" style="background:#D4C44A;" title="Nectar"></div>
                  <div class="mega-color-dot" style="background:#B8BEC4;" title="Mist"></div>
                  <div class="mega-color-dot" style="background:#D4779A;" title="Rose Quartz"></div>
                  <div class="mega-color-dot" style="background:#F5F5F5;border:1px solid #ddd;" title="Branco"></div>
                  <div class="mega-color-dot" style="background:#9B7EB0;" title="Bluebell"></div>
                  <div class="mega-color-dot" style="background:#2060A0;" title="Azure"></div>
                  <div class="mega-color-dot" style="background:#D4A017;" title="Flamme Dorée"></div>
                  <div class="mega-color-dot" style="background:#5A5A5A;" title="Graphite"></div>
                  <div class="mega-color-dot" style="background:#1C1C1C;" title="Matte Black"></div>
                </div>
              </div>
              <div class="mega-col" style="padding-top:4px;">
                <a href="colecao-bleu-riviera.html" style="display:block; overflow:hidden; border-radius:6px;">
                  <img class="mega-img" src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit" alt="Bleu Riviera Le Creuset" />
                </a>
              </div>
            </div>
          </div>
        </li>
        <li class="highlight"><a href="colecao-pascoa.html">Páscoa</a></li>
        <li><a href="colecao-ofertas.html">Ofertas</a></li>
        <li class="blue"><a href="colecao-bleu-riviera.html">Bleu Riviera</a></li>
        <li><a href="colecao-lancamentos.html">Lançamentos</a></li>
        <li><a href="colecao-ferro-fundido.html">Ferro Fundido</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>
        <li><a href="colecao-best-sellers.html">Best-Sellers</a></li>
      </ul>
    </nav>'''

HEADER_ICONS = '''<div class="header-icons">
      <div class="search-box">
        <input type="text" placeholder="Buscar..." />
        <button><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
      </div>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Entrar</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Lista</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Sacola</span></a>
    </div>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Le <span style="color:#c8102e">Creuset</span></a>
        <p>Desde 1925, criamos peças excepcionais que transformam a experiência culinária e duram gerações.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a><a href="#" class="social-btn">in</a><a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul>
        <li><a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a></li>
        <li><a href="colecao-frigideiras-e-skillets.html">Frigideiras</a></li>
        <li><a href="colecao-cacarolas.html">Caçarolas</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="colecao-antiaderente.html">Antiaderente</a></li>
      </ul></div>
      <div class="footer-col"><h4>Atendimento</h4><ul>
        <li><a href="#">Central de Ajuda</a></li>
        <li><a href="#">Rastrear Pedido</a></li>
        <li><a href="#">Trocas e Devoluções</a></li>
        <li><a href="#">Garantia</a></li>
      </ul></div>
      <div class="footer-col"><h4>Empresa</h4><ul>
        <li><a href="#">Sobre Nós</a></li>
        <li><a href="#">Lojas Físicas</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">Receitas</a></li>
      </ul></div>
      <div class="footer-col"><h4>Legal</h4><ul>
        <li><a href="#">Política de Privacidade</a></li>
        <li><a href="#">Termos de Uso</a></li>
        <li><a href="#">Cookies</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Le Creuset do Brasil. Todos os direitos reservados.</p>
      <div class="payment-icons">
        <span class="payment-icon">VISA</span><span class="payment-icon">MASTER</span>
        <span class="payment-icon">PIX</span><span class="payment-icon">BOLETO</span>
      </div>
    </div>
  </div>
</footer>'''

BASE_CSS = '''*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Nunito Sans', sans-serif; color: #000; background: #fff; }
    a { text-decoration: none; color: inherit; }
    .top-bar { background: #1a1a1a; color: #fff; font-size: 12px; text-align: center; padding: 8px 16px; }
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
    .mega-menu { display: none; position: fixed; left: 0; right: 0; top: 64px; background: #fff; border-top: 2px solid #e5e5e5; box-shadow: 0 8px 32px rgba(0,0,0,0.13); z-index: 200; padding: 28px 0 24px; }
    .nav-list > li:hover .mega-menu { display: block; }
    .mega-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: 170px 150px 170px 170px 170px 140px 220px; gap: 0 20px; align-items: start; }
    .mega-col-title { font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: #000; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 1px solid #e5e5e5; }
    .mega-col a { display: block; font-size: 13px; color: #444; padding: 4px 0; transition: color 0.15s; }
    .mega-col a:hover { color: #c8102e; }
    .mega-colors { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
    .mega-color-dot { width: 22px; height: 22px; border-radius: 50%; border: 1.5px solid transparent; cursor: pointer; transition: transform 0.2s, border-color 0.2s; }
    .mega-color-dot:hover { border-color: #000; transform: scale(1.12); }
    .mega-img { width: 100%; object-fit: cover; border-radius: 6px; }
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
    .cat-banner { width: 100%; height: 260px; overflow: hidden; position: relative; background: #1a1a1a; }
    .cat-banner img { width: 100%; height: 100%; object-fit: cover; object-position: center 35%; display: block; }
    .cat-banner-overlay { position: absolute; inset: 0; background: linear-gradient(to right, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.05) 60%); display: flex; flex-direction: column; justify-content: center; padding: 0 80px; }
    .cat-banner-title { color: #fff; font-size: 44px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 10px; }
    .cat-banner-sub { color: rgba(255,255,255,0.85); font-size: 15px; max-width: 500px; line-height: 1.6; }
    .breadcrumb { max-width: 1400px; margin: 0 auto; padding: 14px 24px; font-size: 12px; color: #888; display: flex; gap: 6px; align-items: center; }
    .breadcrumb a { color: #888; } .breadcrumb a:hover { text-decoration: underline; } .breadcrumb span { color: #bbb; }
    .shop-layout { max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; display: grid; grid-template-columns: 220px 1fr; gap: 40px; align-items: start; }
    .sidebar { position: sticky; top: 80px; }
    .sidebar-section { margin-bottom: 28px; }
    .sidebar-title { font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 1px solid #e5e5e5; }
    .sidebar-list { list-style: none; }
    .sidebar-list li { margin-bottom: 8px; }
    .sidebar-list li a { font-size: 13px; color: #444; }
    .sidebar-list li a:hover { color: #c8102e; }
    .product-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
    .product-card { position: relative; }
    .product-card-img { position: relative; overflow: hidden; background: #f8f8f8; aspect-ratio: 1; margin-bottom: 12px; }
    .product-card-img img { width: 100%; height: 100%; object-fit: contain; padding: 16px; transition: transform 0.4s ease; }
    .product-card-img:hover img { transform: scale(1.06); }
    .product-wishlist { position: absolute; top: 10px; right: 10px; width: 32px; height: 32px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    .product-wishlist svg { width: 16px; height: 16px; }
    .product-badge { position: absolute; top: 10px; left: 10px; font-size: 10px; font-weight: 700; padding: 3px 8px; letter-spacing: 0.5px; }
    .product-badge.sale { background: #c8102e; color: #fff; }
    .product-badge.new { background: #2DBECD; color: #fff; }
    .product-badge.star { background: #000; color: #fff; }
    .product-card-name { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
    .product-card-sub { font-size: 12px; color: #888; margin-bottom: 6px; }
    .product-card-price { font-size: 15px; font-weight: 800; }
    .product-card-price-orig { font-size: 12px; color: #aaa; text-decoration: line-through; margin-bottom: 2px; }
    .product-card-price-sale { font-size: 15px; font-weight: 800; color: #c8102e; }
    .results-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
    .results-count { font-size: 13px; color: #888; }
    .sort-select { font-size: 13px; border: 1px solid #ccc; padding: 6px 12px; font-family: inherit; cursor: pointer; }
    /* Nossas Cores specific */
    .cores-section { max-width: 1400px; margin: 0 auto; padding: 48px 24px 80px; }
    .cores-intro { font-size: 15px; color: #555; line-height: 1.7; max-width: 700px; margin-bottom: 48px; }
    .cores-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; margin-bottom: 60px; }
    .cor-card { cursor: pointer; }
    .cor-swatch { width: 100%; aspect-ratio: 1; border-radius: 50%; margin-bottom: 12px; transition: transform 0.2s, box-shadow 0.2s; }
    .cor-card:hover .cor-swatch { transform: scale(1.05); box-shadow: 0 8px 24px rgba(0,0,0,0.15); }
    .cor-name { font-size: 13px; font-weight: 700; text-align: center; margin-bottom: 4px; }
    .cor-sub { font-size: 11px; color: #888; text-align: center; }
    .section-title-big { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 8px; }
    .section-divider { width: 40px; height: 3px; background: #000; margin-bottom: 32px; }
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
    .footer-col ul li a { font-size: 13px; color: #aaa; transition: color 0.2s; }
    .footer-col ul li a:hover { color: #fff; }
    .footer-bottom { border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 12px; color: #666; }
    .payment-icons { display: flex; gap: 8px; }
    .payment-icon { background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }'''

WISHLIST_BTN = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

def card(name, slug, image_url, price, subtitle='', badge='', badge_cls=''):
    badge_html = f'<div class="product-badge {badge_cls}">{badge}</div>' if badge else ''
    sub_html = f'<div class="product-card-sub">{subtitle}</div>' if subtitle else ''
    return f'''    <div class="product-card">
      <a href="{slug}">
        <div class="product-card-img">
          <img src="{image_url}" alt="{name}" />
          {badge_html}{WISHLIST_BTN}
        </div>
      </a>
      <a href="{slug}">
        <div class="product-card-name">{name}</div>
        {sub_html}
        <div class="product-card-price">{price}</div>
      </a>
    </div>'''

def card_sale(name, slug, image_url, price_orig, price_sale, subtitle=''):
    sub_html = f'<div class="product-card-sub">{subtitle}</div>' if subtitle else ''
    return f'''    <div class="product-card">
      <a href="{slug}">
        <div class="product-card-img">
          <img src="{image_url}" alt="{name}" />
          <div class="product-badge sale">OFERTA</div>{WISHLIST_BTN}
        </div>
      </a>
      <a href="{slug}">
        <div class="product-card-name">{name}</div>
        {sub_html}
        <div class="product-card-price-orig">{price_orig}</div>
        <div class="product-card-price-sale">{price_sale}</div>
      </a>
    </div>'''

def page_wrap(title, banner_html, breadcrumb_items, content):
    bc = ''
    for i, (label, href) in enumerate(breadcrumb_items):
        if i < len(breadcrumb_items) - 1:
            bc += f'<a href="{href}">{label}</a><span>/</span>'
        else:
            bc += f'<span>{label}</span>'
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>{BASE_CSS}</style>
</head>
<body>
{TOP_BAR}
<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    {NAV}
    {HEADER_ICONS}
  </div>
</header>
{banner_html}
<div class="breadcrumb">{bc}</div>
{content}
{FOOTER}
</body>
</html>'''

# ── 1. PÁSCOA ────────────────────────────────────────────────────────────────
pascoa_products = [
    ('Caçarola Buffet Signature', 'cacarola-buffet-signature.html',
     img('dwe61a242b', '21180300994450-cacarola-buffet-bleu.jpg'), 'R$ 2.069,25 – R$ 3.269,00', 'Ferro Fundido · Bleu Riviera'),
    ('Mini Cocotte', 'mini-cocotte.html',
     img('dwc027de66', 'produto-lecreuset-minicocotte-laranja-vermelho.png'), 'R$ 167,30 – R$ 239,00', 'Cerâmica · Edição Especial'),
    ('Set 4 Mini Buffet com Tampa Gourmand', 'set-4-mini-buffet-tampa-gourmand.html',
     img('dw25efbfaf', 'mini-cocotte-jardin-250ml-shell%20pink.png'), 'R$ 769,00', 'Cerâmica · Set de 4'),
    ('Bowl Redondo Vancouver', 'bowl-redondo-vancouver.html',
     img('dwda92585c', '70117160997099-bowl-redondo-16cm.jpg'), 'R$ 139,00 – R$ 439,00', 'Cerâmica · Bleu Riviera'),
    ('Caneca London 200ml', 'caneca-london.html',
     img('dwf07f51d0', 'produto-lecreuset-caneca-200ml-vermelho.png'), 'R$ 129,00 – R$ 159,00', 'Cerâmica · Diversas Cores'),
    ('Pote de Manteiga', 'pote-de-manteiga.html',
     img('dwe2c6a579', 'produto-lecreuset-pote-manteiga-vermelho%20(1).png'), 'R$ 319,00', 'Cerâmica'),
    ('Travessa Canelada', 'travessa-canelada.html',
     img('dw678a9329', 'travessa-canelada-vermelho-lecreuset.jpg'), 'R$ 370,30 – R$ 529,00', 'Cerâmica · Para Assar'),
    ('Porta Condimento', 'porta-condimento.html',
     img('dw96391238', 'porta-condimento-laranja-lecreuset4.png'), 'R$ 289,00 – R$ 439,00', 'Cerâmica'),
    ('Mini Cocotte Jardin Shell Pink', 'mini-cocotte.html',
     img('dw25efbfaf', 'mini-cocotte-jardin-250ml-shell%20pink.png'), 'R$ 174,30', 'Coleção Jardim · Edição Especial'),
    ('Caneca Jardin 200ml', 'caneca-jardin.html',
     img('dw4df08c7b', 'caneca-jardin.png'), 'R$ 111,30', 'Coleção Jardim'),
    ('Set Azeite & Vinagre Clássico', 'set-azeite-vinagre.html',
     img('dwe9691760', '80803020600003.jpg'), 'R$ 579,00', 'Presente Perfeito'),
    ('Caçarola Buffet Abóbora', 'cacarola-buffet-abobora.html',
     img('dwca6362ac', 'ca%C3%A7arola-buffet-signature-abobora-pegador-dourado-meringue-28cm.png'), 'R$ 2.299,00', 'Ferro Fundido · Design Especial'),
]

pascoa_cards = '\n'.join(card(n, s, i, p, sub, 'PÁSCOA', 'new') for n, s, i, p, sub in pascoa_products)

pascoa_html = page_wrap(
    'Páscoa',
    f'''<div class="cat-banner" style="height:320px;">
  <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/03%20-%20Marco/pascoa-banner-desk.jpg" alt="Páscoa Le Creuset" style="object-position:center 30%;" />
  <div class="cat-banner-overlay" style="background:linear-gradient(to right,rgba(0,0,0,0.5) 0%,rgba(0,0,0,0.05) 60%);">
    <h1 class="cat-banner-title" style="font-size:52px;">Páscoa Le Creuset</h1>
    <p class="cat-banner-sub">Presentes e peças especiais para celebrar esta data única com elegância e sabor.</p>
  </div>
</div>''',
    [('Home', 'index.html'), ('Páscoa', '')],
    f'''<div class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Presentes</a></li>
        <li><a href="#">Ferro Fundido</a></li>
        <li><a href="#">Cerâmica</a></li>
        <li><a href="#">Sets</a></li>
        <li><a href="#">Coleção Jardim</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Preço</div>
      <ul class="sidebar-list">
        <li><a href="#">Até R$ 250</a></li>
        <li><a href="#">R$ 250 – R$ 500</a></li>
        <li><a href="#">R$ 500 – R$ 1.000</a></li>
        <li><a href="#">Acima de R$ 1.000</a></li>
      </ul>
    </div>
  </aside>
  <div>
    <div class="results-bar">
      <span class="results-count">{len(pascoa_products)} produtos em destaque</span>
      <select class="sort-select"><option>Mais Relevante</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{pascoa_cards}
    </div>
  </div>
</div>'''
)

with open(os.path.join(DIR, 'colecao-pascoa.html'), 'w', encoding='utf-8') as f:
    f.write(pascoa_html)
print('Created: colecao-pascoa.html')

# ── 2. OFERTAS ───────────────────────────────────────────────────────────────
ofertas_products = [
    ('Moedor de Pimenta 21cm', '#',
     img('dw0d048d4a', 'produto-lecreuset-moedores-meringue.png'), 'R$ 369,00', 'R$ 295,20', 'Acessórios · Meringue'),
    ('Moedor de Sal 21cm', '#',
     img('dw0d048d4a', 'produto-lecreuset-moedores-meringue.png'), 'R$ 369,00', 'R$ 295,20', 'Acessórios · Meringue'),
    ('Chaleira Clássica Meringue', '#',
     img('dw6bbc1145', '40104027160000.jpg'), 'R$ 929,00', 'R$ 650,30', 'Aço Esmaltado'),
    ('Caçarola Buffet Signature', 'cacarola-buffet-signature.html',
     img('dw8283d435', 'produto-lecreuset-ca%C3%A7arola-redonda-laranja.png'), 'R$ 2.999,00', 'R$ 2.249,25', 'Ferro Fundido · Laranja'),
    ('Caçarola Buffet Signature Meringue', 'cacarola-buffet-signature.html',
     img('dwd198c7aa', 'produto-lecreuset-ca%C3%A7arola-redonda-meringue.png'), 'R$ 2.999,00', 'R$ 2.249,25', 'Ferro Fundido · Meringue'),
    ('Porta Utensílios Clássico', '#',
     img('dw22ed2a42', 'porta_utensilios_meringue_le_creuset.jpg'), 'R$ 319,00', 'R$ 223,30', 'Cerâmica · Meringue'),
    ('Mini Cocotte', 'mini-cocotte.html',
     img('dw84b7660e', 'produto-lecreuset-minicocotte-laranja-meringue.png'), 'R$ 239,00', 'R$ 167,30', 'Cerâmica · Meringue'),
    ('Travessa Retangular Heritage', '#',
     img('dwf31b1dc6', 'travessas-produto-lecreuset-heritage-laranja.png'), 'R$ 709,00', 'R$ 496,30', 'Cerâmica · Laranja'),
    ('Mini Cocotte Jardin Shell Pink', 'mini-cocotte.html',
     img('dw25efbfaf', 'mini-cocotte-jardin-250ml-shell%20pink.png'), 'R$ 249,00', 'R$ 174,30', 'Coleção Jardim'),
    ('Mini Cocotte Jardin Meringue', 'mini-cocotte.html',
     img('dw757ce2f5', 'mini-cocotte-jardin-250ml-meringue.png'), 'R$ 249,00', 'R$ 174,30', 'Coleção Jardim'),
    ('Caneca Jardin 350ml', 'caneca-jardin.html',
     img('dw0f692789', 'caneca-jardin-350ml-shell%20pink.png'), 'R$ 189,00', 'R$ 132,30', 'Coleção Jardim'),
    ('Stockpot Pegador Fenólico', '#',
     img('dw3fab14a7', 'stockpot-coolmint-lecreuset-peg-fenolico.png'), 'R$ 959,00', 'R$ 671,30', 'Ferro Fundido · Cool Mint'),
]

ofertas_cards = '\n'.join(card_sale(n, s, i, po, ps, sub) for n, s, i, po, ps, sub in ofertas_products)

ofertas_html = page_wrap(
    'Ofertas',
    f'''<div class="cat-banner">
  <img src="{BANNER_BASE}dw160b3f5e/category/cat_banners/categoria-lancamentos-novembro.png" alt="Ofertas Le Creuset" />
  <div class="cat-banner-overlay">
    <h1 class="cat-banner-title">Ofertas</h1>
    <p class="cat-banner-sub">Aproveite descontos exclusivos em peças Le Creuset selecionadas.</p>
  </div>
</div>''',
    [('Home', 'index.html'), ('Ofertas', '')],
    f'''<div class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Ferro Fundido</a></li>
        <li><a href="#">Cerâmica</a></li>
        <li><a href="#">Chaleiras</a></li>
        <li><a href="#">Acessórios</a></li>
        <li><a href="#">Coleção Jardim</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Desconto</div>
      <ul class="sidebar-list">
        <li><a href="#">Até 20% OFF</a></li>
        <li><a href="#">20% – 30% OFF</a></li>
        <li><a href="#">Acima de 30% OFF</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Preço</div>
      <ul class="sidebar-list">
        <li><a href="#">Até R$ 300</a></li>
        <li><a href="#">R$ 300 – R$ 700</a></li>
        <li><a href="#">Acima de R$ 700</a></li>
      </ul>
    </div>
  </aside>
  <div>
    <div class="results-bar">
      <span class="results-count">{len(ofertas_products)} produtos em oferta</span>
      <select class="sort-select"><option>Maior Desconto</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{ofertas_cards}
    </div>
  </div>
</div>'''
)

with open(os.path.join(DIR, 'colecao-ofertas.html'), 'w', encoding='utf-8') as f:
    f.write(ofertas_html)
print('Created: colecao-ofertas.html')

# ── 3. BEST-SELLERS ──────────────────────────────────────────────────────────
bs_products = [
    ('Caçarola Buffet Signature', 'cacarola-buffet-signature.html',
     img('dwe61a242b', '21180300994450-cacarola-buffet-bleu.jpg'), 'R$ 2.069,25 – R$ 3.269,00', 'Ferro Fundido · #1 Mais Vendido'),
    ('Caneca London 200ml', 'caneca-london.html',
     img('dwf07f51d0', 'produto-lecreuset-caneca-200ml-vermelho.png'), 'R$ 129,00 – R$ 159,00', 'Cerâmica · Favorito dos Clientes'),
    ('Mini Cocotte', 'mini-cocotte.html',
     img('dwc027de66', 'produto-lecreuset-minicocotte-laranja-vermelho.png'), 'R$ 167,30 – R$ 239,00', 'Cerâmica · Edição Exclusiva'),
    ('Frigideira Rasa Antiaderente', 'frigideira-rasa-antiaderente.html',
     img('dw9b3c7a15', 'frigideira-rasa-antiaderente-laranja.png'), 'R$ 489,00 – R$ 749,00', 'Antiaderente · Mais Vendida'),
    ('Bowl Redondo Vancouver 16cm', 'bowl-redondo-vancouver.html',
     img('dwc3e0652f', 'produto-lecreuset-bowl-16cm-artichaut1.png'), 'R$ 139,00 – R$ 439,00', 'Cerâmica'),
    ('Caçarola Buffet Signature Petal', 'cacarola-buffet-signature-petal.html',
     img('dwdc236776', 'ca%C3%A7arola-buffet-signature-petal-seasalt%20(2).png'), 'R$ 2.099,00', 'Ferro Fundido · Edição Limitada'),
    ('Prato Raso Vancouver 27cm', 'prato-raso-vancouver.html',
     img('dwcc99b044', 'produto-lecreuset-prato-27cm-vermelho.png'), 'R$ 199,00 – R$ 239,00', 'Cerâmica'),
    ('Set 4 Antiaderente de Cerâmica', 'set-4-antiaderente-ceramica.html',
     img('dw7a4b8c6d', 'set-4-antiaderentes-ceramica-vermelho.png'), 'R$ 1.099,00', 'Antiaderente · Conjunto'),
    ('Skillet Redonda Signature Bleu', '#',
     img('dwa644c41e', '20182230990422-skillet-redonda-blue.jpg'), 'R$ 1.999,00', 'Ferro Fundido · Bleu Riviera'),
    ('Caneca Bistrô 400ml', 'caneca-bistro-400ml.html',
     img('dw2bd91f79', 'Caneca-azure-400ml.png'), 'R$ 189,00', 'Cerâmica · 400ml'),
    ('Travessa Canelada 28cm', 'travessa-canelada.html',
     img('dw678a9329', 'travessa-canelada-vermelho-lecreuset.jpg'), 'R$ 370,30 – R$ 529,00', 'Cerâmica · Para Assar'),
    ('Caçarola Buffet Modern Heritage', 'cacarola-buffet-modern-heritage.html',
     img('dw5a6b2fa5', 'cacarola-buffet-28Cm-Modern-laranja-Heritage.png'), 'R$ 2.099,00', 'Ferro Fundido · Modern Heritage'),
]

bs_cards = '\n'.join(card(n, s, i, p, sub, '★ BEST SELLER', 'star') for n, s, i, p, sub in bs_products)

bs_html = page_wrap(
    'Best-Sellers',
    f'''<div class="cat-banner">
  <img src="{BANNER_BASE}dw370316e7/category/cat_banners/cozinhar.jpg" alt="Best-Sellers Le Creuset" style="object-position:center 30%;" />
  <div class="cat-banner-overlay">
    <h1 class="cat-banner-title">Best-Sellers</h1>
    <p class="cat-banner-sub">As peças Le Creuset mais amadas pelos nossos clientes.</p>
  </div>
</div>''',
    [('Home', 'index.html'), ('Best-Sellers', '')],
    f'''<div class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Ferro Fundido</a></li>
        <li><a href="#">Cerâmica</a></li>
        <li><a href="#">Antiaderente</a></li>
        <li><a href="#">Acessórios</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Preço</div>
      <ul class="sidebar-list">
        <li><a href="#">Até R$ 300</a></li>
        <li><a href="#">R$ 300 – R$ 700</a></li>
        <li><a href="#">R$ 700 – R$ 1.500</a></li>
        <li><a href="#">Acima de R$ 1.500</a></li>
      </ul>
    </div>
  </aside>
  <div>
    <div class="results-bar">
      <span class="results-count">{len(bs_products)} produtos mais vendidos</span>
      <select class="sort-select"><option>Mais Vendidos</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{bs_cards}
    </div>
  </div>
</div>'''
)

with open(os.path.join(DIR, 'colecao-best-sellers.html'), 'w', encoding='utf-8') as f:
    f.write(bs_html)
print('Created: colecao-best-sellers.html')

# ── 4. NOSSAS CORES ──────────────────────────────────────────────────────────
CORES = [
    ('Bleu Riviera', '#2DBECD', False, 'A cor da temporada', 'colecao-bleu-riviera.html'),
    ('Laranja', '#d46820', False, 'O clássico Le Creuset', 'colecao-panelas-de-ferro.html'),
    ('Vermelho', '#c8102e', False, 'Força e paixão', '#'),
    ('Cerise', '#C85250', False, 'Rosa intenso', '#'),
    ('Marronnier', '#6B4226', False, 'Elegância terrosa', '#'),
    ('Nectar', '#D4C44A', False, 'Dourado vibrante', '#'),
    ('Meringue', '#F5F0E8', True, 'Suavidade francesa', '#'),
    ('Branco', '#F5F5F5', True, 'Pureza clássica', '#'),
    ('Mist', '#B8BEC4', False, 'Cinza névoa', '#'),
    ('Rose Quartz', '#D4779A', False, 'Rosa delicado', '#'),
    ('Bluebell', '#9B7EB0', False, 'Lilás encantador', '#'),
    ('Azure', '#2060A0', False, 'Azul profundo', '#'),
    ('Flamme Dorée', '#D4A017', False, 'Dourado especial', '#'),
    ('Graphite', '#5A5A5A', False, 'Grafite moderno', '#'),
    ('Matte Black', '#1C1C1C', False, 'Preto mate sofisticado', '#'),
    ('Shell Pink', '#F0B8C8', False, 'Rosa concha suave', '#'),
]

cores_cards = ''
for name, bg, need_border, desc, href in CORES:
    border_style = ' border: 2px solid #ddd;' if need_border else ''
    cores_cards += f'''    <a href="{href}" class="cor-card">
      <div class="cor-swatch" style="background:{bg};{border_style}"></div>
      <div class="cor-name">{name}</div>
      <div class="cor-sub">{desc}</div>
    </a>\n'''

# Featured products by color
color_featured = [
    ('Caçarola Buffet Signature — Bleu Riviera', 'cacarola-buffet-signature.html',
     img('dwe61a242b', '21180300994450-cacarola-buffet-bleu.jpg'), 'R$ 2.069,25 – R$ 3.269,00', 'Bleu Riviera'),
    ('Caçarola Buffet Signature — Laranja', 'cacarola-buffet-signature.html',
     img('dw8283d435', 'produto-lecreuset-ca%C3%A7arola-redonda-laranja.png'), 'R$ 2.069,25 – R$ 3.269,00', 'Laranja'),
    ('Caneca London — Vermelho', 'caneca-london.html',
     img('dwf07f51d0', 'produto-lecreuset-caneca-200ml-vermelho.png'), 'R$ 129,00 – R$ 159,00', 'Vermelho'),
    ('Bowl Redondo — Bleu Riviera', 'bowl-redondo-vancouver.html',
     img('dwda92585c', '70117160997099-bowl-redondo-16cm.jpg'), 'R$ 139,00 – R$ 439,00', 'Bleu Riviera'),
    ('Caçarola Petal — Sea Salt', 'cacarola-buffet-signature-petal.html',
     img('dwdc236776', 'ca%C3%A7arola-buffet-signature-petal-seasalt%20(2).png'), 'R$ 2.099,00', 'Sea Salt'),
    ('Mini Cocotte — Vermelho', 'mini-cocotte.html',
     img('dwc027de66', 'produto-lecreuset-minicocotte-laranja-vermelho.png'), 'R$ 167,30 – R$ 239,00', 'Vermelho'),
]

color_cards = '\n'.join(card(n, s, i, p, sub) for n, s, i, p, sub in color_featured)

cores_html = page_wrap(
    'Nossas Cores',
    f'''<div class="cat-banner" style="height:280px;background:#f8f4f0;">
  <img src="{BANNER_BASE}dw370316e7/category/cat_banners/cozinhar.jpg" alt="Nossas Cores Le Creuset" style="mix-blend-mode:multiply;opacity:0.4;" />
  <div class="cat-banner-overlay" style="background:linear-gradient(135deg,rgba(200,16,46,0.6) 0%,rgba(45,190,205,0.4) 100%);">
    <h1 class="cat-banner-title" style="font-size:52px;">Nossas Cores</h1>
    <p class="cat-banner-sub">Desde 1925, as cores Le Creuset expressam individualidade, criatividade e paixão pela gastronomia.</p>
  </div>
</div>''',
    [('Home', 'index.html'), ('Nossas Cores', '')],
    f'''<div class="cores-section">
  <p class="cores-intro">Cada cor Le Creuset conta uma história. Desde o icônico Laranja da fundação até o inconfundível Bleu Riviera da temporada atual, nossas cores são muito mais que estética — são uma expressão de personalidade à mesa.</p>

  <h2 class="section-title-big">Paleta de Cores</h2>
  <div class="section-divider"></div>
  <div class="cores-grid">
{cores_cards}  </div>

  <h2 class="section-title-big">Produtos em Destaque por Cor</h2>
  <div class="section-divider"></div>
  <div class="product-grid">
{color_cards}
  </div>
</div>'''
)

with open(os.path.join(DIR, 'colecao-nossas-cores.html'), 'w', encoding='utf-8') as f:
    f.write(cores_html)
print('Created: colecao-nossas-cores.html')

# ── Update nav in all existing HTML files ────────────────────────────────────
REPLACEMENTS = [
    ('<li class="highlight"><a href="#">Páscoa</a></li>',
     '<li class="highlight"><a href="colecao-pascoa.html">Páscoa</a></li>'),
    ('<li><a href="#">Ofertas</a></li>',
     '<li><a href="colecao-ofertas.html">Ofertas</a></li>'),
    ('<li><a href="#">Nossas Cores</a></li>',
     '<li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>'),
    ('<li><a href="#">Best-Sellers</a></li>',
     '<li><a href="colecao-best-sellers.html">Best-Sellers</a></li>'),
]

new_files = {'colecao-pascoa.html', 'colecao-ofertas.html', 'colecao-nossas-cores.html', 'colecao-best-sellers.html'}
updated = 0
for fpath in glob.glob(os.path.join(DIR, '*.html')):
    if os.path.basename(fpath) in new_files:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    new_html = html
    for old, new in REPLACEMENTS:
        new_html = new_html.replace(old, new)
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f'Updated nav in {updated} existing files')
print('Done!')
