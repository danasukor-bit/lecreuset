#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"

# hue-rotate filters to simulate colors from vermelho base
HUE = {
    "Vermelho": "none",
    "Laranja": "hue-rotate(-30deg) saturate(1.4)",
    "Bleu Riviera": "hue-rotate(200deg) saturate(1.3)",
    "Azure": "hue-rotate(195deg) saturate(1.5)",
    "Meringue": "saturate(0.05) brightness(1.5)",
    "Artichaut": "hue-rotate(90deg) saturate(0.7) brightness(0.7)",
    "Branco": "saturate(0) brightness(2)",
    "Flint": "saturate(0.1) brightness(0.7)",
    "Nectar": "hue-rotate(-20deg) saturate(1.2) brightness(1.1)",
    "Black Onyx": "saturate(0) brightness(0.1)",
    "Shell Pink": "hue-rotate(-10deg) saturate(0.4) brightness(1.4)",
    "Thyme": "hue-rotate(85deg) saturate(0.8) brightness(0.75)",
    "Shallot": "hue-rotate(-5deg) saturate(0.6) brightness(1.3)",
    "Bluebell Purple": "hue-rotate(240deg) saturate(0.8) brightness(0.9)",
}
COLOR_HEX = {
    "Vermelho": "#C41E3A", "Laranja": "#FE5000", "Bleu Riviera": "#0066B2",
    "Azure": "#007FFF", "Meringue": "#F5F5DC", "Artichaut": "#4B5320",
    "Branco": "#FFFFFF", "Flint": "#708090", "Nectar": "#FFB347",
    "Black Onyx": "#1a1a1a", "Shell Pink": "#FFB6C1", "Thyme": "#6B8E23",
    "Shallot": "#E8A0A0", "Bluebell Purple": "#8B73C4",
}

