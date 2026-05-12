# -*- coding: utf-8 -*-
import os, glob

DIR  = os.path.dirname(os.path.abspath(__file__))
CDN  = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'
BANNER = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwec30f170/category/Formatos-Especiais2.png'

COLORS_HEX = {
    'Laranja':     '#d46820',
    'Vermelho':    '#c8102e',
    'Azure':       '#2060A0',
    'Shell Pink':  '#F0B8C8',
    'Meringue':    '#F5F0E8',
    'Chambray':    '#8090B0',
    'Flint':       '#9EA5AB',
    'Onyx':        '#1C1C1C',
    'Black Onyx':  '#1C1C1C',
    'Matte Black': '#222222',
    'Nectar':      '#D4C44A',
    'Bamboo':      '#C8A87A',
    'Deep Teal':   '#1A6B6B',
    'Marseille':   '#2DBECD',
    'Bleu Riviera':'#2DBECD',
    'Branco':      '#F5F5F5',
    'Thyme':       '#5A7A3A',
    'Camomille':   '#E8C87A',
    'Rhone':       '#8080A0',
}

def img(h, f): return f'{CDN}{h}/images/{f}?sw=650&sh=650&sm=fit'
def otg(h, f): return f'{CDN}{h}/images/tardes%20de%20verao/{f}?sw=650&sh=650&sm=fit'

