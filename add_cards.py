filepath = r"c:\Users\lojas\OneDrive\Área de Trabalho\lecreuset\colecao-primeira-le-creuset.html"
CDN = "https://www.lecreuset.com.br/dw/image/v2/BDRT_PRD/on/demandware.static/-/Sites-le-creuset-br-master/default/"
def u(p): return CDN + p + "?sw=650&sh=650&sm=fit"

WL = '<div class="product-wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'

def sw(color, title, iid, url, active=False, xs=""):
    ac = ' active' if active else ''
    st = f'background:{color}' + (f';{xs}' if xs else '')
    oc = f"swatchClick(event,this,'{iid}','{url}')"
    return f'          <span class="swatch{ac}" style="{st};" title="{title}" onclick="{oc}"></span>'

def card(n, comment, href, iid, img, alt, swatches, name, sub, price):
    s = '\n'.join(swatches) + '\n'
    return f"""      <!-- {comment} -->
      <div class="product-card">
        <div class="product-card-img">
          <a href="{href}"><img id="{iid}" src="{img}" alt="{alt}" /></a>
          {WL}
        </div>
        <div class="product-colors">
{s}        </div>
        <a href="{href}">
          <div class="product-card-name">{name}</div>
          <div class="product-card-sub">{sub}</div>
          <div class="product-card-price">{price}</div>
        </a>
      </div>"""

# ─── Image URLs ──────────────────────────────────────────────────────────────
# 13 Travessa Retangular Heritage
t13_lar = u("dwf31b1dc6/images/travessas-produto-lecreuset-heritage-laranja.png")
t13_ver = u("dw49913c7c/images/travessas-produto-lecreuset-heritage-vermelho.png")
t13_car = u("dwaa2a8d47/images/travessas-produto-lecreuset-heritage-caribe.png")
t13_nui = u("dwe1816222/images/travessa-retangular-heritage-nuit-23cm.png")

# 14 Manteigueira
t14_ver = u("dwcb6d18b9/images/manteigueira_vermelho_leceruset.jpg")

# 15 Suporte para Ovo
t15_ver = u("dw87cbb4d8/images/produto-lecreuset-porta-ovo-vermelho.png")
t15_lar = u("dw5965a290/images/produto-lecreuset-porta-ovo-laranja.png")
t15_mar = u("dw6a7bee87/images/produto-lecreuset-porta-ovo-marseille.png")
t15_mer = u("dwb82eaadd/images/produto-lecreuset-porta-ovo-meringue.png")
t15_nec = u("dw919ceaff/images/produto-lecreuset-porta-ovo-nectar.png")
t15_azu = u("dw4cda4535/images/suporte-para-ovo-azure.png")

# 16 Chaleira Clássica
t16_lar = u("dwc4ad1a8d/images/92009500490000.jpg")

# 17 Moedor de Pimenta 30cm
t17_lar = u("dw385cddde/images/tardes%20de%20verao/moedor-de-pimenta-30cm-laranja.png")
t17_ver = u("dw6de01276/images/tardes%20de%20verao/moedor-de-pimenta-30cm-vermelho.png")
t17_bla = u("dw703f2293/images/tardes%20de%20verao/moedor-de-pimenta-30cm-blackonyx.png")

# 18 Porta Utensílios Clássico
t18_fli = u("dw42382f9a/images/produto-lecreuset-utensil-flint.png")

# 19 Skillet Redonda Signature
t19_lar = u("dw02921f58/images/produto-lecreuset-skillet-laranja.png")
t19_ver = u("dw3a6991b9/images/produto-lecreuset-skillet-vermelho.png")
t19_bam = u("dw32dc5870/images/produto-lecreuset-skillet-bamboo.png")
t19_mar = u("dwadde9fdc/images/produto-lecreuset-skillet-marseille.png")

