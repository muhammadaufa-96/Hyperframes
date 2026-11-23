"""Covers for the 23/11 video (kabinet hiccup): TikTok (full bleed) + IG Reels (split), 1080x1920, text in the 3:4 centre band."""
import json, os, subprocess, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import covers as cv

A = "/home/user/Hyperframes/assets/footage/f2311/cov/"
OUT = "/home/user/Hyperframes/f2311/deliver/"
T = cv.text("Kerja kabinet di site", "Kena<br><em>hiccup?</em>", "Potong laminate &amp; edging terus di site")
JOBS = {
    "BangFasz_23-11_cover-tiktok": f'<div class="bg" style="top:-420px;background-image:url(\'file://{A}a_5.9.jpg\');background-position:center top"></div>' + T,
    "BangFasz_23-11_cover-ig": (f'<div class="half top" style="background-image:url(\'file://{A}a_5.9.jpg\');background-position:center 40%"></div>'
                                f'<div class="half bot" style="background-image:url(\'file://{A}b_6781_2.2.jpg\');background-position:center 40%"></div><div class="line"></div>' + T),
}
EXTRA = (" .box { top: 1000px; transform: none; } .b { font-size: 150px; } .s { font-size: 44px; } .logo { top: 70px; bottom: auto; }"
         " .sh { background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.68) 55%, rgba(0,0,0,0.68) 86%, rgba(0,0,0,0.3) 100%); }"
         " .stp { position: absolute; right: 60px; top: 190px; transform: rotate(-6deg); font-weight: 800; font-size: 46px; color: #fff; background: #ff3b3b;"
         " border: 6px solid #fff; border-radius: 16px; padding: 8px 22px; text-transform: uppercase; box-shadow: 0 14px 34px rgba(0,0,0,0.5); }")
os.makedirs(OUT, exist_ok=True)
jobs = []
for name, body in JOBS.items():
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{cv.CSS}{EXTRA}</style></head><body>{body}"
            f"<div class='stp'>Settle on the spot!</div><img class='logo' src='file://{cv.LOGO}'></body></html>")
    p = f"/tmp/cover_{name}.html"; open(p, "w").write(html); jobs.append([p, OUT + name + ".jpg"])
open("/tmp/cover_shot.js", "w").write(cv.SHOT.format(jobs=json.dumps(jobs)))
subprocess.run(["node", "/tmp/cover_shot.js"], check=True)
