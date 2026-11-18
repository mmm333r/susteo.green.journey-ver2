# 下層ページ用の図版。illus.py の配色・部品を共有する。
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from illus import (SKY, SKY2, FAR, MID, BRAND, DEEP, INK, WHITE, GREY, GREY2,
                   ACCENT, SAND, svg, sky, hills, trees, truck, excavator, ship,
                   crane, generator, warehouse, factory)

BW, BH, BHZ = 1600, 500, 376          # 帯（16:5）
CW, CH = 800, 500                      # カード（16:10）
TW, TH = 800, 450                      # サムネイル（16:9）


# ------------------------------------------------------------------ 部品
def drum(x, y, s=1.0, body=BRAND, band=WHITE, cap=DEEP):
    """ドラム缶。ローカル 90x130、接地 y=130。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <path d="M0,14 v102 a45,14 0 0 0 90,0 V14 Z" fill="{body}"/>
  <rect x="0" y="42" width="90" height="11" fill="{band}" opacity=".92"/>
  <rect x="0" y="80" width="90" height="11" fill="{band}" opacity=".92"/>
  <ellipse cx="45" cy="14" rx="45" ry="14" fill="{cap}"/>
  <ellipse cx="45" cy="14" rx="26" ry="8" fill="{body}" opacity=".55"/>
</g>'''


def sheet(x, y, s=1.0, accent=BRAND, rows=4, w=130, h=168):
    """書類。ローカル w x h。"""
    lines = ''.join(
        f'<rect x="20" y="{54+i*26}" width="{w-40-(18 if i % 2 else 0)}" height="9" rx="4" fill="{SKY2}"/>'
        for i in range(rows))
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect width="{w}" height="{h}" rx="6" fill="{WHITE}"/>
  <rect width="{w}" height="26" rx="6" fill="{accent}"/>
  {lines}
</g>'''


def chart(x, y, s=1.0, vals=(60, 108, 78, 140), hl=3, w=210, h=170):
    """棒グラフ。ローカル w x h。"""
    bars = ''.join(
        f'<rect x="{30+i*44}" y="{h-26-v}" width="28" height="{v}" rx="4" '
        f'fill="{ACCENT if i == hl else MID}"/>' for i, v in enumerate(vals))
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect width="{w}" height="{h}" rx="6" fill="{WHITE}"/>
  {bars}
  <rect x="18" y="{h-24}" width="{w-36}" height="5" rx="2" fill="{GREY}"/>
</g>'''


def cloud(x, y, s=1.0, fill=WHITE, op=.9):
    return (f'<g transform="translate({x},{y}) scale({s})" opacity="{op}">'
            f'<circle cx="34" cy="34" r="26" fill="{fill}"/>'
            f'<circle cx="68" cy="26" r="20" fill="{fill}"/>'
            f'<circle cx="94" cy="38" r="24" fill="{fill}"/>'
            f'<rect x="30" y="38" width="68" height="24" rx="12" fill="{fill}"/></g>')


def plug(x, y, s=1.0):
    """充電プラグ。ローカル 76x120。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="18" y="0" width="12" height="30" rx="6" fill="{INK}"/>
  <rect x="46" y="0" width="12" height="30" rx="6" fill="{INK}"/>
  <rect x="6" y="28" width="64" height="44" rx="10" fill="{DEEP}"/>
  <path d="M38,72 v22 c0,16 -24,10 -24,26" stroke="{INK}" stroke-width="8"
        fill="none" stroke-linecap="round"/>
</g>'''


def h2tank(x, y, s=1.0):
    """水素タンク。ローカル 150x90、接地 y=90。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="0" y="14" width="150" height="62" rx="31" fill="{WHITE}"/>
  <rect x="0" y="14" width="150" height="62" rx="31" fill="none" stroke="{GREY}" stroke-width="3"/>
  <rect x="26" y="34" width="98" height="22" rx="11" fill="{MID}"/>
  <rect x="0" y="76" width="150" height="14" rx="4" fill="{INK}"/>
</g>'''


