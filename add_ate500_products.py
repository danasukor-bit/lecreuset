filepath = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ate-500.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

ws = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

# Products to add: (num, name, sub, price, img, link, price_min)
products = [
    (19, "Porta Utensílios Clássico (Nectar)", "Cerâmica", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7c7c80a8/images/porta_utens%C3%ADlios_cl%C3%A1ssico_lecreuset_nectar.jpg?sw=650&sh=650&sm=fit",
     "porta-utensilios-classico.html", 319.0),
    (20, "Set Saleiro &amp; Pimenteiro (Laranja)", "Acessórios · Conjunto", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4b44a6db/images/produto-lecreuset-saleiro-pimenteiro-laranja.png?sw=650&sh=650&sm=fit",
     "#", 319.0),
    (21, "Porta Sal (Nectar)", "Cerâmica", "R$ 379,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw901ca336/images/porta-salnectar.png?sw=650&sh=650&sm=fit",
     "porta-sal.html", 379.0),
    (22, "Set Cream &amp; Sugar (Meringue)", "Cerâmica · Conjunto", "R$ 459,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw96919832/images/set-creme-e-a%C3%A7ucar-meringue.png?sw=650&sh=650&sm=fit",
     "set-creme-e-acucar.html", 459.0),
    (23, "Bowl de Preparo 2L (Nectar)", "Cerâmica", "R$ 429,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5893a5c8/images/bowl-de-preparo-2l-nectar.png?sw=650&sh=650&sm=fit",
     "bowl-de-preparo-2l.html", 429.0),
    (24, "Bowl de Preparo 2L (Shell Pink)", "Cerâmica", "R$ 429,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw772c03d7/images/produto-lecreuset-bowl-preparo-shellpink.png?sw=650&sh=650&sm=fit",
     "bowl-de-preparo-2l.html", 429.0),
    (25, "Porta Sal (Caribe)", "Cerâmica", "R$ 379,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9c0aa443/images/porta_sal_azul_caribe.jpg?sw=650&sh=650&sm=fit",
     "porta-sal.html", 379.0),
    (26, "Porta Utensílios Signature (Shell Pink)", "Cerâmica", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw42b02d93/images/produto-lecreuset-porta-utensilios-sig-shellpink.png?sw=650&sh=650&sm=fit",
     "porta-utensilios-signature.html", 319.0),
    (27, "Travessa Canelada (Vermelho) 24cm", "Cerâmica", "R$ 399,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw678a9329/images/travessa-canelada-vermelho-lecreuset.jpg?sw=650&sh=650&sm=fit",
     "travessa-canelada.html", 399.0),
    (28, "Dispenser para Sabão 580ml (Vermelho)", "Cerâmica", "R$ 439,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw550a8664/images/dispenser-para-sabao-580ml-1.png?sw=650&sh=650&sm=fit",
     "dispenser-para-sabao-580ml.html", 439.0),
    (29, "Porta Condimento Grande (Caribe) 800ml", "Cerâmica", "R$ 439,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dweab9487f/images/porta-condimento-caribe-lecreuset1.png?sw=650&sh=650&sm=fit",
     "porta-condimento.html", 439.0),
    (30, "Porta Utensílios Clássico (Caribe)", "Cerâmica", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4071d03b/images/porta_utens%C3%ADlios_classico_lecreuset_azulcaribe.jpg?sw=650&sh=650&sm=fit",
     "porta-utensilios-classico.html", 319.0),
    (31, "Caneca Abóbora 400ml", "Cerâmica", "R$ 449,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw416d5116/images/80313400900003-caneca-abobora-laranja.jpg?sw=650&sh=650&sm=fit",
     "#", 449.0),
    (32, "Set 2 Pratos Gato", "Cerâmica · Conjunto", "R$ 329,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwbd03e362/images/89401008070009-prato-gato.jpg?sw=650&sh=650&sm=fit",
     "set-2-pratos-gato.html", 329.0),
    (33, "Pote de Manteiga (Branco)", "Cerâmica", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw036055c4/images/produto-lecreuset-pote-manteiga-branco%20(2).png?sw=650&sh=650&sm=fit",
     "pote-de-manteiga.html", 319.0),
    (34, "Multi Bowl Jardin (Sea Salt) 3.6L", "Cerâmica", "R$ 433,30",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3ffb5093/images/multi-bowl-jardin-3,6l-sea%20salt%20(2).png?sw=650&sh=650&sm=fit",
     "multi-bowl-jardin.html", 433.3),
    (35, "Porta Utensílios Clássico Grande (Cerise)", "Cerâmica · 2.3L", "R$ 449,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1e87ec35/images/porta_utensilios_2,3_cerise_le_creuset.jpg?sw=650&sh=650&sm=fit",
     "porta-utensilios-classico.html", 449.0),
    (36, "Moedor de Sal 21cm (Bleu Riviera)", "Acessórios", "R$ 369,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw33faad65/images/44001210995200-moedor-bleu.jpg?sw=650&sh=650&sm=fit",
     "#", 369.0),
    (37, "Set 2 Pratos Flower 23cm (Cool Mint)", "Cerâmica · Conjunto", "R$ 329,40",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5dca48b0/images/Flower-coolmint-fotos-primavera.png?sw=650&sh=650&sm=fit",
     "set-2-pratos-flower-23cm.html", 329.4),
    (38, "Pilão (Meringue)", "Cerâmica", "R$ 379,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd7f83aef/images/pilao-meringue-lecreuset.jpg?sw=650&sh=650&sm=fit",
     "pilao.html", 379.0),
    (39, "Porta Óleo 600ml (Azure)", "Cerâmica", "R$ 299,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4b9f9a78/images/porta-oleo-lecreuset-2.png?sw=650&sh=650&sm=fit",
     "porta-oleo-600ml.html", 299.0),
    (40, "Pote de Manteiga (Azure)", "Cerâmica", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw305b7154/images/pote-manteiga-freancesa-azure.png?sw=650&sh=650&sm=fit",
     "pote-de-manteiga.html", 319.0),
    (41, "Porta Óleo 600ml (Vermelho)", "Cerâmica", "R$ 299,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7ac533d2/images/porta-oleo-lecreuset-4.png?sw=650&sh=650&sm=fit",
     "porta-oleo-600ml.html", 299.0),
    (42, "Pote para Mostarda (Dijon)", "Cerâmica", "R$ 379,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8878da41/images/pote-para-mostarda-lecreuset-djon1.png?sw=650&sh=650&sm=fit",
     "pote-para-mostarda.html", 379.0),
    (43, "Moedor de Pimenta 21cm (Laranja)", "Acessórios", "R$ 369,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb7c75690/images/produto-lecreuset-moedores-laranja.png?sw=650&sh=650&sm=fit",
     "#", 369.0),
    (44, "Lancheira 900ml OTG (Shell Pink)", "Acessórios", "R$ 439,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2349b817/images/Lancheira-900ml-Otg-shellpink.png?sw=650&sh=650&sm=fit",
     "lancheira-900ml.html", 439.0),
    (45, "Set Saleiro &amp; Pimenteiro (Branco)", "Acessórios · Conjunto", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb2c50bea/images/produto-lecreuset-saleiro-pimenteiro-branco.png?sw=650&sh=650&sm=fit",
     "#", 319.0),
    (46, "Manteigueira (Branco)", "Cerâmica", "R$ 429,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw079f60e5/images/manteigueira_branca_leceruset.jpg?sw=650&sh=650&sm=fit",
     "manteigueira.html", 429.0),
    (47, "Forma de Pão Retangular Canelada (Bleu Riviera)", "Cerâmica", "R$ 339,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dweea847ff/images/71115230990001-foma-de-pao-canelada.jpg?sw=650&sh=650&sm=fit",
     "forma-pao.html", 339.0),
    (48, "Moedor de Pimenta 21cm (Bleu Riviera)", "Acessórios", "R$ 369,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw33faad65/images/44001210995200-moedor-bleu.jpg?sw=650&sh=650&sm=fit",
     "#", 369.0),
    (49, "Porta Utensílios Clássico Grande (Laranja)", "Cerâmica · 2.3L", "R$ 449,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7877f880/images/porta_utensilios_grande_classico_laranja_lecreuset.jpg?sw=650&sh=650&sm=fit",
     "porta-utensilios-classico.html", 449.0),
    (50, "Bowl Redondo Vancouver (Branco) 24cm", "Cerâmica", "R$ 439,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwcac5bb55/images/produto-lecreuset-bowl-24cm-branco.png?sw=650&sh=650&sm=fit",
     "bowl-redondo-vancouver.html", 439.0),
    (51, "Bule com Infusor (Laranja)", "Cerâmica", "R$ 299,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa238f955/images/bule_de_cha_com_infusor_flame_le_creuset.jpg?sw=650&sh=650&sm=fit",
     "#", 299.0),
    (52, "Porta Sal (Branco)", "Cerâmica", "R$ 379,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw73999081/images/porta_sal_branco.jpg?sw=650&sh=650&sm=fit",
     "porta-sal.html", 379.0),
    (53, "Vaso 1L (Vermelho)", "Cerâmica", "R$ 349,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe0330bcd/images/vaso-1l-vermelho.png?sw=650&sh=650&sm=fit",
     "vaso-1l.html", 349.0),
    (54, "Travessa Retangular Heritage (Bleu Riviera) 19cm", "Cerâmica", "R$ 349,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1876dd56/images/71102190990001-travessa-retangular.jpg?sw=650&sh=650&sm=fit",
     "travessa-retangular-heritage.html", 349.0),
    (55, "Bowl de Preparo 2L (Azure)", "Cerâmica", "R$ 429,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdf36e0a4/images/bowl-para-preprro-azure.png?sw=650&sh=650&sm=fit",
     "bowl-de-preparo-2l.html", 429.0),
    (56, "Mini Cocotte Abóbora (Thyme)", "Cerâmica", "R$ 449,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw09066156/images/mini-cocotte-abobora-thyme-2026.png?sw=650&sh=650&sm=fit",
     "mini-cocotte-abobora.html", 449.0),
    (57, "Porta Utensílios Signature (Caribe)", "Cerâmica", "R$ 319,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe50cc6ff/images/produto-lecreuset-porta-utensilios-sig-caribe.png?sw=650&sh=650&sm=fit",
     "porta-utensilios-signature.html", 319.0),
]