# 20 Stockpot
t20_lar = u("dw2b048ca4/images/stockpot-laranja-lecreuset-2025.png")
t20_ver = u("dwa51ddab9/images/stockpot-vermelho-lecreuset-2025.png")
t20_mer = u("dw6e670b95/images/stockpot-meringue-lecreuset-2025.png")
t20_art = u("dwc94f5e4c/images/stockpot-artichaut-lecreuset-2025.png")

# 21 Pote para Biscoito
t21_ver = u("dw374a4000/images/produto-lecreuset-vermelho-pote.png")

# 22 Grelha Quadrada Signature
t22_lar = u("dwc458a909/images/produto-lecreuset-grelha-laranja.png")

# 23 Moedor de Sal 30cm (same images as pimenta 30)
t23_lar = t17_lar; t23_ver = t17_ver; t23_bla = t17_bla

# 24 Porta Utensílios Signature
t24_lar = u("dwff8efbe1/images/produto-lecreuset-porta-utensilios-sig-laranja.png")
t24_ver = u("dw33b55c5c/images/produto-lecreuset-porta-utensilios-sig-vermelho.png")
t24_car = u("dwe50cc6ff/images/produto-lecreuset-porta-utensilios-sig-caribe.png")
t24_nec = u("dwf63b3362/images/produto-lecreuset-porta-utensilios-sig-nectar.png")
t24_spk = u("dw42b02d93/images/produto-lecreuset-porta-utensilios-sig-shellpink.png")

# 25 Panela Marmita Signature
t25_lar = u("dw1a9d0004/images/produto-lecreuset-panela-marmita-laranja.png")
t25_ver = u("dw16e84237/images/produto-lecreuset-panela-marmita-vermelho.png")
t25_car = u("dw28f2dcbd/images/produto-lecreuset-panela-marmita-caribe.png")
t25_nec = u("dwad357c4e/images/produto-lecreuset-panela-marmita-nectar.png")

# 26 Porta Condimento
t26_lar = u("dw96391238/images/porta-condimento-laranja-lecreuset4.png")
t26_ver = u("dwdf451dfa/images/porta-condimento-vermelho-lecreuset1.png")
t26_mar = u("dw88496a9c/images/porta-condimento-marseille-lecreuset1.png")
t26_car = u("dweab9487f/images/porta-condimento-caribe-lecreuset1.png")
t26_bra = u("dw499c819d/images/porta-condimento-branco-lecreuset1.png")

# 27 Pote para Mostarda
t27_dij = u("dw8878da41/images/pote-para-mostarda-lecreuset-djon1.png")

# 28 Panela Oval Signature
t28_lar = u("dw8bb2f0c6/images/produto-lecreuset-panela-oval-laranja.png")
t28_ver = u("dw6df5e152/images/produto-lecreuset-panela-oval-vermelho.png")
t28_art = u("dw180546c7/images/produto-lecreuset-panela-oval-artichaut.png")
t28_car = u("dw1c6eb7f5/images/produto-lecreuset-panela-oval-caribe.png")
t28_nec = u("dw2efcacf8/images/produto-lecreuset-panela-oval-nectar.png")

# 29 Pote para Geleia
t29_ver = u("dwa384dc5a/images/pote-para-geleia-lecreuset-vermelho.png")

# 30 Bowl de Preparo 2L
t30_ver = u("dw24bf448e/images/produto-lecreuset-bowl-de-prepraro-vermelho4.png")

# 31 Travessa Retangular Clássica
t31_azu = u("dwfe78ea59/images/tardes%20de%20verao/travessa-classica-azure-blue.png")

# 32 Panela de Arroz Every
t32_lar = u("dw854d155d/images/produto-lecreuset-panela-arroz-laranja1.png")
t32_cha = u("dw615f5a46/images/produto-lecreuset-panela-arroz-chambray.png")

