with open('colecao-lancamentos.html', 'r', encoding='utf-8') as f:
    html = f.read()

HEART = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
BADGE = '<div class="product-badge new">NOVO</div>'

def card(nome, sub, preco, parcelas, img):
    return f'''    <div class="product-card">
      <a href="#">
        <div class="product-card-img">
          <img src="{img}" alt="{nome}" />
          {BADGE}
          {HEART}
        </div>
      </a>
      <a href="#">
        <div class="product-card-name">{nome}</div>
        <div class="product-card-sub">{sub}</div>
        <div class="product-card-price">R$ {preco}</div>
        <div class="product-card-sub" style="font-size:11px;color:#888;">{parcelas}</div>
      </a>
    </div>'''

produtos = [
    ("Panela Floral Tradition", "Novo · Ferro Fundido", "2.489,00", "10x R$ 248,90 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw795369d3/images/21934200074460-panela-floral3.jpg?sw=650&sh=650&sm=fit"),
    ("Set 2 Protetores de Silicone Para Tampa", "Novo · Acessórios", "89,00", "1x R$ 89,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw3f5e9969/images/42818110601500-set-2-protetores-vermelho1.jpg?sw=650&sh=650&sm=fit"),
    ("Fecho de Silicone Para Utensílios", "Novo · Acessórios", "89,00", "1x R$ 89,00",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw65d3baa2/images/42416840600000-vermelho-fecho3.jpg?sw=650&sh=650&sm=fit"),
    ("Espátula Pequena de Silicone Signature", "Novo · Utensílios", "159,00", "2x R$ 79,50 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw5b07e83f/images/42074001400000-espatula-pequena.png?sw=650&sh=650&sm=fit"),
    ("Colher de Silicone Signature", "Novo · Utensílios", "199,00", "2x R$ 99,50 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwe2fd90d9/images/42072001400000-colher-de-seilicone.png?sw=650&sh=650&sm=fit"),
    ("Pincel de Silicone Signature", "Novo · Utensílios", "199,00", "2x R$ 99,50 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwb51f556f/images/42071001400000-pincel-de-silicone.png?sw=650&sh=650&sm=fit"),
    ("Espátula Média de Silicone Signature", "Novo · Utensílios", "179,00", "2x R$ 89,50 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw44d99f6b/images/42073001400000-espatula-media.png?sw=650&sh=650&sm=fit"),
    ("Colher Vazada de Madeira Signature", "Novo · Utensílios", "229,00", "3x R$ 76,33 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw9c11af43/images/47411300010004-colher-vazada.jpg?sw=650&sh=650&sm=fit"),
    ("Garfo de Servir de Madeira Signature", "Novo · Utensílios", "229,00", "3x R$ 76,33 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw4bf0be5f/images/47413300010004-garfo-madeira.jpg?sw=650&sh=650&sm=fit"),
    ("Espátula de Madeira Signature", "Novo · Utensílios", "229,00", "3x R$ 76,33 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw2a5bbbc6/images/47412300010004-espatula-madeira.jpg?sw=650&sh=650&sm=fit"),
    ("Colher de Madeira Signature", "Novo · Utensílios", "229,00", "3x R$ 76,33 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dw8defb132/images/47410300010004-colher-madeira.jpg?sw=650&sh=650&sm=fit"),
    ("Travessa Retangular Clássica com Tampa", "Novo · Cerâmica", "1.059,00", "10x R$ 105,90 sem juros",
     "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/dwd20d97eb/images/81001530600005-travessa-retangular.jpg?sw=650&sh=650&sm=fit"),
]

novo_grid = '    <div class="product-grid">\n'
for p in produtos:
    novo_grid += card(*p) + '\n'
novo_grid += '    </div>'

# Find and replace the product grid block
start = html.find('    <div class="product-grid">')
end = html.find('    </div>', start)
end = html.find('    </div>', end + 1)  # get the closing tag of product-grid

# Actually let's find closing </div> after last product-card
# Find the last </div>\n  </div>\n</div> pattern after product-grid start
import re
# Find from product-grid to the next </div> that closes it
grid_start = html.find('    <div class="product-grid">')
# The grid ends with </div>\n    </div> pattern
# Find the position after the last product card's closing </div>
# Search for the pattern that ends the grid
rest = html[grid_start:]
# Find end of grid: it's followed by "  </div>\n</div>\n<footer"
end_marker = '    </div>\n  </div>\n</div>\n<footer'
grid_end_pos = html.find(end_marker)
if grid_end_pos == -1:
    end_marker = '</div>\n  </div>\n</div>\n<footer'
    grid_end_pos = html.find(end_marker)

grid_close = '    </div>'
html = html[:grid_start] + novo_grid + html[grid_end_pos:]

with open('colecao-lancamentos.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('OK')
