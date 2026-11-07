"""7/11/26 carousel: "Kedai nasi padang, rasa hotel 5 bintang" (Pagi Sore, Indonesia).
Stills from the b-roll proxies, bystander faces blurred, 8 slides at 1080x1350.
usage: python3 carousel.py  -> /home/user/Hyperframes/f0711/carousel/slide-N.jpg"""
import os, subprocess
import cv2

ROOT = "/home/user/Hyperframes"
SRC = f"{ROOT}/f0711/stills"
OUT = f"{ROOT}/f0711/carousel"
os.makedirs(f"{OUT}/img", exist_ok=True)
W, H = 1080, 1350

# (still, vertical focus 0..1 for the 4:5 crop)
SLIDES = [
    dict(img="IMG_6178_2.7", fy=0.45, kind="cover", kicker="Pagi Sore, Indonesia",
         title="Kedai nasi padang.<br><em>Rasa macam hotel 5 bintang.</em>",
         body="5 benda yang saya perasan, dari mata kontraktor."),
    dict(img="IMG_6178_3.6", fy=0.6, n=1, title="Lantai corak jadi laluan",
         body="Lantai corak ni macam karpet panjang. Dari pintu, mata terus ikut sampai ke ruang makan."),
    dict(img="IMG_6178_10.0", fy=0.5, n=2, title="Satu tumpuan besar di siling",
         body="Lampu besar berderet dan tingkap gerbang. Masuk je, mata terus naik ke atas. Ruang rasa tinggi dan lapang."),
    dict(img="IMG_6218_5.6", fy=0.5, n=3, title="Bawa hijau masuk ke dalam",
         body="Laluan dari sinki ke ruang makan pun ada taman. Pokok betul, cahaya dari luar. Rasa tenang walaupun kedai penuh."),
    dict(img="IMG_6179_2.9", fy=0.62, n=4, title="Tempat duduk ikut bentuk ruang",
         body="Sofa melengkung ikut bentuk gerbang. Meja besar untuk satu keluarga. Hidang nasi padang memang perlukan meja macam ni."),
    dict(img="IMG_6219_1.6", fy=0.42, n=5, title="Ruang belakang pun dapat design",
         body="Surau ada skrin ukiran dan taman kecil. Tempat wuduk kemas. Ramai kedai lupa ruang ni."),
    dict(img="IMG_6180_3.4", fy=0.55, kind="lesson", title="Untuk kedai atau klinik awak",
         rows=["Pilih satu tumpuan. Jangan semua benda nak menonjol.",
               "Fikir laluan pelanggan, dari pintu sampai dia duduk.",
               "Jaga ruang belakang. Surau dan tandas pun pelanggan nilai."]),
    dict(img="IMG_6178_1.9", fy=0.5, kind="cta", title="Save untuk rujukan design.",
         body="Share pada kawan yang nak buka kedai atau klinik."),
]

det = cv2.FaceDetectorYN.create("/root/models/yunet.onnx", "", (540, 960), 0.7, 0.3, 5000)


