import re

filepath = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ate-250.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# === 1. FIX WRONG IMAGES IN EXISTING CARDS ===
img_fixes = [
    # Set Tampa para Moedores - using pie-bird image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8591622f/images/71206001400100-pie-bird.jpg?sw=650&sh=650&sm=fit" alt="Set Tampa para Moedores"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw43209926/images/93010800140200.jpg?sw=650&sh=650&sm=fit" alt="Set Tampa para Moedores"'),
    # Caneca Jardin 350ml - using 200ml image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4df08c7b/images/caneca-jardin.png?sw=650&sh=650&sm=fit" alt="Caneca Jardin 350ml"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0f692789/images/caneca-jardin-350ml-shell%20pink.png?sw=650&sh=650&sm=fit" alt="Caneca Jardin 350ml"'),
    # Caneca London 200ml (Caribe) - using 100ml image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd4a35bc2/images/produto-lecreuset-caneca-100ml-caribe.png?sw=650&sh=650&sm=fit" alt="Caneca London 200ml Caribe"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd4adbf46/images/produto-lecreuset-caneca-200ml-caribe.png?sw=650&sh=650&sm=fit" alt="Caneca London 200ml Caribe"'),
    # Caneca London 350ml Nectar - using bowl image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw38257761/images/produto-lecreuset-bowl-16cm-nectar.png?sw=650&sh=650&sm=fit" alt="Caneca London 350ml Nectar"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9db8797a/images/produto-lecreuset-caneca-350ml-nectar.png?sw=650&sh=650&sm=fit" alt="Caneca London 350ml Nectar"'),
    # Prato Raso Jardin 22cm - using mini-cocotte-jardin image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw290a503c/images/mini-cocotte-jardin-250ml%20(2).png?sw=650&sh=650&sm=fit" alt="Prato Raso Jardin 22cm"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwabe4156a/images/prato-raso-jardin-22cm-meringueprato-raso-jardin-22cm-meringue.png?sw=650&sh=650&sm=fit" alt="Prato Raso Jardin 22cm"'),
    # Bandeja Para 6 Ovos - using pie bird image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6672a6ab/images/71206000600000-vermelho2.png?sw=650&sh=650&sm=fit" alt="Bandeja Para 6 Ovos"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaf0871e9/images/bandeja-para-6-ovos-laranja.png?sw=650&sh=650&sm=fit" alt="Bandeja Para 6 Ovos"'),
    # Caneca Bistrô 400ml Caribe - using 100ml image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd4a35bc2/images/produto-lecreuset-caneca-100ml-caribe.png?sw=650&sh=650&sm=fit" alt="Caneca Bistr\u00f4 400ml Caribe"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw142a24eb/images/produto-lecreuset-caneca-bistro-400ml-caribe.png?sw=650&sh=650&sm=fit" alt="Caneca Bistr\u00f4 400ml Caribe"'),
    # Pote de Alho Meringue - using descanso image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6d91e854/images/descanso_colher_lecreuset_meringue.jpg?sw=650&sh=650&sm=fit" alt="Pote de Alho Meringue"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7e6363f0/images/porta-alho-meringue.jpg?sw=650&sh=650&sm=fit" alt="Pote de Alho Meringue"'),
    # Mini Cocotte Pegador Colorido - using wrong meringue image
    ('src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw84b7660e/images/produto-lecreuset-minicocotte-laranja-meringue.png?sw=650&sh=650&sm=fit" alt="Mini Cocotte Pegador Colorido"',
     'src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4690e112/images/mini-cocotte-pegador-colorido-agave1.jpg?sw=650&sh=650&sm=fit" alt="Mini Cocotte Pegador Colorido"'),
]

img_fixed = 0
for old, new in img_fixes:
    if old in content:
        content = content.replace(old, new, 1)
        img_fixed += 1
    else:
        print(f"IMG NOT FOUND: {old[:80]}...")

print(f"Fixed {img_fixed} wrong images")

# === 2. ADD MISSING PRODUCT CARDS ===
wishlist_svg = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

