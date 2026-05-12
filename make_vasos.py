#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE   = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN    = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q      = "?sw=650&sh=650&sm=fit"
BANNER = "https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwe49b5872/category/cat_banners/banner-categoria-primavera.jpg"

WISH = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

COLOR_HEX = {
    "Vermelho":"#C41E3A","Laranja":"#FE5000","Black Onyx":"#1a1a1a",
    "Bleu Riviera":"#0066B2","Branco":"#FFFFFF","Meringue":"#FDF5E6",
    "Thyme":"#6D7C5E","Caribe":"#00B5CC","Nectar":"#F4A020",
    "Chambray":"#7BA3C8","Marseille":"#1B5E8D","Shell Pink":"#F4C2C2",
    "Azure":"#007FFF","Sea Salt":"#A8C5BB","Matte Black":"#222222",
    "Flint":"#8C8C8C","Shallot":"#D4956A","Multicor 2":"#FF69B4",
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
          <div class="mega-col"><div class="mega-col-title">Decora&#231;&#227;o</div>
            <a href="colecao-vasos.html">Vasos e Decora&#231;&#227;o</a>
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
        bord = "border:2px solid #ccc;" if hexc in ("#FFFFFF","#FDF5E6","#F4C2C2","#A8C5BB") else "border:2px solid transparent;"
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
  <a href="colecao-vasos.html">Vasos e Decora&#231;&#227;o</a><span>/</span>
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

make_product("vaso-1l.html",
    "Vaso 1L Le Creuset",
    "Vaso 1L", "Cer&#226;mica · 4 cores",
    "R$ 349,00", "ou 3x de R$ 116,33 sem juros",
    [("Vermelho","dwe0330bcd/images/vaso-1l-vermelho.png"),
     ("Laranja","dwed17b97e/images/vaso-1l-laranja.png"),
     ("Caribe","dwaa7c3183/images/vaso-1l-caribe.png"),
     ("Marseille","dw1bb094a6/images/vaso-1l-marseille.png")],
    ["Com uma borda de tr&#234;s an&#233;is, o Vaso 1L oferece uma forma refinada de iluminar as cozinhas durante todo o ano, com tamanho ideal para exibir flores frescas e ervas.",
     "O esmalte colorido resist&#234; a lascas e manchas. F&#225;cil de limpar e apto para lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Capacidade","1L"),
     ("Dimens&#245;es","12cm × 12cm × 15cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","China"),("Garantia","10 anos")])

