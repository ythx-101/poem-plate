"""Example: compose one plate. Usage: python example_compose.py plate.jpg out.png
If it reports the drawing enters the text margin, lower scale_cap (or pass scale=...)."""
import sys
from compose_lib import compose

# Columns run right to left: (text, kind, gap_after). kind = big | mid | small.
COLUMNS = [
    ("懒起画蛾眉\u3000弄妆梳洗迟", "big", 10),
    ("照花前后镜\u3000花面交相映", "big", 8),
    ("温庭筠《菩萨蛮》", "small", 36),
]
compose(sys.argv[1], sys.argv[2], COLUMNS, "诗画\u3000·\u3000其一", scale_cap=1.1)
