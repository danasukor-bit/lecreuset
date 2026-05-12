import re

with open(r'c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ceramica.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1) Fix CSS: remove position:absolute from .product-colors, make it flow below image
old_css = '.product-colors { position: absolute; bottom: 48px; left: 10px; display: flex; gap: 4px; z-index: 2; flex-wrap: wrap; max-width: 90%; }'
new_css = '.product-colors { display: flex; gap: 5px; margin-top: 8px; flex-wrap: wrap; padding: 0 2px; }'
html = html.replace(old_css, new_css)
print('CSS replaced:', old_css in html or new_css in html)

# 2) For each product-card, extract the product-colors div from inside product-card-img
#    and re-insert it AFTER the </div> that closes product-card-img, before the <a> text link.
#
# Pattern for product-card-img block (contains product-colors inside):
#   <div class="product-card-img">
#     ...
#     <div class="product-colors">...</div>   ← inside img div
#     ...
#   </div>
# We want to pull product-colors out to after </div>.

def move_colors_out(html):
    # Match product-card-img blocks that contain product-colors
    # product-card-img ... product-colors ... /product-card-img
    changed = 0

    # Find each product-card-img opening
    pos = 0
    result = []
    while True:
        # Find next product-card-img
        img_start = html.find('<div class="product-card-img">', pos)
        if img_start == -1:
            result.append(html[pos:])
            break
        result.append(html[pos:img_start])

        # Find its closing </div> - need to handle nesting
        depth = 0
        i = img_start
        while i < len(html):
            if html[i:i+4] == '<div':
                depth += 1
                i += 4
            elif html[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    img_end = i + 6  # position after </div>
                    break
                i += 6
            else:
                i += 1
        else:
            result.append(html[img_start:])
            break

        img_block = html[img_start:img_end]

        # Check if this block contains product-colors
        colors_match = re.search(r'\s*(<div class="product-colors">.*?</div>)', img_block, re.DOTALL)
        if colors_match:
            # Remove product-colors from inside the img block
            colors_div = colors_match.group(1)
            img_block_clean = img_block[:colors_match.start()] + img_block[colors_match.end():]
            # Append cleaned img block, then colors div after
            result.append(img_block_clean)
            result.append('\n      ' + colors_div)
            changed += 1
        else:
            result.append(img_block)

        pos = img_end

    print(f'Moved product-colors out of product-card-img: {changed} cards')
    return ''.join(result)

html = move_colors_out(html)

with open(r'c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ceramica.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done')
