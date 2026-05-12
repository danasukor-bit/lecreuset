with open('colecao-best-sellers.html', 'r', encoding='utf-8') as f:
    html = f.read()

HEART = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
BADGE = '<div class="product-badge star">&#9733; BEST SELLER</div>'

CDN = 'https://www.lecreuset.com.br/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'
CDN2 = 'https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-LeCreuset_BR-Library/default/'

produtos = [
    ("Panela Redonda Signature",      "Ferro Fundido · Mais Vendida",       "1.514,25 – R$ 4.399,00", "panela-redonda-signature.html",
     CDN + "dwbdcd2587/images/BestSeller/produto-lecreuset-panela-redonda-vermelha.png"),

    ("Panela de Arroz Every",          "Ferro Fundido · Berry",              "2.199,00",                "panela-arroz-every.html",
     CDN + "dw08061f78/images/BestSeller/panela-de-arroz-berry.png"),

    ("Caçarola Buffet Signature",      "Ferro Fundido · #1 Mais Vendida",   "2.069,25 – R$ 3.269,00", "cacarola-buffet-signature.html",
     CDN + "dw3dbd40c1/images/BestSeller/lecreuset-ca%C3%A7arola-redonda-azure.png"),

    ("Skillet Redonda Signature",      "Ferro Fundido",                      "1.999,00",                "skillet-redonda-signature.html",
     CDN + "dw697b3830/images/BestSeller/produto-lecreuset-skillet-laranja%20(1).png"),

    ("Moedor de Sal 21cm",             "Acessórios · Cerâmica ABS",          "369,00",                  "moedor-sal-21cm.html",
     CDN + "dw2cc21ce4/images/BestSeller/moedores-azure.png"),

    ("Moedor de Pimenta 21cm",         "Acessórios · Cerâmica ABS",          "369,00",                  "moedor-pimenta-21cm.html",
     CDN + "dwd4c4e94a/images/BestSeller/produto-lecreuset-moedores-laranja.png"),

    ("Set Azeite & Vinagre Clássico",  "Acessórios · 2 peças",               "579,00",                  "set-azeite-vinagre-classico.html",
     CDN + "dwda943317/images/BestSeller/best_sellers-mais_vendidos-galheteiros-kit_azeite_e_vinagre-fundo_brancojpg.jpg"),

    ("Moedor de Pimenta 30cm",         "Acessórios · Cerâmica ABS",          "479,00",                  "moedor-pimenta-30cm.html",
     CDN + "dw57e0437f/images/BestSeller/best_sellers-mais_vendidos-Moedor_30_cm-fundo_branco.png"),

    ("Pote para Mel",                  "Cerâmica Esmaltada",                  "379,00",                  "pote-para-mel.html",
     CDN2 + "dw3be00d82/images/BestSeller/best-seller%20(21).jpg?sw=768&sfrm=png"),

    ("Pote de Manteiga",               "Cerâmica Esmaltada",                  "319,00",                  "pote-de-manteiga.html",
     CDN2 + "dwae261b1b/images/BestSeller/best-seller%20(29).jpg?sw=768&sfrm=png"),

    ("Pote para Biscoito 2,4L",        "Cerâmica Esmaltada",                  "649,00",                  "pote-para-biscoito.html",
     CDN2 + "dwd940b159/images/BestSeller/best-seller%20(41).jpg?sw=768&sfrm=png"),

    ("Pote de Alho",                   "Cerâmica Esmaltada",                  "229,00",                  "pote-de-alho.html",
     CDN2 + "dwaf47ea8d/images/BestSeller/pote-para-alho-vermelho.jpg?sw=768&sfrm=png"),

    ("Travessa Retangular Heritage",   "Cerâmica Esmaltada",                  "689,00",                  "travessa-retangular-heritage.html",
     CDN + "dwad6ebcf0/images/BestSeller/travessas-produto-lecreuset-heritage-marseille.png"),

    ("Mini Cocotte",                   "Cerâmica Esmaltada · 250ml",         "167,30 – R$ 239,00",      "mini-cocotte.html",
     CDN + "dw6db25617/images/BestSeller/mini-cocotte-azure.png"),

    ("Chaleira Clássica",              "Aço Esmaltado · Com Apito",          "899,00 – R$ 1.299,00",    "chaleira-classica.html",
     CDN + "dw13421845/images/BestSeller/chaleira-cotton-classica.png"),
]

def card(nome, sub, preco, href, img):
    return f'''    <div class="product-card">
      <a href="{href}">
        <div class="product-card-img">
          <img src="{img}" alt="{nome}" />
          {BADGE}
          {HEART}
        </div>
      </a>
      <a href="{href}">
        <div class="product-card-name">{nome}</div>
        <div class="product-card-sub">{sub}</div>
        <div class="product-card-price">R$ {preco}</div>
      </a>
    </div>'''

novo_grid = '    <div class="product-grid">\n'
for p in produtos:
    novo_grid += card(*p) + '\n'
novo_grid += '    </div>'

# Replace grid
start = html.find('    <div class="product-grid">')
end_marker = '    </div>\n  </div>\n</div>\n<footer'
end = html.find(end_marker)

html = html[:start] + novo_grid + '\n' + html[end:]

# Update results count
html = html.replace('12 produtos mais vendidos', '15 produtos mais vendidos')

with open('colecao-best-sellers.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done - ' + str(len(produtos)) + ' products')
