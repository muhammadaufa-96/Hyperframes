"""Luma Clinic car vlog: driving to see the finished project, with flashbacks to the
pet shop, the 3D design and the renovation, then before/after reveals.
No voice: on-screen subtitles + sound effects only; the client adds their own music.
usage: python3 build_vlog.py"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
from kit import K
import gen
from build_2810 import brate, F, PH, OUT, END

LU = "../assets/footage/luma/"

gen.CSS += r"""
/* Story subtitles: sentence case, key words in yellow */
.vsub { position: absolute; left: 70px; right: 70px; top: 1160px; text-align: center; font-weight: 800; font-size: 60px; line-height: 1.15;
        color: #fff; background: rgba(15,17,20,0.74); border-radius: 22px; padding: 20px 24px 24px; text-shadow: 0 3px 0 rgba(0,0,0,0.35); }
.vsub span { display: inline-block; margin: 0 8px; }
.vsub em { font-style: normal; color: #f5c22e; }
/* VHS rewind overlay */
.vhs { position: absolute; inset: 0; background: repeating-linear-gradient(0deg, rgba(255,255,255,0.08) 0 2px, rgba(0,0,0,0.12) 2px 6px); mix-blend-mode: overlay; }
.vhs-t { position: absolute; left: 70px; top: 160px; font-weight: 800; font-size: 58px; color: #fff; letter-spacing: 0.06em; text-shadow: 3px 0 #ff2b55, -3px 0 #22d3ee; }
.tagb { position: absolute; top: 300px; left: 0; right: 0; display: flex; justify-content: center; }
.tagb span { font-weight: 800; font-size: 46px; padding: 12px 30px; border-radius: 10px; letter-spacing: 0.08em; }
.tagb .d { background: #e11d48; color: #fff; }
.tagb .s { background: #f5c22e; color: #15171a; }
"""


def sub(c, html, start, dur):
    """Subtitle line; words pop in one after another."""
    s = c.uid("vs")
    words = html.split(" ")
    spans = "".join(f'<span id="{s}w{i}">{w}</span>' for i, w in enumerate(words))
    c.layers.append(f'<section id="{s}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="8"><div class="vsub">{spans}</div></section>')
    for i in range(len(words)):
        c.js.append(f'tl.fromTo("#{s}w{i}", {{ y: 24, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.18, ease: "back.out(2)" }}, {start + 0.05 + i * 0.07:.3f});')
    c.js.append(f'tl.to("#{s} .vsub", {{ opacity: 0, duration: 0.18 }}, {start + dur - 0.18:.3f});')


def rewind(c, t, dur=1.0):
    r = c.uid("rw")
    c.layers.append(f'<section id="{r}" class="clip" data-start="{t:.3f}" data-duration="{dur:.3f}" data-track-index="7"><div class="vhs" id="{r}v"></div>'
                    f'<div class="vhs-t" id="{r}t">◀◀ REWIND</div></section>')
    c.js.append(f'tl.fromTo("#{r}v", {{ opacity: 1, y: 0 }}, {{ opacity: 0.3, y: 40, duration: {dur:.3f}, ease: "none" }}, {t:.3f});')
    c.js.append(f'tl.fromTo("#{r}t", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.08, repeat: 5, yoyo: true }}, {t:.3f});')
    c.sfx("glitch-2", t, 0.5)
    c.sfx("whoosh-cinematic", t, 0.35)


def tag(c, before, start, dur):
    g = c.uid("tb")
    cls, text = ("d", "DULU") if before else ("s", "SEKARANG")
    c.layers.append(f'<section id="{g}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6"><div class="tagb"><span class="{cls}" id="{g}s">{text}</span></div></section>')
    c.js.append(f'tl.fromTo("#{g}s", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "back.out(2.5)" }}, {start:.3f});')
    c.js.append(f'tl.to("#{g}s", {{ opacity: 0, duration: 0.15 }}, {start + dur - 0.15:.3f});')


def build():
    c = K("c10-vlog-luma", 0)
    t = 0.0

    def vid(src, a, b, rate=1.0, ms_dur=None):
        nonlocal t
        d = (b - a) / rate
        if rate == 1.0:
            c.broll(src, t, d, media_start=a, zoom=(1.0, 1.06))
        else:
            brate(c, src, t, d, a, rate)
        s = t; t += d
        return s, d

    def img(src, d, zoom=(1.0, 1.1)):
        nonlocal t
        c.image(src, t, d, zoom=zoom)
        s = t; t += d
        return s, d

    # 1. in the car
    s, d = vid(F + "IMG_5528.mp4", 4.5, 8.1)
    c.hook2("POV:", "OTW tengok<br>projek siap", "klinik estetik yang kita renovate", 0.05, d - 0.1)
    c.sfx("click-soft", 0.0, 0.4)

    # 2. flashback: pet shop
    s, d = img(LU + "IMG_1008.jpg", 2.8)
    rewind(c, s, 0.9)
    tag(c, True, s + 0.6, d - 0.7)
    sub(c, "Ingat lagi... dulu tempat ni <em>kedai</em> <em>pet</em>", s + 0.7, d - 0.75)

    # 3. the 3D design
    s, d = img(LU + "r_sofa.jpg", 2.9, zoom=(1.05, 1.15))
    c.whip(s)
    c.chip("Design 3D", s + 0.1, d - 0.2, x=70, y=300, yellow=True)
    sub(c, "Client nak buka <em>klinik</em> <em>estetik</em>, kita design 3D dulu", s + 0.2, d - 0.25)

    # 4. renovation
    s, d = vid(F + "IMG_1004.mp4", 4.0, 15.0, 2.0)
    c.whip(s)
    sub(c, "Lepas tu... <em>renovate</em> bermula", s + 0.2, 2.6)
    sub(c, "Kosong. Berhabuk. Board dan simen.", s + 2.9, d - 2.95)
    s, d = img(LU + "IMG_1006.jpg", 2.4)
    c.whip(s)
    sub(c, "Dinding <em>curving</em> dibentuk satu-satu", s + 0.15, d - 0.2)
    s, d = vid(F + "IMG_1003.mp4", 0.2, 3.6, 1.4)
    c.whip(s)
    sub(c, "<em>Skim</em> <em>coat</em> siling sampai licin", s + 0.15, d - 0.2)

    # 5. time skip back in the car
    s, d = vid(F + "IMG_5528.mp4", 0.6, 2.4)
    c.whip(s)
    c.chip("⏩ Beberapa bulan kemudian", s + 0.1, d - 0.15, x=70, y=300)
    c.sfx("riser", s, 0.3, dur=d)

    # 6. arrive: pet shop -> Luma
    s, d = img(LU + "IMG_1008.jpg", 1.2, zoom=(1.0, 1.04))
    tag(c, True, s, d)
    s2, d2 = vid(F + "IMG_5530.mp4", 0.0, 3.0)
    c.wipe(s2)
    tag(c, False, s2 + 0.1, 1.0)
    c.hook2("Dan hari ni...", "Siap!", "Luma Clinic, Petaling Jaya", s2 + 1.0, d2 - 1.05, shade=False)
    c.sfx("sparkle", s2 + 1.1, 0.45)

    # 7. before / after pairs
    pairs = [(LU + "r_sofa.jpg", PH + "IMG_5536.jpg", "<em>3D</em> vs <em>siap</em>: ruang menunggu"),
             (LU + "IMG_1007_b.jpg", PH + "IMG_5554.jpg", "Laluan arch jadi <em>curving</em> <em>kayu</em> + lampu"),
             (LU + "r_wait2.jpg", PH + "IMG_5535.jpg", "Kaunter <em>registration</em> sama macam design")]
    for b, a, text in pairs:
        s, d = img(b, 1.2, zoom=(1.0, 1.04))
        c.whip(s)
        tag(c, True, s, d)
        s2, d2 = img(a, 2.3)
        c.wipe(s2)
        tag(c, False, s2 + 0.05, d2 - 0.1)
        sub(c, text, s, d + d2 - 0.05)

    # 8. quick walk
    w0 = t
    for src, a, b, rate, label in [(F + "IMG_5559.mp4", 8.0, 15.0, 2.5, "Siling curving + LED"),
                                   (F + "IMG_5565.mp4", 10.0, 15.0, 2.0, "Bilik OT"),
                                   (F + "IMG_5564.mp4", 11.0, 21.0, 3.0, "Toilet two-tone")]:
        s, d = vid(src, a, b, rate)
        c.whip(s)
        c.pill(label, s + 0.2, d - 0.3, y=1480)
        c.sfx("pop", s + 0.2, 0.35)
    c.chip("9 bilik siap A–Z", w0 + 0.1, t - w0 - 0.2, x=70, y=300, yellow=True)

    # 9. closing line, then CTA
    s, d = img(PH + "IMG_5537.jpg", 3.2, zoom=(1.15, 1.0))
    c.whip(s)
    c.hook2("Dari kedai kosong", "Klinik<br>estetik", "dan dah pun beroperasi", s + 0.1, d - 0.1)
    A = t
    c.duration = A + END
    c.shade(0, A + END)
    c.image(PH + "IMG_5536.jpg", A, END)
    c.ckaps_end(A, END)
    c.write(OUT + "c10-vlog-luma.html", "Luma Clinic: vlog OTW tengok projek siap")
    print(f"total {A + END:.2f}s")


if __name__ == "__main__":
    build()
