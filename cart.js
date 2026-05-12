// Le Creuset Cart System
(function(){
  var CART_KEY = 'lc_cart';

  function getCart() {
    try { return JSON.parse(localStorage.getItem(CART_KEY)) || []; }
    catch(e) { return []; }
  }
  function saveCart(c) { localStorage.setItem(CART_KEY, JSON.stringify(c)); }

  function totalQty(cart) {
    return cart.reduce(function(a,b){ return a+(b.qty||1); }, 0);
  }

  function parsePriceNum(str) {
    if(!str) return 0;
    // Handles "R$ 3.819,00" and ranges "R$ 1.514,25 – R$ 4.399,00" (takes first price)
    var m = str.match(/\d[\d.]*,\d{2}/);
    if(!m) return 0;
    return parseFloat(m[0].replace(/\./g,'').replace(',','.')) || 0;
  }

  function formatBRL(val) {
    return 'R$ ' + val.toFixed(2).replace('.',',').replace(/\B(?=(\d{3})+(?!\d))/g,'.');
  }

  function updateBadge() {
    var cart = getCart();
    var count = totalQty(cart);
    var text = count > 0 ? 'Sacola (' + count + ')' : 'Sacola';
    document.querySelectorAll('.header-icons a span, .bottom-nav-item span').forEach(function(el){
      if(/^Sacola/.test(el.textContent.trim())) el.textContent = text;
    });
  }

  // ── Modal ──────────────────────────────────────────────
  var MODAL_ID = 'lcCartModal';

  function injectModalStyles() {
    if(document.getElementById('lcCartModalStyles')) return;
    var s = document.createElement('style');
    s.id = 'lcCartModalStyles';
    s.textContent = [
      '#lcCartModalOverlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.45);z-index:10000;align-items:flex-start;justify-content:center;padding-top:60px;}',
      '#lcCartModalOverlay.open{display:flex;}',
      '#lcCartModal{background:#fff;width:90%;max-width:420px;border-radius:6px;box-shadow:0 8px 40px rgba(0,0,0,0.22);overflow:hidden;font-family:inherit;position:relative;animation:lcSlideIn 0.25s ease;}',
      '@keyframes lcSlideIn{from{opacity:0;transform:translateY(-18px);}to{opacity:1;transform:translateY(0);}}',
      '#lcCartModal .lc-modal-header{display:flex;align-items:center;justify-content:space-between;padding:18px 20px 14px;border-bottom:1px solid #e8e8e8;}',
      '#lcCartModal .lc-modal-title{font-size:15px;font-weight:700;color:#000;}',
      '#lcCartModal .lc-modal-close{background:none;border:none;cursor:pointer;font-size:22px;line-height:1;color:#666;padding:0;}',
      '#lcCartModal .lc-modal-body{display:flex;gap:16px;padding:18px 20px;}',
      '#lcCartModal .lc-modal-img{width:110px;height:110px;flex-shrink:0;object-fit:contain;}',
      '#lcCartModal .lc-modal-info{flex:1;min-width:0;}',
      '#lcCartModal .lc-modal-name{font-size:15px;font-weight:700;color:#000;margin-bottom:6px;line-height:1.3;}',
      '#lcCartModal .lc-modal-meta{font-size:13px;color:#444;margin-bottom:2px;}',
      '#lcCartModal .lc-modal-meta span{font-weight:600;color:#000;}',
      '#lcCartModal .lc-modal-subtotal{border-top:1px solid #e8e8e8;padding:14px 20px;text-align:center;font-size:14px;color:#444;}',
      '#lcCartModal .lc-modal-subtotal strong{font-size:16px;font-weight:700;color:#000;}',
      '#lcCartModal .lc-modal-actions{padding:0 20px 20px;display:flex;flex-direction:column;gap:10px;}',
      '#lcCartModal .lc-btn-cart-go{display:block;width:100%;background:#3d3d3d;color:#fff;border:none;padding:14px;font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;text-align:center;text-decoration:none;cursor:pointer;border-radius:2px;}',
      '#lcCartModal .lc-btn-cart-go:hover{background:#555;}',
      '#lcCartModal .lc-btn-checkout{display:flex;align-items:center;justify-content:center;gap:6px;font-size:13px;font-weight:600;color:#444;text-decoration:none;padding:6px 0;}',
      '#lcCartModal .lc-btn-checkout:hover{color:#000;}',
    ].join('');
    document.head.appendChild(s);
  }

  function buildModal() {
    if(document.getElementById('lcCartModalOverlay')) return;
    var overlay = document.createElement('div');
    overlay.id = 'lcCartModalOverlay';
    overlay.innerHTML = '<div id="'+MODAL_ID+'">'
      + '<div class="lc-modal-header">'
      +   '<div class="lc-modal-title">Adicionado ao carrinho!</div>'
      +   '<button class="lc-modal-close" id="lcCartModalClose">&times;</button>'
      + '</div>'
      + '<div class="lc-modal-body">'
      +   '<img class="lc-modal-img" id="lcModalImg" src="" alt="" />'
      +   '<div class="lc-modal-info">'
      +     '<div class="lc-modal-name" id="lcModalName"></div>'
      +     '<div class="lc-modal-meta">Cor: <span id="lcModalColor"></span></div>'
      +     '<div class="lc-modal-meta">Disponibilidade: <span>Em estoque</span></div>'
      +     '<div class="lc-modal-meta" id="lcModalQtyLine"></div>'
      +   '</div>'
      + '</div>'
      + '<div class="lc-modal-subtotal">Subtotal do carrinho: <strong id="lcModalSubtotal"></strong></div>'
      + '<div class="lc-modal-actions">'
      +   '<a href="carrinho.html" class="lc-btn-cart-go">MEU CARRINHO</a>'
      +   '<a href="checkout.html" class="lc-btn-checkout">OU, ENCERRAR COMPRA &rsaquo;</a>'
      + '</div>'
      + '</div>';
    document.body.appendChild(overlay);

    overlay.addEventListener('click', function(e){
      if(e.target === overlay) closeModal();
    });
    document.getElementById('lcCartModalClose').addEventListener('click', closeModal);
    document.addEventListener('keydown', function(e){
      if(e.key==='Escape') closeModal();
    });
  }

  function openModal(item, subtotal) {
    injectModalStyles();
    buildModal();
    var overlay = document.getElementById('lcCartModalOverlay');
    document.getElementById('lcModalImg').src = item.img || '';
    document.getElementById('lcModalImg').alt = item.name || '';
    document.getElementById('lcModalName').textContent = item.name || '';
    document.getElementById('lcModalColor').textContent = item.color || '';
    var priceNum = parsePriceNum(item.price);
    var qty = item.qty || 1;
    document.getElementById('lcModalQtyLine').innerHTML = 'Qty: <span>'+ qty +' x '+ formatBRL(priceNum) +'</span>';
    document.getElementById('lcModalSubtotal').textContent = formatBRL(subtotal);
    overlay.classList.add('open');
  }

  function closeModal() {
    var overlay = document.getElementById('lcCartModalOverlay');
    if(overlay) overlay.classList.remove('open');
  }

  // ── addToCart ───────────────────────────────────────────
  window.addToCart = function() {
    var nameEl = document.querySelector('.product-title, h1.product-title, h1.product-name, .product-name > a, h1.nome-produto');
    var name = nameEl ? nameEl.textContent.trim() : document.title.split('|')[0].trim();

    var priceEl = document.querySelector('.price-range, .price-main, .product-price-main, .product-price');
    var price = priceEl ? priceEl.textContent.trim() : '';

    var imgEl = document.getElementById('mainImgEl');
    var img = imgEl ? imgEl.src : '';

    var colorEl = document.getElementById('colorName') || document.getElementById('colorDisplay');
    var color = colorEl ? colorEl.textContent.trim() : '';

    var qtyEl = document.getElementById('qtyInput');
    var qty = qtyEl ? (parseInt(qtyEl.value)||1) : 1;

    var href = window.location.pathname.split('/').pop() || window.location.href;
    var priceNum = parsePriceNum(price);

    var cart = getCart();
    var key = href + '|' + color;
    var existing = null;
    for(var i=0;i<cart.length;i++){
      if((cart[i].href+'|'+cart[i].color)===key){ existing=cart[i]; break; }
    }
    if(existing){
      existing.qty = (existing.qty||1) + qty;
      if(!existing.priceNum && priceNum) existing.priceNum = priceNum;
    } else {
      cart.push({name:name, price:price, priceNum:priceNum, img:img, color:color, qty:qty, href:href});
    }
    saveCart(cart);
    updateBadge();

    // Calc subtotal for modal
    var subtotal = cart.reduce(function(acc, item){
      return acc + parsePriceNum(item.price) * (item.qty||1);
    }, 0);

    var addedItem = existing || cart[cart.length-1];
    openModal(addedItem, subtotal);
  };

  // Fix Sacola link + update badge on load
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.header-icons a').forEach(function(a){
      var span = a.querySelector('span');
      if(span && /^Sacola/.test(span.textContent.trim()) && a.getAttribute('href')==='#'){
        a.href = 'carrinho.html';
      }
    });
    updateBadge();
  });
  if(document.readyState!=='loading') updateBadge();

  // Expose for carrinho.html
  window.lcGetCart = getCart;
  window.lcSaveCart = saveCart;
  window.lcTotalQty = totalQty;
})();
