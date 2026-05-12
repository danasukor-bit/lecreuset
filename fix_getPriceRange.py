import glob, re

old = """  function getPriceRange(label) {
    var text = label.textContent || label.innerText || '';
    var nums = text.match(/[\\d.,]+/g);
    if (!nums) return {min:0, max:999999};
    if (text.toLowerCase().indexOf('at') >= 0 && nums.length === 1) {
      return {min:0, max: parsePrice('R$ ' + nums[0])};
    }
    if ((text.toLowerCase().indexOf('mais') >= 0 || text.toLowerCase().indexOf('acima') >= 0 || text.indexOf('+') >= 0) && nums.length === 1) {
      return {min: parsePrice('R$ ' + nums[0]), max: 999999};
    }
    if (nums.length >= 2) {
      return {min: parsePrice('R$ ' + nums[0]), max: parsePrice('R$ ' + nums[1])};
    }
    return {min:0, max:999999};
  }"""

new = """  function getPriceRange(label) {
    // Clone label and remove filter-count span to avoid polluting price parsing
    var clone = label.cloneNode(true);
    var countSpan = clone.querySelector('.filter-count');
    if (countSpan) countSpan.remove();
    var text = clone.textContent || clone.innerText || '';
    var nums = text.match(/[\\d.,]+/g);
    if (!nums) return {min:0, max:999999};
    var lower = text.toLowerCase();
    if (lower.indexOf('mais') >= 0 || lower.indexOf('acima') >= 0 || text.indexOf('+') >= 0) {
      return {min: parsePrice('R$ ' + nums[0]), max: 999999};
    }
    if (lower.indexOf('at') >= 0 && nums.length === 1) {
      return {min:0, max: parsePrice('R$ ' + nums[0])};
    }
    if (nums.length >= 2) {
      return {min: parsePrice('R$ ' + nums[0]), max: parsePrice('R$ ' + nums[1])};
    }
    return {min:0, max:999999};
  }"""

files = glob.glob("colecao-*.html")
fixed = 0
for f in files:
    if f == "colecao-panelas-de-ferro.html":
        continue  # already fixed
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    if old in content:
        content = content.replace(old, new)
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        fixed += 1
        print(f"Fixed: {f}")
    else:
        print(f"Skipped (pattern not found): {f}")

print(f"\nTotal fixed: {fixed}")
