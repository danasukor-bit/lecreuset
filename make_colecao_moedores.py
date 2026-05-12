#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset"
CDN  = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
Q    = "?sw=650&sh=650&sm=fit"

WISHLIST_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# helper: create one product card
def card(img_id, href, img_src, alt, name, sub, price, swatches_html):
    return f"""    <div class="product-card">
      <a href="{href}">
        <div class="product-card-img">
          <img id="{img_id}" src="{img_src}" alt="{alt}"/>
          <div class="product-wishlist">{WISHLIST_SVG}</div>
        </div>
      </a>
      <a href="{href}">
        <div class="product-card-name">{name}</div>
        <div class="product-card-sub">{sub}</div>
        <div class="product-card-price">{price}</div>
      </a>
      <div class="card-swatches">{swatches_html}</div>
    </div>"""

# helper: swatch span (with optional filter for hue-rotate simulation)
def sw(img_id, hex_color, label, url, filt="", active=False, border=""):
    active_class = " active" if active else ""
    border_style = f"border:1.5px solid {border};" if border else "border:1.5px solid transparent;"
    if filt:
        onclick = f"swatchClick(event,this,'{img_id}','{url}','{filt}')"
    else:
        onclick = f"swatchClick(event,this,'{img_id}','{url}','')"
    return f'<span class="swatch{active_class}" style="background:{hex_color};{border_style}" onclick="{onclick}" title="{label}"></span>'


# ── product definitions ───────────────────────────────────────────────────────

# 21cm base image (vermelho) — others use CSS hue-rotate
IMG_21  = CDN + "dw7138e9be/images/produto-lecreuset-moedores-vermelho.png" + Q
COLORS_21 = [
    ("#C41E3A","Vermelho",  IMG_21, ""),
    ("#FE5000","Laranja",   IMG_21, "hue-rotate(-30deg) saturate(1.4)"),
    ("#0066B2","Bleu Riviera", IMG_21, "hue-rotate(200deg) saturate(1.3)"),
    ("#007FFF","Azure",     IMG_21, "hue-rotate(195deg) saturate(1.5)"),
    ("#FFB347","Nectar",    IMG_21, "hue-rotate(-20deg) saturate(1.2) brightness(1.1)"),
    ("#1a1a1a","Black Onyx",IMG_21, "saturate(0) brightness(0.1)"),
]

# 30cm specific images
IMG_30_LAR = CDN + "dw385cddde/images/tardes%20de%20verao/moedor-de-pimenta-30cm-laranja.png" + Q
IMG_30_VER = CDN + "dw6de01276/images/tardes%20de%20verao/moedor-de-pimenta-30cm-vermelho.png" + Q
IMG_30_BLK = CDN + "dw703f2293/images/tardes%20de%20verao/moedor-de-pimenta-30cm-blackonyx.png" + Q

# madeira
IMG_MAD_SAL = CDN + "dw7c2c8aec/images/moedor-de-madeira-de-sal.png" + Q
IMG_MAD_PIM = CDN + "dwef3671a4/images/moedor-de-madeira-de-pimenta.png" + Q

# modern bluebell
IMG_MOD_SAL = CDN + "dwa69e3f54/images/moedor-Modern-Bluebell-sal.png" + Q
IMG_MOD_PIM = CDN + "dwdb71c36f/images/moedor-Modern-Bluebell-pimenta.png" + Q

# set coracao
IMG_COR_VER = CDN + "dw7e22f027/images/kit-saleiro-pimenteiro-vermelho.png" + Q
IMG_COR_SHA = CDN + "dw20fde0be/images/kit-saleiro-pimenteiro-shallot.png" + Q
IMG_COR_BRA = CDN + "dwee16c0e3/images/kit-saleiro-pimenteiro-branco.png" + Q

# others
IMG_TECA  = CDN + "dw3df69a85/images/saleiro-redondo-madeira-teca.png" + Q
IMG_AZV   = CDN + "dwe9691760/images/80803020600003.jpg" + Q
IMG_TAMPA = CDN + "dwf311dea5/images/produto-lecreuset-tampa-set-silicone.png" + Q


