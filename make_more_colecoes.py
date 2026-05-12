# -*- coding: utf-8 -*-
import os, re, glob

DIR = os.path.dirname(os.path.abspath(__file__))
BASE_IMG = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'
BANNER_BASE = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/'

def img(h, f, q='sw=650&sh=650&sm=fit'):
    return f'{BASE_IMG}{h}/images/{f}?{q}'

# ── Shared HTML fragments (same nav/header/footer pattern) ──────────────────

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
        <li class="highlight"><a href="#">Páscoa</a></li>
        <li><a href="#">Ofertas</a></li>
        <li class="blue"><a href="colecao-bleu-riviera.html">Bleu Riviera</a></li>
        <li><a href="colecao-lancamentos.html">Lançamentos</a></li>
        <li><a href="colecao-ferro-fundido.html">Ferro Fundido</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="#">Nossas Cores</a></li>
        <li><a href="#">Best-Sellers</a></li>
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
    .sidebar-list li a { font-size: 13px; color: #444; display: flex; align-items: center; gap: 8px; }
    .sidebar-list li a:hover { color: #c8102e; }
    .sidebar-colors { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }
    .sidebar-dot { width: 22px; height: 22px; border-radius: 50%; cursor: pointer; border: 1.5px solid transparent; transition: transform 0.15s, border-color 0.15s; }
    .sidebar-dot:hover { border-color: #000; transform: scale(1.1); }
    .product-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
    .product-card { position: relative; }
    .product-card-img { position: relative; overflow: hidden; background: #f8f8f8; aspect-ratio: 1; margin-bottom: 12px; }
    .product-card-img img { width: 100%; height: 100%; object-fit: contain; padding: 16px; transition: transform 0.4s ease; }
    .product-card-img:hover img { transform: scale(1.06); }
    .product-wishlist { position: absolute; top: 10px; right: 10px; width: 32px; height: 32px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    .product-wishlist svg { width: 16px; height: 16px; }
    .product-badge { position: absolute; top: 10px; left: 10px; background: #000; color: #fff; font-size: 10px; font-weight: 700; padding: 3px 8px; letter-spacing: 0.5px; }
    .product-badge.new { background: #2DBECD; }
    .product-card-name { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
    .product-card-sub { font-size: 12px; color: #888; margin-bottom: 6px; }
    .product-card-price { font-size: 15px; font-weight: 800; }
    .results-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
    .results-count { font-size: 13px; color: #888; }
    .sort-select { font-size: 13px; border: 1px solid #ccc; padding: 6px 12px; font-family: inherit; cursor: pointer; }
    /* Ferro fundido hub */
    .hub-section { max-width: 1400px; margin: 0 auto; padding: 40px 24px 80px; }
    .hub-title { font-size: 13px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: #888; margin-bottom: 32px; }
    .category-tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 60px; }
    .cat-tile { position: relative; overflow: hidden; aspect-ratio: 4/3; border-radius: 4px; cursor: pointer; }
    .cat-tile img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
    .cat-tile:hover img { transform: scale(1.05); }
    .cat-tile-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.1) 60%); display: flex; flex-direction: column; justify-content: flex-end; padding: 20px; }
    .cat-tile-title { color: #fff; font-size: 20px; font-weight: 800; letter-spacing: -0.3px; margin-bottom: 8px; }
    .cat-tile-btn { display: inline-block; background: #fff; color: #000; font-size: 11px; font-weight: 700; padding: 6px 14px; letter-spacing: 0.5px; text-transform: uppercase; align-self: flex-start; }
    .cat-tile-btn:hover { background: #000; color: #fff; }
    .featured-section { margin-bottom: 60px; }
    .section-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 24px; padding-bottom: 12px; border-bottom: 2px solid #000; }
    .section-title { font-size: 22px; font-weight: 800; }
    .section-link { font-size: 12px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; border-bottom: 1px solid #000; padding-bottom: 2px; }
    .section-link:hover { color: #c8102e; border-color: #c8102e; }
    /* Bleu Riviera hero */
    .bleu-hero { width: 100%; height: 480px; overflow: hidden; position: relative; background: #1a3a5c; }
    .bleu-hero img { width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; }
    .bleu-hero-overlay { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,55,100,0.7) 0%, rgba(0,100,180,0.3) 50%, transparent 100%); display: flex; flex-direction: column; justify-content: center; padding: 0 100px; }
    .bleu-hero-title { color: #fff; font-size: 56px; font-weight: 800; letter-spacing: -1px; line-height: 1; margin-bottom: 12px; }
    .bleu-hero-sub { color: rgba(255,255,255,0.9); font-size: 16px; max-width: 420px; line-height: 1.6; margin-bottom: 24px; }
    .bleu-hero-btn { display: inline-block; background: #fff; color: #000; padding: 14px 28px; font-size: 13px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; align-self: flex-start; }
    .bleu-hero-btn:hover { background: #000; color: #fff; }
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

WISHLIST_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def product_card(name, slug, image_url, price, subtitle='', badge='', badge_cls=''):
    badge_html = f'<div class="product-badge {badge_cls}">{badge}</div>' if badge else ''
    sub_html = f'<div class="product-card-sub">{subtitle}</div>' if subtitle else ''
    return f'''    <div class="product-card">
      <a href="{slug}">
        <div class="product-card-img">
          <img src="{image_url}" alt="{name}" />
          {badge_html}
          <div class="product-wishlist">{WISHLIST_SVG}</div>
        </div>
      </a>
      <a href="{slug}">
        <div class="product-card-name">{name}</div>
        {sub_html}
        <div class="product-card-price">{price}</div>
      </a>
    </div>'''

def page_wrapper(title, css_extra, banner_html, breadcrumb_items, content, scripts=''):
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
  <style>{BASE_CSS}{css_extra}</style>
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
{scripts}
</body>
</html>'''

# ── 1. FERRO FUNDIDO hub page ────────────────────────────────────────────────
ferro_banner = f'''<div class="cat-banner">
  <img src="{BANNER_BASE}dw370316e7/category/cat_banners/cozinhar.jpg" alt="Ferro Fundido Le Creuset" />
  <div class="cat-banner-overlay">
    <h1 class="cat-banner-title">Ferro Fundido</h1>
    <p class="cat-banner-sub">O melhor ferro fundido do mundo — distribuição de calor superior, resistência excepcional e cores que inspiram.</p>
  </div>
</div>'''

# Products to feature from existing collections
ferro_products_panelas = [
    ('Caçarola Buffet Signature', 'cacarola-buffet-signature.html',
     img('dwe61a242b', '21180300994450-cacarola-buffet-bleu.jpg'), 'R$ 2.069,25 – R$ 3.269,00', 'Ferro Fundido · 26cm / 30cm'),
    ('Caçarola Redonda', 'colecao-panelas-de-ferro.html',
     img('dw8283d435', 'produto-lecreuset-ca%C3%A7arola-redonda-laranja.png'), 'R$ 1.569,00 – R$ 2.969,00', 'Ferro Fundido · 20cm a 30cm'),
    ('Caçarola Buffet Modern Heritage', 'cacarola-buffet-modern-heritage.html',
     img('dw5a6b2fa5', 'cacarola-buffet-28Cm-Modern-laranja-Heritage.png'), 'R$ 2.099,00', 'Ferro Fundido · 28cm'),
]
ferro_products_frigideiras = [
    ('Skillet Redonda Signature', 'colecao-frigideiras-e-skillets.html',
     img('dwa644c41e', '20182230990422-skillet-redonda-blue.jpg'), 'R$ 1.999,00', 'Ferro Fundido · 30cm'),
    ('Frigideira Grill Quadrada', 'colecao-grelhas.html',
     img('dwff3c7614', 'produto-lecreuset-grelha-quadrada-laranja.png'), 'R$ 1.299,00', 'Ferro Fundido · 26cm'),
    ('Plancha Retangular', 'colecao-grelhas.html',
     img('dw9d3b2801', 'produto-lecreuset-plancha-retangular-laranja.png'), 'R$ 1.399,00', 'Ferro Fundido'),
]

def make_product_row(products):
    return '\n'.join(product_card(n, s, i, p, sub) for n, s, i, p, sub in products)

ferro_content = f'''<div class="hub-section">
  <div class="hub-title">Coleções de Ferro Fundido</div>

  <div class="category-tiles">
    <a href="colecao-panelas-de-ferro.html" class="cat-tile">
      <img src="{img('dw8283d435', 'produto-lecreuset-ca%C3%A7arola-redonda-laranja.png')}" alt="Panelas de Ferro" />
      <div class="cat-tile-overlay">
        <div class="cat-tile-title">Panelas de Ferro</div>
        <span class="cat-tile-btn">Ver Coleção</span>
      </div>
    </a>
    <a href="colecao-frigideiras-e-skillets.html" class="cat-tile">
      <img src="{img('dwa644c41e', '20182230990422-skillet-redonda-blue.jpg')}" alt="Frigideiras e Skillets" />
      <div class="cat-tile-overlay">
        <div class="cat-tile-title">Frigideiras e Skillets</div>
        <span class="cat-tile-btn">Ver Coleção</span>
      </div>
    </a>
    <a href="colecao-grelhas.html" class="cat-tile">
      <img src="{img('dwff3c7614', 'produto-lecreuset-grelha-quadrada-laranja.png')}" alt="Grelhas e Grills" />
      <div class="cat-tile-overlay">
        <div class="cat-tile-title">Grelhas e Grills</div>
        <span class="cat-tile-btn">Ver Coleção</span>
      </div>
    </a>
  </div>

  <div class="featured-section">
    <div class="section-header">
      <div class="section-title">Panelas de Ferro em Destaque</div>
      <a href="colecao-panelas-de-ferro.html" class="section-link">Ver Todos</a>
    </div>
    <div class="product-grid">
{make_product_row(ferro_products_panelas)}
    </div>
  </div>

  <div class="featured-section">
    <div class="section-header">
      <div class="section-title">Frigideiras e Grelhas</div>
      <a href="colecao-frigideiras-e-skillets.html" class="section-link">Ver Todos</a>
    </div>
    <div class="product-grid">
{make_product_row(ferro_products_frigideiras)}
    </div>
  </div>
</div>'''

ferro_html = page_wrapper(
    'Ferro Fundido',
    '',
    ferro_banner,
    [('Home', 'index.html'), ('Ferro Fundido', '')],
    ferro_content
)

with open(os.path.join(DIR, 'colecao-ferro-fundido.html'), 'w', encoding='utf-8') as f:
    f.write(ferro_html)
print('Created: colecao-ferro-fundido.html')

# ── 2. BLEU RIVIERA collection ───────────────────────────────────────────────
bleu_products = [
    ('Skillet Redonda Signature', '#',
     img('dwa644c41e', '20182230990422-skillet-redonda-blue.jpg'), 'R$ 1.999,00', 'Ferro Fundido · Bleu Riviera'),
    ('Caneca London 350ml', '#',
     img('dw07ae9b98', '70302350990002-caneca-350ml-riviera.jpg'), 'R$ 159,00', 'Cerâmica · 350ml'),
    ('Bowl Redondo Vancouver 16cm', 'bowl-redondo-vancouver.html',
     img('dwda92585c', '70117160997099-bowl-redondo-16cm.jpg'), 'R$ 209,00', 'Cerâmica · 16cm'),
    ('Chaleira Cloche', '#',
     img('dwdf67a668', '40109010991000-chaleira-cloche.jpg'), 'R$ 1.069,00', 'Aço Esmaltado'),
    ('Prato Raso Vancouver 22cm', 'prato-raso-vancouver.html',
     img('dw99b3e915', '70202270997099-prato-raso22cm-bleu.png'), 'R$ 219,00', 'Cerâmica · 22cm'),
    ('Travessa Retangular Heritage', '#',
     img('dw1876dd56', '71102190990001-travessa-retangular.jpg'), 'R$ 709,00', 'Cerâmica · 32cm'),
    ('Caneca London 200ml', 'caneca-london.html',
     img('dw1af63394', '70303200990099-caneca-300ml-riviera.jpg'), 'R$ 139,00', 'Cerâmica · 200ml'),
    ('Prato Fundo 22cm', 'prato-fundo-22cm.html',
     img('dw9dccf1a0', '70102220997099-prato-fundo-bleu.jpg'), 'R$ 219,00', 'Cerâmica · 22cm'),
    ('Chaleira Clássica Pegador Aço Inox', '#',
     img('dw147839aa', 'chaleira-classica-flint-pegador-inox.png'), 'R$ 929,00', 'Aço Esmaltado'),
    ('Colher de Silicone Signature', '#',
     img('dwe01b3a17', '42072000990000-colher-de-silicone.jpg'), 'R$ 199,00', 'Utensílios'),
    ('Espátula Média de Silicone', '#',
     img('dwb2545411', '42073000990000-espatula-medida-silicone.jpg'), 'R$ 179,00', 'Utensílios'),
    ('Caçarola Buffet Signature', 'cacarola-buffet-signature.html',
     img('dwe61a242b', '21180300994450-cacarola-buffet-bleu.jpg'), 'R$ 2.069,25 – R$ 3.269,00', 'Ferro Fundido'),
]

bleu_cards = '\n'.join(
    product_card(n, s, i, p, sub, 'BLEU RIVIERA', 'new')
    for n, s, i, p, sub in bleu_products
)

bleu_banner = f'''<div class="bleu-hero">
  <img src="{BANNER_BASE}dw1df60bac/category/cat_banners/banner_bleu_categoria.jpeg" alt="Bleu Riviera Le Creuset" />
  <div class="bleu-hero-overlay">
    <h1 class="bleu-hero-title">Bleu Riviera</h1>
    <p class="bleu-hero-sub">Uma cor que evoca as águas cristalinas do Mediterrâneo. Descubra toda a linha Bleu Riviera Le Creuset.</p>
    <a href="#produtos" class="bleu-hero-btn">Explorar a Coleção</a>
  </div>
</div>'''

bleu_content = f'''<div id="produtos" class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Panelas e Caçarolas</a></li>
        <li><a href="#">Frigideiras e Skillets</a></li>
        <li><a href="#">Cerâmica</a></li>
        <li><a href="#">Chaleiras</a></li>
        <li><a href="#">Utensílios</a></li>
        <li><a href="#">Travessas</a></li>
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
      <span class="results-count">{len(bleu_products)} produtos em Bleu Riviera</span>
      <select class="sort-select"><option>Mais Relevante</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{bleu_cards}
    </div>
  </div>
</div>'''

bleu_html = page_wrapper(
    'Bleu Riviera',
    '',
    bleu_banner,
    [('Home', 'index.html'), ('Bleu Riviera', '')],
    bleu_content
)

with open(os.path.join(DIR, 'colecao-bleu-riviera.html'), 'w', encoding='utf-8') as f:
    f.write(bleu_html)
print('Created: colecao-bleu-riviera.html')

# ── 3. LANÇAMENTOS collection ────────────────────────────────────────────────
lanc_products = [
    ('Chaleira Clássica Pegador Aço Inox', '#',
     img('dw147839aa', 'chaleira-classica-flint-pegador-inox.png'), 'R$ 929,00', 'Novo · Aço Esmaltado'),
    ('Travessa Retangular Clássica com Tampa', '#',
     img('dwd20d97eb', '81001530600005-travessa-retangular.jpg'), 'R$ 1.059,00', 'Novo · Cerâmica'),
    ('Chaleira Cloche Bleu Riviera', '#',
     img('dwdf67a668', '40109010991000-chaleira-cloche.jpg'), 'R$ 1.069,00', 'Novo · Aço Esmaltado'),
    ('Colher de Silicone Signature', '#',
     img('dwe01b3a17', '42072000990000-colher-de-silicone.jpg'), 'R$ 199,00', 'Novo · Utensílios'),
    ('Espátula Pequena de Silicone', '#',
     img('dwa51e9835', '42074000990000-espatula-media-silicone.jpg'), 'R$ 159,00', 'Novo · Utensílios'),
    ('Pincel de Silicone Signature', '#',
     img('dwc39367ed', '42071000990000-pincel-de-silicone.jpg'), 'R$ 199,00', 'Novo · Utensílios'),
    ('Espátula Média de Silicone', '#',
     img('dwb2545411', '42073000990000-espatula-medida-silicone.jpg'), 'R$ 179,00', 'Novo · Utensílios'),
    ('Travessa com Tampa Heritage para Peixe', '#',
     img('dw34668c60', '81065600990350-travessa-peixe-1.jpg'), 'R$ 1.219,00', 'Novo · Ferro Fundido'),
    ('Prato para Aperitivos e Molhos', '#',
     img('dw0c4da547', '8200034099009-prato-para-aperitivos.jpg'), 'R$ 889,00', 'Novo · Cerâmica'),
    ('Caneca Sphere 320ml', '#',
     img('dwd8b68a52', '80324320990099-caneca-sphere.jpg'), 'R$ 189,00', 'Novo · Cerâmica'),
    ('Caneca Seattle Alça Dourada 400ml', '#',
     img('dw0a9940b7', '80317400995699-caneca-seattle-bleu.jpg'), 'R$ 239,00', 'Novo · Cerâmica'),
    ('Caneca Abóbora 400ml', 'caneca-bistro-400ml.html',
     img('dw416d5116', '80313400900003-caneca-abobora-laranja.jpg'), 'R$ 449,00', 'Novo · Cerâmica'),
]

lanc_cards = '\n'.join(
    product_card(n, s, i, p, sub, 'NOVO', 'new')
    for n, s, i, p, sub in lanc_products
)

lanc_banner = f'''<div class="cat-banner">
  <img src="{BANNER_BASE}dw1df60bac/category/cat_banners/banner_bleu_categoria.jpeg" alt="Lançamentos Le Creuset" />
  <div class="cat-banner-overlay">
    <h1 class="cat-banner-title">Lançamentos</h1>
    <p class="cat-banner-sub">As últimas novidades Le Creuset — descubra peças exclusivas e edições especiais.</p>
  </div>
</div>'''

lanc_content = f'''<div class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Ferro Fundido</a></li>
        <li><a href="#">Cerâmica</a></li>
        <li><a href="#">Chaleiras</a></li>
        <li><a href="#">Utensílios</a></li>
        <li><a href="#">Travessas</a></li>
        <li><a href="#">Canecas</a></li>
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
      <span class="results-count">{len(lanc_products)} novos produtos</span>
      <select class="sort-select"><option>Mais Novo</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{lanc_cards}
    </div>
  </div>
</div>'''

lanc_html = page_wrapper(
    'Lançamentos',
    '',
    lanc_banner,
    [('Home', 'index.html'), ('Lançamentos', '')],
    lanc_content
)

with open(os.path.join(DIR, 'colecao-lancamentos.html'), 'w', encoding='utf-8') as f:
    f.write(lanc_html)
print('Created: colecao-lancamentos.html')

# ── Update nav in all existing HTML files ────────────────────────────────────
REPLACEMENTS = [
    ('<a href="#">Bleu Riviera</a>', '<a href="colecao-bleu-riviera.html">Bleu Riviera</a>'),
    ('<a href="#">Lançamentos</a>', '<a href="colecao-lancamentos.html">Lançamentos</a>'),
    ('<a href="#">Ferro Fundido</a>', '<a href="colecao-ferro-fundido.html">Ferro Fundido</a>'),
    # Update mega menu image link
    ('<a href="#" style="display:block; overflow:hidden; border-radius:6px;">\n                  <img class="mega-img" src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit" alt="Bleu Riviera Le Creuset" />',
     '<a href="colecao-bleu-riviera.html" style="display:block; overflow:hidden; border-radius:6px;">\n                  <img class="mega-img" src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit" alt="Bleu Riviera Le Creuset" />'),
]

updated = 0
new_files = {'colecao-ferro-fundido.html', 'colecao-bleu-riviera.html', 'colecao-lancamentos.html'}
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
