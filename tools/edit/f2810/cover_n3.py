"""Thumbnails for the 4/11 boutique marking video: TikTok + IG Reels (both 1080x1920, text in the 3:4 centre band)."""
import json, os, subprocess
import covers as cv

A = "/home/user/Hyperframes/assets/footage/f0611/"
OUT = "/home/user/Hyperframes/deliver/0611/"
T = cv.text("Kontraktor review kafe", "9.5/10<br><em>untuk design</em>", "tapi makanan…?")
JOBS = {
    "n3-cover-tiktok": f'<div class="bg" style="top:-120px;background-image:url(\'file://{A}f_28.jpg\');background-position:center top"></div>' + T,
    "n3-cover-ig": (f'<div class="half top" style="background-image:url(\'file://{A}f_28.jpg\');background-position:center 25%"></div>'
                    f'<div class="half bot" style="background-image:url(\'file://{A}IMG_6123.jpg\')"></div><div class="line"></div>' + T),
}
os.makedirs(OUT, exist_ok=True)
jobs = []
for name, body in JOBS.items():
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{cv.CSS} .box {{ top: 1040px; transform: none; }} .b {{ font-size: 122px; }} .logo {{ top: 70px; bottom: auto; }} .sh {{ background: linear-gradient(180deg, rgba(0,0,0,0) 45%, rgba(0,0,0,0.65) 62%, rgba(0,0,0,0.65) 88%, rgba(0,0,0,0.3) 100%); }}</style></head><body>{body}<img class='logo' src='file://{cv.LOGO}'></body></html>"
    p = f"/tmp/cover_{name}.html"; open(p, "w").write(html); jobs.append([p, OUT + name + ".jpg"])
open("/tmp/cover_shot.js", "w").write(cv.SHOT.format(jobs=json.dumps(jobs)))
subprocess.run(["node", "/tmp/cover_shot.js"], check=True)
