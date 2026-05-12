# -*- coding: utf-8 -*-
import os, glob

DIR  = os.path.dirname(os.path.abspath(__file__))
CDN  = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/'
BANNER = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwec30f170/category/Formatos-Especiais2.png'

COLORS_HEX = {
    'Laranja':    '#d46820',
    'Vermelho':   '#c8102e',
    'Azure':      '#2060A0',
    'Shell Pink': '#F0B8C8',
    'Meringue':   '#F5F0E8',
    'Chambray':   '#8090B0',
    'Azul':       '#1E4D8C',
}

PRODUCTS = [
    {
        'slug': 'panela-para-pao-signature',
        'name': 'Panela Para Pão Signature',
        'sub':  'Ferro Fundido Esmaltado · França',
        'price':'R$ 2.999,00',
        'img':  CDN+'dw2da26e47/images/panela-para-pao-signature-vermelho-lecreuset6.jpg?sw=650&sh=650&sm=fit',
        'colors':[
            ('Laranja', CDN+'dw65d0bbce/images/produto-lecreuset-panela-pao-laranja.png?sw=650&sh=650&sm=fit'),
            ('Vermelho',CDN+'dwa8a8be21/images/produto-lecreuset-panela-pao-vermelho.png?sw=650&sh=650&sm=fit'),
        ],
        'desc':'''<p>A Panela para Pão Signature da Le Creuset é funcional e bonita. Apresenta uma tampa em forma de cúpula que prende e circula o vapor para um excelente sabor final, enquanto sua base assa uma camada uniforme e produz uma crosta dourada e crocante marcada com nossos três anéis escrito Le Creuset.</p>
<p>Com um esmalte interior Matte Black fácil de limpar com alças e pegas ergonómicas, a panela para pão Le Creuset faz com que seja fácil cozinhar em casa.</p>
<p>Fabricado a partir do nosso lendário ferro fundido que mantém uma distribuição superior de calor e um formato especial construída e pensada para produzir resultados de qualidade de padaria.</p>
<p><strong>Destaques:</strong></p>
<ul>
<li>Fabricado a partir do nosso lendário ferro fundido para uma distribuição e retenção excepcionais de calor</li>
<li>A tampa em forma de cúpula é especialmente concebida para reter e circular o vapor para criar uma crosta para elevação máxima e excelente sabor</li>
<li>A base produz uma crosta dourada e crocante marcada com nossos três anéis escrito Le Creuset</li>
<li>O esmalte interior Matte Black é fácil de limpar e manter. Desenvolve uma pátina ao longo do tempo para melhorar o desempenho de cozedura</li>
<li>Resistente a manchas, lascas e fissuras</li>
<li>Pode ser usado na lava-louças (recomenda-se lavagem a mão)</li>
<li>Seguro para forno a 250°C</li>
</ul>''',
        'specs':{'Material':'Ferro Fundido Esmaltado','Origem':'França','Compatibilidade':'Forno, indução, gás, elétrico','Temperatura máx.':'250°C','Limpeza':'À mão ou lava-louças','Garantia':'Vitalícia'},
        'care':'Lavar à mão com água quente e sabão. Compatível com lava-louças, mas recomenda-se lavagem manual para maior durabilidade.',
    },
    {
        'slug': 'panela-arroz-every',
        'name': 'Panela de Arroz Every',
        'sub':  'Ferro Fundido Esmaltado · França · 18cm',
        'price':'R$ 2.519,00',
        'img':  CDN+'dw854d155d/images/produto-lecreuset-panela-arroz-laranja1.png?sw=650&sh=650&sm=fit',
        'colors':[
            ('Laranja',  CDN+'dw854d155d/images/produto-lecreuset-panela-arroz-laranja1.png?sw=650&sh=650&sm=fit'),
            ('Chambray', CDN+'dw615f5a46/images/produto-lecreuset-panela-arroz-chambray.png?sw=650&sh=650&sm=fit'),
        ],
        'desc':'''<p>Faça sempre arroz e grãos perfeitos com a Panela de Arroz Every da Le Creuset. Laterais curvos altos e uma tampa de precisão promovem convecção e circulação de umidade para grãos uniformemente cozidos.</p>
<ul>
<li>Ferro fundido esmaltado oferece distribuição e retenção de calor superior</li>
<li>Pronto para usar, não requer tempero</li>
<li>O esmalte durável e fácil de limpeza resiste a opacidade, manchas, lascas e rachaduras</li>
<li>O esmalte acetinado preto no interior é especialmente formulado para temperaturas de superfície mais altas</li>
<li>Alças ergonômicas são projetadas para facilitar o manuseio</li>
<li>O ferro fundido mais leve por litro do mercado</li>
<li>Compatível com todos os cooktops e forno seguro até 260°C</li>
<li>Seguro para lava-louças e utensílios de metal</li>
<li>Capacidade: até quatro xícaras de arroz cozido</li>
</ul>''',
        'specs':{'Material':'Ferro Fundido Esmaltado','Diâmetro':'18 cm','Capacidade':'4 xícaras de arroz cozido','Compatibilidade':'Todos os fogões, forno até 260°C','Origem':'França','Garantia':'Vitalícia'},
        'care':'Compatível com lava-louças. Lavar à mão recomendado para maior durabilidade do esmalte.',
    },
    {
        'slug': 'fondue-queijo-carne',
        'name': 'Fondue de Queijo & Carne',
        'sub':  'Ferro Fundido Esmaltado · China',
        'price':'R$ 3.189,00',
        'img':  CDN+'dw9debafed/images/fondue-queijo-carne-laranja-lecreuset.jpg?sw=650&sh=650&sm=fit',
        'colors':[
            ('Laranja', CDN+'dw9debafed/images/fondue-queijo-carne-laranja-lecreuset.jpg?sw=650&sh=650&sm=fit'),
        ],
        'desc':'''<p>O fondue de ferro fundido da Le Creuset é feito de material ideal para aquecimento uniforme e acrescenta beleza a qualquer mesa de jantar com um esmalte brilhante e um design distinto e fácil de usar.</p>
<p>O fondue como é conhecido hoje é original das montanhas da Suíça, porém, seu nome é derivado da palavra francesa <em>fondre</em>, que significa derreter.</p>
<ul>
<li>O suporte durável eleva o reservatório acima do queimador</li>
<li>Seis garfos para mergulhar carnes e pães em queijo derretido ou frutas em chocolate</li>
<li>Distribuição de calor uniforme e retenção superior de calor</li>
<li>Esmalte interior durável, não reativo</li>
<li>O esmalte exterior colorido e duradouro resiste a rachaduras e a descascamento</li>
</ul>''',
        'specs':{'Material':'Ferro Fundido Esmaltado','Inclui':'6 garfos + suporte','Origem':'China','Limpeza':'Somente à mão','Garantia':'Vitalícia'},
        'care':'Lavar somente à mão. Não utilizar lava-louças.',
    },
    {
        'slug': 'fondue-gourmand',
        'name': 'Fondue Gourmand',
        'sub':  'Ferro Fundido Esmaltado',
        'price':'R$ 2.959,00',
        'img':  CDN+'dw0f5589db/images/60090000602400.jpg?sw=650&sh=650&sm=fit',
        'colors':[
            ('Laranja', CDN+'dw0f5589db/images/60090000602400.jpg?sw=650&sh=650&sm=fit'),
        ],
        'desc':'<p>Sua construção de ferro permite que a temperatura se mantenha quente por muito tempo. O cabo longo facilita o manuseio, e o kit vem com seis garfos coloridos.</p>',
        'specs':{'Material':'Ferro Fundido Esmaltado','Limpeza':'Somente à mão','Garantia':'Vitalícia'},
        'care':'Lavar somente à mão. Não utilizar lava-louças.',
    },
    {
        'slug': 'tagine-tradition',
        'name': 'Tagine Tradition 27cm',
        'sub':  'Ferro Fundido Esmaltado · 27cm · França',
        'price':'R$ 2.191,20',
        'img':  CDN+'dwc58f4908/images/produto-lecreuset-tagine-vermelho.png?sw=650&sh=650&sm=fit',
        'colors':[
            ('Vermelho', CDN+'dwc58f4908/images/produto-lecreuset-tagine-vermelho.png?sw=650&sh=650&sm=fit'),
        ],
        'desc':'<p>A Tagine Le Creuset é um recipiente para cozinhar tradicionalmente as fortemente temperadas comidas do Norte da África em um cozimento lento. A distinta tampa de cerâmica em forma de cone promove a circulação natural do vapor para manter a carne bovina, cordeiro e outras carnes perfeitamente macias e excepcionalmente saborosas. Especialmente formulado para cozimento em temperaturas de superfície mais altas, o esmalte interior acetinado preto desenvolve uma pátina natural ao longo do tempo que é ideal para queimar no fogão e mantém os alimentos quentes na mesa. A superfície esmaltada colorida minimiza a colagem e manchas, não requer nenhum pré-tempero e é fácil de limpar.</p>',
        'specs':{'Diâmetro':'27 cm','Material':'Ferro Fundido Esmaltado','Porções':'2–3 pessoas','Dimensões':'27×27×21 cm','Compatibilidade':'Fogão e forno','Origem':'França','Garantia':'Vitalícia'},
        'care':'Compatível com lava-louças. Lavar à mão recomendado.',
    },
    {
        'slug': 'crepeira-27cm',
        'name': 'Crepeira 27cm',
        'sub':  'Ferro Fundido Esmaltado · 27cm · França',
        'price':'R$ 1.579,00',
        'img':  CDN+'dwd7d565ac/images/crepeira_27cm_cerise_le_creuset.jpg?sw=650&sh=650&sm=fit',
        'colors':[
            ('Vermelho', CDN+'dwd7d565ac/images/crepeira_27cm_cerise_le_creuset.jpg?sw=650&sh=650&sm=fit'),
        ],
        'desc':'<p>A Crepeira tem formato perfeito para criar crepes e panquecas espetaculares que douram bem e se soltam sem esforço. O ferro fundido também ajuda e garante que o calor seja distribuído de maneira suave e uniforme para que você obtenha grandes resultados na sua receita. Por que parar nos crepes e panquecas? Esta frigideira é brilhante para grelhar, dourar e fritar todos os tipos de alimentos.</p>',
        'specs':{'Diâmetro':'27 cm','Material':'Ferro Fundido Esmaltado','Compatibilidade':'Todos os fogões incluindo indução, forno até 260°C','Origem':'França','Garantia':'Vitalícia'},
        'care':'Compatível com lava-louças. Secar bem após lavagem para evitar oxidação.',
    },
    {
        'slug': 'panela-wok',
        'name': 'Panela Wok 32cm',
        'sub':  'Ferro Fundido · 32cm · França',
        'price':'R$ 2.949,00',
        'img':  CDN+'dw2032c303/images/produto-lecreuset-wok-laranja-vidro.png?sw=650&sh=650&sm=fit',
        'colors':[
            ('Laranja', CDN+'dw2032c303/images/produto-lecreuset-wok-laranja-vidro.png?sw=650&sh=650&sm=fit'),
        ],
        'desc':'''<p>O design asiático clássico da Panela Wok em ferro fundido da Le Creuset apresenta uma superfície de cozimento interior curva, lisa e contínua, ideal para refogar, saltear legumes e carnes grelhadas, e tem um peso perfeitamente equilibrado e uma base plana.</p>
<ul>
<li>Ferro fundido oferece distribuição e retenção de calor superior</li>
<li>Pronto para usar, não requer tempero</li>
<li>O esmalte durável e fácil de limpar resiste a opacidade, manchas, lascas e rachaduras</li>
<li>O esmalte acetinado para interior preto é especialmente formulado para temperaturas de superfície mais altas para melhorar o desempenho de cozimento</li>
<li>A base plana estabiliza a panela no fogão e as alças ergonômicas são projetadas para facilitar o levantamento</li>
<li>A tampa de vidro temperado bem ajustada trava na umidade</li>
<li>O ferro fundido mais leve por litro do mercado</li>
<li>Seguro para lava-louças e utensílios de metal</li>
</ul>''',
        'specs':{'Diâmetro':'32 cm','Porções':'5–6 pessoas','Material':'Ferro Fundido','Compatibilidade':'Cerâmica, indução, elétrico, gás, grelha, forno até 260°C','Tampa de vidro':'Até 220°C','Origem':'França','Garantia':'Vitalícia'},
        'care':'Compatível com lava-louças. Não lavar enquanto quente. Secar imediatamente após lavagem.',
    },
    # accessories – only collection grid, no detail page
    {
        'slug': '#',
        'name': 'Bandeja Coração Sphere Shell Pink',
        'sub':  'Shell Pink',
        'price':'R$ 549,00',
        'img':  CDN+'dw4de44d25/images/80616327770003-bandeja-shellpink1.jpg?sw=650&sh=650&sm=fit',
        'colors':[], 'desc':'', 'specs':{}, 'care':'',
    },
    {
        'slug': '#',
        'name': 'Bandeja Coração Sphere Vermelho',
        'sub':  'Vermelho',
        'price':'R$ 549,00',
        'img':  CDN+'dw1bdbab72/images/80616320600003-bandeja-vermelho.jpg?sw=650&sh=650&sm=fit',
        'colors':[], 'desc':'', 'specs':{}, 'care':'',
    },
    {
        'slug': '#',
        'name': 'Ramekin de Coração',
        'sub':  'Vermelho',
        'price':'R$ 159,00',
        'img':  CDN+'dwa8329dd0/images/ramekin_coracao_vermelho_lecreuset.jpg?sw=650&sh=650&sm=fit',
        'colors':[], 'desc':'', 'specs':{}, 'care':'',
    },
    {
        'slug': '#',
        'name': 'Set Saleiro & Pimenteiro Coração',
        'sub':  'Vermelho',
        'price':'R$ 379,00',
        'img':  CDN+'dw7e22f027/images/kit-saleiro-pimenteiro-vermelho.png?sw=650&sh=650&sm=fit',
        'colors':[], 'desc':'', 'specs':{}, 'care':'',
    },
    {
        'slug': '#',
        'name': 'Descanso Coração Para Colher 13cm',
        'sub':  'Vermelho',
        'price':'R$ 219,00',
        'img':  CDN+'dw4aafc127/images/descanso-cora%C3%A7%C3%A3o-parac-colher-vermelho-1.png?sw=650&sh=650&sm=fit',
        'colors':[], 'desc':'', 'specs':{}, 'care':'',
    },
]