cards_html = ""
for num, name, sub, price, img, link, price_min in products:
    cards_html += f"""
    <!-- {num} -->
    <div class="product-card" data-price-min="{price_min}">
      <a href="{link}">
        <div class="product-card-img">
          <img src="{img}" alt="{name}" />
          {ws}
        </div>
      </a>
      <a href="{link}">
        <div class="product-card-name">{name}</div>
        <div class="product-card-sub">{sub}</div>
        <div class="product-card-price">{price}</div>
      </a>
    </div>"""

# Insert before closing
old = """    </div>
  </div>
</div>
<footer>"""
new = f"""{cards_html}

    </div>
  </div>
</div>
<footer>"""

content = content.replace(old, new, 1)

# Update counts (18 original + 39 new = 57... wait let me count)
total = 18 + len(products)  # 18 + 39 = 57
content = content.replace('<strong>18</strong> resultados', f'<strong>{total}</strong> resultados')
content = content.replace('18 produtos', f'{total} produtos')

# Also add data-price-min to original cards that lack it
originals = [
    ('<!-- 1. Porta Utensílios Clássico -->\n    <div class="product-card">', 319.0),
    ('<!-- 2. Moedor de Sal 21cm -->\n    <div class="product-card">', 369.0),
    ('<!-- 3. Moedor de Pimenta 21cm -->\n    <div class="product-card">', 369.0),
    ('<!-- 4. Pote de Manteiga (Caribe) -->\n    <div class="product-card">', 319.0),
    ('<!-- 5. Saleiro Redondo Madeira Teca -->\n    <div class="product-card">', 349.0),
    ('<!-- 6. Travessa Retangular Heritage (26cm) -->\n    <div class="product-card">', 349.0),
    ('<!-- 7. Porta Sal -->\n    <div class="product-card">', 379.0),
    ('<!-- 8. Vaso para Ervas com Bandeja -->\n    <div class="product-card">', 289.0),
    ('<!-- 9. Açucareiro -->\n    <div class="product-card">', 259.0),
    ('<!-- 10. Set Saleiro & Pimenteiro -->\n    <div class="product-card">', 319.0),
    ('<!-- 11. Moedor de Sal em Madeira 21cm -->\n    <div class="product-card">', 369.0),
    ('<!-- 12. Moedor de Pimenta em Madeira 21cm -->\n    <div class="product-card">', 369.0),
    ('<!-- 13. Bowl de Preparo 2L -->\n    <div class="product-card">', 429.0),
    ('<!-- 14. Porta Óleo 600ml -->\n    <div class="product-card">', 299.0),
    ('<!-- 15. Garrafa de Hidratação -->\n    <div class="product-card">', 289.0),
    ('<!-- 16. Moedor de Pimenta 30cm -->\n    <div class="product-card">', 479.0),
    ('<!-- 17. Moedor de Sal 30cm -->\n    <div class="product-card">', 479.0),
]

fixed = 0
for old_str, pm in originals:
    new_str = old_str.replace('<div class="product-card">', f'<div class="product-card" data-price-min="{pm}">')
    if old_str in content:
        content = content.replace(old_str, new_str, 1)
        fixed += 1

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Added {len(products)} new products. Total: {total}")
print(f"Added data-price-min to {fixed} original cards")
