# Abdelrhman Mohamed — UGC Creator

A cinematic, bilingual (EN / AR-RTL) one-page website for an 18-year-old UGC creator: **$25 per video, first video free**.
It is plain HTML/CSS/JS, so it deploys to GitHub Pages as-is, with no build step and no backend.

- **Motion:** GSAP 3.15 (ScrollTrigger + SplitText) and Lenis 1.3.26, bundled locally in `vendor/`.
- **Fonts:** self-hosted in `public/fonts/` (Anton, Manrope, Ms Madi, Alexandria, Aref Ruqaa; all SIL OFL).
- **Images:** WebP with JPG/PNG fallbacks, responsive `srcset`, lazy-loaded below the fold.
- **Lighthouse** (gzip like GitHub Pages):
  - Mobile: Performance ≈ 90, Accessibility 100, Best Practices 100, SEO 100, CLS 0.
  - Desktop: Performance ≈ 95, Accessibility 100, Best Practices 100, SEO 100, CLS 0.
- Respects `prefers-reduced-motion`, works without JavaScript, has no console errors, and opens straight from disk (file://).
- **Content is honest.** The six phones in "What I make" illustrate the video *formats* he films; they are not client work. The WhatsApp chat in "Pricing" is an illustrative example of the ordering flow. The only numbers on the page are real facts: 18 years old, $25 per video, first video free.

---

## خطوات النشر السريعة (عربي): ريبو جديد

الموقع كله **50 ملف**، فممكن تترفع من المتصفح **مرة واحدة** (الحد 100 ملف في المرة).

1. اعمل ريبو جديد **Public** من https://github.com/new، مثلاً باسم `abdelrhman` أو `ugc`.
2. في صفحة الريبو اضغط **uploading an existing file**. افتح مجلد `abdelrhman-portfolio` على جهازك، وحدّد **كل اللي جواه** (الملفات والمجلدات: `css` و`js` و`public` و`vendor` و`tools` …)، واسحبهم لصفحة الرفع، وبعدها **Commit changes**.
3. من **Settings ← Pages** اختار **Deploy from a branch**، وبعدها **Branch: `main`** و **`/ (root)`**، ثم **Save**.
4. بعد دقيقة أو اتنين هيظهر الرابط، وهيكون بالشكل ده: `https://USERNAME.github.io/REPO/`.
5. **مهم:** غيّر `https://YOUR-USERNAME.github.io/YOUR-REPO/` للرابط الحقيقي في `index.html` و`robots.txt` و`sitemap.xml`. ده بيخلي صورة المعاينة تظهر صح لما الرابط يتبعت على واتساب أو فيسبوك. أو ابعتلي اسم الريبو وأنا أظبطه.

لازم تسحب **المجلدات نفسها** (مش الملفات اللي جواها بس)، عشان المسارات تفضل صحيحة. الموقع ده منفصل تماماً عن ريبو يوسف `yousefharby/Yousef` ومش بيلمسه.

---

## File tree

```
abdelrhman-portfolio/
├── index.html              ← the whole page (English copy lives here)
├── 404.html                ← self-contained "page not found" (works for user & project sites)
├── favicon.ico
├── site.webmanifest
├── robots.txt              ← [EDIT] URL
├── sitemap.xml             ← [EDIT] URL
├── .nojekyll               ← tells GitHub Pages to serve files as-is
├── README.md
├── css/
│   └── main.css            ← design tokens, layout, phone mockups, RTL, responsive, reduced-motion
├── js/
│   ├── i18n.js             ← Arabic translations + JS-only strings (WhatsApp messages, calculator)
│   ├── data.js             ← the 6 video formats shown in the detail overlay (EN + AR)
│   └── main.js             ← preloader, hero, formats gallery, overlay, pricing calculator, chat, language switch
├── vendor/
│   ├── gsap/               ← gsap.min.js, ScrollTrigger.min.js, SplitText.min.js (3.15.0)
│   └── lenis/              ← lenis.min.js (1.3.26)
├── public/
│   ├── fonts/              ← woff2 files + license note
│   ├── icons/              ← favicon.svg, apple-touch-icon, 192/512 app icons
│   └── img/                ← cut-out portrait (webp+png), red glow, on-location photo crops, og-image.jpg
└── tools/                  ← asset pipeline (not needed at runtime)
    ├── cutout_photo.py     ← background removal (rembg + hair-aware matting)
    ├── process_assets.py   ← portrait crop, glow, shirt mask, on-location crops (WebP + fallbacks)
    ├── trace_mask.py       ← turns the shirt mask into the inline SVG used in main.css
    ├── body-mask.png
    ├── og-image.html       ← 1200×630 social-share card template
    └── render-og.mjs       ← renders og-image.html with Playwright
```

---

## Things to edit: `[EDIT]` checklist

| Where | What | Currently |
|---|---|---|
| `index.html` (head + JSON-LD), `robots.txt`, `sitemap.xml` | Final site URL, so link previews and the sitemap point to the right place | `https://YOUR-USERNAME.github.io/YOUR-REPO/` |
| `index.html` → Contact list (commented spot) | His TikTok / Instagram links. Copy a contact block and use `#i-tiktok` / `#i-instagram` (both icons are already in the sprite) | not added yet |
| `index.html` → Footer | Optional "Website by Yousef Harby" credit. Delete the line if you don't want it | shown |
| `index.html` + `js/i18n.js` → Contact "Based in" | City, if he wants one | Egypt · working with brands worldwide |
| Price (if it ever changes) | `PRICE` in `js/main.js`, plus every "$25" / "25 دولار" in `index.html` and `js/i18n.js` | $25, first video free |
| Phone (if it ever changes) | `WA_NUMBER` in `js/main.js`, plus `wa.me/…` and `tel:` links in `index.html` | +20 10 2531 1120 |

Arabic versions of the page text are in `js/i18n.js`, under the same keys as the `data-i18n` attributes.

---

## Editing content

- **English text:** edit it directly in `index.html`.
- **Arabic text:** edit `js/i18n.js`. Every key matches a `data-i18n="…"` attribute in the HTML.
- **Format overlay** (lead, "best for", steps, "great for", WhatsApp message): edit `js/data.js`.
- **WhatsApp messages:** every WhatsApp button opens a chat with a ready-made message in the visitor's language. These messages live in `js/i18n.js` (`YH.UI`) and `js/data.js` (`wa`).
- **Adding real videos later:** replace a phone's inner `.device__screen` content in `index.html` with a `<video muted loop playsinline autoplay poster="…">` (9:16), or keep the phone design and swap the background image.
- **Language:** the EN/AR button remembers the choice. Share `?lang=ar` to open the Arabic version directly.

## Preview locally

Double-clicking `index.html` works. For the most accurate preview, serve the folder:

```bash
cd abdelrhman-portfolio
python3 -m http.server 8000      # then open http://localhost:8000
```

## Deploy to GitHub Pages (English)

1. Create a **public** repository at https://github.com/new.
2. Upload the **contents** of this folder (not the folder itself) to the repository root. It is 50 files, so one browser upload works (*Add file → Upload files*). Or use git:
   ```bash
   cd abdelrhman-portfolio
   git init && git add . && git commit -m "UGC website"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo>.git
   git push -u origin main
   ```
3. Go to **Settings → Pages → Build and deployment**, set **Source: Deploy from a branch**, then **Branch: `main` / `(root)`**, and click **Save**.
4. Replace `https://YOUR-USERNAME.github.io/YOUR-REPO/` with the live URL in `index.html`, `robots.txt` and `sitemap.xml`.
5. *(Optional custom domain)* In Settings → Pages → Custom domain, enter your domain, then add the DNS records GitHub shows you.

All paths are relative, so the site works both at a domain root and under `/<repo>/`.

## Regenerating images (only if the photos change)

```bash
pip install "rembg[cpu]" pymatting opencv-python-headless pillow numpy
python3 tools/cutout_photo.py path/to/studio-photo.jpg tools/            # → tools/cutout-full.png
python3 tools/process_assets.py tools/cutout-full.png path/to/outdoor.jpg .
python3 tools/trace_mask.py tools/body-mask.png 960 988                   # paste output into --shirt-mask in css/main.css
node tools/render-og.mjs                                                  # optional: new social-share image
```

The studio photo should be on a plain white background, like the current one.

## Credits & licenses

- GSAP & plugins: GreenSock "Standard No-Charge License" (free, including commercial use), https://gsap.com/standard-license
- Lenis: MIT, by darkroom.engineering
- Fonts: SIL Open Font License 1.1 (see `public/fonts/README.txt`)
- Icons: Feather (MIT) and Font Awesome brand icons (CC BY 4.0), inlined as an SVG sprite
