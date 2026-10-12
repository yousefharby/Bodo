"""
Cut the studio portrait out of its white background (hair-detail aware).

Pipeline
  1. rembg (isnet-general-use) gives a coarse person mask.
  2. Around dark edges (hair, shirt) alpha is re-estimated from luminance against the
     known white backdrop -> every curl that exists in the source survives.
  3. Semi-transparent edge pixels are colour-unmixed from white (no white halo on dark bg).
  4. Bright edges (ears/neck skin) keep the refined model mask.

Usage:  python3 tools/cutout_photo.py <photo.jpg> <out_dir>
Needs:  pip install "rembg[cpu]" pymatting opencv-python-headless pillow numpy
"""
import sys, os
import numpy as np, cv2
from PIL import Image
from pymatting import estimate_foreground_ml


def coarse_mask(src_rgb):
    import onnxruntime as ort
    from rembg import new_session, remove
    so = ort.SessionOptions()
    so.enable_cpu_mem_arena = False
    so.enable_mem_pattern = False
    sess = new_session('isnet-general-use', sess_opts=so)
    m = remove(src_rgb, session=sess, only_mask=True, post_process_mask=False)
    return np.asarray(m.convert('L')).astype(np.float64) / 255.0


def matte(img, m):
    L = img @ np.array([0.299, 0.587, 0.114])
    k = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
    mb = (m > 0.5).astype(np.uint8)
    core = cv2.erode(mb, k(10)).astype(np.float64)

    def nconv(v, sig):
        return cv2.GaussianBlur(v * core, (0, 0), sig), cv2.GaussianBlur(core, (0, 0), sig)

    num, den = nconv(L, 14)
    Lf = np.where(den > 1e-3, num / np.maximum(den, 1e-6), 0.5)
    Fc = np.zeros_like(img)
    for c in range(3):
        n, d = nconv(img[..., c], 14)
        Fc[..., c] = np.where(d > 1e-3, n / np.maximum(d, 1e-6), 0.2)
    for s in (30, 60):
        n2, d2 = nconv(L, s)
        far = den <= 0.02
        Lf = np.where(far, n2 / np.maximum(d2, 1e-6), Lf)
        for c in range(3):
            n3, d3 = nconv(img[..., c], s)
            Fc[..., c] = np.where(far, n3 / np.maximum(d3, 1e-6), Fc[..., c])

    Lbg, noise = 0.992, 0.014                     # measured backdrop: 251-255
    alpha_lum = np.clip((Lbg - L - noise) / np.maximum(Lbg - Lf - noise, 0.12), 0, 1)
    region = cv2.GaussianBlur(cv2.dilate(mb, k(28)).astype(np.float64), (0, 0), 3)
    alpha_lum *= region
    alpha_lum[alpha_lum < 0.035] = 0
    w_dark = np.clip((0.52 - Lf) / 0.18, 0, 1)    # 1 = hair/shirt edge, 0 = skin edge

    solid = np.maximum((alpha_lum >= 0.08).astype(np.uint8), core.astype(np.uint8))
    d = cv2.distanceTransform(solid, cv2.DIST_L2, 5)
    boost = np.clip((d - 3.0) / 13.0, 0, 1)
    alpha_dark = alpha_lum + (1 - alpha_lum) * boost

    B = np.full(3, Lbg)
    a3 = np.maximum(alpha_lum, 1e-3)[..., None]
    F_unmix = np.clip((img - (1 - a3) * B) / a3, 0, 1)
    t = np.clip((alpha_lum - 0.06) / 0.3, 0, 1)[..., None]
    F_dark = (1 - t) * Fc + t * F_unmix
    b3 = boost[..., None]
    F_dark = (1 - b3) * F_dark + b3 * img

    m_skin = cv2.GaussianBlur(cv2.erode((m > 0.6).astype(np.uint8), k(1)).astype(np.float64), (0, 0), 0.9)
    alpha_skin = np.maximum(core, m_skin)
    alpha = np.clip(w_dark * alpha_dark + (1 - w_dark) * alpha_skin, 0, 1)

    # white gaps between arm and torso at the very bottom of the frame
    H = img.shape[0]
    sat = img.max(axis=2) - img.min(axis=2)
    bottom_white = (L > 0.86) & (sat < 0.08)
    bottom_white[: int(H * 0.88)] = False
    bw = cv2.dilate(bottom_white.astype(np.uint8), k(1)).astype(bool)
    alpha[bw] = 0
    alpha[alpha < 0.03] = 0

    fg_ml = estimate_foreground_ml(img, np.clip(alpha_skin, 0, 1))
    c3 = core[..., None]
    F_skin = c3 * img + (1 - c3) * fg_ml
    wd = w_dark[..., None]
    fg = wd * F_dark + (1 - wd) * F_skin
    return np.clip(fg, 0, 1), alpha


if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    pil = Image.open(src).convert('RGB')
    img = np.asarray(pil).astype(np.float64) / 255.0
    m = coarse_mask(pil)
    fg, alpha = matte(img, m)
    rgba = np.dstack([fg, alpha])
    Image.fromarray((rgba * 255 + 0.5).astype(np.uint8), 'RGBA').save(os.path.join(out, 'cutout-full.png'))
    print('saved', os.path.join(out, 'cutout-full.png'))
