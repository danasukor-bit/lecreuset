#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE   = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN    = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q      = "?sw=650&sh=650&sm=fit"
BANNER = "https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwfb0a8e24/category/cat_banners/categoria-site-bowl-laranja.png"

WISH = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

COLOR_HEX = {
    "Vermelho":"#C41E3A","Laranja":"#FE5000","Black Onyx":"#1a1a1a",
    "Bleu Riviera":"#0066B2","Branco":"#FFFFFF","Meringue":"#FDF5E6",
    "Thyme":"#6D7C5E","Caribe":"#00B5CC","Nectar":"#F4A020",
    "Chambray":"#7BA3C8","Marseille":"#1B5E8D","Shell Pink":"#F4C2C2",
    "Azure":"#007FFF","Sea Salt":"#A8C5BB","Matte Black":"#222222",
    "Flint":"#8C8C8C","Artichaut":"#8B9467","Bamboo":"#D4A857",
    "Camomille":"#F5E090","Peche":"#FFCBA4","Nata":"#FFF8DC",
    "Mauve Pink":"#CF9BAE","Rhone":"#6B2D2D","Deep Teal":"#005F5F",
    "Multicor 2":"#FF69B4","Bluebell Purple":"#7B68C8","Cotton":"#F0EDE8",
}

NAV = """<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    <nav><ul class="nav-list">
      <li><a href="#">Comprar</a>
        <div class="mega-menu"><div class="mega-inner">
          <div class="mega-col"><div class="mega-col-title">Cozinhar</div>
            <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
            <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
            <a href="colecao-cacarolas.html">Ca&#231;arolas</a>
            <a href="colecao-acessorios.html">Acess&#243;rios</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Assar</div>
            <a href="colecao-assadeiras-travessas.html">Assadeiras e Travessas</a>
            <a href="colecao-formas-metal-bakeware.html">Formas Metal Bakeware</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Preparar &amp; Servir</div>
            <a href="colecao-bowls.html">Bowls</a>
            <a href="colecao-utensilios.html">Utensilios</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Acess&#243;rios</div>
            <a href="colecao-moedores-e-galheteiro.html">Moedores e Galheteiro</a>
            <a href="colecao-potes-e-porta-mantimentos.html">Potes e Porta-Mantimentos</a>
            <a href="colecao-acessorios-de-vinhos.html">Acess&#243;rios de Vinhos</a>
            <a href="colecao-sets.html">Sets</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Cole&#231;&#245;es</div>
            <a href="colecao-bleu-riviera.html">Bleu Riviera</a>
            <a href="colecao-lancamentos.html">Lan&#231;amentos</a>
            <a href="colecao-best-sellers.html">Best-Sellers</a>
          </div>
        </div></div>
      </li>
      <li class="highlight"><a href="colecao-pascoa.html">P&#225;scoa</a></li>
      <li><a href="colecao-ofertas.html">Ofertas</a></li>
      <li class="blue"><a href="colecao-bleu-riviera.html">Bleu Riviera</a></li>
      <li><a href="colecao-lancamentos.html">Lan&#231;amentos</a></li>
      <li><a href="colecao-ferro-fundido.html">Ferro Fundido</a></li>
      <li><a href="colecao-ceramica.html">Cer&#226;mica</a></li>
      <li><a href="colecao-best-sellers.html">Best-Sellers</a></li>
    </ul></nav>
    <div class="header-icons">
      <div class="search-box">
        <input type="text" placeholder="Buscar..."/>
        <button><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
      </div>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Entrar</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Sacola</span></a>
    </div>
  </div>
</header>"""

FOOT = """<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Le <span>Creuset</span></a>
        <p>Desde 1925, criando pe&#231;as excepcionais que transformam o cozinhar em arte.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a><a href="#" class="social-btn">in</a><a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul>
        <li><a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a></li>
        <li><a href="colecao-ceramica.html">Cer&#226;mica</a></li>
        <li><a href="colecao-acessorios.html">Acess&#243;rios</a></li>
      </ul></div>
      <div class="footer-col"><h4>Atendimento</h4><ul>
        <li><a href="#">Central de Ajuda</a></li><li><a href="#">Rastrear Pedido</a></li>
        <li><a href="#">Trocas e Devolu&#231;&#245;es</a></li>
      </ul></div>
      <div class="footer-col"><h4>Empresa</h4><ul>
        <li><a href="#">Sobre N&#243;s</a></li><li><a href="#">Blog</a></li>
      </ul></div>
      <div class="footer-col"><h4>Legal</h4><ul>
        <li><a href="#">Privacidade</a></li><li><a href="#">Termos</a></li>
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
</footer>"""

