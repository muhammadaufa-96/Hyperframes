"""Luma Clinic: full-clinic walkthrough short (under 60 s).
No voice and no captions: text hooks + sound effects only; the client adds their own music.
usage: python3 build_full.py"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
from kit import K
from build_2810 import brate, F, PH, OUT, END

# (kind, src, media_start, media_end_or_dur, rate) placed back to back
SHOTS = [
    ("v", "IMG_5530", 0.0, 3.0, 1.0),     # exterior (hook)
    ("v", "IMG_5558", 0.4, 2.0, 1.0),     # glass door -> waiting area
    ("v", "IMG_5559", 0.0, 4.0, 2.0),     # waiting area sofas
    ("i", "IMG_5535", 0, 2.2, 0),         # reception counter (photo: no staff in frame)
    ("v", "IMG_5559", 8.0, 15.0, 2.5),    # curving LED ceiling
    ("v", "IMG_5559", 22.0, 28.0, 2.0),   # curving wood behind counter
    ("v", "IMG_5564", 0.0, 7.0, 3.0),     # waiting area 2
    ("v", "IMG_5564", 11.0, 21.0, 3.0),   # patient toilet
    ("v", "IMG_5565", 1.0, 9.0, 4.0),     # corridor -> OT door
    ("v", "IMG_5565", 10.0, 15.0, 2.0),   # OT room
    ("v", "IMG_5565", 26.0, 42.0, 4.0),   # cabinets, quartz top, drawers
    ("i", "IMG_5544", 0, 1.6, 0),         # treatment room
    ("i", "IMG_5570", 0, 1.4, 0),         # consultation
    ("i", "IMG_5569", 0, 1.4, 0),         # doctor room
    ("i", "IMG_5543", 0, 1.4, 0),         # utility sink
    ("i", "IMG_5568", 0, 1.4, 0),         # slat wood feature
    ("v", "IMG_5563", 8.0, 17.0, 2.5),    # pantry
    ("i", "IMG_5537", 0, 3.0, 0),         # lobby wide (recap)
]


def build():
    t, at = 0.0, []
    for kind, src, a, b, rate in SHOTS:
        d = (b - a) / rate if kind == "v" else b
        at.append((t, d))
        t += d
    A = t
    c = K("c9-full-klinik", A + END)
    for (kind, src, a, b, rate), (s, d) in zip(SHOTS, at):
        if kind == "i":
            c.image(PH + src + ".jpg", s, d, zoom=(1.0, 1.1) if src != "IMG_5537" else (1.15, 1.0))
        elif rate == 1.0:
            c.broll(F + src + ".mp4", s, d, media_start=a, zoom=(1.0, 1.06))
        else:
            brate(c, F + src + ".mp4", s, d, a, rate)
    c.shade(0, A + END)
    T = [s for s, d in at]
    for s in T[1:]:
        c.whip(s)

    # hook
    c.hook2("Owner klinik estetik?", "Tengok<br>ni dulu", "sebelum korang renovate 👀", 0.05, T[1] - 0.1)

    # room labels 01-09 and one callout per shot
    rooms = [(1, "Ruang menunggu", 1, 3), (2, "Kaunter", 3, 6), (3, "Waiting area 2", 6, 7), (4, "Toilet pesakit", 7, 8),
             (5, "Bilik OT", 8, 11), (6, "Bilik treatment", 11, 12), (7, "Konsultasi & doktor", 12, 14),
             (8, "Utility sink", 14, 16), (9, "Pantry staf", 16, 17)]
    for i, title, k0, k1 in rooms:
        c.section(i, 9, title, T[k0], T[k1] - T[k0])
    calls = {1: "Nature + minimalis", 2: "Lounge selesa", 3: "Kaunter premium", 4: "Siling curving + LED",
             5: "Curving elemen kayu", 6: "Lantai two-tone", 7: "Tiles two-tone", 8: "Mini OT",
             9: "Hair transplant", 10: "Kabinet · top quartz stone", 11: "Lampu arch feature",
             12: "Bilik konsultasi", 13: "Bilik doktor", 14: "Syarat klinik estetik", 15: "Feature slat kayu",
             16: "Top quartz stone"}
    for k, text in calls.items():
        s, d = at[k]
        c.pill(text, s + 0.25, d - 0.3, y=1480)
        c.sfx("pop", s + 0.25, 0.35)

    # recap over the lobby wide, then the CTA
    s, d = at[17]
    c.hook2("Luma Clinic · Petaling Jaya", "Design &amp;<br>build A–Z", "siap dari kosong sampai beroperasi ✨", s + 0.1, d - 0.1)
    c.image(PH + "IMG_5536.jpg", A, END)
    c.ckaps_end(A, END)
    c.write(OUT + "c9-full-klinik.html", "Luma Clinic: full tour bawah 60 saat")
    print(f"total {A + END:.2f}s")


if __name__ == "__main__":
    build()
