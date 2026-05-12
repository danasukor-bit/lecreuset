# -*- coding: utf-8 -*-
import os, re, glob

DIR = os.path.dirname(os.path.abspath(__file__))
BASE_IMG = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'

def img(h, f):
    return f'{BASE_IMG}{h}/images/{f}?sw=650&sh=650&sm=fit'

COLORS_HEX = {
    'Laranja':      ('#d46820', False),
    'Vermelho':     ('#c8102e', False),
    'Bleu Riviera': ('#2DBECD', False),
    'Azure':        ('#2060A0', False),
    'Meringue':     ('#F5F0E8', True),
    'Branco':       ('#F5F5F5', True),
    'Flint':        ('#9EA5AB', False),
    'Nectar':       ('#D4C44A', False),
    'Black Onyx':   ('#1C1C1C', False),
    'Shell Pink':   ('#F0B8C8', False),
    'Caribe':       ('#00B8D4', False),
    'Thyme':        ('#5A7A3A', False),
    'Bamboo':       ('#C8A87A', False),
    'Rhone':        ('#8080A0', False),
    'Kiwi':         ('#8DB650', False),
    'Camomille':    ('#E8C87A', False),
}

PRODUCTS = [
    {
        'id': 'cp1', 'slug': 'caneca-london',
        'name': 'Caneca London', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 100ml / 200ml / 350ml',
        'price_range': 'R$ 129,00 – R$ 159,00',
        'installment': 'ou 10x de R$ 15,90 sem juros',
        'img': img('dwf07f51d0', 'produto-lecreuset-caneca-200ml-vermelho.png'),
        'colors': ['Laranja','Vermelho','Bleu Riviera','Azure','Meringue','Branco','Flint','Nectar','Black Onyx'],
        'desc': 'A Caneca London da Le Creuset é feita em cerâmica premium com superfície esmaltada que facilita a remoção dos alimentos, tornando o processo de limpeza mais rápido e fácil. Com excelente retenção de calor, mantém suas bebidas quentes ou frias por mais tempo. Disponível em diferentes capacidades e nas cores exclusivas Le Creuset.',
        'features': [
            'Cerâmica premium para uso diário',
            'Superfície esmaltada que facilita a remoção dos alimentos e a limpeza',
            'Excelente retenção de calor — mantém bebidas quentes ou frias por mais tempo',
            'Segura para forno, micro-ondas, freezer e lava-louças',
            'Disponível em 100 ml, 200 ml e 350 ml',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Capacidade','100 ml / 200 ml / 350 ml'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Segura para uso em forno e micro-ondas',
                 'Não use sobre chama direta','Aguarde esfriar antes de lavar'],
    },
    {
        'id': 'cp2', 'slug': 'bowl-redondo-vancouver',
        'name': 'Bowl Redondo Vancouver', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 11cm / 16cm / 24cm',
        'price_range': 'R$ 139,00 – R$ 439,00',
        'installment': 'ou 10x de R$ 43,90 sem juros',
        'img': img('dwc3e0652f', 'produto-lecreuset-bowl-16cm-artichaut1.png'),
        'colors': ['Laranja','Vermelho','Bleu Riviera','Azure','Meringue','Branco','Flint','Nectar','Shell Pink','Bamboo','Rhone'],
        'desc': 'O Bowl Redondo Vancouver da Le Creuset é ideal para cereais, mingaus e sopas. Feito em cerâmica premium com esmalte vitrificado nas cores exclusivas Le Creuset, a superfície lisa facilita a remoção dos alimentos e permite uma limpeza rápida. Disponível em três tamanhos para atender diferentes necessidades à mesa.',
        'features': [
            'Cerâmica premium projetada para uso diário',
            'Esmalte vitrificado facilita a remoção dos alimentos',
            'Excelente retenção de calor — mantém a comida quente ou fria durante o serviço',
            'Seguro para forno, micro-ondas, freezer e lava-louças',
            'Disponível em 11 cm, 16 cm e 24 cm',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Tamanhos','11 cm / 16 cm / 24 cm'),
            ('Porções','1 porção (11cm) / 2 porções (16cm) / 4 porções (24cm)'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Segura para uso em forno e micro-ondas',
                 'Não lave enquanto a peça estiver quente','Não use sobre chama direta'],
    },
    {
        'id': 'cp3', 'slug': 'mini-cocotte',
        'name': 'Mini Cocotte', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 250ml',
        'price_range': 'R$ 167,30 – R$ 239,00',
        'installment': 'ou 10x de R$ 23,90 sem juros',
        'img': img('dwc027de66', 'produto-lecreuset-minicocotte-laranja-vermelho.png'),
        'colors': ['Laranja','Vermelho','Bleu Riviera','Azure','Caribe','Meringue','Branco','Nectar','Black Onyx','Thyme'],
        'desc': 'A Mini Cocotte da Le Creuset é um recipiente versátil em cerâmica premium, perfeito para porções individuais ou como elemento decorativo na cozinha. Combina o design clássico Le Creuset com funcionalidade prática para o uso diário — ideal para servir fondues, cremes, sobremesas e acompanhamentos diretamente na mesa.',
        'features': [
            'Cerâmica premium projetada para uso diário',
            'Superfície esmaltada que facilita a remoção dos alimentos e a limpeza',
            'Excelente retenção de calor — mantém a comida quente ou fria durante o serviço',
            'Segura para forno, micro-ondas, freezer e lava-louças',
            'Capacidade de 250 ml — porção individual',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Capacidade','250 ml'),
            ('Dimensões','14 cm (C) × 11 cm (L) × 8 cm (H)'), ('Porções','1 porção'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Segura para uso em forno e micro-ondas',
                 'Não use sobre chama direta','Aguarde esfriar antes de lavar'],
    },
    {
        'id': 'cp4', 'slug': 'caneca-bistro-400ml',
        'name': 'Caneca Bistrô 400ml', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 400ml',
        'price_range': 'R$ 189,00',
        'installment': 'ou 10x de R$ 18,90 sem juros',
        'img': img('dw2bd91f79', 'Caneca-azure-400ml.png'),
        'colors': ['Laranja','Vermelho','Bleu Riviera','Caribe','Meringue','Branco','Flint','Nectar','Black Onyx','Shell Pink','Kiwi'],
        'desc': 'Com forma que remete aos bistrôs franceses e capacidade generosa de 400 ml, a Caneca Bistrô da Le Creuset é ideal para café, chá, chocolate quente, sopas e muito mais. A cerâmica premium com superfície esmaltada mantém as bebidas na temperatura ideal por mais tempo e facilita a limpeza.',
        'features': [
            'Cerâmica premium para uso diário',
            'Superfície esmaltada que facilita a remoção dos alimentos e a limpeza',
            'Excelente retenção de calor — mantém bebidas quentes ou frias por mais tempo',
            'Segura para forno, micro-ondas, freezer e lava-louças',
            'Capacidade de 400 ml',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Capacidade','400 ml'),
            ('Dimensões','11 cm (C) × 15 cm (L) × 8 cm (H)'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Segura para uso em forno e micro-ondas',
                 'Não use sobre chama direta','Aguarde esfriar antes de lavar'],
    },
    {
        'id': 'cp5', 'slug': 'prato-raso-vancouver',
        'name': 'Prato Raso Vancouver', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 17cm / 22cm / 27cm',
        'price_range': 'R$ 199,00 – R$ 239,00',
        'installment': 'ou 10x de R$ 23,90 sem juros',
        'img': img('dwcc99b044', 'produto-lecreuset-prato-27cm-vermelho.png'),
        'colors': ['Laranja','Vermelho','Bleu Riviera','Azure','Caribe','Meringue','Branco','Flint','Nectar','Shell Pink','Rhone','Thyme'],
        'desc': 'O Prato Raso Vancouver da Le Creuset é feito em cerâmica premium, disponível nas cores irresistíveis da Le Creuset, ideal para quem ama cozinhar e montar uma mesa elegante. O acabamento em esmalte vitrificado resiste a lascas, arranhões e manchas, enquanto a superfície esmaltada facilita a remoção dos alimentos, tornando a limpeza mais rápida.',
        'features': [
            'Cerâmica premium projetada para uso diário',
            'Esmalte vitrificado resiste a lascas, arranhões e manchas',
            'Superfície esmaltada facilita a remoção dos alimentos e a limpeza',
            'Seguro para micro-ondas, freezer, forno e lava-louças',
            'Disponível em 17 cm, 22 cm e 27 cm',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Tamanhos','17 cm / 22 cm / 27 cm'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Não lave enquanto a peça estiver quente','Use descansos protetores após retirar do forno',
                 'Não coloque diretamente sobre chama aberta','Lava-louças e lavagem à mão'],
    },
    {
        'id': 'cp6', 'slug': 'prato-fundo-22cm',
        'name': 'Prato Fundo 22cm', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 22cm',
        'price_range': 'R$ 219,00',
        'installment': 'ou 10x de R$ 21,90 sem juros',
        'img': img('dwa640170f', 'produto-lecreuset-prato-fundo-vermelho.png'),
        'colors': ['Laranja','Vermelho','Bleu Riviera','Meringue','Branco','Flint','Nectar','Shell Pink'],
        'desc': 'O Prato Fundo 22cm da Le Creuset é perfeito para saborear uma variedade de massas, saladas e entradas. Fabricado em cerâmica premium nas cores exclusivas da marca, a peça apresenta superfície esmaltada que facilita a remoção dos alimentos, tornando a limpeza mais rápida, e é compatível com lava-louças.',
        'features': [
            'Cerâmica premium projetada para uso diário',
            'Superfície esmaltada permite limpeza mais fácil e rápida',
            'Excelente retenção de calor — mantém a comida quente ou fria',
            'Seguro para micro-ondas, freezer e lava-louças',
            '22 cm de diâmetro — ideal para massas e sopas',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Tamanho','22 cm'),
            ('Dimensões','22 cm (C) × 22 cm (L) × 4 cm (H)'), ('Porções','1 porção'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Não lave enquanto a peça estiver quente','Use descansos protetores após retirar do forno',
                 'Não coloque diretamente sobre chama aberta','Lava-louças e lavagem à mão'],
    },
    {
        'id': 'cp7', 'slug': 'travessa-canelada',
        'name': 'Travessa Canelada', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · 24cm / 28cm',
        'price_range': 'R$ 370,30 – R$ 529,00',
        'installment': 'ou 10x de R$ 52,90 sem juros',
        'img': img('dw678a9329', 'travessa-canelada-vermelho-lecreuset.jpg'),
        'colors': ['Laranja','Vermelho','Bleu Riviera'],
        'desc': 'A Travessa Canelada da Le Creuset foi projetada para preparar pratos caseiros, sobremesas e doces, como tortas de fruta ou tartes planas. Com design canelado clássico e cerâmica premium da Le Creuset, esta travessa vai da assadeira direto para a mesa com elegância.',
        'features': [
            'Cerâmica premium com excelente distribuição de calor para assar de forma uniforme',
            'Esmalte colorido não poroso, não reativo, resistente a arranhões e manchas',
            'Superfície esmaltada libera os alimentos facilmente para limpeza rápida',
            'Resistente a rachaduras',
            'Segura para freezer, forno, micro-ondas, lava-louças e utensílios de metal',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Tamanhos','24 cm / 28 cm'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Segura para uso em forno e micro-ondas',
                 'Não use sobre chama direta','Aguarde esfriar antes de lavar'],
    },
    {
        'id': 'cp8', 'slug': 'porta-sal',
        'name': 'Porta Sal', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada',
        'price_range': 'R$ 265,30 – R$ 379,00',
        'installment': 'ou 10x de R$ 37,90 sem juros',
        'img': img('dw3b75d249', 'porta_sal_vermelho_cerise.jpg'),
        'colors': ['Laranja','Bamboo','Branco','Flint','Nectar'],
        'desc': 'Este porta-sal de estilo clássico da Le Creuset apresenta uma abertura lateral ampla para fácil acesso ao sal, especiarias e temperos. Combina funcionalidade com a estética exclusiva da marca, sendo um acessório indispensável na cozinha de quem aprecia qualidade e bom gosto.',
        'features': [
            'Cerâmica premium para uso diário',
            'Superfície esmaltada facilita a limpeza',
            'Abertura lateral ampla para fácil acesso',
            'Design clássico Le Creuset',
            'Compatível com lava-louças',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'),
            ('Dimensões','12 cm (C) × 12 cm (L) × 13 cm (H)'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Lava-louças, lavagem à mão'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Não use sobre chama direta',
                 'Superfície esmaltada facilita a limpeza','Aguarde esfriar antes de lavar'],
    },
    {
        'id': 'cp9', 'slug': 'set-azeite-vinagre',
        'name': 'Set Azeite & Vinagre Clássico', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada · Set com 2 peças',
        'price_range': 'R$ 579,00',
        'installment': 'ou 10x de R$ 57,90 sem juros',
        'img': img('dwe9691760', '80803020600003.jpg'),
        'colors': [],
        'desc': 'O Set Azeite & Vinagre Clássico da Le Creuset é composto por duas galheteiras de cerâmica premium com rolhas de cortiça. Perfeito para presentear ou para quem busca elegância e praticidade à mesa. A cerâmica esmaltada não altera o sabor dos líquidos e mantém o produto protegido da luz.',
        'features': [
            'Set com 2 galheteiras de cerâmica premium',
            'Rolhas de cortiça naturais incluídas',
            'Cerâmica esmaltada não reativa — não altera o sabor do azeite ou vinagre',
            'Design clássico Le Creuset',
            'Ideal como presente',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Conteúdo','2 galheteiras + rolhas de cortiça'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Lava-louças, lavagem à mão'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Não use sobre chama direta',
                 'Superfície esmaltada facilita a limpeza'],
    },
    {
        'id': 'cp10', 'slug': 'pote-de-manteiga',
        'name': 'Pote de Manteiga', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada',
        'price_range': 'R$ 319,00',
        'installment': 'ou 10x de R$ 31,90 sem juros',
        'img': img('dwe2c6a579', 'produto-lecreuset-pote-manteiga-vermelho%20(1).png'),
        'colors': ['Laranja','Vermelho','Branco','Flint','Nectar'],
        'desc': 'O Pote de Manteiga da Le Creuset mantém a manteiga fresca e em temperatura ambiente ideal para fácil espalhamento, sem necessidade de refrigeração. Feito em cerâmica premium com esmalte vitrificado, é uma peça funcional e elegante que vai da geladeira direto para a mesa.',
        'features': [
            'Cerâmica premium — mantém a manteiga fresca em temperatura ambiente',
            'Design que facilita espalhamento sem necessidade de refrigeração',
            'Superfície esmaltada não reativa, não absorve aromas',
            'Compatível com lava-louças',
            'Inclui tampa',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Lava-louças, lavagem à mão'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Não use sobre chama direta',
                 'Superfície esmaltada facilita a limpeza','Guarde em local seco'],
    },
    {
        'id': 'cp11', 'slug': 'porta-condimento',
        'name': 'Porta Condimento', 'badge': 'Cerâmica',
        'subtitle': 'Cerâmica Esmaltada',
        'price_range': 'R$ 289,00 – R$ 439,00',
        'installment': 'ou 10x de R$ 43,90 sem juros',
        'img': img('dw96391238', 'porta-condimento-laranja-lecreuset4.png'),
        'colors': ['Laranja','Vermelho','Branco','Flint','Nectar'],
        'desc': 'O Porta Condimento da Le Creuset é ideal para organizar e servir azeite, vinagre, molhos e outros condimentos com elegância. Feito em cerâmica premium esmaltada nas cores exclusivas Le Creuset, combina praticidade e design sofisticado para qualquer mesa.',
        'features': [
            'Cerâmica premium para uso diário',
            'Superfície esmaltada não reativa — não altera o sabor dos condimentos',
            'Design elegante para servir à mesa',
            'Compatível com lava-louças',
            'Disponível em diferentes tamanhos',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'),
            ('Origem','Tailândia'), ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Lava-louças, lavagem à mão'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Não use sobre chama direta',
                 'Superfície esmaltada facilita a limpeza'],
    },
    {
        'id': 'cp12', 'slug': 'caneca-jardin',
        'name': 'Caneca Jardin 200ml', 'badge': 'Coleção Jardim',
        'subtitle': 'Cerâmica Esmaltada · 200ml',
        'price_range': 'R$ 111,30',
        'installment': 'ou 10x de R$ 11,13 sem juros',
        'img': img('dw4df08c7b', 'caneca-jardin.png'),
        'colors': [],
        'desc': 'A Caneca Jardin 200ml faz parte da encantadora Coleção Jardim da Le Creuset, com ilustrações botânicas delicadas sobre cerâmica premium. Perfeita para o café da manhã ou momentos de pausa, combina o charme artístico da linha Jardim com a qualidade e durabilidade que são marcas registradas da Le Creuset.',
        'features': [
            'Coleção Jardim — ilustrações botânicas exclusivas',
            'Cerâmica premium para uso diário',
            'Superfície esmaltada que facilita a limpeza',
            'Segura para forno, micro-ondas, freezer e lava-louças',
            'Capacidade de 200 ml',
        ],
        'specs': [
            ('Material','Cerâmica esmaltada'), ('Capacidade','200 ml'),
            ('Coleção','Jardim'), ('Origem','Tailândia'),
            ('Garantia','10 anos contra defeitos de fabricação'),
            ('Compatível com','Forno, micro-ondas, freezer, lava-louças'),
        ],
        'care': ['Pode ser lavada na lava-louças ou à mão','Segura para uso em forno e micro-ondas',
                 'Não use sobre chama direta','Aguarde esfriar antes de lavar'],
    },
]

# ── Shared HTML fragments ────────────────────────────────────────────────────

TOP_BAR = '<div class="top-bar">\U0001f69a Frete Grátis em compras acima de R$ 1.500,00 &nbsp;|&nbsp; 5% OFF no PIX &nbsp;|&nbsp; 10x Sem Juros</div>'

NAV = '''<nav>
      <ul class="nav-list">
        <li>
          <a href="#">Comprar</a>
          <div class="mega-menu">
            <div class="mega-inner">
              <div class="mega-col">
                <div class="mega-col-title">Cozinhar</div>
                <a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a>
                <a href="colecao-frigideiras-e-skillets.html">Frigideiras e Skillets</a>
                <a href="colecao-grelhas.html">Grelhas</a>
                <a href="colecao-antiaderente.html">Antiaderente</a>
                <a href="colecao-cacarolas.html">Caçarolas</a>
                <a href="#">Chaleiras de Aço Esmaltado</a>
                <a href="#">3-Ply Aço Inox</a>
                <a href="#">Aço Inox</a>
                <a href="#">Formatos Especiais</a>
                <a href="#">Acessórios</a>
                <a href="#">Minha Primeira Le Creuset</a>
                <a href="#">Stockpots</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Assar</div>
                <a href="#">Mini Cocotte e Ramekins</a>
                <a href="#">Formas Metal Bakeware</a>
                <a href="#">Assadeiras e Travessas</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Acessórios</div>
                <a href="#">Moedores e Galheteiro</a>
                <a href="#">Utensílios</a>
                <a href="#">Utensílios de Madeira</a>
                <a href="#">Suportes e Descansos</a>
                <a href="#">Potes e Porta-Mantimentos</a>
                <a href="#">Acessórios de Vinhos</a>
                <a href="#">Sets</a>
                <a href="#">Decoração</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Preparar e Servir</div>
                <a href="colecao-ceramica.html">Bowls</a>
                <a href="colecao-ceramica.html">Pratos</a>
                <a href="colecao-ceramica.html">Canecas e Xícaras</a>
                <a href="#">Bules e Jarras</a>
                <a href="#">Chaleiras</a>
                <a href="colecao-ceramica.html">Travessas</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Coleções</div>
                <a href="#">Flamme Dorée</a>
                <a href="#">Gift Collection</a>
                <a href="#">Churrasco</a>
                <a href="#">Coleção Alpine</a>
                <a href="#">Modern Heritage</a>
                <a href="#">Coleção Jardim</a>
                <a href="#">Culinária Oriental</a>
                <a href="#">Coleção Gourmand</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Nossas Cores</div>
                <div class="mega-colors">
                  <div class="mega-color-dot" style="background:#2DBECD;" title="Bleu Riviera"></div>
                  <div class="mega-color-dot" style="background:#d46820;" title="Laranja"></div>
                  <div class="mega-color-dot" style="background:#c8102e;" title="Vermelho"></div>
                  <div class="mega-color-dot" style="background:#C85250;" title="Cerise"></div>
                  <div class="mega-color-dot" style="background:#6B4226;" title="Marronnier"></div>
                  <div class="mega-color-dot" style="background:#D4C44A;" title="Nectar"></div>
                  <div class="mega-color-dot" style="background:#B8BEC4;" title="Mist"></div>
                  <div class="mega-color-dot" style="background:#D4779A;" title="Rose Quartz"></div>
                  <div class="mega-color-dot" style="background:#F5F5F5;border:1px solid #ddd;" title="Branco"></div>
                  <div class="mega-color-dot" style="background:#9B7EB0;" title="Bluebell"></div>
                  <div class="mega-color-dot" style="background:#2060A0;" title="Azure"></div>
                  <div class="mega-color-dot" style="background:#D4A017;" title="Flamme Dorée"></div>
                  <div class="mega-color-dot" style="background:#5A5A5A;" title="Graphite"></div>
                  <div class="mega-color-dot" style="background:#1C1C1C;" title="Matte Black"></div>
                </div>
              </div>
              <div class="mega-col" style="padding-top:4px;">
                <a href="#" style="display:block; overflow:hidden; border-radius:6px;">
                  <img class="mega-img" src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit" alt="Bleu Riviera Le Creuset" />
                </a>
              </div>
            </div>
          </div>
        </li>
        <li class="highlight"><a href="#">Páscoa</a></li>
        <li><a href="#">Ofertas</a></li>
        <li class="blue"><a href="#">Bleu Riviera</a></li>
        <li><a href="#">Lançamentos</a></li>
        <li><a href="#">Ferro Fundido</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="#">Nossas Cores</a></li>
        <li><a href="#">Best-Sellers</a></li>
      </ul>
    </nav>'''

HEADER_ICONS = '''<div class="header-icons">
      <div class="search-box">
        <input type="text" placeholder="Buscar..." />
        <button><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
      </div>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Entrar</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Lista</span></a>
      <a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4zM3 6h18M16 10a4 4 0 0 1-8 0" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Sacola</span></a>
    </div>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Le <span style="color:#c8102e">Creuset</span></a>
        <p>Desde 1925, criamos peças excepcionais que transformam a experiência culinária e duram gerações.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a>
          <a href="#" class="social-btn">in</a>
          <a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul>
        <li><a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a></li>
        <li><a href="colecao-frigideiras-e-skillets.html">Frigideiras</a></li>
        <li><a href="colecao-cacarolas.html">Caçarolas</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="colecao-antiaderente.html">Antiaderente</a></li>
      </ul></div>
      <div class="footer-col"><h4>Atendimento</h4><ul>
        <li><a href="#">Central de Ajuda</a></li>
        <li><a href="#">Rastrear Pedido</a></li>
        <li><a href="#">Trocas e Devoluções</a></li>
        <li><a href="#">Garantia</a></li>
      </ul></div>
      <div class="footer-col"><h4>Empresa</h4><ul>
        <li><a href="#">Sobre Nós</a></li>
        <li><a href="#">Lojas Físicas</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">Receitas</a></li>
      </ul></div>
      <div class="footer-col"><h4>Legal</h4><ul>
        <li><a href="#">Política de Privacidade</a></li>
        <li><a href="#">Termos de Uso</a></li>
        <li><a href="#">Cookies</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Le Creuset do Brasil. Todos os direitos reservados.</p>
      <div class="payment-icons">
        <span class="payment-icon">VISA</span>
        <span class="payment-icon">MASTER</span>
        <span class="payment-icon">PIX</span>
        <span class="payment-icon">BOLETO</span>
      </div>
    </div>
  </div>
</footer>'''

# ── Collection page CSS ──────────────────────────────────────────────────────
COL_CSS = '''*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Nunito Sans', sans-serif; color: #000; background: #fff; }
    a { text-decoration: none; color: inherit; }
    .top-bar { background: #1a1a1a; color: #fff; font-size: 12px; text-align: center; padding: 8px 16px; }
    header { background: #fff; border-bottom: 1px solid #e5e5e5; position: sticky; top: 0; z-index: 100; }
    .header-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: flex; align-items: center; height: 64px; gap: 24px; }
    .logo { font-size: 22px; font-weight: 800; letter-spacing: -1px; white-space: nowrap; flex-shrink: 0; }
    .logo span { color: #c8102e; }
    nav { flex: 1; }
    .nav-list { display: flex; list-style: none; align-items: center; }
    .nav-list > li { position: relative; }
    .nav-list > li > a { display: block; padding: 22px 14px; font-size: 13px; font-weight: 600; color: #000; white-space: nowrap; border-bottom: 2px solid transparent; transition: border-color 0.2s; }
    .nav-list > li > a:hover { border-bottom-color: #000; }
    .nav-list > li.highlight > a { color: #c8102e; }
    .nav-list > li.blue > a { color: #2563ab; }
    .mega-menu { display: none; position: fixed; left: 0; right: 0; top: 64px; background: #fff; border-top: 2px solid #e5e5e5; box-shadow: 0 8px 32px rgba(0,0,0,0.13); z-index: 200; padding: 28px 0 24px; }
    .nav-list > li:hover .mega-menu { display: block; }
    .mega-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: 170px 150px 170px 170px 170px 140px 220px; gap: 0 20px; align-items: start; }
    .mega-col-title { font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: #000; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 1px solid #e5e5e5; }
    .mega-col a { display: block; font-size: 13px; color: #444; padding: 4px 0; transition: color 0.15s; }
    .mega-col a:hover { color: #c8102e; }
    .mega-colors { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
    .mega-color-dot { width: 22px; height: 22px; border-radius: 50%; border: 1.5px solid transparent; cursor: pointer; transition: transform 0.2s, border-color 0.2s; }
    .mega-color-dot:hover { border-color: #000; transform: scale(1.12); }
    .mega-img { width: 100%; object-fit: cover; border-radius: 6px; }
    .dropdown { display: none; position: absolute; top: 100%; left: 0; background: #fff; border: 1px solid #e5e5e5; min-width: 200px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); z-index: 200; padding: 12px 0; }
    .nav-list > li:hover .dropdown { display: block; }
    .dropdown a { display: block; padding: 8px 20px; font-size: 13px; color: #333; }
    .dropdown a:hover { background: #f5f5f5; }
    .header-icons { display: flex; align-items: center; gap: 16px; flex-shrink: 0; }
    .header-icons a { font-size: 12px; font-weight: 600; display: flex; flex-direction: column; align-items: center; gap: 2px; color: #000; }
    .header-icons svg { width: 22px; height: 22px; }
    .search-box { display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px; overflow: hidden; height: 36px; }
    .search-box input { border: none; outline: none; padding: 0 12px; font-size: 13px; width: 180px; font-family: inherit; }
    .search-box button { background: #000; border: none; cursor: pointer; padding: 0 12px; height: 100%; display: flex; align-items: center; }
    .search-box button svg { fill: #fff; width: 16px; height: 16px; }
    .cat-banner { width: 100%; height: 220px; overflow: hidden; position: relative; background: #1a1a1a; }
    .cat-banner img { width: 100%; height: 100%; object-fit: cover; object-position: center 40%; display: block; }
    .cat-banner-overlay { position: absolute; inset: 0; background: linear-gradient(to right, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.1) 60%); display: flex; align-items: center; padding: 0 80px; }
    .cat-banner-title { color: #fff; font-size: 40px; font-weight: 800; letter-spacing: -0.5px; }
    .breadcrumb { max-width: 1400px; margin: 0 auto; padding: 14px 24px; font-size: 12px; color: #888; display: flex; gap: 6px; align-items: center; }
    .breadcrumb a { color: #888; } .breadcrumb a:hover { text-decoration: underline; } .breadcrumb span { color: #bbb; }
    .shop-layout { max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; display: grid; grid-template-columns: 220px 1fr; gap: 40px; align-items: start; }
    .sidebar { position: sticky; top: 80px; }
    .sidebar-section { margin-bottom: 28px; }
    .sidebar-title { font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 1px solid #e5e5e5; }
    .sidebar-list { list-style: none; }
    .sidebar-list li { margin-bottom: 8px; }
    .sidebar-list li a { font-size: 13px; color: #444; display: flex; align-items: center; gap: 8px; }
    .sidebar-list li a:hover { color: #c8102e; }
    .sidebar-colors { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }
    .sidebar-dot { width: 22px; height: 22px; border-radius: 50%; cursor: pointer; border: 1.5px solid transparent; transition: transform 0.15s, border-color 0.15s; }
    .sidebar-dot:hover { border-color: #000; transform: scale(1.1); }
    .product-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
    .product-card { position: relative; }
    .product-card-img { position: relative; overflow: hidden; background: #f8f8f8; aspect-ratio: 1; margin-bottom: 12px; }
    .product-card-img img { width: 100%; height: 100%; object-fit: contain; padding: 16px; transition: transform 0.4s ease; }
    .product-card-img:hover img { transform: scale(1.06); }
    .product-wishlist { position: absolute; top: 10px; right: 10px; width: 32px; height: 32px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    .product-wishlist svg { width: 16px; height: 16px; }
    .product-card-name { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
    .product-card-sub { font-size: 12px; color: #888; margin-bottom: 6px; }
    .product-card-price { font-size: 15px; font-weight: 800; }
    .product-card-price-sub { font-size: 11px; color: #888; }
    .product-colors { position: absolute; bottom: 48px; left: 10px; display: flex; gap: 4px; z-index: 2; flex-wrap: wrap; max-width: 90%; }
    .swatch { width: 18px; height: 18px; border-radius: 50%; cursor: pointer; border: 1.5px solid rgba(255,255,255,0.8); display: inline-block; transition: transform 0.2s, border-color 0.2s; }
    .swatch:hover, .swatch.active { border-color: #000; transform: scale(1.15); }
    .results-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
    .results-count { font-size: 13px; color: #888; }
    .sort-select { font-size: 13px; border: 1px solid #ccc; padding: 6px 12px; font-family: inherit; cursor: pointer; }
    footer { background: #111; color: #fff; padding: 60px 24px 30px; }
    .footer-inner { max-width: 1400px; margin: 0 auto; }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
    .footer-brand .logo { font-size: 20px; margin-bottom: 16px; display: block; }
    .footer-brand p { font-size: 13px; color: #aaa; line-height: 1.7; max-width: 280px; margin-bottom: 20px; }
    .footer-social { display: flex; gap: 12px; }
    .social-btn { width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; transition: border-color 0.2s, background 0.2s; }
    .social-btn:hover { border-color: #fff; background: rgba(255,255,255,0.1); }
    .footer-col h4 { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 16px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul li a { font-size: 13px; color: #aaa; transition: color 0.2s; }
    .footer-col ul li a:hover { color: #fff; }
    .footer-bottom { border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 12px; color: #666; }
    .payment-icons { display: flex; gap: 8px; }
    .payment-icon { background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }'''

# ── Product page CSS ─────────────────────────────────────────────────────────
PROD_CSS = '''*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Nunito Sans', sans-serif; color: #000; background: #fff; }
    a { text-decoration: none; color: inherit; }
    .top-bar { background: #1a1a1a; color: #fff; font-size: 12px; text-align: center; padding: 8px 16px; letter-spacing: 0.5px; }
    header { background: #fff; border-bottom: 1px solid #e5e5e5; position: sticky; top: 0; z-index: 100; }
    .header-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: flex; align-items: center; height: 64px; gap: 24px; }
    .logo { font-size: 22px; font-weight: 800; letter-spacing: -1px; white-space: nowrap; flex-shrink: 0; }
    .logo span { color: #c8102e; }
    nav { flex: 1; }
    .nav-list { display: flex; list-style: none; align-items: center; }
    .nav-list > li { position: relative; }
    .nav-list > li > a { display: block; padding: 22px 14px; font-size: 13px; font-weight: 600; color: #000; white-space: nowrap; border-bottom: 2px solid transparent; transition: border-color 0.2s; }
    .nav-list > li > a:hover { border-bottom-color: #000; }
    .nav-list > li.highlight > a { color: #c8102e; }
    .nav-list > li.blue > a { color: #2563ab; }
    .mega-menu { display: none; position: fixed; left: 0; right: 0; top: 64px; background: #fff; border-top: 2px solid #e5e5e5; box-shadow: 0 8px 32px rgba(0,0,0,0.13); z-index: 200; padding: 28px 0 24px; }
    .nav-list > li:hover .mega-menu { display: block; }
    .mega-inner { max-width: 1400px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: 170px 150px 170px 170px 170px 140px 220px; gap: 0 20px; align-items: start; }
    .mega-col-title { font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: #000; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 1px solid #e5e5e5; }
    .mega-col a { display: block; font-size: 13px; color: #444; padding: 4px 0; transition: color 0.15s; }
    .mega-col a:hover { color: #c8102e; }
    .mega-colors { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
    .mega-color-dot { width: 22px; height: 22px; border-radius: 50%; border: 1.5px solid transparent; cursor: pointer; transition: transform 0.2s, border-color 0.2s; }
    .mega-color-dot:hover { border-color: #000; transform: scale(1.12); }
    .mega-img { width: 100%; object-fit: cover; border-radius: 6px; }
    .dropdown { display: none; position: absolute; top: 100%; left: 0; background: #fff; border: 1px solid #e5e5e5; min-width: 200px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); z-index: 200; padding: 12px 0; }
    .nav-list > li:hover .dropdown { display: block; }
    .dropdown a { display: block; padding: 8px 20px; font-size: 13px; color: #333; }
    .dropdown a:hover { background: #f5f5f5; }
    .header-icons { display: flex; align-items: center; gap: 16px; flex-shrink: 0; }
    .header-icons a { font-size: 12px; font-weight: 600; display: flex; flex-direction: column; align-items: center; gap: 2px; color: #000; }
    .header-icons svg { width: 22px; height: 22px; }
    .search-box { display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px; overflow: hidden; height: 36px; }
    .search-box input { border: none; outline: none; padding: 0 12px; font-size: 13px; width: 180px; font-family: inherit; }
    .search-box button { background: #000; border: none; cursor: pointer; padding: 0 12px; height: 100%; display: flex; align-items: center; }
    .search-box button svg { fill: #fff; width: 16px; height: 16px; }
    .breadcrumb { max-width: 1400px; margin: 0 auto; padding: 14px 24px; font-size: 12px; color: #888; display: flex; gap: 6px; align-items: center; }
    .breadcrumb a { color: #888; } .breadcrumb a:hover { text-decoration: underline; } .breadcrumb span { color: #bbb; }
    .product-wrap { max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; }
    .gallery { position: sticky; top: 80px; }
    .gallery-main { width: 100%; aspect-ratio: 1; background: #f8f8f8; display: flex; align-items: center; justify-content: center; overflow: hidden; cursor: zoom-in; }
    .gallery-main img { width: 100%; height: 100%; object-fit: contain; padding: 24px; transition: transform 0.4s ease; }
    .gallery-main:hover img { transform: scale(1.08); }
    .product-info { padding-top: 4px; }
    .product-badges-top { display: flex; gap: 8px; margin-bottom: 12px; }
    .badge-pill { font-size: 11px; font-weight: 700; padding: 3px 10px; letter-spacing: 0.5px; border: 1px solid #000; }
    .product-title { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; line-height: 1.2; margin-bottom: 6px; }
    .product-subtitle { font-size: 14px; color: #666; margin-bottom: 20px; }
    .product-price-block { margin-bottom: 20px; }
    .price-range { font-size: 24px; font-weight: 800; color: #000; }
    .price-installment { font-size: 13px; color: #555; margin-top: 4px; }
    .price-pix { font-size: 12px; color: #c8102e; font-weight: 700; margin-top: 4px; }
    .color-picker { margin-bottom: 20px; }
    .color-picker-label { font-size: 13px; font-weight: 600; margin-bottom: 10px; }
    .color-swatches { display: flex; gap: 8px; flex-wrap: wrap; }
    .color-swatch { width: 28px; height: 28px; border-radius: 50%; cursor: pointer; border: 2px solid transparent; transition: transform 0.2s, border-color 0.2s; }
    .color-swatch:hover { transform: scale(1.15); }
    .color-swatch.active { border-color: #000; }
    .qty-row { display: flex; align-items: center; gap: 16px; margin-bottom: 16px; }
    .qty-label { font-size: 13px; font-weight: 600; }
    .qty-control { display: flex; align-items: center; border: 1px solid #ccc; }
    .qty-btn { width: 36px; height: 36px; background: none; border: none; cursor: pointer; font-size: 18px; display: flex; align-items: center; justify-content: center; }
    .qty-btn:hover { background: #f5f5f5; }
    .qty-input { width: 48px; height: 36px; border: none; border-left: 1px solid #ccc; border-right: 1px solid #ccc; text-align: center; font-size: 14px; font-family: inherit; outline: none; }
    .btn-cart { width: 100%; background: #000; color: #fff; border: none; padding: 16px; font-size: 14px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer; font-family: inherit; margin-bottom: 12px; transition: background 0.2s; }
    .btn-cart:hover { background: #222; }
    .btn-wishlist { width: 100%; background: #fff; color: #000; border: 1px solid #000; padding: 14px; font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 24px; transition: background 0.2s; }
    .btn-wishlist:hover { background: #f5f5f5; }
    .btn-wishlist svg { width: 18px; height: 18px; }
    .shipping-info { border-top: 1px solid #e5e5e5; padding-top: 20px; }
    .shipping-row { font-size: 13px; color: #555; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
    .shipping-row svg { width: 18px; height: 18px; flex-shrink: 0; }
    .cep-input { display: flex; gap: 8px; }
    .cep-input input { flex: 1; border: 1px solid #ccc; padding: 8px 12px; font-size: 13px; font-family: inherit; outline: none; }
    .cep-input button { background: #000; color: #fff; border: none; padding: 8px 16px; font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; }
    .trust-badges-wrap { background: #f8f8f8; padding: 32px 24px; }
    .trust-badges { max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
    .trust-badge { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; }
    .trust-badge-icon svg { width: 40px; height: 40px; }
    .trust-badge-text { font-size: 13px; font-weight: 700; }
    .trust-badge-sub { font-size: 11px; color: #666; }
    .product-tabs { max-width: 1400px; margin: 0 auto; padding: 0 24px 60px; }
    .tab { border-bottom: 1px solid #e5e5e5; }
    .tab-header { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; cursor: pointer; font-size: 15px; font-weight: 700; }
    .tab-header svg { width: 20px; height: 20px; transition: transform 0.3s; flex-shrink: 0; }
    .tab-header.open svg { transform: rotate(180deg); }
    .tab-body { display: none; padding: 0 0 24px; }
    .tab-body.open { display: block; }
    .tab-body p { font-size: 14px; line-height: 1.8; color: #444; margin-bottom: 12px; }
    .tab-body ul { padding-left: 20px; }
    .tab-body ul li { font-size: 14px; line-height: 1.8; color: #444; margin-bottom: 6px; }
    .specs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
    .spec-row { display: flex; padding: 10px 0; border-bottom: 1px solid #f0f0f0; gap: 16px; }
    .spec-key { font-size: 13px; color: #888; min-width: 160px; flex-shrink: 0; }
    .spec-val { font-size: 13px; font-weight: 600; }
    footer { background: #111; color: #fff; padding: 60px 24px 30px; }
    .footer-inner { max-width: 1400px; margin: 0 auto; }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
    .footer-brand .logo { font-size: 20px; margin-bottom: 16px; display: block; }
    .footer-brand p { font-size: 13px; color: #aaa; line-height: 1.7; max-width: 280px; margin-bottom: 20px; }
    .footer-social { display: flex; gap: 12px; }
    .social-btn { width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; transition: border-color 0.2s, background 0.2s; }
    .social-btn:hover { border-color: #fff; background: rgba(255,255,255,0.1); }
    .footer-col h4 { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 16px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul li a { font-size: 13px; color: #aaa; transition: color 0.2s; }
    .footer-col ul li a:hover { color: #fff; }
    .footer-bottom { border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 12px; color: #666; }
    .payment-icons { display: flex; gap: 8px; }
    .payment-icon { background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }'''

PROD_JS = '''<script>
function toggleTab(header) {
  var body = header.nextElementSibling;
  header.classList.toggle('open');
  body.classList.toggle('open');
}
function selectColor(el, name, src) {
  document.querySelectorAll('.color-swatch').forEach(function(s){ s.classList.remove('active'); });
  el.classList.add('active');
  document.getElementById('colorName').textContent = name;
  if (src) { document.getElementById('mainImgEl').src = src; }
}
function changeQty(delta) {
  var inp = document.getElementById('qtyInput');
  inp.value = Math.max(1, parseInt(inp.value) + delta);
}
</script>'''

COL_JS = '''<script>
function swatchClick(swatch, imgId, newSrc) {
  var colors = swatch.parentElement;
  colors.querySelectorAll('.swatch').forEach(function(s){ s.classList.remove('active'); });
  swatch.classList.add('active');
  var img = document.getElementById(imgId);
  if (img) img.src = newSrc;
}
</script>'''

# ── Build collection page ────────────────────────────────────────────────────
def build_collection():
    cards_html = ''
    for p in PRODUCTS:
        img_tag = f'<img id="{p["id"]}" src="{p["img"]}" alt="{p["name"]}" />'
        # Color swatches for collection card
        if p['colors']:
            spans = ''
            for i, cname in enumerate(p['colors'][:8]):  # show max 8 in card
                if cname not in COLORS_HEX:
                    continue
                bg, need_border = COLORS_HEX[cname]
                border_style = ' border:1px solid #ccc;' if need_border else ''
                active_cls = ' active' if i == 0 else ''
                spans += f'\n            <span class="swatch{active_cls}" style="background:{bg};{border_style}" title="{cname}" onclick="swatchClick(this,\'{p["id"]}\',\'{p["img"]}\')"></span>'
            swatch_div = f'\n          <div class="product-colors">{spans}\n          </div>'
        else:
            swatch_div = ''

        cards_html += f'''    <div class="product-card">
      <a href="{p["slug"]}.html">
        <div class="product-card-img">
          {img_tag}</a>{swatch_div}
          <div class="product-wishlist">
            <svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
        </div>
      </div>
      <a href="{p["slug"]}.html">
        <div class="product-card-name">{p["name"]}</div>
        <div class="product-card-sub">{p["subtitle"]}</div>
        <div class="product-card-price">{p["price_range"]}</div>
      </a>
    </div>\n'''

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Cerâmica | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>{COL_CSS}</style>
</head>
<body>
{TOP_BAR}
<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    {NAV}
    {HEADER_ICONS}
  </div>
</header>

<div class="cat-banner">
  <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dw557e5a8f/category/cat_banners/ceramica_categoria_banner.jpg" alt="Cerâmica Le Creuset" />
  <div class="cat-banner-overlay">
    <h1 class="cat-banner-title">Cerâmica</h1>
  </div>
</div>

<div class="breadcrumb">
  <a href="index.html">Home</a><span>/</span>
  <span>Cerâmica</span>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Canecas e Xícaras</a></li>
        <li><a href="#">Bowls</a></li>
        <li><a href="#">Mini Cocottes</a></li>
        <li><a href="#">Pratos</a></li>
        <li><a href="#">Travessas e Assadeiras</a></li>
        <li><a href="#">Armazenar e Servir</a></li>
        <li><a href="#">Sets e Presenteáveis</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Cores</div>
      <div class="sidebar-colors">
        <div class="sidebar-dot" style="background:#d46820;" title="Laranja"></div>
        <div class="sidebar-dot" style="background:#c8102e;" title="Vermelho"></div>
        <div class="sidebar-dot" style="background:#2DBECD;" title="Bleu Riviera"></div>
        <div class="sidebar-dot" style="background:#2060A0;" title="Azure"></div>
        <div class="sidebar-dot" style="background:#F5F0E8;border:1px solid #ccc;" title="Meringue"></div>
        <div class="sidebar-dot" style="background:#F5F5F5;border:1px solid #ccc;" title="Branco"></div>
        <div class="sidebar-dot" style="background:#9EA5AB;" title="Flint"></div>
        <div class="sidebar-dot" style="background:#D4C44A;" title="Nectar"></div>
        <div class="sidebar-dot" style="background:#1C1C1C;" title="Black Onyx"></div>
        <div class="sidebar-dot" style="background:#F0B8C8;" title="Shell Pink"></div>
        <div class="sidebar-dot" style="background:#00B8D4;" title="Caribe"></div>
        <div class="sidebar-dot" style="background:#5A7A3A;" title="Thyme"></div>
      </div>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Preço</div>
      <ul class="sidebar-list">
        <li><a href="#">Até R$ 150</a></li>
        <li><a href="#">R$ 150 – R$ 300</a></li>
        <li><a href="#">R$ 300 – R$ 500</a></li>
        <li><a href="#">Acima de R$ 500</a></li>
      </ul>
    </div>
  </aside>
  <div>
    <div class="results-bar">
      <span class="results-count">{len(PRODUCTS)} produtos</span>
      <select class="sort-select"><option>Mais Relevante</option><option>Menor Preço</option><option>Maior Preço</option><option>Mais Novo</option></select>
    </div>
    <div class="product-grid">
{cards_html}    </div>
  </div>
</div>

{FOOTER}
{COL_JS}
</body>
</html>'''
    return html

# ── Build product page ───────────────────────────────────────────────────────
SVG_CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>'

def build_product(p):
    # Color swatches
    if p['colors']:
        first_color = p['colors'][0]
        color_name_span = first_color
        swatches_html = ''
        for i, cname in enumerate(p['colors']):
            if cname not in COLORS_HEX:
                continue
            bg, need_border = COLORS_HEX[cname]
            border_style = ' border:1px solid #ccc;' if need_border else ''
            active_cls = ' active' if i == 0 else ''
            swatches_html += f'\n        <div class="color-swatch{active_cls}" style="background:{bg};{border_style}" title="{cname}" onclick="selectColor(this,\'{cname}\',null)"></div>'
        color_picker = f'''<div class="color-picker">
      <div class="color-picker-label">Cor: <span id="colorName">{color_name_span}</span></div>
      <div class="color-swatches">{swatches_html}
      </div>
    </div>'''
    else:
        color_picker = ''

    # Specs
    specs_html = ''
    for key, val in p['specs']:
        specs_html += f'\n        <div class="spec-row"><span class="spec-key">{key}</span><span class="spec-val">{val}</span></div>'

    # Care
    care_html = ''.join(f'\n        <li>{c}</li>' for c in p['care'])

    # Features / description bullets
    features_html = ''.join(f'\n        <li>{f}</li>' for f in p['features'])

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["name"]} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>{PROD_CSS}</style>
</head>
<body>
{TOP_BAR}
<header>
  <div class="header-inner">
    <a href="index.html" class="logo">Le <span>Creuset</span></a>
    {NAV}
    {HEADER_ICONS}
  </div>
</header>

<div class="breadcrumb">
  <a href="index.html">Home</a><span>/</span>
  <a href="colecao-ceramica.html">Cerâmica</a><span>/</span>
  <span>{p["name"]}</span>
</div>

<div class="product-wrap">
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImgEl" src="{p["img"]}" alt="{p["name"]}" />
    </div>
  </div>
  <div class="product-info">
    <div class="product-badges-top">
      <span class="badge-pill">{p["badge"]}</span>
    </div>
    <h1 class="product-title">{p["name"]}</h1>
    <p class="product-subtitle">{p["subtitle"]}</p>
    <div class="product-price-block">
      <div class="price-range">{p["price_range"]}</div>
      <div class="price-installment">{p["installment"]}</div>
      <div class="price-pix">5% OFF no PIX</div>
    </div>
    {color_picker}
    <div class="qty-row">
      <span class="qty-label">Quantidade</span>
      <div class="qty-control">
        <button class="qty-btn" onclick="changeQty(-1)">&#8722;</button>
        <input class="qty-input" type="number" id="qtyInput" value="1" min="1" />
        <button class="qty-btn" onclick="changeQty(1)">+</button>
      </div>
    </div>
    <button class="btn-cart">Adicionar ao Carrinho</button>
    <button class="btn-wishlist">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Adicionar à Lista de Desejos
    </button>
    <div class="shipping-info">
      <div class="shipping-row">
        <svg viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="1.5"><path d="M1 3h15v13H1zM16 8h4l3 3v5h-7V8zM5.5 21a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM18.5 21a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Calcular frete e prazo de entrega:
      </div>
      <div class="cep-input">
        <input type="text" placeholder="Digite seu CEP" maxlength="9" />
        <button>Calcular</button>
      </div>
    </div>
  </div>
</div>

<div class="trust-badges-wrap">
  <div class="trust-badges">
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M32 6 L54 14 L54 34 C54 48 43 56 32 60 C21 56 10 48 10 34 L10 14 Z"/><polyline points="22 32 29 39 42 26"/></svg></div>
      <div class="trust-badge-text">10 Anos de Garantia</div>
      <div class="trust-badge-sub">Garantia contra defeitos de fabricação</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="28" r="18"/><path d="M20 52 C20 44 44 44 44 52"/><path d="M26 22 L32 16 L38 22 M32 16 L32 36"/></svg></div>
      <div class="trust-badge-text">Fabricado na Tailândia</div>
      <div class="trust-badge-sub">Qualidade e tradição Le Creuset</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="20" width="36" height="24" rx="2"/><path d="M40 28 L52 28 L60 38 L60 44 L40 44 Z"/><circle cx="16" cy="48" r="5"/><circle cx="50" cy="48" r="5"/></svg></div>
      <div class="trust-badge-text">Frete Grátis*</div>
      <div class="trust-badge-sub">Em compras acima de R$ 1.500,00</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M32 8 L36 20 L50 20 L39 28 L43 42 L32 34 L21 42 L25 28 L14 20 L28 20 Z"/></svg></div>
      <div class="trust-badge-text">30 Dias para Trocar</div>
      <div class="trust-badge-sub">Troca ou devolução sem custo</div>
    </div>
  </div>
</div>

<div class="product-tabs">
  <div class="tab">
    <div class="tab-header open" onclick="toggleTab(this)">Descrição {SVG_CHEVRON}</div>
    <div class="tab-body open">
      <p>{p["desc"]}</p>
      <ul>{features_html}
      </ul>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">Especificações Técnicas {SVG_CHEVRON}</div>
    <div class="tab-body">
      <div class="specs-grid"><div>{specs_html}
      </div></div>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">Uso e Cuidado {SVG_CHEVRON}</div>
    <div class="tab-body">
      <ul>{care_html}
      </ul>
    </div>
  </div>
</div>

{FOOTER}
{PROD_JS}
</body>
</html>'''
    return html

# ── Write files ──────────────────────────────────────────────────────────────
# Collection page
col_path = os.path.join(DIR, 'colecao-ceramica.html')
with open(col_path, 'w', encoding='utf-8') as f:
    f.write(build_collection())
print('Created: colecao-ceramica.html')

# Product pages
for p in PRODUCTS:
    path = os.path.join(DIR, f'{p["slug"]}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_product(p))
    print(f'Created: {p["slug"]}.html')

# ── Update nav in all existing HTML files ────────────────────────────────────
updated = 0
for fpath in glob.glob(os.path.join(DIR, '*.html')):
    if os.path.basename(fpath) == 'colecao-ceramica.html':
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    new_html = html.replace(
        '<a href="#">Cerâmica</a>',
        '<a href="colecao-ceramica.html">Cerâmica</a>'
    )
    # Also update "Preparar e Servir" links if they're still placeholder
    new_html = new_html.replace(
        '<a href="#">Bowls</a>\n                <a href="#">Pratos</a>\n                <a href="#">Canecas e Xícaras</a>',
        '<a href="colecao-ceramica.html">Bowls</a>\n                <a href="colecao-ceramica.html">Pratos</a>\n                <a href="colecao-ceramica.html">Canecas e Xícaras</a>'
    )
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f'Updated nav in {updated} existing files')
print('Done!')