# ── shared nav (read from any existing file) ──────────────────────────────────
def get_nav():
    sample = os.path.join(DIR, 'colecao-3ply-aco-inox.html')
    with open(sample, encoding='utf-8') as f:
        html = f.read()
    start = html.index('<div class="top-bar">')
    end   = html.index('</header>') + len('</header>')
    return html[start:end]

NAV = get_nav()

# ── page shell ────────────────────────────────────────────────────────────────
STYLE_SHARED = '''*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
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
    .header-icons { display: flex; align-items: center; gap: 16px; flex-shrink: 0; }
    .header-icons a { font-size: 12px; font-weight: 600; display: flex; flex-direction: column; align-items: center; gap: 2px; color: #000; }
    .header-icons svg { width: 22px; height: 22px; }
    .search-box { display: flex; align-items: center; border: 1px solid #ccc; border-radius: 4px; overflow: hidden; height: 36px; }
    .search-box input { border: none; outline: none; padding: 0 12px; font-size: 13px; width: 180px; font-family: inherit; }
    .search-box button { background: #000; border: none; cursor: pointer; padding: 0 12px; height: 100%; display: flex; align-items: center; }
    .search-box button svg { fill: #fff; width: 16px; height: 16px; }
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

FOOTER_HTML = '''<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo">Le <span>Creuset</span></a>
        <p>Desde 1925, criando peças excepcionais que transformam o cozinhar em arte. Qualidade francesa para a sua cozinha brasileira.</p>
        <div class="footer-social">
          <a href="#" class="social-btn">f</a><a href="#" class="social-btn">in</a><a href="#" class="social-btn">yt</a>
        </div>
      </div>
      <div class="footer-col"><h4>Produtos</h4><ul>
        <li><a href="colecao-panelas-de-ferro.html">Panelas de Ferro</a></li>
        <li><a href="colecao-frigideiras-e-skillets.html">Frigideiras</a></li>
        <li><a href="colecao-cacarolas.html">Caçarolas</a></li>
        <li><a href="colecao-3ply-aco-inox.html">3-Ply Aço Inox</a></li>
        <li><a href="colecao-formatos-especiais.html">Formatos Especiais</a></li>
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

