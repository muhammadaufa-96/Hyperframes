"""Video 3: checklist site visit (no voice; the host records VO in CapCut)."""
import sys
sys.path.insert(0, "/home/user/Hyperframes/raw/scripts")
from gen import Comp

F = "../assets/footage/"
c = Comp("v3-checklist", 41.0)

# VO slots (start, end) the host records against; also used for the timing sheet
SLOTS = [
    ("Hook", 0.0, 4.6, "Nak renovate shoplot jadi klinik? Sebelum sign apa-apa, check 4 benda ni dulu."),
    ("Konteks", 4.6, 8.4, "Minggu ni aku site visit untuk klinik 3 tingkat kat Subang."),
    ("1 Lift", 8.4, 12.4, "Satu, lift. Bangunan bertingkat, pesakit kena senang naik turun."),
    ("2 Wiring", 12.4, 19.0, "Dua, wiring. Buka DB box, tengok keadaan dia. Kalau dah lama dan bersepah macam ni, kena buat full rewiring."),
    ("3 Emergency exit", 19.0, 23.0, "Tiga, emergency exit. Pastikan laluan keluar ada dan tak terhalang."),
    ("4 Toilet", 23.0, 29.0, "Empat, toilet. Kira berapa unit dan kat mana kedudukan dia, sebab nak alih paip memang makan kos."),
    ("Bonus", 29.0, 33.0, "Bonus, bawa laser measure. Ukur cepat, tak payah risau tape hilang."),
    ("CTA", 33.0, 41.0, "Save video ni untuk site visit korang nanti. Nak renovate klinik atau kedai? DM aku."),
]

# Hook: corridor with loose conduit
c.broll(F + "IMG_5112.mp4", 0.0, 4.6, media_start=6.5, zoom=(1.0, 1.18))
c.shade(0.0, 41.0)
c.hook(["Nak renovate shoplot?", "Check 4 benda ni dulu ⚠️"], 0.1, 4.4)

# Context: building exterior
c.broll(F + "IMG_5111.mp4", 4.6, 3.8, media_start=0.3, zoom=(1.12, 1.0))
c.chip("📍 Subang", 4.8, 3.5, x=70, y=300, yellow=True)
c.chip("Klinik · 3 tingkat", 5.3, 3.0, x=70, y=410)

# 1 Lift
c.broll(F + "IMG_5112.mp4", 8.4, 4.0, media_start=3.0, zoom=(1.0, 1.1))
c.card("1", "Lift", "Pesakit senang naik turun", 8.5, 3.9)

# 2 Wiring: DB box photo, then ceiling conduit
c.image(F + "db_box.jpg", 12.4, 3.4, zoom=(1.0, 1.15), origin="45% 45%")
c.broll(F + "IMG_5112.mp4", 15.8, 3.2, media_start=10.0, zoom=(1.05, 1.15))
c.card("2", "Wiring", "Lama & bersepah? Full rewiring", 12.5, 6.5)

# 3 Emergency exit
c.broll(F + "IMG_5112.mp4", 19.0, 2.2, media_start=16.6, zoom=(1.0, 1.12))
c.broll(F + "IMG_5128.mp4", 21.2, 1.8, media_start=1.5, zoom=(1.0, 1.08))
c.card("3", "Emergency exit", "Laluan keluar tak terhalang", 19.1, 3.9)

# 4 Toilet: before -> after
c.broll(F + "IMG_5112.mp4", 23.0, 2.8, media_start=20.0, zoom=(1.0, 1.1))
c.broll(F + "IMG_4943.mp4", 25.8, 3.2, media_start=22.5, zoom=(1.08, 1.0))
c.card("4", "Toilet", "Berapa unit & kedudukan paip", 23.1, 5.9)
c.chip("Sebelum", 23.6, 2.1, x=70, y=1450)
c.chip("Selepas ✨", 25.9, 3.0, x=70, y=1450, yellow=True, sfx="sparkle")

# Bonus: laser measure graphic
c.laser(29.0, 4.0, kicker="BONUS 📏", title="Bawa laser measure", badge="Ukur cepat, tak risau tape hilang")

# CTA: finished projects montage, then end card with logo
c.broll(F + "IMG_4940.mp4", 33.0, 1.4, media_start=0.5, zoom=(1.1, 1.0))
c.broll(F + "IMG_2530.mp4", 34.4, 1.3, media_start=1.0, zoom=(1.0, 1.1))
c.broll(F + "IMG_8310.mp4", 35.7, 1.3, media_start=5.0, zoom=(1.1, 1.0))
c.broll(F + "7695A0AD.mp4", 37.0, 4.0, media_start=1.0, zoom=(1.0, 1.08))
c.chip("Save 📌 untuk site visit", 33.1, 4.0, x=70, y=300, yellow=True)
c.sfx("whoosh-short", 34.4, 0.35); c.sfx("whoosh-short", 35.7, 0.35); c.sfx("whoosh-short", 37.0, 0.35)
c.endcard(38.0, 3.0, '<span class="ln">Nak renovate klinik / kedai?</span><em class="ln">DM aku</em>', "Renovate like corporate, price like DIY",
          logo="../assets/brand/enoxin-logo-white.png")

c.write("/home/user/Hyperframes/compositions/v3-checklist.html", "Video 3: Checklist site visit")

if __name__ == "__main__":
    with open("/home/user/Hyperframes/raw/edit/v3_vo_timing.txt", "w") as f:
        for name, a, b, line in SLOTS:
            f.write(f"{a:5.1f}s - {b:5.1f}s  [{name}]  {line}\n")