# 33 Garrafa de Hidratação
t33_ver = u("dwf2749dc7/images/garrafa_hidratacao_squeeze_vermelho_cerise-5.jpg")
t33_mar = u("dw28dae310/images/garrafa_hidratacao_squeeze_azul_marseille-6.jpg")
t33_lar = u("dw1c240449/images/garrafa_hidratacao_squeeze_laranja_flame-7.jpg")

# 34 Pote para Mel
t34_nec = u("dw7ad6078c/images/pote-para-mel-lecreuset-nectar7.png")

# ─── Build new cards ─────────────────────────────────────────────────────────
new_cards = []

new_cards.append(card(13,'13. Travessa Retangular Heritage','https://www.lecreuset.com.br/travessa-retangular-heritage/71102.html','cp13',t13_lar,'Travessa Retangular Heritage',[
    sw('#d46820','Laranja','cp13',t13_lar,True), sw('#c8102e','Vermelho','cp13',t13_ver),
    sw('#00B8D4','Caribe','cp13',t13_car), sw('#2C3E6B','Nuit','cp13',t13_nui),
    sw('#2DBECD','Bleu Riviera','cp13',t13_lar), sw('#6B7C45','Artichaut','cp13',t13_lar),
    sw('#F5F5F5','Branco','cp13',t13_lar,xs='border:1px solid #ccc'), sw('#9EA5AB','Flint','cp13',t13_lar),
    sw('#F5F0E8','Meringue','cp13',t13_lar,xs='border:1px solid #ccc'), sw('#D4C44A','Nectar','cp13',t13_lar),
    sw('#F0B8C8','Shell Pink','cp13',t13_lar),
],'Travessa Retangular Heritage','Cer\u00e2mica Esmaltada \u00b7 23cm / 32cm','R$ 349,00 \u2013 R$ 499,00'))

new_cards.append(card(14,'14. Manteigueira','https://www.lecreuset.com.br/manteigueira-lecreuset/91015800.html','cp14',t14_ver,'Manteigueira',[
    sw('#c8102e','Vermelho','cp14',t14_ver,True), sw('#d46820','Laranja','cp14',t14_ver),
    sw('#2DBECD','Bleu Riviera','cp14',t14_ver), sw('#2060A0','Azure','cp14',t14_ver),
    sw('#6B7C45','Artichaut','cp14',t14_ver), sw('#F5F5F5','Branco','cp14',t14_ver,xs='border:1px solid #ccc'),
    sw('#9EA5AB','Flint','cp14',t14_ver),
],'Manteigueira','Cer\u00e2mica Esmaltada','R$ 429,00'))

new_cards.append(card(15,'15. Suporte para Ovo','https://www.lecreuset.com.br/porta-ovo/7170200.html','cp15',t15_lar,'Suporte para Ovo',[
    sw('#d46820','Laranja','cp15',t15_lar,True), sw('#c8102e','Vermelho','cp15',t15_ver),
    sw('#2060A0','Azure','cp15',t15_azu), sw('#4080B0','Marseille','cp15',t15_mar),
    sw('#F5F0E8','Meringue','cp15',t15_mer,xs='border:1px solid #ccc'), sw('#D4C44A','Nectar','cp15',t15_nec),
    sw('#F5F5F5','Branco','cp15',t15_lar,xs='border:1px solid #ccc'), sw('#9EA5AB','Flint','cp15',t15_lar),
    sw('#1C1C1C','Black Onyx','cp15',t15_lar),
],'Suporte para Ovo','Cer\u00e2mica Esmaltada','R$ 79,00'))