new_cards = f"""
    <!-- 22. Pie Bird (Branco) -->
    <div class="product-card" data-price-min="99.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8591622f/images/71206001400100-pie-bird.jpg?sw=650&sh=650&sm=fit" alt="Pie Bird Branco" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Pie Bird (Branco)</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 99,00</div>
      </a>
    </div>

    <!-- 23. Caneca London 350ml (Laranja) -->
    <div class="product-card" data-price-min="159.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe8712606/images/produto-lecreuset-caneca-350ml-laranja.png?sw=650&sh=650&sm=fit" alt="Caneca London 350ml Laranja" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca London 350ml (Laranja)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; 350ml</div>
        <div class="product-card-price">R$ 159,00</div>
      </a>
    </div>

    <!-- 24. Bowl Redondo Vancouver (Shell Pink) -->
    <div class="product-card" data-price-min="209.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1ddcff55/images/produto-lecreuset-bowl-16cm-shellpink.png?sw=650&sh=650&sm=fit" alt="Bowl Redondo Vancouver Shell Pink" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Bowl Redondo Vancouver (Shell Pink)</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 209,00</div>
      </a>
    </div>

    <!-- 25. Mini Cocotte Jardin (Meringue) - SALE 30% OFF -->
    <div class="product-card" data-price-min="174.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw757ce2f5/images/mini-cocotte-jardin-250ml-meringue.png?sw=650&sh=650&sm=fit" alt="Mini Cocotte Jardin Meringue" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Mini Cocotte Jardin (Meringue)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-orig">R$ 249,00</div>
        <div class="product-card-price-sale">R$ 174,30</div>
      </a>
    </div>

    <!-- 26. Mini Cocotte Jardin (Shell Pink) - SALE 30% OFF -->
    <div class="product-card" data-price-min="174.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw25efbfaf/images/mini-cocotte-jardin-250ml-shell%20pink.png?sw=650&sh=650&sm=fit" alt="Mini Cocotte Jardin Shell Pink" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Mini Cocotte Jardin (Shell Pink)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-orig">R$ 249,00</div>
        <div class="product-card-price-sale">R$ 174,30</div>
      </a>
    </div>

    <!-- 27. Mini Cocotte (Nectar) -->
    <div class="product-card" data-price-min="239.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwee67cc9b/images/produto-lecreuset-minicocotte-laranja-nectar.png?sw=650&sh=650&sm=fit" alt="Mini Cocotte Nectar" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Mini Cocotte (Nectar)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Ferro Fundido</div>
        <div class="product-card-price">R$ 239,00</div>
      </a>
    </div>

    <!-- 28. Mini Cocotte (Caribe) -->
    <div class="product-card" data-price-min="239.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1d08d118/images/produto-lecreuset-minicocotte-laranja-caribe.png?sw=650&sh=650&sm=fit" alt="Mini Cocotte Caribe" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Mini Cocotte (Caribe)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Ferro Fundido</div>
        <div class="product-card-price">R$ 239,00</div>
      </a>
    </div>

    <!-- 29. Mini Cocotte Sunflower (Caribe) - SALE -->
    <div class="product-card" data-price-min="181.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw626a705e/images/mini-cocotte-flower-caribe%20(1).png?sw=650&sh=650&sm=fit" alt="Mini Cocotte Sunflower Caribe" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Mini Cocotte Sunflower (Caribe)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Edi&ccedil;&atilde;o Especial</div>
        <div class="product-card-price-sale">R$ 181,30</div>
      </a>
    </div>

    <!-- 30. Caneca Jardin 200ml (Meringue) -->
    <div class="product-card" data-price-min="159.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1dac1db3/images/caneca-jardim-200ml-meringue.png?sw=650&sh=650&sm=fit" alt="Caneca Jardin 200ml Meringue" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca Jardin 200ml (Meringue)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price">R$ 159,00</div>
      </a>
    </div>

    <!-- 31. Caneca Jardin 200ml (Shell Pink) - SALE -->
    <div class="product-card" data-price-min="111.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe5c8c698/images/caneca-jardin-200ml-shellpink.png?sw=650&sh=650&sm=fit" alt="Caneca Jardin 200ml Shell Pink" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca Jardin 200ml (Shell Pink)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-orig">R$ 159,00</div>
        <div class="product-card-price-sale">R$ 111,30</div>
      </a>
    </div>

    <!-- 32. Bowl Jardin 320ml (Camomille) - SALE -->
    <div class="product-card" data-price-min="139.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw25bfe4dd/images/bowl-jardim-320ml-camomille%20(2).png?sw=650&sh=650&sm=fit" alt="Bowl Jardin 320ml Camomille" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Bowl Jardin 320ml (Camomille)</div>
        <div class="product-card-sub">Cer&amiaca;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-sale">R$ 139,30</div>
      </a>
    </div>

    <!-- 33. Jarra Jardin 440ml (Camomille) - SALE -->
    <div class="product-card" data-price-min="223.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8b21dbe1/images/jarra-jardin-440ml-camomille.png?sw=650&sh=650&sm=fit" alt="Jarra Jardin 440ml Camomille" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Jarra Jardin 440ml (Camomille)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-sale">R$ 223,30</div>
      </a>
    </div>

    <!-- 34. Prato Raso Jardin 22cm - SALE -->
    <div class="product-card" data-price-min="167.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwabe4156a/images/prato-raso-jardin-22cm-meringueprato-raso-jardin-22cm-meringue.png?sw=650&sh=650&sm=fit" alt="Prato Raso Jardin 22cm Variacao" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Prato Raso Jardin 22cm (Camomille)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-sale">R$ 167,30</div>
      </a>
    </div>

    <!-- 35. Ramekin 200ml (Caribe) -->
    <div class="product-card" data-price-min="139.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw75fb8201/images/Ramekin_200ml_caribe_lecreuset.jpg?sw=650&sh=650&sm=fit" alt="Ramekin 200ml Caribe" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Ramekin 200ml (Caribe)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; 200ml</div>
        <div class="product-card-price">R$ 139,00</div>
      </a>
    </div>

    <!-- 36. Espátula Venus -->
    <div class="product-card" data-price-min="159.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb49abfb1/images/espatula-pequena-venus-coolmint.png?sw=650&sh=650&sm=fit" alt="Esp&aacute;tula Venus" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Esp&aacute;tula Venus</div>
        <div class="product-card-sub">Acess&oacute;rios &middot; Sil&iacute;cone</div>
        <div class="product-card-price">R$ 159,00</div>
      </a>
    </div>

    <!-- 37. Espátula Silicone Signature -->
    <div class="product-card" data-price-min="159.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb2545411/images/42073000990000-espatula-medida-silicone.jpg?sw=650&sh=650&sm=fit" alt="Esp&aacute;tula Silicone Signature" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Esp&aacute;tula Silicone Signature</div>
        <div class="product-card-sub">Acess&oacute;rios &middot; Sil&iacute;cone</div>
        <div class="product-card-price">R$ 159,00</div>
      </a>
    </div>

    <!-- 38. Jarra Clássica (Nectar) -->
    <div class="product-card" data-price-min="229.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8dd34bdc/images/jarra-600ml-lecreuset-nectar.jpg?sw=650&sh=650&sm=fit" alt="Jarra Cl&aacute;ssica Nectar" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Jarra Cl&aacute;ssica 600ml (Nectar)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; 600ml</div>
        <div class="product-card-price">R$ 229,00</div>
      </a>
    </div>

    <!-- 39. Prato Fundo Kobe -->
    <div class="product-card" data-price-min="229.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw45f78070/images/tardes%20de%20verao/prato-fundo-kobe-22cm-white.png?sw=650&sh=650&sm=fit" alt="Prato Fundo Kobe" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Prato Fundo Kobe</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 229,00</div>
      </a>
    </div>

    <!-- 40. Descanso Oval para Colher (Nectar) -->
    <div class="product-card" data-price-min="199.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw35be13ed/images/descanso-oval-nectar.jpg?sw=650&sh=650&sm=fit" alt="Descanso Oval para Colher Nectar" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Descanso Oval para Colher (Nectar)</div>
        <div class="product-card-sub">Acess&oacute;rios</div>
        <div class="product-card-price">R$ 199,00</div>
      </a>
    </div>

    <!-- 41. Descanso Oval para Colher (Branco) -->
    <div class="product-card" data-price-min="199.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8f661edf/images/descanso_oval_lecreuset_branco_lecreuset.jpg?sw=650&sh=650&sm=fit" alt="Descanso Oval para Colher Branco" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Descanso Oval para Colher (Branco)</div>
        <div class="product-card-sub">Acess&oacute;rios</div>
        <div class="product-card-price">R$ 199,00</div>
      </a>
    </div>

    <!-- 42. Caneca Seattle 400ml (Nectar) -->
    <div class="product-card" data-price-min="199.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw96261301/images/produto-lecreuset-caneca-400ml-seattle-nectar%20(1).png?sw=650&sh=650&sm=fit" alt="Caneca Seattle 400ml Nectar" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca Seattle 400ml (Nectar)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; 400ml</div>
        <div class="product-card-price">R$ 199,00</div>
      </a>
    </div>

    <!-- 43. Caneca London 100ml (Branco) -->
    <div class="product-card" data-price-min="129.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1d80798c/images/produto-lecreuset-caneca-100ml-branco.png?sw=650&sh=650&sm=fit" alt="Caneca London 100ml Branco" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca London 100ml (Branco)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; 100ml</div>
        <div class="product-card-price">R$ 129,00</div>
      </a>
    </div>

    <!-- 44. Caneca London 200ml (Riviera) -->
    <div class="product-card" data-price-min="139.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1af63394/images/70303200990099-caneca-300ml-riviera.jpg?sw=650&sh=650&sm=fit" alt="Caneca London 200ml Riviera" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca London 200ml (Riviera)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; 200ml</div>
        <div class="product-card-price">R$ 139,00</div>
      </a>
    </div>

    <!-- 45. Bowl Octagon (Vermelho) -->
    <div class="product-card" data-price-min="199.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3f9ce51d/images/bowl-octagon-vermelho-12cm%20(2).png?sw=650&sh=650&sm=fit" alt="Bowl Octagon Vermelho" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Bowl Octagon (Vermelho)</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 199,00</div>
      </a>
    </div>

    <!-- 46. Prato Raso Vancouver 22cm (Caribe) -->
    <div class="product-card" data-price-min="219.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6e36bc36/images/produto-lecreuset-prato-22cm-caribe.png?sw=650&sh=650&sm=fit" alt="Prato Raso Vancouver 22cm Caribe" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Prato Raso Vancouver 22cm (Caribe)</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 219,00</div>
      </a>
    </div>

    <!-- 47. Prato Raso Vancouver 27cm (Nectar) -->
    <div class="product-card" data-price-min="239.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw89e45d75/images/produto-lecreuset-prato-27cm-nectar.png?sw=650&sh=650&sm=fit" alt="Prato Raso Vancouver 27cm Nectar" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Prato Raso Vancouver 27cm (Nectar)</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 239,00</div>
      </a>
    </div>

    <!-- 48. Prato Raso Vancouver 27cm (Shell Pink) -->
    <div class="product-card" data-price-min="239.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwbfd5690f/images/produto-lecreuset-prato-27cm-shellpink.png?sw=650&sh=650&sm=fit" alt="Prato Raso Vancouver 27cm Shell Pink" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Prato Raso Vancouver 27cm (Shell Pink)</div>
        <div class="product-card-sub">Cer&acirc;mica</div>
        <div class="product-card-price">R$ 239,00</div>
      </a>
    </div>

    <!-- 49. Bowl para Pet (Azure) -->
    <div class="product-card" data-price-min="239.0">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw66f2bb29/images/bowl-para-pet-azure.png?sw=650&sh=650&sm=fit" alt="Bowl para Pet Azure" />
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Bowl para Pet (Azure)</div>
        <div class="product-card-sub">Acess&oacute;rios</div>
        <div class="product-card-price">R$ 239,00</div>
      </a>
    </div>

    <!-- 50. Caneca Jardin 350ml (Shell Pink) - SALE -->
    <div class="product-card" data-price-min="132.3">
      <a href="#">
        <div class="product-card-img">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0f692789/images/caneca-jardin-350ml-shell%20pink.png?sw=650&sh=650&sm=fit" alt="Caneca Jardin 350ml Shell Pink" />
          <div class="product-badge sale">SALE</div>
          {wishlist_svg}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">Caneca Jardin 350ml (Shell Pink)</div>
        <div class="product-card-sub">Cer&acirc;mica &middot; Cole&ccedil;&atilde;o Jardim</div>
        <div class="product-card-price-orig">R$ 189,00</div>
        <div class="product-card-price-sale">R$ 132,30</div>
      </a>
    </div>
"""

