"""TikTok + IG Reels covers for the 13/11 edits (1080x1920, text kept in the centre band)."""
import json, os, subprocess
import covers as cv

A = "/home/user/Hyperframes/assets/footage/f1311/"
OUT = "/home/user/Hyperframes/deliver/1311/covers/"
EXTRA = " .box {{ top: 1000px; transform: none; }} .b {{ font-size: 116px; }} .logo {{ top: 70px; bottom: auto; }} .sh {{ background: linear-gradient(180deg, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0) 30%, rgba(0,0,0,0.65) 55%, rgba(0,0,0,0.7) 90%, rgba(0,0,0,0.4) 100%); }}"
V = {
    "m1": ("shutter.jpg", "arch.jpg", cv.text("Kontraktor share", "3 benda<br><em>renovate<br>lambat siap</em>", "berapa lama nak siap?")),
    "m2": ("butik.jpg", "arch.jpg", cv.text("Nak buka butik?", "Nampak<br><em>mahal?</em>", "2 benda ni penting")),
    "m3": ("fasa.jpg", "pickup.jpg", cv.text("Kontraktor share", "<em>5 fasa</em><br>renovate kedai", "fasa 1 dah nak siap")),
    "m4": ("arch.jpg", "live.jpg", cv.text("Butik 1,200 sqft", "Ada 2<br><em>bilik live?</em>", "tour layout butik")),
    "m5": ("pickup.jpg", "hall.jpg", cv.text("Progress site", "<em>Fasa 2</em><br>bermula", "Setia Alam")),
}
os.makedirs(OUT, exist_ok=True)
jobs = []
for k, (main, second, T) in V.items():
    for kind, body in {
        "tiktok": (f'<div class="bg" style="top:-420px;background-image:url(\'file://{A}{main}\');background-position:center top"></div>' if k == "m3" else cv.bg(A + main, "center 30%")) + T,
        "ig": (f'<div class="half top" style="background-image:url(\'file://{A}{main}\');background-position:center 30%"></div>'
               f'<div class="half bot" style="background-image:url(\'file://{A}{second}\')"></div><div class="line"></div>' + T),
    }.items():
        html = f"<!doctype html><html><head><meta charset='utf-8'><style>{cv.CSS}{EXTRA.format()}</style></head><body>{body}<img class='logo' src='file://{cv.LOGO}'></body></html>"
        p = f"/tmp/cover_{k}_{kind}.html"; open(p, "w").write(html); jobs.append([p, f"{OUT}{k}-cover-{kind}.jpg"])
open("/tmp/cover_shot.js", "w").write(cv.SHOT.format(jobs=json.dumps(jobs)))
subprocess.run(["node", "/tmp/cover_shot.js"], check=True)
