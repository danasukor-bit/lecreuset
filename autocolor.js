// Auto-select color from URL param ?cor=Bleu+Riviera
(function() {
  var params = new URLSearchParams(window.location.search);
  var cor = params.get('cor');
  if (!cor) return;

  function trySelect() {
    var swatches = document.querySelectorAll('.color-swatch');
    if (!swatches.length) return false;
    var found = false;
    swatches.forEach(function(s) {
      if (s.title.toLowerCase() === cor.toLowerCase()) {
        found = true;
        if (typeof window.selectColor === 'function') {
          // Get image from data-img attribute or extract from onclick
          var src = s.dataset.img;
          if (!src) {
            var oc = s.getAttribute('onclick') || '';
            var m = oc.match(/selectColor\([^,]+,[^,]+,\s*'([^']+)'/);
            if (m) src = m[1];
          }
          window.selectColor(s, s.title, src);
        } else {
          s.click();
        }
      }
    });
    return found;
  }

  // Try immediately (script is at bottom of page, DOM is ready)
  if (!trySelect()) {
    document.addEventListener('DOMContentLoaded', trySelect);
  }
})();
