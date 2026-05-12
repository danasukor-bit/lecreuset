import os

BASE = r'c:\Users\teste\aa\lecreuset'
IMG = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default'

PRODUCTS = [
  {
    'file': 'panela-redonda-signature-foret.html',
    'title': 'Panela Redonda Signature Foret 28 cm',
    'subtitle': 'Ferro Fundido Esmaltado - Foret',
    'price': 'R$ 3.429,00',
    'installments': '10x R$ 342,90 sem juros',
    'pix': 'R$ 3.257,55 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'A panela redonda iconica da Le Creuset em sua versao mais popular. O ferro fundido esmaltado distribui e reten calor de forma uniforme, ideal para cozimento lento. Pronta para uso sem pre-tempero, com interior esmaltado na cor areia que resiste a odores e sabores. 15 artesaos especializados inspecionam manualmente cada peca produzida na Franca desde 1925.',
    'specs': [('Material','Ferro Fundido Esmaltado'),('Cor','Foret'),('Capacidade','6,7 L'),('Tamanho','28 cm'),('Dimensoes','37,7 x 29,7 x 18,4 cm'),('Fontes de calor','Vitroceramico, Inducao, Eletrico, Gas'),('Origem','Franca'),('Garantia','Vitalicia'),('Limpeza','Lavagem a mao')],
    'images': [
      IMG+'/dw5cb33aa8/images/21177240984450-panela-redonda-foret.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw400cfa84/images/21177240984450-panela-redonda-foret-1.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw4357ddb9/images/21177240984450-panela-redonda-foret-2.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw01fb5b90/images/21177240984450-panela-redonda-foret-3.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'panela-oval-signature-foret.html',
    'title': 'Panela Oval Signature Foret 31 cm',
    'subtitle': 'Ferro Fundido Esmaltado - Foret',
    'price': 'R$ 3.399,00',
    'installments': '10x R$ 339,90 sem juros',
    'pix': 'R$ 3.229,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'A panela oval iconica da Le Creuset em ferro fundido esmaltado. O formato oval e especialmente adequado para cortes maiores de carne, aves inteiras e paes ovais. Distribuicao de calor superior com retencao excepcional que preserva umidade e sabor.',
    'specs': [('Material','Ferro Fundido Esmaltado'),('Cor','Foret'),('Capacidade','6,3 L'),('Tamanho','31 cm'),('Dimensoes','40,4 x 25,7 x 17,9 cm'),('Fontes de calor','Vitroceramico, Inducao, Eletrico, Gas'),('Forno','Ate 260 graus C'),('Origem','Franca'),('Garantia','Vitalicia'),('Limpeza','Lavagem a mao')],
    'images': [
      IMG+'/dw1047b189/images/21178310984450-panela-oval.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'cacarola-buffet-signature-foret.html',
    'title': 'Cacarola Buffet Signature Foret 30 cm',
    'subtitle': 'Ferro Fundido Esmaltado - Foret',
    'price': 'R$ 2.999,00',
    'installments': '10x R$ 299,90 sem juros',
    'pix': 'R$ 2.849,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'Cacarola de ferro fundido esmaltado com distribuicao e retencao de calor excepcionais. Vai do forno direto a mesa de forma elegante. Pronta para uso sem tempero, resiste a manchas e lascas. Tampa hermetica circula vapor e devolve umidade aos alimentos.',
    'specs': [('Material','Ferro Fundido Esmaltado'),('Cor','Foret'),('Capacidade','3,5 L'),('Porcoes','6-8 pessoas'),('Tamanho','30 cm'),('Dimensoes','40,2 x 31,7 x 13,5 cm'),('Fontes de calor','Inducao, Gas, Eletrico, Forno'),('Origem','Franca'),('Garantia','Vitalicia'),('Limpeza','Lava-loucas ou mao')],
    'images': [
      IMG+'/dw913d8b67/images/21180300984450-cacarola-buffet-foret.png?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'panela-redonda-signature-foret-20cm.html',
    'title': 'Panela Redonda Signature Foret 20 cm',
    'subtitle': 'Ferro Fundido Esmaltado - Foret',
    'price': 'R$ 2.329,00',
    'installments': '10x R$ 232,90 sem juros',
    'pix': 'R$ 2.212,55 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'A panela redonda iconica Le Creuset em versao compacta, ideal para 2-3 pessoas. O mesmo desempenho excepcional do ferro fundido esmaltado: distribuicao uniforme de calor e retencao superior. Perfeita para molhos, porcoes individuais e receitas menores.',
    'specs': [('Material','Ferro Fundido Esmaltado'),('Cor','Foret'),('Capacidade','2,4 L'),('Tamanho','20 cm'),('Dimensoes','27,3 x 21,5 x 14,1 cm'),('Fontes de calor','Vitroceramico, Inducao, Eletrico, Gas'),('Origem','Franca'),('Garantia','Vitalicia'),('Limpeza','Lavagem a mao')],
    'images': [
      IMG+'/dw5cb33aa8/images/21177240984450-panela-redonda-foret.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw400cfa84/images/21177240984450-panela-redonda-foret-1.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'travessa-retangular-san-francisco-foret.html',
    'title': 'Travessa Retangular com Tampa San Francisco Foret 31 cm',
    'subtitle': 'Ceramica - Foret',
    'price': 'R$ 1.199,00',
    'installments': '10x R$ 119,90 sem juros',
    'pix': 'R$ 1.139,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'Travessa retangular de ceramica com tampa da colecao San Francisco na exclusiva cor Foret. Com 4L de capacidade, e perfeita para servir e armazenar com elegancia. Vai ao forno, micro-ondas e congelador. A tampa veda os aromas e preserva a umidade dos alimentos.',
    'specs': [('Material','Ceramica'),('Cor','Foret'),('Capacidade','4 L'),('Tamanho','31 cm'),('Dimensoes','40,9 x 25,4 x 13,45 cm'),('Fontes de calor','Forno, Micro-ondas, Congelador'),('Origem','Tailandia'),('Garantia','10 anos'),('Limpeza','Lava-loucas ou mao')],
    'images': [
      IMG+'/dw553d597a/images/71025310980280-travessa-retagular-com-tampa-san.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw865d4887/images/71025310980280-travessa-retagular-com-tampa-san-1.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw148edb42/images/71025310980280-travessa-retagular-com-tampa-san-2.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'travessa-quadrada-san-francisco-foret.html',
    'title': 'Travessa Quadrada com Tampa San Francisco Foret',
    'subtitle': 'Ceramica - Foret',
    'price': 'R$ 899,00',
    'installments': '9x R$ 99,89 sem juros',
    'pix': 'R$ 854,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'Travessa quadrada de ceramica com tampa da colecao San Francisco na cor Foret. Com 2,9L de capacidade, ideal para servir e armazenar com elegancia. Tampa inclusa para preservar aromas e umidade. Combina funcionalidade com o design assinado da Le Creuset.',
    'specs': [('Material','Ceramica'),('Cor','Foret'),('Capacidade','2,9 L'),('Dimensoes','33,3 x 25,3 x 13,3 cm'),('Fontes de calor','Forno, Micro-ondas, Congelador'),('Origem','Tailandia'),('Garantia','10 anos'),('Limpeza','Lava-loucas ou mao')],
    'images': [
      IMG+'/dw62754017/images/71026230980280-travessa-quadrada-com-tampa-san-francisco.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw0d9ae26e/images/71026230980280-travessa-quadrada-com-tampa-san-francisco-1.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dwa0d4ac53/images/71026230980280-travessa-quadrada-com-tampa-san-francisco-2.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw6af506b8/images/71026230980280-travessa-quadrada-com-tampa-san-francisco-3.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'chaleira-classica-foret.html',
    'title': 'Chaleira Classica Foret',
    'subtitle': 'Aco Carbono Esmaltado - Foret',
    'price': 'R$ 929,00',
    'installments': '9x R$ 103,22 sem juros',
    'pix': 'R$ 882,55 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'Adicione um toque classico a sua cozinha com a Chaleira Classica da Le Creuset na exclusiva cor Foret. Feita em aco carbono esmaltado para ferver agua rapidamente. Apito de tom unico avisa quando a agua ferve. Inclui marcacoes internas de nivel e alca resistente ao calor.',
    'specs': [('Material','Aco Carbono Esmaltado'),('Cor','Foret'),('Capacidade','1,6 L'),('Porcoes','6 xicaras'),('Dimensoes','26,4 x 20,9 x 25,1 cm'),('Fontes de calor','Vitroceramico, Inducao, Eletrico, Gas'),('Origem','Tailandia'),('Garantia','5 anos'),('Limpeza','Lavagem a mao')],
    'images': [
      IMG+'/dw05492d65/images/40104010981000-chaleira-classica-foret.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dwf61f32b8/images/40104010981000-chaleira-classica-foret-1.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'chaleira-kone-foret.html',
    'title': 'Chaleira Kone Foret',
    'subtitle': 'Aco Carbono Esmaltado - Foret',
    'price': 'R$ 839,00',
    'installments': '8x R$ 104,88 sem juros',
    'pix': 'R$ 797,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'A Chaleira Kone e feita com Aco Carbono Esmaltado que possibilita ferver agua rapidamente. Possui apito de tom unico indicando quando a agua ferve, marcacoes internas e base generosa. Compativel com todas as fontes de calor incluindo inducao. Design moderno e iconico.',
    'specs': [('Material','Aco Carbono Esmaltado'),('Cor','Foret'),('Capacidade','1,6 L'),('Dimensoes','25,2 x 20 x 24 cm'),('Fontes de calor','Vitroceramico, Inducao, Eletrico, Gas'),('Origem','Tailandia'),('Garantia','5 anos'),('Limpeza','Lavagem a mao')],
    'images': [
      IMG+'/dwebf93040/images/40125600982300-chaleira-kone-foret.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw181a64f0/images/40125600982300-chaleira-kone-foret-1.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dwacb02a63/images/40125600982300-chaleira-kone-foret2.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'moedor-sal-foret.html',
    'title': 'Moedor de Sal 21 cm Foret',
    'subtitle': 'Acessorios - Foret',
    'price': 'R$ 369,00',
    'installments': '3x R$ 123,00 sem juros',
    'pix': 'R$ 350,55 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'Moedor de sal premium com mecanismo de moagem ceramica ajustavel. Controle o tamanho da granulacao via pino superior ajustavel, do fino ao grosso. Ideal para uso a mesa, churrascos e aplicacoes com sal grosso. Combine com o Moedor de Pimenta Foret.',
    'specs': [('Material','Plastico ABS'),('Mecanismo','Ceramica ajustavel'),('Cor','Foret'),('Dimensoes','6,1 x 6,1 x 20,6 cm'),('Origem','China'),('Garantia','10 anos'),('Limpeza','Pano seco ou escova')],
    'images': [
      IMG+'/dw8a52997b/images/44002210985200-moedor-foret.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dwa6a9c05d/images/44002210985200-moedor-sal.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'moedor-pimenta-foret.html',
    'title': 'Moedor de Pimenta 21 cm Foret',
    'subtitle': 'Acessorios - Foret',
    'price': 'R$ 369,00',
    'installments': '3x R$ 123,00 sem juros',
    'pix': 'R$ 350,55 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'Moedor de pimenta que combina sofisticacao e praticidade. Sistema de moagem ceramica ajustavel do fino ao grosso. Exterior em plastico ABS resistente a odores e facil de limpar. Design ergonomico para o dia a dia e ocasioes especiais. Combine com o Moedor de Sal Foret.',
    'specs': [('Material','Plastico ABS'),('Mecanismo','Ceramica ajustavel'),('Cor','Foret'),('Dimensoes','6,1 x 6,1 x 20,6 cm'),('Origem','China'),('Garantia','10 anos'),('Limpeza','Pano seco ou escova')],
    'images': [
      IMG+'/dw8a52997b/images/44002210985200-moedor-foret.jpg?sw=650&sh=650&sm=fit',
      IMG+'/dw94398809/images/44001210985200-moedor-pimenta.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'caneca-200ml-foret.html',
    'title': 'Caneca London 200ml Foret',
    'subtitle': 'Ceramica - Foret',
    'price': 'R$ 139,00',
    'installments': 'em ate 1x sem juros',
    'pix': 'R$ 132,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'A Caneca London e perfeita para cafe, cha e chocolate quente. Ceramica premium com superficie esmaltada para facil limpeza e higiene. Vai ao forno, micro-ondas e congelador. O formato classico e a cor Foret trazem elegancia ao momento do seu cafe.',
    'specs': [('Material','Ceramica'),('Cor','Foret'),('Capacidade','200 ml'),('Dimensoes','10,7 x 7,8 x 7,8 cm'),('Fontes de calor','Forno, Micro-ondas, Congelador'),('Origem','Tailandia'),('Garantia','10 anos'),('Limpeza','Lava-loucas ou mao')],
    'images': [
      IMG+'/dw75fddb92/images/70303200980099-caneca-foret-200ml.jpg?sw=650&sh=650&sm=fit',
    ],
  },
  {
    'file': 'ramekin-200ml-foret.html',
    'title': 'Ramekin 200ml Foret',
    'subtitle': 'Ceramica - Foret',
    'price': 'R$ 139,00',
    'installments': 'em ate 1x sem juros',
    'pix': 'R$ 132,05 no PIX (5% OFF)',
    'badge': 'LANCAMENTO',
    'desc': 'De bolos a gratinados e tortas, tudo fica mais saboroso no Ramekin Le Creuset. Superficie esmaltada para facil desenformagem e excelente retencao de calor. Borda interna permite empilhamento sem grudar. Vai ao forno, micro-ondas e congelador.',
    'specs': [('Material','Ceramica'),('Cor','Foret'),('Capacidade','200 ml'),('Dimensoes','9,3 x 9,3 x 5,6 cm'),('Fontes de calor','Forno, Micro-ondas, Congelador'),('Origem','Tailandia'),('Garantia','10 anos'),('Limpeza','Lava-loucas ou mao')],
    'images': [
      IMG+'/dw8f850e0f/images/70403200980099-mini-cocotte.jpg?sw=650&sh=650&sm=fit',
    ],
  },
]

tmpl = open(BASE + r'\_prod_tmpl.html', encoding='utf-8').read()

def make_thumbs(images):
    if len(images) <= 1:
        return ''
    items = ''
    for i, u in enumerate(images):
        cls = 'thumb active' if i == 0 else 'thumb'
        items += f'<div class="{cls}" onclick="setImg(this,\'{u}\')"><img src="{u}" alt="" /></div>\n'
    return f'<div class="gallery-thumbs">{items}</div>'

def make_specs(sl):
    rows = ''
    for k, v in sl:
        rows += f'<tr><td class="spec-key">{k}</td><td class="spec-val">{v}</td></tr>\n'
    return f'<table class="spec-table">{rows}</table>'

count = 0
for p in PRODUCTS:
    html = tmpl
    html = html.replace('{{TITLE}}', p['title'])
    html = html.replace('{{SUBTITLE}}', p['subtitle'])
    html = html.replace('{{PRICE}}', p['price'])
    html = html.replace('{{INSTALLMENTS}}', p['installments'])
    html = html.replace('{{PIX}}', p['pix'])
    html = html.replace('{{BADGE}}', p['badge'])
    html = html.replace('{{DESC}}', p['desc'])
    html = html.replace('{{SPECS}}', make_specs(p['specs']))
    html = html.replace('{{THUMBS}}', make_thumbs(p['images']))
    html = html.replace('{{IMG0}}', p['images'][0])
    path = os.path.join(BASE, p['file'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1
    print(f'OK: {p["file"]}')

print(f'\nTotal: {count} paginas criadas')