new_cards.append(card(16,'16. Chaleira Cl\u00e1ssica','https://www.lecreuset.com.br/chaleira-classica/920095.html','cp16',t16_lar,'Chaleira Cl\u00e1ssica',[
    sw('#d46820','Laranja','cp16',t16_lar,True), sw('#2DBECD','Bleu Riviera','cp16',t16_lar),
    sw('#F5F0E8','Meringue','cp16',t16_lar,xs='border:1px solid #ccc'), sw('#6B7C45','Artichaut','cp16',t16_lar),
    sw('#9EA5AB','Flint','cp16',t16_lar), sw('#1C1C1C','Black Onyx','cp16',t16_lar),
    sw('#F0B8C8','Shell Pink','cp16',t16_lar),
],'Chaleira Cl\u00e1ssica','A\u00e7o com Al\u00e7a Fen\u00f3lica \u00b7 1,6L / 2,1L','R$ 650,30 \u2013 R$ 1.059,00'))

new_cards.append(card(17,'17. Moedor de Pimenta 30cm','https://www.lecreuset.com.br/moedor-de-pimenta-30cm/960027.html','cp17',t17_lar,'Moedor de Pimenta 30cm',[
    sw('#d46820','Laranja','cp17',t17_lar,True), sw('#c8102e','Vermelho','cp17',t17_ver),
    sw('#1C1C1C','Black Onyx','cp17',t17_bla),
],'Moedor de Pimenta 30cm','ABS Acr\u00edlico \u00b7 Moagem em Cer\u00e2mica \u00b7 30cm','R$ 479,00'))

new_cards.append(card(18,'18. Porta Utens\u00edlios Cl\u00e1ssico','https://www.lecreuset.com.br/porta-utensilios-classico-lecreuset/71501.html','cp18',t18_fli,'Porta Utens\u00edlios Cl\u00e1ssico',[
    sw('#9EA5AB','Flint','cp18',t18_fli,True), sw('#d46820','Laranja','cp18',t18_fli),
    sw('#c8102e','Vermelho','cp18',t18_fli), sw('#2060A0','Azure','cp18',t18_fli),
    sw('#00B8D4','Caribe','cp18',t18_fli), sw('#F5F0E8','Meringue','cp18',t18_fli,xs='border:1px solid #ccc'),
    sw('#F5F5F5','Branco','cp18',t18_fli,xs='border:1px solid #ccc'), sw('#D4C44A','Nectar','cp18',t18_fli),
    sw('#1C1C1C','Black Onyx','cp18',t18_fli), sw('#F0B8C8','Shell Pink','cp18',t18_fli),
],'Porta Utens\u00edlios Cl\u00e1ssico','Cer\u00e2mica Esmaltada \u00b7 M\u00e9dio / Grande','R$ 223,30 \u2013 R$ 449,00'))

new_cards.append(card(19,'19. Skillet Redonda Signature','https://www.lecreuset.com.br/skillet-redonda-signature-lecreuset/20182.html','cp19',t19_lar,'Skillet Redonda Signature',[
    sw('#d46820','Laranja','cp19',t19_lar,True), sw('#c8102e','Vermelho','cp19',t19_ver),
    sw('#C8A87A','Bamboo','cp19',t19_bam), sw('#4080B0','Marseille','cp19',t19_mar),
    sw('#2DBECD','Bleu Riviera','cp19',t19_lar), sw('#2060A0','Azure','cp19',t19_lar),
    sw('#6B7C45','Artichaut','cp19',t19_lar), sw('#F5F5F5','Branco','cp19',t19_lar,xs='border:1px solid #ccc'),
    sw('#9EA5AB','Flint','cp19',t19_lar), sw('#D4C44A','Nectar','cp19',t19_lar),
    sw('#1C1C1C','Black Onyx','cp19',t19_lar), sw('#6B5B7B','Rhone','cp19',t19_lar),
    sw('#F5E6A0','Camomille','cp19',t19_lar),
],'Skillet Redonda Signature','Ferro Fundido Esmaltado \u00b7 20cm a 30cm','R$ 1.304,25 \u2013 R$ 1.999,00'))