def train(x, y, s=1.0):
    """鉄道車両（側面）。ローカル 300x120、接地 y=120。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <path d="M0,6 h250 c28,0 50,22 50,50 v38 H0 Z" fill="{DEEP}"/>
  <rect x="18" y="26" width="52" height="34" rx="4" fill="{SKY2}"/>
  <rect x="86" y="26" width="52" height="34" rx="4" fill="{SKY2}"/>
  <rect x="154" y="26" width="52" height="34" rx="4" fill="{SKY2}"/>
  <path d="M232,26 h28 c14,0 26,12 26,26 v8 h-54 Z" fill="{SKY2}"/>
  <rect x="0" y="86" width="300" height="10" fill="{ACCENT}"/>
  <circle cx="60" cy="108" r="14" fill="{INK}"/><circle cx="110" cy="108" r="14" fill="{INK}"/>
  <circle cx="200" cy="108" r="14" fill="{INK}"/><circle cx="250" cy="108" r="14" fill="{INK}"/>
</g>'''


def plane(x, y, s=1.0):
    """航空機。ローカル 330x150。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <path d="M10,86 h212 c30,0 58,-10 78,-26 l24,-18 -30,6 -56,22 h-40 l-44,-44 h-26 l22,46
           h-52 l-26,-26 h-18 l14,30 -22,8 z" fill="{WHITE}"/>
  <path d="M10,86 h212 c30,0 58,-10 78,-26 l24,-18 -30,6 -56,22 h-40 l-44,-44 h-26 l22,46
           h-52 l-26,-26 h-18 l14,30 -22,8 z" fill="none" stroke="{GREY}" stroke-width="3"/>
  <rect x="60" y="74" width="120" height="9" rx="4" fill="{BRAND}"/>
  <circle cx="232" cy="70" r="7" fill="{ACCENT}"/>
</g>'''


def tanker(x, y, s=1.0):
    """タンクローリー。ローカル 392x178、接地 y=178。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="6" y="34" width="246" height="84" rx="42" fill="{WHITE}"/>
  <rect x="6" y="34" width="246" height="84" rx="42" fill="none" stroke="{GREY}" stroke-width="3"/>
  <rect x="48" y="66" width="164" height="22" rx="11" fill="{BRAND}"/>
  <rect x="14" y="118" width="340" height="12" fill="{INK}" opacity=".22"/>
  <path d="M258,34 h70 c11,0 20,6 25,16 l23,42 c3,6 4,11 4,17 v11 h-122 z" fill="{BRAND}"/>
  <path d="M294,46 h32 c7,0 12,4 15,10 l15,28 h-62 z" fill="{SKY2}"/>
  <circle cx="62" cy="152" r="26" fill="{INK}"/><circle cx="62" cy="152" r="10" fill="{GREY2}"/>
  <circle cx="114" cy="152" r="26" fill="{INK}"/><circle cx="114" cy="152" r="10" fill="{GREY2}"/>
  <circle cx="330" cy="152" r="26" fill="{INK}"/><circle cx="330" cy="152" r="10" fill="{GREY2}"/>
</g>'''


