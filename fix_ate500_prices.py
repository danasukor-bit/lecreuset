import re

filepath = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-ate-500.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed = 0
i = 0
while i < len(lines):
    line = lines[i]
    if '<div class="product-card">' in line and 'data-price-min' not in line:
        # Look ahead for price in next ~15 lines
        price_min = None
        for j in range(i+1, min(i+15, len(lines))):
            # Check for sale price first
            m = re.search(r'product-card-price-sale">R\$\s*([\d.,]+)', lines[j])
            if m:
                price_min = float(m.group(1).replace('.', '').replace(',', '.'))
                break
            # Regular price
            m = re.search(r'product-card-price">R\$\s*([\d.,]+)', lines[j])
            if m:
                price_min = float(m.group(1).replace('.', '').replace(',', '.'))
                break
        if price_min:
            lines[i] = line.replace('<div class="product-card">', f'<div class="product-card" data-price-min="{price_min}">')
            fixed += 1
    i += 1

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Fixed {fixed} cards")
