import glob, re

# CSS to inject/replace for mobile product grid - matching lecreuset.com.br style
NEW_MOBILE_CSS = """
      /* ── MOBILE PRODUCT GRID (lecreuset.com.br style) ── */
      .product-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
      .product-card { background: #fff; border-radius: 6px; overflow: hidden; }
      .product-card-media { aspect-ratio: 1; background: #f5f5f5; border-radius: 6px 6px 0 0; }
      .product-card-media img { padding: 8px; }
      .product-quick-buy { display: none; }
      .product-wishlist { opacity: 1; width: 28px; height: 28px; top: 6px; right: 6px; box-shadow: none; background: rgba(255,255,255,0.85); }
      .product-wishlist svg { width: 14px; height: 14px; }
      .product-info { padding: 8px 8px 10px; }
      .product-name { font-size: 12px; font-weight: 600; line-height: 1.35; margin-bottom: 2px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
      .product-name a { color: #1a1a1a; }
      .product-sizes { font-size: 10px; color: #999; margin-bottom: 4px; }
      .product-price { font-size: 13px; font-weight: 800; }
      .product-price-old { font-size: 10.5px; }
      .product-installment { font-size: 10px; color: #888; margin-top: 1px; }
      .product-colors { margin-top: 6px; gap: 4px; }
      .swatch { width: 16px; height: 16px; }
      .product-badge { font-size: 9px; padding: 2px 6px; top: 6px; left: 6px; border-radius: 2px; }
      .collection-header { padding: 12px 0 14px; flex-wrap: wrap; gap: 8px; }
      .results-count { font-size: 12px; }
      .sort-select { font-size: 12px; padding: 6px 10px; }"""

NEW_480_CSS = """
      /* ── EXTRA SMALL ── */
      .product-grid { grid-template-columns: repeat(2, 1fr); gap: 8px; }
      .product-name { font-size: 11.5px; }
      .product-price { font-size: 12.5px; }
      .product-info { padding: 6px 6px 8px; }
      .swatch { width: 14px; height: 14px; }"""

files = glob.glob(r"C:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-*.html")
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    original = content

    # Find the @media (max-width: 768px) block and replace product grid CSS inside it
    # Strategy: find the 768px media query, then replace the product-grid line and add our comprehensive mobile CSS

    # Remove old mobile product-grid overrides in 768px block
    # Pattern: look for .product-grid inside @media 768px and replace with our new CSS

    # We'll do it by finding the 768px media block start and injecting our CSS after "/* Grid */" or after ".mobile-filter-btn"

    # Approach: replace known patterns
    old_patterns_768 = [
        ".product-grid { grid-template-columns: repeat(2, 1fr); gap: 12px; }",
        ".product-grid { grid-template-columns: repeat(2, 1fr); gap: 14px; }",
        ".product-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }",
    ]

    old_patterns_480 = [
        ".product-grid { grid-template-columns: repeat(2, 1fr); gap: 9px; }",
        ".product-grid { grid-template-columns: repeat(2, 1fr); gap: 8px; }",
        ".product-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }",
    ]

    # For 768px block: find the existing product-grid line and surrounding product card CSS, replace with new block
    # Use regex to find and replace the product grid section in the 768px media query

    # Step 1: Replace the 768px media query's grid-related CSS
    # Find pattern: lines between "/* Grid */" (or .mobile-filter-btn) and "/* Footer */" in 768px block

    # Simpler approach: find existing product-grid in 768px and replace the whole chunk
    pattern_768 = re.compile(
        r'(\.mobile-filter-btn \{ display: flex; \})\s*\n'
        r'\s*/\* Grid \*/\s*\n'
        r'(.*?)(?=\s*/\* Footer \*/|\s*footer\s*\{)',
        re.DOTALL
    )

    match = pattern_768.search(content)
    if match:
        content = content[:match.start()] + match.group(1) + "\n" + NEW_MOBILE_CSS + "\n" + content[match.end():]
    else:
        # Try alternative: just find the grid line in 768px and replace it
        # Find .product-grid after @media (max-width: 768px)
        idx_768 = content.find('@media (max-width: 768px)')
        if idx_768 > -1:
            # Find .product-grid { grid-template-columns: repeat(2 after that
            grid_pattern = re.compile(r'\.product-grid \{ grid-template-columns: repeat\(2, 1fr\); gap: \d+px; \}')
            grid_match = grid_pattern.search(content, idx_768)
            if grid_match:
                # Find the end of the product-related CSS lines after this
                pos = grid_match.end()
                # Consume subsequent product-card related lines
                remaining = content[pos:]
                lines_to_skip = []
                for line in remaining.split('\n'):
                    stripped = line.strip()
                    if stripped.startswith('.product-card') or stripped.startswith('.product-') or stripped.startswith('.swatch') or stripped.startswith('.results') or stripped.startswith('.sort-select'):
                        lines_to_skip.append(line)
                    elif stripped == '':
                        lines_to_skip.append(line)
                    else:
                        break
                skip_len = sum(len(l) + 1 for l in lines_to_skip)
                content = content[:grid_match.start()] + NEW_MOBILE_CSS.strip() + "\n" + content[pos + skip_len:]

    # Step 2: Replace 480px product grid CSS
    idx_480 = content.find('@media (max-width: 480px)')
    if idx_480 > -1:
        grid_pattern_480 = re.compile(r'\.product-grid \{ grid-template-columns: repeat\(2, 1fr\); gap: \d+px; \}')
        grid_match_480 = grid_pattern_480.search(content, idx_480)
        if grid_match_480:
            pos = grid_match_480.end()
            remaining = content[pos:]
            lines_to_skip = []
            for line in remaining.split('\n'):
                stripped = line.strip()
                if stripped.startswith('.product-card') or stripped.startswith('.product-') or stripped.startswith('.swatch'):
                    lines_to_skip.append(line)
                elif stripped == '':
                    lines_to_skip.append(line)
                else:
                    break
            skip_len = sum(len(l) + 1 for l in lines_to_skip)
            content = content[:grid_match_480.start()] + NEW_480_CSS.strip() + "\n" + content[pos + skip_len:]

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f"OK: {f.split(chr(92))[-1]}")
    else:
        print(f"SKIP: {f.split(chr(92))[-1]}")

print(f"\n=== {count} files updated ===")
