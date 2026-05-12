with open('colecao-lancamentos.html', 'r', encoding='utf-8') as f:
    html = f.read()

HEART = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
BADGE = '<div class="product-badge new">NOVO</div>'

def fmt_price(p):
    if not p or p == 'N/A':
        return 'Consulte'
    try:
        v = float(str(p).replace(',','').replace('.','').replace('R$','').strip())
        if v > 999:
            return f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
        return f'{v:.2f}'.replace('.',',')
    except:
        return str(p)

def installments(price_str):
    try:
        v = float(str(price_str))
        if v >= 100:
            p = v / 10
            return f'10x R$ {fmt_price(p)} sem juros'
        return f'1x R$ {fmt_price(price_str)}'
    except:
        return ''

def card(nome, preco, img):
    p_fmt = fmt_price(preco)
    inst = installments(preco)
    return f'''    <div class="product-card">
      <a href="#">
        <div class="product-card-img">
          <img src="{img}" alt="{nome}" loading="lazy" />
          {BADGE}
          {HEART}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">{nome}</div>
        <div class="product-card-sub">Novo · Lançamento</div>
        <div class="product-card-price">R$ {p_fmt}</div>
        <div class="product-card-sub" style="font-size:11px;color:#888;">{inst}</div>
      </a>
    </div>'''

