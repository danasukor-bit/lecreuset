import re

# Template base: cacarola-buffet-signature.html
with open('cacarola-buffet-signature.html', 'r', encoding='utf-8') as f:
    template = f.read()

produtos = [
    {
        'file': 'panela-marmita-signature.html',
        'title': 'Panela Marmita Signature | Le Creuset Brasil',
        'nome': 'Panela Marmita Signature',
        'preco': '2.789,00',
        'parcelas': '10x R$ 278,90 sem juros',
        'descricao': 'A Panela Marmita Signature em Bleu Riviera combina design sofisticado e versatilidade. Ideal para cozimentos longos, mantém o calor uniformemente.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwee98c815/images/21114260990450-panela-marmita.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwee98c815/images/21114260990450-panela-marmita.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Panela Marmita Signature',
    },
    {
        'file': 'set-3-travessas-retangulares.html',
        'title': 'Set de 3 Travessas Retangulares Heritage | Le Creuset Brasil',
        'nome': 'Set de 3 Travessas Retangulares Heritage',
        'preco': '1.349,00',
        'parcelas': '10x R$ 134,90 sem juros',
        'descricao': 'O Set de 3 Travessas Retangulares Heritage em Bleu Riviera é perfeito para apresentar seus pratos com estilo.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc263a57a/images/79342000990082-set-3-travessas.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc263a57a/images/79342000990082-set-3-travessas.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Set de 3 Travessas Retangulares Heritage',
    },
    {
        'file': 'travessa-redonda-torta-heritage.html',
        'title': 'Travessa Redonda para Torta Heritage | Le Creuset Brasil',
        'nome': 'Travessa Redonda para Torta Heritage',
        'preco': '429,00',
        'parcelas': '4x R$ 107,25 sem juros',
        'descricao': 'A Travessa Redonda para Torta Heritage em Bleu Riviera é a escolha ideal para apresentar tortas e quiches com elegância.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc3940810/images/71131230990001-travessa-para-torta.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc3940810/images/71131230990001-travessa-para-torta.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Travessa Redonda para Torta Heritage',
    },
    {
        'file': 'grelha-quadrada-signature.html',
        'title': 'Grelha Quadrada Signature | Le Creuset Brasil',
        'nome': 'Grelha Quadrada Signature',
        'preco': '1.859,00',
        'parcelas': '10x R$ 185,90 sem juros',
        'descricao': 'A Grelha Quadrada Signature em Bleu Riviera oferece marcas de grelha perfeitas e distribuição uniforme do calor.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaac10f34/images/20183260990422-grelha-quadrada.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwaac10f34/images/20183260990422-grelha-quadrada.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Grelha Quadrada Signature',
    },
    {
        'file': 'panela-arroz-every.html',
        'title': 'Panela de Arroz Every sem Tampa Interna | Le Creuset Brasil',
        'nome': 'Panela de Arroz Every sem Tampa Interna',
        'preco': '2.199,00',
        'parcelas': '10x R$ 219,90 sem juros',
        'descricao': 'A Panela de Arroz Every em Bleu Riviera é especialmente projetada para cozinhar arroz perfeito com distribuição uniforme do calor.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8ed90701/images/21110200990449-Panela-de-Arroz.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8ed90701/images/21110200990449-Panela-de-Arroz.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Panela de Arroz Every',
    },
    {
        'file': 'grelha-retangular-tradicional.html',
        'title': 'Grelha Retangular Tradicional | Le Creuset Brasil',
        'nome': 'Grelha Retangular Tradicional',
        'preco': '1.429,00',
        'parcelas': '10x R$ 142,90 sem juros',
        'descricao': 'A Grelha Retangular Tradicional em Bleu Riviera oferece a perfeita combinação entre funcionalidade e design.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4b48406c/images/20202320990460-grelha-retangular.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4b48406c/images/20202320990460-grelha-retangular.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Grelha Retangular Tradicional',
    },
    {
        'file': 'travessa-retangular-heritage-tampa.html',
        'title': 'Travessa Retangular Heritage com Tampa | Le Creuset Brasil',
        'nome': 'Travessa Retangular Heritage com Tampa',
        'preco': '1.059,00',
        'parcelas': '10x R$ 105,90 sem juros',
        'descricao': 'A Travessa Retangular Heritage com Tampa em Bleu Riviera mantém seus pratos quentes e apresenta uma aparência impecável à mesa.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc7eb44f2/images/71002400990080-travessa-retantular-com-tampa.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwc7eb44f2/images/71002400990080-travessa-retantular-com-tampa.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Travessa Retangular Heritage com Tampa',
    },
    {
        'file': 'travessa-canelada.html',
        'title': 'Travessa Canelada | Le Creuset Brasil',
        'nome': 'Travessa Canelada',
        'preco': '529,00',
        'parcelas': '5x R$ 105,80 sem juros',
        'descricao': 'A Travessa Canelada em Bleu Riviera é uma peça versátil e elegante para servir e assar.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8cf77cfb/images/71120280990001-travessa-canelada-bleu.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8cf77cfb/images/71120280990001-travessa-canelada-bleu.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Travessa Canelada',
    },
    {
        'file': 'panela-oblong-signature.html',
        'title': 'Panela Oblong Signature | Le Creuset Brasil',
        'nome': 'Panela Oblong Signature',
        'preco': '2.759,00',
        'parcelas': '10x R$ 275,90 sem juros',
        'descricao': 'A Panela Oblong Signature em Bleu Riviera é ideal para assar carnes, aves e legumes. Seu formato alongado maximiza o espaço no forno.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwec210ab5/images/21112310994450-panela-oblong-bleu.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwec210ab5/images/21112310994450-panela-oblong-bleu.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Panela Oblong Signature',
    },
    {
        'file': 'travessa-retangular-tampa-signature.html',
        'title': 'Travessa Retangular com Tampa Signature | Le Creuset Brasil',
        'nome': 'Travessa Retangular com Tampa Signature',
        'preco': '999,00',
        'parcelas': '10x R$ 99,90 sem juros',
        'descricao': 'A Travessa Retangular com Tampa Signature em Bleu Riviera combina funcionalidade e beleza para servir à mesa.',
        'img_bleu': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1c630c59/images/79126310990080-travessa-com-tampa-2.jpg?sw=650&sh=650&sm=fit',
        'img_padrao': 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw1c630c59/images/79126310990080-travessa-com-tampa-2.jpg?sw=650&sh=650&sm=fit',
        'breadcrumb': 'Travessa Retangular com Tampa Signature',
    },
]

