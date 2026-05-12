#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE   = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN    = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q      = "?sw=650&sh=650&sm=fit"
BANNER = "https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dw641e9c73/category/cat_banners/categoria-site-prato1.png"

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
    "Bluebell Purple":"#7B68C8","Cool Mint":"#A8D5C2","Preto e Branco":"#333333",
    "Inox":"#B0B0B0",
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
          </div>
          <div class="mega-col"><div class="mega-col-title">Assar</div>
            <a href="colecao-assadeiras-travessas.html">Assadeiras e Travessas</a>
            <a href="colecao-formas-metal-bakeware.html">Formas Metal Bakeware</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Preparar &amp; Servir</div>
            <a href="colecao-bowls.html">Bowls</a>
            <a href="colecao-pratos.html">Pratos</a>
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

LIGHT = {"#FFFFFF","#FDF5E6","#F4C2C2","#A8C5BB","#FFF8DC","#F5E090","#FFCBA4","#F0EDE8","#A8D5C2"}

def make_product(filename, title, name, sub, price, install, colors_imgs, desc, specs,
                 sold_out=False, price_original=None):
    first_c, first_img = colors_imgs[0]
    swatches = ""
    for i, (cname, cimg) in enumerate(colors_imgs):
        url = CDN + cimg + Q
        hexc = COLOR_HEX.get(cname, "#888")
        bord = "border:2px solid #ccc;" if hexc in LIGHT else "border:2px solid transparent;"
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
  <a href="colecao-pratos.html">Pratos</a><span>/</span>
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

make_product("prato-raso-vancouver.html",
    "Prato Raso Vancouver Le Creuset",
    "Prato Raso Vancouver", "Cer&#226;mica · 17cm · 22cm · 27cm",
    "R$ 199,00 – R$ 239,00", "a partir de 2x de R$ 99,50 sem juros",
    [("Vermelho","dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"),
     ("Laranja","dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"),
     ("Branco","dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"),
     ("Shell Pink","dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"),
     ("Azure","dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"),
     ("Meringue","dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png")],
    ["O Prato Raso Vancouver Le Creuset &#233; a escolha perfeita para o dia a dia e ocasi&#245;es especiais.",
     "Cer&#226;mica premium com superf&#237;cie esmaltada resist&#234;nte a lascas e manchas. Vai ao microondas, forno, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","17cm · 22cm · 27cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-fundo-22cm.html",
    "Prato Fundo 22cm Le Creuset",
    "Prato Fundo 22cm", "Cer&#226;mica · 22cm",
    "R$ 219,00", "ou 2x de R$ 109,50 sem juros",
    [("Vermelho","dwa640170f/images/produto-lecreuset-prato-fundo-vermelho.png"),
     ("Marseille","dw94bb8693/images/produto-lecreuset-prato-fundo-marseille%20(2).png"),
     ("Bamboo","dw2a6ac032/images/produto-lecreuset-prato-fundo-bamboo.png"),
     ("Artichaut","dw11e3da05/images/produto-lecreuset-prato-fundo-artichaut.png")],
    ["O Prato Fundo 22cm Le Creuset &#233; perfeito para saborear uma variedade de massas, saladas e entradas.",
     "Cer&#226;mica premium com esmalte que facilita a remo&#231;&#227;o dos alimentos e &#233; apto para lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","22cm"),("Altura","4cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-raso-san-francisco.html",
    "Prato Raso San Francisco Le Creuset",
    "Prato Raso San Francisco", "Cer&#226;mica · 22cm · 27cm",
    "R$ 219,00 – R$ 239,00", "a partir de 2x de R$ 109,50 sem juros",
    [("Peche","dw125979d7/images/produto-lecreuset-prato-set-22cm-preche.png"),
     ("Bleu Riviera","dw125979d7/images/produto-lecreuset-prato-set-22cm-preche.png")],
    ["O Prato Raso San Francisco Le Creuset &#233; minimalista em cer&#226;mica premium, vers&#225;til para servir refeições, aperitivos, p&#227;o, saladas ou sobremesas.",
     "Design com resist&#234;ncia a lascas e arranhões. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","22cm · 27cm"),
     ("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")])

make_product("prato-fundo-san-francisco.html",
    "Prato Fundo San Francisco Le Creuset",
    "Prato Fundo San Francisco", "Cer&#226;mica · Cole&#231;&#227;o San Francisco",
    "R$ 219,00", "ou 2x de R$ 109,50 sem juros",
    [("Peche","dw125979d7/images/produto-lecreuset-prato-fundo-san-francisco-peche.png"),
     ("Bleu Riviera","dw125979d7/images/produto-lecreuset-prato-fundo-san-francisco-peche.png")],
    ["O Prato Fundo San Francisco Le Creuset &#233; ideal para massas, saladas e pratos com molhos.",
     "Cer&#226;mica premium com esmalte que facilita a limpeza. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")])