DESCRIPTIONS = {
    'garrafa-hidratacao': {
        'desc': '<p>A Garrafa de Hidratação Le Creuset em aço inox com isolamento de parede dupla mantém bebidas quentes por até 12 horas e frias por até 24 horas. Com 500ml de capacidade, é ideal para academia, escritório ou passeios diários. Disponível nas icônicas cores Le Creuset.</p><ul><li>Isolamento de parede dupla a vácuo</li><li>Mantém quente até 12h e frio até 24h</li><li>Garantia de 5 anos contra defeitos de fabricação</li><li>Lavar somente à mão com detergente neutro</li><li>Não usar na lava-louças, micro-ondas ou freezer</li></ul>',
        'specs': {'Capacidade': '500 ml', 'Material': 'Aço Inox', 'Isolamento': 'Parede dupla a vácuo', 'Manter quente': 'até 12 horas', 'Manter frio': 'até 24 horas', 'Modo de Lavagem': 'Somente à mão', 'Garantia': '5 anos'},
    },
    'garrafa-termica-otg': {
        'desc': '<p>A linha On The Go Le Creuset oferece a solução perfeita para quem busca praticidade e estilo no dia a dia. A Garrafa Térmica OTG combina durabilidade e eficiência para manter a temperatura das bebidas por horas.</p><ul><li>Alça dobrável resistente e fixada, sem deformações</li><li>Isolamento de parede dupla a vácuo — quente até 12h, frio até 24h</li><li>Tampa hermética com vedação segura para transporte</li><li>Base de silicone antiderrapante com logo da marca</li><li>Tampa que funciona como xícara</li><li>Lavar somente à mão com água morna e sabão neutro</li></ul>',
        'specs': {'Material': 'Aço Inox', 'Isolamento': 'Parede dupla a vácuo', 'Manter quente': 'até 12 horas', 'Manter frio': 'até 24 horas', 'Base': 'Silicone antiderrapante', 'Modo de Lavagem': 'Somente à mão'},
    },
    'copo-termico-350ml': {
        'desc': '<p>O Copo Térmico 350ml da linha On The Go foi desenvolvido para pessoas em movimento constante, unindo praticidade, estilo e qualidade Le Creuset. Compacto e eficiente, é ideal para café, chá e outras bebidas.</p><ul><li>Capacidade: 350ml</li><li>Mantém quente até 6h e frio até 24h</li><li>Isolamento de parede dupla a vácuo</li><li>Tampa com vedação hermética antirespingo</li><li>Trava de segurança nas posições aberta e fechada</li><li>Base de silicone antiderrapante com logo da marca</li><li>Lavar somente à mão com água morna e sabão neutro</li></ul>',
        'specs': {'Capacidade': '350 ml', 'Material': 'Aço Inox', 'Isolamento': 'Parede dupla a vácuo', 'Manter quente': 'até 6 horas', 'Manter frio': 'até 24 horas', 'Modo de Lavagem': 'Somente à mão'},
    },
    'pote-termico-500ml': {
        'desc': '<p>O Pote Térmico 500ml da linha On The Go combina funcionalidade, design elegante e durabilidade para o dia a dia. Ideal para transportar sopas, ensopados, snacks ou refeições mantendo a temperatura por horas.</p><ul><li>Capacidade: 500ml — ideal para porções individuais</li><li>Isolamento de parede dupla a vácuo — quente até 6h, frio até 24h</li><li>Tampa hermética antirespingo</li><li>Não usar para cozinhar — apenas para manutenção de temperatura</li><li>Lavar somente à mão com água morna e sabão neutro</li></ul>',
        'specs': {'Capacidade': '500 ml', 'Material': 'Aço Inox', 'Isolamento': 'Parede dupla a vácuo', 'Manter quente': 'até 6 horas', 'Manter frio': 'até 24 horas', 'Modo de Lavagem': 'Somente à mão'},
    },
    'lancheira-900ml': {
        'desc': '<p>A Lancheira 900ml da linha On The Go Le Creuset traz praticidade e estilo para a rotina diária. Design moderno e funcional para transportar refeições com segurança e elegância — para o trabalho, escola ou atividades ao ar livre.</p><ul><li>Capacidade: 900ml — ideal para refeições completas</li><li>Design compacto, cabe facilmente em bolsas e mochilas</li><li>Tampa hermética — evita entrada de ar, umidade e impurezas</li><li>Preserva o sabor e a textura dos alimentos ao longo do dia</li><li>Não possui função térmica</li><li>Lavar à mão com água morna e sabão neutro</li></ul>',
        'specs': {'Capacidade': '900 ml', 'Material': 'Aço Inox', 'Função térmica': 'Não', 'Fechamento': 'Tampa hermética', 'Modo de Lavagem': 'Somente à mão'},
    },
    'luva-dupla': {
        'desc': '<p>Proteja as suas mãos com as Luvas Duplas para forno Le Creuset. Feitas em 100% algodão, são resistentes ao calor e ao vapor, proporcionando proteção máxima ao transferir panelas, frigideiras e bandejas quentes do forno para o fogão, balcão ou mesa.</p>',
        'specs': {'Material': 'Têxtil', 'Composição': '100% Algodão', 'Resistência': 'Calor e vapor', 'Modo de Lavagem': 'Máquina de lavar', 'País de Origem': 'China'},
    },
    'luva-para-forno': {
        'desc': '<p>Proteja suas mãos com a Luva para Forno Le Creuset. Feita de 100% algodão, projetada para oferecer proteção máxima contra calor e vapor. Um prático ímã embutido ajudará você a manter a luva sempre ao alcance. Totalmente lavável na máquina de lavar.</p>',
        'specs': {'Material': 'Têxtil', 'Composição': '100% Algodão', 'Resistência': 'Calor e vapor', 'Extras': 'Ímã embutido', 'Modo de Lavagem': 'Máquina de lavar', 'País de Origem': 'China'},
    },
    'avental-chef': {
        'desc': '<p>Proteja-se de pingos e respingos vestindo o icônico Avental Chef Le Creuset. Feito em 100% algodão de lona e totalmente lavável na máquina. Conta com alças de pescoço ajustáveis, bolsos frontais e laterais profundos para guardar utensílios de cozinha, e laço para pendurar panos.</p>',
        'specs': {'Material': 'Têxtil', 'Composição': '100% Algodão de lona', 'Extras': 'Alças ajustáveis, bolsos profundos', 'Modo de Lavagem': 'Máquina de lavar', 'País de Origem': 'China'},
    },
    'avental-jeans': {
        'desc': '<p>Proteja-se de pingos e respingos com o Avental do Chef Jeans Le Creuset. Feito em 100% algodão resistente e lavável na máquina, oferece praticidade e conforto. Ajuste a alça de pescoço para o encaixe perfeito, guarde seus utensílios nos bolsos frontais espaçosos e utilize o laço para segurar o pano de cozinha.</p>',
        'specs': {'Material': 'Têxtil', 'Composição': '100% Algodão Jeans', 'Extras': 'Alça ajustável, bolsos frontais', 'Modo de Lavagem': 'Máquina de lavar', 'País de Origem': 'China'},
    },
    'pegador-jeans': {
        'desc': '<p>Quer seja para mover utensílios de uma boca do fogão para outra ou para levar uma refeição pronta para a mesa, o Pegador Jeans para Cabo Le Creuset foi projetado para proteger as mãos do calor ao mesmo tempo em que oferece uma pegada segura e confortável.</p>',
        'specs': {'Material': 'Têxtil', 'Composição': 'Algodão Jeans', 'Uso': 'Fogão e forno', 'Modo de Lavagem': 'Máquina de lavar'},
    },
    'set-pegadores-silicone': {
        'desc': '<p>O Set Pegadores de Silicone Le Creuset proporcionam uma aderência segura e protegem as mãos enquanto cozinha. Use-os no fogão ou no forno. Disponíveis nas principais cores da linha Le Creuset.</p>',
        'specs': {'Material': 'Silicone', 'Uso': 'Fogão e forno', 'Modo de Lavagem': 'Lava-louças'},
    },
    'pegador-silicone-cabo': {
        'desc': '<p>O Pegador de Silicone para Cabo Le Creuset protege as mãos ao pegar e mover panelas e frigideiras quentes. Fabricado em silicone de alta qualidade, resistente ao calor e ao vapor.</p>',
        'specs': {'Material': 'Silicone', 'Uso': 'Fogão e forno', 'Modo de Lavagem': 'Lava-louças'},
    },
    'espatula-venus': {
        'desc': '<p>A linha Venus representa a nova geração de inovações funcionais na cozinha Le Creuset. Desenvolvida por amantes da gastronomia e chefs, cada utensílio conta com silicone premium e cabo de madeira cuidadosamente elaborado para melhorar a aderência em diversas tarefas culinárias.</p><ul><li>Borda de silicone curva perfeita para tigelas, panelas, cocottes e caçarolas</li><li>Cabo com anéis para melhor controle e conforto</li><li>Lâmina de silicone resistente a até 250°C</li><li>Segura para lava-louças</li></ul>',
        'specs': {'Material': 'Silicone + Madeira', 'Resistência térmica': 'até 250°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'colher-venus': {
        'desc': '<p>A Colher Venus Grande integra a nova geração de utensílios funcionais Le Creuset. Fabricada com silicone premium e cabo de madeira, proporciona melhor aderência em diversas tarefas na cozinha. A borda curva é ideal para tigelas, panelas e cocottes.</p><ul><li>Borda de silicone curva para panelas, cocottes e caçarolas</li><li>Cabo com anéis para melhor controle</li><li>Resistente a até 250°C</li><li>Segura para lava-louças</li></ul>',
        'specs': {'Material': 'Silicone + Madeira', 'Resistência térmica': 'até 250°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'espatula-revolution-duo': {
        'desc': '<p>Os utensílios Revolution® Duo-Material foram concebidos para melhorar até as mais difíceis tarefas de cozinha. A combinação do silicone flexível e nylon rígido reforçado permite que se adaptem às bordas de panelas e frigideiras, mantendo resistência e durabilidade. As alças elípticas patenteadas proporcionam conforto e controle. A borda rígida corta e vira ingredientes; a borda macia de silicone pega com precisão.</p>',
        'specs': {'Material': 'Silicone + Nylon', 'Alça': 'Elíptica patenteada', 'Modo de Lavagem': 'Lava-louças'},
    },
    'colher-revolution-duo': {
        'desc': '<p>Os utensílios Revolution® Duo-Material foram concebidos para melhorar até as mais difíceis tarefas de cozinha. A combinação de silicone flexível e nylon rígido permite adaptar-se às bordas das panelas, mantendo resistência e durabilidade. Borda larga e flexível que limpa ingredientes eficientemente, evitando que grudem.</p>',
        'specs': {'Material': 'Silicone + Nylon', 'Alça': 'Elíptica patenteada', 'Modo de Lavagem': 'Lava-louças'},
    },
    'concha-revolution-duo': {
        'desc': '<p>Os utensílios Revolution® Duo-Material foram concebidos para melhorar até as mais difíceis tarefas de cozinha. A borda maleável da concha se curva para caber nos cantos, facilitando a remoção de líquidos sem ter que inclinar a panela.</p>',
        'specs': {'Material': 'Silicone + Nylon', 'Alça': 'Elíptica patenteada', 'Modo de Lavagem': 'Lava-louças'},
    },
    'colher-macarrao-duo': {
        'desc': '<p>A Colher para Macarrão Duo-Material Le Creuset foi concebida para facilitar o manuseio de macarrão e massas. Combina silicone flexível e nylon rígido para adaptar-se às bordas das panelas com resistência e durabilidade.</p>',
        'specs': {'Material': 'Silicone + Nylon', 'Alça': 'Elíptica patenteada', 'Modo de Lavagem': 'Lava-louças'},
    },
    'espatula-revolution-inox-silicone': {
        'desc': '<p>Funcional e resistente, a Espátula Vazada Revolution combina a durabilidade do aço inox com a flexibilidade do silicone, protegendo superfícies antiaderentes. O design vazado facilita o escorrimento de líquidos ao virar e servir os alimentos.</p>',
        'specs': {'Material': 'Aço Inox + Silicone', 'Modo de Lavagem': 'Lava-louças'},
    },
    'bowl-inox-19cm': {
        'desc': '<p>O Bowl em Aço Inox com Tampa de Vidro 19cm é a escolha ideal para quem busca praticidade e versatilidade na cozinha. Transita com facilidade da preparação ao armazenamento de alimentos. A tampa de vidro temperado permite visualizar o conteúdo e preservar os alimentos.</p>',
        'specs': {'Diâmetro': '19 cm', 'Material': 'Aço Inox + Vidro Temperado', 'Modo de Lavagem': 'Lava-louças'},
    },
    'bowl-inox-23cm': {
        'desc': '<p>O Bowl em Aço Inox com Tampa de Vidro 23cm é a escolha ideal para quem busca praticidade e versatilidade na cozinha. Transita com facilidade da preparação ao armazenamento de alimentos. A tampa de vidro temperado permite visualizar o conteúdo e preservar os alimentos.</p>',
        'specs': {'Diâmetro': '23 cm', 'Material': 'Aço Inox + Vidro Temperado', 'Modo de Lavagem': 'Lava-louças'},
    },
    'bowl-inox-27cm': {
        'desc': '<p>O Bowl em Aço Inox com Tampa de Vidro 27cm é a escolha ideal para quem busca praticidade e versatilidade na cozinha. Transita com facilidade da preparação ao armazenamento de alimentos. A tampa de vidro temperado permite visualizar o conteúdo e preservar os alimentos.</p>',
        'specs': {'Diâmetro': '27 cm', 'Material': 'Aço Inox + Vidro Temperado', 'Modo de Lavagem': 'Lava-louças'},
    },
    'molheira-460ml': {
        'desc': '<p>A Molheira 460ml Le Creuset em cerâmica premium conta com bico largo projetado para servir molhos e caldas sem respingos. O cabo oferece conforto e uma pegada segura. Disponível nas icônicas cores Le Creuset.</p>',
        'specs': {'Capacidade': '460 ml', 'Material': 'Cerâmica', 'Resistência térmica': '-23°C a +260°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'suporte-silicone-french': {
        'desc': '<p>O Suporte Silicone French Le Creuset une a funcionalidade e performance do silicone com os estilos decorativos do ferro fundido, criando uma peça elegante e funcional para a cozinha. Resistente ao calor até 250°C, ideal para apoiar panelas e assadeiras após o cozimento.</p>',
        'specs': {'Material': 'Silicone', 'Resistência térmica': 'até 250°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'suporte-silicone': {
        'desc': '<p>O Suporte de Silicone Le Creuset é resistente ao calor até 250°C, ideal para apoiar panelas, frigideiras e assadeiras quentes após o cozimento. Material de silicone de alta qualidade, seguro para lava-louças.</p>',
        'specs': {'Material': 'Silicone', 'Resistência térmica': 'até 250°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'suporte-silicone-coracao': {
        'desc': '<p>O Suporte de Silicone Coração Le Creuset é o acessório perfeito para apoiar colheres, espátulas e outros utensílios durante o preparo das refeições. Design em coração exclusivo Le Creuset, resistente ao calor até 250°C.</p>',
        'specs': {'Material': 'Silicone', 'Resistência térmica': 'até 250°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'descanso-oval-colher': {
        'desc': '<p>O Descanso Oval para Colher em cerâmica é o herói na cozinha — acomoda utensílios enquanto você cozinha, capturando qualquer gota perdida. Espaçoso o suficiente para utensílios maiores. Excepcionalmente forte e durável, com resistência a temperaturas de -23°C a +260°C. Seguro para lava-louças.</p>',
        'specs': {'Material': 'Cerâmica', 'Resistência térmica': '-23°C a +260°C', 'Modo de Lavagem': 'Lava-louças'},
    },
    'set-tampa-moedores': {
        'desc': '<p>O Set Tampa para Moedores 21cm Le Creuset em silicone é compatível com os moedores de aço inox e cerâmica Le Creuset. Preserva a frescura dos condimentos e facilita o armazenamento.</p>',
        'specs': {'Material': 'Silicone', 'Compatível com': 'Moedores Le Creuset 21cm', 'Modo de Lavagem': 'Lava-louças'},
    },
    'set-3-protetores': {
        'desc': '<p>Resistentes e duráveis, o Set de 3 Protetores de panelas em feltro fornecem uma camada macia e acolchoada entre panelas e frigideiras empilhadas no armazenamento. Projetado para ajudar a evitar lascas e arranhões, o design em estrela se acomoda perfeitamente aos utensílios Le Creuset.</p>',
        'specs': {'Material': 'Feltro', 'Conteúdo': '3 protetores', 'Uso': 'Empilhamento de panelas'},
    },
    'pie-bird': {
        'desc': '<p>O Pie Bird é um acessório de confeitaria tradicional para preparar tortas com recheios úmidos. Posicionado no centro da torta antes de ir ao forno, funciona como uma pequena chaminé, liberando o vapor durante o cozimento para evitar o transbordamento do recheio e garantir uma crosta uniforme e crocante.</p><p>Ideal para tortas doces e salgadas com recheios cremosos ou com muito líquido.</p>',
        'specs': {'Material': 'Cerâmica', 'Uso': 'Tortas e pies', 'Modo de Lavagem': 'Lava-louças'},
    },
}

PRODUCTS = [
    # ── Térmica OTG ───────────────────────────────────────────────────────────
    {
        'slug':'garrafa-hidratacao',
        'name':'Garrafa de Hidratação',
        'sub': 'Aço Inox · 500ml',
        'price':'R$ 319,00',
        'img': img('dwf2749dc7','garrafa_hidratacao_squeeze_vermelho_cerise-5.jpg'),
        'colors':[
            ('Vermelho', img('dwf2749dc7','garrafa_hidratacao_squeeze_vermelho_cerise-5.jpg')),
            ('Marseille',img('dw28dae310','garrafa_hidratacao_squeeze_azul_marseille-6.jpg')),
            ('Laranja',  img('dw1c240449','garrafa_hidratacao_squeeze_laranja_flame-7.jpg')),
        ],
    },
    {
        'slug':'garrafa-termica-otg',
        'name':'Garrafa Térmica OTG',
        'sub': 'Aço Inox · 500ml',
        'price':'R$ 319,00 – R$ 379,00',
        'img': otg('dwa0f63c36','1garrafa-t%C3%A9rmica-1l-otg-laranja.png'),
        'colors':[
            ('Laranja',     otg('dwa0f63c36','1garrafa-t%C3%A9rmica-1l-otg-laranja.png')),
            ('Vermelho',    otg('dw69b90f39','1garrafa-t%C3%A9rmica-1l-otg-vermelho.png')),
            ('Azure',       otg('dw78163f72','1garrafa-t%C3%A9rmica-1l-otg-azureblue.png')),
            ('Bamboo',      otg('dw392332da','1garrafa-t%C3%A9rmica-1l-otg-bamboo.png')),
            ('Matte Black', otg('dwa48d4d14','1garrafa-t%C3%A9rmica-1l-otg-matteblack.png')),
            ('Nectar',      otg('dw1ef07307','1garrafa-t%C3%A9rmica-1l-otg-nectar.png')),
            ('Shell Pink',  otg('dw845c4783','1garrafa-t%C3%A9rmica-1l-otg-shellpink.png')),
        ],
    },
    {
        'slug':'copo-termico-350ml',
        'name':'Copo Térmico 350ml OTG',
        'sub': 'Aço Inox',
        'price':'R$ 289,00',
        'img': otg('dw0d2b265b','caneca-termica%20(2).png'),
        'colors':[
            ('Laranja',     otg('dw0d2b265b','caneca-termica%20(2).png')),
            ('Vermelho',    otg('dw3bd05c90','caneca-t%C3%A9rmica-350ml-otg-vermelho.png')),
            ('Azure',       otg('dwb8764249','caneca-t%C3%A9rmica-350ml-otg-azureblue.png')),
            ('Bamboo',      otg('dw079f61b5','caneca-t%C3%A9rmica-350ml-otg-bamboo.png')),
            ('Matte Black', otg('dw9147573e','caneca-t%C3%A9rmica-350ml-otg-matteblack.png')),
            ('Nectar',      otg('dw984ed6d9','caneca-t%C3%A9rmica-350ml-otg-nectar.png')),
            ('Shell Pink',  otg('dw83ee620a','caneca-t%C3%A9rmica-350ml-otg-shellpink.png')),
        ],
    },
    {
        'slug':'pote-termico-500ml',
        'name':'Pote Térmico 500ml OTG',
        'sub': 'Aço Inox',
        'price':'R$ 309,00',
        'img': otg('dw20e446d7','pote-t%C3%A9rmico-500ml-otg-vermelho.png'),
        'colors':[
            ('Vermelho',    otg('dw20e446d7','pote-t%C3%A9rmico-500ml-otg-vermelho.png')),
            ('Deep Teal',   otg('dw65c63b20','pote-t%C3%A9rmico-500ml-otg-deepteal.png')),
            ('Matte Black', otg('dw12d3fc80','pote-t%C3%A9rmico-500ml-otg-matteblack.png')),
            ('Shell Pink',  otg('dw532716a8','pote-t%C3%A9rmico-500ml-otg-shellpink%20(2).png')),
        ],
    },
    {
        'slug':'lancheira-900ml',
        'name':'Lancheira 900ml OTG',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dw99efbad9','Lancheira-900ml-Otg-vermelha.png'),
        'colors':[
            ('Vermelho',    img('dw99efbad9','Lancheira-900ml-Otg-vermelha.png')),
            ('Deep Teal',   img('dw4658c3ac','Lancheira-900ml-Otg-deepteal.png')),
            ('Matte Black', img('dw5e3a5609','Lancheira-900ml-Otg-black.png')),
        ],
    },
    # ── Luvas & Avental ───────────────────────────────────────────────────────
    {
        'slug':'luva-dupla',
        'name':'Luva Dupla',
        'sub': 'Silicone',
        'price':'R$ 409,00',
        'img': img('dwdc764d6d','luva_dupla_vermelho_cerise.jpg'),
        'colors':[
            ('Vermelho', img('dwdc764d6d','luva_dupla_vermelho_cerise.jpg')),
            ('Onyx',     img('dw807ecb08','luva_dupla_preta.jpg')),
        ],
    },
    {
        'slug':'luva-para-forno',
        'name':'Luva para Forno',
        'sub': 'Silicone',
        'price':'R$ 319,00',
        'img': img('dwc0aa27d6','produto-lecreuset-luva-vermelho.png'),
        'colors':[
            ('Vermelho', img('dwc0aa27d6','produto-lecreuset-luva-vermelho.png')),
            ('Onyx',     img('dw5ffe385b','produto-lecreuset-luva-onyx.png')),
        ],
    },
    {
        'slug':'avental-chef',
        'name':'Avental Chef',
        'sub': 'Algodão',
        'price':'R$ 549,00',
        'img': img('dwf8005aec','avental_chef_vermelho_cerise.jpg'),
        'colors':[
            ('Vermelho', img('dwf8005aec','avental_chef_vermelho_cerise.jpg')),
            ('Onyx',     img('dw807ecb08','avental_chef_preto.jpg')),
        ],
    },
    {
        'slug':'avental-jeans',
        'name':'Avental Jeans do Chef',
        'sub': 'Jeans',
        'price':'R$ 549,00',
        'img': img('dwba3d4786','avental_jeans_le-creuset_1.png'),
        'colors':[],
    },
    {
        'slug':'pegador-jeans',
        'name':'Pegador Jeans para Cabo',
        'sub': 'Jeans',
        'price':'R$ 89,00',
        'img': img('dw456ea039','protetor-cabo-penela-jeans_le-creuset_3.png'),
        'colors':[],
    },
    # ── Pegadores de silicone (consolidados) ──────────────────────────────────
    {
        'slug':'set-pegadores-silicone',
        'name':'Set Pegadores de Silicone',
        'sub': 'Silicone',
        'price':'R$ 219,00',
        'img': img('dw309d5819','produto-lecreuset-utensilio-pegadores-vermelho.png'),
        'colors':[
            ('Vermelho',   img('dw309d5819','produto-lecreuset-utensilio-pegadores-vermelho.png')),
            ('Laranja',    img('dwf8e4e3a6','produto-lecreuset-utensilio-pegadores-laranja.png')),
            ('Nectar',     img('dw87039a69','produto-lecreuset-utensilio-pegadores-nectar.png')),
            ('Meringue',   img('dw9abe5cad','produto-lecreuset-utensilio-pegadores-meringue.png')),
            ('Black Onyx', img('dwc36d4bf5','pegador_silicone_preto_black_onyx_lecreuset_4.jpg')),
            ('Flint',      img('dw510cc4c1','844x660-produto-lecreuset-pegador-lecreuset2.png')),
            ('Marseille',  img('dw48f6f78f','produto-lecreuset-utensilio-pegadores-marseille.png')),
        ],
    },
    {
        'slug':'pegador-silicone-cabo',
        'name':'Pegador de Silicone para Cabo',
        'sub': 'Silicone',
        'price':'R$ 109,00',
        'img': img('dw154830ab','93004616060000.jpg'),
        'colors':[],
    },
    # ── Utensílios Venus ──────────────────────────────────────────────────────
    {
        'slug':'espatula-venus',
        'name':'Espátula Venus',
        'sub': 'Silicone',
        'price':'R$ 159,00 – R$ 209,00',
        'img': img('dw150493e2','espatula_grande_vermelho_cerise_venus_lecreuset.jpg'),
        'colors':[
            ('Vermelho',   img('dw150493e2','espatula_grande_vermelho_cerise_venus_lecreuset.jpg')),
            ('Laranja',    img('dw6dc7ff2c','espatula_grande_laranja_flame_venus_lecreuset_1.jpg')),
            ('Branco',     img('dw3969d495','espatula_grande_branco_white_venus_lecreuset_1.jpg')),
            ('Black Onyx', img('dw067314d8','espatula_grande_preto_black_onyx_venus_lecreuset_1.jpg')),
        ],
    },
    {
        'slug':'colher-venus',
        'name':'Colher Venus Grande',
        'sub': 'Silicone',
        'price':'R$ 209,00',
        'img': img('dwd84312d6','93007603060000.jpg'),
        'colors':[],
    },
    # ── Revolution Aço Inox & Silicone ────────────────────────────────────────
    {
        'slug':'espatula-revolution-duo',
        'name':'Espátula Vazada Revolution® Duo-Material',
        'sub': 'Aço Inox + Silicone',
        'price':'R$ 231,20',
        'img': img('dwc730b9b1','93100100060008.jpg'),
        'colors':[],
    },
    {
        'slug':'colher-revolution-duo',
        'name':'Colher Vazada Revolution® Duo-Material',
        'sub': 'Aço Inox + Silicone',
        'price':'R$ 175,20',
        'img': img('dwc0491049','93100300060008.jpg'),
        'colors':[],
    },
    {
        'slug':'concha-revolution-duo',
        'name':'Concha Revolution® Duo-Material',
        'sub': 'Aço Inox + Silicone',
        'price':'R$ 231,20',
        'img': img('dwf08bdabb','93100400090011.jpg'),
        'colors':[],
    },
    {
        'slug':'colher-macarrao-duo',
        'name':'Colher para Macarrão Duo-Material',
        'sub': 'Aço Inox + Silicone',
        'price':'R$ 167,20',
        'img': img('dw3844e9a1','produto-lecreuset-utensilio-macarrao-vermelho1.png'),
        'colors':[],
    },
    {
        'slug':'espatula-revolution-inox-silicone',
        'name':'Espátula Vazada Revolution Inox + Silicone',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dw11afde64','espatula_vazada_revolution_aco_inox_e_silicone-41007350010100-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'pinca-revolution-inox',
        'name':'Pinça Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 339,00',
        'img': img('dw80f46c97','pinca_revolution_de_aco_inox-98401900000000-img01.jpg'),
        'colors':[],
    },
    {
        'slug':'pegador-massa-revolution',
        'name':'Pegador de Massa Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dw7ed7ea76','pegador_de_massa_revolution_aco_inox-41009000010000-img01.jpg'),
        'colors':[],
    },
    {
        'slug':'colher-revolution-inox',
        'name':'Colher Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dwa5ac9575','colher_revolution_aco_inox-41010000010000-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'peneira-revolution-inox',
        'name':'Peneira Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 489,00',
        'img': img('dwa0512a82','41006150000000.jpg'),
        'colors':[],
    },
    {
        'slug':'batedor-revolution-inox',
        'name':'Batedor Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 329,00',
        'img': img('dw03e71561','batedor_revolution_aco_inox-41026000010000-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'escumadeira-revolution-inox',
        'name':'Escumadeira Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dw9b2b2108','escumadeira_revolution_aco_inox-41005000010000-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'concha-revolution-inox',
        'name':'Concha Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dw19d55861','concha_revolution_aco_inox-41008000010000-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'espatula-revolution-inox',
        'name':'Espátula Vazada Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dwed80bad0','espatula_vazada_revolution_aco_inox-41001000010000-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'amassador-batatas-revolution',
        'name':'Amassador de Batatas Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dw516ea012','amassador_de_batatas_revolution_aco_inox-41002000010000-img1.jpg'),
        'colors':[],
    },
    {
        'slug':'colher-vazada-revolution-inox',
        'name':'Colher Vazada Revolution Aço Inox',
        'sub': 'Aço Inox',
        'price':'R$ 439,00',
        'img': img('dwc82e4186','colher_vazada_revolution_aco_inox-41003000010000-img1.jpg'),
        'colors':[],
    },
    # ── Acessórios de Mesa / Servir ───────────────────────────────────────────
    {
        'slug':'molheira-460ml',
        'name':'Molheira 460ml',
        'sub': 'Cerâmica',
        'price':'R$ 309,00',
        'img': img('dw66740c39','molheira-360-lecreuset-vermelho.jpg'),
        'colors':[
            ('Vermelho', img('dw66740c39','molheira-360-lecreuset-vermelho.jpg')),
        ],
    },
    {
        'slug':'descanso-oval-colher',
        'name':'Descanso Oval para Colher',
        'sub': 'Cerâmica',
        'price':'R$ 199,00',
        'img': img('dwd320efe2','descanso-oval-nuit.png'),
        'colors':[],
    },
    {
        'slug':'suporte-silicone-french',
        'name':'Suporte Silicone French',
        'sub': 'Silicone',
        'price':'R$ 139,00',
        'img': img('dw7c62123a','suporte_silicone_flint_lecreuset11.jpg'),
        'colors':[],
    },
    {
        'slug':'suporte-silicone',
        'name':'Suporte de Silicone',
        'sub': 'Silicone',
        'price':'R$ 139,00',
        'img': img('dwb45a3d7f','42404200990000-suporte-silicone.jpg'),
        'colors':[],
    },
    {
        'slug':'suporte-silicone-coracao',
        'name':'Suporte de Silicone Coração',
        'sub': 'Silicone · Vermelho',
        'price':'R$ 159,00',
        'img': img('dw36a8baf3','844x660-receita-lecreuset-suporte-cora%C3%A7%C3%A3o.png'),
        'colors':[],
    },
    {
        'slug':'set-tampa-moedores',
        'name':'Set Tampa para Moedores 21cm',
        'sub': 'Silicone',
        'price':'R$ 79,00',
        'img': img('dwf311dea5','produto-lecreuset-tampa-set-silicone.png'),
        'colors':[],
    },
    {
        'slug':'set-3-protetores',
        'name':'Set 3 Protetores',
        'sub': 'Silicone',
        'price':'R$ 239,00',
        'img': img('dw646049c0','set-protetor-para-panela%20(1).png'),
        'colors':[],
    },
    # ── Pegadores para panela ─────────────────────────────────────────────────
    {
        'slug':'pegador-signature-dourado',
        'name':'Pegador Signature Dourado',
        'sub': 'Aço Inox',
        'price':'R$ 349,00 – R$ 369,00',
        'img': img('dwce4c6db4','pegador-dourado-sugnature-lecreuset.jpg'),
        'colors':[],
    },
    {
        'slug':'pegador-signature-cobre',
        'name':'Pegador Signature Cobre',
        'sub': 'Aço Inox',
        'price':'R$ 349,00 – R$ 379,00',
        'img': img('dwada5d368','pegador-signature-bronze-lecreuset.jpg'),
        'colors':[],
    },
    {
        'slug':'pegador-inox-signature',
        'name':'Pegador Aço Inox Signature',
        'sub': 'Aço Inox',
        'price':'R$ 349,00 – R$ 379,00',
        'img': img('dw8b4acff4','pegador-inox-signature.png'),
        'colors':[],
    },
    {
        'slug':'pegador-inox-tradition',
        'name':'Pegador Aço Inox Tradition',
        'sub': 'Aço Inox',
        'price':'R$ 349,00',
        'img': img('dwcbae14df','pegador-inox-tradition-50mm.png'),
        'colors':[],
    },
    {
        'slug':'pegador-fenolico-tradition',
        'name':'Pegador Tradition Fenólico',
        'sub': 'Baquelite',
        'price':'R$ 339,00',
        'img': img('dw381edacd','pegador-fenolico-lecreuset.jpg'),
        'colors':[],
    },
    {
        'slug':'pegador-fenolico-signature',
        'name':'Pegador Signature Fenólico',
        'sub': 'Baquelite',
        'price':'R$ 349,00 – R$ 359,00',
        'img': img('dw3dcc0896','pegador-signature-grande-fenolico.jpg'),
        'colors':[],
    },
    # ── Tampa & Outros ────────────────────────────────────────────────────────
    {
        'slug':'tampa-vidro-ensc',
        'name':'Tampa de Vidro ENSC',
        'sub': 'Vidro Temperado',
        'price':'R$ 239,00 – R$ 409,00',
        'img': img('dwa1904ece','96200824000000.jpg'),
        'colors':[],
    },
    {
        'slug':'tela-protetora-frituras',
        'name':'Tela Protetora Para Frituras',
        'sub': 'Aço Inox',
        'price':'R$ 619,00 – R$ 689,00',
        'img': img('dw9d50ef66','tela_protetora_frituras_lecreuset_5.jpg'),
        'colors':[],
    },
    {
        'slug':'bowl-inox-19cm',
        'name':'Bowl Inox com Tampa de Vidro 19cm',
        'sub': 'Aço Inox · 19cm',
        'price':'R$ 399,00',
        'img': img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
        'colors':[],
    },
    {
        'slug':'bowl-inox-23cm',
        'name':'Bowl Inox com Tampa de Vidro 23cm',
        'sub': 'Aço Inox · 23cm',
        'price':'R$ 489,00',
        'img': img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
        'colors':[],
    },
    {
        'slug':'bowl-inox-27cm',
        'name':'Bowl Inox com Tampa de Vidro 27cm',
        'sub': 'Aço Inox · 27cm',
        'price':'R$ 689,00',
        'img': img('dwf8b78720','bowl-inox-tampa-de-vidro.png'),
        'colors':[],
    },
    {
        'slug':'pie-bird',
        'name':'Pie Bird',
        'sub': 'Cerâmica',
        'price':'R$ 99,00',
        'img': img('dw8591622f','71206001400100-pie-bird.jpg'),
        'colors':[],
    },
]

# ── shared nav ────────────────────────────────────────────────────────────────
def get_nav():
    sample = os.path.join(DIR, 'colecao-3ply-aco-inox.html')
    with open(sample, encoding='utf-8') as f:
        html = f.read()
    start = html.index('<div class="top-bar">')
    end   = html.index('</header>') + len('</header>')
    return html[start:end]

NAV = get_nav()

FOOTER_HTML = '''<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Le <span>Creuset</span></a>
        <p>Desde 1925, criando peças excepcionais que transformam o cozinhar em arte.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a><a href="#" class="social-btn">in</a><a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul>
        <li><a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a></li>
        <li><a href="colecao-3ply-aco-inox.html">3-Ply Aço Inox</a></li>
        <li><a href="colecao-formatos-especiais.html">Formatos Especiais</a></li>
        <li><a href="colecao-acessorios.html">Acessórios</a></li>
      </ul></div>
      <div class="footer-col"><h4>Atendimento</h4><ul>
        <li><a href="#">Central de Ajuda</a></li>
        <li><a href="#">Rastrear Pedido</a></li>
        <li><a href="#">Trocas e Devoluções</a></li>
      </ul></div>
      <div class="footer-col"><h4>Empresa</h4><ul>
        <li><a href="#">Sobre Nós</a></li>
        <li><a href="#">Blog</a></li>
      </ul></div>
      <div class="footer-col"><h4>Legal</h4><ul>
        <li><a href="#">Privacidade</a></li>
        <li><a href="#">Termos</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Le Creuset do Brasil. Todos os direitos reservados.</p>
      <div class="payment-icons">
        <span class="payment-icon">VISA</span><span class="payment-icon">MASTER</span>
        <span class="payment-icon">PIX</span><span class="payment-icon">BOLETO</span>
      </div>
    </div>
  </div>
</footer>'''

# ── build card ────────────────────────────────────────────────────────────────
def build_card(p):
    img_id = 'img_' + p['slug'].replace('-', '')
    href = p['slug'] + '.html'
    color_swatches = ''
    if p['colors']:
        swatches = ''
        for i, (cname, curl) in enumerate(p['colors']):
            hx = COLORS_HEX.get(cname, '#ccc')
            border = '1.5px solid #ccc' if hx in ('#F5F0E8','#F5F5F5') else '1.5px solid transparent'
            active = ' active' if i == 0 else ''
            swatches += (f'<span class="swatch{active}" style="background:{hx};border:{border};" '
                         f'onclick="swatchClick(event,this,\'{img_id}\',\'{curl}\')" title="{cname}"></span>')
        color_swatches = f'<div class="card-swatches">{swatches}</div>'

    return f'''    <div class="product-card">
      <a href="{href}">
        <div class="product-card-img">
          <img id="{img_id}" src="{p['img']}" alt="{p['name']}" />
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
      </a>
      <a href="{href}">
        <div class="product-card-name">{p['name']}</div>
        <div class="product-card-sub">{p['sub']}</div>
        <div class="product-card-price">{p['price']}</div>
      </a>
      {color_swatches}
    </div>'''

# ── build product page ────────────────────────────────────────────────────────
def build_product(p):
    img_id = 'mainImgEl'
    first_color = p['colors'][0][0] if p['colors'] else ''
    color_html = ''
    if p['colors']:
        swatches = ''
        for i, (cname, curl) in enumerate(p['colors']):
            hx = COLORS_HEX.get(cname, '#ccc')
            border = '2px solid #ccc' if hx in ('#F5F0E8','#F5F5F5','#F5F5F5') else '2px solid transparent'
            active = ' active' if i == 0 else ''
            swatches += (f'<span class="color-swatch{active}" style="background:{hx};outline:2px solid transparent;" '
                         f'onclick="selectColor(this,\'{cname}\',\'{curl}\')" title="{cname}"></span>')
        color_html = f'''<div class="color-selector">
      <p class="color-label">Selecione Cor: <strong id="colorName">{first_color}</strong></p>
      <div class="color-swatches">{swatches}</div>
    </div>'''
    d = DESCRIPTIONS.get(p['slug'], {})
    desc = d.get('desc', f'<p>{p["name"]} Le Creuset — {p["sub"]}. Qualidade excepcional para sua cozinha.</p>')
    raw_specs = d.get('specs', {'Material': p['sub'], 'Marca': 'Le Creuset'})
    specs_rows = ''.join(f'<tr><td class="sk">{k}:</td><td class="sv">{v}</td></tr>' for k, v in raw_specs.items())
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{p['name']} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
  <style>*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:'Nunito Sans',sans-serif;color:#000;background:#fff;}}
    a{{text-decoration:none;color:inherit;}}
    .top-bar{{background:#1a1a1a;color:#fff;font-size:12px;text-align:center;padding:8px 16px;}}
    header{{background:#fff;border-bottom:1px solid #e5e5e5;position:sticky;top:0;z-index:100;}}
    .header-inner{{max-width:1400px;margin:0 auto;padding:0 24px;display:flex;align-items:center;height:64px;gap:24px;}}
    .logo{{font-size:22px;font-weight:800;letter-spacing:-1px;white-space:nowrap;flex-shrink:0;}}
    .logo span{{color:#c8102e;}}
    nav{{flex:1;}}
    .nav-list{{display:flex;list-style:none;align-items:center;}}
    .nav-list>li{{position:relative;}}
    .nav-list>li>a{{display:block;padding:22px 14px;font-size:13px;font-weight:600;color:#000;white-space:nowrap;border-bottom:2px solid transparent;transition:border-color 0.2s;}}
    .nav-list>li>a:hover{{border-bottom-color:#000;}}
    .nav-list>li.highlight>a{{color:#c8102e;}}
    .nav-list>li.blue>a{{color:#2563ab;}}
    .mega-menu{{display:none;position:fixed;left:0;right:0;top:64px;background:#fff;border-top:2px solid #e5e5e5;box-shadow:0 8px 32px rgba(0,0,0,0.13);z-index:200;padding:28px 0 24px;}}
    .nav-list>li:hover .mega-menu{{display:block;}}
    .mega-inner{{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:170px 150px 170px 170px 170px 140px 220px;gap:0 20px;align-items:start;}}
    .mega-col-title{{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#000;margin-bottom:14px;padding-bottom:6px;border-bottom:1px solid #e5e5e5;}}
    .mega-col a{{display:block;font-size:13px;color:#444;padding:4px 0;}}
    .mega-col a:hover{{color:#c8102e;}}
    .mega-img{{width:100%;object-fit:cover;border-radius:6px;}}
    .header-icons{{display:flex;align-items:center;gap:16px;flex-shrink:0;}}
    .header-icons a{{font-size:12px;font-weight:600;display:flex;flex-direction:column;align-items:center;gap:2px;color:#000;}}
    .header-icons svg{{width:22px;height:22px;}}
    .search-box{{display:flex;align-items:center;border:1px solid #ccc;border-radius:4px;overflow:hidden;height:36px;}}
    .search-box input{{border:none;outline:none;padding:0 12px;font-size:13px;width:180px;font-family:inherit;}}
    .search-box button{{background:#000;border:none;cursor:pointer;padding:0 12px;height:100%;display:flex;align-items:center;}}
    .search-box button svg{{fill:#fff;width:16px;height:16px;}}
    .breadcrumb{{max-width:1400px;margin:0 auto;padding:16px 24px 0;font-size:12px;color:#888;display:flex;gap:5px;align-items:center;}}
    .breadcrumb a{{color:#888;}} .breadcrumb a:hover{{color:#000;text-decoration:underline;}}
    .product-wrap{{max-width:1400px;margin:0 auto;padding:24px 24px 0;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;}}
    .product-img-wrap{{position:sticky;top:80px;}}
    .product-main-img{{width:100%;aspect-ratio:1;border:1px solid #f0f0f0;display:flex;align-items:center;justify-content:center;background:#fafafa;overflow:hidden;}}
    .product-main-img img{{width:100%;height:100%;object-fit:contain;padding:40px;}}
    .product-info{{padding-top:8px;}}
    .product-brand{{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#888;margin-bottom:6px;}}
    .product-name{{font-size:28px;font-weight:800;line-height:1.2;margin-bottom:8px;}}
    .product-sub{{font-size:14px;color:#555;margin-bottom:20px;}}
    .product-price{{font-size:26px;font-weight:800;color:#000;margin-bottom:4px;}}
    .product-installment{{font-size:13px;color:#666;margin-bottom:24px;}}
    .color-selector{{margin-bottom:28px;}}
    .color-label{{font-size:13px;color:#333;margin-bottom:12px;font-weight:600;}}
    .color-label strong{{font-weight:800;}}
    .color-swatches{{display:flex;gap:10px;flex-wrap:wrap;}}
    .color-swatch{{width:32px;height:32px;border-radius:50%;cursor:pointer;display:inline-block;transition:transform 0.15s,box-shadow 0.15s;border:2px solid transparent;}}
    .color-swatch:hover{{transform:scale(1.12);}}
    .color-swatch.active{{box-shadow:0 0 0 2px #fff,0 0 0 4px #000;}}
    .btn-cart{{display:block;width:100%;background:#000;color:#fff;border:none;padding:16px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;margin-bottom:12px;}}
    .btn-cart:hover{{background:#222;}}
    .btn-wishlist{{display:block;width:100%;background:#fff;color:#000;border:2px solid #000;padding:14px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;font-family:inherit;}}
    .desc-specs-wrap{{max-width:1400px;margin:40px auto 0;padding:48px 24px 80px;border-top:1px solid #e5e5e5;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;}}
    .section-title{{font-size:28px;font-weight:300;margin-bottom:20px;letter-spacing:-0.3px;}}
    .desc-text{{font-size:14px;line-height:1.8;color:#333;}}
    .desc-text p{{margin-bottom:12px;}}
    .desc-text ul{{padding-left:18px;}} .desc-text ul li{{margin-bottom:6px;}}
    .specs-table{{width:100%;border-collapse:collapse;}}
    .specs-table tr{{border-bottom:1px solid #e5e5e5;}}
    .specs-table tr:first-child{{border-top:1px solid #e5e5e5;}}
    .specs-table td{{padding:13px 0;font-size:14px;}}
    .specs-table td.sk{{color:#555;width:48%;}}
    .specs-table td.sv{{color:#000;}}
    footer{{background:#111;color:#fff;padding:60px 24px 30px;}}
    .footer-inner{{max-width:1400px;margin:0 auto;}}
    .footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}}
    .footer-brand .logo{{font-size:20px;margin-bottom:16px;display:block;}}
    .footer-brand p{{font-size:13px;color:#aaa;line-height:1.7;max-width:280px;margin-bottom:20px;}}
    .footer-social{{display:flex;gap:12px;}}
    .social-btn{{width:36px;height:36px;border:1px solid #444;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;}}
    .footer-col h4{{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:16px;}}
    .footer-col ul{{list-style:none;}}
    .footer-col ul li{{margin-bottom:10px;}}
    .footer-col ul li a{{font-size:13px;color:#aaa;}}
    .footer-col ul li a:hover{{color:#fff;}}
    .footer-bottom{{border-top:1px solid #333;padding-top:24px;display:flex;justify-content:space-between;align-items:center;}}
    .footer-bottom p{{font-size:12px;color:#666;}}
    .payment-icons{{display:flex;gap:8px;}}
    .payment-icon{{background:#222;border:1px solid #444;border-radius:4px;padding:4px 8px;font-size:10px;font-weight:700;color:#aaa;}}
  </style>
</head>
<body>
{NAV}
<div class="breadcrumb">
  <a href="index.html">Início</a><span>/</span>
  <a href="colecao-acessorios.html">Acessórios</a><span>/</span>
  <span>{p['name']}</span>
</div>
<div class="product-wrap">
  <div class="product-img-wrap">
    <div class="product-main-img">
      <img id="{img_id}" src="{p['img']}" alt="{p['name']}"/>
    </div>
  </div>
  <div class="product-info">
    <div class="product-brand">Le Creuset</div>
    <h1 class="product-name">{p['name']}</h1>
    <div class="product-sub">{p['sub']}</div>
    <div class="product-price">{p['price']}</div>
    <div class="product-installment">ou 10x sem juros</div>
    {color_html}
    <button class="btn-cart">Adicionar ao Carrinho</button>
    <button class="btn-wishlist">&#9825; Lista de Desejos</button>
  </div>
</div>
<div class="desc-specs-wrap">
  <div>
    <h2 class="section-title">Descrição</h2>
    <div class="desc-text">{desc}</div>
  </div>
  <div>
    <h2 class="section-title">Especificações</h2>
    <table class="specs-table"><tbody>{specs_rows}</tbody></table>
  </div>
</div>
{FOOTER_HTML}
<script>
function selectColor(el,name,src){{
  el.parentElement.querySelectorAll('.color-swatch').forEach(x=>x.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('mainImgEl').src=src;
  document.getElementById('colorName').textContent=name;
}}
</script>
</body>
</html>'''

# ── build collection ──────────────────────────────────────────────────────────
def build_collection():
    cards = '\n'.join(build_card(p) for p in PRODUCTS)
    total = len(PRODUCTS)
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Acessórios | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet"/>
  <style>*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:'Nunito Sans',sans-serif;color:#000;background:#fff;}}
    a{{text-decoration:none;color:inherit;}}
    .top-bar{{background:#1a1a1a;color:#fff;font-size:12px;text-align:center;padding:8px 16px;}}
    header{{background:#fff;border-bottom:1px solid #e5e5e5;position:sticky;top:0;z-index:100;}}
    .header-inner{{max-width:1400px;margin:0 auto;padding:0 24px;display:flex;align-items:center;height:64px;gap:24px;}}
    .logo{{font-size:22px;font-weight:800;letter-spacing:-1px;white-space:nowrap;flex-shrink:0;}}
    .logo span{{color:#c8102e;}}
    nav{{flex:1;}}
    .nav-list{{display:flex;list-style:none;align-items:center;}}
    .nav-list>li{{position:relative;}}
    .nav-list>li>a{{display:block;padding:22px 14px;font-size:13px;font-weight:600;color:#000;white-space:nowrap;border-bottom:2px solid transparent;transition:border-color 0.2s;}}
    .nav-list>li>a:hover{{border-bottom-color:#000;}}
    .nav-list>li.highlight>a{{color:#c8102e;}}
    .nav-list>li.blue>a{{color:#2563ab;}}
    .mega-menu{{display:none;position:fixed;left:0;right:0;top:64px;background:#fff;border-top:2px solid #e5e5e5;box-shadow:0 8px 32px rgba(0,0,0,0.13);z-index:200;padding:28px 0 24px;}}
    .nav-list>li:hover .mega-menu{{display:block;}}
    .mega-inner{{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:170px 150px 170px 170px 170px 140px 220px;gap:0 20px;align-items:start;}}
    .mega-col-title{{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:#000;margin-bottom:14px;padding-bottom:6px;border-bottom:1px solid #e5e5e5;}}
    .mega-col a{{display:block;font-size:13px;color:#444;padding:4px 0;}}
    .mega-col a:hover{{color:#c8102e;}}
    .mega-img{{width:100%;object-fit:cover;border-radius:6px;}}
    .header-icons{{display:flex;align-items:center;gap:16px;flex-shrink:0;}}
    .header-icons a{{font-size:12px;font-weight:600;display:flex;flex-direction:column;align-items:center;gap:2px;color:#000;}}
    .header-icons svg{{width:22px;height:22px;}}
    .search-box{{display:flex;align-items:center;border:1px solid #ccc;border-radius:4px;overflow:hidden;height:36px;}}
    .search-box input{{border:none;outline:none;padding:0 12px;font-size:13px;width:180px;font-family:inherit;}}
    .search-box button{{background:#000;border:none;cursor:pointer;padding:0 12px;height:100%;display:flex;align-items:center;}}
    .search-box button svg{{fill:#fff;width:16px;height:16px;}}
    /* banner */
    .cat-banner-wrap{{border-bottom:1px solid #e0e0e0;}}
    .cat-banner{{max-width:1400px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr 1fr;min-height:280px;}}
    .cat-banner-left{{padding:28px 40px 28px 0;display:flex;flex-direction:column;justify-content:center;}}
    .cat-banner-crumb{{font-size:12px;color:#888;display:flex;gap:5px;align-items:center;margin-bottom:14px;flex-wrap:wrap;}}
    .cat-banner-crumb a{{color:#888;}} .cat-banner-crumb a:hover{{color:#000;text-decoration:underline;}}
    .cat-banner-title{{font-size:26px;font-weight:700;color:#000;margin-bottom:12px;}}
    .cat-banner-features{{list-style:disc;padding-left:18px;}}
    .cat-banner-features li{{font-size:13px;color:#333;margin-bottom:4px;line-height:1.55;}}
    .cat-banner-right{{overflow:hidden;max-height:320px;}}
    .cat-banner-right img{{width:100%;height:100%;object-fit:cover;object-position:center 40%;display:block;}}
    /* shop */
    .shop-layout{{max-width:1400px;margin:0 auto;padding:24px 24px 80px;display:grid;grid-template-columns:220px 1fr;gap:40px;align-items:start;}}
    .sidebar{{position:sticky;top:80px;}}
    .filter-section{{border-bottom:1px solid #e5e5e5;}}
    .filter-header{{display:flex;justify-content:space-between;align-items:center;padding:14px 0;cursor:pointer;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;user-select:none;}}
    .filter-header svg{{width:14px;height:14px;transition:transform 0.2s;}}
    .filter-header.open svg{{transform:rotate(180deg);}}
    .filter-body{{padding-bottom:12px;display:none;}}
    .filter-body.open{{display:block;}}
    .filter-option{{display:flex;align-items:center;gap:8px;padding:5px 0;font-size:13px;color:#444;cursor:pointer;}}
    .filter-option input{{width:14px;height:14px;cursor:pointer;accent-color:#000;}}
    .filter-clear{{font-size:11px;font-weight:700;letter-spacing:0.5px;color:#000;text-transform:uppercase;cursor:pointer;border:none;background:none;padding:0;display:flex;align-items:center;gap:4px;}}
    .filter-clear:hover{{text-decoration:underline;}}
    .results-bar{{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;}}
    .results-count{{font-size:13px;color:#888;}}
    .sort-select{{font-size:13px;border:1px solid #ccc;padding:6px 12px;font-family:inherit;cursor:pointer;}}
    /* grid */
    .product-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;}}
    .product-card{{position:relative;}}
    .product-card-img{{position:relative;overflow:hidden;background:#fff;aspect-ratio:1;margin-bottom:10px;border:1px solid #f0f0f0;}}
    .product-card-img img{{width:100%;height:100%;object-fit:contain;padding:16px;transition:transform 0.4s ease;}}
    .product-card-img:hover img{{transform:scale(1.06);}}
    .product-wishlist{{position:absolute;top:8px;right:8px;width:30px;height:30px;background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,0.1);}}
    .product-wishlist svg{{width:15px;height:15px;}}
    .product-card-name{{font-size:13px;font-weight:700;margin-bottom:3px;line-height:1.3;}}
    .product-card-sub{{font-size:11px;color:#888;margin-bottom:5px;}}
    .product-card-price{{font-size:14px;font-weight:800;}}
    .card-swatches{{display:flex;gap:5px;margin-top:7px;flex-wrap:wrap;}}
    .swatch{{width:18px;height:18px;border-radius:50%;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;display:inline-block;}}
    .swatch:hover{{transform:scale(1.15);}}
    .swatch.active{{box-shadow:0 0 0 2px #fff,0 0 0 3.5px #000;}}
    footer{{background:#111;color:#fff;padding:60px 24px 30px;}}
    .footer-inner{{max-width:1400px;margin:0 auto;}}
    .footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px;}}
    .footer-brand .logo{{font-size:20px;margin-bottom:16px;display:block;}}
    .footer-brand p{{font-size:13px;color:#aaa;line-height:1.7;max-width:280px;margin-bottom:20px;}}
    .footer-social{{display:flex;gap:12px;}}
    .social-btn{{width:36px;height:36px;border:1px solid #444;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;}}
    .footer-col h4{{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;margin-bottom:16px;}}
    .footer-col ul{{list-style:none;}}
    .footer-col ul li{{margin-bottom:10px;}}
    .footer-col ul li a{{font-size:13px;color:#aaa;}}
    .footer-col ul li a:hover{{color:#fff;}}
    .footer-bottom{{border-top:1px solid #333;padding-top:24px;display:flex;justify-content:space-between;align-items:center;}}
    .footer-bottom p{{font-size:12px;color:#666;}}
    .payment-icons{{display:flex;gap:8px;}}
    .payment-icon{{background:#222;border:1px solid #444;border-radius:4px;padding:4px 8px;font-size:10px;font-weight:700;color:#aaa;}}
  </style>
</head>
<body>
{NAV}

<div class="cat-banner-wrap">
<div class="cat-banner">
  <div class="cat-banner-left">
    <div class="cat-banner-crumb">
      <a href="index.html">Início</a><span style="color:#ccc;">/</span>
      <a href="#">Cozinhar</a><span style="color:#ccc;">/</span>
      <span style="color:#555;">Acessórios</span>
    </div>
    <h1 class="cat-banner-title">Acessórios</h1>
    <ul class="cat-banner-features">
      <li>Utensílios e acessórios Le Creuset para todas as etapas do preparo;</li>
      <li>Luvas, aventais e pegadores com proteção superior;</li>
      <li>Garrafas e copos térmicos em aço inox de alta qualidade;</li>
      <li>Revolution® Aço Inox: linha completa de utensílios profissionais;</li>
    </ul>
  </div>
  <div class="cat-banner-right">
    <img src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwf2749dc7/images/garrafa_hidratacao_squeeze_vermelho_cerise-5.jpg?sw=1200&sh=600&sm=fit" alt="Acessórios Le Creuset"/>
  </div>
</div>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Categoria
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Térmicos OTG</label>
        <label class="filter-option"><input type="checkbox"> Luvas & Aventais</label>
        <label class="filter-option"><input type="checkbox"> Utensílios Silicone</label>
        <label class="filter-option"><input type="checkbox"> Revolution Aço Inox</label>
        <label class="filter-option"><input type="checkbox"> Acessórios de Mesa</label>
        <label class="filter-option"><input type="checkbox"> Pegadores</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Preço
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Até R$ 100</label>
        <label class="filter-option"><input type="checkbox"> R$ 100 – R$ 300</label>
        <label class="filter-option"><input type="checkbox"> R$ 300 – R$ 500</label>
        <label class="filter-option"><input type="checkbox"> + R$ 500</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Cor
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Vermelho</label>
        <label class="filter-option"><input type="checkbox"> Laranja</label>
        <label class="filter-option"><input type="checkbox"> Nectar</label>
        <label class="filter-option"><input type="checkbox"> Shell Pink</label>
        <label class="filter-option"><input type="checkbox"> Marseille</label>
        <label class="filter-option"><input type="checkbox"> Matte Black</label>
        <label class="filter-option"><input type="checkbox"> Flint</label>
      </div>
    </div>
  </aside>

  <div>
    <div class="results-bar">
      <button class="filter-clear">LIMPAR TODOS OS FILTROS <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="9 18 15 12 9 6"/></svg></button>
      <span class="results-count">{total} produtos</span>
      <select class="sort-select"><option>Mais Populares</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{cards}
    </div>
  </div>
</div>

{FOOTER_HTML}
<script>
function toggleFilter(h){{h.classList.toggle('open');h.nextElementSibling.classList.toggle('open');}}
function swatchClick(e,s,imgId,src){{
  e.preventDefault();e.stopPropagation();
  s.parentElement.querySelectorAll('.swatch').forEach(x=>x.classList.remove('active'));
  s.classList.add('active');
  var el=document.getElementById(imgId);if(el)el.src=src;
}}
</script>
</body>
</html>'''

# ── write ─────────────────────────────────────────────────────────────────────
html = build_collection()
with open(os.path.join(DIR, 'colecao-acessorios.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print('Created: colecao-acessorios.html')

# individual product pages
for p in PRODUCTS:
    page = build_product(p)
    fname = p['slug'] + '.html'
    with open(os.path.join(DIR, fname), 'w', encoding='utf-8') as f:
        f.write(page)
print(f'Created {len(PRODUCTS)} product pages')

# nav update
updated = 0
for fpath in glob.glob(os.path.join(DIR, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    new = content.replace(
        '<a href="#">Acessórios</a>',
        '<a href="colecao-acessorios.html">Acessórios</a>'
    )
    if new != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new)
        updated += 1

print(f'Updated nav in {updated} files')
print('Done!')