# ── COLLECTION PAGE ───────────────────────────────────────────────────────────
def build_card(p):
    href = p['slug'] + '.html' if p['slug'] != '#' else '#'
    img_id = 'img_' + p['slug'].replace('-', '')
    color_swatches = ''
    if p['colors']:
        swatches = ''
        for i, (cname, curl) in enumerate(p['colors']):
            hex_color = COLORS_HEX.get(cname, '#ccc')
            border = '1.5px solid #ccc' if hex_color in ('#F5F0E8','#F5F5F5') else '1.5px solid transparent'
            active = ' active' if i == 0 else ''
            swatches += f'<span class="swatch{active}" style="background:{hex_color};border:{border};" onclick="swatchClick(event,this,\'{img_id}\',\'{curl}\')" title="{cname}"></span>'
        color_swatches = f'<div class="card-swatches">{swatches}</div>'
    return f'''<div class="product-card">
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

def build_collection():
    cards = '\n'.join(build_card(p) for p in PRODUCTS)
    total = len(PRODUCTS)
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Formatos Especiais | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>{STYLE_SHARED}
    /* banner */
    .cat-banner-wrap {{ border-bottom: 1px solid #e0e0e0; }}
    .cat-banner {{ max-width: 1400px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: 1fr 1fr; min-height: 320px; }}
    .cat-banner-left {{ padding: 32px 48px 32px 0; display: flex; flex-direction: column; justify-content: center; background: #fff; }}
    .cat-banner-crumb {{ font-size: 12px; color: #888; display: flex; gap: 5px; align-items: center; margin-bottom: 16px; flex-wrap: wrap; }}
    .cat-banner-crumb a {{ color: #888; }} .cat-banner-crumb a:hover {{ color: #000; text-decoration: underline; }}
    .cat-banner-title {{ font-size: 28px; font-weight: 700; color: #000; margin-bottom: 14px; }}
    .cat-banner-features {{ list-style: disc; padding-left: 18px; }}
    .cat-banner-features li {{ font-size: 13px; color: #333; margin-bottom: 5px; line-height: 1.6; }}
    .cat-banner-right {{ overflow: hidden; max-height: 380px; }}
    .cat-banner-right img {{ width: 100%; height: 100%; object-fit: cover; object-position: center 40%; display: block; }}
    /* layout */
    .shop-layout {{ max-width: 1400px; margin: 0 auto; padding: 24px 24px 80px; display: grid; grid-template-columns: 220px 1fr; gap: 40px; align-items: start; }}
    .sidebar {{ position: sticky; top: 80px; }}
    .filter-section {{ border-bottom: 1px solid #e5e5e5; }}
    .filter-header {{ display: flex; justify-content: space-between; align-items: center; padding: 14px 0; cursor: pointer; font-size: 11px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; user-select: none; }}
    .filter-header svg {{ width: 14px; height: 14px; transition: transform 0.2s; }}
    .filter-header.open svg {{ transform: rotate(180deg); }}
    .filter-body {{ padding-bottom: 12px; display: none; }}
    .filter-body.open {{ display: block; }}
    .filter-option {{ display: flex; align-items: center; gap: 8px; padding: 5px 0; font-size: 13px; color: #444; cursor: pointer; }}
    .filter-option input {{ width: 14px; height: 14px; cursor: pointer; accent-color: #000; }}
    .filter-clear {{ font-size: 11px; font-weight: 700; letter-spacing: 0.5px; color: #000; text-transform: uppercase; cursor: pointer; border: none; background: none; padding: 0; display: flex; align-items: center; gap: 4px; }}
    .filter-clear:hover {{ text-decoration: underline; }}
    .results-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }}
    .results-count {{ font-size: 13px; color: #888; }}
    .sort-select {{ font-size: 13px; border: 1px solid #ccc; padding: 6px 12px; font-family: inherit; cursor: pointer; }}
    .product-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }}
    .product-card {{ position: relative; }}
    .product-card-img {{ position: relative; overflow: hidden; background: #fff; aspect-ratio: 1; margin-bottom: 12px; border: 1px solid #f0f0f0; }}
    .product-card-img img {{ width: 100%; height: 100%; object-fit: contain; padding: 20px; transition: transform 0.4s ease; }}
    .product-card-img:hover img {{ transform: scale(1.06); }}
    .product-wishlist {{ position: absolute; top: 10px; right: 10px; width: 32px; height: 32px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }}
    .product-wishlist svg {{ width: 16px; height: 16px; }}
    .product-card-name {{ font-size: 14px; font-weight: 700; margin-bottom: 4px; }}
    .product-card-sub {{ font-size: 12px; color: #888; margin-bottom: 6px; }}
    .product-card-price {{ font-size: 15px; font-weight: 800; }}
    .card-swatches {{ display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap; }}
    .swatch {{ width: 20px; height: 20px; border-radius: 50%; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; display: inline-block; }}
    .swatch:hover {{ transform: scale(1.15); }}
    .swatch.active {{ box-shadow: 0 0 0 2px #fff, 0 0 0 3.5px #000; }}
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
      <span style="color:#555;">Formatos Especiais</span>
    </div>
    <h1 class="cat-banner-title">Formatos Especiais</h1>
    <ul class="cat-banner-features">
      <li>Panelas e utensílios com formatos únicos para cada receita;</li>
      <li>Ferro fundido esmaltado com desempenho excepcional;</li>
      <li>Do pão artesanal ao fondue, do tagine ao wok;</li>
      <li>Design icônico Le Creuset desde 1925;</li>
      <li>*Garantia vitalícia contra defeitos de fabricação;</li>
    </ul>
  </div>
  <div class="cat-banner-right">
    <img src="{BANNER}" alt="Formatos Especiais Le Creuset" />
  </div>
</div>
</div>

<div class="shop-layout">
  <aside class="sidebar">
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Preço
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Até R$ 500</label>
        <label class="filter-option"><input type="checkbox"> R$ 500 – R$ 1.500</label>
        <label class="filter-option"><input type="checkbox"> R$ 1.500 – R$ 3.000</label>
        <label class="filter-option"><input type="checkbox"> + R$ 3.000</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Tipo
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Panelas</label>
        <label class="filter-option"><input type="checkbox"> Fondue</label>
        <label class="filter-option"><input type="checkbox"> Crepeira</label>
        <label class="filter-option"><input type="checkbox"> Tagine</label>
        <label class="filter-option"><input type="checkbox"> Wok</label>
        <label class="filter-option"><input type="checkbox"> Acessórios</label>
      </div>
    </div>
    <div class="filter-section">
      <div class="filter-header open" onclick="toggleFilter(this)">
        Cor
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="filter-body open">
        <label class="filter-option"><input type="checkbox"> Laranja</label>
        <label class="filter-option"><input type="checkbox"> Vermelho</label>
        <label class="filter-option"><input type="checkbox"> Chambray</label>
        <label class="filter-option"><input type="checkbox"> Shell Pink</label>
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

# ── PRODUCT DETAIL PAGE ───────────────────────────────────────────────────────
def build_product(p):
    if not p['desc']:
        return None

    # color picker
    color_picker = ''
    if p['colors']:
        thumbs = ''
        for i,(cname,curl) in enumerate(p['colors']):
            active = ' active' if i==0 else ''
            thumbs += (f'<div class="color-thumb{active}" onclick="selectColor(this,\'{cname}\',\'{curl}\')" title="{cname}">'
                       f'<img src="{curl}" alt="{cname}"/></div>')
        first_color = p['colors'][0][0]
        color_picker = f'''<div class="color-section">
      <div class="color-label">Selecione Cor: <strong id="colorName">{first_color}</strong></div>
      <div class="color-gallery">{thumbs}</div>
    </div>'''

    specs_rows = ''.join(f'<tr><td class="spec-key">{k}</td><td class="spec-val">{v}</td></tr>' for k,v in p['specs'].items())

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['name']} | Le Creuset Brasil</title>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700;800&display=swap" rel="stylesheet" />
  <style>{STYLE_SHARED}
    .breadcrumb {{ max-width: 1400px; margin: 0 auto; padding: 14px 24px; font-size: 12px; color: #888; display: flex; gap: 6px; align-items: center; }}
    .breadcrumb a {{ color: #888; }} .breadcrumb a:hover {{ text-decoration: underline; }} .breadcrumb span {{ color: #bbb; }}
    .product-wrap {{ max-width: 1400px; margin: 0 auto; padding: 0 24px 48px; display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; }}
    .product-tabs-wrap {{ max-width: 1400px; margin: 0 auto; padding: 0 24px 80px; border-top: 1px solid #e5e5e5; }}
    .gallery {{ position: sticky; top: 80px; }}
    .gallery-main {{ width: 100%; aspect-ratio: 1; background: #f9f9f9; display: flex; align-items: center; justify-content: center; overflow: hidden; cursor: zoom-in; border: 1px solid #f0f0f0; }}
    .gallery-main img {{ width: 100%; height: 100%; object-fit: contain; padding: 32px; transition: transform 0.4s ease; }}
    .gallery-main:hover img {{ transform: scale(1.07); }}
    .product-info {{ padding-top: 4px; }}
    .product-title {{ font-size: 26px; font-weight: 800; letter-spacing: -0.5px; line-height: 1.2; margin-bottom: 6px; }}
    .product-subtitle {{ font-size: 14px; color: #666; margin-bottom: 20px; }}
    .price-main {{ font-size: 26px; font-weight: 800; margin-bottom: 4px; }}
    .price-installment {{ font-size: 13px; color: #555; margin-bottom: 4px; }}
    .price-pix {{ font-size: 12px; color: #c8102e; font-weight: 700; margin-bottom: 20px; }}
    .color-section {{ margin-bottom: 20px; }}
    .color-label {{ font-size: 13px; color: #555; margin-bottom: 10px; }}
    .color-label strong {{ color: #000; font-weight: 700; }}
    .color-gallery {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .color-thumb {{ width: 64px; height: 64px; border: 2px solid #e0e0e0; cursor: pointer; overflow: hidden; background: #f8f8f8; flex-shrink: 0; transition: border-color 0.15s; }}
    .color-thumb:hover {{ border-color: #999; }}
    .color-thumb.active {{ border-color: #000; }}
    .color-thumb img {{ width: 100%; height: 100%; object-fit: contain; padding: 6px; display: block; }}
    .qty-row {{ display: flex; align-items: center; gap: 16px; margin-bottom: 16px; }}
    .qty-label {{ font-size: 13px; font-weight: 600; }}
    .qty-control {{ display: flex; align-items: center; border: 1px solid #ccc; }}
    .qty-btn {{ width: 36px; height: 36px; background: none; border: none; cursor: pointer; font-size: 18px; display: flex; align-items: center; justify-content: center; }}
    .qty-btn:hover {{ background: #f5f5f5; }}
    .qty-input {{ width: 48px; height: 36px; border: none; border-left: 1px solid #ccc; border-right: 1px solid #ccc; text-align: center; font-size: 14px; font-family: inherit; outline: none; }}
    .btn-cart {{ width: 100%; background: #000; color: #fff; border: none; padding: 16px; font-size: 14px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; cursor: pointer; font-family: inherit; margin-bottom: 12px; transition: background 0.2s; }}
    .btn-cart:hover {{ background: #222; }}
    .btn-wishlist {{ width: 100%; background: #fff; color: #000; border: 1px solid #000; padding: 14px; font-size: 13px; font-weight: 600; cursor: pointer; font-family: inherit; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 24px; }}
    .btn-wishlist:hover {{ background: #f5f5f5; }}
    .trust-badges {{ display: grid; grid-template-columns: repeat(4,1fr); gap: 12px; border-top: 1px solid #e5e5e5; padding-top: 20px; margin-bottom: 28px; }}
    .trust-item {{ display: flex; flex-direction: column; align-items: center; text-align: center; gap: 6px; }}
    .trust-icon {{ font-size: 20px; }}
    .trust-label {{ font-size: 10px; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; color: #555; line-height: 1.3; }}
    .tab-bar {{ display: flex; border-bottom: 1px solid #e5e5e5; margin-top: 32px; margin-bottom: 28px; }}
    .tab-btn {{ padding: 12px 20px; font-size: 13px; font-weight: 600; cursor: pointer; border: none; background: none; font-family: inherit; border-bottom: 2px solid transparent; color: #888; }}
    .tab-btn.active {{ border-bottom-color: #000; color: #000; }}
    .tab-content {{ display: none; font-size: 14px; color: #444; line-height: 1.7; }}
    .tab-content.active {{ display: block; }}
    .tab-content p {{ margin-bottom: 12px; }}
    .tab-content ul {{ padding-left: 20px; margin-bottom: 12px; }}
    .tab-content ul li {{ margin-bottom: 6px; }}
    .spec-table {{ width: 100%; border-collapse: collapse; }}
    .spec-table td {{ padding: 10px 0; border-bottom: 1px solid #f0f0f0; font-size: 13px; vertical-align: top; }}
    .spec-key {{ font-weight: 700; width: 40%; color: #000; }}
    .spec-val {{ color: #555; }}
  </style>
</head>
<body>
{NAV}
<div class="breadcrumb">
  <a href="index.html">Home</a><span>/</span>
  <a href="colecao-formatos-especiais.html">Formatos Especiais</a><span>/</span>
  <span>{p['name']}</span>
</div>
<div class="product-wrap">
  <div class="gallery">
    <div class="gallery-main">
      <img id="mainImgEl" src="{p['img']}" alt="{p['name']}" />
    </div>
  </div>
  <div class="product-info">
    <h1 class="product-title">{p['name']}</h1>
    <p class="product-subtitle">{p['sub']}</p>
    <div class="price-main">{p['price']}</div>
    <div class="price-installment">ou 10x sem juros</div>
    <div class="price-pix">5% OFF no PIX</div>
    {color_picker}
    <div class="qty-row">
      <span class="qty-label">Quantidade</span>
      <div class="qty-control">
        <button class="qty-btn" onclick="var i=document.getElementById('qi');i.value=Math.max(1,+i.value-1)">&#8722;</button>
        <input class="qty-input" type="number" id="qi" value="1" min="1" />
        <button class="qty-btn" onclick="var i=document.getElementById('qi');i.value=+i.value+1">&#43;</button>
      </div>
    </div>
    <button class="btn-cart">ADICIONAR À SACOLA</button>
    <button class="btn-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5" width="18" height="18"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg> ADICIONAR À LISTA DE DESEJOS</button>
    <div class="trust-badges">
      <div class="trust-item"><div class="trust-icon">🛡️</div><div class="trust-label">Garantia Vitalícia</div></div>
      <div class="trust-item"><div class="trust-icon">🇫🇷</div><div class="trust-label">Fabricado na França</div></div>
      <div class="trust-item"><div class="trust-icon">🚚</div><div class="trust-label">Frete Grátis*</div></div>
      <div class="trust-item"><div class="trust-icon">💳</div><div class="trust-label">10x Sem Juros</div></div>
    </div>
  </div>
</div>
<div class="product-tabs-wrap">
  <div class="tab-bar">
    <button class="tab-btn active" onclick="showTab('desc',this)">Descrição</button>
    <button class="tab-btn" onclick="showTab('specs',this)">Especificações</button>
    <button class="tab-btn" onclick="showTab('care',this)">Cuidados</button>
  </div>
  <div id="desc" class="tab-content active">{p['desc']}</div>
  <div id="specs" class="tab-content"><table class="spec-table">{specs_rows}</table></div>
  <div id="care" class="tab-content"><p>{p['care']}</p></div>
</div>
{FOOTER_HTML}
<script>
function selectColor(el,name,src){{
  el.parentElement.querySelectorAll('.color-thumb').forEach(x=>x.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('mainImgEl').src=src;
  document.getElementById('colorName').textContent=name;
}}
function showTab(id,btn){{
  document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}}
</script>
</body>
</html>'''

# ── WRITE FILES ───────────────────────────────────────────────────────────────
col_html = build_collection()
with open(os.path.join(DIR,'colecao-formatos-especiais.html'),'w',encoding='utf-8') as f:
    f.write(col_html)
print('Created: colecao-formatos-especiais.html')

for p in PRODUCTS:
    if p['slug'] == '#' or not p['desc']:
        continue
    html = build_product(p)
    if html:
        fname = p['slug'] + '.html'
        with open(os.path.join(DIR, fname),'w',encoding='utf-8') as f:
            f.write(html)
        print(f'Created: {fname}')

# ── NAV UPDATE ────────────────────────────────────────────────────────────────
updated = 0
for fpath in glob.glob(os.path.join(DIR,'*.html')):
    with open(fpath,'r',encoding='utf-8') as f:
        html = f.read()
    new_html = html.replace(
        '<a href="#">Formatos Especiais</a>',
        '<a href="colecao-formatos-especiais.html">Formatos Especiais</a>'
    )
    if new_html != html:
        with open(fpath,'w',encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f'Updated nav in {updated} existing files')
print('Done!')
