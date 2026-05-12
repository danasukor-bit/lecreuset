import re

filepath = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ate-999.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

wishlist_svg = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

new_products = [
    # (num, name, sub, price, sale_price, orig_price, img, link, badge, price_min)
    (16, "Frigideira Funda 3-Ply Signature 24cm", "3-Ply Aço Inox", None, "R$ 895,30", "R$ 1.279,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw58a73101/images/frigideira_sem_anti_aderente_3ply_lecreuset.jpg?sw=650&sh=650&sm=fit",
     "frigideira-funda-3ply.html", "sale", 895.30),

    (17, "Suporte para Bolo (Branco)", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1da69c43/images/suporte-para-bolo4.png?sw=650&sh=650&sm=fit",
     "suporte-para-bolo.html", None, 709.0),

    (18, "Set 3 Espátulas e 1 Pincel Craft (Meringue)", "Acessórios · Conjunto", "R$ 769,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw73a85cc7/images/set-3-espatulas-1-pincel-craft-com-porta-utensilios-meringue.png?sw=650&sh=650&sm=fit",
     "set-espatulas-pincel-craft.html", None, 769.0),

    (19, "Travessa Retangular Heritage (Cayenne) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw95ec4ff6/images/travessas-produto-lecreuset-heritage-cayenne.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (20, "Travessa Retangular Heritage (Flame) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwf31b1dc6/images/travessas-produto-lecreuset-heritage-laranja.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (21, "Set Azeite &amp; Vinagre Signature (Thyme)", "Acessórios · Conjunto", "R$ 629,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwf1aa168f/images/80842301730003-oleo-e-vinagre-thyme.jpg?sw=650&sh=650&sm=fit",
     "#", None, 629.0),

    (22, "Stockpot (Branco) 22cm", "Ferro Fundido", "R$ 959,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw25e2b9f6/images/stockpot-branco-lecreuset-2025.png?sw=650&sh=650&sm=fit",
     "#", None, 959.0),

    (23, "Set Canecas 350ml Gift Collection", "Cerâmica · Conjunto", "R$ 879,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9430574f/images/gift-collection-350ml-lecreuset-2025-1.png?sw=650&sh=650&sm=fit",
     "#", None, 879.0),

    (24, "Stockpot Pegador Aço Inox (Laranja) 20cm", "Ferro Fundido", "R$ 769,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw250b1a0b/images/stockpot-pegador-inox-laranja.png?sw=650&sh=650&sm=fit",
     "#", None, 769.0),

    (25, "Bandeja de Servir Oval Jardin (Meringue) 36cm", "Cerâmica", "R$ 529,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe6e4c3ef/images/bandeja-de-servir-oval-jardin-36cm-meringue.png?sw=650&sh=650&sm=fit",
     "bandeja-de-servir-oval-jardin.html", None, 529.0),

    (26, "Chaleira Kone (Cool Mint)", "Aço Esmaltado", "R$ 839,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw02de7c18/images/chaleira-kone-coolmint.png?sw=650&sh=650&sm=fit",
     "chaleira-kone.html", None, 839.0),

    (27, "Travessa Retangular Heritage (Caribe) 26cm", "Cerâmica", "R$ 529,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaa2a8d47/images/travessas-produto-lecreuset-heritage-caribe.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 529.0),

    (28, "Set Azeite &amp; Vinagre Clássico (Laranja)", "Acessórios · Conjunto", "R$ 579,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1bcf6eba/images/set-azeite-vinagre-laranja.png?sw=650&sh=650&sm=fit",
     "#", None, 579.0),

    (29, "Travessa Retangular Heritage (Shell Pink) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5afbbb92/images/travessas-produto-lecreuset-heritage-shellpink%20(5).png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (30, "Pote para Biscoito (Caribe) 2L", "Cerâmica", "R$ 649,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2fc2f54/images/Pote-para-biscoito-caribe.png?sw=650&sh=650&sm=fit",
     "pote-para-biscoito.html", None, 649.0),

    (31, "Travessa com Tampa (Bleu Riviera)", "Cerâmica", "R$ 999,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1c630c59/images/79126310990080-travessa-com-tampa-2.jpg?sw=650&sh=650&sm=fit",
     "#", None, 999.0),

    (32, "Travessa Retangular Heritage (Vermelho) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw49913c7c/images/travessas-produto-lecreuset-heritage-vermelho.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (33, "Bandeja de Servir Oval Jardin (Sea Salt) 36cm", "Cerâmica", "R$ 529,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7f32c691/images/bandeja-de-servir-oval-jardin-36cm-sea-salt.png?sw=650&sh=650&sm=fit",
     "bandeja-de-servir-oval-jardin.html", None, 529.0),

    (34, "Travessa Retangular Heritage (Meringue) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw61a9b6d1/images/travessas-produto-lecreuset-heritage-meringue1.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (35, "Travessa Canelada (Vermelho)", "Cerâmica", "R$ 529,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw678a9329/images/travessa-canelada-vermelho-lecreuset.jpg?sw=650&sh=650&sm=fit",
     "travessa-canelada.html", None, 529.0),

    (36, "Travessa Canelada (Laranja)", "Cerâmica", "R$ 529,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8937f1cb/images/Travessa-canelada-laranja-lecreuset.jpg?sw=650&sh=650&sm=fit",
     "travessa-canelada.html", None, 529.0),

    (37, "Travessa Terrine Heritage 1.1L", "Cerâmica", "R$ 789,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw49089fea/images/82013100600009-travessa-terrine-vermelho.jpg?sw=650&sh=650&sm=fit",
     "travessa-terrine-heritage.html", None, 789.0),

    (38, "Caçarola Aço Esmaltado (Creme)", "Aço Esmaltado", "R$ 849,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw63aa120b/images/56002204812600-mini-stockpot-flores.jpg?sw=650&sh=650&sm=fit",
     "cacarola-aco-esmaltado.html", None, 849.0),

    (39, "Chaleira Clássica (Laranja)", "Aço Esmaltado", "R$ 929,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc63ba8a3/images/92009500090000.jpg?sw=650&sh=650&sm=fit",
     "chaleira-classica.html", None, 929.0),

    (40, "Bowl de Servir Ruffle (Branco)", "Cerâmica", "R$ 769,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw580e185a/images/bowl-de-servir-ruffle-white%20(2).png?sw=650&sh=650&sm=fit",
     "bowl-de-servir-ruffle.html", None, 769.0),

    (41, "Set 2 Canecas 200ml com Pires (Laranja)", "Cerâmica · Conjunto", "R$ 579,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw524d5e68/images/set-2-canecas-expresso-laranja.png?sw=650&sh=650&sm=fit",
     "set-2-canecas-200ml-com-pires.html", None, 579.0),

    (42, "Travessa Retangular Heritage (Artichaut) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw997a2d43/images/travessas-produto-lecreuset-heritage-artichaut1.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (43, "Set 3 Espátulas e Pincel (Laranja)", "Acessórios · Conjunto", "R$ 769,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw24351e58/images/set-4-espatulas-com-porta-tensilios-laranja.png?sw=650&sh=650&sm=fit",
     "set-espatulas-pincel-craft.html", None, 769.0),

    (44, "Set 5 Mini Pratos Pétalas", "Cerâmica · Conjunto", "R$ 659,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw408ec32f/images/Set%205%20Mini%20Pratos%20Petalas%20(2).png?sw=650&sh=650&sm=fit",
     "set-5-mini-pratos-petalas.html", None, 659.0),

    (45, "Chaleira Kone (Meringue)", "Aço Esmaltado", "R$ 839,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd0f0a5d6/images/chaleira-kone-meringue-lecreuset.jpg?sw=650&sh=650&sm=fit",
     "chaleira-kone.html", None, 839.0),

    (46, "Set Azeite &amp; Vinagre Clássico (Onyx)", "Acessórios · Conjunto", "R$ 579,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb12346a8/images/80803021400003.jpg?sw=650&sh=650&sm=fit",
     "#", None, 579.0),

    (47, "Prensa Francesa (Branco)", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa8efb6e0/images/prensa-francesa-white-lc%20(2).png?sw=650&sh=650&sm=fit",
     "#", None, 709.0),

    (48, "Set 12 Formas Mini Cocotte", "Metal Bakeware · Conjunto", "R$ 559,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd3dcfeb9/images/Set-Formas-12-Mini-Cocotte.png?sw=650&sh=650&sm=fit",
     "set-12-formas-mini-cocotte.html", None, 559.0),

    (49, "Porta Mantimentos (Cerise)", "Cerâmica", "R$ 549,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc773011e/images/porta-mantimentos-vermelho-lecreuset.png?sw=650&sh=650&sm=fit",
     "porta-mantimentos.html", None, 549.0),

    (50, "Stockpot Pegador Aço Inox (Vermelho) 20cm", "Ferro Fundido", "R$ 769,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwcbd4a957/images/stockpot-pegador-inox-vermelho.png?sw=650&sh=650&sm=fit",
     "#", None, 769.0),

    (51, "Pote para Biscoito (Meringue) 2L", "Cerâmica", "R$ 649,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5d5c5336/images/pote-biscoito-meringue-lc.png?sw=650&sh=650&sm=fit",
     "pote-para-biscoito.html", None, 649.0),

    (52, "Travessa Retangular Heritage (Caribe) 32cm", "Cerâmica", "R$ 709,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaa2a8d47/images/travessas-produto-lecreuset-heritage-caribe.png?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", None, 709.0),

    (53, "Travessa Terrine Heritage 700ml", "Cerâmica", "R$ 599,00", None, None,
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dweed1aa5a/images/81013700600009-terrine-vermelho.jpg?sw=650&sh=650&sm=fit",
     "travessa-terrine-heritage.html", None, 599.0),
]

cards_html = ""
for p in new_products:
    num, name, sub, price, sale_price, orig_price, img, link, badge, price_min = p
    badge_html = ""
    if badge == "sale":
        badge_html = '<div class="product-badge sale">SALE</div>'
    elif badge == "new":
        badge_html = '<div class="product-badge new">NOVO</div>'
    elif badge:
        badge_html = f'<div class="product-badge">{badge}</div>'

    if sale_price:
        price_html = f"""        <div class="product-card-price-orig">{orig_price}</div>
        <div class="product-card-price-sale">{sale_price}</div>"""
    else:
        price_html = f'        <div class="product-card-price">{price}</div>'

    card = f"""
    <!-- {num} -->
    <div class="product-card" data-price-min="{price_min}">
      <a href="{link}">
        <div class="product-card-img">
          <img src="{img}" alt="{name}" />
          {badge_html}{wishlist_svg}
        </div>
      </a>
      <a href="{link}">
        <div class="product-card-name">{name}</div>
        <div class="product-card-sub">{sub}</div>
{price_html}
      </a>
    </div>"""
    cards_html += card

# Insert before closing product-grid div
old_end = """    </div>
  </div>
</div>
<footer>"""

new_end = f"""{cards_html}

    </div>
  </div>
</div>
<footer>"""

content = content.replace(old_end, new_end, 1)

# Update product counts
content = content.replace('<strong>15</strong> resultados', '<strong>53</strong> resultados')
content = content.replace('15 produtos', '53 produtos')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Added {len(new_products)} products. Total now: 53")
