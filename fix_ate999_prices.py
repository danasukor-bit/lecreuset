import re

filepath = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ate-999.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add data-price-min to the 14 original cards that don't have it
# Format: (comment text to find, price_min value)
fixes = [
    ("<!-- 1. Travessa Retangular Heritage -->\n    <div class=\"product-card\">",
     "<!-- 1. Travessa Retangular Heritage -->\n    <div class=\"product-card\" data-price-min=\"529.0\">"),
    ("<!-- 2. Molheira Abóbora 400ml -->\n    <div class=\"product-card\">",
     "<!-- 2. Molheira Abóbora 400ml -->\n    <div class=\"product-card\" data-price-min=\"549.0\">"),
    ("<!-- 3. Set Azeite & Vinagre Clássico -->\n    <div class=\"product-card\">",
     "<!-- 3. Set Azeite & Vinagre Clássico -->\n    <div class=\"product-card\" data-price-min=\"579.0\">"),
    ("<!-- 4. Set Azeite & Vinagre Signature -->\n    <div class=\"product-card\">",
     "<!-- 4. Set Azeite & Vinagre Signature -->\n    <div class=\"product-card\" data-price-min=\"629.0\">"),
    ("<!-- 5. Set Caneca 100ml Gift Collection -->\n    <div class=\"product-card\">",
     "<!-- 5. Set Caneca 100ml Gift Collection -->\n    <div class=\"product-card\" data-price-min=\"639.0\">"),
    ("<!-- 6. Set 2 Assadeiras Retangulares -->\n    <div class=\"product-card\">",
     "<!-- 6. Set 2 Assadeiras Retangulares -->\n    <div class=\"product-card\" data-price-min=\"639.0\">"),
    ("<!-- 7. Stockpot Pegador Fenólico (SALE) -->\n    <div class=\"product-card\">",
     "<!-- 7. Stockpot Pegador Fenólico (SALE) -->\n    <div class=\"product-card\" data-price-min=\"671.3\">"),
    ("<!-- 8. Travessa Retangular Heritage 32cm -->\n    <div class=\"product-card\">",
     "<!-- 8. Travessa Retangular Heritage 32cm -->\n    <div class=\"product-card\" data-price-min=\"709.0\">"),
    ("<!-- 9. Caçarola Aço Esmaltado (Cool Mint) -->\n    <div class=\"product-card\">",
     "<!-- 9. Caçarola Aço Esmaltado (Cool Mint) -->\n    <div class=\"product-card\" data-price-min=\"789.0\">"),
    ("<!-- 10. Chaleira Demi (Caribe) -->\n    <div class=\"product-card\">",
     "<!-- 10. Chaleira Demi (Caribe) -->\n    <div class=\"product-card\" data-price-min=\"809.0\">"),
    ("<!-- 11. Chaleira Clássica (Meringue) -->\n    <div class=\"product-card\">",
     "<!-- 11. Chaleira Clássica (Meringue) -->\n    <div class=\"product-card\" data-price-min=\"929.0\">"),
    ("<!-- 12. Chaleira Clássica Pegador Aço Inox -->\n    <div class=\"product-card\">",
     "<!-- 12. Chaleira Clássica Pegador Aço Inox -->\n    <div class=\"product-card\" data-price-min=\"929.0\">"),
    ("<!-- 13. Miniatura Collection -->\n    <div class=\"product-card\">",
     "<!-- 13. Miniatura Collection -->\n    <div class=\"product-card\" data-price-min=\"989.0\">"),
    ("<!-- 14. Bowl Inox com Tampa de Vidro (NOVO, range) -->\n    <div class=\"product-card\">",
     "<!-- 14. Bowl Inox com Tampa de Vidro (NOVO, range) -->\n    <div class=\"product-card\" data-price-min=\"399.0\">"),
]

