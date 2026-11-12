"""Minimal smoke test. Usage: POEM_FONT=/path/to/chinese-font.otf python tests/smoke_test.py"""
import os
import sys
import tempfile
from pathlib import Path

font = os.environ.get("POEM_FONT")
if not font or not Path(font).is_file():
    print("skip: set POEM_FONT to a Chinese font file")
    sys.exit(0)

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

from PIL import Image
from compose_lib import compose

COLUMNS = [
    ("懒起画蛾眉　弄妆梳洗迟", "big", 10),
    ("照花前后镜　花面交相映", "big", 8),
    ("温庭筠《菩萨蛮》", "small", 36),
]

with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "out.png"
    compose(str(root / "examples" / "xinfu-raw.jpg"), str(out), COLUMNS, "诗画　·　其一", scale_cap=1.1)
    assert out.exists(), "output not written"
    im = Image.open(out).convert("RGB")
    assert im.size == (1500, 2000), f"unexpected size {im.size}"
    px = im.getpixel((8, 8))
    assert all(abs(a - b) <= 3 for a, b in zip(px, (0xF5, 0xF4, 0xED))), f"background {px}"
print("OK")
