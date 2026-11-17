# サステオ デモ用のイラスト生成。フラットなベクターで、ブランド配色に統一する。
SKY, SKY2 = '#E7F3F0', '#D7EBE6'
FAR, MID  = '#BCDFD7', '#86CCBE'
BRAND, DEEP = '#009E8A', '#00796A'
INK = '#26332F'
WHITE = '#FFFFFF'
GREY, GREY2 = '#C7D4CE', '#A3B4AD'
ACCENT = '#EE8AAA'
SAND = '#D9CFBC'


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{label}">\n{body}\n</svg>\n')


def sky(w, h, horizon):
    return (f'<rect width="{w}" height="{h}" fill="{SKY}"/>'
            f'<rect y="{horizon-90}" width="{w}" height="90" fill="{SKY2}"/>')


def hills(w, horizon):
    return (f'<path d="M0,{horizon} C{w*0.12:.0f},{horizon-70} {w*0.22:.0f},{horizon-64} '
            f'{w*0.34:.0f},{horizon} Z" fill="{FAR}"/>'
            f'<path d="M{w*0.26:.0f},{horizon} C{w*0.42:.0f},{horizon-96} {w*0.58:.0f},{horizon-88} '
            f'{w*0.74:.0f},{horizon} Z" fill="{FAR}"/>'
            f'<path d="M{w*0.66:.0f},{horizon} C{w*0.78:.0f},{horizon-58} {w*0.9:.0f},{horizon-54} '
            f'{w},{horizon} Z" fill="{FAR}"/>')


def trees(xs, horizon, scale=1.0):
    out = []
    for i, x in enumerate(xs):
        s = scale * (0.86 + 0.12 * (i % 3))
        tw, th = 26 * s, 54 * s
        out.append(f'<path d="M{x},{horizon} l{-tw/2:.1f},0 l{tw/2:.1f},{-th:.1f} l{tw/2:.1f},{th:.1f} Z" fill="{MID}"/>')
        out.append(f'<path d="M{x},{horizon-th*0.5:.1f} l{-tw*0.42:.1f},0 l{tw*0.42:.1f},{-th*0.55:.1f} '
                   f'l{tw*0.42:.1f},{th*0.55:.1f} Z" fill="{BRAND}" opacity=".55"/>')
    return ''.join(out)


def truck(tx, ty, s=1.0, body=WHITE, cab=BRAND):
    """側面のトラック。ローカル 392x178、接地はローカル y=178。"""
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <rect x="0" y="0" width="250" height="120" rx="4" fill="{body}"/>
  <rect x="0" y="0" width="250" height="13" rx="4" fill="{SKY2}"/>
  <rect x="0" y="107" width="250" height="13" fill="{GREY}"/>
  <rect x="14" y="120" width="340" height="12" fill="{INK}" opacity=".22"/>
  <path d="M258,34 h70 c11,0 20,6 25,16 l23,42 c3,6 4,11 4,17 v11 h-122 z" fill="{cab}"/>
  <path d="M294,46 h32 c7,0 12,4 15,10 l15,28 h-62 z" fill="{SKY2}"/>
  <rect x="368" y="104" width="24" height="16" rx="3" fill="{DEEP}"/>
  <circle cx="62" cy="152" r="26" fill="{INK}"/><circle cx="62" cy="152" r="10" fill="{GREY2}"/>
  <circle cx="114" cy="152" r="26" fill="{INK}"/><circle cx="114" cy="152" r="10" fill="{GREY2}"/>
  <circle cx="330" cy="152" r="26" fill="{INK}"/><circle cx="330" cy="152" r="10" fill="{GREY2}"/>
</g>'''


def excavator(tx, ty, s=1.0):
    """ローカル 320x178、接地は y=178。"""
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <path d="M166,100 L236,46" stroke="{BRAND}" stroke-width="21" stroke-linecap="round" fill="none"/>
  <path d="M236,46 L286,108" stroke="{DEEP}" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M286,108 l24,8 -7,28 -32,-7 z" fill="{INK}"/>
  <rect x="26" y="86" width="18" height="54" rx="4" fill="{DEEP}"/>
  <rect x="40" y="84" width="130" height="58" rx="6" fill="{BRAND}"/>
  <rect x="44" y="40" width="64" height="46" rx="6" fill="{DEEP}"/>
  <rect x="53" y="49" width="46" height="28" rx="3" fill="{SKY2}"/>
  <rect x="0" y="140" width="210" height="38" rx="19" fill="{INK}"/>
  <rect x="16" y="151" width="178" height="16" rx="8" fill="{GREY2}"/>
</g>'''