def tank(x, y, s=1.0):
    """貯蔵タンク。ローカル 190x150、接地 y=150。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="0" y="22" width="190" height="118" rx="10" fill="{WHITE}"/>
  <rect x="0" y="22" width="190" height="118" rx="10" fill="none" stroke="{GREY}" stroke-width="3"/>
  <path d="M-6,22 h202 l-16,-22 h-170 z" fill="{DEEP}"/>
  <rect x="26" y="62" width="138" height="20" rx="10" fill="{MID}"/>
  <rect x="26" y="96" width="92" height="14" rx="7" fill="{SKY2}"/>
  <rect x="0" y="140" width="190" height="10" rx="3" fill="{INK}"/>
</g>'''


def stepdots(x, y, s=1.0, n=5, hl=0, gap=120):
    """工程の丸印を線でつなぐ。ローカル (n-1)*gap+72 x 72。"""
    line = f'<rect x="36" y="32" width="{(n-1)*gap}" height="6" rx="3" fill="{MID}"/>'
    dots = ''.join(
        f'<circle cx="{36+i*gap}" cy="35" r="{30 if i == hl else 24}" '
        f'fill="{ACCENT if i == hl else BRAND}"/>'
        f'<circle cx="{36+i*gap}" cy="35" r="{14 if i == hl else 11}" fill="{WHITE}"/>'
        for i in range(n))
    return f'<g transform="translate({x},{y}) scale({s})">{line}{dots}</g>'


def clipboard(x, y, s=1.0):
    """確認用のクリップボード。ローカル 140x180。"""
    checks = ''.join(
        f'<rect x="24" y="{62+i*34}" width="20" height="20" rx="4" fill="{SKY2}"/>'
        f'<path d="M28,{72+i*34} l6,6 10,-12" stroke="{BRAND if i < 2 else GREY2}" '
        f'stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<rect x="54" y="{68+i*34}" width="{62-i*8}" height="8" rx="4" fill="{SKY2}"/>'
        for i in range(3))
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect y="14" width="140" height="166" rx="8" fill="{WHITE}"/>
  <rect y="14" width="140" height="166" rx="8" fill="none" stroke="{GREY}" stroke-width="3"/>
  <rect x="44" y="0" width="52" height="26" rx="8" fill="{DEEP}"/>
  {checks}
</g>'''


def badge(x, y, s=1.0, fill=BRAND):
    """認証バッジ。ローカル 130x150。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <circle cx="65" cy="62" r="56" fill="{fill}"/>
  <circle cx="65" cy="62" r="42" fill="{WHITE}" opacity=".25"/>
  <path d="M44,62 l14,14 28,-30" stroke="{WHITE}" stroke-width="10"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M38,104 l-10,46 37,-20 37,20 -10,-46 z" fill="{ACCENT}"/>
</g>'''


# ------------------------------------------------------------------ 帯（16:5）
def h2cyl(x, y, s=1.0):
    """水素ボンベ。ローカル 90x192、接地 y=192。"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="10" y="40" width="70" height="152" rx="24" fill="{WHITE}"/>
  <rect x="10" y="40" width="70" height="152" rx="24" fill="none" stroke="{GREY}" stroke-width="3"/>
  <rect x="34" y="8" width="22" height="36" rx="6" fill="{INK}"/>
  <rect x="24" y="2" width="42" height="12" rx="6" fill="{DEEP}"/>
  <rect x="20" y="92" width="50" height="28" rx="14" fill="{MID}"/>
</g>'''


def seal(x, y, s=1.0):
    """確認印。ローカル 120x120。"""
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<circle cx="60" cy="60" r="58" fill="{ACCENT}"/>'
            f'<circle cx="60" cy="60" r="44" fill="none" stroke="{WHITE}" stroke-width="7"/>'
            f'<rect x="38" y="52" width="44" height="7" rx="3" fill="{WHITE}"/>'
            f'<rect x="38" y="68" width="44" height="7" rx="3" fill="{WHITE}"/></g>')


def _band(extra='', hz=BHZ, ground='#DCE7E2', top=GREY, scenery=True):
    out = sky(BW, BH, hz)
    if scenery:
        out += hills(BW, hz)
    out += (f'<rect y="{hz}" width="{BW}" height="{BH-hz}" fill="{ground}"/>'
            f'<rect y="{hz+18}" width="{BW}" height="{BH-hz-18}" fill="{top}"/>')
    return out + extra


def _flat():
    """書類まわりの帯。地面は薄い帯だけにする。"""
    return (f'<rect width="{BW}" height="{BH}" fill="{SKY}"/>'
            f'<rect y="{BH-104}" width="{BW}" height="104" fill="{SKY2}"/>')


def b_products():
    """左：サステオ100（HVOのみ）／右：サステオ51（HVO＋軽油）。"""
    b = [_band()]
    b.append(drum(400, 142, 1.8, BRAND, WHITE))
    b.append(f'<rect x="386" y="404" width="190" height="12" rx="6" fill="{BRAND}"/>')
    b.append(drum(940, 142, 1.8, BRAND, WHITE))
    b.append(drum(1120, 142, 1.8, GREY2, WHITE, INK))
    b.append(f'<rect x="926" y="404" width="190" height="12" rx="6" fill="{BRAND}"/>')
    b.append(f'<rect x="1120" y="404" width="184" height="12" rx="6" fill="{GREY2}"/>')
    b.append(f'<rect x="760" y="250" width="12" height="80" rx="6" fill="{MID}"/>')
    return svg(BW, BH, '\n'.join(b), 'サステオ100とサステオ51の製品イメージ')