new_cards.append(card(20,'20. Stockpot Pegador Fen\u00f3lico','https://www.lecreuset.com.br/stockpot/921000.html','cp20',t20_lar,'Stockpot Pegador Fen\u00f3lico',[
    sw('#d46820','Laranja','cp20',t20_lar,True), sw('#c8102e','Vermelho','cp20',t20_ver),
    sw('#F5F0E8','Meringue','cp20',t20_mer,xs='border:1px solid #ccc'), sw('#6B7C45','Artichaut','cp20',t20_art),
    sw('#00B8D4','Caribe','cp20',t20_lar), sw('#F5F5F5','Branco','cp20',t20_lar,xs='border:1px solid #ccc'),
    sw('#A8D8C0','Cool Mint','cp20',t20_lar),
],'Stockpot Pegador Fen\u00f3lico','Ferro Fundido Esmaltado \u00b7 20cm / 22cm / 26cm','R$ 671,30 \u2013 R$ 1.279,00'))

new_cards.append(card(21,'21. Pote para Biscoito 2,4L','https://www.lecreuset.com.br/pote-para-biscoito/910267.html','cp21',t21_ver,'Pote para Biscoito 2,4L',[
    sw('#c8102e','Vermelho','cp21',t21_ver,True), sw('#d46820','Laranja','cp21',t21_ver),
    sw('#2060A0','Azure','cp21',t21_ver), sw('#00B8D4','Caribe','cp21',t21_ver),
    sw('#F5F0E8','Meringue','cp21',t21_ver,xs='border:1px solid #ccc'), sw('#F0B8C8','Shell Pink','cp21',t21_ver),
],'Pote para Biscoito 2,4L','Cer\u00e2mica Esmaltada \u00b7 2,4L','R$ 649,00'))

new_cards.append(card(22,'22. Grelha Quadrada Signature','https://www.lecreuset.com.br/grelha-quadrada-lecreuset/20183.html','cp22',t22_lar,'Grelha Quadrada Signature',[
    sw('#d46820','Laranja','cp22',t22_lar,True), sw('#c8102e','Vermelho','cp22',t22_lar),
    sw('#2DBECD','Bleu Riviera','cp22',t22_lar), sw('#6B7C45','Artichaut','cp22',t22_lar),
    sw('#F5F5F5','Branco','cp22',t22_lar,xs='border:1px solid #ccc'), sw('#9EA5AB','Flint','cp22',t22_lar),
    sw('#D4C44A','Nectar','cp22',t22_lar), sw('#1C1C1C','Black Onyx','cp22',t22_lar),
    sw('#6B5B7B','Rhone','cp22',t22_lar),
],'Grelha Quadrada Signature','Ferro Fundido \u00b7 26cm / 30cm','R$ 1.759,00 \u2013 R$ 1.859,00'))

new_cards.append(card(23,'23. Moedor de Sal 30cm','https://www.lecreuset.com.br/moedor-de-sal/960028.html','cp23',t23_lar,'Moedor de Sal 30cm',[
    sw('#d46820','Laranja','cp23',t23_lar,True), sw('#c8102e','Vermelho','cp23',t23_ver),
    sw('#1C1C1C','Black Onyx','cp23',t23_bla),
],'Moedor de Sal 30cm','ABS Acr\u00edlico \u00b7 Moagem em Cer\u00e2mica \u00b7 30cm','R$ 479,00'))

new_cards.append(card(24,'24. Porta Utens\u00edlios Signature','https://www.lecreuset.com.br/porta-utensilios-signature-1l/71502.html','cp24',t24_lar,'Porta Utens\u00edlios Signature',[
    sw('#d46820','Laranja','cp24',t24_lar,True), sw('#c8102e','Vermelho','cp24',t24_ver),
    sw('#00B8D4','Caribe','cp24',t24_car), sw('#D4C44A','Nectar','cp24',t24_nec),
    sw('#F0B8C8','Shell Pink','cp24',t24_spk), sw('#F5F5F5','Branco','cp24',t24_lar,xs='border:1px solid #ccc'),
],'Porta Utens\u00edlios Signature','Cer\u00e2mica Esmaltada \u00b7 1L','R$ 319,00 \u2013 R$ 449,00'))

