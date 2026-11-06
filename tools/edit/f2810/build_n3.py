"""6/11/26: contractor's review of The Dolomites / Valley Market, Sentul.
usage: python3 build_n3.py   (needs f2810/edit/aroll_n3.mp4 + n3_segs.json + chk/n3/words.json)"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build_2810 as b
from build_2810 import base, find, finish, F, END

b.HOT |= {"sentul", "hd", "pemandangan", "english", "cottage", "view", "makanan", "sirloin", "environment", "workflow",
          "9.5", "7", "kurang", "win", "konsep", "design", "description", "location", "like", "share"}
P6 = "../assets/footage/f0611/"


def n3():
    c, segs, sp, w, A = base("n3", "n3-dolomites-review")
    # opening: walking outside, "kita dekat mana?"
    i0, i1 = sp["intro"]
    c.hook2("Kontraktor review kafe", "9.5/10<br>untuk design", "tapi makanan…?", 0.05, 3.1)
    tv = find(w, "valley", i0)
    c.pin("The Dolomites", "Valley Market · Sentul", tv - 0.2, i1 - tv + 0.1, top=420)

    # the view: windmill, then the mountains
    v0, v1 = sp["view"]
    c.whip(v0)
    c.broll(F + "IMG_6081.mp4", v0, min(3.2, v1 - v0), media_start=1.0, zoom=(1.0, 1.08))
    w0, w1 = sp["view2"]
    c.whip(w0)
    tg = find(w, "pergunungan", w0)
    c.broll(F + "IMG_6006.mp4", tg - 0.3, 3.0, media_start=5.5, zoom=(1.1, 1.0))
    c.chip("Pemandangan gunung", tg - 0.1, 2.7, x=70, y=300, yellow=True)

    # quick photo montage of the place while he describes the vibe
    k0, k1 = sp["cottage"]
    c.whip(k0)
    te = find(w, "english", k0)
    c.broll(F + "IMG_5954.mp4", te - 0.3, 2.6, media_start=2.0, zoom=(1.0, 1.06))
    c.chip("English cottage", te, 2.2, x=70, y=300, yellow=True)
    tv = find(w, "view", k0)
    t = tv - 0.2
    for img in ["IMG_6123", "IMG_6022", "IMG_6089", "IMG_6014"]:
        c.image(P6 + img + ".jpg", t, 0.85, zoom=(1.0, 1.08))
        c.whip(t)
        t += 0.85
    c.broll(F + "IMG_6007.mp4", t, max(0.6, k1 - t), media_start=2.0, zoom=(1.0, 1.06))

    # food + ratings
    r0, r1 = sp["rate"]
    c.whip(r0)
    c.broll(F + "IMG_5978.mp4", r0, 2.6, media_start=0.3, zoom=(1.0, 1.1))
    c.pill("Sirloin", find(w, "sirloin", r0) - 0.1, 1.8, y=1480)
    t95 = find(w, "9.5", r0)
    t7 = find(w, "7", r0)
    c.chip("Environment & workflow", t95 - 0.5, t7 - t95 - 0.2, x=70, y=140)
    c.rating([], 9.5, t95 - 0.4, t7 - t95, top=420)
    c.chip("Makanan & servis", t7 - 0.4, 2.8, x=70, y=140)
    c.rating([], 7.0, t7 - 0.3, 2.9, top=420)
    tw = find(w, "win", r0)
    c.glass("Kenapa dia win", ["Workflow lancar", "Konsep design kuat"], tw - 0.2, r1 - tw + 0.2,
            at=[find(w, "workflow", tw - 0.1), find(w, "konsep", tw)], top=420)

    # natural CTA, then the follow card
    q0, q1 = sp["cta"]
    c.whip(q0)
    tl = find(w, "location", q0)
    c.pill("Location dalam description", tl - 0.4, 2.4, y=1480)
    c.sfx("pop", tl - 0.4, 0.35)
    tk = find(w, "like", q0)
    c.pill("Like · Share", tk - 0.1, 2.0, y=1480)
    c.sfx("pop", tk - 0.1, 0.35)
    # ending over the outdoor walk
    c.broll(F + "IMG_6005.mp4", q0, 5.5, media_start=0.5, zoom=(1.0, 1.06))
    c.whip(q0 + 5.5)
    c.broll(F + "IMG_6007.mp4", q0 + 5.5, 3.6, media_start=2.0, zoom=(1.0, 1.06))
    c.whip(q0 + 9.1)
    c.broll(F + "IMG_6005.mp4", q0 + 9.1, q1 - q0 - 9.1, media_start=33.5, zoom=(1.0, 1.06))
    c.follow_end(A, END)
    finish(c, w, A, "n3-dolomites-review.html", "6/11: Kontraktor review The Dolomites, Sentul", end=None,
           bg=F + "IMG_6081.mp4", bg_ms=2.0)


if __name__ == "__main__":
    n3()
