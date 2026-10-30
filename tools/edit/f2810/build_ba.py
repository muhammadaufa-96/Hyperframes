"""Luma Clinic before & after, told in three acts like the Mediq reference reel:
BEFORE (the old pet-shop unit) -> PROSES (renovation) -> AFTER (walk-through with the reason behind each element).
No voice: narrative captions + soft sound effects; the client adds their own music.
usage: python3 build_ba.py"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
from kit import K
import gen
from build_2810 import brate, F, PH, OUT, END

LU = "../assets/footage/luma/"

gen.CSS += r"""
/* Narrative caption: white box, top-left, Enoxin-yellow accent */
.nar { position: absolute; left: 64px; top: 250px; max-width: 800px; border-left: 10px solid #f5c22e; }
.nar::after { content: ""; position: absolute; left: -10px; bottom: -10px; width: 120px; height: 10px; background: #f5c22e; }
.nar .bx { background: #ffffff; padding: 20px 26px 22px; box-shadow: 0 14px 34px rgba(0,0,0,0.28); }
.nar .k { display: block; font-weight: 800; font-size: 28px; letter-spacing: 0.12em; text-transform: uppercase; color: #a8810a; margin-bottom: 8px; }
.nar .t { display: block; font-weight: 800; font-style: italic; font-size: 42px; line-height: 1.24; color: #15171a; }
/* Opening title */
.bat { position: absolute; left: 0; right: 0; top: 1060px; text-align: center; padding: 34px 0 40px; background: linear-gradient(180deg, rgba(10,12,15,0) 0%, rgba(10,12,15,0.72) 22%, rgba(10,12,15,0.72) 78%, rgba(10,12,15,0) 100%); }
.bat .a { display: block; font-weight: 800; font-size: 120px; line-height: 1; color: #fff; text-shadow: 0 6px 0 rgba(0,0,0,0.35), 0 0 40px rgba(0,0,0,0.5); }
.bat .b { display: block; font-weight: 800; font-size: 84px; line-height: 1.1; color: #f5c22e; text-shadow: 0 5px 0 rgba(0,0,0,0.35), 0 0 30px rgba(0,0,0,0.5); }
.flw { position: absolute; inset: 0; background: #fff; }
"""


def nar(c, kicker, text, start, dur):
    n = c.uid("nr")
    k = f'<span class="k">{kicker}</span>' if kicker else ""
    c.layers.append(f'<section id="{n}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="8">'
                    f'<div class="nar" id="{n}n"><div class="bx" id="{n}b">{k}<span class="t" id="{n}t">{text}</span></div></div></section>')
    c.js.append(f'tl.fromTo("#{n}b", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 0.45, ease: "power3.out" }}, {start:.3f});')
    c.js.append(f'tl.fromTo("#{n}t", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.4 }}, {start + 0.25:.3f});')
    c.js.append(f'tl.to("#{n}n", {{ opacity: 0, duration: 0.25 }}, {start + dur - 0.25:.3f});')
    c.sfx("click-soft", start, 0.3)


def flash(c, t, dur=0.5):
    f = c.uid("fw")
    c.layers.append(f'<section id="{f}" class="clip" data-start="{t - 0.1:.3f}" data-duration="{dur:.3f}" data-track-index="7"><div class="flw" id="{f}x"></div></section>')
    c.js.append(f'tl.fromTo("#{f}x", {{ opacity: 0.95 }}, {{ opacity: 0, duration: {dur - 0.1:.3f}, ease: "power2.out" }}, {t:.3f});')


def build():
    c = K("c11-before-after-luma", 0)
    t = 0.0

    def vid(src, a, b, rate=1.0):
        nonlocal t
        d = (b - a) / rate
        if rate == 1.0:
            c.broll(src, t, d, media_start=a, zoom=(1.0, 1.05))
        else:
            brate(c, src, t, d, a, rate, zoom=(1.0, 1.05))
        s = t; t += d
        return s, d

    def img(src, d, zoom=(1.0, 1.08)):
        nonlocal t
        c.image(src, t, d, zoom=zoom)
        s = t; t += d
        return s, d

    # ---- BEFORE ---------------------------------------------------------
    s, d = img(LU + "IMG_1008.jpg", 4.2, zoom=(1.12, 1.0))
    ti = c.uid("ti")
    c.layers.append(f'<section id="{ti}" class="clip" data-start="0.050" data-duration="2.000" data-track-index="8">'
                    f'<div class="bat"><span class="a" id="{ti}a">Before &amp; After</span><span class="b" id="{ti}b">Luma Clinic</span></div></section>')
    c.js.append(f'tl.fromTo("#{ti}a", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "power3.out" }}, 0.05);')
    c.js.append(f'tl.fromTo("#{ti}b", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "power3.out" }}, 0.25);')
    c.js.append(f'tl.to("#{ti} .bat", {{ opacity: 0, duration: 0.3 }}, 1.75);')
    c.sfx("whoosh-cinematic", 0.0, 0.4)
    c.sfx("impact-bass-1", 0.2, 0.35)
    nar(c, "", "Dulunya sebuah kedai haiwan peliharaan di Petaling Jaya.", 2.0, d - 2.05)

    s, d = vid(F + "IMG_8773_c.mp4", 1.0, 16.0, 3.0)
    s2, d2 = vid(F + "IMG_8772_c.mp4", 12.0, 24.0, 3.0)
    nar(c, "", "Ruang terbuka, toilet lama, dinding kosong.", s + 0.2, d - 0.3)
    nar(c, "", "Tapi kami nampak potensinya.", s2 + 0.2, d2 - 0.3)
    s, d = vid(F + "IMG_8772_c.mp4", 1.0, 8.0, 2.33)
    nar(c, "", "Semua bermula dengan satu layout.", s + 0.2, d - 0.3)

    # ---- PROSES ---------------------------------------------------------
    s, d = vid(F + "IMG_9207_c.mp4", 0.0, 5.0, 2.0)
    c.sfx("whoosh-short", s, 0.35)
    s2, d2 = vid(F + "IMG_9208_c.mp4", 0.0, 36.0, 6.0)
    nar(c, "Proses", "Yang lama dibongkar. Ruang dibina semula, satu demi satu.", s + 0.2, d + d2 - 0.3)
    s, d = vid(F + "IMG_9209_c.mp4", 1.0, 6.0, 2.0)
    s2, d2 = vid(F + "IMG_1004_o.mp4", 4.0, 13.0, 3.0)
    nar(c, "", "Ia boleh jadi lebih dari tempat rawatan. Ia boleh jadi satu pengalaman.", s + 0.2, d + d2 - 0.3)
    c.sfx("riser", t - 1.6, 0.35, dur=1.6)

    # ---- AFTER ----------------------------------------------------------
    s, d = vid(F + "IMG_5558.mp4", 0.3, 3.7)
    flash(c, s, 0.6)
    c.sfx("chime", s, 0.4)
    c.sfx("sparkle", s + 0.2, 0.35)
    nar(c, "Luma Clinic hari ini", "Designed with intention. Built with care.", s + 0.4, d - 0.45)

    areas = [
        ([("v", "IMG_5559.mp4", 0.0, 4.0, 1.3), ("i", "IMG_5536.jpg", 2.2)], "Ruang menunggu",
         "Konsep nature + minimalis, dinding texture paint. Supaya klien terus rasa tenang sebaik masuk."),
        ([("i", "IMG_5535.jpg", 2.3), ("v", "IMG_5559.mp4", 22.0, 28.0, 2.0)], "Kaunter",
         "Blockboard, bukan melamin: lebih tahan dan kemas. Elemen kayu curving di belakang jadi identiti klinik."),
        ([("v", "IMG_5559.mp4", 8.0, 15.0, 1.6)], "Siling",
         "Siling curving + L-box dengan lampu tersembunyi. Ambience yang buat klien rasa 'expensive'."),
        ([("v", "IMG_5565.mp4", 0.0, 9.0, 3.0), ("i", "IMG_5554.jpg", 2.2)], "Laluan treatment",
         "Lengkung kayu + lampu. Klien rasa masuk 'dimensi lain' sebelum sampai bilik rawatan."),
        ([("v", "IMG_5565.mp4", 10.0, 15.0, 1.7), ("v", "IMG_5565.mp4", 36.0, 42.0, 2.0)], "Bilik OT",
         "Bilik utama dijadikan mini OT untuk hair transplant. Kabinet custom, top quartz stone, soft close."),
        ([("v", "IMG_5564.mp4", 11.0, 21.0, 2.4)], "Toilet pesakit",
         "Dibuat tertutup supaya klien yang menunggu tak terbau. Tiles two-tone + tempat pegang."),
        ([("i", "IMG_5543.jpg", 2.0), ("i", "IMG_5567.jpg", 2.0)], "Utility sink",
         "Utility sink double + janitor. Syarat wajib klinik estetik."),
    ]
    for shots, kicker, text in areas:
        a0 = t
        for sh in shots:
            if sh[0] == "v":
                vid(F + sh[1], sh[2], sh[3], sh[4])
            else:
                img(PH + sh[1], sh[2])
        c.sfx("whoosh-short", a0, 0.3)
        nar(c, kicker, text, a0 + 0.2, t - a0 - 0.3)

    s, d = vid(F + "IMG_5530.mp4", 0.0, 4.2)
    nar(c, "", "Daripada kedai haiwan… kini klinik estetik yang dah beroperasi.", s + 0.3, d - 0.35)
    A = t
    c.duration = A + END
    c.shade(0, A + END)
    c.image(PH + "IMG_5536.jpg", A, END)
    c.ckaps_end(A, END)
    c.write(OUT + "c11-before-after-luma.html", "Luma Clinic: before & after")
    print(f"total {A + END:.2f}s  (after starts {s:.2f})")


if __name__ == "__main__":
    build()