new_cards.append(card(25,'25. Panela Marmita Signature','https://www.lecreuset.com.br/panela-marmita-signature/21114.html','cp25',t25_lar,'Panela Marmita Signature',[
    sw('#d46820','Laranja','cp25',t25_lar,True), sw('#c8102e','Vermelho','cp25',t25_ver),
    sw('#00B8D4','Caribe','cp25',t25_car), sw('#D4C44A','Nectar','cp25',t25_nec),
    sw('#2DBECD','Bleu Riviera','cp25',t25_lar), sw('#2060A0','Azure','cp25',t25_lar),
    sw('#F5F0E8','Meringue','cp25',t25_lar,xs='border:1px solid #ccc'), sw('#6B7C45','Artichaut','cp25',t25_lar),
    sw('#F5F5F5','Branco','cp25',t25_lar,xs='border:1px solid #ccc'), sw('#6B5B7B','Rhone','cp25',t25_lar),
],'Panela Marmita Signature','Ferro Fundido Esmaltado \u00b7 26cm / 28cm / 32cm','R$ 2.091,75 \u2013 R$ 3.279,00'))

new_cards.append(card(26,'26. Porta Condimento','https://www.lecreuset.com.br/porta-condimento-lecreuset/910114.html','cp26',t26_ver,'Porta Condimento',[
    sw('#c8102e','Vermelho','cp26',t26_ver,True), sw('#d46820','Laranja','cp26',t26_lar),
    sw('#4080B0','Marseille','cp26',t26_mar), sw('#00B8D4','Caribe','cp26',t26_car),
    sw('#F5F5F5','Branco','cp26',t26_bra,xs='border:1px solid #ccc'),
],'Porta Condimento','Cer\u00e2mica Esmaltada \u00b7 200ml / 400ml / 800ml','R$ 289,00 \u2013 R$ 439,00'))

new_cards.append(card(27,'27. Pote para Mostarda','https://www.lecreuset.com.br/pote-para-mostarda/91019900700000.html','cp27',t27_dij,'Pote para Mostarda',[
    sw('#D4A830','Dijon','cp27',t27_dij,True),
],'Pote para Mostarda','Cer\u00e2mica Esmaltada \u00b7 200ml','R$ 379,00'))

new_cards.append(card(28,'28. Panela Oval Signature','https://www.lecreuset.com.br/panela-oval-signature/21178.html','cp28',t28_lar,'Panela Oval Signature',[
    sw('#d46820','Laranja','cp28',t28_lar,True), sw('#c8102e','Vermelho','cp28',t28_ver),
    sw('#6B7C45','Artichaut','cp28',t28_art), sw('#00B8D4','Caribe','cp28',t28_car),
    sw('#D4C44A','Nectar','cp28',t28_nec), sw('#2DBECD','Bleu Riviera','cp28',t28_lar),
    sw('#2060A0','Azure','cp28',t28_lar), sw('#F5F0E8','Meringue','cp28',t28_lar,xs='border:1px solid #ccc'),
    sw('#F5F5F5','Branco','cp28',t28_lar,xs='border:1px solid #ccc'), sw('#1C1C1C','Black Onyx','cp28',t28_lar),
    sw('#6B5B7B','Rhone','cp28',t28_lar),
],'Panela Oval Signature','Ferro Fundido Esmaltado \u00b7 29cm a 40cm','R$ 3.079,00 \u2013 R$ 4.889,00'))

new_cards.append(card(29,'29. Pote para Geleia','https://www.lecreuset.com.br/pote-para-geleia-vermelho/91020000060000.html','cp29',t29_ver,'Pote para Geleia',[
    sw('#c8102e','Vermelho','cp29',t29_ver,True),
],'Pote para Geleia','Cer\u00e2mica Esmaltada \u00b7 200ml','R$ 379,00'))

