import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

# Find all colecao-*.html files
files = sorted(Path('.').glob('colecao-*.html'))

OLD_FONT_IMPORT = "family=Nunito+Sans:wght@300;400;600;700;800&display=swap"
NEW_FONT_IMPORT = "family=Nunito+Sans:wght@300;400;600;700;800&family=Playfair+Display:ital@1&display=swap"

# Old title CSS patterns (with and without mobile variant)
OLD_TITLE_CSS = "font-size: 36px; font-weight: 800; letter-spacing: -0.5px; color: #000;"
NEW_TITLE_CSS = "font-size: 36px; font-family: 'Playfair Display', serif; font-style: italic; font-weight: 400; color: #6080A8; letter-spacing: 0;"

count = 0
for f in files:
    text = f.read_text(encoding='utf-8')
    orig = text

    # 1. Update Google Fonts import
    text = text.replace(OLD_FONT_IMPORT, NEW_FONT_IMPORT)

    # 2. Update all occurrences of the title CSS (covers both desktop and mobile breakpoint)
    text = text.replace(OLD_TITLE_CSS, NEW_TITLE_CSS)

    if text != orig:
        f.write_text(text, encoding='utf-8')
        count += 1
        print(f"  Updated: {f.name}")
    else:
        print(f"  No change: {f.name}")

print(f"\nDone: {count} files updated")
