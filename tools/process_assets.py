"""
Build every optimized image the site uses.
Usage: python3 tools/process_assets.py <cutout.png> <outdoor.jpg> <site root>
  cutout.png  = output of tools/cutout_photo.py (transparent studio portrait)
  outdoor.jpg = the on-location photo
"""
import sys, os
import numpy as np, cv2
from PIL import Image

CUT, OUTDOOR, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
IMG = f'{OUT}/public/img'
os.makedirs(IMG, exist_ok=True)

def resize_w(im, w):
    return im if im.width == w else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)

def save(im, name, widths, q=82, alpha=False):
    for w in widths:
        r = resize_w(im, w)
        r.save(f'{IMG}/{name}-{w}.webp', 'WEBP', quality=q, method=6)
        if alpha:
            r.save(f'{IMG}/{name}-{w}.png', optimize=True)
        else:
            r.convert('RGB').save(f'{IMG}/{name}-{w}.jpg', 'JPEG', quality=q, optimize=True, progressive=True)

# ------------------------------------------------------------- hero portrait
cut = Image.open(CUT).convert('RGBA')
a = np.asarray(cut)[..., 3]
top = max(int(np.where(a.max(axis=1) > 8)[0].min()) - 24, 0)
bottom = int(cut.height * 0.90)                 # bottom is faded out in CSS anyway -> person reads larger
cut = cut.crop((0, top, cut.width, bottom))
print('portrait', cut.size, 'aspect', round(cut.width / cut.height, 4))
save(cut, 'abdelrhman-cutout', [960, 640], q=86, alpha=True)

# red rim-light glow (blurred silhouette, fades out towards the bottom)
PAD = 160
al = np.asarray(cut)[..., 3].astype(np.float32) / 255.0
canvas = np.zeros((al.shape[0] + 2 * PAD, al.shape[1] + 2 * PAD), np.float32)
canvas[PAD:PAD + al.shape[0], PAD:PAD + al.shape[1]] = al
g = cv2.GaussianBlur(canvas, (0, 0), 46) * 0.95 + cv2.GaussianBlur(canvas, (0, 0), 16) * 0.45
yy = (np.arange(canvas.shape[0], dtype=np.float32) - PAD) / al.shape[0]
v = np.clip((0.78 - yy) / (0.78 - 0.40), 0, 1) ** 1.4
g = np.clip(g * v[:, None], 0, 1)
glow = np.zeros((g.shape[0], g.shape[1], 4), np.uint8)
glow[..., 0], glow[..., 1], glow[..., 2] = 255, 34, 12
glow[..., 3] = (g * 255).astype(np.uint8)
gi = Image.fromarray(glow, 'RGBA')
gi = gi.resize((gi.width // 2, gi.height // 2), Image.LANCZOS)   # big enough to stay crisp on large screens
gi.save(f'{IMG}/abdelrhman-glow.webp', 'WEBP', quality=70, method=6)
gi.save(f'{IMG}/abdelrhman-glow.png', optimize=True)
print('glow', gi.size, 'pad% x', round(PAD / cut.width * 100, 3), 'y', round(PAD / cut.height * 100, 3))

# shirt mask (front "PORTFOLIO" layer passes in front of the shirt only)
rgb = np.asarray(cut.convert('RGB')).astype(np.float32) / 255.0
lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)
alpha = np.asarray(cut)[..., 3].astype(np.float32) / 255.0
dark = np.clip((0.40 - lum) / (0.40 - 0.24), 0, 1)
Hc = alpha.shape[0]
yy = np.arange(Hc, dtype=np.float32)[:, None] / Hc
below = np.clip((yy - 0.405) / 0.03, 0, 1)
m = alpha * dark * below
mb = (m > 0.5).astype(np.uint8)
n, lab, stats, _ = cv2.connectedComponentsWithStats(mb, 8)
if n > 1:
    mb = (lab == 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))).astype(np.uint8)
mb = cv2.morphologyEx(mb, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
soft = cv2.GaussianBlur(mb.astype(np.float32), (0, 0), 1.6) * np.clip(alpha * 1.2, 0, 1)
mask = np.zeros((Hc, alpha.shape[1], 4), np.uint8); mask[..., 3] = (np.clip(soft, 0, 1) * 255).astype(np.uint8)
Image.fromarray(mask, 'RGBA').save(f'{OUT}/tools/body-mask.png', optimize=True)
print('mask -> tools/body-mask.png  (trace with: python3 tools/trace_mask.py tools/body-mask.png 960 988)')

# ------------------------------------------------------------- on-location photo
od = Image.open(OUTDOOR).convert('RGB')
W, H = od.size
save(od, 'creator-on-set', [1200, 800], q=80)                                       # 3:4 full frame
cx = int(W * 0.66); w9 = int(H * 9 / 16)                                             # 9:16 around him
x0 = max(0, min(W - w9, cx - w9 // 2))
save(od.crop((x0, 0, x0 + w9, H)), 'creator-vertical', [720, 480], q=80)
fx0, fy0, fw = int(W * 0.40), int(H * 0.22), int(W * 0.56)                            # 4:3 upper body
save(od.crop((fx0, fy0, fx0 + fw, fy0 + int(fw * 3 / 4))), 'creator-closeup', [800], q=80)
print('on-location', od.size, '9:16 x0', x0)
