#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN  = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q    = "?sw=650&sh=650&sm=fit"
BANNER = "https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dw58a9ab0b/category/cat_banners/banner_categoria_acessorios_de_vinho.jpg"
WISH = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

COLOR_HEX = {
    "Vermelho":"#C41E3A","Laranja":"#FE5000","Black Onyx":"#1a1a1a",
    "Bleu Riviera":"#0066B2","Matte Black":"#222222","Inox":"#B0B0B0",
    "Madeira":"#8B5E3C","Preto":"#1a1a1a",
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
    .btn-cart:hover{background:#222;}
    .btn-wishlist{display:block;width:100%;background:#fff;color:#000;border:2px solid #000;padding:14px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;}
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


def make_product(filename, title, name, sub, price, install, colors_imgs, desc, specs):
    first_c, first_img = colors_imgs[0]
    swatches = ""
    for i, (cname, cimg) in enumerate(colors_imgs):
        url = CDN + cimg + Q
        hexc = COLOR_HEX.get(cname, "#888")
        bord = "border:2px solid #ccc;" if hexc in ("#FFFFFF","#F5F5DC","#B0B0B0") else "border:2px solid transparent;"
        act = " active" if i == 0 else ""
        swatches += f'<span class="color-swatch{act}" style="background:{hexc};{bord}" title="{cname}" onclick="selectColor(this,\'{cname}\',\'{url}\')"></span>\n      '

    specs_html = "".join(f"<tr><td class='sk'>{k}:</td><td class='sv'>{v}</td></tr>" for k,v in specs)
    desc_html  = "".join(f"<p>{p}</p>" for p in desc)
    first_url  = CDN + first_img + Q

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
  <a href="colecao-acessorios-de-vinhos.html">Acess&#243;rios de Vinhos</a><span>/</span>
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
    <h1 class="product-name">{name}</h1>
    <div class="product-sub">{sub}</div>
    <div class="product-price">{price}</div>
    <div class="product-installment">{install}</div>
    <div class="color-selector">
      <div class="color-label">Cor: <strong id="colorName">{first_c}</strong></div>
      <div class="color-swatches">{swatches.strip()}</div>
    </div>
    <button class="btn-cart">Adicionar ao Carrinho</button>
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


# ── 7 product pages ──────────────────────────────────────────────────────────

make_product("saca-rolhas-modelo-garcom.html","Saca Rolhas Modelo Garçom Le Creuset",
    "Saca Rolhas Modelo Gar&#231;om","A&#231;o Inox com cabo ABS","R$ 299,00","ou 3x de R$ 99,67 sem juros",
    [("Black Onyx","dwb6c04dfb/images/844x660-produto-lecreuset-black.png")],
    ["O Saca Rolhas Modelo Gar&#231;om Le Creuset possui design em dois est&#225;gios que maximiza a alavancagem para remover a rolha suavemente, sem esfor&#231;o.",
     "Inclui cortador de papel de aluminio integrado e abridor de garrafas. Remove rolhas longas e fr&#225;geis verticalmente sem danific&#225;-las."],
    [("Material","A&#231;o Inox + cabo ABS"),("Dimens&#245;es","12cm × 3cm × 2,1cm"),
     ("Inclui","Cortador de papel + abridor"),("Origem","China"),("Garantia","5 anos")])

make_product("cooler-sleeve.html","Cooler Sleeve Le Creuset",
    "Cooler Sleeve","Gel refrigerante","R$ 309,00","ou 3x de R$ 103,00 sem juros",
    [("Laranja","dw821097d3/images/59142014306068.jpg")],
    ["O Cooler Sleeve Le Creuset resfria vinho em poucos minutos e mant&#233;m a temperatura ideal por horas. Basta guardar no freezer para ativar o gel refrigerante.",
     "Resfria at&#233; a temperatura de servi&#231;o em 15 minutos e mant&#233;m a temperatura &#243;tima por 45 minutos. Compativel com garrafas de vinho, cerveja e refri."],
    [("Material","Gel refrigerante"),("Tempo de resfriamento","~15 minutos"),
     ("Manuten&#231;&#227;o da temperatura","~45 minutos"),("Limpeza","&#192; m&#227;o"),("Garantia","5 anos")])

make_product("saca-rolhas-tm100.html","Saca-Rolhas TM100 Onyx Le Creuset",
    "Saca-Rolhas TM100","A&#231;o Inox · Black Onyx","R$ 309,00","ou 3x de R$ 103,00 sem juros",
    [("Black Onyx","dw0b39468d/images/produto-lecreuset-saca-rolhas-tm100.png")],
    ["O Saca-Rolhas TM100 Le Creuset combina design sofisticado com mecanismo de alta precis&#227;o. O cabo ergon&#244;mico em Black Onyx oferece grip confort&#225;vel.",
     "Perfeito para abrir qualquer tipo de rolha com m&#237;nimo esfor&#231;o. Um acess&#243;rio essencial para amantes de vinho."],
    [("Material","A&#231;o Inox + cabo polim&#233;rico"),("Cor","Black Onyx"),
     ("Origem","China"),("Garantia","5 anos")])

make_product("abridor-de-champanhe.html","Abridor de Champanhe Le Creuset",
    "Abridor de Champanhe","A&#231;o Inox","R$ 469,00","ou 4x de R$ 117,25 sem juros",
    [("Inox","dwaf0c3f27/images/abridor_champagne_lecreuset_2.jpg")],
    ["O Abridor de Champanhe Le Creuset remove a gaiola e a rolha de garrafas espumantes com seguran&#231;a e precis&#227;o. Design sofisticado em a&#231;o inox polido.",
     "Ideal para espumantes, champanhe e prosecco. Mantém o controle total durante a abertura, evitando acidentes."],
    [("Material","A&#231;o Inox"),("Uso","Espumantes e Champanhe"),
     ("Origem","Europa"),("Garantia","5 anos")])

make_product("saca-rolhas-garcom-aco-inox.html","Saca-Rolhas Garçom Aço Inox WT-110 Le Creuset",
    "Saca-Rolhas Gar&#231;om A&#231;o Inox WT-110","A&#231;o Inox polido","R$ 309,00","ou 3x de R$ 103,00 sem juros",
    [("Inox","dw79ccdc0b/images/59814017808074-saca-rolha.png")],
    ["O Saca-Rolhas Gar&#231;om WT-110 em A&#231;o Inox Le Creuset &#233; o parceiro ideal para sommeli&#234;rs e amantes de vinho. Design cl&#225;ssico de gar&#231;om em a&#231;o inox polido.",
     "Inclui espiral de a&#231;o inox, alavanca de duplo est&#225;gio e cortador de papel integrado. Resistente e duradouro."],
    [("Material","A&#231;o Inox"),("Mecanismo","Dupla alavanca"),
     ("Inclui","Cortador de papel integrado"),("Origem","Europa"),("Garantia","5 anos")])

make_product("lm-250.html","LM 250 Abridor de Alavanca Le Creuset",
    "LM 250 Abridor de Alavanca","A&#231;o Inox · Premium","R$ 1.729,00","ou 10x de R$ 172,90 sem juros",
    [("Inox","dwc13fc613/images/59058013009410.jpg")],
    ["O LM 250 &#233; o abridor de vinho de alavanca premium da Le Creuset, com mecanismo de precis&#227;o que remove qualquer tipo de rolha sem esfor&#231;o.",
     "Fixado na parede ou em bancada, oferece abertura elegante e eficiente. Constru&#231;&#227;o robusta em a&#231;o inox para uso intenso e duradouro."],
    [("Material","A&#231;o Inox premium"),("Tipo","Abridor de alavanca fixo"),
     ("Instala&#231;&#227;o","Parede ou bancada"),("Origem","Portug"), ("Garantia","10 anos")])

make_product("kit-bomba-vacuo.html","Kit Bomba Vácuo Le Creuset",
    "Kit Bomba V&#225;cuo","Pl&#225;stico ABS · 2 rolhas inclu&#237;das","R$ 239,00","ou 3x de R$ 79,67 sem juros",
    [("Preto","dw706b6ca5/images/49200000000000.jpg")],
    ["O Kit Bomba V&#225;cuo Le Creuset remove o ar da garrafa de vinho aberta, preservando o sabor e aroma por at&#233; 5 dias.",
     "O kit inclui a bomba manual e 2 rolhas de silicone reutiliz&#225;veis. Simples de usar e indispens&#225;vel para quem aprecia vinho."],
    [("Material","Pl&#225;stico ABS + Silicone"),("Inclui","Bomba + 2 rolhas"),
     ("Conserva&#231;&#227;o","At&#233; 5 dias"),("Limpeza","&#192; m&#227;o"),("Garantia","2 anos")])


# ── Collection page ───────────────────────────────────────────────────────────
print("\nCriando colecao-acessorios-de-vinhos.html...")

def sw(img_id, hexc, label, url, active=False):
    act = " active" if active else ""
    brd = "border:1.5px solid #ccc;" if hexc in ("#FFFFFF","#B0B0B0") else "border:1.5px solid transparent;"
    return f'<span class="swatch{act}" style="background:{hexc};{brd}" onclick="swatchClick(event,this,\'{img_id}\',\'{url}\')" title="{label}"></span>'

def card(img_id, href, img_src, alt, name, sub, price, swatches):
    return f"""    <div class="product-card">
      <a href="{href}">
        <div class="product-card-img">
          <img id="{img_id}" src="{img_src}" alt="{alt}"/>
          <div class="product-wishlist">{WISH}</div>
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

cards.append(card("i_garcom","saca-rolhas-modelo-garcom.html",
    C+"dwb6c04dfb/images/844x660-produto-lecreuset-black.png"+Q,"Saca Rolhas Modelo Garçom",
    "Saca Rolhas Modelo Gar&#231;om","A&#231;o Inox · Dupla Alavanca","R$ 299,00",
    sw("i_garcom","#1a1a1a","Black Onyx",C+"dwb6c04dfb/images/844x660-produto-lecreuset-black.png"+Q,True)))

cards.append(card("i_cooler","cooler-sleeve.html",
    C+"dw821097d3/images/59142014306068.jpg"+Q,"Cooler Sleeve",
    "Cooler Sleeve","Gel Refrigerante · M&#250;ltiplas Cores","R$ 309,00",
    sw("i_cooler","#FE5000","Laranja",C+"dw821097d3/images/59142014306068.jpg"+Q,True)))

cards.append(card("i_tm100","saca-rolhas-tm100.html",
    C+"dw0b39468d/images/produto-lecreuset-saca-rolhas-tm100.png"+Q,"Saca-Rolhas TM100",
    "Saca-Rolhas TM100","A&#231;o Inox · Black Onyx","R$ 309,00",
    sw("i_tm100","#1a1a1a","Black Onyx",C+"dw0b39468d/images/produto-lecreuset-saca-rolhas-tm100.png"+Q,True)))

cards.append(card("i_champagne","abridor-de-champanhe.html",
    C+"dwaf0c3f27/images/abridor_champagne_lecreuset_2.jpg"+Q,"Abridor de Champanhe",
    "Abridor de Champanhe","A&#231;o Inox","R$ 469,00",
    sw("i_champagne","#B0B0B0","Inox",C+"dwaf0c3f27/images/abridor_champagne_lecreuset_2.jpg"+Q,True)))

cards.append(card("i_wt110m","saca-rolhas-garcon-wt110.html",
    C+"dw03905133/images/saca-rolhas-efeito-garcom-madeira-lecreuset.1.jpg"+Q,"Saca Rolhas Wt-110 Madeira",
    "Saca Rolhas WT-110 Madeira","A&#231;o Inox + Madeira","R$ 309,00",
    sw("i_wt110m","#8B5E3C","Madeira",C+"dw03905133/images/saca-rolhas-efeito-garcom-madeira-lecreuset.1.jpg"+Q,True)))

cards.append(card("i_wt110i","saca-rolhas-garcom-aco-inox.html",
    C+"dw79ccdc0b/images/59814017808074-saca-rolha.png"+Q,"Saca-Rolhas Garçom Aço Inox WT-110",
    "Saca-Rolhas Gar&#231;om A&#231;o Inox WT-110","A&#231;o Inox polido","R$ 309,00",
    sw("i_wt110i","#B0B0B0","Inox",C+"dw79ccdc0b/images/59814017808074-saca-rolha.png"+Q,True)))

cards.append(card("i_lm250","lm-250.html",
    C+"dwc13fc613/images/59058013009410.jpg"+Q,"LM 250 Abridor de Alavanca",
    "LM 250 Abridor de Alavanca","A&#231;o Inox Premium","R$ 1.729,00",
    sw("i_lm250","#B0B0B0","Inox",C+"dwc13fc613/images/59058013009410.jpg"+Q,True)))

cards.append(card("i_bomba","kit-bomba-vacuo.html",
    C+"dw706b6ca5/images/49200000000000.jpg"+Q,"Kit Bomba Vácuo",
    "Kit Bomba V&#225;cuo","Inclui 2 rolhas de silicone","R$ 239,00",
    sw("i_bomba","#222222","Preto",C+"dw706b6ca5/images/49200000000000.jpg"+Q,True)))

N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Acessórios de Vinhos | Le Creuset Brasil</title>
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
    .cat-banner-right img{{width:100%;height:100%;object-fit:cover;display:block;}}
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
      <span style="color:#555;">Acess&#243;rios de Vinhos</span>
    </div>
    <h1 class="cat-banner-title">Acess&#243;rios de Vinhos</h1>
    <ul class="cat-banner-features">
      <li>Saca-rolhas de alta precis&#227;o com mecanismo de dupla alavanca;</li>
      <li>Cooler Sleeve com gel refrigerante &#8212; resfria em 15 minutos;</li>
      <li>Bomba de v&#225;cuo para conservar o vinho por at&#233; 5 dias;</li>
      <li>Design elegante e materiais de alta qualidade Le Creuset;</li>
    </ul>
  </div>
  <div class="cat-banner-right">
    <img src="{BANNER}" alt="Acessórios de Vinhos Le Creuset"/>
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
        <label class="filter-option"><input type="checkbox"> Saca-Rolhas</label>
        <label class="filter-option"><input type="checkbox"> Abridores</label>
        <label class="filter-option"><input type="checkbox"> Cooler &amp; Conserva&#231;&#227;o</label>
        <label class="filter-option"><input type="checkbox"> Kits e Acess&#243;rios</label>
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
      <div class="filter-header open" onclick="toggleFilter(this)">Material
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> A&#231;o Inox</label>
        <label class="filter-option"><input type="checkbox"> ABS + Inox</label>
        <label class="filter-option"><input type="checkbox"> Madeira</label>
        <label class="filter-option"><input type="checkbox"> Silicone / Gel</label>
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
function toggleFilter(h){{h.classList.toggle('open');h.nextElementSibling.classList.toggle('open');}}
function swatchClick(e,s,imgId,src){{
  e.preventDefault();e.stopPropagation();
  s.parentElement.querySelectorAll('.swatch').forEach(x=>x.classList.remove('active'));
  s.classList.add('active');
  var el=document.getElementById(imgId);if(el)el.src=src;
}}
</script>
</body></html>"""

with open(os.path.join(BASE, "colecao-acessorios-de-vinhos.html"), "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"  Coleção: colecao-acessorios-de-vinhos.html ({N} produtos)")
print("\nTudo pronto!")