def ship(tx, ty, s=1.0):
    """ローカル 420x150、喫水線は y=150。"""
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <rect x="96" y="60" width="54" height="34" fill="{ACCENT}"/>
  <rect x="152" y="60" width="54" height="34" fill="{BRAND}"/>
  <rect x="208" y="60" width="54" height="34" fill="{MID}"/>
  <rect x="124" y="26" width="54" height="34" fill="{BRAND}"/>
  <rect x="180" y="26" width="54" height="34" fill="{DEEP}"/>
  <rect x="300" y="34" width="86" height="60" rx="4" fill="{WHITE}"/>
  <rect x="312" y="48" width="18" height="14" fill="{SKY2}"/>
  <rect x="338" y="48" width="18" height="14" fill="{SKY2}"/>
  <rect x="312" y="70" width="44" height="12" fill="{SKY2}"/>
  <rect x="340" y="6" width="26" height="28" rx="3" fill="{BRAND}"/>
  <path d="M0,94 h420 l-44,56 h-332 z" fill="{DEEP}"/>
  <rect x="26" y="108" width="368" height="9" fill="{ACCENT}" opacity=".85"/>
</g>'''


def crane(tx, ty, s=1.0):
    """岸壁のコンテナクレーン。ローカル 360x260、接地は y=260。"""
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <path d="M190,52 h170" stroke="{BRAND}" stroke-width="15" stroke-linecap="round" fill="none"/>
  <path d="M8,52 h66" stroke="{BRAND}" stroke-width="15" stroke-linecap="round" fill="none"/>
  <path d="M130,30 L330,48" stroke="{INK}" stroke-width="6" fill="none"/>
  <path d="M130,30 L36,48" stroke="{INK}" stroke-width="6" fill="none"/>
  <rect x="48" y="60" width="164" height="16" rx="3" fill="{DEEP}"/>
  <rect x="98" y="22" width="64" height="38" rx="4" fill="{DEEP}"/>
  <path d="M62,250 L62,76" stroke="{INK}" stroke-width="12" fill="none"/>
  <path d="M198,250 L198,76" stroke="{INK}" stroke-width="12" fill="none"/>
  <path d="M62,160 L198,160" stroke="{INK}" stroke-width="8" fill="none"/>
  <rect x="284" y="44" width="34" height="16" rx="3" fill="{INK}"/>
  <path d="M301,60 L301,146" stroke="{INK}" stroke-width="4" fill="none"/>
  <rect x="266" y="146" width="70" height="34" rx="2" fill="{ACCENT}"/>
  <rect x="40" y="248" width="180" height="12" rx="3" fill="{INK}"/>
</g>'''


def generator(tx, ty, s=1.0):
    """ローカル 250x152、接地は y=152。"""
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <rect x="8" y="34" width="228" height="98" rx="6" fill="{WHITE}"/>
  <rect x="8" y="34" width="228" height="16" rx="6" fill="{BRAND}"/>
  <rect x="26" y="62" width="76" height="52" rx="3" fill="{SKY2}"/>
  <rect x="34" y="70" width="60" height="5" fill="{GREY2}"/>
  <rect x="34" y="82" width="60" height="5" fill="{GREY2}"/>
  <rect x="34" y="94" width="60" height="5" fill="{GREY2}"/>
  <rect x="124" y="62" width="88" height="52" rx="3" fill="{DEEP}"/>
  <circle cx="150" cy="80" r="9" fill="{SKY2}"/>
  <rect x="168" y="74" width="34" height="8" rx="4" fill="{MID}"/>
  <rect x="168" y="90" width="34" height="8" rx="4" fill="{ACCENT}"/>
  <path d="M236,116 c26,0 30,24 52,24" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>
  <rect x="0" y="132" width="250" height="20" rx="4" fill="{INK}"/>
