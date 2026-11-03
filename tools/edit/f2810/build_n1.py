"""4/11/26: site marking at the Puncak Alam boutique (talking A-roll + site b-roll).
usage: python3 build_n1.py   (needs f2810/edit/aroll_n1.mp4 + n1_segs.json + chk/n1/words.json)"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build_2810 as b
from build_2810 import base, find, finish, F, END

b.HOT |= {"marking", "sizing", "tepat", "layout", "confirm", "confirmation", "klien", "puncak", "alam", "butik",
          "nantikan", "hasil", "commercial", "renovation", "follow", "like", "share"}
P4 = "../assets/footage/f0411/"


def n1():
    c, segs, sp, w, A = base("n1", "n1-marking-butik")
    h0, h1 = sp["hook"]
    c.hook2("Kontraktor masuk site…", "Step #1<br>bukan terus bina", "ni yang kita buat dulu", 0.05, min(3.0, h1 - 0.1))

    # marking
    tm = find(w, "marking", h0)
    c.whip(tm - 0.1)
    c.broll(F + "IMG_5842.mp4", tm - 0.1, h1 - tm + 0.1, media_start=3.0, zoom=(1.0, 1.08))
    c.pill("Marking dulu", tm + 0.1, h1 - tm - 0.2, y=1480)
    c.sfx("pop", tm + 0.1, 0.35)

    # sizing: door opening discussion
    s0, s1 = sp["size"]
    c.whip(s0)
    c.broll(F + "IMG_5840.mp4", s0, s1 - s0 + 0.4, media_start=6.5, zoom=(1.0, 1.06))
    c.glass("Saiz pintu standard", ["Tinggi 83 inci", "Lebar 34 inci"], s0, s1 - s0 + 0.4,
            at=[find(w, "sizing", s0), find(w, "tepat", s0)], top=420)

    # layout: plan (client name blurred), then the checklist over the A-roll
    l0, l1 = sp["layout"]
    tl = find(w, "layout", l0)
    c.whip(tl - 0.15)
    c.image(P4 + "plan_b.jpg", tl - 0.15, 3.2, zoom=(1.0, 1.12), fit="contain", bg="#f3efe9")
    c.sfx("whoosh-short", tl - 0.2, 0.35)
    k0 = tl + 3.1
    c.glass("Sebelum jalan kerja", ["Marking", "Sizing tepat", "Layout confirm", "Klien approve"], k0, l1 - k0 + 0.2,
            at=[k0 + 0.3, k0 + 0.9, k0 + 1.5, find(w, "confirmation", l0)], top=420)

    # on site: Puncak Alam boutique
    p0, p1 = sp["site"]
    c.whip(p0)
    tp = find(w, "puncak", p0)
    c.pin("Puncak Alam", "Projek butik", tp - 0.2, 2.6, top=420)
    tb = find(w, "butik", p0)
    c.broll(F + "IMG_5841.mp4", tb - 0.3, 2.6, media_start=5.5, zoom=(1.0, 1.06))
    c.chip("Arch", tb - 0.1, 1.2, x=90, y=760)
    c.chip("Platform", tb + 0.9, 1.4, x=520, y=980)
    tn = find(w, "nantikan", p0)
    c.broll(F + "IMG_5839.mp4", tn - 0.2, p1 - tn + 0.3, media_start=0.3, zoom=(1.0, 1.08))
    c.chip("Nantikan part 2", tn, p1 - tn + 0.1, x=70, y=300, yellow=True)

    # CTA kept natural, then the follow card
    q0, q1 = sp["cta"]
    c.whip(q0)
    tk = find(w, "like", q0)
    c.pill("Like · Share · Follow", tk - 0.1, 2.4, y=1480)
    c.sfx("pop", tk - 0.1, 0.35)
    c.follow_end(A, END)
    finish(c, w, A, "n1-marking-butik.html", "4/11: Marking dulu sebelum jalan kerja (butik Puncak Alam)", end=None,
           bg=F + "IMG_5839.mp4", bg_ms=2.0)


if __name__ == "__main__":
    n1()