HEADER = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{title} | Le Creuset Brasil</title>
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
    .breadcrumb{{max-width:1400px;margin:0 auto;padding:16px 24px 0;font-size:12px;color:#888;display:flex;gap:5px;align-items:center;}}
    .breadcrumb a{{color:#888;}} .breadcrumb a:hover{{color:#000;text-decoration:underline;}}
    .product-wrap{{max-width:1400px;margin:0 auto;padding:24px 24px 0;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;}}
    .product-img-wrap{{position:sticky;top:80px;}}
    .product-main-img{{width:100%;aspect-ratio:1;border:1px solid #f0f0f0;display:flex;align-items:center;justify-content:center;background:#fafafa;overflow:hidden;}}
    .product-main-img img{{width:100%;height:100%;object-fit:contain;padding:40px;transition:filter 0.3s;}}
    .product-info{{padding-top:8px;}}
    .product-brand{{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#888;margin-bottom:6px;}}
    .product-name{{font-size:28px;font-weight:800;line-height:1.2;margin-bottom:8px;}}
    .product-sub{{font-size:14px;color:#555;margin-bottom:20px;}}
    .product-price{{font-size:26px;font-weight:800;color:#000;margin-bottom:4px;}}
    .product-installment{{font-size:13px;color:#666;margin-bottom:24px;}}
    .color-selector{{margin-bottom:28px;}}
    .color-label{{font-size:13px;color:#333;margin-bottom:12px;font-weight:600;}}
    .color-label strong{{font-weight:800;}}
    .color-swatches{{display:flex;gap:10px;flex-wrap:wrap;}}
    .color-swatch{{width:32px;height:32px;border-radius:50%;cursor:pointer;display:inline-block;transition:transform 0.15s,box-shadow 0.15s;border:2px solid transparent;}}
    .color-swatch:hover{{transform:scale(1.12);}}
    .color-swatch.active{{box-shadow:0 0 0 2px #fff,0 0 0 4px #000;}}
    .btn-cart{{display:block;width:100%;background:#000;color:#fff;border:none;padding:16px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;margin-bottom:12px;}}
    .btn-cart:hover{{background:#222;}}
    .btn-wishlist{{display:block;width:100%;background:#fff;color:#000;border:2px solid #000;padding:14px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;}}
    .desc-specs-wrap{{max-width:1400px;margin:40px auto 0;padding:48px 24px 80px;border-top:1px solid #e5e5e5;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;}}
    .section-title{{font-size:28px;font-weight:300;margin-bottom:20px;letter-spacing:-0.3px;}}
    .desc-text{{font-size:14px;line-height:1.8;color:#333;}}
    .desc-text p{{margin-bottom:12px;}}
    .specs-table{{width:100%;border-collapse:collapse;}}
    .specs-table tr{{border-bottom:1px solid #e5e5e5;}}
    .specs-table tr:first-child{{border-top:1px solid #e5e5e5;}}
    .specs-table td{{padding:13px 0;font-size:14px;}}
    .specs-table td.sk{{color:#555;width:48%;}}
    .specs-table td.sv{{color:#000;}}
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
<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    <nav>
      <ul class="nav-list">
        <li>
          <a href="#">Comprar</a>
          <div class="mega-menu">
            <div class="mega-inner">
              <div class="mega-col">
                <div class="mega-col-title">Cozinhar</div>
                <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
                <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
                <a href="colecao-cacarolas.html">Ca&#231;arolas</a>
                <a href="colecao-antiaderente.html">Antiaderente</a>
                <a href="colecao-acessorios.html">Acess&#243;rios</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Assar</div>
                <a href="colecao-assadeiras-travessas.html">Assadeiras e Travessas</a>
                <a href="colecao-formas-metal-bakeware.html">Formas Metal Bakeware</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Acess&#243;rios</div>
                <a href="colecao-utensilios.html">Utensilios</a>
                <a href="colecao-utensilios-madeira.html">Utensilios de Madeira</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Cole&#231;&#245;es</div>
                <a href="colecao-bleu-riviera.html">Bleu Riviera</a>
                <a href="colecao-lancamentos.html">Lan&#231;amentos</a>
                <a href="colecao-best-sellers.html">Best-Sellers</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Nossas Cores</div>
                <a href="colecao-nossas-cores.html">Ver Todas as Cores</a>
              </div>
            </div>
          </div>
        </li>
        <li class="highlight"><a href="colecao-pascoa.html">P&#225;scoa</a></li>
        <li><a href="colecao-ofertas.html">Ofertas</a></li>
        <li class="blue"><a href="colecao-bleu-riviera.html">Bleu Riviera</a></li>
        <li><a href="colecao-lancamentos.html">Lan&#231;amentos</a></li>
        <li><a href="colecao-ferro-fundido.html">Ferro Fundido</a></li>
        <li><a href="colecao-ceramica.html">Cer&#226;mica</a></li>
        <li><a href="colecao-best-sellers.html">Best-Sellers</a></li>
      </ul>
    </nav>
    <div class="header-icons">
      <div class="search-box">
        <input type="text" placeholder="Buscar..."/>
        <button><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
      </div>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Entrar</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Sacola</span></a>
    </div>
  </div>
</header>
"""

FOOTER = """<footer>
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
        <li><a href="colecao-utensilios-madeira.html">Utensilios de Madeira</a></li>
      </ul></div>
      <div class="footer-col"><h4>Atendimento</h4><ul>
        <li><a href="#">Central de Ajuda</a></li>
        <li><a href="#">Rastrear Pedido</a></li>
        <li><a href="#">Trocas e Devolu&#231;&#245;es</a></li>
      </ul></div>
      <div class="footer-col"><h4>Empresa</h4><ul>
        <li><a href="#">Sobre N&#243;s</a></li>
        <li><a href="#">Blog</a></li>
      </ul></div>
      <div class="footer-col"><h4>Legal</h4><ul>
        <li><a href="#">Privacidade</a></li>
        <li><a href="#">Termos</a></li>
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
</footer>
<script>
function selectColor(el,name,src,filterVal){
  el.parentElement.querySelectorAll('.color-swatch').forEach(x=>x.classList.remove('active'));
  el.classList.add('active');
  var img=document.getElementById('mainImgEl');
  if(src) img.src=src;
  img.style.filter=filterVal||'none';
  document.getElementById('colorName').textContent=name;
}
</script>
</body>
</html>"""


def make_swatches(colors, base_img, specific_imgs=None):
    """Generate swatch HTML. specific_imgs is dict color->url (optional)."""
    html = ""
    for i, color in enumerate(colors):
        img_url = (specific_imgs or {}).get(color, base_img)
        filt = HUE.get(color, "none")
        hex_c = COLOR_HEX.get(color, "#888")
        active = " active" if i == 0 else ""
        # first color: use img_url directly (no filter if it's a specific img)
        if specific_imgs and color in specific_imgs:
            filter_arg = "none"
        else:
            filter_arg = filt
        onclick = f"selectColor(this,'{color}','{img_url}','{filter_arg}')"
        border = "border:2px solid #ccc;" if hex_c in ("#FFFFFF", "#F5F5DC") else ""
        html += f'<span class="color-swatch{active}" style="background:{hex_c};{border}" title="{color}" onclick="{onclick}"></span>\n      '
    return html.strip()


def make_page(filename, title, breadcrumb_cat, breadcrumb_cat_url, name, sub, price,
              installment, colors, base_img, specific_imgs, description, specs_rows,
              default_filter="none"):
    first_color = colors[0]
    first_img = (specific_imgs or {}).get(first_color, base_img)
    first_filter = "none" if (specific_imgs and first_color in specific_imgs) else HUE.get(first_color, "none")

    swatches = make_swatches(colors, base_img, specific_imgs)
    specs_html = ""
    for k, v in specs_rows:
        specs_html += f"<tr><td class='sk'>{k}:</td><td class='sv'>{v}</td></tr>"

    desc_paras = "".join(f"<p>{p}</p>" for p in description)

    html = HEADER.format(title=title)
    html += f"""<div class="breadcrumb">
  <a href="index.html">In&#237;cio</a><span>/</span>
  <a href="{breadcrumb_cat_url}">{breadcrumb_cat}</a><span>/</span>
  <span>{name}</span>
</div>
<div class="product-wrap">
  <div class="product-img-wrap">
    <div class="product-main-img">
      <img id="mainImgEl" src="{first_img}?sw=650&sh=650&sm=fit" alt="{name}" style="filter:{first_filter};"/>
    </div>
  </div>
  <div class="product-info">
    <div class="product-brand">Le Creuset</div>
    <h1 class="product-name">{name}</h1>
    <div class="product-sub">{sub}</div>
    <div class="product-price">{price}</div>
    <div class="product-installment">{installment}</div>
    <div class="color-selector">
      <div class="color-label">Cor: <strong id="colorName">{first_color}</strong></div>
      <div class="color-swatches">
      {swatches}
      </div>
    </div>
    <button class="btn-cart">Adicionar ao Carrinho</button>
    <button class="btn-wishlist">&#9825; Lista de Desejos</button>
  </div>
</div>
<div class="desc-specs-wrap">
  <div>
    <h2 class="section-title">Descri&#231;&#227;o</h2>
    <div class="desc-text">{desc_paras}</div>
  </div>
  <div>
    <h2 class="section-title">Especifica&#231;&#245;es</h2>
    <table class="specs-table"><tbody>{specs_html}</tbody></table>
  </div>
</div>
"""
    html += FOOTER

    path = os.path.join(BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Criado: {filename}")


# ── 1. Moedor de Sal 21cm ────────────────────────────────────────────────────
COLORS_21 = ["Vermelho","Laranja","Bleu Riviera","Azure","Meringue","Artichaut",
             "Branco","Flint","Nectar","Black Onyx","Shell Pink","Thyme"]
IMG_21_SAL = CDN + "dw7138e9be/images/produto-lecreuset-moedores-vermelho.png"

make_page(
    filename="moedor-sal-21cm.html",
    title="Moedor de Sal 21cm Le Creuset",
    breadcrumb_cat="Acess&#243;rios",
    breadcrumb_cat_url="colecao-acessorios.html",
    name="Moedor de Sal 21cm",
    sub="Pl&#225;stico ABS com mecanismo cer&#226;mico",
    price="R$ 369,00",
    installment="ou 3x de R$ 123,00 sem juros",
    colors=COLORS_21,
    base_img=IMG_21_SAL,
    specific_imgs=None,
    description=[
        "O Moedor de Sal 21cm Le Creuset combina design ic&#244;nico e tecnologia de moagem de prec&#227;o. O exterior em pl&#225;stico ABS resistente &#233; disponivel em diversas cores da paleta Le Creuset.",
        "O mecanismo cer&#226;mico ajust&#225;vel permite controlar a granulometria do sal, do fino ao grosso. N&#227;o absorve odores e &#233; f&#225;cil de limpar."
    ],
    specs_rows=[
        ("Material","Pl&#225;stico ABS / Mecanismo Cer&#226;mico"),
        ("Dimens&#245;es","6cm (L) x 6cm (W) x 21cm (A)"),
        ("Moagem","Ajust&#225;vel (fino ao grosso)"),
        ("Limpeza","Pano seco — n&#227;o lavar na m&#225;quina"),
        ("Origem","China"),
        ("Garantia","10 anos"),
    ]
)

# ── 2. Moedor de Pimenta 21cm ────────────────────────────────────────────────
COLORS_21P = ["Vermelho","Laranja","Bleu Riviera","Azure","Meringue","Artichaut",
              "Branco","Flint","Nectar","Black Onyx","Shell Pink","Thyme"]
IMG_21_PIM = CDN + "dw7138e9be/images/produto-lecreuset-moedores-vermelho.png"

make_page(
    filename="moedor-pimenta-21cm.html",
    title="Moedor de Pimenta 21cm Le Creuset",
    breadcrumb_cat="Acess&#243;rios",
    breadcrumb_cat_url="colecao-acessorios.html",
    name="Moedor de Pimenta 21cm",
    sub="Pl&#225;stico ABS com mecanismo cer&#226;mico",
    price="R$ 369,00",
    installment="ou 3x de R$ 123,00 sem juros",
    colors=COLORS_21P,
    base_img=IMG_21_PIM,
    specific_imgs=None,
    description=[
        "O Moedor de Pimenta 21cm Le Creuset garante uma moagem uniforme e ajust&#225;vel para pimenta do reino. O design er&#233;gon&#244;mico e as cores ic&#244;nicas da marca transformam o moedor em pe&#231;a de decora&#231;&#227;o da mesa.",
        "Mecanismo cer&#226;mico de alta precis&#227;o que n&#227;o enferruja e n&#227;o absorve odores. Ideal para uso di&#225;rio e ocasi&#245;es especiais."
    ],
    specs_rows=[
        ("Material","Pl&#225;stico ABS / Mecanismo Cer&#226;mico"),
        ("Dimens&#245;es","6cm (L) x 6cm (W) x 21cm (A)"),
        ("Moagem","Ajust&#225;vel (fino ao grosso)"),
        ("Limpeza","Pano seco — n&#227;o lavar na m&#225;quina"),
        ("Origem","China"),
        ("Garantia","10 anos"),
    ]
)

# ── 3. Moedor de Sal 30cm ────────────────────────────────────────────────────
COLORS_30S = ["Vermelho","Laranja","Black Onyx"]
IMGS_30S = {
    "Vermelho": CDN + "dw6de01276/images/tardes%20de%20verao/moedor-de-pimenta-30cm-vermelho.png",
    "Laranja":  CDN + "dw385cddde/images/tardes%20de%20verao/moedor-de-pimenta-30cm-laranja.png",
    "Black Onyx": CDN + "dw703f2293/images/tardes%20de%20verao/moedor-de-pimenta-30cm-blackonyx.png",
}
make_page(
    filename="moedor-sal-30cm.html",
    title="Moedor de Sal 30cm Le Creuset",
    breadcrumb_cat="Acess&#243;rios",
    breadcrumb_cat_url="colecao-acessorios.html",
    name="Moedor de Sal 30cm",
    sub="Pl&#225;stico ABS com mecanismo cer&#226;mico",
    price="R$ 479,00",
    installment="ou 5x de R$ 95,80 sem juros",
    colors=COLORS_30S,
    base_img=IMGS_30S["Vermelho"],
    specific_imgs=IMGS_30S,
    description=[
        "O Moedor de Sal 30cm Le Creuset &#233; a vers&#227;o grande e imponente para quem busca praticidade e estilo. Com mecanismo cer&#226;mico ajust&#225;vel e capacidade maior, &#233; ideal para uso intenso na cozinha e na mesa.",
        "O exterior em pl&#225;stico ABS resist&#234;nte &#233; f&#225;cil de segurar e limpar. Disponivel nas cores cl&#225;ssicas da Le Creuset."
    ],
    specs_rows=[
        ("Material","Pl&#225;stico ABS / Mecanismo Cer&#226;mico"),
        ("Altura","30 cm"),
        ("Moagem","Ajust&#225;vel"),
        ("Limpeza","Pano seco — n&#227;o lavar na m&#225;quina"),
        ("Origem","China"),
        ("Garantia","10 anos"),
    ]
)

# ── 4. Moedor de Pimenta 30cm ────────────────────────────────────────────────
COLORS_30P = ["Laranja","Vermelho","Black Onyx"]
IMGS_30P = {
    "Laranja":  CDN + "dw385cddde/images/tardes%20de%20verao/moedor-de-pimenta-30cm-laranja.png",
    "Vermelho": CDN + "dw6de01276/images/tardes%20de%20verao/moedor-de-pimenta-30cm-vermelho.png",
    "Black Onyx": CDN + "dw703f2293/images/tardes%20de%20verao/moedor-de-pimenta-30cm-blackonyx.png",
}
make_page(
    filename="moedor-pimenta-30cm.html",
    title="Moedor de Pimenta 30cm Le Creuset",
    breadcrumb_cat="Acess&#243;rios",
    breadcrumb_cat_url="colecao-acessorios.html",
    name="Moedor de Pimenta 30cm",
    sub="Pl&#225;stico ABS com mecanismo cer&#226;mico",
    price="R$ 479,00",
    installment="ou 5x de R$ 95,80 sem juros",
    colors=COLORS_30P,
    base_img=IMGS_30P["Laranja"],
    specific_imgs=IMGS_30P,
    description=[
        "O Moedor de Pimenta 30cm Le Creuset impressiona pelo tamanho e pela precis&#227;o. O mecanismo cer&#226;mico ajust&#225;vel garante moagem uniforme do grosso ao fino, sem absorver odores.",
        "Design er&#233;gon&#244;mico e f&#225;cil de manusear, mesmo com as m&#227;os cheias. Disponivel em cores ic&#244;nicas da paleta Le Creuset."
    ],
    specs_rows=[
        ("Material","Pl&#225;stico ABS / Mecanismo Cer&#226;mico"),
        ("Altura","30 cm"),
        ("Moagem","Ajust&#225;vel"),
        ("Limpeza","Pano seco — n&#227;o lavar na m&#225;quina"),
        ("Origem","China"),
        ("Garantia","10 anos"),
    ]
)

# ── 5. Moedor de Sal Modern 21cm ─────────────────────────────────────────────
IMGS_MOD_SAL = {
    "Bluebell Purple": CDN + "dwa69e3f54/images/moedor-Modern-Bluebell-sal.png",
}
make_page(
    filename="moedor-sal-modern-21cm.html",
    title="Moedor de Sal Modern 21cm Le Creuset",
    breadcrumb_cat="Lan&#231;amentos",
    breadcrumb_cat_url="colecao-lancamentos.html",
    name="Moedor de Sal Modern 21cm",
    sub="Cole&#231;&#227;o Modern — Bluebell Purple",
    price="R$ 369,00",
    installment="ou 3x de R$ 123,00 sem juros",
    colors=["Bluebell Purple"],
    base_img=IMGS_MOD_SAL["Bluebell Purple"],
    specific_imgs=IMGS_MOD_SAL,
    description=[
        "Com design cl&#225;ssico e tecnologia moderna, o Moedor de Sal Modern 21cm Le Creuset traz um toque da cor Bluebell Purple — um dos lan&#231;amentos mais esperados da paleta Le Creuset.",
        "O mecanismo ajust&#225;vel no topo permite controlar com precis&#227;o a granulometria. O exterior em pl&#225;stico ABS &#233; resistente e f&#225;cil de limpar."
    ],
    specs_rows=[
        ("Material","Pl&#225;stico ABS / Mecanismo Cer&#226;mico"),
        ("Dimens&#245;es","6cm (L) x 6cm (W) x 21cm (A)"),
        ("Cor","Bluebell Purple"),
        ("Moagem","Ajust&#225;vel"),
        ("Limpeza","Pano seco"),
        ("Origem","China"),
        ("Garantia","10 anos"),
    ]
)

# ── 6. Moedor de Pimenta Modern 21cm ─────────────────────────────────────────
IMGS_MOD_PIM = {
    "Bluebell Purple": CDN + "dwdb71c36f/images/moedor-Modern-Bluebell-pimenta.png",
}
make_page(
    filename="moedor-pimenta-modern-21cm.html",
    title="Moedor de Pimenta Modern 21cm Le Creuset",
    breadcrumb_cat="Lan&#231;amentos",
    breadcrumb_cat_url="colecao-lancamentos.html",
    name="Moedor de Pimenta Modern 21cm",
    sub="Cole&#231;&#227;o Modern — Bluebell Purple",
    price="R$ 369,00",
    installment="ou 3x de R$ 123,00 sem juros",
    colors=["Bluebell Purple"],
    base_img=IMGS_MOD_PIM["Bluebell Purple"],
    specific_imgs=IMGS_MOD_PIM,
    description=[
        "Com design cl&#225;ssico e tecnologia moderna, o Moedor de Pimenta Modern 21cm Le Creuset traz um toque da cor Bluebell Purple — um dos lan&#231;amentos mais esperados da paleta Le Creuset.",
        "O mecanismo ajust&#225;vel no topo permite controlar com precis&#227;o a granulometria. O exterior em pl&#225;stico ABS &#233; resistente e f&#225;cil de limpar."
    ],
    specs_rows=[
        ("Material","Pl&#225;stico ABS / Mecanismo Cer&#226;mico"),
        ("Dimens&#245;es","6cm (L) x 6cm (W) x 21cm (A)"),
        ("Cor","Bluebell Purple"),
        ("Moagem","Ajust&#225;vel"),
        ("Limpeza","Pano seco"),
        ("Origem","China"),
        ("Garantia","10 anos"),
    ]
)

# ── 7. Set Saleiro & Pimenteiro Coração ──────────────────────────────────────
IMGS_CORACAO = {
    "Vermelho": CDN + "dw7e22f027/images/kit-saleiro-pimenteiro-vermelho.png",
    "Shallot":  CDN + "dw20fde0be/images/kit-saleiro-pimenteiro-shallot.png",
    "Branco":   CDN + "dwee16c0e3/images/kit-saleiro-pimenteiro-branco.png",
}
make_page(
    filename="set-saleiro-pimenteiro-coracao.html",
    title="Set Saleiro e Pimenteiro Coracao Le Creuset",
    breadcrumb_cat="Acess&#243;rios",
    breadcrumb_cat_url="colecao-acessorios.html",
    name="Set Saleiro &amp; Pimenteiro Cora&#231;&#227;o",
    sub="Cer&#226;mica — formato cora&#231;&#227;o",
    price="R$ 379,00",
    installment="ou 3x de R$ 126,33 sem juros",
    colors=["Vermelho","Shallot","Branco"],
    base_img=IMGS_CORACAO["Vermelho"],
    specific_imgs=IMGS_CORACAO,
    description=[
        "O Set Saleiro &amp; Pimenteiro Cora&#231;&#227;o Le Creuset &#233; uma pe&#231;a encantadora para decorar e usar &#224; mesa. O formato cora&#231;&#227;o em cer&#226;mica esmaltada traz charme e personalidade ao seu jantar.",
        "Adequado para lavar na lav&#225;dora de lou&#231;as. N&#227;o usar diretamente sobre chama ou fonte de calor."
    ],
    specs_rows=[
        ("Material","Cer&#226;mica Esmaltada"),
        ("Dimens&#245;es","11cm (L) x 6cm (W) x 10cm (A)"),
        ("Conte&#250;do","1 saleiro + 1 pimenteiro"),
        ("Limpeza","Lav&#225;dora de lou&#231;as"),
        ("Origem","Tail&#226;ndia"),
        ("Garantia","10 anos"),
    ]
)

print("\nTodos os arquivos criados com sucesso!")