def swatches_21(img_id):
    out = ""
    for i, (hex_c, lbl, url, filt) in enumerate(COLORS_21):
        out += sw(img_id, hex_c, lbl, url, filt, active=(i==0))
    return out

cards = []

# 1. Moedor de Sal 21cm
cards.append(card(
    "img_moedorsal21", "moedor-sal-21cm.html",
    IMG_21, "Moedor de Sal 21cm",
    "Moedor de Sal 21cm", "Pl&#225;stico ABS · Mecanismo Cer&#226;mico", "R$ 369,00",
    swatches_21("img_moedorsal21")
))

# 2. Moedor de Pimenta 21cm
cards.append(card(
    "img_moedorpimenta21", "moedor-pimenta-21cm.html",
    IMG_21, "Moedor de Pimenta 21cm",
    "Moedor de Pimenta 21cm", "Pl&#225;stico ABS · Mecanismo Cer&#226;mico", "R$ 369,00",
    swatches_21("img_moedorpimenta21")
))

# 3. Moedor de Sal 30cm
cards.append(card(
    "img_moedorsal30", "moedor-sal-30cm.html",
    IMG_30_VER, "Moedor de Sal 30cm",
    "Moedor de Sal 30cm", "Pl&#225;stico ABS · Mecanismo Cer&#226;mico", "R$ 479,00",
    sw("img_moedorsal30","#C41E3A","Vermelho",IMG_30_VER,"",True) +
    sw("img_moedorsal30","#FE5000","Laranja",IMG_30_LAR,"") +
    sw("img_moedorsal30","#1a1a1a","Black Onyx",IMG_30_BLK,"")
))

# 4. Moedor de Pimenta 30cm
cards.append(card(
    "img_moedorpimenta30", "moedor-pimenta-30cm.html",
    IMG_30_LAR, "Moedor de Pimenta 30cm",
    "Moedor de Pimenta 30cm", "Pl&#225;stico ABS · Mecanismo Cer&#226;mico", "R$ 479,00",
    sw("img_moedorpimenta30","#FE5000","Laranja",IMG_30_LAR,"",True) +
    sw("img_moedorpimenta30","#C41E3A","Vermelho",IMG_30_VER,"") +
    sw("img_moedorpimenta30","#1a1a1a","Black Onyx",IMG_30_BLK,"")
))

# 5. Moedor de Sal em Madeira 21cm
cards.append(card(
    "img_moedoralmadeira", "moedor-sal-madeira-21cm.html",
    IMG_MAD_SAL, "Moedor de Sal em Madeira 21cm",
    "Moedor de Sal em Madeira 21cm", "Madeira · Mecanismo Cer&#226;mico", "R$ 369,00",
    sw("img_moedoralmadeira","#8B5E3C","Madeira",IMG_MAD_SAL,"",True)
))

# 6. Moedor de Pimenta em Madeira 21cm
cards.append(card(
    "img_moedorpimentamadeira", "moedor-pimenta-madeira-21cm.html",
    IMG_MAD_PIM, "Moedor de Pimenta em Madeira 21cm",
    "Moedor de Pimenta em Madeira 21cm", "Madeira · Mecanismo Cer&#226;mico", "R$ 369,00",
    sw("img_moedorpimentamadeira","#8B5E3C","Madeira",IMG_MAD_PIM,"",True)
))

# 7. Moedor de Sal Modern 21cm
cards.append(card(
    "img_moedoralmoder", "moedor-sal-modern-21cm.html",
    IMG_MOD_SAL, "Moedor de Sal Modern 21cm",
    "Moedor de Sal Modern 21cm", "Cole&#231;&#227;o Modern · Bluebell Purple", "R$ 369,00",
    sw("img_moedoralmoder","#8B73C4","Bluebell Purple",IMG_MOD_SAL,"",True)
))

