#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cria 13 páginas de produto + colecao-potes-e-porta-mantimentos.html
"""
import os

BASE = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN  = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q    = "?sw=650&sh=650&sm=fit"
WISH = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

COLOR_HEX = {
    "Vermelho": "#C41E3A", "Laranja": "#FE5000", "Bleu Riviera": "#0066B2",
    "Azure": "#007FFF",    "Meringue": "#F5F5DC", "Artichaut": "#4B5320",
    "Branco": "#FFFFFF",   "Flint": "#708090",    "Nectar": "#FFB347",
    "Black Onyx": "#1a1a1a","Shell Pink": "#FFB6C1","Thyme": "#6B8E23",
    "Caribe": "#1CA3A3",   "Marseille": "#2860A0", "Bamboo": "#C8A87A",
    "Dijon": "#C8A838",    "Marronnier": "#6B4226","Vapeur": "#B0B0B0",
    "Teca": "#6B4226",     "Inox": "#B0B0B0",
}

# ── helpers ──────────────────────────────────────────────────────────────────

HEADER_TPL = """<!DOCTYPE html>
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
    .product-main-img img{{width:100%;height:100%;object-fit:contain;padding:40px;}}
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
    <nav><ul class="nav-list">
      <li><a href="#">Comprar</a>
        <div class="mega-menu"><div class="mega-inner">
          <div class="mega-col"><div class="mega-col-title">Cozinhar</div>
            <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
            <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
            <a href="colecao-cacarolas.html">Ca&#231;arolas</a>
            <a href="colecao-antiaderente.html">Antiaderente</a>
            <a href="colecao-acessorios.html">Acess&#243;rios</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Assar</div>
            <a href="colecao-assadeiras-travessas.html">Assadeiras e Travessas</a>
            <a href="colecao-formas-metal-bakeware.html">Formas Metal Bakeware</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Acess&#243;rios</div>
            <a href="colecao-moedores-e-galheteiro.html">Moedores e Galheteiro</a>
            <a href="colecao-potes-e-porta-mantimentos.html">Potes e Porta-Mantimentos</a>
            <a href="colecao-utensilios.html">Utensilios</a>
            <a href="colecao-utensilios-madeira.html">Utensilios de Madeira</a>
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
</header>
"""

FOOTER_TPL = """<footer>
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
function selectColor(el,name,src){{
  el.parentElement.querySelectorAll('.color-swatch').forEach(x=>x.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('mainImgEl').src=src;
  document.getElementById('colorName').textContent=name;
}}
</script>
</body></html>"""


def make_product(filename, title, crumb_cat, crumb_url, name, sub, price, installment,
                 colors_imgs, description, specs):
    """colors_imgs: list of (color_name, img_hash_path) tuples"""
    first_color, first_hash = colors_imgs[0]
    first_img = CDN + first_hash + Q

    swatches_html = ""
    for i, (cname, chash) in enumerate(colors_imgs):
        url = CDN + chash + Q
        hexc = COLOR_HEX.get(cname, "#888888")
        bord = "border:2px solid #ccc;" if hexc in ("#FFFFFF","#F5F5DC") else "border:2px solid transparent;"
        act  = " active" if i == 0 else ""
        swatches_html += (
            f'<span class="color-swatch{act}" style="background:{hexc};{bord}" '
            f'title="{cname}" onclick="selectColor(this,\'{cname}\',\'{url}\')"></span>\n      '
        )

    specs_html = "".join(f"<tr><td class='sk'>{k}:</td><td class='sv'>{v}</td></tr>" for k,v in specs)
    desc_html  = "".join(f"<p>{p}</p>" for p in description)

    html = HEADER_TPL.format(title=title)
    html += f"""<div class="breadcrumb">
  <a href="index.html">In&#237;cio</a><span>/</span>
  <a href="{crumb_url}">{crumb_cat}</a><span>/</span>
  <span>{name}</span>
</div>
<div class="product-wrap">
  <div class="product-img-wrap">
    <div class="product-main-img">
      <img id="mainImgEl" src="{first_img}" alt="{name}"/>
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
      {swatches_html.strip()}
      </div>
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
"""
    html += FOOTER_TPL

    path = os.path.join(BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Produto: {filename}")


# ══════════════════════════════════════════════════════════════════════════════
# 13 PRODUCT PAGES
# ══════════════════════════════════════════════════════════════════════════════
print("Criando páginas de produto...")

make_product("pote-de-manteiga.html","Pote de Manteiga Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Pote de Manteiga","Cer&#226;mica Esmaltada","R$ 319,00","ou 3x de R$ 106,33 sem juros",
    [("Vermelho","dwe2c6a579/images/produto-lecreuset-pote-manteiga-vermelho (1).png")],
    ["O Pote de Manteiga Le Creuset em cer&#226;mica esmaltada mant&#233;m a manteiga fresca e macia &#224; temperatura ambiente.",
     "O design cl&#225;ssico e as cores ic&#244;nicas da Le Creuset tornam este pote um elemento decorativo e funcional na sua mesa."],
    [("Material","Cer&#226;mica Esmaltada"),("Capacidade","Barra padr&#227;o de manteiga"),
     ("Limpeza","Lav&#225;dora de lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("acucareiro.html","Açucareiro Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "A&#231;ucareiro","Cer&#226;mica Esmaltada","R$ 259,00","ou 3x de R$ 86,33 sem juros",
    [("Vermelho","dw982a3489/images/acucareiro_vermelho_cerise.jpg")],
    ["O A&#231;ucareiro Le Creuset combina funcionalidade e beleza em cer&#226;mica esmaltada de alta qualidade.",
     "A tampa veda perfeitamente para manter o a&#231;&#250;car seco e sem umidade. Ideal para uso di&#225;rio e para presentear."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","Lav&#225;dora de lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("manteigueira.html","Manteigueira Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Manteigueira","Cer&#226;mica Esmaltada","R$ 429,00","ou 4x de R$ 107,25 sem juros",
    [("Vermelho","dwcb6d18b9/images/manteigueira_vermelho_leceruset.jpg")],
    ["A Manteigueira Le Creuset &#233; fabricada em cer&#226;mica esmaltada de alta qualidade, com tampa que encaixa perfeitamente.",
     "Ideal para servir manteiga &#224; mesa com estilo. Dispon&#237;vel nas cores ic&#244;nicas da paleta Le Creuset."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","Lav&#225;dora de lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("pote-para-biscoito.html","Pote para Biscoito 2,4L Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Pote para Biscoito 2,4L","Cer&#226;mica Esmaltada","R$ 649,00","ou 5x de R$ 129,80 sem juros",
    [("Vermelho","dw374a4000/images/produto-lecreuset-vermelho-pote.png")],
    ["O Pote para Biscoito 2,4L Le Creuset em cer&#226;mica esmaltada &#233; perfeito para armazenar biscoitos, balas e doces com charme.",
     "A tampa de encaixe perfeito mant&#233;m os alimentos frescos por mais tempo. Um item decorativo e funcional para a sua cozinha."],
    [("Material","Cer&#226;mica Esmaltada"),("Capacidade","2,4 litros"),
     ("Limpeza","Lav&#225;dora de lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("porta-mantimentos.html","Porta Mantimentos Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Porta Mantimentos","Cer&#226;mica Esmaltada","R$ 549,00 &#8211; R$ 659,00","ou 5x de R$ 109,80 sem juros",
    [("Vermelho","dwc773011e/images/porta-mantimentos-vermelho-lecreuset.png")],
    ["O Porta Mantimentos Le Creuset em cer&#226;mica esmaltada &#233; ideal para armazenar massas, arroz, caf&#233; e outros alimentos secos.",
     "A tampa vedante mant&#233;m os alimentos frescos. Dispon&#237;vel em diferentes tamanhos e cores ic&#244;nicas da Le Creuset."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","Lav&#225;dora de lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("pilao.html","Pilão Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Pil&#227;o","Cer&#226;mica Esmaltada","R$ 265,30 &#8211; R$ 379,00","ou 3x de R$ 88,43 sem juros",
    [("Vermelho","dw71867725/images/pilao-vermelho-lecreuset.jpg")],
    ["O Pil&#227;o Le Creuset em cer&#226;mica esmaltada &#233; perfeito para moer temperos, ervas e especiarias. A superf&#237;cie porosa interna garante moagem eficiente.",
     "Combina funcionalidade com o design cl&#225;ssico das cores Le Creuset. Ideal para cozinhas que valorizam est&#233;tica e performance."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","&#192; m&#227;o — n&#227;o lavar na m&#225;quina"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("pote-de-silicone.html","Pote de Silicone Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Pote de Silicone","Silicone Premium","R$ 219,00 &#8211; R$ 449,00","ou 3x de R$ 73,00 sem juros",
    [("Laranja","dw9e436629/images/Recipiente-de-armazenamento-de-silicone7.png")],
    ["O Pote de Silicone Le Creuset &#233; flex&#237;vel, resist&#234;nte e ve&#225;dor herm&#233;tico. Ideal para armazenar alimentos na geladeira, freezer ou micro-ondas.",
     "Dispon&#237;vel em m&#250;ltiplos tamanhos (500ml, 1L e 2L) e nas cores Laranja, Vermelho e Vapeur."],
    [("Material","Silicone Premium"),("Capacidades","500ml, 1L e 2L"),
     ("Uso","Geladeira, freezer, micro-ondas"),("Limpeza","Lav&#225;dora de lou&#231;as"),("Garantia","10 anos")])

make_product("set-creme-e-acucar.html","Set Cream e Sugar Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Set Cream &amp; Sugar","Cer&#226;mica Esmaltada","R$ 321,30 &#8211; R$ 459,00","ou 4x de R$ 80,33 sem juros",
    [("Vermelho","dwf6a18990/images/set-creme-e-a\u00e7ucar-lecreuset6.png"),
     ("Laranja","dwd277d668/images/set-creme-e-a\u00e7ucar-laranja4.png"),
     ("Meringue","dw0398f4ac/images/set-creme-e-a\u00e7ucar-meringue4.png")],
    ["O Set Cream &amp; Sugar Le Creuset re&#250;ne a&#231;ucareiro e cremeira em cer&#226;mica esmaltada, perfeito para servir caf&#233; e ch&#225; com estilo.",
     "Conjunto funcional e decorativo nas cores mais amadas da paleta Le Creuset. Lav&#225;vel na m&#225;quina de lou&#231;as."],
    [("Material","Cer&#226;mica Esmaltada"),("Conte&#250;do","1 a&#231;ucareiro + 1 cremeira"),
     ("Limpeza","Lav&#225;dora de lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("pote-de-alho.html","Pote de Alho Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Pote de Alho","Cer&#226;mica Esmaltada","R$ 229,00","ou 3x de R$ 76,33 sem juros",
    [("Meringue","dw7e6363f0/images/porta-alho-meringue.jpg"),
     ("Vermelho","dw84fd544b/images/pote-para-alho-vermelho.png")],
    ["O Pote de Alho Le Creuset em cer&#226;mica esmaltada mant&#233;m o alho fresco por mais tempo. Os furos na tampa permitem ventila&#231;&#227;o ideal.",
     "Design compacto e charmoso que complementa qualquer decora&#231;&#227;o de cozinha."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","&#192; m&#227;o"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("porta-utensilios-classico.html","Porta Utensílios Clássico Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Porta Utensilios Cl&#225;ssico","Cer&#226;mica Esmaltada","R$ 223,30 &#8211; R$ 449,00","ou 3x de R$ 74,43 sem juros",
    [("Flint","dw42382f9a/images/produto-lecreuset-utensil-flint.png")],
    ["O Porta Utensilios Cl&#225;ssico Le Creuset em cer&#226;mica esmaltada organiza seus utensilios de cozinha com estilo.",
     "Dispon&#237;vel em diversas cores ic&#244;nicas. Resistente e duradouro, com superf&#237;cie esmaltada f&#225;cil de limpar."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","Lav&#225;dora de lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("porta-utensilios-signature.html","Porta Utensílios Signature 1L Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Porta Utensilios Signature 1L","Cer&#226;mica Esmaltada","R$ 319,00 &#8211; R$ 449,00","ou 4x de R$ 79,75 sem juros",
    [("Vermelho","dw33b55c5c/images/produto-lecreuset-porta-utensilios-sig-vermelho.png"),
     ("Laranja","dwff8efbe1/images/produto-lecreuset-porta-utensilios-sig-laranja.png"),
     ("Caribe","dwe50cc6ff/images/produto-lecreuset-porta-utensilios-sig-caribe.png"),
     ("Nectar","dwf63b3362/images/produto-lecreuset-porta-utensilios-sig-nectar.png"),
     ("Shell Pink","dw42b02d93/images/produto-lecreuset-porta-utensilios-sig-shellpink.png")],
    ["O Porta Utensilios Signature 1L Le Creuset &#233; maior e mais robusto, ideal para cozinhas que possuem muitos utensilios.",
     "Cer&#226;mica esmaltada com borda arredondada e alc&#231;a generosa. Dispon&#237;vel em 5 cores com fotos reais para cada cor."],
    [("Material","Cer&#226;mica Esmaltada"),("Capacidade","1 litro"),
     ("Limpeza","Lav&#225;dora de lou&#231;as"),("Origem","Tail&#226;ndia"),("Garantia","10 anos")])

make_product("molheira-abobora-400ml.html","Molheira Abóbora 400ml Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Molheira Ab&#243;bora 400ml","Ferro Fundido Esmaltado","R$ 549,00","ou 5x de R$ 109,80 sem juros",
    [("Laranja","dwa677674c/images/molheira-abobora-flame-le creuset.png"),
     ("Thyme","dw0051bba8/images/molheira-abobora-thyme-le creuset.png"),
     ("Marronnier","dw6fd9a760/images/molheira-abobora-marronier3.png")],
    ["A Molheira Ab&#243;bora 400ml Le Creuset tem o icônico formato de ab&#243;bora em ferro fundido esmaltado.",
     "Perfeita para servir molhos, caldas e cremes quentes diretamente &#224; mesa. O ferro fundido mant&#233;m a temperatura por mais tempo."],
    [("Material","Ferro Fundido Esmaltado"),("Capacidade","400ml"),
     ("Uso","N&#227;o usar micro-ondas"),("Limpeza","&#192; m&#227;o"),
     ("Origem","China"),("Garantia","Lifetime")])

make_product("pote-de-condimentos.html","Pote de Condimentos Le Creuset",
    "Potes e Porta-Mantimentos","colecao-potes-e-porta-mantimentos.html",
    "Pote de Condimentos","Cer&#226;mica Esmaltada","R$ 379,00","ou 4x de R$ 94,75 sem juros",
    [("Laranja","dwd505d24e/images/produto-lecreuset-condimentos-laranja (1).png"),
     ("Vermelho","dw498bc49d/images/produto-lecreuset-condimentos-vermelho (1).png"),
     ("Branco","dw0ff48c7d/images/produto-lecreuset-condimentos-branco (1).png"),
     ("Marseille","dwe479f717/images/produto-lecreuset-condimentos-marseiile (1).png")],
    ["O Pote de Condimentos Le Creuset em cer&#226;mica esmaltada &#233; ideal para servir molhos, azeite, vinagre e condimentos &#224; mesa.",
     "Tampa com vedação perfeita e design elegante nas cores cl&#225;ssicas da Le Creuset."],
    [("Material","Cer&#226;mica Esmaltada"),("Limpeza","Lav&#225;dora de lou&#231;as"),
     ("Origem","Tail&#226;ndia"),("Garantia","10 anos")])


# ══════════════════════════════════════════════════════════════════════════════
# COLLECTION PAGE
# ══════════════════════════════════════════════════════════════════════════════
print("\nCriando colecao-potes-e-porta-mantimentos.html...")

def sw(img_id, hex_c, label, url, active=False, border=""):
    act = " active" if active else ""
    brd = f"border:1.5px solid {border};" if border else "border:1.5px solid transparent;"
    return (f'<span class="swatch{act}" style="background:{hex_c};{brd}" '
            f'onclick="swatchClick(event,this,\'{img_id}\',\'{url}\')" title="{label}"></span>')

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

C = CDN  # shortcut

# ── image URLs ───────────────────────────────────────────────────────────────
cards = []

# 1. Porta Sal
cards.append(card("i_portasal","porta-sal.html",
    C+"dw3b75d249/images/porta_sal_vermelho_cerise.jpg"+Q,"Porta Sal",
    "Porta Sal","Cer&#226;mica · M&#250;ltiplas cores","R$ 265,30 &#8211; R$ 379,00",
    sw("i_portasal","#C41E3A","Vermelho",C+"dw3b75d249/images/porta_sal_vermelho_cerise.jpg"+Q,True)))

# 2. Pote de Manteiga
cards.append(card("i_potemanteiga","pote-de-manteiga.html",
    C+"dwe2c6a579/images/produto-lecreuset-pote-manteiga-vermelho (1).png"+Q,"Pote de Manteiga",
    "Pote de Manteiga","Cer&#226;mica Esmaltada","R$ 319,00",
    sw("i_potemanteiga","#C41E3A","Vermelho",C+"dwe2c6a579/images/produto-lecreuset-pote-manteiga-vermelho (1).png"+Q,True)))

# 3. Porta Condimento — 5 cores reais
IMG_PC = {
    "Laranja": C+"dw96391238/images/porta-condimento-laranja-lecreuset4.png"+Q,
    "Vermelho": C+"dwdf451dfa/images/porta-condimento-vermelho-lecreuset1.png"+Q,
    "Marseille": C+"dw88496a9c/images/porta-condimento-marseille-lecreuset1.png"+Q,
    "Caribe": C+"dweab9487f/images/porta-condimento-caribe-lecreuset1.png"+Q,
    "Branco": C+"dw499c819d/images/porta-condimento-branco-lecreuset1.png"+Q,
}
cards.append(card("i_portacond","porta-condimento.html",
    IMG_PC["Laranja"],"Porta Condimento",
    "Porta Condimento","Cer&#226;mica Esmaltada","R$ 289,00 &#8211; R$ 439,00",
    sw("i_portacond","#FE5000","Laranja",IMG_PC["Laranja"],True)+
    sw("i_portacond","#C41E3A","Vermelho",IMG_PC["Vermelho"])+
    sw("i_portacond","#2860A0","Marseille",IMG_PC["Marseille"])+
    sw("i_portacond","#1CA3A3","Caribe",IMG_PC["Caribe"])+
    sw("i_portacond","#FFFFFF","Branco",IMG_PC["Branco"],border="#ccc")))

# 4. Açucareiro
cards.append(card("i_acucareiro","acucareiro.html",
    C+"dw982a3489/images/acucareiro_vermelho_cerise.jpg"+Q,"Açucareiro",
    "A&#231;ucareiro","Cer&#226;mica Esmaltada","R$ 259,00",
    sw("i_acucareiro","#C41E3A","Vermelho",C+"dw982a3489/images/acucareiro_vermelho_cerise.jpg"+Q,True)))

# 5. Manteigueira
cards.append(card("i_manteig","manteigueira.html",
    C+"dwcb6d18b9/images/manteigueira_vermelho_leceruset.jpg"+Q,"Manteigueira",
    "Manteigueira","Cer&#226;mica Esmaltada","R$ 429,00",
    sw("i_manteig","#C41E3A","Vermelho",C+"dwcb6d18b9/images/manteigueira_vermelho_leceruset.jpg"+Q,True)))

# 6. Pote para Biscoito
cards.append(card("i_biscoito","pote-para-biscoito.html",
    C+"dw374a4000/images/produto-lecreuset-vermelho-pote.png"+Q,"Pote para Biscoito 2,4L",
    "Pote para Biscoito 2,4L","Cer&#226;mica Esmaltada","R$ 649,00",
    sw("i_biscoito","#C41E3A","Vermelho",C+"dw374a4000/images/produto-lecreuset-vermelho-pote.png"+Q,True)))

# 7. Porta Mantimentos
cards.append(card("i_portamant","porta-mantimentos.html",
    C+"dwc773011e/images/porta-mantimentos-vermelho-lecreuset.png"+Q,"Porta Mantimentos",
    "Porta Mantimentos","Cer&#226;mica Esmaltada","R$ 549,00 &#8211; R$ 659,00",
    sw("i_portamant","#C41E3A","Vermelho",C+"dwc773011e/images/porta-mantimentos-vermelho-lecreuset.png"+Q,True)))

# 8. Pote Tampa Madeira 220ml
cards.append(card("i_ptm220","pote-tampa-madeira-220ml.html",
    C+"dwd587fe8b/images/Pote-tampa-420-vermelho.png"+Q,"Pote Com Tampa de Madeira 220ml",
    "Pote Com Tampa de Madeira 220ml","Cer&#226;mica + Tampa Madeira","R$ 349,00",
    sw("i_ptm220","#C41E3A","Vermelho",C+"dwd587fe8b/images/Pote-tampa-420-vermelho.png"+Q,True)))

# 9. Pilão
cards.append(card("i_pilao","pilao.html",
    C+"dw71867725/images/pilao-vermelho-lecreuset.jpg"+Q,"Pilão",
    "Pil&#227;o","Cer&#226;mica Esmaltada","R$ 265,30 &#8211; R$ 379,00",
    sw("i_pilao","#C41E3A","Vermelho",C+"dw71867725/images/pilao-vermelho-lecreuset.jpg"+Q,True)))

# 10. Bowl Inox 19cm
cards.append(card("i_bowl19","bowl-inox-19cm.html",
    C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,"Bowl Inox com Tampa de Vidro 19cm",
    "Bowl Inox com Tampa de Vidro 19cm","A&#231;o Inox + Tampa Vidro","R$ 399,00",
    sw("i_bowl19","#B0B0B0","Inox",C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,True)))

# 11. Pote Tampa Madeira 1,9L
cards.append(card("i_ptm19l","pote-tampa-madeira-19l.html",
    C+"dwbc447da1/images/Pote-tampa-1,9-vermelho.png"+Q,"Pote Com Tampa de Madeira 1,9L",
    "Pote Com Tampa de Madeira 1,9L","Cer&#226;mica + Tampa Madeira","R$ 619,00",
    sw("i_ptm19l","#C41E3A","Vermelho",C+"dwbc447da1/images/Pote-tampa-1,9-vermelho.png"+Q,True)))

# 12. Pote para Mostarda
cards.append(card("i_mostarda","pote-para-mostarda.html",
    C+"dw8878da41/images/pote-para-mostarda-lecreuset-djon1.png"+Q,"Pote para Mostarda",
    "Pote para Mostarda","Cer&#226;mica Esmaltada","R$ 379,00",
    sw("i_mostarda","#C8A838","Dijon",C+"dw8878da41/images/pote-para-mostarda-lecreuset-djon1.png"+Q,True)))

# 13. Pote Tampa Madeira 1,1L
cards.append(card("i_ptm11l","pote-tampa-madeira-11l.html",
    C+"dw74904681/images/Pote-tampa-1,1-vermelho.png"+Q,"Pote Com Tampa de Madeira 1,1L",
    "Pote Com Tampa de Madeira 1,1L","Cer&#226;mica + Tampa Madeira","R$ 519,00",
    sw("i_ptm11l","#C41E3A","Vermelho",C+"dw74904681/images/Pote-tampa-1,1-vermelho.png"+Q,True)))

# 14. Pote para Geleia
cards.append(card("i_geleia","pote-para-geleia.html",
    C+"dwa384dc5a/images/pote-para-geleia-lecreuset-vermelho.png"+Q,"Pote para Geleia",
    "Pote para Geleia","Cer&#226;mica Esmaltada","R$ 379,00",
    sw("i_geleia","#C41E3A","Vermelho",C+"dwa384dc5a/images/pote-para-geleia-lecreuset-vermelho.png"+Q,True)))

# 15. Pote de Silicone
cards.append(card("i_silicone","pote-de-silicone.html",
    C+"dw9e436629/images/Recipiente-de-armazenamento-de-silicone7.png"+Q,"Pote de Silicone",
    "Pote de Silicone","Silicone Premium","R$ 219,00 &#8211; R$ 449,00",
    sw("i_silicone","#FE5000","Laranja",C+"dw9e436629/images/Recipiente-de-armazenamento-de-silicone7.png"+Q,True)))

# 16-18. Bowl Inox 23cm e 27cm
cards.append(card("i_bowl23","bowl-inox-23cm.html",
    C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,"Bowl Inox com Tampa de Vidro 23cm",
    "Bowl Inox com Tampa de Vidro 23cm","A&#231;o Inox + Tampa Vidro","R$ 489,00",
    sw("i_bowl23","#B0B0B0","Inox",C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,True)))

cards.append(card("i_bowl27","bowl-inox-27cm.html",
    C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,"Bowl Inox com Tampa de Vidro 27cm",
    "Bowl Inox com Tampa de Vidro 27cm","A&#231;o Inox + Tampa Vidro","R$ 689,00",
    sw("i_bowl27","#B0B0B0","Inox",C+"dwf8b78720/images/bowl-inox-tampa-de-vidro.png"+Q,True)))

# 19. Set Cream & Sugar — 3 cores reais
IMG_CS = {
    "Vermelho": C+"dwf6a18990/images/set-creme-e-a\u00e7ucar-lecreuset6.png"+Q,
    "Laranja":  C+"dwd277d668/images/set-creme-e-a\u00e7ucar-laranja4.png"+Q,
    "Meringue": C+"dw0398f4ac/images/set-creme-e-a\u00e7ucar-meringue4.png"+Q,
}
cards.append(card("i_creamsugar","set-creme-e-acucar.html",
    IMG_CS["Vermelho"],"Set Cream & Sugar",
    "Set Cream &amp; Sugar","Cer&#226;mica Esmaltada","R$ 321,30 &#8211; R$ 459,00",
    sw("i_creamsugar","#C41E3A","Vermelho",IMG_CS["Vermelho"],True)+
    sw("i_creamsugar","#FE5000","Laranja",IMG_CS["Laranja"])+
    sw("i_creamsugar","#F5F5DC","Meringue",IMG_CS["Meringue"],border="#ccc")))

# 20. Pote de Alho — 2 cores reais
IMG_ALH = {
    "Meringue": C+"dw7e6363f0/images/porta-alho-meringue.jpg"+Q,
    "Vermelho":  C+"dw84fd544b/images/pote-para-alho-vermelho.png"+Q,
}
cards.append(card("i_alho","pote-de-alho.html",
    IMG_ALH["Meringue"],"Pote de Alho",
    "Pote de Alho","Cer&#226;mica Esmaltada","R$ 229,00",
    sw("i_alho","#F5F5DC","Meringue",IMG_ALH["Meringue"],True,border="#ccc")+
    sw("i_alho","#C41E3A","Vermelho",IMG_ALH["Vermelho"])))

# 21. Saleiro Teca
cards.append(card("i_tecasalt","saleiro-redondo-madeira-teca.html",
    C+"dw3df69a85/images/saleiro-redondo-madeira-teca.png"+Q,"Saleiro Redondo de Madeira Teca",
    "Saleiro Redondo de Madeira Teca 160ml","Madeira Teca · 160ml","R$ 349,00",
    sw("i_tecasalt","#6B4226","Teca",C+"dw3df69a85/images/saleiro-redondo-madeira-teca.png"+Q,True)))

# 22. Pote Tampa Madeira 420ml
cards.append(card("i_ptm420","pote-tampa-madeira-420ml.html",
    C+"dwf0169b3c/images/Pote-tampa-220-vermelho.png"+Q,"Pote Com Tampa de Madeira 420ml",
    "Pote Com Tampa de Madeira 420ml","Cer&#226;mica + Tampa Madeira","R$ 469,00",
    sw("i_ptm420","#C41E3A","Vermelho",C+"dwf0169b3c/images/Pote-tampa-220-vermelho.png"+Q,True)))

# 23. Porta Utensílios Clássico
cards.append(card("i_utclassico","porta-utensilios-classico.html",
    C+"dw42382f9a/images/produto-lecreuset-utensil-flint.png"+Q,"Porta Utensílios Clássico",
    "Porta Utensilios Cl&#225;ssico","Cer&#226;mica Esmaltada","R$ 223,30 &#8211; R$ 449,00",
    sw("i_utclassico","#708090","Flint",C+"dw42382f9a/images/produto-lecreuset-utensil-flint.png"+Q,True)))

# 24. Molheira Abóbora — 3 cores reais
IMG_MOL = {
    "Laranja":    C+"dwa677674c/images/molheira-abobora-flame-le creuset.png"+Q,
    "Thyme":      C+"dw0051bba8/images/molheira-abobora-thyme-le creuset.png"+Q,
    "Marronnier": C+"dw6fd9a760/images/molheira-abobora-marronier3.png"+Q,
}
cards.append(card("i_molhabob","molheira-abobora-400ml.html",
    IMG_MOL["Laranja"],"Molheira Abóbora 400ml",
    "Molheira Ab&#243;bora 400ml","Ferro Fundido Esmaltado","R$ 549,00",
    sw("i_molhabob","#FE5000","Laranja",IMG_MOL["Laranja"],True)+
    sw("i_molhabob","#6B8E23","Thyme",IMG_MOL["Thyme"])+
    sw("i_molhabob","#6B4226","Marronnier",IMG_MOL["Marronnier"])))

# 25. Porta Utensílios Signature — 5 cores reais
IMG_SIG = {
    "Vermelho":   C+"dw33b55c5c/images/produto-lecreuset-porta-utensilios-sig-vermelho.png"+Q,
    "Laranja":    C+"dwff8efbe1/images/produto-lecreuset-porta-utensilios-sig-laranja.png"+Q,
    "Caribe":     C+"dwe50cc6ff/images/produto-lecreuset-porta-utensilios-sig-caribe.png"+Q,
    "Nectar":     C+"dwf63b3362/images/produto-lecreuset-porta-utensilios-sig-nectar.png"+Q,
    "Shell Pink": C+"dw42b02d93/images/produto-lecreuset-porta-utensilios-sig-shellpink.png"+Q,
}
cards.append(card("i_utsig","porta-utensilios-signature.html",
    IMG_SIG["Vermelho"],"Porta Utensílios Signature 1L",
    "Porta Utensilios Signature 1L","Cer&#226;mica Esmaltada","R$ 319,00 &#8211; R$ 449,00",
    sw("i_utsig","#C41E3A","Vermelho",IMG_SIG["Vermelho"],True)+
    sw("i_utsig","#FE5000","Laranja",IMG_SIG["Laranja"])+
    sw("i_utsig","#1CA3A3","Caribe",IMG_SIG["Caribe"])+
    sw("i_utsig","#FFB347","Nectar",IMG_SIG["Nectar"])+
    sw("i_utsig","#FFB6C1","Shell Pink",IMG_SIG["Shell Pink"])))

# 26. Molheira 460ml
cards.append(card("i_molh460","molheira-460ml.html",
    C+"dw66740c39/images/molheira-360-lecreuset-vermelho.jpg"+Q,"Molheira 460ml",
    "Molheira 460ml","Cer&#226;mica Esmaltada","R$ 309,00",
    sw("i_molh460","#C41E3A","Vermelho",C+"dw66740c39/images/molheira-360-lecreuset-vermelho.jpg"+Q,True)))

# 27. Pote de Condimentos — 4 cores reais
IMG_COND = {
    "Laranja":   C+"dwd505d24e/images/produto-lecreuset-condimentos-laranja (1).png"+Q,
    "Vermelho":  C+"dw498bc49d/images/produto-lecreuset-condimentos-vermelho (1).png"+Q,
    "Branco":    C+"dw0ff48c7d/images/produto-lecreuset-condimentos-branco (1).png"+Q,
    "Marseille": C+"dwe479f717/images/produto-lecreuset-condimentos-marseiile (1).png"+Q,
}
cards.append(card("i_potecond","pote-de-condimentos.html",
    IMG_COND["Laranja"],"Pote de Condimentos",
    "Pote de Condimentos","Cer&#226;mica Esmaltada","R$ 379,00",
    sw("i_potecond","#FE5000","Laranja",IMG_COND["Laranja"],True)+
    sw("i_potecond","#C41E3A","Vermelho",IMG_COND["Vermelho"])+
    sw("i_potecond","#FFFFFF","Branco",IMG_COND["Branco"],border="#ccc")+
    sw("i_potecond","#2860A0","Marseille",IMG_COND["Marseille"])))

# 28. Pote para Mel
cards.append(card("i_mel","pote-para-mel.html",
    C+"dw7ad6078c/images/pote-para-mel-lecreuset-nectar7.png"+Q,"Pote para Mel",
    "Pote para Mel","Cer&#226;mica Esmaltada","R$ 379,00",
    sw("i_mel","#FFB347","Nectar",C+"dw7ad6078c/images/pote-para-mel-lecreuset-nectar7.png"+Q,True)))

N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Potes e Porta-Mantimentos | Le Creuset Brasil</title>
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
    .cat-banner-crumb{{font-size:12px;color:#888;display:flex;gap:5px;align-items:center;margin-bottom:14px;flex-wrap:wrap;}}
    .cat-banner-crumb a{{color:#888;}} .cat-banner-crumb a:hover{{color:#000;text-decoration:underline;}}
    .cat-banner-title{{font-size:26px;font-weight:700;color:#000;margin-bottom:12px;}}
    .cat-banner-features{{list-style:disc;padding-left:18px;}}
    .cat-banner-features li{{font-size:13px;color:#333;margin-bottom:4px;line-height:1.55;}}
    .cat-banner-right{{overflow:hidden;display:flex;align-items:center;justify-content:center;gap:16px;padding:20px 0;}}
    .cat-banner-right img{{height:200px;object-fit:contain;}}
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
    .filter-clear{{font-size:11px;font-weight:700;letter-spacing:0.5px;color:#000;text-transform:uppercase;cursor:pointer;border:none;background:none;padding:0;display:flex;align-items:center;gap:4px;}}
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
<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    <nav><ul class="nav-list">
      <li><a href="#">Comprar</a>
        <div class="mega-menu"><div class="mega-inner">
          <div class="mega-col"><div class="mega-col-title">Cozinhar</div>
            <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
            <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
            <a href="colecao-cacarolas.html">Ca&#231;arolas</a>
            <a href="colecao-antiaderente.html">Antiaderente</a>
            <a href="colecao-acessorios.html">Acess&#243;rios</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Assar</div>
            <a href="colecao-assadeiras-travessas.html">Assadeiras e Travessas</a>
            <a href="colecao-formas-metal-bakeware.html">Formas Metal Bakeware</a>
          </div>
          <div class="mega-col"><div class="mega-col-title">Acess&#243;rios</div>
            <a href="colecao-moedores-e-galheteiro.html">Moedores e Galheteiro</a>
            <a href="colecao-potes-e-porta-mantimentos.html">Potes e Porta-Mantimentos</a>
            <a href="colecao-utensilios.html">Utensilios</a>
            <a href="colecao-utensilios-madeira.html">Utensilios de Madeira</a>
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
</header>

<div class="cat-banner-wrap">
<div class="cat-banner">
  <div class="cat-banner-left">
    <div class="cat-banner-crumb">
      <a href="index.html">In&#237;cio</a><span style="color:#ccc;">/</span>
      <a href="colecao-acessorios.html">Acess&#243;rios</a><span style="color:#ccc;">/</span>
      <span style="color:#555;">Potes e Porta-Mantimentos</span>
    </div>
    <h1 class="cat-banner-title">Potes e Porta-Mantimentos</h1>
    <ul class="cat-banner-features">
      <li>Cer&#226;mica esmaltada de alta qualidade para organizar e decorar sua cozinha;</li>
      <li>Porta condimentos, a&#231;ucareiros, manteigueiras e pil&#245;es nas cores ic&#244;nicas;</li>
      <li>Potes com tampa de madeira para armazenamento elegante;</li>
      <li>Garantia de 10 anos contra defeitos de fabrica&#231;&#227;o;</li>
    </ul>
  </div>
  <div class="cat-banner-right">
    <img src="{C}dw96391238/images/porta-condimento-laranja-lecreuset4.png{Q}" alt="Porta Condimento Le Creuset"/>
    <img src="{C}dwf6a18990/images/set-creme-e-a\u00e7ucar-lecreuset6.png{Q}" alt="Set Cream Sugar Le Creuset"/>
    <img src="{C}dw33b55c5c/images/produto-lecreuset-porta-utensilios-sig-vermelho.png{Q}" alt="Porta Utensílios Le Creuset"/>
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
        <label class="filter-option"><input type="checkbox"> Porta Condimentos</label>
        <label class="filter-option"><input type="checkbox"> Potes com Tampa</label>
        <label class="filter-option"><input type="checkbox"> A&#231;ucareiros e Manteigueiras</label>
        <label class="filter-option"><input type="checkbox"> Bowls e Pil&#245;es</label>
        <label class="filter-option"><input type="checkbox"> Porta Utensilios</label>
        <label class="filter-option"><input type="checkbox"> Potes para Gelateia e Mel</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Pre&#231;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> At&#233; R$ 250</label>
        <label class="filter-option"><input type="checkbox"> R$ 250 &#8211; R$ 400</label>
        <label class="filter-option"><input type="checkbox"> R$ 400 &#8211; R$ 600</label>
        <label class="filter-option"><input type="checkbox"> + R$ 600</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">Material
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Cer&#226;mica Esmaltada</label>
        <label class="filter-option"><input type="checkbox"> Ferro Fundido</label>
        <label class="filter-option"><input type="checkbox"> Madeira</label>
        <label class="filter-option"><input type="checkbox"> A&#231;o Inox</label>
        <label class="filter-option"><input type="checkbox"> Silicone</label>
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
        <label class="filter-option"><input type="checkbox"> Marseille</label>
        <label class="filter-option"><input type="checkbox"> Meringue</label>
        <label class="filter-option"><input type="checkbox"> Shell Pink</label>
        <label class="filter-option"><input type="checkbox"> Nectar</label>
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

<footer>
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
function toggleFilter(h){{h.classList.toggle('open');h.nextElementSibling.classList.toggle('open');}}
function swatchClick(e,s,imgId,src){{
  e.preventDefault();e.stopPropagation();
  s.parentElement.querySelectorAll('.swatch').forEach(x=>x.classList.remove('active'));
  s.classList.add('active');
  var el=document.getElementById(imgId);if(el)el.src=src;
}}
</script>
</body></html>"""

path = os.path.join(BASE, "colecao-potes-e-porta-mantimentos.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"  Coleção: colecao-potes-e-porta-mantimentos.html ({N} produtos)")
print("\nTudo criado com sucesso!")