new_cards.append(card(30,'30. Bowl de Preparo 2L','https://www.lecreuset.com.br/bowl-de-preparo-lecreuset-2l/701062.html','cp30',t30_ver,'Bowl de Preparo 2L',[
    sw('#c8102e','Vermelho','cp30',t30_ver,True), sw('#d46820','Laranja','cp30',t30_ver),
    sw('#2060A0','Azure','cp30',t30_ver), sw('#D4C44A','Nectar','cp30',t30_ver),
    sw('#F0B8C8','Shell Pink','cp30',t30_ver),
],'Bowl de Preparo 2L','Cer\u00e2mica Esmaltada \u00b7 2L','R$ 300,30 \u2013 R$ 429,00'))

new_cards.append(card(31,'31. Travessa Retangular Cl\u00e1ssica','https://www.lecreuset.com.br/travessa-retangular-classica/910047.html','cp31',t31_azu,'Travessa Retangular Cl\u00e1ssica',[
    sw('#2060A0','Azure','cp31',t31_azu,True), sw('#d46820','Laranja','cp31',t31_azu),
    sw('#c8102e','Vermelho','cp31',t31_azu), sw('#F5F0E8','Meringue','cp31',t31_azu,xs='border:1px solid #ccc'),
    sw('#F5F5F5','Branco','cp31',t31_azu,xs='border:1px solid #ccc'), sw('#D4C44A','Nectar','cp31',t31_azu),
],'Travessa Retangular Cl\u00e1ssica','Cer\u00e2mica Esmaltada','R$ 519,00 \u2013 R$ 709,00'))

new_cards.append(card(32,'32. Panela de Arroz Every','https://www.lecreuset.com.br/panela-arroz-every-lecreuset/4111018.html','cp32',t32_lar,'Panela de Arroz Every',[
    sw('#d46820','Laranja','cp32',t32_lar,True), sw('#8BAABE','Chambray','cp32',t32_cha),
    sw('#c8102e','Vermelho','cp32',t32_lar), sw('#2060A0','Azure','cp32',t32_lar),
    sw('#F0B8C8','Shell Pink','cp32',t32_lar),
],'Panela de Arroz Every','Cer\u00e2mica com Ferro Fundido \u00b7 18cm / 20cm','R$ 2.519,00 \u2013 R$ 2.769,00'))

new_cards.append(card(33,'33. Garrafa de Hidrata\u00e7\u00e3o','https://www.lecreuset.com.br/garrafa-de-hidratacao-em-aco-inox/4120850.html','cp33',t33_lar,'Garrafa de Hidrata\u00e7\u00e3o',[
    sw('#d46820','Laranja','cp33',t33_lar,True), sw('#c8102e','Vermelho','cp33',t33_ver),
    sw('#4080B0','Marseille','cp33',t33_mar),
],'Garrafa de Hidrata\u00e7\u00e3o','A\u00e7o Inoxid\u00e1vel \u00b7 500ml','R$ 319,00'))

new_cards.append(card(34,'34. Pote para Mel','https://www.lecreuset.com.br/pote-para-mel/690954.html','cp34',t34_nec,'Pote para Mel',[
    sw('#D4C44A','Nectar','cp34',t34_nec,True), sw('#F5F0E8','Meringue','cp34',t34_nec,xs='border:1px solid #ccc'),
],'Pote para Mel','Cer\u00e2mica Esmaltada \u00b7 200ml','R$ 379,00'))

# ─── Inject into file ────────────────────────────────────────────────────────
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

insert_marker = '\n    </div><!-- end product-grid -->'
insert_idx = content.index(insert_marker)

new_html = '\n' + '\n'.join(new_cards) + '\n    '
new_content = content[:insert_idx] + new_html + content[insert_idx:]

# Update product count
new_content = new_content.replace('12 produtos', '34 produtos', 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done. Added 22 new cards. Total file: {len(new_content)} chars")