for p in produtos:
    html = template

    # Title
    html = re.sub(r'<title>.*?</title>', f'<title>{p["title"]}</title>', html)

    # Breadcrumb last item
    html = re.sub(r'Ca[çc]arola Buffet Signature</li>', f'{p["nome"]}</li>', html)

    # Product name in h1
    html = re.sub(
        r'(<h1[^>]*>)Ca[çc]arola Buffet Signature(</h1>)',
        rf'\g<1>{p["nome"]}\g<2>',
        html
    )

    # Main image src (mainImgEl)
    html = re.sub(
        r'(id="mainImgEl"[^>]*src=")[^"]*(")',
        rf'\g<1>{p["img_padrao"]}\g<2>',
        html
    )

    # Price
    html = re.sub(r'R\$\s*2\.999,00', f'R$ {p["preco"]}', html)
    html = re.sub(r'10x R\$ 299,90 sem juros', p['parcelas'], html)

    # Description paragraph (product description)
    html = re.sub(
        r'(id="prodDesc"[^>]*>)[^<]*(</p>)',
        rf'\g<1>{p["descricao"]}\g<2>',
        html
    )

    # Bleu Riviera swatch image
    html = html.replace(
        'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit',
        p['img_bleu']
    )

    # Add autocolor.js if not present
    if 'autocolor.js' not in html:
        html = html.replace('<script src="cart.js"></script>', '<script src="cart.js"></script>\n<script src="autocolor.js"></script>')

    with open(p['file'], 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Criado: {p["file"]}')

print('Pronto!')