</g>'''


def warehouse(tx, ty, s=1.0):
    """物流センター。ローカル 360x190、接地は y=190。"""
    doors = ''.join(
        f'<rect x="{34+i*110}" y="102" width="78" height="88" rx="2" fill="{SKY2}"/>'
        f'<rect x="{34+i*110}" y="102" width="78" height="11" fill="{ACCENT if i == 2 else BRAND}"/>'
        for i in range(3))
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <rect x="0" y="40" width="360" height="150" fill="{WHITE}"/>
  <rect x="-8" y="28" width="376" height="16" rx="3" fill="{DEEP}"/>
  <rect x="0" y="62" width="360" height="8" fill="{GREY}"/>
  {doors}
  <rect x="18" y="88" width="324" height="10" rx="3" fill="{GREY}"/>
</g>'''


def factory(tx, ty, s=1.0):
    """のこぎり屋根の工場。ローカル 330x200、接地は y=200。"""
    teeth = ''.join(
        f'<path d="M{120+i*70},96 L{120+i*70},66 L{190+i*70},96 Z" fill="{DEEP}"/>'
        for i in range(3))
    return f'''<g transform="translate({tx},{ty}) scale({s})">
  <circle cx="73" cy="16" r="17" fill="{WHITE}" opacity=".9"/>
  <circle cx="99" cy="4" r="12" fill="{WHITE}" opacity=".7"/>
  <circle cx="52" cy="2" r="10" fill="{WHITE}" opacity=".55"/>
  <rect x="58" y="34" width="28" height="166" fill="{DEEP}"/>
  <rect x="53" y="34" width="38" height="11" rx="2" fill="{INK}"/>
  <rect x="96" y="78" width="20" height="122" fill="{BRAND}"/>
  <rect x="92" y="78" width="28" height="9" rx="2" fill="{INK}"/>
  {teeth}
  <rect x="120" y="96" width="210" height="104" fill="{WHITE}"/>
  <rect x="120" y="96" width="210" height="9" fill="{GREY}"/>
  <rect x="144" y="132" width="34" height="30" fill="{SKY2}"/>
  <rect x="198" y="132" width="34" height="30" fill="{SKY2}"/>
  <rect x="252" y="132" width="34" height="30" fill="{ACCENT}"/>
  <rect x="144" y="176" width="142" height="24" fill="{SKY2}"/>
  <rect x="4" y="146" width="40" height="54" rx="6" fill="{MID}"/>
  <rect x="4" y="146" width="40" height="9" rx="4" fill="{DEEP}"/>
</g>'''



