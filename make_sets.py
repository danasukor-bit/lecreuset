#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE   = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN    = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q      = "?sw=650&sh=650&sm=fit"
BANNER = "https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwbb491913/category/cat_banners/categoria-site-sets2.jpeg"

WISH = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

COLOR_HEX = {
    "Vermelho":"#C41E3A","Laranja":"#FE5000","Black Onyx":"#1a1a1a",
    "Bleu Riviera":"#0066B2","Branco":"#FFFFFF","Meringue":"#FDF5E6",
    "Thyme":"#6D7C5E","Bamboo":"#D4A857","Artichaut":"#8B9467",
    "Caribe":"#00B5CC","Nectar":"#F4A020","Chambray":"#7BA3C8",
    "Bluebell Purple":"#7B68C8","Mauve Pink":"#CF9BAE","Multicor 2":"#FF69B4",
    "Azure":"#007FFF","Onyx":"#1a1a1a","Matte Black":"#222222",
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
          <div class="mega-col"><div class="mega-col-title">Acess&#243;rios</div>
            <a href="colecao-moedores-e-galheteiro.html">Moedores e Galheteiro</a>
            <a href="colecao-potes-e-porta-mantimentos.html">Potes e Porta-Mantimentos</a>
            <a href="colecao-acessorios-de-vinhos.html">Acess&#243;rios de Vinhos</a>
            <a href="colecao-sets.html">Sets</a>
            <a href="colecao-utensilios.html">Utensilios</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Cole&#231;&#245;es</div>
            <a href="colecao-bleu-riviera.html">Bleu Riviera</a>
            <a href="colecao-lancamentos.html">Lan&#231;amentos</a>
            <a href="colecao-best-sellers.html">Best-Sellers</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Nossas Cores</div>
            <a href="colecao-nossas-cores.html">Ver Todas as Cores</a>
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
    .color-swatch{width:32px;height:32px;border-radius:50%;cursor:pointer;display:inline-block;transition:transform 0.15s,box-shadow 0.15s;border:2px solid transparent;}
    .color-swatch:hover{transform:scale(1.12);}
    .color-swatch.active{box-shadow:0 0 0 2px #fff,0 0 0 4px #000;}
    .btn-cart{display:block;width:100%;background:#000;color:#fff;border:none;padding:16px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;margin-bottom:12px;}
    .btn-cart:hover:not([disabled]){background:#222;}
    .btn-wishlist{display:block;width:100%;background:#fff;color:#000;border:2px solid #000;padding:14px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;}
    .badge-oos{display:inline-block;background:#888;color:#fff;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:3px;margin-bottom:16px;}
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


def make_product(filename, title, name, sub, price, install, colors_imgs, desc, specs, sold_out=False):
    first_c, first_img = colors_imgs[0]
    swatches = ""
    for i, (cname, cimg) in enumerate(colors_imgs):
        url = CDN + cimg + Q
        hexc = COLOR_HEX.get(cname, "#888")
        bord = "border:2px solid #ccc;" if hexc in ("#FFFFFF","#FDF5E6","#B0B0B0") else "border:2px solid transparent;"
        act  = " active" if i == 0 else ""
        swatches += f'<span class="color-swatch{act}" style="background:{hexc};{bord}" title="{cname}" onclick="selectColor(this,\'{cname}\',\'{url}\')"></span>\n      '

    specs_html = "".join(f"<tr><td class='sk'>{k}:</td><td class='sv'>{v}</td></tr>" for k, v in specs)
    desc_html  = "".join(f"<p>{p}</p>" for p in desc)
    first_url  = CDN + first_img + Q

    oos_badge = '<div class="badge-oos">Esgotado</div>' if sold_out else ""
    if sold_out:
        cart_btn = '<button class="btn-cart" disabled style="opacity:0.5;cursor:not-allowed;">Produto Esgotado</button>'
    else:
        cart_btn = '<button class="btn-cart">Adicionar ao Carrinho</button>'

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
  <a href="colecao-sets.html">Sets</a><span>/</span>
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
    {oos_badge}
    <h1 class="product-name">{name}</h1>
    <div class="product-sub">{sub}</div>
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

make_product("set-azeite-vinagre-classico.html",
    "Set Azeite & Vinagre Clássico Le Creuset",
    "Set Azeite &amp; Vinagre Cl&#225;ssico", "Cer&#226;mica · 2 pe&#231;as",
    "R$ 579,00", "ou 5x de R$ 115,80 sem juros",
    [("Laranja","dwe9691760/images/80803020600003.jpg")],
    ["O Set Azeite &amp; Vinagre Cl&#225;ssico Le Creuset combina conveni&#234;ncia e personalidade &#224; bancada ou mesa.",
     "A superf&#237;cie esmaltada facilita a remo&#231;&#227;o dos alimentos, tornando o processo de limpeza mais r&#225;pido. Apto para lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","7cm × 7cm × 17cm"),
     ("Quantidade","2 pe&#231;as"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("set-caneca-100ml-gift-collection.html",
    "Set Caneca 100ml Gift Collection Le Creuset",
    "Set Caneca 100ml Gift Collection", "Cer&#226;mica · 6 pe&#231;as",
    "R$ 639,00", "ou 6x de R$ 106,50 sem juros",
    [("Multicor 2","dw72d4c5ef/images/79114105219030-gift-collection.jpg")],
    ["A paleta vibrante da cole&#231;&#227;o Gift Collection ilumina todas as refei&#231;&#245;es.",
     "Feito de cer&#226;mica com esmalte dur&#225;vel que resiste a marcas de utens&#237;lios e arranhões. A cer&#226;mica densa bloqueia a absor&#231;&#227;o de umidade.",
     "O conjunto inclui 6 can&#233;cas de 100ml em cores diferentes da Gift Collection."],
    [("Material","Cer&#226;mica"),("Capacidade","100ml cada"),
     ("Quantidade","6 can&#233;cas"),("Cor","Multicor 2"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("set-pegadores-de-silicone.html",
    "Set Pegadores de Silicone Le Creuset",
    "Set Pegadores de Silicone", "Silicone · 2 pe&#231;as",
    "R$ 219,00", "ou 2x de R$ 109,50 sem juros",
    [("Vermelho","dw309d5819/images/produto-lecreuset-utensilio-pegadores-vermelho.png"),
     ("Laranja","dwf8e4e3a6/images/produto-lecreuset-utensilio-pegadores-laranja.png"),
     ("Bleu Riviera","dw48f6f78f/images/produto-lecreuset-utensilio-pegadores-bleu-riviera.png"),
     ("Nectar","dw87039a69/images/produto-lecreuset-utensilio-pegadores-nectar.png"),
     ("Black Onyx","dwc36d4bf5/images/produto-lecreuset-utensilio-pegadores-black-onyx.png")],
    ["O Set Pegadores de Silicone Le Creuset proporcionam uma ader&#234;ncia segura e protegem as m&#227;os enquanto cozinha.",
     "Use-os no fog&#227;o ou no forno. O silicone resist&#234;ncia ao calor garante seguran&#231;a total durante o manuseio de panelas e travessas quentes."],
    [("Material","Silicone"),("Dimens&#245;es","12cm × 6cm × 3,5cm"),
     ("Quantidade","2 pe&#231;as"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","China"),("Garantia","5 anos")])

make_product("set-4-utensilios-inox-alpine.html",
    "Set 4 Utensílios Inox Alpine Le Creuset",
    "Set 4 Utensilios Inox Alpine", "A&#231;o Inox · Black Onyx · 4 pe&#231;as",
    "R$ 1.429,00", "ou 10x de R$ 142,90 sem juros",
    [("Black Onyx","dw6d406278/images/conjunto-alpine-4-pecas-inox.png")],
    ["O Set 4 Utensilios Inox Alpine &#233; o conjunto ideal para os amantes de churrasco. Pe&#231;as ideais para virar, pegar, pincelar e servir.",
     "A esp&#225;tula possui abridor de garrafas integrado. O garfo de dois dentes &#233; perfeito para manusear carnes e o pincel garante aplica&#231;&#227;o uniforme de molhos.",
     "O conjunto inclui bolsa exclusiva Le Creuset para transporte e armazenamento."],
    [("Material","A&#231;o Inox"),("Cor","Black Onyx"),
     ("Dimens&#245;es","49cm × 21cm × 7cm"),("Quantidade","4 pe&#231;as + bolsa"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","China"),("Garantia","5 anos")])

make_product("set-3-protetores.html",
    "Set 3 Protetores Le Creuset",
    "Set 3 Protetores", "Feltro · Protetor estrela para panelas",
    "R$ 239,00", "ou 2x de R$ 119,50 sem juros",
    [("Laranja","dw646049c0/images/set-protetor-para-panela%20(1).png"),
     ("Black Onyx","dw236a5715/images/set-protetor-para-panela%20(2).png")],
    ["Resistentes e dur&#225;veis, o Set de 3 Protetores de panelas, fabricados em feltro, fornecem uma camada macia e acolchoada entre panelas e frigideiras empilhadas quando armazenadas.",
     "O design em estrela ajuda a evitar lascas e arranhões durante o armazenamento. Indispens&#225;vel para preservar o esmalte das suas panelas Le Creuset."],
    [("Material","T&#234;xtil (feltro)"),("Quantidade","3 protetores"),
     ("Cuidados","Lavagem &#224; m&#227;o"),("Origem","Fran&#231;a"),("Garantia","2 anos")])

make_product("set-molhos-condimentos.html",
    "Set Molhos & Condimentos Le Creuset",
    "Set Molhos &amp; Condimentos", "Cer&#226;mica · Ideal para servir",
    "R$ 449,00", "ou 4x de R$ 112,25 sem juros",
    [("Vermelho","dw05bb12d2/images/91027800010000.jpg")],
    ["Pr&#225;tico e elegante, o Set Molhos e Condimentos &#233; perfeito para servir uma sele&#231;&#227;o de molhos e temperos, adicionando um toque de cor &#224; mesa.",
     "A superf&#237;cie esmaltada facilita a remo&#231;&#227;o dos alimentos e &#233; apta para lava-lou&#231;as. Ideal para azeite, vinagre, molho shoyu e outros condimentos."],
    [("Material","Cer&#226;mica com esmalte"),("Dimens&#245;es","10cm × 8cm × 5cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("set-3-mini-pratos-de-tapas.html",
    "Set 3 Mini Pratos de Tapas Le Creuset",
    "Set 3 Mini Pratos de Tapas", "Cer&#226;mica · Chambray · 3 pe&#231;as",
    "R$ 314,30", "ou 3x de R$ 104,77 sem juros",
    [("Chambray","dwb489c4a7/images/prato-triangulo-chambray.png")],
    ["O Set 3 Mini Pratos de Tapas inclui uma tigela triangular de 200ml, uma tigela redonda de 240ml e uma tigela quadrada de 300ml.",
     "Feito de cer&#226;mica premium na cor Chambray, &#233; perfeito para servir molhos, temperos e entradas. O acabamento dur&#225;vel resiste a lascas, arranhões e manchas.",
     "Vai ao forno, microondas, geladeira, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidades","200ml · 240ml · 300ml"),
     ("Quantidade","3 pe&#231;as"),("Cor","Chambray"),
     ("Dimens&#245;es","23cm × 11cm × 7cm"),("Origem","China"),("Garantia","10 anos")])

make_product("set-5-mini-pratos-petalas.html",
    "Set 5 Mini Pratos Pétalas Le Creuset",
    "Set 5 Mini Pratos P&#233;talas", "Cer&#226;mica · Bluebell Purple · 5 pe&#231;as",
    "R$ 659,00", "ou 6x de R$ 109,83 sem juros",
    [("Bluebell Purple","dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png")],
    ["O Set 5 Mini Pratos P&#233;talas &#233; perfeito para servir aperitivos, petiscos e acompanhamentos com charme &#250;nico.",
     "Os pratos em formato de p&#233;tala s&#227;o feitos de cer&#226;mica premium com superf&#237;cie esmaltada de f&#225;cil limpeza. Vão ao forno, microondas, geladeira, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","23cm × 23cm × 5cm"),
     ("Quantidade","5 pe&#231;as"),("Cor","Bluebell Purple"),
     ("Origem","China"),("Garantia","10 anos")])

make_product("set-bowl-prato.html",
    "Set Bowl & Prato Le Creuset",
    "Set Bowl &amp; Prato", "Cer&#226;mica · Mauve Pink · 2 pe&#231;as",
    "R$ 409,00", "ou 4x de R$ 102,25 sem juros",
    [("Mauve Pink","dw29ba298c/images/Set%20Bowl%20+%20Prato.png")],
    ["O Set Bowl &amp; Prato &#233; ideal para servir acompanhamentos, entradas ou doces de um jeito criativo e cheio de personalidade.",
     "A cer&#226;mica premium com acabamento esmaltado &#233; resistente a lascas e manchas. Vai ao forno, microondas, geladeira, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","15cm × 15cm × 7cm"),
     ("Quantidade","2 pe&#231;as"),("Cor","Mauve Pink"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","China"),("Garantia","10 anos")])

make_product("set-tampa-para-moedores-21cm.html",
    "Set Tampa para Moedores 21cm Le Creuset",
    "Set Tampa para Moedores 21cm", "Silicone · 2 tampas",
    "R$ 79,00", "ou 2x de R$ 39,50 sem juros",
    [("Laranja","dwf311dea5/images/produto-lecreuset-tampa-set-silicone.png"),
     ("Azure","dw454a79d3/images/kit-2-tampas-de-silicone-para-moedores-azure-blue.png")],
    ["As tampas de silicone Le Creuset coletam res&#237;duos de sal e pimenta, mantendo as bancadas limpas.",
     "Projetadas para encaixar perfeitamente nos moedores Le Creuset 21cm. O material de silicone de alta qualidade &#233; apto para lava-lou&#231;as e f&#225;cil de limpar."],
    [("Material","Silicone"),("Dimens&#245;es","6,5cm × 6,5cm × 1,5cm"),
     ("Quantidade","2 tampas"),("Compatibilidade","Moedores Le Creuset 21cm"),
     ("Cuidados","Lava-lou&#231;as"),("Garantia","5 anos")])

make_product("set-saleiro-pimenteiro.html",
    "Set Saleiro & Pimenteiro Le Creuset",
    "Set Saleiro &amp; Pimenteiro", "Cer&#226;mica · 2 pe&#231;as",
    "R$ 319,00", "ou 3x de R$ 106,33 sem juros",
    [("Laranja","dw4b44a6db/images/produto-lecreuset-saleiro-pimenteiro-laranja.png"),
     ("Vermelho","dw2c3611db/images/produto-lecreuset-saleiro-pimenteiro-vermelho.png"),
     ("Artichaut","dw756f8ec6/images/produto-lecreuset-saleiro-pimenteiro-artichaut.png"),
     ("Caribe","dwc39e9fcd/images/produto-lecreuset-saleiro-pimenteiro-caribe.png"),
     ("Branco","dwb2c50bea/images/produto-lecreuset-saleiro-pimenteiro-branco.png")],
    ["Na mesa para uso durante as refei&#231;&#245;es ou na bancada para temperar seus pratos, o Set Saleiro &amp; Pimenteiro trazem mais cor e sabor para o seu dia a dia.",
     "A superf&#237;cie esmaltada facilita a remo&#231;&#227;o dos alimentos, tornando o processo de limpeza mais r&#225;pido. Apto para lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Quantidade","2 pe&#231;as"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("set-2-canecas-200ml-com-pires.html",
    "Set 2 Canecas 200ml com Pires Le Creuset",
    "Set 2 Can&#233;cas 200ml com Pires", "Cer&#226;mica · Laranja · 4 pe&#231;as",
    "R$ 579,00", "ou 5x de R$ 115,80 sem juros",
    [("Laranja","dw524d5e68/images/set-2-canecas-expresso-laranja.png")],
    ["O Set 2 Can&#233;cas 200ml com Pires mant&#233;m caf&#233;, ch&#225;, chocolate quente e cappuccino quente ou frio.",
     "Feito de cer&#226;mica premium com superf&#237;cie esmaltada que facilita a limpeza. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidade","200ml cada"),
     ("Quantidade","2 can&#233;cas + 2 pires"),("Cor","Laranja"),
     ("Cuidados","Microondas · Lava-lou&#231;as"),("Garantia","10 anos")])

make_product("set-chaleira-demi-e-2-canecas-seattle.html",
    "Set Chaleira Demi e 2 Canecas Seattle Le Creuset",
    "Set Chaleira Demi e 2 Can&#233;cas Seattle", "A&#231;o Carbono Esmaltado + Cer&#226;mica",
    "R$ 1.149,00", "ou 10x de R$ 114,90 sem juros",
    [("Laranja","dwcc27cd7f/images/set-chaleira-demi-&-2-canecas-seattle-laranja.png")],
    ["O Set re&#250;ne a Chaleira Demi de 1,1L com 2 Can&#233;cas Seattle de 400ml — a combina&#231;&#227;o perfeita para os momentos de caf&#233; e ch&#225;.",
     "A chaleira em a&#231;o carbono esmaltado &#233; compat&#237;vel com todos os fog&#245;es, incluindo indu&#231;&#227;o. As can&#233;cas de cer&#226;mica v&#227;o ao microondas, forno, freezer e lava-lou&#231;as."],
    [("Material","A&#231;o carbono esmaltado (chaleira) · Cer&#226;mica (can&#233;cas)"),
     ("Capacidade chaleira","1,1L"),("Capacidade can&#233;cas","400ml cada"),
     ("Quantidade","1 chaleira + 2 can&#233;cas"),
     ("Compat&#237;vel com","Todos os fog&#245;es + indu&#231;&#227;o"),
     ("Cuidados","Chaleira: &#224; m&#227;o · Can&#233;cas: lava-lou&#231;as"),
     ("Garantia","5 anos")])

make_product("set-azeite-vinagre-signature.html",
    "Set Azeite & Vinagre Signature Le Creuset",
    "Set Azeite &amp; Vinagre Signature", "Cer&#226;mica · 2 pe&#231;as",
    "R$ 629,00", "ou 6x de R$ 104,83 sem juros",
    [("Meringue","dwc44577d9/images/set-azeite-vinagre.png"),
     ("Thyme","dwc44577d9/images/set-azeite-vinagre.png")],
    ["O Set de Azeite e Vinagre de cer&#226;mica Le Creuset trazem conveni&#234;ncia e personalidade &#224; bancada ou mesa.",
     "A superf&#237;cie esmaltada de alta qualidade facilita a remo&#231;&#227;o dos alimentos e garante limpeza r&#225;pida. Ideal para uso di&#225;rio."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","17cm × 8cm × 20cm"),
     ("Quantidade","2 pe&#231;as"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("set-2-suportes-para-velas.html",
    "Set 2 Suportes para Velas Le Creuset",
    "Set 2 Suportes para Velas", "Cer&#226;mica · 2 pe&#231;as",
    "R$ 239,00", "Produto indispon&#237;vel",
    [("Vermelho","dw0867dbb8/images/suporte-para-vela-lecreuset2.png")],
    ["O Set 2 Suportes para Velas Le Creuset adicionam charme e sofistica&#231;&#227;o &#224; decora&#231;&#227;o da sua mesa.",
     "Feito de cer&#226;mica com acabamento esmaltado caracter&#237;stico da Le Creuset."],
    [("Material","Cer&#226;mica"),("Quantidade","2 pe&#231;as"),
     ("Garantia","10 anos")],
    sold_out=True)

make_product("bowl-coracao-650ml.html",
    "Bowl Coração 650ml Le Creuset",
    "Bowl Cora&#231;&#227;o 650ml", "Cer&#226;mica · Vermelho · 650ml",
    "R$ 249,00", "Produto indispon&#237;vel",
    [("Vermelho","dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png")],
    ["O Bowl Cora&#231;&#227;o 650ml Le Creuset &#233; uma pe&#231;a especial para servir sobremesas, frutas e acompanhamentos com muito estilo.",
     "Feito de cer&#226;mica premium no formato de cora&#231;&#227;o, combina funcionalidade e design &#250;nico."],
    [("Material","Cer&#226;mica"),("Capacidade","650ml"),
     ("Cor","Vermelho"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-4-pratos-fundos-22cm.html",
    "Set 4 Pratos Fundos 22cm Le Creuset",
    "Set 4 Pratos Fundos 22cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 869,00", "Produto indispon&#237;vel",
    [("Chambray","dwe90d3019/images/produto-lecreuset-prato-fundo-chambray.png")],
    ["O Set 4 Pratos Fundos 22cm Le Creuset &#233; a escolha perfeita para servir sopas, massas e pratos com molhos.",
     "Feito de cer&#226;mica premium com acabamento esmaltado na cor Chambray. Resistente a lascas, microondas e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","22cm"),
     ("Quantidade","4 pe&#231;as"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-suporte-ovo-gift-collection.html",
    "Set Suporte Ovo Gift Collection Le Creuset",
    "Set Suporte Ovo Gift Collection", "Cer&#226;mica · 6 cores",
    "R$ 409,00", "Produto indispon&#237;vel",
    [("Multicor 2","dw95548df0/images/porta-ovo-gift-lecreuset2.png")],
    ["O Set Suporte Ovo Gift Collection Le Creuset &#233; uma pe&#231;a especial para servir e apresentar ovos com muito estilo.",
     "Cada suporte vem em uma cor diferente da vibrante paleta Gift Collection."],
    [("Material","Cer&#226;mica"),("Cor","Multicor 2"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-4-pratos-rasos-22cm.html",
    "Set 4 Pratos Rasos 22cm Le Creuset",
    "Set 4 Pratos Rasos 22cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 869,00", "Produto indispon&#237;vel",
    [("Chambray","dw56bd1039/images/produto-lecreuset-prato-set-chambray-22cm.png")],
    ["O Set 4 Pratos Rasos 22cm Le Creuset &#233; ideal para refei&#231;&#245;es do dia a dia e ocasiões especiais.",
     "Feito de cer&#226;mica premium com acabamento esmaltado na cor Chambray. Resistente a lascas e apto para lava-lou&#231;as e microondas."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","22cm"),
     ("Quantidade","4 pe&#231;as"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)

make_product("set-4-pratos-rasos-27cm.html",
    "Set 4 Pratos Rasos 27cm Le Creuset",
    "Set 4 Pratos Rasos 27cm", "Cer&#226;mica · Chambray · 4 pe&#231;as",
    "R$ 959,00", "Produto indispon&#237;vel",
    [("Chambray","dw43149ac5/images/produto-lecreuset-prato-set-chambray-27cm.png")],
    ["O Set 4 Pratos Rasos 27cm Le Creuset &#233; o tamanho perfeito para pratos principais.",
     "Feito de cer&#226;mica premium com acabamento esmaltado na cor Chambray. Resistente a lascas e apto para lava-lou&#231;as e microondas."],
    [("Material","Cer&#226;mica"),("Di&#226;metro","27cm"),
     ("Quantidade","4 pe&#231;as"),("Cor","Chambray"),("Garantia","10 anos")],
    sold_out=True)


# ── Collection page ───────────────────────────────────────────────────────────
print("\nCriando colecao-sets.html...")

def sw(img_id, hexc, label, url, active=False):
    act = " active" if active else ""
    brd = "border:1.5px solid #ccc;" if hexc in ("#FFFFFF","#FDF5E6") else "border:1.5px solid transparent;"
    return f'<span class="swatch{act}" style="background:{hexc};{brd}" onclick="swatchClick(event,this,\'{img_id}\',\'{url}\')" title="{label}"></span>'

def card(img_id, href, img_src, alt, name, sub, price, swatches, sold_out=False):
    badge = '<div class="oos-badge">ESGOTADO</div>' if sold_out else ""
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

cards.append(card("i_classico","set-azeite-vinagre-classico.html",
    C+"dwe9691760/images/80803020600003.jpg"+Q,"Set Azeite Vinagre Clássico",
    "Set Azeite &amp; Vinagre Cl&#225;ssico","Cer&#226;mica · 2 pe&#231;as","R$ 579,00",
    sw("i_classico","#FE5000","Laranja",C+"dwe9691760/images/80803020600003.jpg"+Q,True)))

cards.append(card("i_gift","set-caneca-100ml-gift-collection.html",
    C+"dw72d4c5ef/images/79114105219030-gift-collection.jpg"+Q,"Set Caneca Gift Collection",
    "Set Can&#233;ca 100ml Gift Collection","Cer&#226;mica · 6 pe&#231;as","R$ 639,00",
    sw("i_gift","#FF69B4","Multicor 2",C+"dw72d4c5ef/images/79114105219030-gift-collection.jpg"+Q,True)))

cards.append(card("i_peg","set-pegadores-de-silicone.html",
    C+"dw309d5819/images/produto-lecreuset-utensilio-pegadores-vermelho.png"+Q,"Set Pegadores de Silicone",
    "Set Pegadores de Silicone","Silicone · 5 cores","R$ 219,00",
    sw("i_peg","#C41E3A","Vermelho",C+"dw309d5819/images/produto-lecreuset-utensilio-pegadores-vermelho.png"+Q,True)+
    sw("i_peg","#FE5000","Laranja",C+"dwf8e4e3a6/images/produto-lecreuset-utensilio-pegadores-laranja.png"+Q)+
    sw("i_peg","#0066B2","Bleu Riviera",C+"dw48f6f78f/images/produto-lecreuset-utensilio-pegadores-bleu-riviera.png"+Q)+
    sw("i_peg","#F4A020","Nectar",C+"dw87039a69/images/produto-lecreuset-utensilio-pegadores-nectar.png"+Q)+
    sw("i_peg","#1a1a1a","Black Onyx",C+"dwc36d4bf5/images/produto-lecreuset-utensilio-pegadores-black-onyx.png"+Q)))

cards.append(card("i_alpine","set-4-utensilios-inox-alpine.html",
    C+"dw6d406278/images/conjunto-alpine-4-pecas-inox.png"+Q,"Set 4 Utensílios Inox Alpine",
    "Set 4 Utensilios Inox Alpine","A&#231;o Inox · 4 pe&#231;as + bolsa","R$ 1.429,00",
    sw("i_alpine","#1a1a1a","Black Onyx",C+"dw6d406278/images/conjunto-alpine-4-pecas-inox.png"+Q,True)))

cards.append(card("i_prot","set-3-protetores.html",
    C+"dw646049c0/images/set-protetor-para-panela%20(1).png"+Q,"Set 3 Protetores",
    "Set 3 Protetores","Feltro · 3 pe&#231;as","R$ 239,00",
    sw("i_prot","#FE5000","Laranja",C+"dw646049c0/images/set-protetor-para-panela%20(1).png"+Q,True)+
    sw("i_prot","#1a1a1a","Black Onyx",C+"dw236a5715/images/set-protetor-para-panela%20(2).png"+Q)))

cards.append(card("i_molho","set-molhos-condimentos.html",
    C+"dw05bb12d2/images/91027800010000.jpg"+Q,"Set Molhos Condimentos",
    "Set Molhos &amp; Condimentos","Cer&#226;mica · Servidor de molhos","R$ 449,00",
    sw("i_molho","#C41E3A","Vermelho",C+"dw05bb12d2/images/91027800010000.jpg"+Q,True)))

cards.append(card("i_tapas","set-3-mini-pratos-de-tapas.html",
    C+"dwb489c4a7/images/prato-triangulo-chambray.png"+Q,"Set 3 Mini Pratos de Tapas",
    "Set 3 Mini Pratos de Tapas","Cer&#226;mica · Chambray · 3 pe&#231;as","R$ 314,30",
    sw("i_tapas","#7BA3C8","Chambray",C+"dwb489c4a7/images/prato-triangulo-chambray.png"+Q,True)))

cards.append(card("i_petalas","set-5-mini-pratos-petalas.html",
    C+"dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png"+Q,"Set 5 Mini Pratos Pétalas",
    "Set 5 Mini Pratos P&#233;talas","Cer&#226;mica · Bluebell Purple · 5 pe&#231;as","R$ 659,00",
    sw("i_petalas","#7B68C8","Bluebell Purple",C+"dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png"+Q,True)))

cards.append(card("i_bowl","set-bowl-prato.html",
    C+"dw29ba298c/images/Set%20Bowl%20+%20Prato.png"+Q,"Set Bowl Prato",
    "Set Bowl &amp; Prato","Cer&#226;mica · Mauve Pink · 2 pe&#231;as","R$ 409,00",
    sw("i_bowl","#CF9BAE","Mauve Pink",C+"dw29ba298c/images/Set%20Bowl%20+%20Prato.png"+Q,True)))

cards.append(card("i_tampa","set-tampa-para-moedores-21cm.html",
    C+"dwf311dea5/images/produto-lecreuset-tampa-set-silicone.png"+Q,"Set Tampa para Moedores 21cm",
    "Set Tampa para Moedores 21cm","Silicone · 2 tampas","R$ 79,00",
    sw("i_tampa","#FE5000","Laranja",C+"dwf311dea5/images/produto-lecreuset-tampa-set-silicone.png"+Q,True)+
    sw("i_tampa","#007FFF","Azure",C+"dw454a79d3/images/kit-2-tampas-de-silicone-para-moedores-azure-blue.png"+Q)))

cards.append(card("i_sal","set-saleiro-pimenteiro.html",
    C+"dw4b44a6db/images/produto-lecreuset-saleiro-pimenteiro-laranja.png"+Q,"Set Saleiro Pimenteiro",
    "Set Saleiro &amp; Pimenteiro","Cer&#226;mica · 5 cores · 2 pe&#231;as","R$ 319,00",
    sw("i_sal","#FE5000","Laranja",C+"dw4b44a6db/images/produto-lecreuset-saleiro-pimenteiro-laranja.png"+Q,True)+
    sw("i_sal","#C41E3A","Vermelho",C+"dw2c3611db/images/produto-lecreuset-saleiro-pimenteiro-vermelho.png"+Q)+
    sw("i_sal","#8B9467","Artichaut",C+"dw756f8ec6/images/produto-lecreuset-saleiro-pimenteiro-artichaut.png"+Q)+
    sw("i_sal","#00B5CC","Caribe",C+"dwc39e9fcd/images/produto-lecreuset-saleiro-pimenteiro-caribe.png"+Q)+
    sw("i_sal","#FFFFFF","Branco",C+"dwb2c50bea/images/produto-lecreuset-saleiro-pimenteiro-branco.png"+Q)))

cards.append(card("i_can2","set-2-canecas-200ml-com-pires.html",
    C+"dw524d5e68/images/set-2-canecas-expresso-laranja.png"+Q,"Set 2 Canecas 200ml com Pires",
    "Set 2 Can&#233;cas 200ml com Pires","Cer&#226;mica · Laranja · 4 pe&#231;as","R$ 579,00",
    sw("i_can2","#FE5000","Laranja",C+"dw524d5e68/images/set-2-canecas-expresso-laranja.png"+Q,True)))

cards.append(card("i_chal","set-chaleira-demi-e-2-canecas-seattle.html",
    C+"dwcc27cd7f/images/set-chaleira-demi-&-2-canecas-seattle-laranja.png"+Q,"Set Chaleira Demi e 2 Canecas Seattle",
    "Set Chaleira Demi e 2 Can&#233;cas Seattle","1,1L + 2× 400ml","R$ 1.149,00",
    sw("i_chal","#FE5000","Laranja",C+"dwcc27cd7f/images/set-chaleira-demi-&-2-canecas-seattle-laranja.png"+Q,True)))

cards.append(card("i_sig","set-azeite-vinagre-signature.html",
    C+"dwc44577d9/images/set-azeite-vinagre.png"+Q,"Set Azeite Vinagre Signature",
    "Set Azeite &amp; Vinagre Signature","Cer&#226;mica · 2 pe&#231;as","R$ 629,00",
    sw("i_sig","#FDF5E6","Meringue",C+"dwc44577d9/images/set-azeite-vinagre.png"+Q,True)+
    sw("i_sig","#6D7C5E","Thyme",C+"dwc44577d9/images/set-azeite-vinagre.png"+Q)))

cards.append(card("i_velas","set-2-suportes-para-velas.html",
    C+"dw0867dbb8/images/suporte-para-vela-lecreuset2.png"+Q,"Set 2 Suportes para Velas",
    "Set 2 Suportes para Velas","Cer&#226;mica · 2 pe&#231;as","R$ 239,00",
    sw("i_velas","#C41E3A","Vermelho",C+"dw0867dbb8/images/suporte-para-vela-lecreuset2.png"+Q,True),
    sold_out=True))

cards.append(card("i_corac","bowl-coracao-650ml.html",
    C+"dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png"+Q,"Bowl Coração 650ml",
    "Bowl Cora&#231;&#227;o 650ml","Cer&#226;mica · Vermelho · 650ml","R$ 249,00",
    sw("i_corac","#C41E3A","Vermelho",C+"dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png"+Q,True),
    sold_out=True))

cards.append(card("i_pfundo","set-4-pratos-fundos-22cm.html",
    C+"dwe90d3019/images/produto-lecreuset-prato-fundo-chambray.png"+Q,"Set 4 Pratos Fundos 22cm",
    "Set 4 Pratos Fundos 22cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 869,00",
    sw("i_pfundo","#7BA3C8","Chambray",C+"dwe90d3019/images/produto-lecreuset-prato-fundo-chambray.png"+Q,True),
    sold_out=True))

cards.append(card("i_ovo","set-suporte-ovo-gift-collection.html",
    C+"dw95548df0/images/porta-ovo-gift-lecreuset2.png"+Q,"Set Suporte Ovo Gift Collection",
    "Set Suporte Ovo Gift Collection","Cer&#226;mica · 6 cores","R$ 409,00",
    sw("i_ovo","#FF69B4","Multicor 2",C+"dw95548df0/images/porta-ovo-gift-lecreuset2.png"+Q,True),
    sold_out=True))

cards.append(card("i_p22r","set-4-pratos-rasos-22cm.html",
    C+"dw56bd1039/images/produto-lecreuset-prato-set-chambray-22cm.png"+Q,"Set 4 Pratos Rasos 22cm",
    "Set 4 Pratos Rasos 22cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 869,00",
    sw("i_p22r","#7BA3C8","Chambray",C+"dw56bd1039/images/produto-lecreuset-prato-set-chambray-22cm.png"+Q,True),
    sold_out=True))

cards.append(card("i_p27r","set-4-pratos-rasos-27cm.html",
    C+"dw43149ac5/images/produto-lecreuset-prato-set-chambray-27cm.png"+Q,"Set 4 Pratos Rasos 27cm",
    "Set 4 Pratos Rasos 27cm","Cer&#226;mica · Chambray · 4 pe&#231;as","R$ 959,00",
    sw("i_p27r","#7BA3C8","Chambray",C+"dw43149ac5/images/produto-lecreuset-prato-set-chambray-27cm.png"+Q,True),
    sold_out=True))

N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Sets | Le Creuset Brasil</title>
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
    .cat-banner-wrap{{border-bottom:1px solid #e0e0e0;}}
    .cat-banner{{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr 1fr;min-height:260px;}}
    .cat-banner-left{{padding:28px 40px 28px 0;display:flex;flex-direction:column;justify-content:center;}}
    .cat-banner-crumb{{font-size:12px;color:#888;display:flex;gap:5px;align-items:center;margin-bottom:14px;}}
    .cat-banner-crumb a{{color:#888;}} .cat-banner-crumb a:hover{{color:#000;text-decoration:underline;}}
    .cat-banner-title{{font-size:26px;font-weight:700;color:#000;margin-bottom:12px;}}
    .cat-banner-features{{list-style:disc;padding-left:18px;}}
    .cat-banner-features li{{font-size:13px;color:#333;margin-bottom:4px;line-height:1.55;}}
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
    <div class="cat-banner-crumb">
      <a href="index.html">In&#237;cio</a><span style="color:#ccc;">/</span>
      <a href="colecao-acessorios.html">Acess&#243;rios</a><span style="color:#ccc;">/</span>
      <span style="color:#555;">Sets</span>
    </div>
    <h1 class="cat-banner-title">Sets</h1>
    <ul class="cat-banner-features">
      <li>Combina&#231;&#245;es perfeitas de pe&#231;as essenciais para o dia a dia;</li>
      <li>Sets de cer&#226;mica, silicone e inox para todas as ocasi&#245;es;</li>
      <li>Design ic&#244;nico Le Creuset com cores exclusivas;</li>
      <li>Ideais para presentear e expandir sua cole&#231;&#227;o;</li>
    </ul>
  </div>
  <div class="cat-banner-right">
    <img src="{BANNER}" alt="Sets Le Creuset"/>
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
        <label class="filter-option"><input type="checkbox"> Cer&#226;mica</label>
        <label class="filter-option"><input type="checkbox"> Silicone</label>
        <label class="filter-option"><input type="checkbox"> A&#231;o Inox</label>
        <label class="filter-option"><input type="checkbox"> Feltro</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Pre&#231;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> At&#233; R$ 250</label>
        <label class="filter-option"><input type="checkbox"> R$ 250 &#8211; R$ 500</label>
        <label class="filter-option"><input type="checkbox"> R$ 500 &#8211; R$ 1.000</label>
        <label class="filter-option"><input type="checkbox"> + R$ 1.000</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Uso
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Mesa Posta</label>
        <label class="filter-option"><input type="checkbox"> Cozinha</label>
        <label class="filter-option"><input type="checkbox"> Churrasco</label>
        <label class="filter-option"><input type="checkbox"> Bebidas</label>
        <label class="filter-option"><input type="checkbox"> Presentes</label>
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

with open(os.path.join(BASE, "colecao-sets.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"  Cole\u00e7\u00e3o: colecao-sets.html ({N} produtos)")
print("\nTudo pronto!")