produtos = [
    ("Panela Floral Tradition", 2489, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw795369d3/images/21934200074460-panela-floral3.jpg?sw=650&sh=650&sm=fit"),
    ("Set 2 Protetores de Silicone Para Tampa", 89, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3f5e9969/images/42818110601500-set-2-protetores-vermelho1.jpg?sw=650&sh=650&sm=fit"),
    ("Fecho de Silicone Para Utensílios", 89, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw65d3baa2/images/42416840600000-vermelho-fecho3.jpg?sw=650&sh=650&sm=fit"),
    ("Espátula Pequena de Silicone Signature", 159, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5b07e83f/images/42074001400000-espatula-pequena.png?sw=650&sh=650&sm=fit"),
    ("Colher de Silicone Signature", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2fd90d9/images/42072001400000-colher-de-seilicone.png?sw=650&sh=650&sm=fit"),
    ("Pincel de Silicone Signature", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb51f556f/images/42071001400000-pincel-de-silicone.png?sw=650&sh=650&sm=fit"),
    ("Espátula Média de Silicone Signature", 179, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw44d99f6b/images/42073001400000-espatula-media.png?sw=650&sh=650&sm=fit"),
    ("Colher Vazada de Madeira Signature", 229, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9c11af43/images/47411300010004-colher-vazada.jpg?sw=650&sh=650&sm=fit"),
    ("Garfo de Servir de Madeira Signature", 229, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4bf0be5f/images/47413300010004-garfo-madeira.jpg?sw=650&sh=650&sm=fit"),
    ("Espátula de Madeira Signature", 229, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2a5bbbc6/images/47412300010004-espatula-madeira.jpg?sw=650&sh=650&sm=fit"),
    ("Colher de Madeira Signature", 229, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8defb132/images/47410300010004-colher-madeira.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular Clássica com Tampa", 1059, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd20d97eb/images/81001530600005-travessa-retangular.jpg?sw=650&sh=650&sm=fit"),
    ("Chaleira Cloche", 1069, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdf67a668/images/40109010991000-chaleira-cloche.jpg?sw=650&sh=650&sm=fit"),
    ("Colher de Silicone Signature", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe01b3a17/images/42072000990000-colher-de-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Espátula Pequena de Silicone Signature", 159, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa51e9835/images/42074000990000-espatula-media-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Pincel de Silicone Signature", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc39367ed/images/42071000990000-pincel-de-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Espátula Média de Silicone Signature", 179, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb2545411/images/42073000990000-espatula-medida-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Prato para Aperitivos e Molhos", 889, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0c4da547/images/8200034099009-prato-para-aperitivos.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca Sphere 320ml", 189, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd8b68a52/images/80324320990099-caneca-sphere.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca Seattle Alça Dourada 400ml", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0a9940b7/images/80317400995699-caneca-seattle-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca Abóbora 400ml", 449, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw416d5116/images/80313400900003-caneca-abobora-laranja.jpg?sw=650&sh=650&sm=fit"),
    ("Saleiro Redondo de Madeira Teca 160ml", 349, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3df69a85/images/saleiro-redondo-madeira-teca.png?sw=650&sh=650&sm=fit"),
    ("Pie Bird", 99, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6672a6ab/images/71206000600000-vermelho2.png?sw=650&sh=650&sm=fit"),
    ("Pie Bird", 99, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8591622f/images/71206001400100-pie-bird.jpg?sw=650&sh=650&sm=fit"),
    ("Descanso Coração Para Colher 13Cm", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4aafc127/images/descanso-cora%C3%A7%C3%A3o-parac-colher-vermelho-1.png?sw=650&sh=650&sm=fit"),
    ("Descanso Coração Para Colher 13Cm", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9611b972/images/descanso_coracao_branco_1.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl Coração 650ml", 249, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2ff2e063/images/bowl-cora%C3%A7%C3%A3o-vermelho.png?sw=650&sh=650&sm=fit"),
    ("Set Azeite & Vinagre Signature", 629, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6ff64c62/images/80842307160003-kit-oleo-vinagre.jpg?sw=650&sh=650&sm=fit"),
    ("Porta Óleo 600ml", 299, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7ac533d2/images/porta-oleo-lecreuset-4.png?sw=650&sh=650&sm=fit"),
    ("Bowl Inox com Tampa de Vidro", 0, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwf8b78720/images/bowl-inox-tampa-de-vidro.png?sw=650&sh=650&sm=fit"),
    ("Caçarola Aço Esmaltado", 789, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1ce46797/images/56002200602200-mini-stockpot.jpg?sw=650&sh=650&sm=fit"),
    ("Caçarola Aço Esmaltado", 789, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwcdc1fe6f/images/56002200902200-mini-stockpot.jpg?sw=650&sh=650&sm=fit"),
    ("Caçarola Aço Esmaltado Flores", 849, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw63aa120b/images/56002204812600-mini-stockpot-flores.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl para Pet", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw66f2bb29/images/bowl-para-pet-azure.png?sw=650&sh=650&sm=fit"),
    ("Travessa Terrine Heritage", 599, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dweed1aa5a/images/81013700600009-terrine-vermelho.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Terrine Heritage", 599, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw49089fea/images/82013100600009-travessa-terrine-vermelho.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Oval com Tampa Heritage", 1099, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwae51ed71/images/71006400600080-travessa-tampa-heritage1.jpg?sw=650&sh=650&sm=fit"),
    ("Moedor de Sal em Madeira 21cm", 369, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7c2c8aec/images/moedor-de-madeira-de-sal.png?sw=650&sh=650&sm=fit"),
    ("Moedor de Pimenta em Madeira 21cm", 369, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwef3671a4/images/moedor-de-madeira-de-pimenta.png?sw=650&sh=650&sm=fit"),
    ("Chaleira Cloche Bleu Riviera", 1069, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwdf67a668/images/40109010991000-chaleira-cloche.jpg?sw=650&sh=650&sm=fit"),
    ("Set 2 Pratos Gato", 329, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwbd03e362/images/89401008070009-prato-gato.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Para Pão Oval", 2999, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw13f7201f/images/21302290600430-panela-pao-oblong.jpg?sw=650&sh=650&sm=fit"),
    ("Set Caneca 100ml Gift Collection", 639, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw72d4c5ef/images/79114105219030-gift-collection.jpg?sw=650&sh=650&sm=fit"),
    ("Saca-Rolhas Garçom Aço Inox", 309, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw79ccdc0b/images/59814017808074-saca-rolha.png?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Tradition Pegador Urso", 1267, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw92db77f9/images/panela-redonda-tradition-pegador-urso-cool%20mint.png?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature", 2019, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2e8c06a/images/panela-redonda-riviera-1.jpg?sw=650&sh=650&sm=fit"),
    ("Moedor de Pimenta 21cm", 369, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw33faad65/images/44001210995200-moedor-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Panela de Arroz Every sem Tampa Interna", 2199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8ed90701/images/21110200990449-Panela-de-Arroz.jpg?sw=650&sh=650&sm=fit"),
    ("Skillet Redonda Funda Signature", 1859, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2220c009/images/20187260990422-skillet-funda.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca Seattle 400ml", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw11d01c28/images/70317400990099-caneca-seattle-riviera.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Canelada", 529, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8cf77cfb/images/71120280990001-travessa-canelada-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Manteigueira", 429, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb10fb024/images/70837170990000-manteigueira-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Grelha Quadrada Signature", 1859, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaac10f34/images/20183260990422-grelha-quadrada.jpg?sw=650&sh=650&sm=fit"),
    ("Moedor de Sal 21cm", 369, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw33faad65/images/44001210995200-moedor-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Vaso para Ervas com Bandeja", 379, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5b37cb03/images/71302140990099-vaso-ervas-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca London 100ml", 129, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2a9c7e20/images/70305100990099-caneca-100ml-riviera.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca Bistrô 400ml", 189, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb4f02b8c/images/70304400990002-caneca-bistro-riviera.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl Redondo Vancouver", 139, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw95fdeb79/images/70158330990099-bowl-de-snack.jpg?sw=650&sh=650&sm=fit"),
    ("Grelha Retangular Tradicional", 1429, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4b48406c/images/20202320990460-grelha-retangular.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca London 300ml", 139, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1af63394/images/70303200990099-caneca-300ml-riviera.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Molheira Signature", 2099, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5e96c08c/images/21181160994450-panela-molheira-blue.jpg?sw=650&sh=650&sm=fit"),
    ("Mini Cocotte Pegador Preto", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7d622005/images/71901100990100-mini-cocotte-peg-preto.jpg?sw=650&sh=650&sm=fit"),
    ("Mini Cocotte Pegador Colorido", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw13e6bec8/images/71901100990000-mini-cocotte-peg-colorido-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Suporte de Silicone", 139, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb45a3d7f/images/42404200990000-suporte-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Suporte Silicone French", 139, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4c94c53d/images/42401200990000-suporte-de-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Set Pegadores de Silicone", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw78fe1175/images/42813000990000-pegador-de-silicone.jpg?sw=650&sh=650&sm=fit"),
    ("Set de 3 Travessas Retangulares Heritage", 1349, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc263a57a/images/79342000990082-set-3-travessas.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Oblong Signature", 2759, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwec210ab5/images/21112310994450-panela-oblong-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Cooler Sleeve", 309, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw805620ef/images/49309000990000-coler-sleeve-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Descanso Oval para Colher", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7e59948f/images/71507150990099-descanso-para-colher-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Jarra Clássica 600ml", 229, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw7420408d/images/70903060990002-jarra-600ml-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Caneca London 350ml", 159, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw07ae9b98/images/70302350990002-caneca-350ml-riviera.jpg?sw=650&sh=650&sm=fit"),
    ("Forma de Pão Retangular Canelada", 339, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dweea847ff/images/71115230990001-foma-de-pao-canelada.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular Heritage com Tampa", 1059, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc7eb44f2/images/71002400990080-travessa-retantular-com-tampa.jpg?sw=650&sh=650&sm=fit"),
    ("Descanso Redondo para Colher", 179, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw08bc9101/images/71512000990001-descanso-para-colher-oval.jpg?sw=650&sh=650&sm=fit"),
    ("Suporte para Ovo", 79, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5dedbf8a/images/71702000990099-suporte-de-ovo-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Forma de Pão Retangular Signature", 1759, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3b4fe2bd/images/20221230990422-forma-pao-sig-bleu-riviera-1.png?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular Heritage 19cm", 529, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1876dd56/images/71102190990001-travessa-retangular.jpg?sw=650&sh=650&sm=fit"),
    ("Ramekin 200ml", 139, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3c4b110f/images/70403200990099-ramekin-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl Redondo San Francisco", 449, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw125979d7/images/70157850997099-bowl-san-francisco-10.png?sw=650&sh=650&sm=fit"),
    ("Travessa Redonda para Torta Heritage", 429, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc3940810/images/71131230990001-travessa-para-torta.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular com Tampa Signature", 999, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1c630c59/images/79126310990080-travessa-com-tampa-2.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Everyday Signature", 2469, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw80a8723a/images/20331280990422-panela-redonda-everyday.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Quadrada Heritage", 399, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaeaac21b/images/71114230990001-travessa-quadrada.jpg?sw=650&sh=650&sm=fit"),
    ("Porta Utensílios Reto Signature 2.5L", 479, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw581def34/images/71500500990001-utensilio-reto-bleu-2.5.jpg?sw=650&sh=650&sm=fit"),
    ("Prato Raso San Francisco 22cm", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw30d6e7cb/images/70234220997099-prato-raso-san-22cm-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Prato Fundo 22cm", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9dccf1a0/images/70102220997099-prato-fundo-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Set 2 Ramekins 200ml", 249, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw233d3fce/images/79294200990006-set-ramekin-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Marmita Signature", 2789, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwee98c815/images/21114260990450-panela-marmita.jpg?sw=650&sh=650&sm=fit"),
    ("Panela de Arroz Every sem Tampa Interna", 2329, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8ed90701/images/21110200990449-Panela-de-Arroz.jpg?sw=650&sh=650&sm=fit"),
    ("Caçarola Buffet Signature", 2999, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature 20cm", 2329, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2e8c06a/images/panela-redonda-riviera-1.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature 22cm", 2619, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2e8c06a/images/panela-redonda-riviera-1.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature 24cm", 2949, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2e8c06a/images/panela-redonda-riviera-1.jpg?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature 26cm", 3429, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2e8c06a/images/panela-redonda-riviera-1.jpg?sw=650&sh=650&sm=fit"),
    ("Skillet Redonda Signature 23cm", 1739, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa644c41e/images/20182230990422-skillet-redonda-blue.jpg?sw=650&sh=650&sm=fit"),
    ("Skillet Redonda Signature 20cm", 1559, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa644c41e/images/20182230990422-skillet-redonda-blue.jpg?sw=650&sh=650&sm=fit"),
    ("Skillet Redonda Signature 26cm", 1999, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa644c41e/images/20182230990422-skillet-redonda-blue.jpg?sw=650&sh=650&sm=fit"),
    ("Porta Utensílios Reto Signature 1.1L", 319, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw73e517fb/images/71500100990001-utensilio-classico-bleu-1.1L.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl Redondo Vancouver 24cm", 439, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9a49755a/images/70120240990001-Bowl-Redondo-24cm.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl Redondo Vancouver 16cm", 209, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwda92585c/images/70117160997099-bowl-redondo-16cm.jpg?sw=650&sh=650&sm=fit"),
    ("Prato Fundo San Francisco", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw942c1bd2/images/70156960997099-pratosan-francisco-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Prato Raso San Francisco 27cm", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw30d6e7cb/images/70234220997099-prato-raso-san-22cm-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Prato Raso Vancouver 27cm", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw21007f59/images/70202270997099-prato-raso27cm-bleu.jpg?sw=650&sh=650&sm=fit"),
    ("Bowl Redondo San Francisco 10cm", 239, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw125979d7/images/70157850997099-bowl-san-francisco-10.png?sw=650&sh=650&sm=fit"),
    ("Prato Raso Vancouver 22cm", 219, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw99b3e915/images/70202270997099-prato-raso22cm-bleu.png?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular Heritage 32cm", 709, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1876dd56/images/71102190990001-travessa-retangular.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular Heritage 26cm", 349, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1876dd56/images/71102190990001-travessa-retangular.jpg?sw=650&sh=650&sm=fit"),
    ("Set de 3 Travessas Retangulares Heritage Thyme", 1349, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe5f15ecb/images/kit-3-travessas-heritage-thyme%20(2).png?sw=650&sh=650&sm=fit"),
    ("Descanso Oval para Colher Rose Quartz", 199, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw53bae0e8/images/produto-descanso-para-colher-quartz-1.png?sw=650&sh=650&sm=fit"),
    ("Suporte para Ovo Rose Quartz", 79, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw6c42c3cd/images/produto-suporte-para-ovo-quartz.png?sw=650&sh=650&sm=fit"),
    ("Porta Óleo 600ml Rose Quartz", 299, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc730b776/images/produto-suporte-para-oleo-quartz-lecreuset.png?sw=650&sh=650&sm=fit"),
    ("Manteigueira Rose Quartz", 429, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw0d603fd1/images/produto-manteigueira-quartz-lecreuset.png?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature Glinda Wicked Collection", 3399, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw99d3d451/images/panela-redonda-colecao-wicked-glinda%20(2).png?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Modern Heritage", 3699, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwfdb403b0/images/panela-redonda-26Cm-Modern-Heritage-meringue.png?sw=650&sh=650&sm=fit"),
    ("Caçarola Buffet Modern Heritage", 3819, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5a6b2fa5/images/cacarola-buffet-28Cm-Modern-laranja-Heritage.png?sw=650&sh=650&sm=fit"),
    ("Panela Redonda Signature Flamme Dorée", 3449, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwbfeb8b92/images/100%20Anos/panela-redonda-flame-doree.png?sw=650&sh=650&sm=fit"),
    ("Panela Abóbora Flamme Dorée", 4379, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwa57c56ea/images/100%20Anos/panela-abobora-flame-doree.png?sw=650&sh=650&sm=fit"),
    ("Livro Centenário Le Creuset", 1569, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw897e94ae/images/100%20Anos/livro-100-anos-lecreuset.png?sw=650&sh=650&sm=fit"),
    ("Caçarola Buffet Signature Flamme Dorée", 3449, "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe3d241cf/images/100%20Anos/Cacarola-redonda-flame-doree.png?sw=650&sh=650&sm=fit"),
]

print(f'Total produtos: {len(produtos)}')

novo_grid = '    <div class="product-grid">\n'
for p in produtos:
    novo_grid += card(*p) + '\n'
novo_grid += '    </div>'

start = html.find('    <div class="product-grid">')
end_marker = '    </div>\n  </div>\n</div>\n<footer'
grid_end_pos = html.find(end_marker)

html = html[:start] + novo_grid + html[grid_end_pos:]

# Update counts
import re
html = re.sub(r'<strong>\d+</strong> resultados', '<strong>120</strong> resultados', html)
html = re.sub(r'<span class="results-count">\d+ novos produtos</span>', '<span class="results-count">120 novos produtos</span>', html)

with open('colecao-lancamentos.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Pronto!')