# Insert before closing product-grid div
insert_marker = "    </div>\n  </div>\n</div>\n<footer>"
if insert_marker in content:
    content = content.replace(insert_marker, new_cards + "\n    </div>\n  </div>\n</div>\n<footer>", 1)
    print("Inserted new product cards")
else:
    print("ERROR: Could not find insertion point!")

# === 3. ADD data-price-min TO EXISTING CARDS WITHOUT IT ===
lines = content.split('\n')
fixed_prices = 0
i = 0
while i < len(lines):
    line = lines[i]
    if '<div class="product-card">' in line and 'data-price-min' not in line:
        price_min = None
        for j in range(i+1, min(i+15, len(lines))):
            m = re.search(r'product-card-price-sale">R\$\s*([\d.,]+)', lines[j])
            if m:
                price_min = float(m.group(1).replace('.', '').replace(',', '.'))
                break
            m = re.search(r'product-card-price">R\$\s*([\d.,]+)', lines[j])
            if m:
                price_min = float(m.group(1).replace('.', '').replace(',', '.'))
                break
        if price_min:
            lines[i] = line.replace('<div class="product-card">', f'<div class="product-card" data-price-min="{price_min}">')
            fixed_prices += 1
    i += 1
content = '\n'.join(lines)
print(f"Added data-price-min to {fixed_prices} existing cards")

# === 4. UPDATE COUNTERS ===
total_cards = content.count('class="product-card"')
# Mobile counter
content = re.sub(r'<strong>\d+</strong> resultados', f'<strong>{total_cards}</strong> resultados', content)
# Desktop results bar
content = re.sub(r'<span class="results-count">\d+ produtos</span>', f'<span class="results-count">{total_cards} produtos</span>', content)
print(f"Updated counters to {total_cards} produtos")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