def prep(name, fy, w=W, h=H):
    """Blur bystander faces on the full frame, then crop to w:h around the vertical focus."""
    im = cv2.imread(f"{SRC}/{name}.jpg")
    ih, iw = im.shape[:2]
    det.setInputSize((iw, ih))
    _, faces = det.detect(im)
    sx, sy = 1.0, 1.0
    for f in (faces if faces is not None else []):
        x, y, fw, fh = [int(v) for v in (f[0] * sx, f[1] * sy, f[2] * sx, f[3] * sy)]
        pad = int(0.35 * max(fw, fh))
        x0, y0, x1, y1 = max(0, x - pad), max(0, y - pad), min(iw, x + fw + pad), min(ih, y + fh + pad)
        roi = im[y0:y1, x0:x1]
        k = max(15, (max(fw, fh) // 2) * 2 + 1)
        im[y0:y1, x0:x1] = cv2.GaussianBlur(roi, (k, k), 0)
    scale = w / iw
    im = cv2.resize(im, (w, int(ih * scale)), interpolation=cv2.INTER_LANCZOS4)
    top = int(min(max(0, fy * im.shape[0] - h / 2), im.shape[0] - h))
    im = im[top:top + h]
    p = f"{OUT}/img/{name}_{w}x{h}.jpg"
    cv2.imwrite(p, im, [cv2.IMWRITE_JPEG_QUALITY, 94])
    n = 0 if faces is None else len(faces)
    print(f"{name}: {n} face(s) blurred")
    return p


CSS = f"""
@font-face {{ font-family: M; font-weight: 600; src: url(file://{ROOT}/assets/fonts/montserrat-latin-600-normal.woff2); }}
@font-face {{ font-family: M; font-weight: 800; src: url(file://{ROOT}/assets/fonts/montserrat-latin-800-normal.woff2); }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ width: {W}px; height: {H}px; overflow: hidden; background: #111; font-family: M, sans-serif; color: #fff; }}
.bg {{ position: absolute; inset: 0; background-size: cover; background-position: center; }}
.split {{ position: absolute; inset: 0; display: grid; grid-template-rows: 1fr 1fr; gap: 6px; background: #111; }}
.split div {{ background-size: cover; background-position: center; }}
.sh {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 26%, rgba(0,0,0,0) 42%, rgba(0,0,0,0.88) 78%, rgba(0,0,0,0.94) 100%); }}
.sh.full {{ background: rgba(8,9,11,0.72); }}
.top {{ position: absolute; left: 64px; right: 64px; top: 56px; display: flex; justify-content: space-between; align-items: center; font-weight: 800; font-size: 30px; letter-spacing: 0.04em; }}
.top .pg {{ background: rgba(0,0,0,0.5); border-radius: 999px; padding: 8px 20px; font-size: 26px; }}
.box {{ position: absolute; left: 64px; right: 64px; bottom: 80px; }}
.n {{ display: inline-flex; align-items: center; justify-content: center; width: 96px; height: 96px; border-radius: 50%; background: #f5c22e; color: #15171a; font-weight: 800; font-size: 54px; margin-bottom: 26px; }}
.k {{ display: inline-block; background: #f5c22e; color: #15171a; font-weight: 800; font-size: 30px; letter-spacing: 0.08em; text-transform: uppercase; padding: 10px 22px; border-radius: 8px; margin-bottom: 26px; }}
h1 {{ font-weight: 800; font-size: 76px; line-height: 1.04; text-transform: uppercase; }}
h1 em {{ font-style: normal; color: #f5c22e; }}
h2 {{ font-weight: 800; font-size: 62px; line-height: 1.06; text-transform: uppercase; }}
p {{ margin-top: 24px; font-weight: 600; font-size: 38px; line-height: 1.32; color: #ececec; }}
.rows {{ margin-top: 34px; display: flex; flex-direction: column; gap: 24px; }}
.row {{ display: flex; gap: 22px; align-items: flex-start; font-weight: 600; font-size: 38px; line-height: 1.3; }}
.row i {{ flex: none; width: 58px; height: 58px; border-radius: 50%; background: #f5c22e; color: #15171a; font-style: normal; font-weight: 800; font-size: 32px; display: flex; align-items: center; justify-content: center; margin-top: -4px; }}
.btn {{ margin-top: 40px; display: inline-block; background: #f5c22e; color: #15171a; font-weight: 800; font-size: 40px; text-transform: uppercase; padding: 20px 40px; border-radius: 999px; }}
.swipe {{ margin-top: 30px; font-weight: 800; font-size: 30px; letter-spacing: 0.06em; text-transform: uppercase; color: #f5c22e; }}
"""


def page(i, s, total):
    bg = (f'<div class="split"><div style="background-image:url(file://{s["p"]})"></div><div style="background-image:url(file://{s["p2"]})"></div></div>'
          if "p2" in s else f'<div class="bg" style="background-image:url(file://{s["p"]})"></div>')
    full = s.get("kind") in ("lesson", "cta")
    top = f'<div class="top"><span>@bangfasz</span><span class="pg">{i}/{total}</span></div>'
    kind = s.get("kind")
    if kind == "cover":
        box = (f'<div class="k">{s["kicker"]}</div><h1>{s["title"]}</h1><p>{s["body"]}</p>'
               f'<div class="swipe">Swipe untuk tengok &rarr;</div>')
    elif kind == "lesson":
        rows = "".join(f'<div class="row"><i>{k + 1}</i><span>{r}</span></div>' for k, r in enumerate(s["rows"]))
        box = f'<div class="k">Pengajaran</div><h2>{s["title"]}</h2><div class="rows">{rows}</div>'
    elif kind == "cta":
        box = f'<h2>{s["title"]}</h2><p>{s["body"]}</p><div class="btn">Follow @bangfasz</div>'
    else:
        box = f'<div class="n">{s["n"]}</div><h2>{s["title"]}</h2><p>{s["body"]}</p>'
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'{bg}<div class="sh{" full" if full else ""}"></div>{top}<div class="box">{box}</div></body></html>')


def main():
    for s in SLIDES:
        if "img2" in s:
            s["p"] = prep(s["img"], 0.45, W, H // 2)
            s["p2"] = prep(s["img2"], 0.55, W, H // 2)
        else:
            s["p"] = prep(s["img"], s["fy"])
    for i, s in enumerate(SLIDES, 1):
        open(f"{OUT}/slide-{i}.html", "w").write(page(i, s, len(SLIDES)))
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{W},height:{H}}},deviceScaleFactor:1}});"
          f"for(let i=1;i<={len(SLIDES)};i++){{await p.goto('file://{OUT}/slide-'+i+'.html');await p.waitForTimeout(300);"
          f"await p.screenshot({{path:'{OUT}/slide-'+i+'.png'}});}}await b.close();}})();")
    subprocess.run(["node", "-e", js], check=True, cwd="/tmp")
    for i in range(1, len(SLIDES) + 1):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}/slide-{i}.png", "-q:v", "2", f"{OUT}/slide-{i}.jpg"], check=True)
        os.remove(f"{OUT}/slide-{i}.png")
    print("CAROUSELDONE")


if __name__ == "__main__":
    main()