CSS_PRODUCT = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    body{font-family:'Nunito Sans',sans-serif;color:#000;background:#fff;}
    a{text-decoration:none;color:inherit;}
    .top-bar{background:#1a1a1a;color:#fff;font-size:12px;text-align:center;padding:8px 16px;}
    header{background:#fff;border-bottom:1px solid #e5e5e5;position:sticky;top:0;z-index:100;}
    .header-inner{max-width:1400px;margin:0 auto;padding:0 24px;display:flex;align-items:center;height:64px;gap:24px;}
    .logo{font-size:22px;font-weight:800;letter-spacing:-1px;white-space:nowrap;flex-shrink:0;}
    .logo span{color:#c8102e;}
    nav{flex:1;}
    .nav-list{display:flex;list-style:none;align-items:center;}
    .nav-list>li{position:relative;}
    .nav-list>li>a{display:block;padding:22px 14px;font-size:13px;font-weight:600;color:#000;white-space:nowrap;border-bottom:2px solid transparent;transition:border-color 0.2s;}
    .nav-list>li>a:hover{border-bottom-color:#000;}
    .nav-list>li.highlight>a{color:#c8102e;}
    .nav-list>li.blue>a{color:#2563ab;}
    .mega-menu{display:none;position:fixed;left:0;right:0;top:64px;background:#fff;border-top:2px solid #e5e5e5;box-shadow:0 8px 32px rgba(0,0,0,0.13);z-index:200;padding:28px 0 24px;}
    .nav-list>li:hover .mega-menu{display:block;}
    .mega-inner{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:170px 150px 170px 170px 170px;gap:0 20px;align-items:start;}
    .mega-col-title{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#000;margin-bottom:14px;padding-bottom:6px;border-bottom:1px solid #e5e5e5;}
    .mega-col a{display:block;font-size:13px;color:#444;padding:4px 0;}
    .mega-col a:hover{color:#c8102e;}
    .header-icons{display:flex;align-items:center;gap:16px;flex-shrink:0;}
    .header-icons a{font-size:12px;font-weight:600;display:flex;flex-direction:column;align-items:center;gap:2px;color:#000;}
    .header-icons svg{width:22px;height:22px;}
    .search-box{display:flex;align-items:center;border:1px solid #ccc;border-radius:4px;overflow:hidden;height:36px;}
    .search-box input{border:none;outline:none;padding:0 12px;font-size:13px;width:180px;font-family:inherit;}
    .search-box button{background:#000;border:none;cursor:pointer;padding:0 12px;height:100%;display:flex;align-items:center;}
    .search-box button svg{fill:#fff;width:16px;height:16px;}
    .breadcrumb{max-width:1400px;margin:0 auto;padding:16px 24px 0;font-size:12px;color:#888;display:flex;gap:5px;align-items:center;}
    .breadcrumb a{color:#888;} .breadcrumb a:hover{color:#000;text-decoration:underline;}
    .product-wrap{max-width:1400px;margin:0 auto;padding:24px 24px 0;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;}
    .product-img-wrap{position:sticky;top:80px;}
    .product-main-img{width:100%;aspect-ratio:1;border:1px solid #f0f0f0;display:flex;align-items:center;justify-content:center;background:#fafafa;overflow:hidden;}
    .product-main-img img{width:100%;height:100%;object-fit:contain;padding:40px;}
    .product-info{padding-top:8px;}
    .product-brand{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#888;margin-bottom:6px;}
    .product-name{font-size:28px;font-weight:800;line-height:1.2;margin-bottom:8px;}
    .product-sub{font-size:14px;color:#555;margin-bottom:20px;}
    .product-price{font-size:26px;font-weight:800;color:#000;margin-bottom:4px;}
    .product-installment{font-size:13px;color:#666;margin-bottom:24px;}
    .color-selector{margin-bottom:28px;}
    .color-label{font-size:13px;color:#333;margin-bottom:12px;font-weight:600;}
    .color-label strong{font-weight:800;}
    .color-swatches{display:flex;gap:10px;flex-wrap:wrap;}
    .color-swatch{width:32px;height:32px;border-radius:50%;cursor:pointer;display:inline-block;transition:transform 0.15s,box-shadow 0.15s;}
    .color-swatch:hover{transform:scale(1.12);}
    .color-swatch.active{box-shadow:0 0 0 2px #fff,0 0 0 4px #000;}
    .btn-cart{display:block;width:100%;background:#000;color:#fff;border:none;padding:16px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;margin-bottom:12px;}
    .btn-cart:hover:not([disabled]){background:#222;}
    .btn-wishlist{display:block;width:100%;background:#fff;color:#000;border:2px solid #000;padding:14px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;}
    .badge-oos{display:inline-block;background:#888;color:#fff;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:3px;margin-bottom:16px;}
    .badge-promo{display:inline-block;background:#c8102e;color:#fff;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:3px;margin-bottom:16px;}
    .price-original{font-size:14px;color:#888;text-decoration:line-through;margin-bottom:2px;}
    .desc-specs-wrap{max-width:1400px;margin:40px auto 0;padding:48px 24px 80px;border-top:1px solid #e5e5e5;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;}
    .section-title{font-size:28px;font-weight:300;margin-bottom:20px;letter-spacing:-0.3px;}
    .desc-text{font-size:14px;line-height:1.8;color:#333;}
    .desc-text p{margin-bottom:12px;}
    .specs-table{width:100%;border-collapse:collapse;}
    .specs-table tr{border-bottom:1px solid #e5e5e5;}
    .specs-table tr:first-child{border-top:1px solid #e5e5e5;}
    .specs-table td{padding:13px 0;font-size:14px;}
    .specs-table td.sk{color:#555;width:48%;}
    .specs-table td.sv{color:#000;}
    footer{background:#111;color:#fff;padding:60px 24px 30px;}
    .footer-inner{max-width:1400px;margin:0 auto;}
    .footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}
    .footer-brand .logo{font-size:20px;margin-bottom:16px;display:block;}
    .footer-brand p{font-size:13px;color:#aaa;line-height:1.7;max-width:280px;margin-bottom:20px;}
    .footer-social{display:flex;gap:12px;}
    .social-btn{width:36px;height:36px;border:1px solid #444;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;}
    .footer-col h4{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:16px;}
    .footer-col ul{list-style:none;}
    .footer-col ul li{margin-bottom:10px;}
    .footer-col ul li a{font-size:13px;color:#aaa;}
    .footer-col ul li a:hover{color:#fff;}
    .footer-bottom{border-top:1px solid #333;padding-top:24px;display:flex;justify-content:space-between;align-items:center;}
    .footer-bottom p{font-size:12px;color:#666;}
    .payment-icons{display:flex;gap:8px;}
    .payment-icon{background:#222;border:1px solid #444;border-radius:4px;padding:4px 8px;font-size:10px;font-weight:700;color:#aaa;}"""


def make_product(filename, title, name, sub, price, install, colors_imgs, desc, specs,
                 sold_out=False, price_original=None, breadcrumb_cat="colecao-bowls.html", breadcrumb_label="Bowls"):
    first_c, first_img = colors_imgs[0]
    swatches = ""
    for i, (cname, cimg) in enumerate(colors_imgs):
        url = CDN + cimg + Q
        hexc = COLOR_HEX.get(cname, "#888")
        bord = "border:2px solid #ccc;" if hexc in ("#FFFFFF","#FDF5E6","#F4C2C2","#A8C5BB","#FFF8DC","#F5E090","#FFCBA4","#F0EDE8") else "border:2px solid transparent;"
        act  = " active" if i == 0 else ""
        swatches += f'<span class="color-swatch{act}" style="background:{hexc};{bord}" title="{cname}" onclick="selectColor(this,\'{cname}\',\'{url}\')"></span>\n      '

    specs_html = "".join(f"<tr><td class='sk'>{k}:</td><td class='sv'>{v}</td></tr>" for k, v in specs)
    desc_html  = "".join(f"<p>{p}</p>" for p in desc)
    first_url  = CDN + first_img + Q

    badge = ""
    if sold_out:
        badge = '<div class="badge-oos">Esgotado</div>'
        cart_btn = '<button class="btn-cart" disabled style="opacity:0.5;cursor:not-allowed;">Produto Esgotado</button>'
    elif price_original:
        badge = '<div class="badge-promo">Oferta</div>'
        cart_btn = '<button class="btn-cart">Adicionar ao Carrinho</button>'
    else:
        cart_btn = '<button class="btn-cart">Adicionar ao Carrinho</button>'

    orig_html = f'<div class="price-original">{price_original}</div>' if price_original else ""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{title} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
  <style>{CSS_PRODUCT}</style>
</head>
<body>
<div class="top-bar">&#128666; Frete Gr&#225;tis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>
{NAV}
<div class="breadcrumb">
  <a href="index.html">In&#237;cio</a><span>/</span>
  <a href="{breadcrumb_cat}">{breadcrumb_label}</a><span>/</span>
  <span>{name}</span>
</div>
<div class="product-wrap">
  <div class="product-img-wrap">
    <div class="product-main-img">
      <img id="mainImgEl" src="{first_url}" alt="{name}"/>
    </div>
  </div>
  <div class="product-info">
    <div class="product-brand">Le Creuset</div>
    {badge}
    <h1 class="product-name">{name}</h1>
    <div class="product-sub">{sub}</div>
    {orig_html}
    <div class="product-price">{price}</div>
    <div class="product-installment">{install}</div>
    <div class="color-selector">
      <div class="color-label">Cor: <strong id="colorName">{first_c}</strong></div>
      <div class="color-swatches">{swatches.strip()}</div>
    </div>
    {cart_btn}
    <button class="btn-wishlist">&#9825; Lista de Desejos</button>
  </div>
</div>
<div class="desc-specs-wrap">
  <div><h2 class="section-title">Descri&#231;&#227;o</h2>
    <div class="desc-text">{desc_html}</div>
  </div>
  <div><h2 class="section-title">Especifica&#231;&#245;es</h2>
    <table class="specs-table"><tbody>{specs_html}</tbody></table>
  </div>
</div>
{FOOT}
<script>
function selectColor(el,name,src){{
  el.parentElement.querySelectorAll('.color-swatch').forEach(x=>x.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('mainImgEl').src=src;
  document.getElementById('colorName').textContent=name;
}}
</script>
</body></html>"""

    with open(os.path.join(BASE, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Produto: {filename}")


# ── Product pages ─────────────────────────────────────────────────────────────

make_product("bowl-redondo-vancouver.html",
    "Bowl Redondo Vancouver Le Creuset",
    "Bowl Redondo Vancouver", "Cer&#226;mica · Tamanhos 11cm, 16cm, 24cm",
    "R$ 139,00 – R$ 439,00", "a partir de 2x de R$ 69,50 sem juros",
    [("Artichaut","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"),
     ("Laranja","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"),
     ("Vermelho","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"),
     ("Bleu Riviera","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"),
     ("Azure","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"),
     ("Meringue","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"),
     ("Shell Pink","dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png")],
    ["O Bowl Redondo Vancouver Le Creuset &#233; a escolha ideal para servir cereais, mingaus e sopas com estilo.",
     "A superf&#237;cie esmaltada facilita a remo&#231;&#227;o dos alimentos e &#233; apta para lava-lou&#231;as. Vai ao forno, microondas e freezer."],
    [("Material","Cer&#226;mica"),("Tamanhos","11cm · 16cm · 24cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-redondo.html",
    "Bowl Redondo Le Creuset",
    "Bowl Redondo", "Cer&#226;mica · Tamanhos 19cm e 24cm",
    "R$ 399,00 – R$ 489,00", "a partir de 3x de R$ 133,00 sem juros",
    [("Vermelho","dw23b665b7/images/91005302060000.jpg"),
     ("Laranja","dw23b665b7/images/91005302060000.jpg"),
     ("Branco","dw23b665b7/images/91005302060000.jpg")],
    ["O Bowl Redondo Le Creuset &#233; vers&#225;til para misturar, mexer, armazenar e servir.",
     "Cer&#226;mica premium com superf&#237;cie esmaltada de f&#225;cil limpeza. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","19cm · 24cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-inox-com-tampa-de-vidro.html",
    "Bowl Inox com Tampa de Vidro Le Creuset",
    "Bowl Inox com Tampa de Vidro", "A&#231;o Inox · Tamanhos 19cm, 23cm, 27cm",
    "R$ 399,00 – R$ 689,00", "a partir de 3x de R$ 133,00 sem juros",
    [("Inox","dwf8b78720/images/bowl-inox-tampa-de-vidro.png")],
    ["Produzido em a&#231;o inoxid&#225;vel, acompanha todas as etapas da rotina, do preparo ao armazenamento, com efici&#234;ncia e elega&#234;ncia.",
     "A tampa de vidro temperado permite visualizar o conte&#250;do com facilidade. Base e aro de silicone antiderrapante com log Le Creuset.",
     "Design empilh&#225;vel para organiza&#231;&#227;o f&#225;cil. Apto para lava-lou&#231;as e freezer."],
    [("Material","A&#231;o Inox + Tampa de Vidro Temperado"),("Tamanhos","19cm · 23cm · 27cm"),
     ("Base","Silicone antiderrapante"),("Cuidados","Lava-lou&#231;as · Freezer"),
     ("Origem","China"),("Garantia","5 anos")])

make_product("multi-bowl-holly.html",
    "Multi Bowl Holly Le Creuset",
    "Multi Bowl Holly", "Cer&#226;mica · 25cm · 4 cores",
    "R$ 619,00", "ou 6x de R$ 103,17 sem juros",
    [("Thyme","dw49ca2d17/images/mult-bowl-holly-thyme.png"),
     ("Vermelho","dw1a1a95a2/images/multi-bowl-holly-vermelho2.png"),
     ("Branco","dw821802b5/images/multi-bowl-holly-branco.png"),
     ("Nata","dw6777c187/images/Nata-lecreuset-2025-2.png")],
    ["O Multi Bowl Holly &#233; o tamanho ideal para ovos mexidos, acompanhamentos, caldos e outros pratos.",
     "Os bowls s&#227;o empilh&#225;veis, facilitando a organiza&#231;&#227;o da cozinha. Cer&#226;mica premium com superf&#237;cie esmaltada de f&#225;cil limpeza. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","25cm × 25cm × 10cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-de-servir-ruffle.html",
    "Bowl de Servir Ruffle 3,8L Le Creuset",
    "Bowl de Servir Ruffle 3,8L", "Cer&#226;mica · 34cm · 2 cores",
    "R$ 769,00", "ou 7x de R$ 109,86 sem juros",
    [("Branco","dw580e185a/images/bowl-de-servir-ruffle-white%20(2).png"),
     ("Shell Pink","dw72dec93d/images/Bowl-servir-Servir-ruffle-shellpink-3%2C8l1.png")],
    ["O Bowl de Servir Ruffle 3,8L Le Creuset combina design elegante com funcionalidade para valorizar qualquer mesa.",
     "Com bordas onduladas caracter&#237;sticas e capacidade generosa, &#233; perfeito para saladas, massas e pratos principais. Cer&#226;mica premium com acabamento esmaltado resist&#234;nte."],
    [("Material","Cer&#226;mica"),("Capacidade","3,8L"),
     ("Dimens&#245;es","34cm × 26,4cm × 11cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-octagon.html",
    "Bowl Octagon Le Creuset",
    "Bowl Octagon", "Cer&#226;mica · 12cm · Design octagonal",
    "R$ 199,00", "ou 2x de R$ 99,50 sem juros",
    [("Vermelho","dw3f9ce51d/images/bowl-octagon-vermelho-12cm%20(2).png")],
    ["O Bowl Octagon Le Creuset &#233; uma pe&#231;a cer&#226;mica essencial para quem aprecia design &#250;nico e versatilidade.",
     "A forma octagonal combina estilo e funcionalidade para servir ou preparar receitas. Superf&#237;cie esmaltada resist&#234;nte e f&#225;cil de limpar."],
    [("Material","Cer&#226;mica"),("Tamanho","12cm"),
     ("Dimens&#245;es","12cm × 12cm × 5cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","China"),("Garantia","10 anos")])

make_product("sopeira-heritage-600ml.html",
    "Sopeira Heritage 600ml Le Creuset",
    "Sopeira Heritage 600ml", "Cer&#226;mica · 600ml",
    "R$ 329,00", "ou 3x de R$ 109,67 sem juros",
    [("Azure","dwb8f660b1/images/sopeira-heritage-azure-600ml.png"),
     ("Branco","dw995ed52d/images/sopeira-heritage-white-600ml.png")],
    ["A Sopeira Heritage 600ml Le Creuset combina durabilidade e design sofisticado para o dia a dia e ocasi&#245;es especiais.",
     "A superf&#237;cie esmaltada facilita a remo&#231;&#227;o dos alimentos e torna a limpeza mais r&#225;pida. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidade","600ml"),
     ("Dimens&#245;es","11,8cm × 11,8cm × 9,4cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-redondo-kobe.html",
    "Bowl Redondo Kobe Le Creuset",
    "Bowl Redondo Kobe", "Cer&#226;mica · 3 tamanhos · Inspira&#231;&#227;o asi&#225;tica",
    "R$ 159,00 – R$ 209,00", "a partir de 2x de R$ 79,50 sem juros",
    [("Laranja","dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png"),
     ("Vermelho","dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png"),
     ("Branco","dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png")],
    ["A cole&#231;&#227;o Kobe se inspira na tradi&#231;&#227;o e funcionalidade da culin&#225;ria asi&#225;tica. Perfeito para servir acompanhamentos, pratos asi&#225;ticos como ramen e udon, ou sobremesas.",
     "A superf&#237;cie esmaltada facilita a limpeza e mant&#233;m a temperatura dos alimentos. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidades","150ml · 300ml · 600ml"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","China"),("Garantia","10 anos")])

make_product("noodle-bowl-kobe.html",
    "Noodle Bowl Kobe Le Creuset",
    "Noodle Bowl Kobe", "Cer&#226;mica · 19cm · Cole&#231;&#227;o Kobe",
    "R$ 223,30", "ou 3x de R$ 74,43 sem juros",
    [("Laranja","dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png"),
     ("Vermelho","dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png"),
     ("Branco","dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png")],
    ["O Noodle Bowl Kobe &#233; ideal para por&#231;&#245;es generosas de sopas, ensopados e, especialmente, pratos de macarr&#227;o asi&#225;tico.",
     "O design profundo e bordas levemente inclinadas facilitam o manuseio dos utens&#237;lios e a reten&#231;&#227;o de calor."],
    [("Material","Cer&#226;mica"),("Tamanho","19cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","China"),("Garantia","10 anos")],
    price_original="R$ 319,00")

make_product("multi-bowl-jardin.html",
    "Multi Bowl Jardin Le Creuset",
    "Multi Bowl Jardin", "Cer&#226;mica · 3 cores · Cole&#231;&#227;o Jardin",
    "R$ 433,30 – R$ 619,00", "a partir de 4x de R$ 108,33 sem juros",
    [("Shell Pink","dwe0c5f985/images/multi-bowl-jardin-3%2C6l-shell%20pink%20(2).png"),
     ("Camomille","dw3a5569e5/images/multi-bowl-jardin-3%2C6l-camomille.png"),
     ("Sea Salt","dw9053c99c/images/multi-bowl-jardin-3%2C6l-sea%20salt.png")],
    ["O Multi Bowl Jardin &#233; vers&#225;til para aperitivos, acompanhamentos e sobremesas com design funcional e cer&#226;mica premium.",
     "A superf&#237;cie esmaltada facilita a limpeza. Vai ao forno, microondas, freezer e lava-lou&#231;as. Cores suaves da cole&#231;&#227;o Jardin."],
    [("Material","Cer&#226;mica"),("Cole&#231;&#227;o","Jardin"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-redondo-san-francisco.html",
    "Bowl Redondo San Francisco Le Creuset",
    "Bowl Redondo San Francisco", "Cer&#226;mica · Minimalista · 2 tamanhos",
    "R$ 239,00 – R$ 449,00", "a partir de 2x de R$ 119,50 sem juros",
    [("Peche","dw125979d7/images/70157850997099-bowl-san-francisco-10.png"),
     ("Bleu Riviera","dw840afbd0/images/produto-lecreuset-bowl-san-francisco-peche.png")],
    ["Minimalista em cer&#226;mica premium, o Bowl Redondo San Francisco &#233; projetado para servir cereais, mingaus e sopas com elegancia.",
     "Superf&#237;cie esmaltada de f&#225;cil limpeza. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidades","770ml · 1,6L"),
     ("Dimens&#245;es","15cm × 15cm × 6,25cm"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")])

make_product("bowl-de-preparo-2l.html",
    "Bowl de Preparo 2L Le Creuset",
    "Bowl de Preparo 2L", "Cer&#226;mica · Com bico e al&#231;a",
    "R$ 300,30 – R$ 429,00", "a partir de 3x de R$ 100,10 sem juros",
    [("Vermelho","dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"),
     ("Laranja","dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"),
     ("Azure","dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"),
     ("Nectar","dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"),
     ("Shell Pink","dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png")],
    ["O Bowl de Preparo 2L Le Creuset oferece amplo espa&#231;o para mexer receitas com massa. A al&#231;a e o bico facilitam a transfer&#234;ncia de ingredientes.",
     "Finalizado com esmalte vibrante f&#225;cil de limpar, resist&#234;nte a lascas, arranhões e manchas. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidade","2L"),
     ("Dimens&#245;es","26,1cm × 18,3cm × 12,3cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bowl-jardin-320ml.html",
    "Bowl Jardin 320ml Le Creuset",
    "Bowl Jardin 320ml", "Cer&#226;mica · 320ml · Cole&#231;&#227;o Jardin",
    "R$ 139,30 – R$ 199,00", "a partir de 2x de R$ 69,65 sem juros",
    [("Camomille","dw25bfe4dd/images/bowl-jardim-320ml-camomille%20(2).png"),
     ("Sea Salt","dw25bfe4dd/images/bowl-jardim-320ml-camomille%20(2).png")],
    ["O Bowl Jardin 320ml Le Creuset &#233; ideal para sobremesas, acompanhamentos e snacks com o charme floral da cole&#231;&#227;o Jardin.",
     "Cer&#226;mica premium com superf&#237;cie esmaltada. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidade","320ml"),
     ("Cole&#231;&#227;o","Jardin"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")],
    sold_out=True)

make_product("bowl-coracao-650ml-bowls.html",
    "Bowl Coração 650ml Le Creuset",
    "Bowl Cora&#231;&#227;o 650ml", "Cer&#226;mica · 650ml · Formato cora&#231;&#227;o",
    "R$ 249,00", "Produto indispon&#237;vel",
    [("Vermelho","dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png")],
    ["O Bowl Cora&#231;&#227;o 650ml Le Creuset &#233; uma pe&#231;a especial para servir sobremesas e frutas com estilo.",
     "Formato de cora&#231;&#227;o em cer&#226;mica premium com acabamento esmaltado."],
    [("Material","Cer&#226;mica"),("Capacidade","650ml"),("Garantia","10 anos")],
    sold_out=True)

make_product("bowl-redondo-flora.html",
    "Bowl Redondo Flora Le Creuset",
    "Bowl Redondo Flora", "Cer&#226;mica · 550ml · Mauve Pink",
    "R$ 219,00 – R$ 229,00", "Produto indispon&#237;vel",
    [("Mauve Pink","dwe8cf48a4/images/bowl-redondo-flora-550ml-mauve-pink.png")],
    ["O Bowl Redondo Flora Le Creuset combina design floral delicado com funcionalidade premium.",
     "Cer&#226;mica com superf&#237;cie esmaltada resist&#234;nte na suave cor Mauve Pink."],
    [("Material","Cer&#226;mica"),("Capacidade","550ml"),
     ("Cor","Mauve Pink"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-4-bowls-redondos-16cm.html",
    "Set 4 Bowls Redondos 16cm Le Creuset",
    "Set 4 Bowls Redondos 16cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 729,00", "Produto indispon&#237;vel",
    [("Chambray","dwfd8cae96/images/produto-lecreuset-bowl-set-chambray.png")],
    ["O Set 4 Bowls Redondos 16cm Le Creuset &#233; o conjunto ideal para montar a mesa com estilo e uniformidade.",
     "Quatro bowls de cer&#226;mica premium na cor Chambray com acabamento esmaltado resist&#234;nte."],
    [("Material","Cer&#226;mica"),("Tamanho","16cm cada"),
     ("Quantidade","4 bowls"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)


# ── Collection page ───────────────────────────────────────────────────────────
print("\nCriando colecao-bowls.html...")

def sw(img_id, hexc, label, url, active=False):
    act = " active" if active else ""
    brd = "border:1.5px solid #ccc;" if hexc in ("#FFFFFF","#FDF5E6","#F4C2C2","#A8C5BB","#FFF8DC","#F5E090","#FFCBA4","#F0EDE8") else "border:1.5px solid transparent;"
    return f'<span class="swatch{act}" style="background:{hexc};{brd}" onclick="swatchClick(event,this,\'{img_id}\',\'{url}\')" title="{label}"></span>'

def card(img_id, href, img_src, alt, name, sub, price, swatches, sold_out=False, promo=False):
    badge = ""
    if sold_out:
        badge = '<div class="oos-badge">ESGOTADO</div>'
    elif promo:
        badge = '<div class="promo-badge">OFERTA</div>'
    return f"""    <div class="product-card">
      <a href="{href}">
        <div class="product-card-img">
          <img id="{img_id}" src="{img_src}" alt="{alt}"/>
          <div class="product-wishlist">{WISH}</div>
          {badge}
        </div>
      </a>
      <a href="{href}">
        <div class="product-card-name">{name}</div>
        <div class="product-card-sub">{sub}</div>
        <div class="product-card-price">{price}</div>
      </a>
      <div class="card-swatches">{swatches}</div>
    </div>"""

C = CDN
cards = []

cards.append(card("i_van","bowl-redondo-vancouver.html",
    C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q,"Bowl Redondo Vancouver",
    "Bowl Redondo Vancouver","Cer&#226;mica · 11cm · 16cm · 24cm","A partir de R$ 139,00",
    sw("i_van","#8B9467","Artichaut",C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q,True)+
    sw("i_van","#FE5000","Laranja",C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q)+
    sw("i_van","#C41E3A","Vermelho",C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q)+
    sw("i_van","#0066B2","Bleu Riviera",C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q)+
    sw("i_van","#007FFF","Azure",C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q)+
    sw("i_van","#F4C2C2","Shell Pink",C+"dwc3e0652f/images/produto-lecreuset-bowl-16cm-artichaut1.png"+Q)))

cards.append(card("i_bred","bowl-redondo.html",
    C+"dw23b665b7/images/91005302060000.jpg"+Q,"Bowl Redondo",
    "Bowl Redondo","Cer&#226;mica · 19cm · 24cm","A partir de R$ 399,00",
    sw("i_bred","#C41E3A","Vermelho",C+"dw23b665b7/images/91005302060000.jpg"+Q,True)+
    sw("i_bred","#FE5000","Laranja",C+"dw23b665b7/images/91005302060000.jpg"+Q)+
    sw("i_bred","#FFFFFF","Branco",C+"dw23b665b7/images/91005302060000.jpg"+Q)))

cards.append(card("i_inox","bowl-inox-com-tampa-de-vidro.html",
    C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,"Bowl Inox com Tampa de Vidro",
    "Bowl Inox com Tampa de Vidro","A&#231;o Inox · 19cm · 23cm · 27cm","A partir de R$ 399,00",
    sw("i_inox","#B0B0B0","Inox",C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,True)))

cards.append(card("i_holly","multi-bowl-holly.html",
    C+"dw49ca2d17/images/mult-bowl-holly-thyme.png"+Q,"Multi Bowl Holly",
    "Multi Bowl Holly","Cer&#226;mica · 25cm · 4 cores","R$ 619,00",
    sw("i_holly","#6D7C5E","Thyme",C+"dw49ca2d17/images/mult-bowl-holly-thyme.png"+Q,True)+
    sw("i_holly","#C41E3A","Vermelho",C+"dw1a1a95a2/images/multi-bowl-holly-vermelho2.png"+Q)+
    sw("i_holly","#FFFFFF","Branco",C+"dw821802b5/images/multi-bowl-holly-branco.png"+Q)+
    sw("i_holly","#FFF8DC","Nata",C+"dw6777c187/images/Nata-lecreuset-2025-2.png"+Q)))

cards.append(card("i_ruffle","bowl-de-servir-ruffle.html",
    C+"dw580e185a/images/bowl-de-servir-ruffle-white%20(2).png"+Q,"Bowl de Servir Ruffle 3,8L",
    "Bowl de Servir Ruffle 3,8L","Cer&#226;mica · 34cm · 2 cores","R$ 769,00",
    sw("i_ruffle","#FFFFFF","Branco",C+"dw580e185a/images/bowl-de-servir-ruffle-white%20(2).png"+Q,True)+
    sw("i_ruffle","#F4C2C2","Shell Pink",C+"dw72dec93d/images/Bowl-servir-Servir-ruffle-shellpink-3%2C8l1.png"+Q)))

cards.append(card("i_oct","bowl-octagon.html",
    C+"dw3f9ce51d/images/bowl-octagon-vermelho-12cm%20(2).png"+Q,"Bowl Octagon",
    "Bowl Octagon","Cer&#226;mica · 12cm · Design octagonal","R$ 199,00",
    sw("i_oct","#C41E3A","Vermelho",C+"dw3f9ce51d/images/bowl-octagon-vermelho-12cm%20(2).png"+Q,True)))

cards.append(card("i_sop","sopeira-heritage-600ml.html",
    C+"dwb8f660b1/images/sopeira-heritage-azure-600ml.png"+Q,"Sopeira Heritage 600ml",
    "Sopeira Heritage 600ml","Cer&#226;mica · 600ml · 2 cores","R$ 329,00",
    sw("i_sop","#007FFF","Azure",C+"dwb8f660b1/images/sopeira-heritage-azure-600ml.png"+Q,True)+
    sw("i_sop","#FFFFFF","Branco",C+"dw995ed52d/images/sopeira-heritage-white-600ml.png"+Q)))

cards.append(card("i_tap","set-3-mini-pratos-de-tapas.html",
    C+"dwb489c4a7/images/prato-triangulo-chambray.png"+Q,"Set 3 Mini Pratos de Tapas",
    "Set 3 Mini Pratos de Tapas","Cer&#226;mica · Chambray · 3 pe&#231;as","R$ 314,30",
    sw("i_tap","#7BA3C8","Chambray",C+"dwb489c4a7/images/prato-triangulo-chambray.png"+Q,True)))

cards.append(card("i_pet","set-5-mini-pratos-petalas.html",
    C+"dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png"+Q,"Set 5 Mini Pratos Pétalas",
    "Set 5 Mini Pratos P&#233;talas","Cer&#226;mica · Bluebell Purple · 5 pe&#231;as","R$ 659,00",
    sw("i_pet","#7B68C8","Bluebell Purple",C+"dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png"+Q,True)))

cards.append(card("i_bwp","set-bowl-prato.html",
    C+"dw29ba298c/images/Set%20Bowl%20+%20Prato.png"+Q,"Set Bowl & Prato",
    "Set Bowl &amp; Prato","Cer&#226;mica · Mauve Pink · 2 pe&#231;as","R$ 409,00",
    sw("i_bwp","#CF9BAE","Mauve Pink",C+"dw29ba298c/images/Set%20Bowl%20+%20Prato.png"+Q,True)))

cards.append(card("i_kobe","bowl-redondo-kobe.html",
    C+"dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png"+Q,"Bowl Redondo Kobe",
    "Bowl Redondo Kobe","Cer&#226;mica · 3 tamanhos · Cole&#231;&#227;o Kobe","A partir de R$ 159,00",
    sw("i_kobe","#FE5000","Laranja",C+"dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png"+Q,True)+
    sw("i_kobe","#C41E3A","Vermelho",C+"dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png"+Q)+
    sw("i_kobe","#FFFFFF","Branco",C+"dw924fb8ee/images/tardes%20de%20verao/bowl-redondo-kobe%20(5).png"+Q)))

cards.append(card("i_nood","noodle-bowl-kobe.html",
    C+"dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png"+Q,"Noodle Bowl Kobe",
    "Noodle Bowl Kobe","Cer&#226;mica · 19cm · Cole&#231;&#227;o Kobe","R$ 223,30",
    sw("i_nood","#FE5000","Laranja",C+"dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png"+Q,True)+
    sw("i_nood","#C41E3A","Vermelho",C+"dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png"+Q)+
    sw("i_nood","#FFFFFF","Branco",C+"dwfd2bf3e6/images/tardes%20de%20verao/1noodle-bowl-kobe-19cm-laranja.png"+Q),
    promo=True))

cards.append(card("i_jard","multi-bowl-jardin.html",
    C+"dwe97c55a6/images/multibowl-jardin.png"+Q,"Multi Bowl Jardin",
    "Multi Bowl Jardin","Cer&#226;mica · 3 cores · Cole&#231;&#227;o Jardin","A partir de R$ 433,30",
    sw("i_jard","#F4C2C2","Shell Pink",C+"dwe0c5f985/images/multi-bowl-jardin-3%2C6l-shell%20pink%20(2).png"+Q,True)+
    sw("i_jard","#F5E090","Camomille",C+"dw3a5569e5/images/multi-bowl-jardin-3%2C6l-camomille.png"+Q)+
    sw("i_jard","#A8C5BB","Sea Salt",C+"dw9053c99c/images/multi-bowl-jardin-3%2C6l-sea%20salt.png"+Q)))

cards.append(card("i_sf","bowl-redondo-san-francisco.html",
    C+"dw125979d7/images/70157850997099-bowl-san-francisco-10.png"+Q,"Bowl Redondo San Francisco",
    "Bowl Redondo San Francisco","Cer&#226;mica · 2 tamanhos","A partir de R$ 239,00",
    sw("i_sf","#FFCBA4","Peche",C+"dw125979d7/images/70157850997099-bowl-san-francisco-10.png"+Q,True)+
    sw("i_sf","#0066B2","Bleu Riviera",C+"dw840afbd0/images/produto-lecreuset-bowl-san-francisco-peche.png"+Q)))

cards.append(card("i_prep","bowl-de-preparo-2l.html",
    C+"dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"+Q,"Bowl de Preparo 2L",
    "Bowl de Preparo 2L","Cer&#226;mica · 2L · Com bico e al&#231;a","A partir de R$ 300,30",
    sw("i_prep","#C41E3A","Vermelho",C+"dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"+Q,True)+
    sw("i_prep","#FE5000","Laranja",C+"dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"+Q)+
    sw("i_prep","#007FFF","Azure",C+"dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"+Q)+
    sw("i_prep","#F4A020","Nectar",C+"dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"+Q)+
    sw("i_prep","#F4C2C2","Shell Pink",C+"dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png"+Q)))

cards.append(card("i_jardp","bowl-jardin-320ml.html",
    C+"dw25bfe4dd/images/bowl-jardim-320ml-camomille%20(2).png"+Q,"Bowl Jardin 320ml",
    "Bowl Jardin 320ml","Cer&#226;mica · 320ml · Cole&#231;&#227;o Jardin","R$ 139,30",
    sw("i_jardp","#F5E090","Camomille",C+"dw25bfe4dd/images/bowl-jardim-320ml-camomille%20(2).png"+Q,True)+
    sw("i_jardp","#A8C5BB","Sea Salt",C+"dw25bfe4dd/images/bowl-jardim-320ml-camomille%20(2).png"+Q),
    sold_out=True))

cards.append(card("i_corac","bowl-coracao-650ml-bowls.html",
    C+"dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png"+Q,"Bowl Coração 650ml",
    "Bowl Cora&#231;&#227;o 650ml","Cer&#226;mica · 650ml · Formato cora&#231;&#227;o","R$ 249,00",
    sw("i_corac","#C41E3A","Vermelho",C+"dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png"+Q,True),
    sold_out=True))

cards.append(card("i_flora","bowl-redondo-flora.html",
    C+"dwe8cf48a4/images/bowl-redondo-flora-550ml-mauve-pink.png"+Q,"Bowl Redondo Flora",
    "Bowl Redondo Flora","Cer&#226;mica · 550ml · Mauve Pink","R$ 219,00",
    sw("i_flora","#CF9BAE","Mauve Pink",C+"dwe8cf48a4/images/bowl-redondo-flora-550ml-mauve-pink.png"+Q,True),
    sold_out=True))

cards.append(card("i_set4","set-4-bowls-redondos-16cm.html",
    C+"dwfd8cae96/images/produto-lecreuset-bowl-set-chambray.png"+Q,"Set 4 Bowls Redondos 16cm",
    "Set 4 Bowls Redondos 16cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 729,00",
    sw("i_set4","#7BA3C8","Chambray",C+"dwfd8cae96/images/produto-lecreuset-bowl-set-chambray.png"+Q,True),
    sold_out=True))

N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Bowls | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
  <style>*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:'Nunito Sans',sans-serif;color:#000;background:#fff;}}
    a{{text-decoration:none;color:inherit;}}
    .top-bar{{background:#1a1a1a;color:#fff;font-size:12px;text-align:center;padding:8px 16px;}}
    header{{background:#fff;border-bottom:1px solid #e5e5e5;position:sticky;top:0;z-index:100;}}
    .header-inner{{max-width:1400px;margin:0 auto;padding:0 24px;display:flex;align-items:center;height:64px;gap:24px;}}
    .logo{{font-size:22px;font-weight:800;letter-spacing:-1px;white-space:nowrap;flex-shrink:0;}}
    .logo span{{color:#c8102e;}}
    nav{{flex:1;}}
    .nav-list{{display:flex;list-style:none;align-items:center;}}
    .nav-list>li{{position:relative;}}
    .nav-list>li>a{{display:block;padding:22px 14px;font-size:13px;font-weight:600;color:#000;white-space:nowrap;border-bottom:2px solid transparent;transition:border-color 0.2s;}}
    .nav-list>li>a:hover{{border-bottom-color:#000;}}
    .nav-list>li.highlight>a{{color:#c8102e;}}
    .nav-list>li.blue>a{{color:#2563ab;}}
    .mega-menu{{display:none;position:fixed;left:0;right:0;top:64px;background:#fff;border-top:2px solid #e5e5e5;box-shadow:0 8px 32px rgba(0,0,0,0.13);z-index:200;padding:28px 0 24px;}}
    .nav-list>li:hover .mega-menu{{display:block;}}
    .mega-inner{{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:170px 150px 170px 170px 170px;gap:0 20px;align-items:start;}}
    .mega-col-title{{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#000;margin-bottom:14px;padding-bottom:6px;border-bottom:1px solid #e5e5e5;}}
    .mega-col a{{display:block;font-size:13px;color:#444;padding:4px 0;}}
    .mega-col a:hover{{color:#c8102e;}}
    .header-icons{{display:flex;align-items:center;gap:16px;flex-shrink:0;}}
    .header-icons a{{font-size:12px;font-weight:600;display:flex;flex-direction:column;align-items:center;gap:2px;color:#000;}}
    .header-icons svg{{width:22px;height:22px;}}
    .search-box{{display:flex;align-items:center;border:1px solid #ccc;border-radius:4px;overflow:hidden;height:36px;}}
    .search-box input{{border:none;outline:none;padding:0 12px;font-size:13px;width:180px;font-family:inherit;}}
    .search-box button{{background:#000;border:none;cursor:pointer;padding:0 12px;height:100%;display:flex;align-items:center;}}
    .search-box button svg{{fill:#fff;width:16px;height:16px;}}
    .cat-banner-wrap{{border-bottom:1px solid #e0e0e0;overflow:hidden;}}
    .cat-banner{{max-width:1400px;margin:0 auto;display:grid;grid-template-columns:2fr 3fr;min-height:300px;}}
    .cat-banner-left{{position:relative;padding:32px 48px 40px 32px;display:flex;flex-direction:column;justify-content:flex-end;background:#f5f0ee;overflow:hidden;}}
    .cat-banner-left::before{{content:'';position:absolute;inset:0;background-image:url('{BANNER}');background-size:cover;background-position:center;opacity:0.12;}}
    .cat-banner-left-content{{position:relative;z-index:1;}}
    .cat-banner-crumb{{font-size:12px;color:#888;display:flex;gap:5px;align-items:center;margin-bottom:auto;padding-bottom:100px;}}
    .cat-banner-crumb a{{color:#888;}} .cat-banner-crumb a:hover{{color:#000;text-decoration:underline;}}
    .cat-banner-title{{font-size:32px;font-weight:300;color:#000;margin-bottom:12px;letter-spacing:-0.5px;}}
    .cat-banner-desc{{font-size:13px;color:#444;line-height:1.6;max-width:300px;}}
    .cat-banner-right{{overflow:hidden;}}
    .cat-banner-right img{{width:100%;height:100%;object-fit:cover;object-position:center;display:block;}}
    .shop-layout{{max-width:1400px;margin:0 auto;padding:24px 24px 80px;display:grid;grid-template-columns:220px 1fr;gap:40px;align-items:start;}}
    .sidebar{{position:sticky;top:80px;}}
    .filter-section{{border-bottom:1px solid #e5e5e5;}}
    .filter-header{{display:flex;justify-content:space-between;align-items:center;padding:14px 0;cursor:pointer;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;user-select:none;}}
    .filter-header svg{{width:14px;height:14px;transition:transform 0.2s;}}
    .filter-header.open svg{{transform:rotate(180deg);}}
    .filter-body{{padding-bottom:12px;display:none;}}
    .filter-body.open{{display:block;}}
    .filter-option{{display:flex;align-items:center;gap:8px;padding:5px 0;font-size:13px;color:#444;cursor:pointer;}}
    .filter-option input{{width:14px;height:14px;cursor:pointer;accent-color:#000;}}
    .filter-clear{{font-size:11px;font-weight:700;color:#000;text-transform:uppercase;cursor:pointer;border:none;background:none;padding:0;display:flex;align-items:center;gap:4px;}}
    .results-bar{{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;}}
    .results-count{{font-size:13px;color:#888;}}
    .sort-select{{font-size:13px;border:1px solid #ccc;padding:6px 12px;font-family:inherit;cursor:pointer;}}
    .product-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;}}
    .product-card{{position:relative;}}
    .product-card-img{{position:relative;overflow:hidden;background:#fff;aspect-ratio:1;margin-bottom:10px;border:1px solid #f0f0f0;}}
    .product-card-img img{{width:100%;height:100%;object-fit:contain;padding:16px;transition:transform 0.4s ease;}}
    .product-card-img:hover img{{transform:scale(1.06);}}
    .product-wishlist{{position:absolute;top:8px;right:8px;width:30px;height:30px;background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,0.1);}}
    .product-wishlist svg{{width:15px;height:15px;}}
    .oos-badge{{position:absolute;bottom:8px;left:8px;background:#666;color:#fff;font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;border-radius:2px;}}
    .promo-badge{{position:absolute;bottom:8px;left:8px;background:#c8102e;color:#fff;font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;border-radius:2px;}}
    .product-card-name{{font-size:13px;font-weight:700;margin-bottom:3px;line-height:1.3;}}
    .product-card-sub{{font-size:11px;color:#888;margin-bottom:5px;}}
    .product-card-price{{font-size:14px;font-weight:800;}}
    .card-swatches{{display:flex;gap:5px;margin-top:7px;flex-wrap:wrap;}}
    .swatch{{width:18px;height:18px;border-radius:50%;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;display:inline-block;}}
    .swatch:hover{{transform:scale(1.15);}}
    .swatch.active{{box-shadow:0 0 0 2px #fff,0 0 0 3.5px #000;}}
    footer{{background:#111;color:#fff;padding:60px 24px 30px;}}
    .footer-inner{{max-width:1400px;margin:0 auto;}}
    .footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}}
    .footer-brand .logo{{font-size:20px;margin-bottom:16px;display:block;}}
    .footer-brand p{{font-size:13px;color:#aaa;line-height:1.7;max-width:280px;margin-bottom:20px;}}
    .footer-social{{display:flex;gap:12px;}}
    .social-btn{{width:36px;height:36px;border:1px solid #444;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;}}
    .footer-col h4{{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:16px;}}
    .footer-col ul{{list-style:none;}}
    .footer-col ul li{{margin-bottom:10px;}}
    .footer-col ul li a{{font-size:13px;color:#aaa;}}
    .footer-col ul li a:hover{{color:#fff;}}
    .footer-bottom{{border-top:1px solid #333;padding-top:24px;display:flex;justify-content:space-between;align-items:center;}}
    .footer-bottom p{{font-size:12px;color:#666;}}
    .payment-icons{{display:flex;gap:8px;}}
    .payment-icon{{background:#222;border:1px solid #444;border-radius:4px;padding:4px 8px;font-size:10px;font-weight:700;color:#aaa;}}
  </style>
</head>
<body>
<div class="top-bar">&#128666; Frete Gr&#225;tis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>
{NAV}

<div class="cat-banner-wrap">
  <div class="cat-banner">
    <div class="cat-banner-left">
      <div class="cat-banner-left-content">
        <div class="cat-banner-crumb">
          <a href="index.html">In&#237;cio</a><span>/</span>
          <a href="#">Preparar &amp; Servir</a><span>/</span>
          <span>Bowls</span>
        </div>
        <h1 class="cat-banner-title">Bowls</h1>
        <p class="cat-banner-desc">Os bowls Le Creuset, em cer&#226;mica premium e a&#231;o inox, combinam funcionalidade e design ic&#244;nico para preparar e servir com muito estilo.</p>
      </div>
    </div>
    <div class="cat-banner-right">
      <img src="{BANNER}" alt="Bowls Le Creuset"/>
    </div>
  </div>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Tipo
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Bowls Redondos</label>
        <label class="filter-option"><input type="checkbox"> Multi Bowls</label>
        <label class="filter-option"><input type="checkbox"> Bowls de Preparo</label>
        <label class="filter-option"><input type="checkbox"> Noodle Bowls</label>
        <label class="filter-option"><input type="checkbox"> Sopeiras</label>
        <label class="filter-option"><input type="checkbox"> Sets</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Material
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Cer&#226;mica</label>
        <label class="filter-option"><input type="checkbox"> A&#231;o Inox</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Pre&#231;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> At&#233; R$ 200</label>
        <label class="filter-option"><input type="checkbox"> R$ 200 &#8211; R$ 400</label>
        <label class="filter-option"><input type="checkbox"> R$ 400 &#8211; R$ 700</label>
        <label class="filter-option"><input type="checkbox"> + R$ 700</label>
      </div>
    </div>
  </aside>

  <div>
    <div class="results-bar">
      <button class="filter-clear">LIMPAR FILTROS <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="9 18 15 12 9 6"/></svg></button>
      <span class="results-count">{N} produtos</span>
      <select class="sort-select"><option>Mais Populares</option><option>Menor Pre&#231;o</option><option>Maior Pre&#231;o</option></select>
    </div>
    <div class="product-grid">
{"".join(cards)}
    </div>
  </div>
</div>

{FOOT}
<script>
function toggleFilter(h){{
  h.classList.toggle('open');
  h.nextElementSibling.classList.toggle('open');
}}
function swatchClick(e,el,imgId,src){{
  e.preventDefault();e.stopPropagation();
  el.parentElement.querySelectorAll('.swatch').forEach(x=>x.classList.remove('active'));
  el.classList.add('active');
  document.getElementById(imgId).src=src;
}}
</script>
</body></html>"""

with open(os.path.join(BASE, "colecao-bowls.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"  Cole\u00e7\u00e3o: colecao-bowls.html ({N} produtos)")
print("\nTudo pronto!")