# 8. Moedor de Pimenta Modern 21cm
cards.append(card(
    "img_moedorpimentamodern", "moedor-pimenta-modern-21cm.html",
    IMG_MOD_PIM, "Moedor de Pimenta Modern 21cm",
    "Moedor de Pimenta Modern 21cm", "Cole&#231;&#227;o Modern · Bluebell Purple", "R$ 369,00",
    sw("img_moedorpimentamodern","#8B73C4","Bluebell Purple",IMG_MOD_PIM,"",True)
))

# 9. Set Saleiro & Pimenteiro Coração
cards.append(card(
    "img_setcoracao", "set-saleiro-pimenteiro-coracao.html",
    IMG_COR_VER, "Set Saleiro &amp; Pimenteiro Cora&#231;&#227;o",
    "Set Saleiro &amp; Pimenteiro Cora&#231;&#227;o", "Cer&#226;mica Esmaltada", "R$ 379,00",
    sw("img_setcoracao","#C41E3A","Vermelho",IMG_COR_VER,"",True) +
    sw("img_setcoracao","#E8A0A0","Shallot",IMG_COR_SHA,"") +
    sw("img_setcoracao","#FFFFFF","Branco",IMG_COR_BRA,"","","#ccc")
))

# 10. Saleiro Redondo de Madeira Teca
cards.append(card(
    "img_saleiromadeira", "saleiro-redondo-madeira-teca.html",
    IMG_TECA, "Saleiro Redondo de Madeira Teca 160ml",
    "Saleiro Redondo de Madeira Teca 160ml", "Madeira Teca · 160ml", "R$ 349,00",
    sw("img_saleiromadeira","#6B4226","Teca",IMG_TECA,"",True)
))

# 11. Set Azeite & Vinagre Clássico
cards.append(card(
    "img_setazeite", "set-azeite-vinagre.html",
    IMG_AZV, "Set Azeite &amp; Vinagre Cl&#225;ssico",
    "Set Azeite &amp; Vinagre Cl&#225;ssico", "Cer&#226;mica Esmaltada", "R$ 579,00",
    sw("img_setazeite","#C41E3A","Vermelho",IMG_AZV,"",True)
))

# 12. Set Tampa para Moedores 21cm
cards.append(card(
    "img_settampa", "set-tampa-moedores.html",
    IMG_TAMPA, "Set Tampa para Moedores 21cm",
    "Set Tampa para Moedores 21cm", "Silicone", "R$ 79,00",
    sw("img_settampa","#C41E3A","Vermelho",IMG_TAMPA,"",True)
))


GRID = "\n".join(cards)
N = len(cards)

