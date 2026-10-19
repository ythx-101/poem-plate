#!/usr/bin/env python3
"""poem-plate compose: AI-drawn plate -> 1500x2000 (3:4), paper/ink/gold soft map, vertical CJK text.

Features:
- frame crop is optional (no rule -> keep whole image)
- FEATHER lowered to 28, and the outer band of the plate has its light mid-greys
  lifted to paper so cut edges never read as a grey pasted rectangle
- shared series skeleton: fixed text top / signature baseline, gold series tag
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1500, 2000
PAPER = np.array([0xF5, 0xF4, 0xED], np.float32)
INK = np.array([0x14, 0x14, 0x13], np.float32)
GOLD = np.array([0xB8, 0x89, 0x3A], np.float32)
LGOLD = np.array([0xD4, 0xAF, 0x6A], np.float32)
import os
# Any CJK serif font works; Noto Serif SC Light is the reference look.
FONT_PATH = os.environ.get("POEM_FONT", "NotoSerifSC-Light.otf")
SIGNATURE = os.environ.get("POEM_SIGNATURE", "青月")   # vertical name at lower left
HANDLE = os.environ.get("POEM_HANDLE", "@YuLin807")    # rotated handle under the name

# Series skeleton (identical on all four plates)
MARGIN = 600          # text zone width on the left
RIGHT_PAD = 24
TEXT_RIGHT = 540      # rightmost text column edge
TEXT_TOP = 230
SIG_BOTTOM = 1790     # bottom of the handle
FEATHER = 28
EDGE_BAND = 70
TAG_SIZE, TAG_STEP = 24, 36

BIG = (64, 92, 80)    # size, step, column width   (回目)
MID = (50, 72, 66)    # 判词 / 原话
SMALL = (26, 40, 42)  # 出处
SIG = (48, 70, 62)


def soft_map(im):
    arr = np.asarray(im).astype(np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    y = 0.299 * r + 0.587 * g + 0.114 * b
    y_paper = float(np.median(y[:, 40:180]))
    hi = y_paper - 8.0
    lo = 10.0
    t = np.clip((y - lo) / (hi - lo), 0.0, 1.0)
    base = INK * (1.0 - t)[..., None] + PAPER * t[..., None]
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    chroma = mx - mn
    safe = np.where(chroma < 1.0, 1.0, chroma)
    hue = np.zeros_like(r)
    hue = np.where(mx == r, ((g - b) / safe) % 6.0, hue)
    hue = np.where((mx == g) & (mx != r), ((b - r) / safe) + 2.0, hue)
    hue = np.where((mx != r) & (mx != g), ((r - g) / safe) + 4.0, hue)
    hue = (hue * 60.0) % 360.0
    hue_score = np.clip(1.0 - np.abs(hue - 41.0) / 18.0, 0.0, 1.0)
    chroma_score = np.clip((chroma - 30.0) / 16.0, 0.0, 1.0)
    warm = np.clip((r - b - 14.0) / 18.0, 0.0, 1.0)
    lit = np.clip((y - 40.0) / 30.0, 0.0, 1.0)
    gold_w = hue_score * chroma_score * warm * lit
    strong = gold_w > 0.55
    if int(strong.sum()) > 50:
        y_lo = float(np.percentile(y[strong], 8))
        y_hi = float(np.percentile(y[strong], 92))
    else:
        y_lo, y_hi = 100.0, 200.0
    tg = np.clip((y - y_lo) / max(1.0, y_hi - y_lo), 0.0, 1.0)
    gold_col = GOLD * (1.0 - tg)[..., None] + LGOLD * tg[..., None]
    out = base * (1.0 - gold_w)[..., None] + gold_col * gold_w[..., None]
    return np.clip(out, 0, 255).astype(np.uint8), gold_w


def _sprite(text, size, rotate_deg=0, pad=6):
    scale = 4
    font = ImageFont.truetype(FONT_PATH, size * scale)
    bbox = font.getbbox(text)
    p = pad * scale
    g = Image.new("L", (max(1, bbox[2] - bbox[0] + 2 * p), max(1, bbox[3] - bbox[1] + 2 * p)), 0)
    ImageDraw.Draw(g).text((p - bbox[0], p - bbox[1]), text, font=font, fill=255)
    if rotate_deg:
        g = g.rotate(rotate_deg, expand=True, resample=Image.Resampling.BICUBIC)
    g = g.resize((max(1, round(g.width / scale)), max(1, round(g.height / scale))), Image.Resampling.LANCZOS)
    return np.asarray(g)


def glyph(ch, size):
    if ch in "《》〈〉":
        return _sprite(ch, size, -90)
    if ch in "·":
        return _sprite("・", size)
    return _sprite(ch, size)


def blit(rgb, gray, cx, cy, color=INK):
    sh, sw = gray.shape
    x0 = int(round(cx - sw / 2)); y0 = int(round(cy - sh / 2))
    sx0, sy0 = max(0, -x0), max(0, -y0)
    dx0, dy0 = max(0, x0), max(0, y0)
    dx1, dy1 = min(W, x0 + sw), min(H, y0 + sh)
    foot = np.zeros((H, W), np.uint8)
    if dx1 <= dx0 or dy1 <= dy0:
        return foot
    src = gray[sy0:sy0 + (dy1 - dy0), sx0:sx0 + (dx1 - dx0)]
    cov = src.astype(np.float32) / 255.0
    reg = rgb[dy0:dy1, dx0:dx1].astype(np.float32)
    rgb[dy0:dy1, dx0:dx1] = np.clip(reg * (1 - cov)[..., None] + color * cov[..., None], 0, 255).astype(np.uint8)
    foot[dy0:dy1, dx0:dx1] = src
    return foot


def column(rgb, text, size, step, cx, top, color=INK):
    foot = np.zeros((H, W), np.uint8)
    for i, ch in enumerate(text):
        if ch in "\u3000 ":
            continue
        foot = np.maximum(foot, blit(rgb, glyph(ch, size), cx, top + i * step + step / 2.0, color))
    return foot


def place_text(rgb, columns, tag):
    """columns: list of (text, kind, gap_after). Right to left. Signature column is last, auto."""
    dist = np.linalg.norm(rgb.astype(np.float32) - PAPER, axis=2)
    art = dist > 14.0
    dil = np.asarray(Image.fromarray(art.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(45))) > 0
    kinds = {"big": BIG, "mid": MID, "small": SMALL}
    cursor = TEXT_RIGHT
    foot = np.zeros((H, W), np.uint8)
    log = []
    for text, kind, gap in columns:
        size, step, cw = kinds[kind]
        cx = cursor - cw / 2
        top = TEXT_TOP if kind != "small" else TEXT_TOP + 8
        foot = np.maximum(foot, column(rgb, text, size, step, cx, top))
        log.append(f"cx={cx:.0f} {text}  bottom={top + len(text) * step:.0f}")
        cursor -= cw + gap
    # signature column: gold series tag at top, SIGNATURE + handle at the bottom
    size, step, cw = SIG
    cx = 115.0  # fixed signature/tag column across the series
    handle = _sprite(HANDLE, 24, -90, pad=8)
    hy_bottom = SIG_BOTTOM
    hy = hy_bottom - handle.shape[0] / 2
    sig_top = hy_bottom - handle.shape[0] - 16 - 2 * step
    foot = np.maximum(foot, column(rgb, SIGNATURE, size, step, cx, sig_top))
    foot = np.maximum(foot, blit(rgb, handle, cx, hy))
    foot = np.maximum(foot, column(rgb, tag, TAG_SIZE, TAG_STEP, cx, TEXT_TOP + 8, GOLD))
    log.append(f"cx={cx:.0f} sig top={sig_top:.0f} tag={tag}")
    left = cx - cw / 2
    hit = int(((foot > 40) & dil).sum())
    for l in log:
        print("  ", l)
    if hit:
        raise SystemExit(f"text overlaps the drawing ({hit} px)")
    if left < 40:
        raise SystemExit(f"text runs off the left edge ({left:.0f})")
    print(f"text block x {left:.0f}..{TEXT_RIGHT}")
    return rgb


def crop_frame(arr):
    y = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    h, w = y.shape
    def find(lines, test):
        for i in lines:
            if test(i):
                return i
        return None
    L = find(range(0, 40), lambda x: (y[:, x] < 90).mean() > 0.7)
    R = find(range(w - 1, w - 41, -1), lambda x: (y[:, x] < 90).mean() > 0.7)
    T = find(range(0, 40), lambda i: (y[i, :] < 90).mean() > 0.7)
    B = find(range(h - 1, h - 41, -1), lambda i: (y[i, :] < 90).mean() > 0.7)
    box = [(L + 6) if L is not None else 0, (T + 6) if T is not None else 0,
           (R - 4) if R is not None else w, (B - 4) if B is not None else h]
    print(f"frame L{L} T{T} R{R} B{B} -> {box}")
    return arr[box[1]:box[3], box[0]:box[2]]


def paper_median(arr):
    h, w = arr.shape[:2]
    patches = [arr[10:60, 10:60], arr[10:60, w - 60:w - 10], arr[h - 60:h - 10, 10:60], arr[h // 2 - 25:h // 2 + 25, 10:60]]
    meds = [np.median(p.reshape(-1, 3), axis=0) for p in patches]
    ys = [0.299 * m[0] + 0.587 * m[1] + 0.114 * m[2] for m in meds]
    return meds[int(np.argmax(ys))]


def flatten_paper(arr, bleed=()):
    med = paper_median(arr)
    dist = np.linalg.norm(arr - med, axis=2)
    y = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    keep = np.clip((dist - 9.0) / 12.0, 0.0, 1.0)
    keep = np.where(y < 185.0, 1.0, keep)
    out = arr * keep[..., None] + PAPER * (1.0 - keep)[..., None]
    # Lift the light greys near the cut edges toward paper (the old grey-fringe fault).
    h, w = arr.shape[:2]
    edge = _edge(h, w, bleed)
    band = np.clip(1.0 - edge / EDGE_BAND, 0.0, 1.0)
    yo = 0.299 * out[:, :, 0] + 0.587 * out[:, :, 1] + 0.114 * out[:, :, 2]
    light = np.clip((yo - 150.0) / 60.0, 0.0, 1.0)      # only pale greys, never ink
    lift = (band * light)[..., None]
    out = out * (1 - lift) + PAPER * lift
    print(f"paper median {med.round(1)}, flattened {(keep < 0.05).mean():.1%}")
    return out


def _edge(h, w, bleed=()):
    big = 1e6
    xx = np.arange(w, dtype=np.float32)[None, :]
    yy = np.arange(h, dtype=np.float32)[:, None]
    l = xx if "left" not in bleed else xx * 0 + big
    r = (w - 1.0 - xx) if "right" not in bleed else xx * 0 + big
    t = yy if "top" not in bleed else yy * 0 + big
    b = (h - 1.0 - yy) if "bottom" not in bleed else yy * 0 + big
    return np.minimum(np.minimum(l, r), np.minimum(t, b))


def feather(arr, bleed=()):
    h, w = arr.shape[:2]
    edge = _edge(h, w, bleed)
    t = np.clip(edge / FEATHER, 0.0, 1.0)
    t = t * t * (3 - 2 * t)
    return arr * t[..., None] + PAPER * (1 - t)[..., None]


def edge_ink_report(arr):
    """How much real ink touches each border of the plate (subject cut-off check)."""
    y = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    dark = y < 120
    r = {"top": dark[:6].mean(), "bottom": dark[-6:].mean(), "left": dark[:, :6].mean(), "right": dark[:, -6:].mean()}
    print("edge ink:", {k: f"{v:.1%}" for k, v in r.items()})
    return r


def place(arr, crop_left_auto=True, scale_cap=None, valign="center", scale=None, oy=None, ox=None):
    h, w = arr.shape[:2]
    dist = np.linalg.norm(arr - PAPER, axis=2)
    content = dist > 16.0
    xs = np.where(content.mean(axis=0) > 0.008)[0]
    cl = int(xs[0]) if crop_left_auto else 0
    s = min((W - MARGIN) / max(1, w - cl), (H - 40) / h)
    if scale_cap:
        s = min(s, scale_cap)
    manual = scale is not None
    if manual:
        s = scale
    nw, nh = round(w * s), round(h * s)
    if ox is None:
        ox = W - RIGHT_PAD - nw
    if ox == "bleed":
        ox = W - nw
    if oy is None:
        oy = (H - nh) // 2 if valign == "center" else H - nh - 20
    pl = ox + cl * nw / w
    print(f"scale {s:.3f} {nw}x{nh} at {ox},{oy}; content left {pl:.0f}")
    if not manual and pl < MARGIN - 8:
        raise SystemExit(f"content enters text margin ({pl:.0f})")
    src = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB").resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (W, H), tuple(int(v) for v in PAPER))
    canvas.paste(src, (ox, oy))  # PIL clips anything beyond the canvas
    return np.asarray(canvas).astype(np.float32)


def compose(src, out, columns, tag, bleed=(), **kw):
    arr = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
    arr = crop_frame(arr)
    edge_ink_report(arr)
    plate = feather(flatten_paper(arr, bleed), bleed)
    up = place(plate, **kw)
    rgb, gw = soft_map(up)
    print(f"gold weight mean {gw.mean():.3%}")
    rgb = place_text(rgb, columns, tag)
    for pt in ((8, 8), (8, 400), (40, 1600), (1490, 8), (1490, 1990)):
        px = tuple(int(v) for v in rgb[pt[1], pt[0]])
        if max(abs(a - b) for a, b in zip(px, PAPER)) > 3:
            print(f"WARN background at {pt} is {px}")
    Image.fromarray(rgb, "RGB").save(out, "PNG")
    print("wrote", out)