# ---------------------------------------------------------------- 各シーン
def scene_hero():
    """4:3。地平線を上げ、トラックを大きく置いて空の間延びを抑える。"""
    w, h, hz = 800, 600, 330
    b = [sky(w, h, hz), hills(w, hz), trees([58, 126, 196, 660, 726], hz, 1.5)]
    b.append(f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#DCE7E2"/>')
    b.append(f'<rect y="{hz+30}" width="{w}" height="{h-hz-30}" fill="{GREY}"/>')
    b.append(f'<rect y="{hz+30}" width="{w}" height="5" fill="{WHITE}" opacity=".7"/>')
    for x in range(14, w, 124):
        b.append(f'<rect x="{x}" y="{hz+208}" width="66" height="8" rx="4" fill="{WHITE}" opacity=".85"/>')
    b.append(truck(166, 306, 1.2))
    b.append(f'<rect x="44" y="372" width="96" height="10" rx="5" fill="{WHITE}" opacity=".55"/>')
    b.append(f'<rect x="16" y="414" width="128" height="10" rx="5" fill="{WHITE}" opacity=".4"/>')
    return svg(w, h, '\n'.join(b), '高速道路を走る大型トラックのイラスト')


def scene_leaf():
    w, h = 800, 600
    b = [f'<rect width="{w}" height="{h}" fill="{SKY}"/>',
         f'<circle cx="640" cy="150" r="118" fill="{SKY2}"/>',
         f'<path d="M150,470 C150,250 360,112 648,150 C676,414 452,534 150,470 Z" fill="{MID}" opacity=".5"/>',
         f'<path d="M178,452 C178,258 374,134 636,170 C660,410 452,512 178,452 Z" fill="{BRAND}"/>',
         f'<path d="M196,444 C340,392 500,306 628,178" stroke="{WHITE}" stroke-width="7" '
         f'fill="none" opacity=".72" stroke-linecap="round"/>']
    for t, dx, dy in [(0.22, -58, -46), (0.4, -62, -56), (0.58, -58, -58), (0.74, -48, -52)]:
        x = 196 + (628 - 196) * t
        y = 444 - (444 - 178) * (t ** 0.86)
        b.append(f'<path d="M{x:.0f},{y:.0f} l{dx},{dy}" stroke="{WHITE}" stroke-width="5" '
                 f'opacity=".5" stroke-linecap="round" fill="none"/>')
    b.append(f'<path d="M430,278 c26,34 38,52 38,66 a38,38 0 0 1-76,0 c0-14 12-32 38-66 Z" '
             f'fill="{WHITE}" opacity=".92"/>')
    b.append(f'<circle cx="416" cy="340" r="9" fill="{SKY2}"/>')
    b.append(f'<path d="M600,430 c18,24 26,36 26,46 a26,26 0 0 1-52,0 c0-10 8-22 26-46 Z" '
             f'fill="{WHITE}" opacity=".8"/>')
    return svg(w, h, '\n'.join(b), 'HVOの原料となる植物の葉と水滴のイラスト')


def _ground(w, h, hz, top=GREY, base='#DCE7E2'):
    return (f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="{base}"/>'
            f'<rect y="{hz+20}" width="{w}" height="{h-hz-20}" fill="{top}"/>')


def scene_use(kind):
    w, h, hz = 800, 500, 340
    b = [sky(w, h, hz), hills(w, hz)]
    if kind == 'logistics':
        b += [trees([60, 120, 710], hz, 1.1), _ground(w, h, hz)]
        for x in range(10, w, 110):
            b.append(f'<rect x="{x}" y="{hz+96}" width="56" height="6" rx="3" fill="{WHITE}" opacity=".8"/>')
        b.append(truck(190, 208, 0.84))
        lab = '幹線輸送のトラックのイラスト'
    elif kind == 'construction':
        b += [_ground(w, h, hz, top=SAND, base='#E3DACB')]
        b.append(f'<path d="M520,{hz+20} c50,-40 120,-34 170,6 L800,{hz+20} Z" fill="#CDBEA4"/>')
        b.append(excavator(206, 180, 0.9))
        b.append(f'<path d="M34,{hz+74} c20,-46 118,-46 140,0 Z" fill="#CDBEA4"/>')
        lab = '建設現場で稼働する油圧ショベルのイラスト'
    elif kind == 'port':
        b += [f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#BBD9DA"/>',
              f'<rect y="{hz}" width="{w}" height="22" fill="{GREY}"/>']
        for i in range(5):
            b.append(f'<rect x="{40+i*170}" y="{hz+52+ (i%2)*16}" width="120" height="7" rx="3" '
                     f'fill="{WHITE}" opacity=".55"/>')
        b.append(crane(120, 90, 1.0))
        b.append(f'<rect x="596" y="246" width="70" height="34" fill="{BRAND}"/>')
        b.append(f'<rect x="596" y="282" width="70" height="34" fill="{DEEP}"/>')
        b.append(f'<rect x="672" y="282" width="70" height="34" fill="{MID}"/>')
        lab = '港湾のコンテナクレーンと荷役のイラスト'
    elif kind == 'marine':
        b += [f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="#AFD2D6"/>']
        for i in range(6):
            b.append(f'<rect x="{-20+i*150}" y="{hz+46+(i%3)*26}" width="130" height="8" rx="4" '
                     f'fill="{WHITE}" opacity=".5"/>')
        b.append(ship(178, 190, 0.86))
        lab = '内航船のイラスト'
    elif kind == 'generator':
        b += [trees([700, 760], hz, 1.0), _ground(w, h, hz)]
        b.append(generator(276, 196, 1.0))
        b.append(f'<ellipse cx="104" cy="258" rx="34" ry="11" fill="{DEEP}"/>')
        b.append(f'<path d="M70,258 v78 a34,11 0 0 0 68,0 v-78 Z" fill="{BRAND}"/>')
        b.append(f'<rect x="70" y="284" width="68" height="7" fill="{DEEP}"/>')
        b.append(f'<rect x="70" y="310" width="68" height="7" fill="{DEEP}"/>')
        lab = '仮設電源として使われるディーゼル発電機のイラスト'
    elif kind == 'shipper':
        b += [_ground(w, h, hz)]
        b.append(warehouse(222, 150, 1.0))
        b.append(truck(32, 262, 0.42))
        b.append(truck(628, 262, 0.42))
        lab = '物流センターと委託輸送のイラスト'
    else:  # manufacturing
        b += [_ground(w, h, hz)]
        b.append(factory(240, 140, 1.0))
        b.append(f'<rect x="40" y="250" width="120" height="90" rx="4" fill="{WHITE}"/>')
        b.append(f'<rect x="40" y="250" width="120" height="12" fill="{MID}"/>')
        lab = '工場のボイラー設備のイラスト'
    return svg(w, h, '\n'.join(b), lab)


def scene_thumb(kind):
    w, h = 800, 450
    b = [f'<rect width="{w}" height="{h}" fill="{SKY}"/>']
    if kind == 'column':
        b += [f'<rect x="196" y="70" width="300" height="310" rx="8" fill="{WHITE}"/>',
              f'<rect x="196" y="70" width="300" height="46" rx="8" fill="{BRAND}"/>']
        for i, wd in enumerate([210, 240, 180, 230, 150]):
            b.append(f'<rect x="228" y="{152+i*40}" width="{wd}" height="12" rx="6" fill="{SKY2}"/>')
        b.append(f'<rect x="430" y="196" width="190" height="184" rx="8" fill="{DEEP}"/>')
        for i, bh in enumerate([54, 96, 72, 126]):
            b.append(f'<rect x="{456+i*42}" y="{348-bh}" width="24" height="{bh}" rx="4" '
                     f'fill="{ACCENT if i == 3 else MID}"/>')
        lab = 'コラム・解説記事のイメージイラスト'
    elif kind == 'case':
        b.append(f'<rect y="330" width="{w}" height="120" fill="{GREY}"/>')
        b.append(truck(80, 248, 0.46))
        b.append(truck(330, 248, 0.46))
        b.append(truck(580, 248, 0.46))
        lab = '導入事例のイメージイラスト'
    else:  # faq
        b += [f'<path d="M150,96 h320 a14,14 0 0 1 14,14 v150 a14,14 0 0 1 -14,14 h-240 '
              f'l-62,48 v-48 h-18 a14,14 0 0 1 -14,-14 v-150 a14,14 0 0 1 14,-14 Z" fill="{WHITE}"/>',
              f'<rect x="188" y="146" width="210" height="13" rx="6" fill="{SKY2}"/>',
              f'<rect x="188" y="182" width="248" height="13" rx="6" fill="{SKY2}"/>',
              f'<rect x="188" y="218" width="160" height="13" rx="6" fill="{SKY2}"/>',
              f'<path d="M420,224 h212 a14,14 0 0 1 14,14 v120 a14,14 0 0 1 -14,14 h-150 '
              f'l-50,40 v-40 h-12 a14,14 0 0 1 -14,-14 v-120 a14,14 0 0 1 14,-14 Z" fill="{BRAND}"/>',
              f'<rect x="452" y="266" width="150" height="13" rx="6" fill="{WHITE}" opacity=".85"/>',
              f'<rect x="452" y="302" width="110" height="13" rx="6" fill="{WHITE}" opacity=".6"/>']
        lab = 'よくある質問のイメージイラスト'
    return svg(w, h, '\n'.join(b), lab)


FILES = {
    'hero-truck.svg': (scene_hero(), '高速道路を走る大型トラックのイラスト'),
    'about-leaf.svg': (scene_leaf(), 'HVOの原料となる植物の葉と水滴のイラスト'),
    'use-logistics.svg': (scene_use('logistics'), '幹線輸送のトラックのイラスト'),
    'use-construction.svg': (scene_use('construction'), '建設現場で稼働する油圧ショベルのイラスト'),
    'use-port.svg': (scene_use('port'), '港湾のコンテナクレーンと荷役のイラスト'),
    'use-marine.svg': (scene_use('marine'), '内航船のイラスト'),
    'use-generator.svg': (scene_use('generator'), '仮設電源として使われるディーゼル発電機のイラスト'),
    'use-shipper.svg': (scene_use('shipper'), '物流センターと委託輸送のイラスト'),
    'use-manufacturing.svg': (scene_use('manufacturing'), '工場のボイラー設備のイラスト'),
    'post-column.svg': (scene_thumb('column'), 'コラム・解説記事のイメージイラスト'),
    'post-case.svg': (scene_thumb('case'), '導入事例のイメージイラスト'),
    'post-faq.svg': (scene_thumb('faq'), 'よくある質問のイメージイラスト'),
}

if __name__ == '__main__':
    import pathlib, sys
    out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for name, (content, _) in FILES.items():
        (out / name).write_text(content, encoding='utf-8')
    print(f'{len(FILES)} illustrations -> {out}')
