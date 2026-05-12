# -*- coding: utf-8 -*-
import re

products = {
    'set-4-antiaderente-ceramica.html': {
        'warranty': '10 anos',
        'desc_p': 'Este conjunto de quatro peças com revestimento cerâmico antiaderente possui laterais arredondadas e capacidade generosa, ideal para grelhar, saltear e preparar receitas variadas com praticidade. O revestimento cerâmico de alta performance impede que os alimentos grudem e facilita a limpeza para um preparo mais eficiente.',
        'desc_items': [
            'Frigideira rasa 20 cm',
            'Frigideira rasa 28 cm',
            'Molheira 18 cm com tampa',
            'Panela Saute 26 cm com tampa',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Compatível com lava-louças e seguro para utensílios de metal',
            'Laterais arredondadas para maior capacidade e versatilidade',
            'Altamente ecológico, com emissões reduzidas e embalagem reciclável sem plástico',
            'Resistente a arranhões e de fácil limpeza',
        ],
        'specs': [
            ('Conteúdo', '2 Frigideiras + 2 Panelas com tampas'),
            ('Dimensões totais', '61 cm × 36 cm × 16 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque bem.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Use temperaturas moderadas — a cerâmica aquece rapidamente e retém o calor.',
            'Utensílios de metal são aceitáveis com cuidado; evite raspar bordas ou usar objetos cortantes.',
            'Prefira utensílios de silicone Le Creuset para prolongar a vida do revestimento.',
            'Aguarde esfriar antes de lavar; lave à mão para preservar o revestimento.',
            'Evite esponjas abrasivas; remova manchas persistentes com pasta de bicarbonato e água morna.',
            'Evite choque térmico (não coloque a panela quente em água fria).',
        ],
    },
    'set-2-frigideiras-rasas-24-28cm-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Este conjunto inclui duas frigideiras rasas (24 cm e 28 cm) com revestimento cerâmico antiaderente de alta performance. As laterais arredondadas e a capacidade generosa tornam as peças ideais para grelhar, saltear e preparar receitas variadas. Tampa de vidro não inclusa.',
        'desc_items': [
            'Frigideira rasa 24 cm (altura 7 cm)',
            'Frigideira rasa 28 cm (altura 7 cm)',
            'Tampa de vidro não inclusa',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Laterais arredondadas para fácil soltura dos alimentos',
            'Compatível com todos os tipos de fogão, incluindo indução',
            'Embalagem reciclável sem plástico',
            'Lavalouças (lavagem à mão recomendada para maior durabilidade)',
        ],
        'specs': [
            ('Tamanhos', '24 cm e 28 cm'),
            ('Altura', '7 cm cada'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque completamente.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Utensílios de metal são aceitáveis com cuidado — evite raspar bordas ou usar objetos cortantes.',
            'Aguarde esfriar antes de lavar; a lavagem à mão prolonga a vida do revestimento.',
            'Evite esponjas abrasivas; remova manchas com pasta de bicarbonato e água morna.',
            'Evite choque térmico e impactos.',
        ],
    },
    'set-2-frigideiras-20-26cm-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Conjunto com duas frigideiras rasas (20 cm e 26 cm) com revestimento cerâmico antiaderente de alta performance. As laterais arredondadas facilitam a soltura dos alimentos e a limpeza. Tampa de vidro não inclusa.',
        'desc_items': [
            'Frigideira rasa 20 cm (L20 × W20 × H7 cm)',
            'Frigideira rasa 26 cm (L26 × W26 × H7 cm)',
            'Tampa de vidro não inclusa',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Resistente a arranhões e seguro para utensílios de metal',
            'Laterais arredondadas para maior versatilidade',
            'Embalagem reciclável sem plástico',
            'Lavalouças',
        ],
        'specs': [
            ('Tamanhos', '20 cm e 26 cm'),
            ('Dimensões', '20cm: 20×20×7 cm · 26cm: 26×26×7 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque completamente.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Use temperaturas moderadas — a cerâmica aquece rapidamente.',
            'Utensílios de metal são aceitáveis com cuidado; evite raspar bordas ou usar objetos cortantes.',
            'Aguarde esfriar antes de lavar; a lavagem à mão prolonga a vida do revestimento.',
            'Evite esponjas abrasivas; remova manchas com pasta de bicarbonato e água morna.',
            'Evite choque térmico.',
        ],
    },
    'frigideira-funda-alca-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Frigideira funda com laterais arredondadas e capacidade generosa, ideal para grelhar, saltear e preparar receitas variadas com praticidade. O revestimento cerâmico antiaderente de alta performance impede que os alimentos grudem e facilita a limpeza para um preparo mais eficiente.',
        'desc_items': [
            'Disponível nos tamanhos 28 cm e 30 cm',
            'Revestimento cerâmico natural, ecológico e livre de substâncias nocivas',
            'Embalagem reciclável sem plástico',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Laterais arredondadas para maior capacidade e versatilidade',
            'Altamente ecológico com emissões reduzidas durante a produção',
            'Embalagem reciclável sem plástico',
            'Lavalouças',
        ],
        'specs': [
            ('Tamanhos disponíveis', '28 cm e 30 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque bem.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Utensílios de metal são aceitáveis com cuidado; prefira utensílios de silicone Le Creuset para maior durabilidade.',
            'Aguarde esfriar antes de lavar; a lavagem à mão prolonga a vida do revestimento.',
            'Evite esponjas abrasivas; remova manchas persistentes com pasta de bicarbonato e água morna.',
            'Evite choque térmico.',
        ],
    },
    'frigideira-rasa-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Frigideira rasa com laterais arredondadas, ideal para grelhar, saltear e preparar receitas variadas com praticidade. O revestimento cerâmico de alta performance impede que os alimentos grudem e simplifica a limpeza.',
        'desc_items': [
            'Disponível nos tamanhos: 20 cm, 24 cm, 26 cm, 28 cm e 30 cm',
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Embalagem reciclável sem plástico',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Laterais arredondadas e capacidade generosa',
            'Embalagem reciclável sem plástico',
            'Compatível com todos os tipos de fogão, incluindo indução',
            'Lavalouças (lavagem à mão recomendada)',
        ],
        'specs': [
            ('Tamanhos disponíveis', '20 cm · 24 cm · 26 cm · 28 cm · 30 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque completamente.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Utensílios de metal são aceitáveis com cuidado; evite raspar bordas.',
            'Aguarde esfriar antes de lavar; a lavagem à mão prolonga a vida do revestimento.',
            'Evite esponjas abrasivas; remova manchas com pasta de bicarbonato.',
            'Evite choque térmico e impactos.',
        ],
    },
    'molheira-alca-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Molheira com alça e laterais arredondadas, revestida com cerâmica antiaderente de alta performance. Ideal para grelhar, saltear e cozinhar diversas receitas com praticidade. O revestimento cerâmico facilita a soltura dos alimentos e a limpeza.',
        'desc_items': [
            'Disponível nos tamanhos: 16 cm, 18 cm e 20 cm',
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Embalagem reciclável sem plástico',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Laterais arredondadas e capacidade generosa',
            'Compatível com todos os tipos de fogão, incluindo indução',
            'Embalagem reciclável sem plástico',
            'Lavalouças',
        ],
        'specs': [
            ('Tamanhos disponíveis', '16 cm · 18 cm · 20 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque bem.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Utensílios de metal são aceitáveis com cuidado; prefira utensílios de silicone para maior durabilidade.',
            'Aguarde esfriar antes de lavar; a lavagem à mão prolonga a vida do revestimento.',
            'Evite esponjas abrasivas; remova manchas com pasta de bicarbonato e água morna.',
            'Evite quedas e choque térmico.',
        ],
    },
    'panela-saute-alca-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Panela Saute com alça e laterais arredondadas de capacidade generosa, ideal para grelhar, saltear e preparar receitas variadas com praticidade. O revestimento cerâmico antiaderente de alta performance facilita a soltura dos alimentos e a limpeza. Tampa de vidro inclusa.',
        'desc_items': [
            'Tamanho: 26 cm (altura 4 cm)',
            'Tampa de vidro inclusa',
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
        ],
        'features': [
            'Laterais arredondadas e capacidade generosa',
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Tampa de vidro inclusa',
            'Compatível com todos os tipos de fogão, incluindo indução',
            'Suporta temperaturas de até 280°C',
            'Embalagem reciclável sem plástico',
        ],
        'specs': [
            ('Tamanho', '26 cm'),
            ('Altura', '4 cm'),
            ('Dimensões', '26L × 26W × 16H cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque completamente.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Use temperaturas moderadas para melhor desempenho da cerâmica.',
            'Utensílios de metal são aceitáveis com cuidado; evite arranhões nas bordas.',
            'Prefira utensílios de silicone para prolongar a durabilidade.',
            'Aguarde esfriar antes de lavar; evite esponjas abrasivas.',
            'Remova manchas persistentes com pasta de bicarbonato e água morna.',
            'Evite choque térmico e quedas.',
        ],
    },
    'cacarola-funda-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Caçarola funda com laterais arredondadas e capacidade generosa de 3,8 L, ideal para selar e preparar receitas variadas. O revestimento cerâmico antiaderente de alta qualidade em toda a superfície impede que os alimentos grudem e facilita a limpeza. Compatível com todos os tipos de fogão, incluindo indução.',
        'desc_items': [
            'Tamanho: 20 cm · Capacidade: 3,8 L',
            'Base interna em alumínio espesso para distribuição uniforme do calor',
            'Base em aço inoxidável e aro reforçado para maior durabilidade',
            'Cabo ergonômico resistente ao calor',
        ],
        'features': [
            'Revestimento cerâmico de alta qualidade em toda a superfície, livre de PFAS',
            'Base interna em alumínio espesso para distribuição uniforme do calor',
            'Base em aço inoxidável e aro reforçado para maior durabilidade',
            'Cabo ergonômico resistente ao calor — fica frio ao toque durante o cozimento',
            'Superfície não reativa, resistente a arranhões e manchas',
            'Compatível com todos os tipos de fogão, incluindo indução',
            'Seguro para uso no forno até 288°C',
        ],
        'specs': [
            ('Tamanho', '20 cm'),
            ('Capacidade', '3,8 L'),
            ('Dimensões', '20 cm × 20 cm × 19 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Vitrocerâmica, indução, elétrico, gás, radiante, grelha, forno'),
            ('Temperatura máxima (forno)', '288°C'),
            ('Lavalouças', 'Sim (lavagem à mão recomendada)'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Lave à mão para preservar as características do produto e prolongar a vida útil.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Utensílios de metal são aceitáveis com cuidado; prefira utensílios de silicone Le Creuset.',
            'Aguarde esfriar antes de lavar; evite esponjas abrasivas.',
            'Remova manchas persistentes com pasta de bicarbonato e água morna.',
            'Evite choque térmico.',
        ],
    },
    'cacarola-baixa-antiaderente.html': {
        'warranty': '10 anos',
        'desc_p': 'Caçarola baixa com laterais arredondadas e capacidade generosa, ideal para grelhar, saltear e preparar receitas variadas com praticidade. O revestimento cerâmico antiaderente impede que os alimentos grudem e simplifica a limpeza. Tampa de vidro inclusa.',
        'desc_items': [
            'Disponível nos tamanhos: 28 cm e 30 cm',
            'Tampa de vidro inclusa',
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
        ],
        'features': [
            'Revestimento cerâmico natural, livre de PFOA, PFAS e PTFE',
            'Laterais arredondadas e capacidade generosa',
            'Tampa de vidro inclusa',
            'Aquecimento rápido e uniforme',
            'Embalagem reciclável sem plástico',
            'Lavalouças (lavagem à mão recomendada)',
        ],
        'specs': [
            ('Tamanhos disponíveis', '28 cm e 30 cm'),
            ('Material', 'Non-Stick Ceramic Essential'),
            ('Fontes de calor', 'Gás, elétrico, vitrocerâmica, indução, radiante, grelha, forno'),
            ('Temperatura máxima', '280°C'),
            ('Lavalouças', 'Sim'),
            ('Garantia', '10 anos'),
        ],
        'care': [
            'Antes do primeiro uso, lave com água morna e sabão neutro; seque completamente.',
            'Pré-aqueça em fogo baixo a médio com óleo ou gordura; evite aquecimento vazio.',
            'Utensílios de metal são aceitáveis com cuidado; prefira utensílios de silicone Le Creuset.',
            'Nunca use objetos cortantes diretamente na superfície.',
            'Aguarde esfriar antes de lavar; evite esponjas abrasivas.',
            'Remova manchas com pasta de bicarbonato e água morna.',
        ],
    },
    'tampa-vidro-tns.html': {
        'warranty': '3 anos',
        'desc_p': 'Disponível em uma variedade de tamanhos para encaixar nas panelas da linha TNS da Le Creuset, as tampas de vidro temperado permitem acompanhar o cozimento sem levantar e atrapalhar o processo.',
        'desc_items': [
            'Disponível nos tamanhos: 20 cm, 22 cm, 24 cm, 26 cm, 28 cm e 30 cm',
            'Compatível com a linha de panelas TNS Le Creuset',
            'Vidro temperado de alta resistência ao calor',
        ],
        'features': [
            'Vidro temperado com grande resistência ao calor — suporta até 220°C',
            'Permite monitorar o cozimento sem levantar a tampa',
            'Compatível com a linha de ferro fundido da Le Creuset',
            'Lavalouças',
            'Disponível em 6 tamanhos (20 cm a 30 cm)',
        ],
        'specs': [
            ('Tamanhos disponíveis', '20 cm · 22 cm · 24 cm · 26 cm · 28 cm · 30 cm'),
            ('Material', 'Vidro temperado'),
            ('Temperatura máxima', '220°C'),
            ('Lavalouças', 'Sim'),
            ('Origem', 'China'),
            ('Garantia', '3 anos'),
        ],
        'care': [
            'Pode ser lavada no lava-louças ou à mão.',
            'Evite impactos e quedas — o vidro temperado é resistente, mas não inquebrável.',
            'Evite choque térmico extremo.',
            'Não use objetos abrasivos para limpar.',
        ],
    },
}


def build_desc_tab(p):
    items_html = ''.join(f'\n        <li>{i}</li>' for i in p['desc_items'])
    return (
        '<div class="tab-body open">\n'
        f'      <p>{p["desc_p"]}</p>\n'
        '      <ul>'
        + items_html +
        '\n      </ul>\n'
        '    </div>'
    )


def build_specs_tab(p):
    rows = ''.join(
        f'\n          <div class="spec-row"><span class="spec-key">{k}</span><span class="spec-val">{v}</span></div>'
        for k, v in p['specs']
    )
    return (
        '<div class="tab-body">\n'
        '      <div class="specs-grid"><div>'
        + rows +
        '\n      </div></div>\n'
        '    </div>'
    )


def build_care_tab(p):
    items_html = ''.join(f'\n        <li>{i}</li>' for i in p['care'])
    return (
        '<div class="tab-body">\n'
        '      <ul>'
        + items_html +
        '\n      </ul>\n'
        '    </div>'
    )


import os
base = os.path.dirname(os.path.abspath(__file__))

for fname, data in products.items():
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1) Description tab body (has class "open")
    html = re.sub(
        r'(<div class="tab-header open"[^>]*>\s*Descrição.*?</div>\s*)<div class="tab-body open">.*?</div>',
        lambda m, d=data: m.group(1) + build_desc_tab(d),
        html, flags=re.DOTALL
    )

    # 2) Specs tab body
    html = re.sub(
        r'(<div class="tab-header"[^>]*>\s*Especificações Técnicas.*?</div>\s*)<div class="tab-body">.*?</div>',
        lambda m, d=data: m.group(1) + build_specs_tab(d),
        html, flags=re.DOTALL
    )

    # 3) Care tab body (third tab)
    # Find the "Uso e Cuidado" tab and replace its body
    html = re.sub(
        r'(<div class="tab-header"[^>]*>\s*Uso e Cuidado.*?</div>\s*)<div class="tab-body">.*?</div>',
        lambda m, d=data: m.group(1) + build_care_tab(d),
        html, flags=re.DOTALL
    )

    # 4) Update warranty trust badge
    html = html.replace(
        '<div class="trust-badge-text">2 Anos de Garantia</div>\n      <div class="trust-badge-sub">Garantia de 2 anos contra defeitos de fabricação</div>',
        f'<div class="trust-badge-text">Garantia {data["warranty"]}</div>\n      <div class="trust-badge-sub">Garantia de {data["warranty"]} contra defeitos de fabricação</div>'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated: {fname}')