# Also fix images that are using wrong/placeholder images
img_fixes = [
    # Stockpot Pegador Fenolico - using panela-redonda image
    ('alt="Stockpot Pegador Fenólico" />\n          <div class="product-badge sale">SALE</div>',
     None),  # skip - would need correct image
    # Caçarola Aço Esmaltado - using panela-redonda image
    ('alt="Caçarola Aço Esmaltado" />\n',
     None),
    # Chaleira Demi - using chaleira-cloche image
    ('alt="Chaleira Demi" />\n',
     None),
    # Chaleira Clássica - using chaleira-cloche image
    ('alt="Chaleira Clássica Meringue" />\n',
     None),
    # Chaleira Clássica Pegador - using chaleira-cloche image
    ('alt="Chaleira Clássica Pegador Aço Inox" />\n',
     None),
]

count = 0
for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print(f"NOT FOUND: {old[:60]}...")

# Fix wrong images with correct CDN URLs
# Stockpot Pegador Fenolico
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdc6347e6/images/produto-lecreuset-panela-redonda-laranja.png?sw=650&sh=650&sm=fit" alt="Stockpot Pegador Fenólico"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3fab14a7/images/stockpot-coolmint-lecreuset-peg-fenolico.png?sw=650&sh=650&sm=fit" alt="Stockpot Pegador Fenólico"'
)

# Caçarola Aço Esmaltado
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdc6347e6/images/produto-lecreuset-panela-redonda-laranja.png?sw=650&sh=650&sm=fit" alt="Caçarola Aço Esmaltado"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwf6a52a4e/images/Ca%C3%A7arola%20Redonda%20A%C3%A7o%20Inox-cool-mint%20(3).png?sw=650&sh=650&sm=fit" alt="Caçarola Aço Esmaltado"'
)

# Chaleira Demi
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdf67a668/images/40109010991000-chaleira-cloche.jpg?sw=650&sh=650&sm=fit" alt="Chaleira Demi"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0ecc18c6/images/92000900490000.jpg?sw=650&sh=650&sm=fit" alt="Chaleira Demi"'
)

# Chaleira Clássica Meringue
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdf67a668/images/40109010991000-chaleira-cloche.jpg?sw=650&sh=650&sm=fit" alt="Chaleira Clássica Meringue"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6bbc1145/images/40104027160000.jpg?sw=650&sh=650&sm=fit" alt="Chaleira Clássica Meringue"'
)

# Chaleira Clássica Pegador Aço Inox
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdf67a668/images/40109010991000-chaleira-cloche.jpg?sw=650&sh=650&sm=fit" alt="Chaleira Clássica Pegador Aço Inox"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc30f77f2/images/chaleira-lifestyle_camomille.png?sw=650&sh=650&sm=fit" alt="Chaleira Clássica Pegador Aço Inox"'
)

# Miniatura Collection - using gift-collection image (fix)
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw72d4c5ef/images/79114105219030-gift-collection.jpg?sw=650&sh=650&sm=fit" alt="Miniatura Collection"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0a863909/images/miniatura-collection1.png?sw=650&sh=650&sm=fit" alt="Miniatura Collection"'
)

# Set 2 Assadeiras - using travessa-heritage image (fix)
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe1816222/images/travessa-retangular-heritage-nuit-23cm.png?sw=650&sh=650&sm=fit" alt="Set 2 Assadeiras Retangulares"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2511281b/images/Produto-lecreuset-metal-bakeware-set-formas.png?sw=650&sh=650&sm=fit" alt="Set 2 Assadeiras Retangulares"'
)

# Set Azeite Vinagre Signature - using same image as Classico (fix)
content = content.replace(
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw958dd2ef/images/porta-oleo-lecreuset-1.png?sw=650&sh=650&sm=fit" alt="Set Azeite & Vinagre Signature"',
    'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6ff64c62/images/80842307160003-kit-oleo-vinagre.jpg?sw=650&sh=650&sm=fit" alt="Set Azeite & Vinagre Signature"'
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Added data-price-min to {count} cards")
print("Fixed 8 incorrect product images")
