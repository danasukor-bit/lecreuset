# -*- coding: utf-8 -*-
import os, glob

DIR = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'

def img(h, f):
    return f'{BASE}{h}/images/{f}?sw=650&sh=650&sm=fit'

# color hex + needs-border
C = {
    'Laranja':      ('#d46820',  False),
    'Vermelho':     ('#c8102e',  False),
    'Bleu Riviera': ('#2DBECD',  False),
    'Azure':        ('#2060A0',  False),
    'Meringue':     ('#F5F0E8',  True),
    'Branco':       ('#F5F5F5',  True),
    'Flint':        ('#9EA5AB',  False),
    'Artichaut':    ('#5A7A3A',  False),
    'Shell Pink':   ('#F0B8C8',  False),
    'Caribe':       ('#00B8D4',  False),
    'Deep Teal':    ('#2B7A6E',  False),
    'Cool Mint':    ('#A8D8C8',  False),
    'Rhone':        ('#8080A0',  False),
    'Camomille':    ('#E8C87A',  False),
}

# ── Product definitions ─────────────────────────────────────────────────────
PRODUCTS = [
    {
        'slug': 'chaleira-classica',
        'name': 'Chaleira Clássica',
        'badge': 'Aço Carbono Esmaltado',
        'subtitle': 'Aço Carbono Esmaltado · 1,6 L',
        'price': 'R$ 650,30 – R$ 1.059,00',
        'installment': 'ou 10x de R$ 105,90 sem juros',
        'origin': 'Tailândia',
        'desc': 'Adicione um toque clássico à sua cozinha com a Chaleira Clássica da Le Creuset. Fabricada em aço carbono esmaltado, ferve a água mais rápido do que chaleiras convencionais. O apito de tom único avisa quando a água atingiu o ponto de ebulição, enquanto as marcações internas indicam os níveis mínimo e máximo de água. A base generosa facilita o contato com a fonte de calor, e a alça resistente ao calor garante manuseio seguro.',
        'features': [
            'Aço carbono esmaltado — ferve a água mais rápido',
            'Apito de tom único avisa quando a água atinge o ponto de ebulição',
            'Marcações internas indicam os níveis mínimo e máximo de água',
            'Base generosa facilita o contato com a fonte de calor',
            'Compatível com todas as fontes de calor, incluindo indução',
            'Alça resistente ao calor e suporte em aço inox para manuseio seguro',
            'Superfície esmaltada de fácil limpeza',
        ],
        'specs': [
            ('Material', 'Aço Carbono Esmaltado'),
            ('Capacidade', '1,6 L'),
            ('Dimensões', '18,4 cm × 18,4 cm × 25,1 cm'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmico, indução, radiante'),
            ('Limpeza', 'Somente à mão'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos contra defeitos de fabricação'),
        ],
        'care': [
            'Lave à mão com água quente e sabão; seque completamente',
            'Não deixe água parada dentro da chaleira quando não estiver em uso',
            'Combine o tamanho da zona de calor do fogão com a base da chaleira',
            'Não use na lava-louças',
        ],
        'colors': [
            ('Laranja',      img('dwc63ba8a3', '92009500090000.jpg')),
            ('Vermelho',     img('dw2b9f3ed7', '92009500060000.jpg')),
            ('Bleu Riviera', img('dwc4ad1a8d', '92009500490000.jpg')),
            ('Meringue',     img('dw6bbc1145', '40104027160000.jpg')),
            ('Artichaut',    img('dw3aee7261', 'chaleira-artichaut-classica.jpg')),
            ('Flint',        img('dw959d7206', 'chaleira-classica-flint.png')),
            ('Shell Pink',   img('dw147b1140', 'chaleira-cl%C3%A1ssica-com-apito-pegador-cora%C3%A7%C3%A3o-shell%20pink.png')),
        ],
    },
    {
        'slug': 'chaleira-demi',
        'name': 'Chaleira Demi',
        'badge': 'Aço Carbono Esmaltado',
        'subtitle': 'Aço Carbono Esmaltado · 1,1 L',
        'price': 'R$ 809,00',
        'installment': 'ou 8x de R$ 101,13 sem juros',
        'origin': 'Tailândia',
        'desc': 'A Chaleira Demi traz estilo vintage à cozinha. Ideal para café coado ou chá, é fabricada em aço carbono esmaltado que possibilita aquecimento rápido. O apito de tom único avisa quando a água ferveu. Com base generosa e capacidade de 1,1 L, conta com alça segura para controle total no momento de servir. Disponível em cores elegantes que combinam com qualquer decoração.',
        'features': [
            'Aço carbono esmaltado — aquecimento rápido da água',
            'Apito de tom único indica quando a água atingiu o ponto de ebulição',
            'Marcações internas indicam os níveis mínimo e máximo de água',
            'Base generosa facilita o contato com a fonte de calor',
            'Compatível com todas as fontes de calor, incluindo indução',
            'Alça resistente ao calor e suporte em aço inox para manuseio seguro',
        ],
        'specs': [
            ('Material', 'Aço Carbono Esmaltado'),
            ('Capacidade', '1,1 L'),
            ('Porções', '6 porções'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmico, indução, radiante'),
            ('Limpeza', 'Somente à mão'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos contra defeitos de fabricação'),
        ],
        'care': [
            'Lave à mão com água morna e sabão; seque completamente',
            'Não deixe água parada dentro da chaleira quando não estiver em uso',
            'Não use na lava-louças',
        ],
        'colors': [
            ('Laranja',    img('dw09b1fd1d', '92000900090000.jpg')),
            ('Vermelho',   img('dwa492553e', 'chaleira_demi_vermelha_lecreuset.jpg')),
            ('Caribe',     img('dw0ecc18c6', '92000900490000.jpg')),
            ('Shell Pink', img('dwfa0385af', 'chaleira-demi-1-1l-shellpink.png')),
        ],
    },
    {
        'slug': 'chaleira-kone',
        'name': 'Chaleira Kone',
        'badge': 'Aço Carbono Esmaltado',
        'subtitle': 'Aço Carbono Esmaltado · 1,6 L',
        'price': 'R$ 839,00',
        'installment': 'ou 10x de R$ 83,90 sem juros',
        'origin': 'Tailândia',
        'desc': 'Nada supera o aroma tentador de chá ou café feito na hora. Eleve o seu ritual diário com a elegante Chaleira Kone da Le Creuset. Com design cônico moderno, fabricada em aço carbono esmaltado para aquecimento rápido, e capacidade de 1,6 L. O apito característico avisa quando a água está pronta.',
        'features': [
            'Design cônico exclusivo — estilo moderno e elegante',
            'Aço carbono esmaltado — ferve a água mais rápido',
            'Apito de tom único avisa quando a água atinge o ponto de ebulição',
            'Marcações internas indicam os níveis mínimo e máximo de água',
            'Base generosa facilita o contato com a fonte de calor',
            'Compatível com todas as fontes de calor, incluindo indução',
            'Alça preta resistente ao calor e suporte em aço inox',
        ],
        'specs': [
            ('Material', 'Aço Carbono Esmaltado'),
            ('Capacidade', '1,6 L'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmico, indução'),
            ('Limpeza', 'Somente à mão'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos contra defeitos de fabricação'),
        ],
        'care': [
            'Lave à mão com água quente e sabão; seque completamente',
            'Não deixe água parada dentro da chaleira quando não estiver em uso',
            'Combine o tamanho da zona de calor do fogão com a base da chaleira',
            'Não use na lava-louças',
        ],
        'colors': [
            ('Laranja',   img('dwb688acb4', 'chaleira-kone-laranja-lecreuset.jpg')),
            ('Deep Teal', img('dw0a9e094d', 'chaleira-kone-deepteal%20(1).png')),
            ('Cool Mint', img('dw0a9e094d', 'chaleira-kone-deepteal%20(1).png')),
            ('Rhone',     img('dw0a9e094d', 'chaleira-kone-deepteal%20(1).png')),
            ('Meringue',  img('dw6bbc1145', '40104027160000.jpg')),
        ],
    },
    {
        'slug': 'chaleira-cloche',
        'name': 'Chaleira Cloche',
        'badge': 'Aço Carbono Esmaltado',
        'subtitle': 'Aço Carbono Esmaltado · 2,1 L',
        'price': 'R$ 1.069,00',
        'installment': 'ou 10x de R$ 106,90 sem juros',
        'origin': 'Tailândia',
        'desc': 'A Chaleira Cloche combina design e funcionalidade com capacidade generosa de 2,1 L. Apresenta alça em aço inox escovado e base larga projetada para aquecimento eficiente e uniforme. O indicador de nível na parte externa mostra a linha máxima de enchimento, e a ventilação integrada permite a liberação segura de vapor.',
        'features': [
            'Capacidade de 2,1 L — ideal para servir várias xícaras de uma vez',
            'Indicador de nível adesivo no exterior mostra a linha máxima de enchimento',
            'Ventilação integrada permite a liberação segura de vapor',
            'Base larga favorece aquecimento eficiente e uniforme',
            'Alça fixa que mantém temperatura fria — conforto e segurança',
            'Compatível com todas as fontes de calor, incluindo indução',
            'Disponível nas cores icônicas Le Creuset',
        ],
        'specs': [
            ('Material', 'Aço Carbono Esmaltado'),
            ('Capacidade', '2,1 L'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmico, indução, radiante'),
            ('Limpeza', 'Somente à mão'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos contra defeitos de fabricação'),
        ],
        'care': [
            'Após aquecer, deixe a chaleira na superfície para liberar o vapor completamente antes de servir',
            'Direcione a ventilação de vapor para longe da alça e do corpo para evitar queimaduras',
            'Lave à mão com água quente e sabão; seque completamente',
            'Não use na lava-louças',
        ],
        'colors': [
            ('Laranja',      img('dw3ef38ffc', '40111010900900-chaleira-cloche.jpg')),
            ('Vermelho',     img('dw6e661e9f', '40109010601000-chaleira-cloche.jpg')),
            ('Bleu Riviera', img('dwdf67a668', '40109010991000-chaleira-cloche.jpg')),
            ('Azure',        img('dw199efa8c', '40111012200900-chaleira-cloche.jpg')),
            ('Meringue',     img('dwffea9650', '40111017160900-chaleira-cloche.jpg')),
        ],
    },
    {
        'slug': 'chaleira-classica-pegador-inox',
        'name': 'Chaleira Clássica Pegador Aço Inox',
        'badge': 'Aço Carbono Esmaltado',
        'subtitle': 'Aço Carbono Esmaltado · Pegador Inox',
        'price': 'R$ 929,00',
        'installment': 'ou 10x de R$ 92,90 sem juros',
        'origin': 'Tailândia',
        'desc': 'Adicione um toque clássico à sua cozinha com a Chaleira Clássica Pegador Aço Inox da Le Creuset. Fabricada em aço carbono esmaltado que possibilita ferver a água mais rápido, com apito de tom único e marcações internas de nível. O elegante pegador em aço inox escovado dá um acabamento moderno e sofisticado a esta chaleira atemporal.',
        'features': [
            'Aço carbono esmaltado — ferve a água mais rápido',
            'Apito de tom único avisa quando a água atinge o ponto de ebulição',
            'Marcações internas indicam os níveis mínimo e máximo de água',
            'Pegador em aço inox escovado — acabamento elegante e moderno',
            'Base generosa facilita o contato com a fonte de calor',
            'Compatível com todas as fontes de calor, incluindo indução',
        ],
        'specs': [
            ('Material', 'Aço Carbono Esmaltado + Pegador Aço Inox'),
            ('Dimensões', '18,4 cm × 18,4 cm × 25,1 cm'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmico, indução, radiante'),
            ('Limpeza', 'Somente à mão'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos contra defeitos de fabricação'),
        ],
        'care': [
            'Lave à mão com água quente e sabão; seque completamente',
            'Não deixe água parada dentro da chaleira quando não estiver em uso',
            'Não use na lava-louças',
        ],
        'colors': [
            ('Flint',     img('dw147839aa', 'chaleira-classica-flint-pegador-inox.png')),
            ('Vermelho',  img('dw2b9f3ed7', '92009500060000.jpg')),
            ('Branco',    img('dw959d7206', 'chaleira-classica-flint.png')),
            ('Camomille', img('dw3aee7261', 'chaleira-artichaut-classica.jpg')),
        ],
    },
    {
        'slug': 'set-chaleira-demi-canecas',
        'name': 'Set Chaleira Demi e 2 Canecas Seattle',
        'badge': 'Set',
        'subtitle': 'Chaleira 1,1 L + 2 Canecas Cerâmica 400ml',
        'price': 'R$ 1.149,00',
        'installment': 'ou 10x de R$ 114,90 sem juros',
        'origin': 'Tailândia',
        'desc': 'O Set Chaleira Demi e 2 Canecas Seattle da Le Creuset é a combinação perfeita para presentear ou para quem quer elevar o ritual do chá e do café. O conjunto inclui uma Chaleira Demi de 1,1 L em aço carbono esmaltado e duas Canecas Seattle de 400 ml em cerâmica premium — tudo combinado nas cores exclusivas Le Creuset.',
        'features': [
            'Chaleira Demi 1,1 L — aço carbono esmaltado para aquecimento rápido',
            'Apito clássico avisa quando a água ferveu',
            'Compatível com todas as fontes de calor, incluindo indução',
            '2 Canecas Seattle 400 ml — cerâmica premium com interior esmaltado',
            'Canecas compatíveis com lava-louças, micro-ondas, forno e freezer',
            'Interior esmaltado das canecas não absorve aromas nem sabores',
            'Set coordenado — chaleira e canecas na mesma cor',
        ],
        'specs': [
            ('Conteúdo', 'Chaleira Demi 1,1 L + 2 Canecas Seattle 400 ml'),
            ('Material Chaleira', 'Aço Carbono Esmaltado'),
            ('Material Canecas', 'Cerâmica Esmaltada Premium'),
            ('Chaleira — Fontes de calor', 'Gás, elétrico, vitrocerâmico, indução'),
            ('Canecas — Compatível com', 'Forno, micro-ondas, freezer, lava-louças'),
            ('Origem', 'Tailândia'),
            ('Garantia', '5 anos (chaleira) / 10 anos (canecas) contra defeitos de fabricação'),
        ],
        'care': [
            'Chaleira: lave à mão; não use na lava-louças',
            'Canecas: podem ser lavadas na lava-louças ou à mão',
            'Não deixe água parada dentro da chaleira quando não estiver em uso',
        ],
        'colors': [
            ('Laranja', img('dwcc27cd7f', 'set-chaleira-demi-%26-2-canecas-seattle-laranja.png')),
        ],
    },
]

# ── Shared fragments ─────────────────────────────────────────────────────────
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
                <a href="colecao-chaleiras.html">Chaleiras de Aço Esmaltado</a>
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
                <a href="colecao-chaleiras.html">Chaleiras</a>
                <a href="colecao-ceramica.html">Travessas</a>
              </div>
              <div class="mega-col">
                <div class="mega-col-title">Coleções</div>
                <a href="#">Flamme Dorée</a>
                <a href="#">Gift Collection</a>
                <a href="#">Churrasco</a>
                <a href="#">Coleção Alpine</a>
                <a href="colecao-cacarolas.html">Modern Heritage</a>
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
                <a href="colecao-bleu-riviera.html" style="display:block; overflow:hidden; border-radius:6px;">
                  <img class="mega-img" src="https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe61a242b/images/21180300994450-cacarola-buffet-bleu.jpg?sw=650&sh=650&sm=fit" alt="Bleu Riviera Le Creuset" />
                </a>
              </div>
            </div>
          </div>
        </li>
        <li class="highlight"><a href="colecao-pascoa.html">Páscoa</a></li>
        <li><a href="colecao-ofertas.html">Ofertas</a></li>
        <li class="blue"><a href="colecao-bleu-riviera.html">Bleu Riviera</a></li>
        <li><a href="colecao-lancamentos.html">Lançamentos</a></li>
        <li><a href="colecao-ferro-fundido.html">Ferro Fundido</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>
        <li><a href="colecao-best-sellers.html">Best-Sellers</a></li>
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
          <a href="#" class="social-btn">f</a><a href="#" class="social-btn">in</a><a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul>
        <li><a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a></li>
        <li><a href="colecao-frigideiras-e-skillets.html">Frigideiras</a></li>
        <li><a href="colecao-cacarolas.html">Caçarolas</a></li>
        <li><a href="colecao-ceramica.html">Cerâmica</a></li>
        <li><a href="colecao-chaleiras.html">Chaleiras</a></li>
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
        <span class="payment-icon">VISA</span><span class="payment-icon">MASTER</span>
        <span class="payment-icon">PIX</span><span class="payment-icon">BOLETO</span>
      </div>
    </div>
  </div>
</footer>'''

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
    .dropdown { display: none; }
    .header-icons { display: flex; align-items: center; gap: 16px; flex-shrink: 0; }
    .header-icons a { font-size: 12px; font-weight: 600; display: flex; flex-direction: column; align-items: center; gap: 2px; color: #000; }
    .header-icons svg { width: 22px; height: 22px; }
    .search-box { display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px; overflow: hidden; height: 36px; }
    .search-box input { border: none; outline: none; padding: 0 12px; font-size: 13px; width: 180px; font-family: inherit; }
    .search-box button { background: #000; border: none; cursor: pointer; padding: 0 12px; height: 100%; display: flex; align-items: center; }
    .search-box button svg { fill: #fff; width: 16px; height: 16px; }
    .cat-banner { width: 100%; height: 240px; overflow: hidden; position: relative; background: #1a1a1a; }
    .cat-banner img { width: 100%; height: 100%; object-fit: cover; object-position: center 40%; display: block; }
    .cat-banner-overlay { position: absolute; inset: 0; background: linear-gradient(to right, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.08) 60%); display: flex; align-items: center; padding: 0 80px; }
    .cat-banner-title { color: #fff; font-size: 40px; font-weight: 800; letter-spacing: -0.5px; }
    .breadcrumb { max-width: 1400px; margin: 0 auto; padding: 14px 24px; font-size: 12px; color: #888; display: flex; gap: 6px; align-items: center; }
    .breadcrumb a { color: #888; } .breadcrumb a:hover { text-decoration: underline; } .breadcrumb span { color: #bbb; }
    .shop-layout { max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; display: grid; grid-template-columns: 220px 1fr; gap: 40px; align-items: start; }
    .sidebar { position: sticky; top: 80px; }
    .sidebar-section { margin-bottom: 28px; }
    .sidebar-title { font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 1px solid #e5e5e5; }
    .sidebar-list { list-style: none; }
    .sidebar-list li { margin-bottom: 8px; }
    .sidebar-list li a { font-size: 13px; color: #444; }
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
    .product-colors { position: absolute; bottom: 48px; left: 10px; display: flex; gap: 4px; z-index: 2; flex-wrap: wrap; max-width: 90%; }
    .swatch { width: 18px; height: 18px; border-radius: 50%; cursor: pointer; border: 1.5px solid rgba(255,255,255,0.8); display: inline-block; transition: transform 0.2s, border-color 0.2s; }
    .swatch:hover, .swatch.active { border-color: #000; transform: scale(1.15); }
    .product-card-name { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
    .product-card-sub { font-size: 12px; color: #888; margin-bottom: 6px; }
    .product-card-price { font-size: 15px; font-weight: 800; }
    .results-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
    .results-count { font-size: 13px; color: #888; }
    .sort-select { font-size: 13px; border: 1px solid #ccc; padding: 6px 12px; font-family: inherit; cursor: pointer; }
    footer { background: #111; color: #fff; padding: 60px 24px 30px; }
    .footer-inner { max-width: 1400px; margin: 0 auto; }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
    .footer-brand .logo { font-size: 20px; margin-bottom: 16px; display: block; }
    .footer-brand p { font-size: 13px; color: #aaa; line-height: 1.7; max-width: 280px; margin-bottom: 20px; }
    .footer-social { display: flex; gap: 12px; }
    .social-btn { width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; }
    .footer-col h4 { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; margin-bottom: 16px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul li a { font-size: 13px; color: #aaa; transition: color 0.2s; }
    .footer-col ul li a:hover { color: #fff; }
    .footer-bottom { border-top: 1px solid #333; padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
    .footer-bottom p { font-size: 12px; color: #666; }
    .payment-icons { display: flex; gap: 8px; }
    .payment-icon { background: #222; border: 1px solid #444; border-radius: 4px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #aaa; }'''

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
    .dropdown { display: none; }
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
    .color-swatch { width: 32px; height: 32px; border-radius: 50%; cursor: pointer; border: 2.5px solid transparent; outline: 2px solid transparent; outline-offset: 2px; transition: transform 0.2s, border-color 0.2s, outline-color 0.2s; }
    .color-swatch:hover { transform: scale(1.12); }
    .color-swatch.active { border-color: #000; outline-color: #000; }
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
    .social-btn { width: 36px; height: 36px; border: 1px solid #444; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; }
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
function toggleTab(h){var b=h.nextElementSibling;h.classList.toggle('open');b.classList.toggle('open');}
function selectColor(el,name,src){
  document.querySelectorAll('.color-swatch').forEach(function(s){s.classList.remove('active');});
  el.classList.add('active');
  document.getElementById('colorName').textContent=name;
  document.getElementById('mainImgEl').src=src;
}
function changeQty(d){var i=document.getElementById('qtyInput');i.value=Math.max(1,parseInt(i.value)+d);}
</script>'''

COL_JS = '''<script>
function swatchClick(s,imgId,src){
  s.parentElement.querySelectorAll('.swatch').forEach(function(x){x.classList.remove('active');});
  s.classList.add('active');
  var el=document.getElementById(imgId);if(el)el.src=src;
}
</script>'''

SVG_CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>'

# ── Build product page ───────────────────────────────────────────────────────
def build_product(p):
    first_name, first_src = p['colors'][0]

    swatches = ''
    for i, (cname, csrc) in enumerate(p['colors']):
        bg, border = C.get(cname, ('#ccc', False))
        border_style = ' border:1px solid #ccc;' if border else ''
        active = ' active' if i == 0 else ''
        swatches += f'\n        <div class="color-swatch{active}" style="background:{bg};{border_style}" title="{cname}" onclick="selectColor(this,\'{cname}\',\'{csrc}\')"></div>'

    specs_html = ''.join(
        f'\n        <div class="spec-row"><span class="spec-key">{k}</span><span class="spec-val">{v}</span></div>'
        for k, v in p['specs']
    )
    feat_html = ''.join(f'\n        <li>{f}</li>' for f in p['features'])
    care_html = ''.join(f'\n        <li>{c}</li>' for c in p['care'])

    return f'''<!DOCTYPE html>
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
  <a href="colecao-chaleiras.html">Chaleiras</a><span>/</span>
  <span>{p["name"]}</span>
</div>

<div class="product-wrap">
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImgEl" src="{first_src}" alt="{p["name"]}" />
    </div>
  </div>
  <div class="product-info">
    <div class="product-badges-top"><span class="badge-pill">{p["badge"]}</span></div>
    <h1 class="product-title">{p["name"]}</h1>
    <p class="product-subtitle">{p["subtitle"]}</p>
    <div class="product-price-block">
      <div class="price-range">{p["price"]}</div>
      <div class="price-installment">{p["installment"]}</div>
      <div class="price-pix">5% OFF no PIX</div>
    </div>
    <div class="color-picker">
      <div class="color-picker-label">Cor: <span id="colorName">{first_name}</span></div>
      <div class="color-swatches">{swatches}
      </div>
    </div>
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
      <div class="trust-badge-text">5 Anos de Garantia</div>
      <div class="trust-badge-sub">Contra defeitos de fabricação</div>
    </div>
    <div class="trust-badge">
      <div class="trust-badge-icon"><svg viewBox="0 0 64 64" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="28" r="18"/><path d="M20 52 C20 44 44 44 44 52"/><path d="M26 22 L32 16 L38 22 M32 16 L32 36"/></svg></div>
      <div class="trust-badge-text">Fabricado na {p["origin"]}</div>
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
    <div class="tab-header open" onclick="toggleTab(this)">Descrição {SVG_CHEV}</div>
    <div class="tab-body open">
      <p>{p["desc"]}</p>
      <ul>{feat_html}
      </ul>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">Especificações Técnicas {SVG_CHEV}</div>
    <div class="tab-body">
      <div class="specs-grid"><div>{specs_html}
      </div></div>
    </div>
  </div>
  <div class="tab">
    <div class="tab-header" onclick="toggleTab(this)">Uso e Cuidado {SVG_CHEV}</div>
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

# ── Build collection page ────────────────────────────────────────────────────
def build_collection():
    cards = ''
    for i, p in enumerate(PRODUCTS):
        pid = f'ch{i+1}'
        first_src = p['colors'][0][1]

        # swatches for card
        spans = ''
        for j, (cname, csrc) in enumerate(p['colors']):
            bg, border = C.get(cname, ('#ccc', False))
            bstyle = ' border:1px solid #ccc;' if border else ''
            active = ' active' if j == 0 else ''
            spans += f'\n            <span class="swatch{active}" style="background:{bg};{bstyle}" title="{cname}" onclick="swatchClick(this,\'{pid}\',\'{csrc}\')"></span>'

        cards += f'''    <div class="product-card">
      <a href="{p['slug']}.html">
        <div class="product-card-img">
          <img id="{pid}" src="{first_src}" alt="{p['name']}" />
          <div class="product-colors">{spans}
          </div>
          <div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        </div>
      </a>
      <a href="{p['slug']}.html">
        <div class="product-card-name">{p['name']}</div>
        <div class="product-card-sub">{p['subtitle']}</div>
        <div class="product-card-price">{p['price']}</div>
      </a>
    </div>\n'''

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Chaleiras | Le Creuset Brasil</title>
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
  <img src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dw14f2b808/category/cat_banners/categoria-site-chaleira.png" alt="Chaleiras Le Creuset" />
  <div class="cat-banner-overlay">
    <h1 class="cat-banner-title">Chaleiras de Aço Esmaltado</h1>
  </div>
</div>

<div class="breadcrumb">
  <a href="index.html">Home</a><span>/</span>
  <a href="#">Cozinhar</a><span>/</span>
  <span>Chaleiras</span>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="sidebar-section">
      <div class="sidebar-title">Categorias</div>
      <ul class="sidebar-list">
        <li><a href="#">Chaleira Clássica</a></li>
        <li><a href="#">Chaleira Demi</a></li>
        <li><a href="#">Chaleira Kone</a></li>
        <li><a href="#">Chaleira Cloche</a></li>
        <li><a href="#">Sets</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Capacidade</div>
      <ul class="sidebar-list">
        <li><a href="#">1,1 L</a></li>
        <li><a href="#">1,6 L</a></li>
        <li><a href="#">2,1 L</a></li>
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
        <div class="sidebar-dot" style="background:#9EA5AB;" title="Flint"></div>
        <div class="sidebar-dot" style="background:#5A7A3A;" title="Artichaut"></div>
        <div class="sidebar-dot" style="background:#F0B8C8;" title="Shell Pink"></div>
        <div class="sidebar-dot" style="background:#00B8D4;" title="Caribe"></div>
        <div class="sidebar-dot" style="background:#2B7A6E;" title="Deep Teal"></div>
      </div>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">Preço</div>
      <ul class="sidebar-list">
        <li><a href="#">R$ 500 – R$ 700</a></li>
        <li><a href="#">R$ 700 – R$ 900</a></li>
        <li><a href="#">Acima de R$ 900</a></li>
      </ul>
    </div>
  </aside>
  <div>
    <div class="results-bar">
      <span class="results-count">{len(PRODUCTS)} produtos</span>
      <select class="sort-select"><option>Mais Relevante</option><option>Menor Preço</option><option>Maior Preço</option></select>
    </div>
    <div class="product-grid">
{cards}    </div>
  </div>
</div>

{FOOTER}
{COL_JS}
</body>
</html>'''

# ── Write files ──────────────────────────────────────────────────────────────
with open(os.path.join(DIR, 'colecao-chaleiras.html'), 'w', encoding='utf-8') as f:
    f.write(build_collection())
print('Created: colecao-chaleiras.html')

for p in PRODUCTS:
    path = os.path.join(DIR, f'{p["slug"]}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build_product(p))
    print(f'Created: {p["slug"]}.html')

# ── Update nav in all existing HTML files ────────────────────────────────────
updated = 0
new_files = {'colecao-chaleiras.html'} | {p['slug']+'.html' for p in PRODUCTS}
for fpath in glob.glob(os.path.join(DIR, '*.html')):
    if os.path.basename(fpath) in new_files:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    new_html = html.replace(
        '<a href="#">Chaleiras de Aço Esmaltado</a>',
        '<a href="colecao-chaleiras.html">Chaleiras de Aço Esmaltado</a>'
    ).replace(
        '<a href="#">Chaleiras</a>\n                <a href="colecao-ceramica.html">Travessas</a>',
        '<a href="colecao-chaleiras.html">Chaleiras</a>\n                <a href="colecao-ceramica.html">Travessas</a>'
    )
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f'Updated nav in {updated} existing files')
print('Done!')
