import json, re

with open('products.json','r',encoding='utf-8') as f:
    products = json.load(f)

with open('colecao-panelas-de-ferro.html','r',encoding='utf-8') as f:
    src = f.read()

head_start = src.find('<head>') + 6
head_end = src.find('</head>')
head_css = src[head_start:head_end]

header_start = src.find('<header>')
header_end = src.find('</header>') + 9
header = src[header_start:header_end]

footer_start = src.rfind('<footer>')
footer_end = src.rfind('</footer>') + 9
footer = src[footer_start:footer_end]

nav_start = src.rfind('<!-- Mobile overlay -->')
script_end = src.rfind('</script>') + 9
bottom_stuff = src[nav_start:script_end]

prod_js = json.dumps(products, ensure_ascii=False)

page = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
""" + head_css + """
  <title>Busca | Le Creuset Brasil</title>
  <style>
    .busca-wrap { max-width: 1400px; margin: 0 auto; padding: 24px 24px 80px; }
    .busca-header { display: flex; align-items: center; gap: 16px; margin-bottom: 28px; flex-wrap: wrap; }
    .busca-input-wrap { flex: 1; display: flex; align-items: center; border: 1.5px solid #000; border-radius: 4px; overflow: hidden; height: 46px; min-width: 200px; }
    .busca-input-wrap svg.search-ico { width: 18px; height: 18px; flex-shrink: 0; opacity: .4; margin: 0 12px; }
    .busca-input-wrap input { flex: 1; border: none; outline: none; font-size: 15px; font-family: inherit; padding: 0; }
    .busca-clear { background: none; border: none; cursor: pointer; font-size: 20px; padding: 0 12px; color: #999; line-height: 1; }
    .busca-btn { background: #000; border: none; padding: 0 16px; cursor: pointer; height: 100%; display: flex; align-items: center; flex-shrink: 0; }
    .busca-count { font-size: 14px; color: #666; }
    .busca-count strong { color: #c8102e; }
    .busca-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
    .busca-card { position: relative; }
    .busca-card-img { background: #f8f8f8; aspect-ratio: 1; overflow: hidden; margin-bottom: 10px; position: relative; }
    .busca-card-img img { width: 100%; height: 100%; object-fit: contain; padding: 12px; transition: transform .4s; display: block; }
    .busca-card-img:hover img { transform: scale(1.06); }
    .busca-card-name { font-size: 13px; font-weight: 700; margin-bottom: 3px; }
    .busca-card-sub { font-size: 11px; color: #888; margin-bottom: 5px; }
    .busca-card-price { font-size: 14px; font-weight: 800; }
    .busca-card-price-sale { font-size: 14px; font-weight: 800; color: #c8102e; }
    .busca-card-price-orig { font-size: 11px; color: #aaa; text-decoration: line-through; }
    .busca-badge { position: absolute; top: 8px; left: 8px; font-size: 10px; font-weight: 700; padding: 3px 7px; letter-spacing: .5px; }
    .busca-badge.sale { background: #c8102e; color: #fff; }
    .busca-badge.new { background: #2DBECD; color: #fff; }
    .busca-wishlist { position: absolute; top: 8px; right: 8px; width: 30px; height: 30px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 6px rgba(0,0,0,.1); cursor: pointer; }
    .busca-wishlist svg { width: 14px; height: 14px; }
    .busca-empty { text-align: center; padding: 80px 20px; color: #666; }
    .busca-empty h2 { font-size: 22px; margin-bottom: 10px; }
    @media(max-width:900px) { .busca-grid { grid-template-columns: repeat(3,1fr); } }
    @media(max-width:600px) { .busca-grid { grid-template-columns: repeat(2,1fr); gap: 14px; } .busca-wrap { padding: 16px 12px 60px; } }
  </style>
</head>
<body>
""" + header + """

<div class="busca-wrap">
  <div class="busca-header">
    <div class="busca-input-wrap">
      <svg class="search-ico" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65" stroke-linecap="round"/></svg>
      <input type="text" id="buscaInput" placeholder="O que voc&#234; est&#225; procurando?" autocomplete="off" />
      <button class="busca-clear" id="buscaClear" onclick="clearBusca()" style="display:none">&#215;</button>
      <button class="busca-btn" onclick="doSearch()"><svg viewBox="0 0 24 24"><path d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1 0 5.15 5.15a7.5 7.5 0 0 0 10.5 11.5z" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
    </div>
    <div class="busca-count" id="buscaCount"></div>
  </div>
  <div class="busca-grid" id="buscaGrid"></div>
  <div class="busca-empty" id="buscaEmpty" style="display:none">
    <h2>Nenhum resultado encontrado</h2>
    <p>Tente pesquisar por outro termo.</p>
  </div>
</div>

""" + footer + """

""" + bottom_stuff + """

<script>
var PRODUCTS = """ + prod_js + """;

var wishSVG = '<div class="busca-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>';

function normalize(s) {
  return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9 ]/g,' ');
}

function renderCard(p) {
  var isSale = p.badge && p.badge.toLowerCase().indexOf('sale') >= 0;
  var isNew  = p.badge && p.badge.toLowerCase().indexOf('nov') >= 0;
  var badge  = p.badge ? '<div class="busca-badge ' + (isNew?'new':'sale') + '">' + p.badge + '</div>' : '';
  var priceHtml = p.price_orig
    ? '<div class="busca-card-price-orig">' + p.price_orig + '</div><div class="busca-card-price-sale">' + p.price + '</div>'
    : '<div class="busca-card-price">' + p.price + '</div>';
  var href = p.url || '#';
  return '<div class="busca-card">' +
    '<a href="' + href + '"><div class="busca-card-img">' +
    '<img src="' + p.img + '" alt="' + p.name.replace(/"/g,'&quot;') + '" loading="lazy" />' +
    badge + wishSVG + '</div></a>' +
    '<a href="' + href + '"><div class="busca-card-name">' + p.name + '</div>' +
    (p.sub ? '<div class="busca-card-sub">' + p.sub + '</div>' : '') +
    priceHtml + '</a></div>';
}

function search(q) {
  var grid  = document.getElementById('buscaGrid');
  var empty = document.getElementById('buscaEmpty');
  var count = document.getElementById('buscaCount');
  var clear = document.getElementById('buscaClear');
  if (clear) clear.style.display = q ? '' : 'none';
  if (!q) { grid.innerHTML=''; empty.style.display='none'; count.innerHTML=''; return; }
  var terms = normalize(q).split(' ').filter(function(t){ return t.length > 0; });
  var results = PRODUCTS.filter(function(p) {
    var text = normalize(p.name) + ' ' + normalize(p.sub) + ' ' + normalize(p.file||'');
    return terms.every(function(t){ return text.indexOf(t) >= 0; });
  });
  if (results.length) {
    grid.innerHTML = results.map(renderCard).join('');
    empty.style.display = 'none';
    count.innerHTML = '<strong>' + results.length + '</strong> resultado' + (results.length===1?'':'s') + ' para "<em>' + q + '</em>"';
  } else {
    grid.innerHTML = ''; empty.style.display = '';
    count.innerHTML = '';
  }
}

function doSearch() {
  var q = document.getElementById('buscaInput').value.trim();
  if (q) {
    history.pushState({}, '', 'busca.html?q=' + encodeURIComponent(q));
    search(q);
  }
}

function clearBusca() {
  document.getElementById('buscaInput').value = '';
  search('');
  history.pushState({}, '', 'busca.html');
}

var initQ = new URLSearchParams(window.location.search).get('q') || '';
if (initQ) { document.getElementById('buscaInput').value = initQ; search(initQ); }

document.getElementById('buscaInput').addEventListener('input', function(){ search(this.value.trim()); });
document.getElementById('buscaInput').addEventListener('keydown', function(e){ if(e.key==='Enter') doSearch(); });
</script>
</body>
</html>"""

with open('busca.html', 'w', encoding='utf-8') as f:
    f.write(page)

print('busca.html criado com sucesso! Tamanho:', len(page), 'chars')
