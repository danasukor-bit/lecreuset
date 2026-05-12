# -*- coding: utf-8 -*-
# Fix: swatches inside <a> tags navigate to product page instead of changing color.
# Solution: pass event to swatchClick and call stopPropagation + preventDefault.
import os, glob, re

DIR = os.path.dirname(os.path.abspath(__file__))

OLD_JS = 'function swatchClick(s,imgId,src){\n  s.parentElement.querySelectorAll(\'.swatch\').forEach(function(x){x.classList.remove(\'active\');});\n  s.classList.add(\'active\');\n  var el=document.getElementById(imgId);if(el)el.src=src;\n}'

NEW_JS = 'function swatchClick(e,s,imgId,src){\n  e.preventDefault();e.stopPropagation();\n  s.parentElement.querySelectorAll(\'.swatch\').forEach(function(x){x.classList.remove(\'active\');});\n  s.classList.add(\'active\');\n  var el=document.getElementById(imgId);if(el)el.src=src;\n}'

# Also fix the longer version used in some files
OLD_JS2 = '''function swatchClick(swatch, imgId, newSrc) {
  var colors = swatch.parentElement;
  var swatches = colors.querySelectorAll('.swatch');
  for (var i = 0; i < swatches.length; i++) {
    swatches[i].classList.remove('active');
  }
  swatch.classList.add('active');
  var img = document.getElementById(imgId);
  if (img) img.src = newSrc;
}'''

NEW_JS2 = '''function swatchClick(e, swatch, imgId, newSrc) {
  e.preventDefault();e.stopPropagation();
  var colors = swatch.parentElement;
  var swatches = colors.querySelectorAll('.swatch');
  for (var i = 0; i < swatches.length; i++) {
    swatches[i].classList.remove('active');
  }
  swatch.classList.add('active');
  var img = document.getElementById(imgId);
  if (img) img.src = newSrc;
}'''

updated = 0
for fpath in glob.glob(os.path.join(DIR, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    new_html = html

    # Fix the JS function definitions
    new_html = new_html.replace(OLD_JS, NEW_JS)
    new_html = new_html.replace(OLD_JS2, NEW_JS2)

    # Fix all onclick="swatchClick(this, ..." -> onclick="swatchClick(event,this, ..."
    # Pattern: swatchClick(this, or swatchClick(this,'
    new_html = re.sub(
        r"onclick=\"swatchClick\(this,",
        'onclick="swatchClick(event,this,',
        new_html
    )
    # Also handle swatch, variant
    new_html = re.sub(
        r"onclick=\"swatchClick\(swatch,",
        'onclick="swatchClick(event,swatch,',
        new_html
    )

    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        updated += 1

print(f'Fixed swatchClick in {updated} files')
