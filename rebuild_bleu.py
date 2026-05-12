with open('colecao-bleu-riviera.html', encoding='utf-8') as f:
    content = f.read()

header_end = content.find('</header>') + len('</header>')
footer_start = content.find('<footer>')

new_main = """

<!-- HERO -->
<div style="background:#f2f7f8;">
  <div style="max-width:1400px;margin:0 auto;padding:0 20px;text-align:center;">
    <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/02%20-%20Fevereiro/LP-Bleuriviera.png" alt="Bleu Riviera" style="display:block;max-width:500px;margin:0 auto;padding-top:48px;" />
  </div>
  <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/02%20-%20Fevereiro/LP-Bleuriviera-2.jpg" alt="Bleu Riviera" style="display:block;width:100%;" />
  <div style="max-width:900px;margin:0 auto;padding:60px 24px;text-align:center;">
    <h2 style="font-size:48px;font-weight:400;font-family:'Playfair Display',Georgia,serif;font-style:italic;color:#111;margin-bottom:30px;line-height:1.2;">Um toque mediterr&acirc;neo para sua mesa.</h2>
    <p style="font-size:18px;color:#444;line-height:1.7;margin-bottom:32px;">Tons azul-esverdeados brilhantes, inspirados pelas profundezas do mar, fluem e se entrelaçam ao redor do cl&aacute;ssico pegador dourado. Originária de uma cidade litorânea banhada pelo sol, essa tonalidade marcante acrescenta um toque vibrante aos neutros sofisticados ou complementa com alegria tons intensos e exuberantes.<br><br>A sensação é leve, vibrante e refrescante. <strong>Bleu Riviera &eacute; uma cor repleta de possibilidades.</strong> Seja qual for a forma de usar, seu esp&iacute;rito e sua decoração partem imediatamente para as f&eacute;rias.</p>
    <a href="colecao-bleu-riviera.html" style="display:inline-block;background:#006776;color:#fff;padding:16px 40px;border-radius:8px;font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;">EXPLORE BLEU RIVIERA</a>
  </div>
</div>

<!-- ENCONTRO DE CORES -->
<div style="padding:80px 24px;background:#fff;text-align:center;">
  <div style="max-width:1400px;margin:0 auto;">
    <div style="font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:#006776;margin-bottom:12px;">BLEU RIVIERA &ndash; NEW COLOR</div>
    <h2 style="font-size:36px;font-weight:400;font-family:'Playfair Display',Georgia,serif;font-style:italic;color:#111;margin-bottom:16px;">Encontro de Cores</h2>
    <div style="width:120px;height:2px;background:#006776;margin:0 auto 48px;"></div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;" class="br-colors-grid">
      <div>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/02%20-%20Fevereiro/caribexblue-riviera.png" alt="Caribe" style="width:160px;height:auto;margin:0 auto 16px;display:block;" />
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/Landing/bleu%20riviera/LP-Bleuriviera-1.png" alt="Caribe" style="width:100%;border-radius:8px;margin-bottom:16px;" />
        <h3 style="font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;">CARIBE</h3>
        <ul style="list-style:none;font-size:13px;color:#666;line-height:1.8;"><li>Azul tropical vibrante</li><li>Respingos turquesa iluminados</li><li>Um degrad&ecirc; do mar ao c&eacute;u</li></ul>
      </div>
      <div>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/02%20-%20Fevereiro/azurexblue-riviera.png" alt="Azure" style="width:160px;height:auto;margin:0 auto 16px;display:block;" />
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/Landing/bleu%20riviera/LP-Bleuriviera-2.png" alt="Azure" style="width:100%;border-radius:8px;margin-bottom:16px;" />
        <h3 style="font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;">AZURE</h3>
        <ul style="list-style:none;font-size:13px;color:#666;line-height:1.8;"><li>Azul fresco e Confiante</li><li>Sensação leve de ver&atilde;o</li><li>Tom vibrante e delicado</li></ul>
      </div>
      <div>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/02%20-%20Fevereiro/deeptealxblue-riviera.png" alt="Deep Teal" style="width:160px;height:auto;margin:0 auto 16px;display:block;" />
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/Landing/bleu%20riviera/LP-Bleuriviera-3.png" alt="Deep Teal" style="width:100%;border-radius:8px;margin-bottom:16px;" />
        <h3 style="font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;">DEEP TEAL</h3>
        <ul style="list-style:none;font-size:13px;color:#666;line-height:1.8;"><li>Cativante em sua profundidade</li><li>Calma, seguran&ccedil;a e harmonia</li><li>Tom rico e envolvente</li></ul>
      </div>
      <div>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/homepage/2026/02%20-%20Fevereiro/bleuriviera-2.png" alt="Bleu Riviera" style="width:160px;height:auto;margin:0 auto 16px;display:block;" />
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw507b1eac/images/Landing/bleu%20riviera/LP-Bleuriviera-4.png" alt="Bleu Riviera" style="width:100%;border-radius:8px;margin-bottom:16px;" />
        <h3 style="font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;">BLEU RIVIERA</h3>
        <ul style="list-style:none;font-size:13px;color:#666;line-height:1.8;"><li>Azul esverdeado luminoso</li><li>Leve e refrescante</li><li>Atmosfera mediterr&acirc;nea</li></ul>
      </div>
    </div>
    <div style="margin-top:48px;">
      <a href="colecao-bleu-riviera.html" style="display:inline-block;background:#006776;color:#fff;padding:14px 36px;border-radius:8px;font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;">COMPRAR AGORA</a>
    </div>
  </div>
</div>

<!-- COLECAO HEADING -->
<div style="padding:64px 24px 16px;text-align:center;background:#fff;">
  <h2 style="font-size:36px;font-weight:400;font-family:'Playfair Display',Georgia,serif;font-style:italic;color:#111;margin-bottom:16px;">Cole&ccedil;&atilde;o Bleu Riviera</h2>
  <p style="font-size:15px;color:#666;max-width:700px;margin:0 auto;">Explore panelas de ferro fundido esmaltado, cer&acirc;micas premium e acess&oacute;rios que complementam sua casa com elegan&ccedil;a.</p>
</div>

<!-- PRODUTOS EM DESTAQUE -->
<div style="padding:32px 24px 64px;background:#fff;">
  <div style="max-width:1400px;margin:0 auto;">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:48px;" class="br-featured-grid">
      <div style="position:relative;overflow:hidden;border-radius:12px;background:#f5f9fa;">
        <span style="position:absolute;top:12px;left:12px;background:#fff;color:#7E010B;font-size:10px;font-weight:800;padding:4px 10px;border-radius:4px;z-index:1;">Lan&ccedil;amento</span>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dwe253c13b/images/homepage/2026/02%20-%20Fevereiro/bleu-riviera-image-2.png" alt="Ca&ccedil;arola Buffet Signature" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;" />
        <div style="padding:16px;"><div style="font-size:14px;font-weight:700;margin-bottom:4px;">Ca&ccedil;arola Buffet Signature</div><div style="font-size:13px;color:#006776;font-weight:800;">R$ 2.999,00</div><div style="font-size:11px;color:#888;">10x R$ 299,90 sem juros</div></div>
      </div>
      <div style="position:relative;overflow:hidden;border-radius:12px;background:#f5f9fa;">
        <span style="position:absolute;top:12px;left:12px;background:#fff;color:#7E010B;font-size:10px;font-weight:800;padding:4px 10px;border-radius:4px;z-index:1;">&uacute;ltimas unidades</span>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw58af182e/images/homepage/2026/02%20-%20Fevereiro/bleu-riviera-image-1.png" alt="Panela Redonda Signature" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;" />
        <div style="padding:16px;"><div style="font-size:14px;font-weight:700;margin-bottom:4px;">Panela Redonda Signature</div><div style="font-size:13px;color:#006776;font-weight:800;">R$ 2.949,00</div><div style="font-size:11px;color:#888;">10x R$ 294,90 sem juros</div></div>
      </div>
      <div style="position:relative;overflow:hidden;border-radius:12px;background:#f5f9fa;">
        <span style="position:absolute;top:12px;left:12px;background:#fff;color:#7E010B;font-size:10px;font-weight:800;padding:4px 10px;border-radius:4px;z-index:1;">Lan&ccedil;amento</span>
        <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dwc9457cd8/images/homepage/2026/02%20-%20Fevereiro/bleu-riviera-image-6.png" alt="Travessa Retangular Heritage" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;" />
        <div style="padding:16px;"><div style="font-size:14px;font-weight:700;margin-bottom:4px;">Travessa Retangular Heritage</div><div style="font-size:13px;color:#006776;font-weight:800;">R$ 349,00</div><div style="font-size:11px;color:#888;">3x R$ 116,33 sem juros</div></div>
      </div>
      <div style="position:relative;overflow:hidden;border-radius:12px;background:#f5f9fa;">
        <span style="position:absolute;top:12px;left:12px;background:#fff;color:#7E010B;font-size:10px;font-weight:800;padding:4px 10px;border-radius:4px;z-index:1;">Lan&ccedil;amento</span>
        <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dwcf167a83/images/homepage/2026/02%20-%20Fevereiro/bleu-riviera-image-4.jpg?sw=768&sfrm=png" alt="Travessa Canelada" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;" />
        <div style="padding:16px;"><div style="font-size:14px;font-weight:700;margin-bottom:4px;">Travessa Canelada</div><div style="font-size:13px;color:#006776;font-weight:800;">R$ 529,00</div><div style="font-size:11px;color:#888;">5x R$ 105,80 sem juros</div></div>
      </div>
      <div style="position:relative;overflow:hidden;border-radius:12px;background:#f5f9fa;">
        <span style="position:absolute;top:12px;left:12px;background:#fff;color:#7E010B;font-size:10px;font-weight:800;padding:4px 10px;border-radius:4px;z-index:1;">Lan&ccedil;amento</span>
        <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dwfa3522c9/images/homepage/2026/02%20-%20Fevereiro/bleu-riviera-image-3.jpg?sw=768&sfrm=png" alt="Grelha Quadrada Signature" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;" />
        <div style="padding:16px;"><div style="font-size:14px;font-weight:700;margin-bottom:4px;">Grelha Quadrada Signature</div><div style="font-size:13px;color:#006776;font-weight:800;">R$ 1.859,00</div><div style="font-size:11px;color:#888;">10x R$ 185,90 sem juros</div></div>
      </div>
      <div style="position:relative;overflow:hidden;border-radius:12px;background:#f5f9fa;">
        <span style="position:absolute;top:12px;left:12px;background:#fff;color:#7E010B;font-size:10px;font-weight:800;padding:4px 10px;border-radius:4px;z-index:1;">Lan&ccedil;amento</span>
        <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dwa37dbbfb/images/homepage/2026/02%20-%20Fevereiro/bleu-riviera-image-7.jpg?sw=768&sfrm=png" alt="Panela Redonda Everyday" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block;" />
        <div style="padding:16px;"><div style="font-size:14px;font-weight:700;margin-bottom:4px;">Panela Redonda Everyday Signature</div><div style="font-size:13px;color:#006776;font-weight:800;">R$ 2.469,00</div><div style="font-size:11px;color:#888;">10x R$ 246,90 sem juros</div></div>
      </div>
    </div>
    <div style="text-align:center;">
      <a href="colecao-bleu-riviera.html" style="display:inline-block;border:2px solid #111;color:#111;padding:14px 40px;font-size:13px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;">VER COLE&Ccedil;&Atilde;O</a>
    </div>
  </div>
</div>

<!-- COMBINE BLEU RIVIERA -->
<div style="background:#f9f9f9;padding:80px 24px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;" class="br-combine-grid">
    <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw2867e2ca/images/homepage/2026/02%20-%20Fevereiro/LP-Bleuriviera-21.png" alt="Combine Bleu Riviera" style="width:100%;border-radius:12px;display:block;" />
    <div>
      <h2 style="font-size:40px;font-weight:400;font-family:'Playfair Display',Georgia,serif;font-style:italic;color:#111;margin-bottom:20px;line-height:1.2;">Combine<br>Bleu Riviera</h2>
      <p style="font-size:15px;color:#555;line-height:1.7;margin-bottom:28px;">Uma tonalidade vibrante que se adapta a diferentes composi&ccedil;&otilde;es. Perfeita para criar contrastes sutis ou composi&ccedil;&otilde;es monocrom&aacute;ticas, como Laranja e Nectar.</p>
      <a href="colecao-bleu-riviera.html" style="display:inline-block;background:#111;color:#fff;padding:14px 32px;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;">CONFIRA</a>
    </div>
  </div>
</div>

<!-- UMA NOVA COR NA PALETA -->
<div style="background:#fff;padding:80px 24px;">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;" class="br-combine-grid">
    <div>
      <h2 style="font-size:40px;font-weight:400;font-family:'Playfair Display',Georgia,serif;font-style:italic;color:#111;margin-bottom:20px;line-height:1.2;">Uma nova<br>cor na paleta</h2>
      <p style="font-size:15px;color:#555;line-height:1.7;margin-bottom:28px;">A uni&atilde;o entre Bleu Riviera, Rose Quartz e Meringue cria uma paleta leve e contempor&acirc;nea, onde cores vibrantes e tons suaves convivem em perfeita harmonia &agrave; mesa.</p>
      <a href="colecao-bleu-riviera.html" style="display:inline-block;background:#111;color:#fff;padding:14px 32px;font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;">CONFIRA</a>
    </div>
    <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/dw7b9c8410/images/homepage/2026/02%20-%20Fevereiro/LP-Bleuriviera-20.png" alt="Uma nova cor na paleta" style="width:100%;border-radius:12px;display:block;" />
  </div>
</div>

<!-- BLEU AZUL BLOCK -->
<div style="background:#006776;padding:64px 24px;text-align:center;">
  <div style="max-width:800px;margin:0 auto;">
    <p style="font-size:18px;color:#fff;line-height:1.7;">Este novo azul vibrante e energ&eacute;tico traz exuber&acirc;ncia para a sua mesa. Inspirado pela beleza luminosa da Riviera, cria uma atmosfera leve e alegre. As &aacute;guas serenas e cintilantes e os c&eacute;us claros e ensolarados ganham forma em um tom que transmite frescor e vitalidade. Uma experi&ecirc;ncia que transforma o ambiente em um ref&uacute;gio leve repleto do esp&iacute;rito descontra&iacute;do da vida &agrave; beira-mar.</p>
  </div>
</div>

<!-- PRODUTOS GRID -->
<div style="padding:64px 24px 80px;background:#fff;">
  <div style="max-width:1400px;margin:0 auto;">
    <h3 style="font-size:24px;font-weight:700;margin-bottom:40px;text-align:center;">Produtos que iluminam a mesa:</h3>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;" class="br-products-grid">
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2e8c06a/images/panela-redonda-riviera-1.jpg?sw=650&sh=650&sm=fit" alt="Panela Redonda Signature" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">&uacute;ltimas unidades</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Panela Redonda Signature</div><div style="font-size:11px;color:#888;margin-bottom:4px;">24 cm</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 2.949,00</div><div style="font-size:11px;color:#666;">10x R$ 294,90 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit" alt="Ca&ccedil;arola Buffet Signature" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Ca&ccedil;arola Buffet Signature</div><div style="font-size:11px;color:#888;margin-bottom:4px;">30 cm</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 2.999,00</div><div style="font-size:11px;color:#666;">10x R$ 299,90 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw33faad65/images/44001210995200-moedor-bleu.jpg?sw=650&sh=650&sm=fit" alt="Moedor de Sal 21cm" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Moedor de Sal 21cm</div><div style="font-size:11px;color:#888;margin-bottom:4px;">Bleu Riviera</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 369,00</div><div style="font-size:11px;color:#666;">3x R$ 123,00 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwee98c815/images/21114260990450-panela-marmita.jpg?sw=650&sh=650&sm=fit" alt="Panela Marmita Signature" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Panela Marmita Signature</div><div style="font-size:11px;color:#888;margin-bottom:4px;">26 cm</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 2.789,00</div><div style="font-size:11px;color:#666;">10x R$ 278,90 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc263a57a/images/79342000990082-set-3-travessas.jpg?sw=650&sh=650&sm=fit" alt="Set de 3 Travessas" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Set de 3 Travessas Retangulares</div><div style="font-size:11px;color:#888;margin-bottom:4px;">Bleu Riviera</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 1.349,00</div><div style="font-size:11px;color:#666;">10x R$ 134,90 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw07ae9b98/images/70302350990002-caneca-350ml-riviera.jpg?sw=650&sh=650&sm=fit" alt="Caneca London 350ml" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Caneca London 350ml</div><div style="font-size:11px;color:#888;margin-bottom:4px;">Cer&acirc;mica &middot; 350ml</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 159,00</div><div style="font-size:11px;color:#666;">3x R$ 53,00 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwda92585c/images/70117160997099-bowl-redondo-16cm.jpg?sw=650&sh=650&sm=fit" alt="Bowl Redondo Vancouver 16cm" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Bowl Redondo Vancouver 16cm</div><div style="font-size:11px;color:#888;margin-bottom:4px;">Cer&acirc;mica &middot; 16cm</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 209,00</div><div style="font-size:11px;color:#666;">3x R$ 69,67 sem juros</div></div>
      </div>
      <div class="product-card" style="cursor:pointer;">
        <div style="position:relative;background:#f5f9fa;border-radius:8px;overflow:hidden;aspect-ratio:1;">
          <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw99b3e915/images/70202270997099-prato-raso22cm-bleu.png?sw=650&sh=650&sm=fit" alt="Prato Raso Vancouver 22cm" style="width:100%;height:100%;object-fit:contain;padding:12px;" />
          <span style="position:absolute;top:8px;left:8px;background:#fff;color:#7E010B;font-size:9px;font-weight:800;padding:3px 8px;border-radius:3px;">Lan&ccedil;amento</span>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
        <div style="padding:10px 2px 0;"><div style="font-size:13px;font-weight:600;margin-bottom:2px;">Prato Raso Vancouver 22cm</div><div style="font-size:11px;color:#888;margin-bottom:4px;">Cer&acirc;mica &middot; 22cm</div><div style="font-size:14px;font-weight:800;color:#006776;">R$ 179,00</div><div style="font-size:11px;color:#666;">3x R$ 59,67 sem juros</div></div>
      </div>
    </div>
  </div>
</div>

<style>
@media(max-width:768px){
  .br-featured-grid { grid-template-columns:1fr 1fr !important; gap:12px !important; }
  .br-combine-grid { grid-template-columns:1fr !important; gap:32px !important; }
  .br-products-grid { grid-template-columns:1fr 1fr !important; gap:12px !important; }
  .br-colors-grid { grid-template-columns:1fr 1fr !important; gap:16px !important; }
}
</style>

"""

new_content = content[:header_end] + new_main + content[footer_start:]

with open('colecao-bleu-riviera.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Done! {len(new_content)} chars")
