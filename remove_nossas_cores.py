import glob, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('*.html')
updated = 0

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'nossas-cores' not in html:
        continue

    original = html

    # Remove nav li item (desktop and mobile nav)
    html = html.replace(
        '<li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>\n',
        ''
    )
    html = html.replace(
        '<li><a href="colecao-nossas-cores.html">Nossas Cores</a></li>',
        ''
    )

    # Remove color swatch links pointing to nossas-cores (each on its own line)
    html = re.sub(
        r'    <a href="colecao-nossas-cores\.html" class="mnav-color"[^\n]+\n',
        '',
        html
    )

    if html != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        updated += 1

print(f'Updated {updated} files')

# Delete the page itself
if os.path.exists('colecao-nossas-cores.html'):
    os.remove('colecao-nossas-cores.html')
    print('Deleted colecao-nossas-cores.html')