def b_fuel_compare():
    b = [_band()]
    for i, (col, cap, bar) in enumerate([(BRAND, DEEP, BRAND), (MID, DEEP, MID), (GREY2, INK, GREY2)]):
        x = 300 + i * 420
        b.append(drum(x, 142, 1.8, col, WHITE, cap))
        b.append(f'<rect x="{x-14}" y="404" width="190" height="12" rx="6" fill="{bar}"/>')
    return svg(BW, BH, '\n'.join(b), 'HVO・FAME・軽油の3種類を並べた比較イメージ')


def b_measure_compare():
    b = [_band()]
    b.append(truck(170, 198, 1.0))
    b.append(plug(700, 190, 1.9))
    b.append(f'<rect x="668, 0" y="0" width="0" height="0" fill="none"/>')
    b.append(f'<rect x="676" y="368" width="180" height="12" rx="6" fill="{DEEP}"/>')
    b.append(h2cyl(1130, 184, 1.0))
    b.append(h2cyl(1250, 184, 1.0))
    b.append(f'<rect x="1116" y="382" width="240" height="12" rx="6" fill="{MID}"/>')
    return svg(BW, BH, '\n'.join(b), 'HVO・電化・水素の3つの脱炭素手段の比較イメージ')


def b_feedstock():
    b = [_band()]
    b.append(drum(230, 182, 1.5, SAND, WHITE, GREY2))
    b.append(drum(390, 182, 1.5, MID, WHITE))
    b.append(f'<path d="M640,376 c0,-86 74,-146 172,-152 6,92 -66,152 -172,152 Z" fill="{BRAND}"/>')
    b.append(f'<path d="M662,366 C724,330 772,290 806,238" stroke="{WHITE}" stroke-width="7" '
             f'opacity=".7" fill="none" stroke-linecap="round"/>')
    b.append(factory(1150, 176, 1.0))
    b.append(f'<path d="M900,300 h150 m-26,-22 l26,22 -26,22" stroke="{DEEP}" stroke-width="11" '
             f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(f'<path d="M540,300 h60 m-16,-14 l16,14 -16,14" stroke="{DEEP}" stroke-width="9" '
             f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return svg(BW, BH, '\n'.join(b), '廃食油や植物油などの原料から製造にいたる流れのイメージ')


def b_certification():
    b = [_flat()]
    b.append(sheet(330, 104, 1.5, DEEP, 4, 150, 200))
    b.append(sheet(580, 128, 1.35, BRAND, 4, 150, 200))
    b.append(badge(900, 120, 1.7))
    b.append(f'<path d="M820,250 h56 m-14,-12 l14,12 -14,12" stroke="{MID}" stroke-width="9" '
             f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return svg(BW, BH, '\n'.join(b), 'ISCC認証とPoSなど証憑のイメージ')


def b_standards():
    b = [_flat()]
    b.append(sheet(300, 96, 1.5, BRAND, 5, 150, 200))
    b.append(sheet(560, 120, 1.35, DEEP, 4, 150, 200))
    b.append(sheet(800, 144, 1.2, MID, 4, 150, 200))
    b.append(f'<rect x="1040" y="206" width="300" height="34" rx="17" fill="{WHITE}"/>')
    for i in range(11):
        b.append(f'<rect x="{1062+i*26}" y="206" width="5" height="{20 if i % 3 else 34}" fill="{GREY2}"/>')
    b.append(f'<rect x="1040" y="282" width="190" height="14" rx="7" fill="{ACCENT}"/>')
    return svg(BW, BH, '\n'.join(b), '燃料品質規格と制度上の位置づけのイメージ')


def b_guide():
    b = [_flat()]
    b.append(sheet(220, 118, 1.35, DEEP, 4, 150, 200))
    b.append(stepdots(540, 190, 1.7, 5, 0, 110))
    return svg(BW, BH, '\n'.join(b), '導入判断の5段階を示すイメージ')


def b_ghg():
    b = [_flat()]
    b.append(cloud(230, 110, 1.8, WHITE, .95))
    b.append(f'<g transform="translate(640,120)">'
             f'<rect width="320" height="236" rx="10" fill="{WHITE}"/>'
             f'<rect x="54" y="46" width="74" height="162" rx="6" fill="{MID}"/>'
             f'<rect x="196" y="128" width="74" height="80" rx="6" fill="{ACCENT}"/>'
             f'<rect x="30" y="212" width="260" height="6" rx="3" fill="{GREY}"/></g>')
    b.append(f'<path d="M1040,180 v100 m-24,-26 l24,26 24,-26" stroke="{DEEP}" stroke-width="12" '
             f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(chart(1140, 150, 1.2, (58, 104, 80, 142), 3))
    return svg(BW, BH, '\n'.join(b), 'GHG削減量の試算のイメージ')


def b_cost():
    b = [_flat()]
    b.append(sheet(300, 104, 1.5, BRAND, 5, 150, 200))
    b.append(f'<g transform="translate(610,130) scale(1.45)">'
             f'<rect width="150" height="190" rx="10" fill="{WHITE}"/>'
             f'<rect x="18" y="18" width="114" height="40" rx="5" fill="{SKY2}"/>'
             + ''.join(f'<rect x="{18+c*40}" y="{74+r*34}" width="30" height="26" rx="5" '
                       f'fill="{ACCENT if (r, c) == (2, 2) else MID}"/>'
                       for r in range(3) for c in range(3)) + '</g>')
    b.append(f'<path d="M1010,180 h130 l76,76 -98,98 -76,-76 z" fill="{DEEP}"/>')
    b.append(f'<circle cx="1058" cy="228" r="15" fill="{WHITE}"/>')
    return svg(BW, BH, '\n'.join(b), '見積条件と価格決定要素のイメージ')


def b_supply():
    b = [_band()]
    b.append(tanker(120, 198, 0.9))
    b.append(drum(530, 246, 1.0))
    b.append(drum(630, 246, 1.0, DEEP))
    b.append(tank(800, 226, 1.0))
    b.append(ship(1110, 226, 0.84))
    return svg(BW, BH, '\n'.join(b), 'ローリー・ドラム缶・既存タンク・船舶による供給方法のイメージ')


def b_equipment():
    b = [_band()]
    b.append(excavator(180, 198, 1.0))
    b.append(clipboard(700, 136, 1.4))
    b.append(truck(1010, 198, 0.9))
    return svg(BW, BH, '\n'.join(b), '車両・設備の仕様を確認するイメージ')


def b_tax():
    b = [_flat()]
    b.append(sheet(300, 104, 1.5, DEEP, 5, 150, 200))
    b.append(seal(590, 196, 1.2))
    b.append(f'<rect x="830" y="196" width="20" height="160" fill="{GREY2}"/>')
    b.append(f'<rect x="762" y="138" width="156" height="72" rx="10" fill="{WHITE}"/>')
    b.append(f'<rect x="762" y="138" width="156" height="72" rx="10" fill="none" stroke="{DEEP}" stroke-width="6"/>')
    b.append(f'<rect x="788" y="166" width="104" height="14" rx="7" fill="{DEEP}"/>')
    b.append(truck(1010, 198, 0.9))
    return svg(BW, BH, '\n'.join(b), '公道走行時の税務上の取扱いのイメージ')


def b_flow():
    b = [_flat()]
    b.append(stepdots(250, 186, 1.85, 5, 4, 125))
    for i in range(5):
        b.append(f'<rect x="{264+i*231}" y="332" width="130" height="14" rx="7" '
                 f'fill="{ACCENT if i == 4 else MID}"/>')
    return svg(BW, BH, '\n'.join(b), '初回相談から本導入までの流れのイメージ')


def b_contact():
    b = [_flat()]
    b.append(sheet(330, 116, 1.45, BRAND, 5, 150, 190))
    b.append(f'<path d="M700,136 h400 a18,18 0 0 1 18,18 v148 a18,18 0 0 1 -18,18 h-260 '
             f'l-62,48 v-48 h-78 a18,18 0 0 1 -18,-18 v-148 a18,18 0 0 1 18,-18 Z" fill="{WHITE}"/>')
    b.append(f'<rect x="740" y="184" width="250" height="16" rx="8" fill="{SKY2}"/>')
    b.append(f'<rect x="740" y="224" width="310" height="16" rx="8" fill="{SKY2}"/>')
    b.append(f'<rect x="740" y="264" width="180" height="16" rx="8" fill="{ACCENT}"/>')
    return svg(BW, BH, '\n'.join(b), 'お問い合わせと初期相談のイメージ')


def b_glossary():
    b = [_flat()]
    b.append(f'<g transform="translate(400,96) scale(1.5)">'
             f'<rect width="480" height="250" rx="10" fill="{WHITE}"/>'
             f'<rect x="232" y="0" width="16" height="250" fill="{SKY2}"/>'
             + ''.join(f'<rect x="{34+c*250}" y="{54+r*44}" width="{166-r*22}" height="11" rx="5" '
                       f'fill="{SKY2}"/>' for r in range(4) for c in range(2))
             + f'<rect width="480" height="28" rx="10" fill="{DEEP}"/>'
             + ''.join(f'<rect x="488" y="{54+i*58}" width="34" height="44" rx="6" '
                       f'fill="{ACCENT if i == 1 else MID}"/>' for i in range(3)) + '</g>')
    return svg(BW, BH, '\n'.join(b), 'HVO・脱炭素に関する用語集のイメージ')


# ------------------------------------------------------------------ カード／サムネイル
def c_land():
    hz = 340
    b = [sky(CW, CH, hz), hills(CW, hz), trees([60, 720], hz, 1.1),
         f'<rect y="{hz}" width="{CW}" height="{CH-hz}" fill="#DCE7E2"/>',
         f'<rect y="{hz+22}" width="{CW}" height="{CH-hz-22}" fill="{GREY}"/>']
    b.append(train(90, 218, 0.78))
    b.append(truck(360, 202, 0.78))
    return svg(CW, CH, '\n'.join(b), '陸上の輸送（鉄道とトラック）のイラスト')


def c_sea():
    hz = 330
    b = [sky(CW, CH, hz), hills(CW, hz), f'<rect y="{hz}" width="{CW}" height="{CH-hz}" fill="#AFD2D6"/>']
    for i in range(5):
        b.append(f'<rect x="{-10+i*170}" y="{hz+46+(i%3)*26}" width="130" height="8" rx="4" '
                 f'fill="{WHITE}" opacity=".5"/>')
    b.append(ship(180, 180, 0.86))
    return svg(CW, CH, '\n'.join(b), '海上輸送（内航船）のイラスト')


def c_air():
    b = [f'<rect width="{CW}" height="{CH}" fill="{SKY}"/>',
         cloud(70, 90, 1.2, WHITE, .85), cloud(560, 330, 1.0, WHITE, .6)]
    b.append(plane(210, 160, 1.2))
    return svg(CW, CH, '\n'.join(b), '航空分野（バイオジェット燃料）のイラスト')


def t_tech():
    b = [f'<rect width="{TW}" height="{TH}" fill="{SKY}"/>']
    b.append(generator(100, 180, 1.0))
    b.append(chart(430, 120, 1.1, (54, 96, 72, 128), 3))
    return svg(TW, TH, '\n'.join(b), '実証・技術検証のイメージイラスト')


def t_news():
    b = [f'<rect width="{TW}" height="{TH}" fill="{SKY}"/>']
    b.append(sheet(130, 80, 1.5, DEEP, 4, 150, 200))
    b.append(factory(430, 150, 0.95))
    return svg(TW, TH, '\n'.join(b), 'ニュース・活動情報のイメージイラスト')


FILES2 = {
    'about-products.svg':        (b_products(),        'サステオ100とサステオ51の製品イメージ'),
    'about-fuel-compare.svg':    (b_fuel_compare(),    'HVO・FAME・軽油の3種類を並べた比較イメージ'),
    'about-measure-compare.svg': (b_measure_compare(), 'HVO・電化・水素の3つの脱炭素手段の比較イメージ'),
    'about-feedstock.svg':       (b_feedstock(),       '廃食油や植物油などの原料から製造にいたる流れのイメージ'),
    'about-certification.svg':   (b_certification(),   'ISCC認証とPoSなど証憑のイメージ'),
    'about-standards.svg':       (b_standards(),       '燃料品質規格と制度上の位置づけのイメージ'),
    'adopt-guide.svg':           (b_guide(),           '導入判断の5段階を示すイメージ'),
    'adopt-ghg.svg':             (b_ghg(),             'GHG削減量の試算のイメージ'),
    'adopt-cost.svg':            (b_cost(),            '見積条件と価格決定要素のイメージ'),
    'adopt-supply.svg':          (b_supply(),          'ローリー・ドラム缶・既存タンク・船舶による供給方法のイメージ'),
    'adopt-equipment.svg':       (b_equipment(),       '車両・設備の仕様を確認するイメージ'),
    'adopt-tax.svg':             (b_tax(),             '公道走行時の税務上の取扱いのイメージ'),
    'adopt-flow.svg':            (b_flow(),            '初回相談から本導入までの流れのイメージ'),
    'know-glossary.svg':         (b_glossary(),        'HVO・脱炭素に関する用語集のイメージ'),
    'company-land.svg':          (c_land(),            '陸上の輸送（鉄道とトラック）のイラスト'),
    'company-sea.svg':           (c_sea(),             '海上輸送（内航船）のイラスト'),
    'company-air.svg':           (c_air(),             '航空分野（バイオジェット燃料）のイラスト'),
    'post-tech.svg':             (t_tech(),            '実証・技術検証のイメージイラスト'),
    'post-news.svg':             (t_news(),            'ニュース・活動情報のイメージイラスト'),
}


def b_use(kind):
    """用途ページの帯（16:5）。TOPのカードと同じ題材を横長で組み直す。"""
    hz = BHZ
    if kind == 'logistics':
        b = [_band(), trees([120, 220, 1420, 1510], hz, 1.4)]
        for x in range(20, BW, 150):
            b.append(f'<rect x="{x}" y="{hz+84}" width="76" height="9" rx="4" fill="{WHITE}" opacity=".8"/>')
        b.append(truck(430, 198, 1.0))
        lab = '幹線輸送のトラックのイラスト'
    elif kind == 'construction':
        b = [_band(ground='#E3DACB', top=SAND)]
        b.append(f'<path d="M1120,{hz+18} c70,-56 170,-48 240,8 L1600,{hz+18} Z" fill="#CDBEA4"/>')
        b.append(f'<path d="M190,{hz+96} c28,-62 160,-62 190,0 Z" fill="#CDBEA4"/>')
        b.append(excavator(600, 198, 1.05))
        lab = '建設現場で稼働する油圧ショベルのイラスト'
    elif kind == 'port':
        b = [_band(ground='#BBD9DA', top='#BBD9DA')]
        for i in range(7):
            b.append(f'<rect x="{60+i*220}" y="{hz+56+(i%2)*22}" width="150" height="9" rx="4" '
                     f'fill="{WHITE}" opacity=".5"/>')
        b.append(crane(430, 126, 1.0))
        for i, c in enumerate([BRAND, DEEP, MID, ACCENT]):
            b.append(f'<rect x="{1080+(i%2)*92}" y="{300+(i//2)*40}" width="86" height="38" fill="{c}"/>')
        lab = '港湾のコンテナクレーンと荷役のイラスト'
    elif kind == 'marine':
        b = [_band(ground='#AFD2D6', top='#AFD2D6')]
        for i in range(8):
            b.append(f'<rect x="{-20+i*210}" y="{hz+48+(i%3)*28}" width="160" height="9" rx="4" '
                     f'fill="{WHITE}" opacity=".5"/>')
        b.append(ship(540, 226, 1.0))
        lab = '内航船のイラスト'
    elif kind == 'generator':
        b = [_band(), trees([1420, 1510], hz, 1.3)]
        b.append(generator(620, 224, 1.0))
        b.append(drum(400, 246, 1.0))
        b.append(drum(500, 246, 1.0, DEEP))
        b.append(f'<path d="M940,300 h120 m-22,-18 l22,18 -22,18" stroke="{DEEP}" stroke-width="9" '
                 f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        b.append(excavator(1120, 198, 0.8))
        lab = '仮設電源として使われるディーゼル発電機のイラスト'
    elif kind == 'shipper':
        b = [_band()]
        b.append(warehouse(600, 186, 1.0))
        b.append(truck(130, 198, 0.86))
        b.append(truck(1090, 198, 0.86))
        lab = '物流センターと委託輸送のイラスト'
    else:
        b = [_band()]
        b.append(factory(560, 176, 1.0))
        b.append(tank(240, 226, 1.0))
        b.append(drum(1060, 246, 1.0))
        b.append(drum(1160, 246, 1.0, DEEP))
        lab = '工場のボイラー設備のイラスト'
    return svg(BW, BH, '\n'.join(b), lab)


def b_faq():
    b = [_flat()]
    b.append(f'<path d="M330,120 h400 a18,18 0 0 1 18,18 v150 a18,18 0 0 1 -18,18 h-290 '
             f'l-66,50 v-50 h-44 a18,18 0 0 1 -18,-18 v-150 a18,18 0 0 1 18,-18 Z" fill="{WHITE}"/>')
    b.append(f'<rect x="372" y="170" width="260" height="16" rx="8" fill="{SKY2}"/>')
    b.append(f'<rect x="372" y="212" width="310" height="16" rx="8" fill="{SKY2}"/>')
    b.append(f'<rect x="372" y="254" width="200" height="16" rx="8" fill="{SKY2}"/>')
    b.append(f'<path d="M880,180 h380 a18,18 0 0 1 18,18 v140 a18,18 0 0 1 -18,18 h-250 '
             f'l-60,46 v-46 h-70 a18,18 0 0 1 -18,-18 v-140 a18,18 0 0 1 18,-18 Z" fill="{BRAND}"/>')
    b.append(f'<rect x="920" y="226" width="250" height="16" rx="8" fill="{WHITE}" opacity=".9"/>')
    b.append(f'<rect x="920" y="268" width="170" height="16" rx="8" fill="{WHITE}" opacity=".62"/>')
    return svg(BW, BH, '\n'.join(b), 'よくある質問のイメージ')


for _k in ('logistics', 'construction', 'port', 'marine', 'generator', 'shipper', 'manufacturing'):
    _svg = b_use(_k)
    FILES2[f'sol-{_k}.svg'] = (_svg, _svg.split('aria-label="')[1].split('"')[0])
FILES2['know-faq.svg'] = (b_faq(), 'よくある質問のイメージ')


def t_fuel():
    """HVO・FAME・軽油の3本（16:9）。"""
    hz = 330
    b = [sky(TW, TH, hz), hills(TW, hz),
         f'<rect y="{hz}" width="{TW}" height="{TH-hz}" fill="#DCE7E2"/>',
         f'<rect y="{hz+16}" width="{TW}" height="{TH-hz-16}" fill="{GREY}"/>']
    for i, (col, cap) in enumerate([(BRAND, DEEP), (MID, DEEP), (GREY2, INK)]):
        b.append(drum(150 + i * 200, 200, 1.0, col, WHITE, cap))
    return svg(TW, TH, '\n'.join(b), 'HVO・FAME・軽油を比べるイメージイラスト')


def t_law():
    """制度・法令（16:9）。"""
    b = [f'<rect width="{TW}" height="{TH}" fill="{SKY}"/>',
         f'<rect y="{TH-70}" width="{TW}" height="70" fill="{SKY2}"/>']
    b.append(sheet(150, 70, 1.3, DEEP, 5, 150, 200))
    b.append(sheet(360, 96, 1.15, BRAND, 4, 150, 200))
    b.append(seal(560, 180, 1.0))
    return svg(TW, TH, '\n'.join(b), '制度・法令の解説のイメージイラスト')


FILES2['post-fuel.svg'] = (t_fuel(), 'HVO・FAME・軽油を比べるイメージイラスト')
FILES2['post-law.svg'] = (t_law(), '制度・法令の解説のイメージイラスト')

if __name__ == '__main__':
    import pathlib, sys
    out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for name, (content, _) in FILES2.items():
        (out / name).write_text(content, encoding='utf-8')
    print(f'{len(FILES2)} illustrations -> {out}')