make_product("vaso-flower.html",
    "Vaso Flower Le Creuset",
    "Vaso Flower", "Cer&#226;mica · Design floral",
    "R$ 359,00", "ou 3x de R$ 119,67 sem juros",
    [("Caribe","dwc118c901/images/vaso-flower-caribe%20(1).png"),
     ("Marseille","dwc118c901/images/vaso-flower-caribe%20(1).png"),
     ("Nectar","dwc118c901/images/vaso-flower-caribe%20(1).png"),
     ("Shell Pink","dwc118c901/images/vaso-flower-caribe%20(1).png")],
    ["O Vaso Flower Le Creuset apresenta bordas onduladas elegantes que adicionam alegria e charme a qualquer ambiente.",
     "Tamanho ideal para exibir flores frescas e ervas. O acabamento esmaltado vibrante resiste a lascas e manchas."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","9cm × 9cm × 16cm"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("vaso-ruffle-2l.html",
    "Vaso Ruffle 2L Le Creuset",
    "Vaso Ruffle 2L", "Cer&#226;mica · 2L",
    "R$ 909,00", "ou 9x de R$ 101,00 sem juros",
    [("Shell Pink","dw539ee9f4/images/vaso-ruffle-2l-shell-pink.png"),
     ("Branco","dwb1b55da4/images/vaso-ruffle-2l-branco.png")],
    ["O Vaso Ruffle 2L Le Creuset combina design elegante e funcionalidade para valorizar qualquer ambiente.",
     "Com acabamento esmaltado premium e formato generoso, &#233; perfeito para arranjos florais ou para decorar a mesa. Resist&#234;ncia superior a lascas e manchas."],
    [("Material","Cer&#226;mica"),("Capacidade","2L"),
     ("Cuidados","Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("porta-guardanapo-15cm.html",
    "Porta Guardanapo 15cm Le Creuset",
    "Porta Guardanapo 15cm", "Cer&#226;mica · M&#250;ltiplas cores",
    "R$ 289,00", "ou 2x de R$ 144,50 sem juros",
    [("Sea Salt","dw5e14ebc7/images/porta-guardanapo-15cm-seasalt%20(3).png"),
     ("Vermelho","dwd586ada1/images/porta-guardanapo-15cm-vermelho%20(2).png"),
     ("Azure","dwe2acc49b/images/porta-guardanapo-15cm-meringue%20(2).png")],
    ["O Porta Guardanapo 15cm Le Creuset combina design elegante, durabilidade e praticidade para a decora&#231;&#227;o da mesa.",
     "Feito de cer&#226;mica premium com superf&#237;cie esmaltada de f&#225;cil limpeza. Vai ao microondas, freezer e lava-lou&#231;as."],
    [("Material","Cer&#226;mica"),("Tamanho","15cm"),
     ("Cuidados","Microondas · Lava-lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("vaso-para-ervas-com-bandeja.html",
    "Vaso para Ervas com Bandeja Le Creuset",
    "Vaso para Ervas com Bandeja", "Cer&#226;mica · Com bandeja inclu&#237;da",
    "R$ 379,00", "ou 3x de R$ 126,33 sem juros",
    [("Bleu Riviera","dw2aef3428/images/vaso-bandeja-lifestyle.png")],
    ["O Vaso para Ervas com Bandeja Le Creuset traz frescor e tranquilidade aos ambientes. Ideal para exibir ervas frescas, flores e plantas na bancada, janela ou jardim.",
     "O esmalte vibrante &#233; f&#225;cil de limpar e resistente. Suporta temperaturas de -23&#176;C a +260&#176;C. Inclui bandeja para evitar vazamentos."],
    [("Material","Cer&#226;mica"),("Dimens&#245;es","14cm × 14cm × 12cm"),
     ("Inclui","Bandeja"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("dispenser-para-sabao-580ml.html",
    "Dispenser para Sabão 580ml Le Creuset",
    "Dispenser para Sab&#227;o 580ml", "Cer&#226;mica · 580ml",
    "R$ 439,00", "ou 4x de R$ 109,75 sem juros",
    [("Vermelho","dw550a8664/images/dispenser-para-sabao-580ml-1.png")],
    ["O Dispenser para Sab&#227;o 580ml Le Creuset &#233; feito em cer&#226;mica premium que combina durabilidade e sofistica&#231;&#227;o.",
     "Design elegante que valoriza qualquer bancada de cozinha. Pr&#225;tico e funcional para uso di&#225;rio."],
    [("Material","Cer&#226;mica"),("Capacidade","580ml"),
     ("Altura","24,5cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("porta-oleo-600ml.html",
    "Porta Óleo 600ml Le Creuset",
    "Porta &#211;leo 600ml", "Cer&#226;mica · 600ml",
    "R$ 299,00", "ou 2x de R$ 149,50 sem juros",
    [("Azure","dw4b9f9a78/images/porta-oleo-lecreuset-2.png"),
     ("Vermelho","dw958dd2ef/images/porta-oleo-lecreuset-1.png"),
     ("Branco","dw19258bcb/images/porta-oleo-lecreuset-3.png"),
     ("Meringue","dw635affe5/images/porta-oleo-lecreuset-6.png")],
    ["O Porta &#211;leo 600ml Le Creuset &#233; o acess&#243;rio ideal para manter azeite, vinagre e outros &#243;leos acess&#237;veis na bancada com muito estilo.",
     "Cer&#226;mica n&#227;o porosa e n&#227;o reativa que preserva o sabor e aroma dos &#243;leos. Superf&#237;cie esmaltada resistente a manchas e arranhões."],
    [("Material","Cer&#226;mica"),("Capacidade","600ml"),
     ("Dimens&#245;es","1,95cm × 1,95cm × 28,7cm"),("Cuidados","Lava-lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("miniatura-collection.html",
    "Miniatura Collection Le Creuset",
    "Miniatura Collection", "Cer&#226;mica · Edi&#231;&#227;o 100 anos",
    "R$ 989,00", "ou 9x de R$ 109,89 sem juros",
    [("Multicor 2","dw0a863909/images/miniatura-collection1.png")],
    ["A Miniatura Collection celebra os 100 anos da Le Creuset com pe&#231;as miniatura icônicas: Mini Cocotte, Panela Redonda Modern Heritage, Panela de Arroz e Travessa com Tampa.",
     "Feitas com esmalte dur&#225;vel e acabamento artesanal, s&#227;o ideais para decorar a mesa ou presentear. <strong>Aten&#231;&#227;o:</strong> uso decorativo apenas, n&#227;o para cozinhar."],
    [("Material","Cer&#226;mica"),("Cont&#233;m","4 miniaturas"),
     ("Dimens&#245;es","25cm × 19,3cm × 6,2cm"),("Uso","Decorativo"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])


# ── Collection page ───────────────────────────────────────────────────────────
print("\nCriando colecao-vasos.html...")

def sw(img_id, hexc, label, url, active=False):
    act = " active" if active else ""
    brd = "border:1.5px solid #ccc;" if hexc in ("#FFFFFF","#FDF5E6","#F4C2C2","#A8C5BB") else "border:1.5px solid transparent;"
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

cards.append(card("i_vaso1l","vaso-1l.html",
    C+"dwe0330bcd/images/vaso-1l-vermelho.png"+Q,"Vaso 1L",
    "Vaso 1L","Cer&#226;mica · 4 cores","R$ 349,00",
    sw("i_vaso1l","#C41E3A","Vermelho",C+"dwe0330bcd/images/vaso-1l-vermelho.png"+Q,True)+
    sw("i_vaso1l","#FE5000","Laranja",C+"dwed17b97e/images/vaso-1l-laranja.png"+Q)+
    sw("i_vaso1l","#00B5CC","Caribe",C+"dwaa7c3183/images/vaso-1l-caribe.png"+Q)+
    sw("i_vaso1l","#1B5E8D","Marseille",C+"dw1bb094a6/images/vaso-1l-marseille.png"+Q)))

cards.append(card("i_flower","vaso-flower.html",
    C+"dwc118c901/images/vaso-flower-caribe%20(1).png"+Q,"Vaso Flower",
    "Vaso Flower","Cer&#226;mica · Design floral","R$ 359,00",
    sw("i_flower","#00B5CC","Caribe",C+"dwc118c901/images/vaso-flower-caribe%20(1).png"+Q,True)+
    sw("i_flower","#1B5E8D","Marseille",C+"dwc118c901/images/vaso-flower-caribe%20(1).png"+Q)+
    sw("i_flower","#F4A020","Nectar",C+"dwc118c901/images/vaso-flower-caribe%20(1).png"+Q)+
    sw("i_flower","#F4C2C2","Shell Pink",C+"dwc118c901/images/vaso-flower-caribe%20(1).png"+Q)))

cards.append(card("i_ruffle","vaso-ruffle-2l.html",
    C+"dw539ee9f4/images/vaso-ruffle-2l-shell-pink.png"+Q,"Vaso Ruffle 2L",
    "Vaso Ruffle 2L","Cer&#226;mica · 2L","R$ 909,00",
    sw("i_ruffle","#F4C2C2","Shell Pink",C+"dw539ee9f4/images/vaso-ruffle-2l-shell-pink.png"+Q,True)+
    sw("i_ruffle","#FFFFFF","Branco",C+"dwb1b55da4/images/vaso-ruffle-2l-branco.png"+Q)))

cards.append(card("i_guard","porta-guardanapo-15cm.html",
    C+"dw5e14ebc7/images/porta-guardanapo-15cm-seasalt%20(3).png"+Q,"Porta Guardanapo 15cm",
    "Porta Guardanapo 15cm","Cer&#226;mica · M&#250;ltiplas cores","R$ 289,00",
    sw("i_guard","#A8C5BB","Sea Salt",C+"dw5e14ebc7/images/porta-guardanapo-15cm-seasalt%20(3).png"+Q,True)+
    sw("i_guard","#C41E3A","Vermelho",C+"dwd586ada1/images/porta-guardanapo-15cm-vermelho%20(2).png"+Q)+
    sw("i_guard","#007FFF","Azure",C+"dwe2acc49b/images/porta-guardanapo-15cm-meringue%20(2).png"+Q)))

cards.append(card("i_ervas","vaso-para-ervas-com-bandeja.html",
    C+"dw2aef3428/images/vaso-bandeja-lifestyle.png"+Q,"Vaso para Ervas com Bandeja",
    "Vaso para Ervas com Bandeja","Cer&#226;mica · Com bandeja","R$ 379,00",
    sw("i_ervas","#0066B2","Bleu Riviera",C+"dw2aef3428/images/vaso-bandeja-lifestyle.png"+Q,True)))

cards.append(card("i_disp","dispenser-para-sabao-580ml.html",
    C+"dw550a8664/images/dispenser-para-sabao-580ml-1.png"+Q,"Dispenser para Sabão 580ml",
    "Dispenser para Sab&#227;o 580ml","Cer&#226;mica · 580ml","R$ 439,00",
    sw("i_disp","#C41E3A","Vermelho",C+"dw550a8664/images/dispenser-para-sabao-580ml-1.png"+Q,True)))

cards.append(card("i_oleo","porta-oleo-600ml.html",
    C+"dw4b9f9a78/images/porta-oleo-lecreuset-2.png"+Q,"Porta Óleo 600ml",
    "Porta &#211;leo 600ml","Cer&#226;mica · 4 cores","R$ 299,00",
    sw("i_oleo","#007FFF","Azure",C+"dw4b9f9a78/images/porta-oleo-lecreuset-2.png"+Q,True)+
    sw("i_oleo","#C41E3A","Vermelho",C+"dw958dd2ef/images/porta-oleo-lecreuset-1.png"+Q)+
    sw("i_oleo","#FFFFFF","Branco",C+"dw19258bcb/images/porta-oleo-lecreuset-3.png"+Q)+
    sw("i_oleo","#FDF5E6","Meringue",C+"dw635affe5/images/porta-oleo-lecreuset-6.png"+Q)))

cards.append(card("i_mini","miniatura-collection.html",
    C+"dw0a863909/images/miniatura-collection1.png"+Q,"Miniatura Collection",
    "Miniatura Collection","Cer&#226;mica · Edi&#231;&#227;o 100 anos","R$ 989,00",
    sw("i_mini","#FF69B4","Multicor 2",C+"dw0a863909/images/miniatura-collection1.png"+Q,True)))

cards.append(card("i_velas2","set-2-suportes-para-velas.html",
    C+"dw0867dbb8/images/suporte-para-vela-lecreuset2.png"+Q,"Set 2 Suportes para Velas",
    "Set 2 Suportes para Velas","Cer&#226;mica · 2 pe&#231;as","R$ 239,00",
    sw("i_velas2","#C41E3A","Vermelho",C+"dw0867dbb8/images/suporte-para-vela-lecreuset2.png"+Q,True),
    sold_out=True))

N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Vasos e Decoração | Le Creuset Brasil</title>
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
    .cat-banner{{position:relative;width:100%;overflow:hidden;max-height:420px;}}
    .cat-banner img{{width:100%;height:100%;object-fit:cover;object-position:center;display:block;max-height:420px;}}
    .cat-banner-left{{max-width:1400px;margin:0 auto;padding:16px 24px 12px;}}
    .cat-banner-crumb{{font-size:12px;color:#888;display:flex;gap:5px;align-items:center;margin-bottom:8px;}}
    .cat-banner-crumb a{{color:#888;}} .cat-banner-crumb a:hover{{color:#000;text-decoration:underline;}}
    .cat-banner-title{{font-size:26px;font-weight:700;color:#000;margin-bottom:10px;}}
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
    <img src="{BANNER}" alt="Vasos e Decoração Le Creuset"/>
  </div>
  <div class="cat-banner-left">
    <div class="cat-banner-crumb">
      <a href="index.html">In&#237;cio</a><span>/</span>
      <span>Vasos e Decora&#231;&#227;o</span>
    </div>
    <h1 class="cat-banner-title">Vasos e Decora&#231;&#227;o</h1>
  </div>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Tipo
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Vasos</label>
        <label class="filter-option"><input type="checkbox"> Porta &#211;leo</label>
        <label class="filter-option"><input type="checkbox"> Dispensers</label>
        <label class="filter-option"><input type="checkbox"> Porta Guardanapo</label>
        <label class="filter-option"><input type="checkbox"> Decora&#231;&#227;o</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Pre&#231;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> At&#233; R$ 300</label>
        <label class="filter-option"><input type="checkbox"> R$ 300 &#8211; R$ 500</label>
        <label class="filter-option"><input type="checkbox"> + R$ 500</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Cor
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Vermelho</label>
        <label class="filter-option"><input type="checkbox"> Laranja</label>
        <label class="filter-option"><input type="checkbox"> Caribe</label>
        <label class="filter-option"><input type="checkbox"> Bleu Riviera</label>
        <label class="filter-option"><input type="checkbox"> Shell Pink</label>
        <label class="filter-option"><input type="checkbox"> Sea Salt</label>
        <label class="filter-option"><input type="checkbox"> Branco</label>
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

with open(os.path.join(BASE, "colecao-vasos.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"  Cole\u00e7\u00e3o: colecao-vasos.html ({N} produtos)")
print("\nTudo pronto!")
