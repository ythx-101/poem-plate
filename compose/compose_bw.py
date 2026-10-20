#!/usr/bin/env python3
"""不守规矩的女人 series: reuse honglou-maids/compose_lib (series skeleton) + petal cleanup + 4:5 export."""
import sys, json
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import numpy as np
from PIL import Image
from scipy import ndimage
import compose_lib as L

D = '.'
TAG = '不守规矩的女人\u3000·\u3000其{}'
SP = '\u3000'
PLATES = {
 'qingqing': dict(n='一', src='qingqing/c7_fix.png', clean_x=250,
   cols=[(f'昔为倡家女{SP}今为荡子妇','mid',10),(f'荡子行不归{SP}空床难独守','mid',14),('《古诗十九首·青青河畔草》','small',0)],
   kw=dict(bleed=('right','bottom','top'), scale=1.70, ox=140, oy=-20)),
 'sidixiang': dict(n='二', src='sidixiang/c5_fix.png', clean_x=330, erase=[(230,122,322,185)],
   cols=[(f'春日游{SP}杏花吹满头','mid',10),(f'陌上谁家年少{SP}足风流','mid',10),(f'妾拟将身嫁与{SP}一生休','mid',10),(f'纵被无情弃{SP}不能羞','mid',14),('韦庄《思帝乡》','small',0)],
   kw=dict(bleed=('right','top','bottom'), scale=1.68, ox=10, oy=-16)),
 'qianchang': dict(n='三', src='qianchang/c1_fix5.png', clean_x=520,
   cols=[(f'子惠思我{SP}褰裳涉溱','mid',10),(f'子不我思{SP}岂无他人','mid',10),('狂童之狂也且','mid',14),('《诗经·郑风·褰裳》','small',0)],
   kw=dict(bleed=('right','bottom'), scale=1.85, ox=1500-round(896*1.85)+60, oy=-80)),
 'yuxuanji': dict(n='四', src='yuxuanji/c5.png', clean_x=330,
   cols=[(f'羞日遮罗袖{SP}愁春懒起妆','mid',10),(f'易求无价宝{SP}难得有心郎','mid',10),(f'枕上潜垂泪{SP}花间暗断肠','mid',10),(f'自能窥宋玉{SP}何必恨王昌','mid',14),('鱼玄机《赠邻女》','small',0)],
   kw=dict(bleed=('right','bottom'), scale=1.70, ox=1500-round(896*1.70), oy=-20)),
}

HALF = 0.5   # the full-width space between two half-lines advances only half a step


def column_tight(rgb, text, size, step, cx, top, color=L.INK):
    foot = np.zeros((L.H, L.W), np.uint8)
    y = top
    for ch in text:
        if ch in "\u3000 ":
            y += step * HALF
            continue
        foot = np.maximum(foot, L.blit(rgb, L.glyph(ch, size), cx, y + step / 2.0, color))
        y += step
    return foot


L.column = column_tight


def clean_petals(src, out, clean_x, max_area=2500, erase=()):
    a = np.asarray(Image.open(src).convert('RGB')).astype(np.float32)
    med = L.paper_median(a)
    for (x0, y0, x1, y1) in erase:   # trim stray branch tips that reach into the text zone
        a[y0:y1, x0:x1] = med
    ink = np.linalg.norm(a - med, axis=2) > 30
    lab, n = ndimage.label(ink)
    if n == 0:
        Image.fromarray(a.astype(np.uint8)).save(out); return 0
    idx = np.arange(1, n + 1)
    area = ndimage.sum(ink, lab, idx)
    com = ndimage.center_of_mass(ink, lab, idx)
    rb = a[..., 0] - a[..., 2]
    mrb = ndimage.mean(rb, lab, idx)
    # only gold blobs (falling petals/leaves); never dark ink (eyes, brows, hair strands)
    kill = [i for i, ar, c, g in zip(idx, area, com, mrb) if ar < max_area and c[1] < clean_x and g > 35]
    m = np.isin(lab, kill)
    m = ndimage.binary_dilation(m, iterations=3)
    a[m] = med
    Image.fromarray(a.astype(np.uint8)).save(out)
    return len(kill)

def run(name, p):
    clean = f'{D}/{name}/plate_clean.png'
    k = clean_petals(f"{D}/{p['src']}", clean, p['clean_x'], erase=p.get('erase', ()))
    print(name, 'removed', k, 'small blobs')
    out = f'{D}/{name}/final_3x4.png'
    L.compose(clean, out, p['cols'], TAG.format(p['n']), **p['kw'])
    im = Image.open(out)
    im.crop((0, 60, 1500, 1935)).resize((1080, 1350), Image.LANCZOS).save(f'{D}/{name}/final_4x5.png')

if __name__ == '__main__':
    names = sys.argv[1:] or list(PLATES)
    for nme in names:
        run(nme, PLATES[nme])
