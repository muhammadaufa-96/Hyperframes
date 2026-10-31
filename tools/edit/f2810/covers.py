"""Cover / thumbnail images (1080x1920) for the Luma Clinic videos.
Text sits in the centre band so it survives the 3:4 and 1:1 grid crops on IG / TikTok.
usage: python3 covers.py  -> /home/user/Hyperframes/deliver/2810/covers/*.jpg"""
import os, json, subprocess

ROOT = "/home/user/Hyperframes/"
LU = ROOT + "assets/footage/luma/"
OUT = ROOT + "deliver/2810/covers/"
FONT = ROOT + "assets/fonts/"
LOGO = ROOT + "assets/brand/enoxin-logo-white.png"

CSS = f"""
@font-face {{ font-family: M; font-weight: 800; src: url("file://{FONT}montserrat-latin-800-normal.woff2"); }}
@font-face {{ font-family: M; font-weight: 600; src: url("file://{FONT}montserrat-latin-600-normal.woff2"); }}
* {{ margin: 0; box-sizing: border-box; }}
body {{ width: 1080px; height: 1920px; position: relative; overflow: hidden; font-family: M, sans-serif; background: #111; }}
.bg {{ position: absolute; inset: 0; background-size: cover; background-position: center; }}
.half {{ position: absolute; left: 0; right: 0; height: 960px; background-size: cover; background-position: center; }}
.top {{ top: 0; }} .bot {{ top: 960px; }}
.sh {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.05) 25%, rgba(0,0,0,0.55) 45%, rgba(0,0,0,0.55) 62%, rgba(0,0,0,0.1) 80%, rgba(0,0,0,0.35) 100%); }}
.box {{ position: absolute; left: 60px; right: 60px; top: 50%; transform: translateY(-50%); text-align: center; }}
.k {{ display: inline-block; font-weight: 800; font-size: 44px; letter-spacing: 0.06em; text-transform: uppercase; color: #15171a; background: #f5c22e; padding: 12px 28px; border-radius: 12px; margin-bottom: 26px; }}
.b {{ display: block; font-weight: 800; font-size: 150px; line-height: 0.95; text-transform: uppercase; color: #fff; text-shadow: 0 8px 0 rgba(0,0,0,0.35), 0 0 50px rgba(0,0,0,0.5); }}
.b em {{ font-style: normal; color: #f5c22e; }}
.s {{ display: block; margin-top: 26px; font-weight: 600; font-size: 46px; color: #fff; text-shadow: 0 3px 12px rgba(0,0,0,0.7); }}
.tag {{ position: absolute; left: 50%; transform: translateX(-50%); font-weight: 800; font-size: 54px; padding: 12px 34px; border-radius: 12px; letter-spacing: 0.08em; }}
.tag.d {{ background: #e11d48; color: #fff; }} .tag.n {{ background: #f5c22e; color: #15171a; }}
.line {{ position: absolute; left: 0; right: 0; top: 954px; height: 12px; background: #f5c22e; }}
.logo {{ position: absolute; left: 50%; bottom: 120px; transform: translateX(-50%); width: 230px; opacity: 0.9; }}
"""


def bg(src, pos="center"):
    return f'<div class="bg" style="background-image:url(\'file://{src}\');background-position:{pos}"></div>'


def text(k, b, s):
    return f'<div class="sh"></div><div class="box"><span class="k">{k}</span><span class="b">{b}</span><span class="s">{s}</span></div>'


COVERS = {
    "c1-tour-9-bilik": bg(LU + "a_counter.jpg") + text("Full tour · Luma Clinic", "Klinik<br>estetik<br><em>9 bilik</em>", "dalam ±1,500 sqft. Macam mana?"),
    "c9-full-klinik": bg(LU + "a_wait1.jpg") + text("Owner klinik estetik?", "Tengok<br><em>ni dulu</em>", "sebelum korang renovate"),
    "c10-vlog-luma": (f'<div class="half top" style="background-image:url(\'file://{LU}car.jpg\')"></div>'
                      f'<div class="half bot" style="background-image:url(\'file://{LU}a_counter.jpg\')"></div><div class="line"></div>'
                      + text("POV", "OTW tengok<br><em>projek siap</em>", "klinik estetik yang kita renovate")),
    "c11-before-after-luma": (f'<div class="half top" style="background-image:url(\'file://{LU}IMG_1008.jpg\')"></div>'
                              f'<div class="half bot" style="background-image:url(\'file://{LU}a_wait1.jpg\')"></div><div class="line"></div>'
                              '<div class="tag d" style="top:120px">DULU</div><div class="tag n" style="top:1570px">SEKARANG</div>'
                              + text("Before &amp; After", "Kedai pet<br>jadi <em>klinik<br>estetik</em>", "Luma Clinic, Petaling Jaya")),
}


SHOT = """const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch({{ args: ['--allow-file-access-from-files'] }});
  const pg = await b.newPage({{ viewport: {{ width: 1080, height: 1920 }} }});
  for (const [html, out] of {jobs}) {{
    await pg.goto('file://' + html); await pg.waitForTimeout(500);
    await pg.screenshot({{ path: out, type: 'jpeg', quality: 92 }}); console.log('wrote', out);
  }}
  await b.close();
}})();"""


def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = []
    for name, body in COVERS.items():
        html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}<img class='logo' src='file://{LOGO}'></body></html>"
        path = f"/tmp/cover_{name}.html"
        open(path, "w").write(html)
        jobs.append([path, OUT + name + ".jpg"])
    open("/tmp/cover_shot.js", "w").write(SHOT.format(jobs=json.dumps(jobs)))
    subprocess.run(["node", "/tmp/cover_shot.js"], check=True)


if __name__ == "__main__":
    main()
