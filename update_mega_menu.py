# -*- coding: utf-8 -*-
import os, re, glob

DIR = os.path.dirname(os.path.abspath(__file__))

# ── New mega-menu CSS (replaces old .dropdown CSS) ─────────────────────────
MEGA_CSS = '''.mega-menu { display: none; position: fixed; left: 0; right: 0; top: 64px; background: #fff; border-top: 2px solid #e5e5e5; box-shadow: 0 8px 32px rgba(0,0,0,0.13); z-index: 200; padding: 28px 0 24px; }
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
    .dropdown a:hover { background: #f5f5f5; }'''

# ── New nav HTML ────────────────────────────────────────────────────────────
NEW_NAV = '''<nav>
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
                <a href="#">Bowls</a>
                <a href="#">Pratos</a>
                <a href="#">Canecas e Xícaras</a>
                <a href="#">Bules e Jarras</a>
                <a href="#">Chaleiras</a>
                <a href="#">Travessas</a>
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
                <img class="mega-img" src="https://www.lecreuset.com.br/on/demandware.static/-/Sites-le-creuset-br-storefront/default/dwbcbe171c/images/bleuriviera_swatch.png" alt="Bleu Riviera" style="display:none;" />
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
        <li><a href="#">Cerâmica</a></li>
        <li><a href="#">Nossas Cores</a></li>
        <li><a href="#">Best-Sellers</a></li>
      </ul>
    </nav>'''

# Old CSS to replace
OLD_DROPDOWN_CSS = (
    '.dropdown { display: none; position: absolute; top: 100%; left: 0; background: #fff; '
    'border: 1px solid #e5e5e5; min-width: 200px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); '
    'z-index: 200; padding: 12px 0; }\n'
    '    .nav-list > li:hover .dropdown { display: block; }\n'
    '    .dropdown a { display: block; padding: 8px 20px; font-size: 13px; color: #333; }\n'
    '    .dropdown a:hover { background: #f5f5f5; }'
)

files = glob.glob(os.path.join(DIR, '*.html'))
updated = 0

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # 1) Replace dropdown CSS with mega CSS (if not already done)
    if '.mega-menu' not in html and OLD_DROPDOWN_CSS in html:
        html = html.replace(OLD_DROPDOWN_CSS, MEGA_CSS)
        changed = True

    # 2) Replace nav block
    new_html = re.sub(
        r'<nav>\s*<ul class="nav-list">.*?</ul>\s*</nav>',
        NEW_NAV,
        html,
        flags=re.DOTALL,
        count=1
    )
    if new_html != html:
        html = new_html
        changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

print(f'Updated {updated} files with mega menu')
