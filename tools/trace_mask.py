"""
Trace the shirt mask (tools/body-mask.png, made by process_assets.py) into a compact SVG path and print a
CSS-ready data URI. The SVG is used as `mask-image` for the front "PORTFOLIO" layer.
Usage: python3 tools/trace_mask.py tools/body-mask.png 960 988
(then paste the printed data URI into --shirt-mask in css/main.css)
"""
import sys, urllib.parse
import numpy as np, cv2
from PIL import Image

src, W, H = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
a = np.asarray(Image.open(src).convert('RGBA'))[..., 3]
a = cv2.resize(a, (W, H), interpolation=cv2.INTER_CUBIC)
mb = (a > 127).astype(np.uint8)
cnts, hier = cv2.findContours(mb, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
parts = []
for c in cnts:
    if cv2.contourArea(c) < 60:
        continue
    ap = cv2.approxPolyDP(c, 1.1, True).reshape(-1, 2)
    if len(ap) < 3:
        continue
    d = 'M' + ' '.join(f'{x} {y}' for x, y in ap) + 'Z'
    parts.append(d)
path = ''.join(parts)
svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {W} {H}' preserveAspectRatio='none'>"
       f"<path fill-rule='evenodd' d='{path}'/></svg>")
uri = "data:image/svg+xml," + urllib.parse.quote(svg, safe=" '/:=,.-MZ0123456789")
print(uri)
sys.stderr.write(f'contours={len(parts)} svg_bytes={len(svg)} uri_bytes={len(uri)}\n')
