const fs = require('fs');
const path = require('path');
const BASE = String.raw`c:\Users\teste\aa\lecreuset`;
const IMG = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default';

const PRODUCTS = [
  {
    file: 'garrafa-otg-1l-berry.html',
    title: 'Garrafa Térmica 1L On The Go Berry',
    subtitle: 'On The Go · Aço Inox · Berry',
    price: 'R$ 389,00',
    installments: '3x R$ 129,67 sem juros',
    pix: 'R$ 369,55 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#8B1A8B',
    dotColor: '#c8102e',
    desc: 'A Garrafa Térmica On The Go de 1L da Le Creuset combina estética icônica com alto desempenho. Isolamento a vácuo de parede dupla mantém bebidas quentes por até 12 horas ou frias por até 24 horas. Tampa hermética que serve como copo extra, alça dobrável e base antiderrapante de silicone. Perfeita para o dia a dia, viagens e momentos ao ar livre.',
    specs: [['Material','Aço Inox'],['Cor','Berry'],['Capacidade','1 L'],['Quente','Até 12 horas'],['Frio','Até 24 horas'],['Lavagem','À mão'],['Origem','China'],['Garantia','10 anos']],
    images: [`${IMG}/dwce47f0e3/images/41066334390001-otg-garrafa-1L-1.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'copo-otg-berry.html',
    title: 'Copo Térmico 350ml On The Go Berry',
    subtitle: 'On The Go · Aço Inox · Berry',
    price: 'R$ 279,00',
    installments: '2x R$ 139,50 sem juros',
    pix: 'R$ 265,05 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#8B1A8B',
    dotColor: '#c8102e',
    desc: 'O Copo Térmico On The Go 350ml é compacto e estiloso. Isolamento a vácuo de parede dupla mantém bebidas quentes por até 6 horas ou frias por até 24 horas. Tampa com mecanismo de travamento antiverga e base antiderrapante de silicone. Ideal para o café da manhã ou para levar na mochila.',
    specs: [['Material','Aço Inox'],['Cor','Berry'],['Capacidade','350 ml'],['Quente','Até 6 horas'],['Frio','Até 24 horas'],['Lavagem','À mão'],['Origem','China'],['Garantia','10 anos']],
    images: [`${IMG}/dw60cf70ff/images/41067194390001-otg-copo-berry.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'pote-otg-berry.html',
    title: 'Pote Térmico 500ml On The Go Berry',
    subtitle: 'On The Go · Aço Inox · Berry',
    price: 'R$ 299,00',
    installments: '2x R$ 149,50 sem juros',
    pix: 'R$ 284,05 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#8B1A8B',
    dotColor: '#c8102e',
    desc: 'O Pote Térmico On The Go 500ml é perfeito para levar refeições ou snacks aonde você for. Isolamento a vácuo de parede dupla mantém os alimentos na temperatura ideal. Tampa hermética evita vazamentos e o design ergonômico facilita o transporte.',
    specs: [['Material','Aço Inox'],['Cor','Berry'],['Capacidade','500 ml'],['Lavagem','À mão'],['Origem','China'],['Garantia','10 anos']],
    images: [`${IMG}/dw8a6d9177/images/41068124390001-pote-otg-berry.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'lancheira-otg-berry.html',
    title: 'Lancheira 900ml On The Go Berry',
    subtitle: 'On The Go · Aço Inox · Berry',
    price: 'R$ 419,00',
    installments: '4x R$ 104,75 sem juros',
    pix: 'R$ 398,05 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#8B1A8B',
    dotColor: '#c8102e',
    desc: 'A Lancheira On The Go 900ml da Le Creuset foi criada para trazer praticidade e estilo à sua rotina diária. Com formato retangular e tampa hermética que evita vazamentos, ela é ideal para levar almoço ao trabalho, lanches ao ar livre ou refeições em viagem. Disponivel na vibrante cor Berry.',
    specs: [['Material','Aço Inox'],['Cor','Berry'],['Capacidade','900 ml'],['Lavagem','À mão'],['Origem','China'],['Garantia','10 anos']],
    images: [`${IMG}/dw68d094ec/images/41069224390001-lancheira-otg-berry.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'mini-cocotte-fruits-morango.html',
    title: 'Mini Cocotte Fruits Morango',
    subtitle: 'Cerâmica · Formato Morango',
    price: 'R$ 269,00',
    installments: '2x R$ 134,50 sem juros',
    pix: 'R$ 255,55 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#c8102e',
    dotColor: '#c8102e',
    desc: 'A Mini Cocotte Fruits em formato de Morango é uma peça única e divertida da Le Creuset. Feita em cerâmica premium com superfície esmaltada, combina charme e funcionalidade. Perfeita para sobremesas individuais, molhos, patês ou como peça decorativa. Vai ao forno, micro-ondas e congelador.',
    specs: [['Material','Cerâmica'],['Cor','Vermelho (Morango)'],['Capacidade','570 ml'],['Fontes de calor','Forno, Micro-ondas, Congelador'],['Lava-louças','Sim'],['Origem','Tailândia'],['Garantia','10 anos']],
    images: [`${IMG}/dwb8aa0646/images/coocotte-fruits-morango.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'mini-cocotte-fruits-berry.html',
    title: 'Mini Cocotte Fruits Berry (Vermelho)',
    subtitle: 'Cerâmica · Formato Frutas Vermelhas',
    price: 'R$ 269,00',
    installments: '2x R$ 134,50 sem juros',
    pix: 'R$ 255,55 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#c8102e',
    dotColor: '#c8102e',
    desc: 'A Mini Cocotte Fruits em formato de frutas vermelhas é uma peça encantadora da Le Creuset. Feita em cerâmica premium com superfície esmaltada, combina charme decorativo com funcionalidade real. Ideal para sobremesas individuais, servir molhos ou como presente. Vai ao forno, micro-ondas e congelador.',
    specs: [['Material','Cerâmica'],['Cor','Vermelho'],['Capacidade','570 ml'],['Fontes de calor','Forno, Micro-ondas, Congelador'],['Lava-louças','Sim'],['Origem','Tailândia'],['Garantia','10 anos']],
    images: [`${IMG}/dw22ab93b3/images/cocotte-berry-fruits-vermelho.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'mini-cocotte-fruits-pessego.html',
    title: 'Mini Cocotte Fruits Pêssego (Pêche)',
    subtitle: 'Cerâmica · Formato Pêssego',
    price: 'R$ 269,00',
    installments: '2x R$ 134,50 sem juros',
    pix: 'R$ 255,55 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#c8102e',
    dotColor: '#E8956D',
    desc: 'A Mini Cocotte Fruits em formato de Pêssego traz a leveza e o charme das frutas de verão para a sua cozinha. Feita em cerâmica premium com superfície esmaltada, é perfeita para sobremesas individuais, cremes, gelatinas ou servir pequenas porções. Vai ao forno, micro-ondas e congelador.',
    specs: [['Material','Cerâmica'],['Cor','Pêche'],['Capacidade','570 ml'],['Fontes de calor','Forno, Micro-ondas, Congelador'],['Lava-louças','Sim'],['Origem','Tailândia'],['Garantia','10 anos']],
    images: [`${IMG}/dwa46a8b65/images/cocotte-pessego-fruits-peche.png?sw=650&sh=650&sm=fit`]
  },
  {
    file: 'mini-cocotte-fruits-blueberry.html',
    title: 'Mini Cocotte Fruits Blueberry (Azure)',
    subtitle: 'Cerâmica · Formato Blueberry',
    price: 'R$ 269,00',
    installments: '2x R$ 134,50 sem juros',
    pix: 'R$ 255,55 no PIX (5% OFF)',
    badge: 'LANÇAMENTO',
    badgeColor: '#2060A0',
    dotColor: '#2060A0',
    desc: 'A Mini Cocotte Fruits em formato de Blueberry traz a delicadeza e o colorido das mirtilos para a mesa. Feita em cerâmica premium com superfície esmaltada na cor Azure, é perfeita para sobremesas individuais, gelatinas, cremes ou como peça decorativa única.',
    specs: [['Material','Cerâmica'],['Cor','Azure'],['Capacidade','570 ml'],['Fontes de calor','Forno, Micro-ondas, Congelador'],['Lava-louças','Sim'],['Origem','Tailândia'],['Garantia','10 anos']],
    images: [`${IMG}/dw706b9fa6/images/cocotte-blueberry-fruits-azure.png?sw=650&sh=650&sm=fit`]
  }
];

const TMPL = fs.readFileSync(path.join(BASE, '_prod_tmpl.html'), 'utf8');

function makeThumbs(images) {
  if (images.length <= 1) return '';
  const items = images.map((u,i) =>
    `<div class="${i===0?'thumb active':'thumb'}" onclick="setImg(this,'${u}')"><img src="${u}" alt="" /></div>`
  ).join('\n');
  return `<div class="gallery-thumbs">${items}</div>`;
}

function makeSpecs(sl) {
  return '<table class="spec-table">' +
    sl.map(([k,v]) => `<tr><td class="spec-key">${k}</td><td class="spec-val">${v}</td></tr>`).join('') +
    '</table>';
}

let count = 0;
for (const p of PRODUCTS) {
  let html = TMPL;
  html = html.replaceAll('{{TITLE}}', p.title);
  html = html.replaceAll('{{SUBTITLE}}', p.subtitle);
  html = html.replaceAll('{{PRICE}}', p.price);
  html = html.replaceAll('{{INSTALLMENTS}}', p.installments);
  html = html.replaceAll('{{PIX}}', p.pix);
  html = html.replaceAll('{{BADGE}}', p.badge);
  html = html.replaceAll('{{DESC}}', p.desc);
  html = html.replaceAll('{{SPECS}}', makeSpecs(p.specs));
  html = html.replaceAll('{{THUMBS}}', makeThumbs(p.images));
  html = html.replaceAll('{{IMG0}}', p.images[0]);
  // Fix badge color and back link for non-foret products
  html = html.replace('.badge-pill{display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;letter-spacing:.5px;background:#3B6B3B;color:#fff;margin-bottom:12px;}',
    `.badge-pill{display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;letter-spacing:.5px;background:${p.badgeColor};color:#fff;margin-bottom:12px;}`);
  html = html.replace('href="colecao-foret.html">Voltar para Cole&#231;&#227;o For&#234;t',
    'href="colecao-lancamentos.html">Voltar para Lan&#231;amentos');
  html = html.replace('href="colecao-foret.html">Ver Cole&#231;&#227;o Completa',
    'href="colecao-lancamentos.html">Ver Todos os Lan&#231;amentos');
  html = html.replace('href="colecao-foret.html"', 'href="colecao-lancamentos.html"');
  fs.writeFileSync(path.join(BASE, p.file), html, 'utf8');
  console.log('OK:', p.file);
  count++;
}
console.log(`\nTotal: ${count} páginas criadas`);
