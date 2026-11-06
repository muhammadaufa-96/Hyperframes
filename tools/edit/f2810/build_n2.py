"""5/11/26: airport vlog at 5am, "owner bisnes tak ada cuti".
usage: python3 build_n2.py   (needs f2810/edit/aroll_n2.mp4 + n2_segs.json + chk/n2/words.json)"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build_2810 as b
from build_2810 import base, find, finish, F, END

b.HOT |= {"owner", "business", "cuti", "24", "jam", "5", "pagi", "check-in", "gate", "urusan", "kerja", "untung", "susun",
          "masa", "sendiri", "keras", "25", "sehari", "mengeluh", "rezeki", "keluarga", "setuju", "like", "share"}


def n2():
    c, segs, sp, w, A = base("n2", "n2-owner-tak-cuti")
    h0, h1 = sp["hook"]
    c.hook2("Realiti entrepreneur", "Owner bisnes<br>tak ada cuti", "pagi, petang, malam", 0.05, min(3.6, h1 - 0.1))

    # context: 5am at the airport
    x0, x1 = sp["ctx"]
    c.whip(x0)
    c.broll(F + "IMG_5867.mp4", x0, 2.6, media_start=0.5, zoom=(1.0, 1.08))
    c.chip("05:00 pagi", x0 + 0.15, 2.4, x=70, y=300, yellow=True)
    tc = find(w, "check-in", x0)
    c.whip(tc - 0.3)
    c.broll(F + "IMG_5863.mp4", tc - 0.3, 3.0, media_start=7.0, zoom=(1.0, 1.06))
    tu = find(w, "urusan", x0)
    c.pin("Airport", "Urusan kerja", tu - 0.2, x1 - tu + 0.2, top=420)

    # myth
    m0, m1 = sp["mitos"]
    c.whip(m0)
    c.glass("Mitos", ["Untung", "Susun masa sendiri", "Cuti sendiri"], m0 + 1.0, m1 - m0 - 0.9,
            at=[find(w, "untung", m0), find(w, "susun", m0), find(w, "cuti", m0)],
            icons=[("✕", "w"), ("✕", "w"), ("✕", "w")], top=420)
    c.sfx("error", find(w, "untung", m0), 0.3)

    # reality: quick cuts of real site work from the other folders
    r0, r1 = sp["realiti"]
    c.whip(r0)
    tk = find(w, "takkan", r0)
    cuts = [("IMG_5842.mp4", 3.0), ("IMG_9208_c.mp4", 22.0), ("IMG_1004_o.mp4", 4.5), ("IMG_5841.mp4", 8.0), ("IMG_5840.mp4", 9.0)]
    t = tk - 0.2
    for src, ms in cuts:
        c.broll(F + src, t, 1.25, media_start=ms, zoom=(1.0, 1.05))
        c.sfx("click-soft", t, 0.3)
        t += 1.25
    c.glass("Realiti", ["Tak ada cuti", "Kerja 25 jam sehari", "Tak boleh mengeluh", "Cari rezeki untuk keluarga"], tk - 0.1, r1 - tk + 0.1,
            at=[find(w, "cuti", r0), find(w, "25", r0), find(w, "mengeluh", r0), find(w, "keluarga", r0)], top=420)

    # close: ask the viewer
    k0, k1 = sp["close"]
    c.whip(k0)
    ts = find(w, "setuju", k0)
    c.comment("Setuju tak dengan statement ni?", ts - 0.3, k1 - ts + 0.3, ts)

    # natural CTA, then the follow card
    q0, q1 = sp["cta"]
    c.whip(q0)
    tl = find(w, "like", q0)
    c.pill("Like · Share", tl - 0.1, 2.2, y=1480)
    c.sfx("pop", tl - 0.1, 0.35)
    c.follow_end(A, END)
    finish(c, w, A, "n2-owner-tak-cuti.html", "5/11: Owner bisnes tak ada cuti (airport 5 pagi)", end=None,
           bg=F + "IMG_5867.mp4", bg_ms=2.0)


if __name__ == "__main__":
    n2()