make_product("prato-para-pao-16cm.html",
    "Prato para Pão 16cm Le Creuset",
    "Prato para P&#227;o 16cm", "Cer&#226;mica · 16cm",
    "R$ 109,00", "ou 2x de R$ 54,50 sem juros",
    [("Azure","dwe854514b/images/pires-16cm-azure.png"),
     ("Nectar","dw0e83efa8/images/pires-16cm-nectar.png"),
     ("Caribe","dwce23871b/images/pires-16cm-caribe.png"),
     ("Shell Pink","dwff1777f9/images/pires-16cm-shellpink.png")],
    ["O Prato para P&#227;o 16cm Le Creuset &#233; o companheiro ideal para a sua caneca favorita.",
     "Combina durabilidade, design elegante e praticidade para o uso di&#225;rio. Cer&#226;mica premium com superf&#237;cie esmaltada."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","16cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-raso-sphere-holly.html",
    "Prato Raso Sphere Holly 19cm Le Creuset",
    "Prato Raso Sphere Holly 19cm", "Cer&#226;mica · Cole&#231;&#227;o Holly",
    "R$ 259,00", "ou 2x de R$ 129,50 sem juros",
    [("Branco","dw1e1caa0d/images/prato-raso-sphere-holly-branco.png"),
     ("Thyme","dw921fc859/images/prato-raso-sphere-holly-thyme.png"),
     ("Vermelho","dwf81d34c7/images/prato-raso-sphere-holly-vermelho.png")],
    ["O Prato Raso Sphere Holly Le Creuset celebra a magia das festas &#224; mesa, trazendo elega&#234;ncia e charme a cada refei&#231;&#227;o.",
     "Feito em cer&#226;mica premium com acabamento esmaltado vibrante. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","19cm"),
     ("Cole&#231;&#227;o","Sphere Holly"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("bandeja-estrela-de-servir.html",
    "Bandeja Estrela de Servir Le Creuset",
    "Bandeja Estrela de Servir", "Cer&#226;mica · 36cm · Design estrela",
    "R$ 619,00", "ou 6x de R$ 103,17 sem juros",
    [("Vermelho","dw39d4b309/images/bandeja-estrela-de-servir-vermelho-36cm.png")],
    ["A Bandeja Estrela de Servir Le Creuset traz um charme especial para cada celebra&#231;&#227;o, combinando elega&#234;ncia e praticidade.",
     "Feita em cer&#226;mica premium com design em forma de estrela e acabamento esmaltado. Ideal para servir pratos e confeitos."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","36cm × 34cm × 3,2cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-fundo-ruffle-21cm.html",
    "Prato Fundo Ruffle 21cm Le Creuset",
    "Prato Fundo Ruffle 21cm", "Cer&#226;mica · 21cm · 1,3L",
    "R$ 619,00", "ou 6x de R$ 103,17 sem juros",
    [("Branco","dwdf2048f1/images/prato-fundo-ruffle-21cm-branco1%20(2).png")],
    ["O Prato Fundo Ruffle 21cm Le Creuset combina bordas onduladas elegantes com funcionalidade premium para o dia a dia.",
     "A superf&#237;cie esmaltada facilita a limpeza e prev&#234;ne manchas. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","21cm"),
     ("Capacidade","1,3L"),("Altura","10,3cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-de-servir-ruffle-36cm.html",
    "Prato de Servir Ruffle 36cm Le Creuset",
    "Prato de Servir Ruffle 36cm", "Cer&#226;mica · 36cm · 2 cores",
    "R$ 739,00", "ou 7x de R$ 105,57 sem juros",
    [("Shell Pink","dw85245aba/images/prato-de-servir-ruffle-36cm-shell-pink1.png"),
     ("Branco","dw1d438b2f/images/prato-de-servir-ruffle-36cm-branco1%20(2).png")],
    ["O Prato de Servir Ruffle 36cm Le Creuset apresenta bordas delicadamente onduladas que adicionam charme a qualquer mesa.",
     "Projetado para apresentar entradas, pratos principais e sobremesas com sofistica&#231;&#227;o. Cer&#226;mica premium apta para lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanho","36cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-fundo-kobe.html",
    "Prato Fundo Kobe Le Creuset",
    "Prato Fundo Kobe", "Cer&#226;mica · 17cm e 22cm · Cole&#231;&#227;o Kobe",
    "R$ 229,00 – R$ 269,00", "a partir de 2x de R$ 114,50 sem juros",
    [("Laranja","dw7c5c286c/images/tardes%20de%20verao/prato-fundo-kobe-22cm-laranja.png"),
     ("Vermelho","dwca54c05d/images/tardes%20de%20verao/prato-fundo-kobe-22cm-vermelho.png"),
     ("Branco","dw45f78070/images/tardes%20de%20verao/prato-fundo-kobe-22cm-white.png")],
    ["O Prato Fundo Kobe se inspira na tradi&#231;&#227;o culin&#225;ria asi&#225;tica, perfeito para ramen, udon e sobá, ou como prato principal.",
     "Cer&#226;mica premium com superf&#237;cie esmaltada de f&#225;cil limpeza. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","17cm · 22cm"),
     ("Cole&#231;&#227;o","Kobe"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","China"),("Garantia","10 anos")])

make_product("bandeja-de-servir-oval-jardin.html",
    "Bandeja de Servir Oval Jardin Le Creuset",
    "Bandeja de Servir Oval Jardin", "Cer&#226;mica · 36cm · Cole&#231;&#227;o Jardin",
    "R$ 370,30", "ou 3x de R$ 123,43 sem juros",
    [("Shell Pink","dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"),
     ("Camomille","dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"),
     ("Sea Salt","dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"),
     ("Meringue","dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png")],
    ["A Bandeja de Servir Oval Jardin Le Creuset combina a delic&#226;deza das flores com o charme at&#234;mporal de uma casa no campo.",
     "Com padr&#245;es florais de tulipas e narcisos, &#233; perfeita para apresentar entradas, petiscos e sobremesas. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanho","36cm"),
     ("Cole&#231;&#227;o","Jardin"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")],
    price_original="R$ 529,00")

make_product("prato-raso-jardin-22cm.html",
    "Prato Raso Jardin 22cm Le Creuset",
    "Prato Raso Jardin 22cm", "Cer&#226;mica · Cole&#231;&#227;o Jardin",
    "R$ 167,30 – R$ 239,00", "a partir de 2x de R$ 83,65 sem juros",
    [("Camomille","dwd6edfa02/images/prato-raso-jardin-22cm-camomille.png"),
     ("Shell Pink","dwd64b3fe2/images/prato-raso-jardin-22cm-shell%20pink.png"),
     ("Meringue","dwabe4156a/images/prato-raso-jardin-22cm-meringue.png")],
    ["O Prato Raso Jardin 22cm Le Creuset transforma qualquer ocasi&#227;o, trazendo a tranquilidade e diversidade de um jardim florido para a sua mesa.",
     "Padr&#245;es florais delicados em cer&#226;mica premium com acabamento esmaltado. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","22cm"),
     ("Cole&#231;&#227;o","Jardin"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")])

make_product("set-jantar-vancouver.html",
    "Set Jantar Vancouver Le Creuset",
    "Set Jantar Vancouver", "Cer&#226;mica · 16 pe&#231;as · Serve 4 pessoas",
    "R$ 3.089,00", "ou 10x de R$ 308,90 sem juros",
    [("Vermelho","dw56fcfc5d/images/kit-jantar-vermelho.png"),
     ("Branco","dw279f2810/images/kit-jantar-branco.png")],
    ["O Set Jantar Vancouver Le Creuset &#233; a combina&#231;&#227;o perfeita para montar uma mesa completa para 4 pessoas.",
     "Inclui: 4 Pratos Rasos 27cm, 4 Pratos Rasos 22cm, 4 Bowls Redondos 16cm e 4 Can&#233;cas Seattle 400ml.",
     "Cer&#226;mica premium com esmalte resist&#234;nte a lascas, arranhões e manchas. Apto para microondas e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Cont&#233;m","16 pe&#231;as"),
     ("Serve","4 pessoas"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-flor.html",
    "Prato Flor Le Creuset",
    "Prato Flor", "Cer&#226;mica · 14cm e 23cm · Bluebell Purple",
    "R$ 199,00 – R$ 269,00", "a partir de 2x de R$ 99,50 sem juros",
    [("Bluebell Purple","dw408ec32f/images/Prato%20Flor%2014Cm.png")],
    ["O Prato Flor Le Creuset &#233; uma pe&#231;a &#250;nica com design floral em cer&#226;mica premium.",
     "A superf&#237;cie esmaltada facilita a limpeza e mant&#233;m a temperatura dos alimentos. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","14cm · 23cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("set-2-pratos-flower-23cm.html",
    "Set 2 Pratos Flower 23cm Le Creuset",
    "Set 2 Pratos Flower 23cm", "Cer&#226;mica · Cool Mint · 2 pe&#231;as",
    "R$ 549,00", "ou 5x de R$ 109,80 sem juros",
    [("Cool Mint","dw5dca48b0/images/Flower-coolmint-fotos-primavera.png")],
    ["O Set 2 Pratos Flower 23cm Le Creuset oferece duas pe&#231;as de cer&#226;mica premium com design que embeleza cada refei&#231;&#227;o.",
     "Perfeito para refeições com presen&#231;a e elega&#234;ncia. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","23cm cada"),
     ("Quantidade","2 pratos"),("Cor","Cool Mint"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("prato-oval-raso-flora.html",
    "Prato Oval Raso Flora Le Creuset",
    "Prato Oval Raso Flora", "Cer&#226;mica · 19cm e 24cm · Mauve Pink",
    "R$ 209,00 – R$ 269,00", "a partir de 2x de R$ 104,50 sem juros",
    [("Mauve Pink","dw468719ee/images/prato-oval-raso-flora-24cm-mauvepink%20(2).png")],
    ["O Prato Oval Raso Flora Le Creuset &#233; perfeito para massas, saladas e aperitivos com design floral delicado na cor Mauve Pink.",
     "Cer&#226;mica premium com superf&#237;cie esmaltada de f&#225;cil limpeza. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","19cm · 24cm"),
     ("Cor","Mauve Pink"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","China"),("Garantia","7 anos")])

make_product("prato-octagon.html",
    "Prato Octagon Le Creuset",
    "Prato Octagon", "Cer&#226;mica · 22cm · Design octagonal",
    "R$ 249,00 – R$ 299,00", "a partir de 2x de R$ 124,50 sem juros",
    [("Vermelho","dwe98492df/images/Prato-Octagon-vermelho-28cm-lecreuset-20250-1.png")],
    ["O Prato Octagon Le Creuset &#233; uma pe&#231;a em cer&#226;mica premium com design octagonal &#250;nico que combina estilo e funcionalidade.",
     "Esmalte vibrante resist&#234;nte a lascas, arranhões e manchas. Vai ao forno, microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanhos","22cm · 28cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","China"),("Garantia","10 anos")])

make_product("prato-raso-19cm-shell-pink.html",
    "Prato Raso 19cm Shell Pink Le Creuset",
    "Prato Raso 19cm", "Cer&#226;mica · 19cm · Shell Pink",
    "R$ 209,00", "ou 2x de R$ 104,50 sem juros",
    [("Shell Pink","dw539ee9f4/images/prato-raso-19cm-shell%20pink.png")],
    ["O Prato Raso 19cm Le Creuset em Shell Pink &#233; ideal para refeições menores, sobremesas e petiscos.",
     "Cer&#226;mica premium com acabamento esmaltado. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","19cm"),
     ("Cor","Shell Pink"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")])

make_product("set-2-pratos-gato.html",
    "Set 2 Pratos Gato Le Creuset",
    "Set 2 Pratos Gato", "Cer&#226;mica · Preto e Branco",
    "R$ 329,00", "ou 3x de R$ 109,67 sem juros",
    [("Preto e Branco","dw95548df0/images/89401008070009-prato-gato.jpg")],
    ["O Set 2 Pratos Gato Le Creuset &#233; uma pe&#231;a especial em cer&#226;mica premium com design de gato em preto e branco.",
     "Ideal para presentear ou colecionadores. Superf&#237;cie esmaltada de f&#225;cil limpeza."],
    [("Material","Cer&#226;mica"),("Quantidade","2 pratos"),
     ("Cor","Preto e Branco"),("Cuidados","Lava-lou&#231;as"),("Garantia","10 anos")])

# Esgotados
make_product("set-4-pratos-fundos-22cm.html",
    "Set 4 Pratos Fundos 22cm Le Creuset",
    "Set 4 Pratos Fundos 22cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 869,00", "Produto indispon&#237;vel",
    [("Chambray","dwe90d3019/images/produto-lecreuset-prato-fundo-chambray.png")],
    ["O Set 4 Pratos Fundos 22cm Le Creuset &#233; ideal para sopas, massas e pratos com molhos.",
     "Cer&#226;mica premium Chambray com esmalte resist&#234;nte a lascas e manchas."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","22cm"),
     ("Quantidade","4 pe&#231;as"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-4-pratos-rasos-27cm-pratos.html",
    "Set 4 Pratos Rasos 27cm Le Creuset",
    "Set 4 Pratos Rasos 27cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 959,00", "Produto indispon&#237;vel",
    [("Chambray","dw43149ac5/images/produto-lecreuset-prato-set-chambray-27cm.png")],
    ["O Set 4 Pratos Rasos 27cm Le Creuset &#233; o tamanho perfeito para pratos principais.",
     "Cer&#226;mica premium Chambray com acabamento esmaltado resist&#234;nte."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","27cm"),
     ("Quantidade","4 pe&#231;as"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-4-pratos-rasos-22cm-pratos.html",
    "Set 4 Pratos Rasos 22cm Le Creuset",
    "Set 4 Pratos Rasos 22cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 869,00", "Produto indispon&#237;vel",
    [("Chambray","dw56bd1039/images/produto-lecreuset-prato-set-chambray-22cm.png")],
    ["O Set 4 Pratos Rasos 22cm Le Creuset &#233; ideal para refei&#231;&#245;es do dia a dia.",
     "Cer&#226;mica premium Chambray com acabamento esmaltado resist&#234;nte a lascas."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","22cm"),
     ("Quantidade","4 pe&#231;as"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)

make_product("prato-coracao-23cm.html",
    "Prato Coração 23cm Le Creuset",
    "Prato Cora&#231;&#227;o 23cm", "Cer&#226;mica · 23cm",
    "R$ 249,00", "Produto indispon&#237;vel",
    [("Vermelho","dw2ff2e063/images/prato-cora%C3%A7%C3%A3o-vermelho-lecreuset2.png"),
     ("Shell Pink","dw2ff2e063/images/prato-cora%C3%A7%C3%A3o-vermelho-lecreuset2.png")],
    ["O Prato Cora&#231;&#227;o 23cm Le Creuset &#233; uma pe&#231;a especial para servir sobremesas e petiscos com charme.",
     "Formato de cora&#231;&#227;o em cer&#226;mica premium com acabamento esmaltado."],
    [("Material","Cer&#226;mica"),("Tamanho","23cm"),("Garantia","10 anos")],
    sold_out=True)

make_product("prato-estrela.html",
    "Prato Estrela Le Creuset",
    "Prato Estrela", "Cer&#226;mica · Design estrela",
    "R$ 229,00", "Produto indispon&#237;vel",
    [("Vermelho","dw39d4b309/images/prato-estrela-vermelho.png"),
     ("Branco","dw39d4b309/images/prato-estrela-vermelho.png")],
    ["O Prato Estrela Le Creuset &#233; uma pe&#231;a festiva em cer&#226;mica premium com formato de estrela.",
     "Ideal para servir petiscos e sobremesas em ocasiões especiais."],
    [("Material","Cer&#226;mica"),("Garantia","10 anos")],
    sold_out=True)

make_product("prato-oval-fundo-flora.html",
    "Prato Oval Fundo Flora 22cm Le Creuset",
    "Prato Oval Fundo Flora 22cm", "Cer&#226;mica · Mauve Pink",
    "R$ 239,00", "Produto indispon&#237;vel",
    [("Mauve Pink","dw468719ee/images/prato-oval-fundo-flora-22cm-mauvepink.png")],
    ["O Prato Oval Fundo Flora 22cm Le Creuset combina design floral delicado com funcionalidade em Mauve Pink.",
     "Cer&#226;mica premium com superf&#237;cie esmaltada."],
    [("Material","Cer&#226;mica"),("Tamanho","22cm"),
     ("Cor","Mauve Pink"),("Garantia","10 anos")],
    sold_out=True)

make_product("prato-oblong-25cm.html",
    "Prato Oblong 25cm Le Creuset",
    "Prato Oblong 25cm", "Cer&#226;mica · Formato oblong",
    "R$ 339,00", "Produto indispon&#237;vel",
    [("Laranja","dw24bf448e/images/prato-oblong.png"),
     ("Vermelho","dw24bf448e/images/prato-oblong.png"),
     ("Branco","dw24bf448e/images/prato-oblong.png")],
    ["O Prato Oblong 25cm Le Creuset &#233; perfeito para servir carnes, peixes e pratos principais com muito estilo.",
     "Formato alongado em cer&#226;mica premium com acabamento esmaltado resist&#234;nte."],
    [("Material","Cer&#226;mica"),("Tamanho","25cm"),("Garantia","10 anos")],
    sold_out=True)


# ── Collection page ───────────────────────────────────────────────────────────
print("\nCriando colecao-pratos.html...")

def sw(img_id, hexc, label, url, active=False):
    act = " active" if active else ""
    brd = "border:1.5px solid #ccc;" if hexc in LIGHT else "border:1.5px solid transparent;"
    return f'<span class="swatch{act}" style="background:{hexc};{brd}" onclick="swatchClick(event,this,\'{img_id}\',\'{url}\')" title="{label}"></span>'

def card(img_id, href, img_src, alt, name, sub, price, swatches, sold_out=False, promo=False):
    badge = ""
    if sold_out:  badge = '<div class="oos-badge">ESGOTADO</div>'
    elif promo:   badge = '<div class="promo-badge">OFERTA</div>'
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

cards.append(card("i_van","prato-raso-vancouver.html",
    C+"dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"+Q,"Prato Raso Vancouver",
    "Prato Raso Vancouver","Cer&#226;mica · 17cm · 22cm · 27cm","A partir de R$ 199,00",
    sw("i_van","#C41E3A","Vermelho",C+"dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"+Q,True)+
    sw("i_van","#FFFFFF","Branco",C+"dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"+Q)+
    sw("i_van","#F4C2C2","Shell Pink",C+"dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"+Q)+
    sw("i_van","#007FFF","Azure",C+"dwa640170f/images/produto-lecreuset-prato-27cm-vermelho.png"+Q)))

cards.append(card("i_pfundo","prato-fundo-22cm.html",
    C+"dwa640170f/images/produto-lecreuset-prato-fundo-vermelho.png"+Q,"Prato Fundo 22cm",
    "Prato Fundo 22cm","Cer&#226;mica · 4 cores","R$ 219,00",
    sw("i_pfundo","#C41E3A","Vermelho",C+"dwa640170f/images/produto-lecreuset-prato-fundo-vermelho.png"+Q,True)+
    sw("i_pfundo","#1B5E8D","Marseille",C+"dw94bb8693/images/produto-lecreuset-prato-fundo-marseille%20(2).png"+Q)+
    sw("i_pfundo","#D4A857","Bamboo",C+"dw2a6ac032/images/produto-lecreuset-prato-fundo-bamboo.png"+Q)+
    sw("i_pfundo","#8B9467","Artichaut",C+"dw11e3da05/images/produto-lecreuset-prato-fundo-artichaut.png"+Q)))

cards.append(card("i_sf","prato-raso-san-francisco.html",
    C+"dw125979d7/images/produto-lecreuset-prato-set-22cm-preche.png"+Q,"Prato Raso San Francisco",
    "Prato Raso San Francisco","Cer&#226;mica · 22cm · 27cm","A partir de R$ 219,00",
    sw("i_sf","#FFCBA4","Peche",C+"dw125979d7/images/produto-lecreuset-prato-set-22cm-preche.png"+Q,True)+
    sw("i_sf","#0066B2","Bleu Riviera",C+"dw125979d7/images/produto-lecreuset-prato-set-22cm-preche.png"+Q)))

cards.append(card("i_sfp","prato-fundo-san-francisco.html",
    C+"dw125979d7/images/produto-lecreuset-prato-fundo-san-francisco-peche.png"+Q,"Prato Fundo San Francisco",
    "Prato Fundo San Francisco","Cer&#226;mica · Cole&#231;&#227;o San Francisco","R$ 219,00",
    sw("i_sfp","#FFCBA4","Peche",C+"dw125979d7/images/produto-lecreuset-prato-fundo-san-francisco-peche.png"+Q,True)+
    sw("i_sfp","#0066B2","Bleu Riviera",C+"dw125979d7/images/produto-lecreuset-prato-fundo-san-francisco-peche.png"+Q)))

cards.append(card("i_pao","prato-para-pao-16cm.html",
    C+"dwe854514b/images/pires-16cm-azure.png"+Q,"Prato para Pão 16cm",
    "Prato para P&#227;o 16cm","Cer&#226;mica · 16cm · 4 cores","R$ 109,00",
    sw("i_pao","#007FFF","Azure",C+"dwe854514b/images/pires-16cm-azure.png"+Q,True)+
    sw("i_pao","#F4A020","Nectar",C+"dw0e83efa8/images/pires-16cm-nectar.png"+Q)+
    sw("i_pao","#00B5CC","Caribe",C+"dwce23871b/images/pires-16cm-caribe.png"+Q)+
    sw("i_pao","#F4C2C2","Shell Pink",C+"dwff1777f9/images/pires-16cm-shellpink.png"+Q)))

cards.append(card("i_holly","prato-raso-sphere-holly.html",
    C+"dw1e1caa0d/images/prato-raso-sphere-holly-branco.png"+Q,"Prato Raso Sphere Holly",
    "Prato Raso Sphere Holly 19cm","Cer&#226;mica · Cole&#231;&#227;o Holly","R$ 259,00",
    sw("i_holly","#FFFFFF","Branco",C+"dw1e1caa0d/images/prato-raso-sphere-holly-branco.png"+Q,True)+
    sw("i_holly","#6D7C5E","Thyme",C+"dw921fc859/images/prato-raso-sphere-holly-thyme.png"+Q)+
    sw("i_holly","#C41E3A","Vermelho",C+"dwf81d34c7/images/prato-raso-sphere-holly-vermelho.png"+Q)))

cards.append(card("i_estrela","bandeja-estrela-de-servir.html",
    C+"dw39d4b309/images/bandeja-estrela-de-servir-vermelho-36cm.png"+Q,"Bandeja Estrela de Servir",
    "Bandeja Estrela de Servir","Cer&#226;mica · 36cm","R$ 619,00",
    sw("i_estrela","#C41E3A","Vermelho",C+"dw39d4b309/images/bandeja-estrela-de-servir-vermelho-36cm.png"+Q,True)))

cards.append(card("i_ruffle_f","prato-fundo-ruffle-21cm.html",
    C+"dwdf2048f1/images/prato-fundo-ruffle-21cm-branco1%20(2).png"+Q,"Prato Fundo Ruffle 21cm",
    "Prato Fundo Ruffle 21cm","Cer&#226;mica · 1,3L","R$ 619,00",
    sw("i_ruffle_f","#FFFFFF","Branco",C+"dwdf2048f1/images/prato-fundo-ruffle-21cm-branco1%20(2).png"+Q,True)))

cards.append(card("i_ruffle_s","prato-de-servir-ruffle-36cm.html",
    C+"dw85245aba/images/prato-de-servir-ruffle-36cm-shell-pink1.png"+Q,"Prato de Servir Ruffle 36cm",
    "Prato de Servir Ruffle 36cm","Cer&#226;mica · 36cm · 2 cores","R$ 739,00",
    sw("i_ruffle_s","#F4C2C2","Shell Pink",C+"dw85245aba/images/prato-de-servir-ruffle-36cm-shell-pink1.png"+Q,True)+
    sw("i_ruffle_s","#FFFFFF","Branco",C+"dw1d438b2f/images/prato-de-servir-ruffle-36cm-branco1%20(2).png"+Q)))

cards.append(card("i_kobe","prato-fundo-kobe.html",
    C+"dw7c5c286c/images/tardes%20de%20verao/prato-fundo-kobe-22cm-laranja.png"+Q,"Prato Fundo Kobe",
    "Prato Fundo Kobe","Cer&#226;mica · 3 cores · Cole&#231;&#227;o Kobe","A partir de R$ 229,00",
    sw("i_kobe","#FE5000","Laranja",C+"dw7c5c286c/images/tardes%20de%20verao/prato-fundo-kobe-22cm-laranja.png"+Q,True)+
    sw("i_kobe","#C41E3A","Vermelho",C+"dwca54c05d/images/tardes%20de%20verao/prato-fundo-kobe-22cm-vermelho.png"+Q)+
    sw("i_kobe","#FFFFFF","Branco",C+"dw45f78070/images/tardes%20de%20verao/prato-fundo-kobe-22cm-white.png"+Q)))

cards.append(card("i_jardin_b","bandeja-de-servir-oval-jardin.html",
    C+"dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"+Q,"Bandeja Oval Jardin",
    "Bandeja de Servir Oval Jardin","Cer&#226;mica · Cole&#231;&#227;o Jardin","R$ 370,30",
    sw("i_jardin_b","#F4C2C2","Shell Pink",C+"dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"+Q,True)+
    sw("i_jardin_b","#F5E090","Camomille",C+"dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"+Q)+
    sw("i_jardin_b","#A8C5BB","Sea Salt",C+"dwb4dbd8ba/images/bandeja-de-servir-oval-jardin-36cm-shellpink%20(2).png"+Q),
    promo=True))

cards.append(card("i_jardin_r","prato-raso-jardin-22cm.html",
    C+"dwd6edfa02/images/prato-raso-jardin-22cm-camomille.png"+Q,"Prato Raso Jardin 22cm",
    "Prato Raso Jardin 22cm","Cer&#226;mica · Cole&#231;&#227;o Jardin","A partir de R$ 167,30",
    sw("i_jardin_r","#F5E090","Camomille",C+"dwd6edfa02/images/prato-raso-jardin-22cm-camomille.png"+Q,True)+
    sw("i_jardin_r","#F4C2C2","Shell Pink",C+"dwd64b3fe2/images/prato-raso-jardin-22cm-shell%20pink.png"+Q)+
    sw("i_jardin_r","#FDF5E6","Meringue",C+"dwabe4156a/images/prato-raso-jardin-22cm-meringue.png"+Q)))

cards.append(card("i_jantar","set-jantar-vancouver.html",
    C+"dw56fcfc5d/images/kit-jantar-vermelho.png"+Q,"Set Jantar Vancouver",
    "Set Jantar Vancouver","Cer&#226;mica · 16 pe&#231;as · 4 pessoas","R$ 3.089,00",
    sw("i_jantar","#C41E3A","Vermelho",C+"dw56fcfc5d/images/kit-jantar-vermelho.png"+Q,True)+
    sw("i_jantar","#FFFFFF","Branco",C+"dw279f2810/images/kit-jantar-branco.png"+Q)))

cards.append(card("i_flor","prato-flor.html",
    C+"dw408ec32f/images/Prato%20Flor%2014Cm.png"+Q,"Prato Flor",
    "Prato Flor","Cer&#226;mica · 14cm e 23cm · Bluebell Purple","A partir de R$ 199,00",
    sw("i_flor","#7B68C8","Bluebell Purple",C+"dw408ec32f/images/Prato%20Flor%2014Cm.png"+Q,True)))

cards.append(card("i_flower","set-2-pratos-flower-23cm.html",
    C+"dw5dca48b0/images/Flower-coolmint-fotos-primavera.png"+Q,"Set 2 Pratos Flower 23cm",
    "Set 2 Pratos Flower 23cm","Cer&#226;mica · Cool Mint","R$ 549,00",
    sw("i_flower","#A8D5C2","Cool Mint",C+"dw5dca48b0/images/Flower-coolmint-fotos-primavera.png"+Q,True)))

cards.append(card("i_flora_r","prato-oval-raso-flora.html",
    C+"dw468719ee/images/prato-oval-raso-flora-24cm-mauvepink%20(2).png"+Q,"Prato Oval Raso Flora",
    "Prato Oval Raso Flora","Cer&#226;mica · Mauve Pink","A partir de R$ 209,00",
    sw("i_flora_r","#CF9BAE","Mauve Pink",C+"dw468719ee/images/prato-oval-raso-flora-24cm-mauvepink%20(2).png"+Q,True)))

cards.append(card("i_oct","prato-octagon.html",
    C+"dwe98492df/images/Prato-Octagon-vermelho-28cm-lecreuset-20250-1.png"+Q,"Prato Octagon",
    "Prato Octagon","Cer&#226;mica · Design octagonal","A partir de R$ 249,00",
    sw("i_oct","#C41E3A","Vermelho",C+"dwe98492df/images/Prato-Octagon-vermelho-28cm-lecreuset-20250-1.png"+Q,True)))

cards.append(card("i_19sp","prato-raso-19cm-shell-pink.html",
    C+"dw539ee9f4/images/prato-raso-19cm-shell%20pink.png"+Q,"Prato Raso 19cm Shell Pink",
    "Prato Raso 19cm","Cer&#226;mica · Shell Pink","R$ 209,00",
    sw("i_19sp","#F4C2C2","Shell Pink",C+"dw539ee9f4/images/prato-raso-19cm-shell%20pink.png"+Q,True)))

cards.append(card("i_gato","set-2-pratos-gato.html",
    C+"dw95548df0/images/89401008070009-prato-gato.jpg"+Q,"Set 2 Pratos Gato",
    "Set 2 Pratos Gato","Cer&#226;mica · Preto e Branco","R$ 329,00",
    sw("i_gato","#333333","Preto e Branco",C+"dw95548df0/images/89401008070009-prato-gato.jpg"+Q,True)))

cards.append(card("i_pet","set-5-mini-pratos-petalas.html",
    C+"dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png"+Q,"Set 5 Mini Pratos Pétalas",
    "Set 5 Mini Pratos P&#233;talas","Cer&#226;mica · Bluebell Purple","R$ 659,00",
    sw("i_pet","#7B68C8","Bluebell Purple",C+"dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png"+Q,True)))

# Esgotados
cards.append(card("i_pf22","set-4-pratos-fundos-22cm.html",
    C+"dwe90d3019/images/produto-lecreuset-prato-fundo-chambray.png"+Q,"Set 4 Pratos Fundos 22cm",
    "Set 4 Pratos Fundos 22cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 869,00",
    sw("i_pf22","#7BA3C8","Chambray",C+"dwe90d3019/images/produto-lecreuset-prato-fundo-chambray.png"+Q,True),
    sold_out=True))

cards.append(card("i_pr27","set-4-pratos-rasos-27cm-pratos.html",
    C+"dw43149ac5/images/produto-lecreuset-prato-set-chambray-27cm.png"+Q,"Set 4 Pratos Rasos 27cm",
    "Set 4 Pratos Rasos 27cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 959,00",
    sw("i_pr27","#7BA3C8","Chambray",C+"dw43149ac5/images/produto-lecreuset-prato-set-chambray-27cm.png"+Q,True),
    sold_out=True))

cards.append(card("i_pr22","set-4-pratos-rasos-22cm-pratos.html",
    C+"dw56bd1039/images/produto-lecreuset-prato-set-chambray-22cm.png"+Q,"Set 4 Pratos Rasos 22cm",
    "Set 4 Pratos Rasos 22cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 869,00",
    sw("i_pr22","#7BA3C8","Chambray",C+"dw56bd1039/images/produto-lecreuset-prato-set-chambray-22cm.png"+Q,True),
    sold_out=True))

cards.append(card("i_corac","prato-coracao-23cm.html",
    C+"dw2ff2e063/images/prato-cora%C3%A7%C3%A3o-vermelho-lecreuset2.png"+Q,"Prato Coração 23cm",
    "Prato Cora&#231;&#227;o 23cm","Cer&#226;mica · 23cm","R$ 249,00",
    sw("i_corac","#C41E3A","Vermelho",C+"dw2ff2e063/images/prato-cora%C3%A7%C3%A3o-vermelho-lecreuset2.png"+Q,True),
    sold_out=True))

cards.append(card("i_estb","prato-estrela.html",
    C+"dw39d4b309/images/prato-estrela-vermelho.png"+Q,"Prato Estrela",
    "Prato Estrela","Cer&#226;mica · Design estrela","R$ 229,00",
    sw("i_estb","#C41E3A","Vermelho",C+"dw39d4b309/images/prato-estrela-vermelho.png"+Q,True),
    sold_out=True))

cards.append(card("i_flora_f","prato-oval-fundo-flora.html",
    C+"dw468719ee/images/prato-oval-fundo-flora-22cm-mauvepink.png"+Q,"Prato Oval Fundo Flora 22cm",
    "Prato Oval Fundo Flora 22cm","Cer&#226;mica · Mauve Pink","R$ 239,00",
    sw("i_flora_f","#CF9BAE","Mauve Pink",C+"dw468719ee/images/prato-oval-fundo-flora-22cm-mauvepink.png"+Q,True),
    sold_out=True))

cards.append(card("i_obl","prato-oblong-25cm.html",
    C+"dw24bf448e/images/prato-oblong.png"+Q,"Prato Oblong 25cm",
    "Prato Oblong 25cm","Cer&#226;mica · Formato oblong","R$ 339,00",
    sw("i_obl","#FE5000","Laranja",C+"dw24bf448e/images/prato-oblong.png"+Q,True),
    sold_out=True))

N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Pratos | Le Creuset Brasil</title>
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
    .cat-banner-left{{position:relative;padding:32px 48px 40px 32px;display:flex;flex-direction:column;justify-content:flex-end;background:#f5f2f0;overflow:hidden;}}
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
          <span>Pratos</span>
        </div>
        <h1 class="cat-banner-title">Pratos</h1>
        <p class="cat-banner-desc">Pratos Le Creuset em cer&#226;mica premium com design ic&#244;nico &#8212; para o dia a dia e ocasi&#245;es especiais.</p>
      </div>
    </div>
    <div class="cat-banner-right">
      <img src="{BANNER}" alt="Pratos Le Creuset"/>
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
        <label class="filter-option"><input type="checkbox"> Pratos Rasos</label>
        <label class="filter-option"><input type="checkbox"> Pratos Fundos</label>
        <label class="filter-option"><input type="checkbox"> Bandejas</label>
        <label class="filter-option"><input type="checkbox"> Sets</label>
        <label class="filter-option"><input type="checkbox"> Especiais</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Cole&#231;&#227;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Vancouver</label>
        <label class="filter-option"><input type="checkbox"> San Francisco</label>
        <label class="filter-option"><input type="checkbox"> Kobe</label>
        <label class="filter-option"><input type="checkbox"> Jardin</label>
        <label class="filter-option"><input type="checkbox"> Ruffle</label>
        <label class="filter-option"><input type="checkbox"> Flora</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Pre&#231;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> At&#233; R$ 200</label>
        <label class="filter-option"><input type="checkbox"> R$ 200 &#8211; R$ 400</label>
        <label class="filter-option"><input type="checkbox"> R$ 400 &#8211; R$ 800</label>
        <label class="filter-option"><input type="checkbox"> + R$ 800</label>
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

with open(os.path.join(BASE, "colecao-pratos.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"  Cole\u00e7\u00e3o: colecao-pratos.html ({N} produtos)")
print("\nTudo pronto!")