PAGE = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Moedores e Galheteiro | Le Creuset Brasil</title>
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
    /* banner */
    .cat-banner-wrap{{border-bottom:1px solid #e0e0e0;}}
    .cat-banner{{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr 1fr;min-height:260px;}}
    .cat-banner-left{{padding:28px 40px 28px 0;display:flex;flex-direction:column;justify-content:center;}}
    .cat-banner-crumb{{font-size:12px;color:#888;display:flex;gap:5px;align-items:center;margin-bottom:14px;flex-wrap:wrap;}}
    .cat-banner-crumb a{{color:#888;}} .cat-banner-crumb a:hover{{color:#000;text-decoration:underline;}}
    .cat-banner-title{{font-size:26px;font-weight:700;color:#000;margin-bottom:12px;}}
    .cat-banner-features{{list-style:disc;padding-left:18px;}}
    .cat-banner-features li{{font-size:13px;color:#333;margin-bottom:4px;line-height:1.55;}}
    .cat-banner-right{{overflow:hidden;max-height:300px;display:flex;align-items:center;justify-content:center;gap:20px;padding:24px 0;}}
    .cat-banner-right img{{height:220px;object-fit:contain;}}
    /* shop */
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
    .filter-clear:hover{{text-decoration:underline;}}
    .results-bar{{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;}}
    .results-count{{font-size:13px;color:#888;}}
    .sort-select{{font-size:13px;border:1px solid #ccc;padding:6px 12px;font-family:inherit;cursor:pointer;}}
    .product-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;}}
    .product-card{{position:relative;}}
    .product-card-img{{position:relative;overflow:hidden;background:#fff;aspect-ratio:1;margin-bottom:10px;border:1px solid #f0f0f0;}}
    .product-card-img img{{width:100%;height:100%;object-fit:contain;padding:16px;transition:transform 0.4s ease,filter 0.3s;}}
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
                <a href="colecao-moedores-e-galheteiro.html">Moedores e Galheteiro</a>
                <a href="colecao-utensilios.html">Utensilios</a>
                <a href="colecao-utensilios-madeira.html">Utensilios de Madeira</a>
                <a href="colecao-suporte-descansos.html">Suportes e Descansos</a>
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

<div class="cat-banner-wrap">
<div class="cat-banner">
  <div class="cat-banner-left">
    <div class="cat-banner-crumb">
      <a href="index.html">In&#237;cio</a><span style="color:#ccc;">/</span>
      <a href="colecao-acessorios.html">Acess&#243;rios</a><span style="color:#ccc;">/</span>
      <span style="color:#555;">Moedores e Galheteiro</span>
    </div>
    <h1 class="cat-banner-title">Moedores e Galheteiro</h1>
    <ul class="cat-banner-features">
      <li>Moedores com mecanismo cer&#226;mico ajust&#225;vel de alta precis&#227;o;</li>
      <li>Dispon&#237;veis em 21cm e 30cm, nas cores ic&#244;nicas Le Creuset;</li>
      <li>Op&#231;&#245;es em pl&#225;stico ABS, madeira e cer&#226;mica esmaltada;</li>
      <li>Garantia de 10 anos contra defeitos de fabrica&#231;&#227;o;</li>
    </ul>
  </div>
  <div class="cat-banner-right">
    <img src="{IMG_30_VER}" alt="Moedor 30cm Vermelho Le Creuset"/>
    <img src="{IMG_30_LAR}" alt="Moedor 30cm Laranja Le Creuset"/>
  </div>
</div>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Tipo
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Moedores de Sal</label>
        <label class="filter-option"><input type="checkbox"> Moedores de Pimenta</label>
        <label class="filter-option"><input type="checkbox"> Saleiros</label>
        <label class="filter-option"><input type="checkbox"> Sets e Kits</label>
        <label class="filter-option"><input type="checkbox"> Acess&#243;rios</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Pre&#231;o
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> At&#233; R$ 100</label>
        <label class="filter-option"><input type="checkbox"> R$ 100 &#8211; R$ 300</label>
        <label class="filter-option"><input type="checkbox"> R$ 300 &#8211; R$ 500</label>
        <label class="filter-option"><input type="checkbox"> + R$ 500</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Material
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Pl&#225;stico ABS</label>
        <label class="filter-option"><input type="checkbox"> Madeira</label>
        <label class="filter-option"><input type="checkbox"> Cer&#226;mica</label>
        <label class="filter-option"><input type="checkbox"> Silicone</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Cor
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Vermelho</label>
        <label class="filter-option"><input type="checkbox"> Laranja</label>
        <label class="filter-option"><input type="checkbox"> Bleu Riviera</label>
        <label class="filter-option"><input type="checkbox"> Black Onyx</label>
        <label class="filter-option"><input type="checkbox"> Bluebell Purple</label>
        <label class="filter-option"><input type="checkbox"> Madeira</label>
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
{GRID}
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
function swatchClick(e,s,imgId,src,filt){{
  e.preventDefault();e.stopPropagation();
  s.parentElement.querySelectorAll('.swatch').forEach(x=>x.classList.remove('active'));
  s.classList.add('active');
  var el=document.getElementById(imgId);
  if(el){{el.src=src;el.style.filter=filt||'';}}
}}
</script>
</body>
</html>"""

path = os.path.join(BASE, "colecao-moedores-e-galheteiro.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"Criado: colecao-moedores-e-galheteiro.html  ({len(PAGE)} chars)")
