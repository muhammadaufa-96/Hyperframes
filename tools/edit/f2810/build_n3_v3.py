"""6/11/26 (v3): The Dolomites / Valley Market, Sentul, told from the outdoor walk (IMG_5981)
with the cafe rating in the middle. The earlier cut is kept in build_n3_v2.py.
usage: python3 build_n3.py   (needs f2810/edit/aroll_n3.mp4 + n3_segs.json + chk/n3/words.json)"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build_2810 as b
from build_2810 import base, find, finish, F, END

b.HOT |= {"percaya", "pemandangan", "indah", "end", "zealand", "jiran", "eropah", "best", "english", "cottage", "sirloin",
          "environment", "workflow", "9.5", "7", "kurang", "win", "konsep", "design", "gempak", "quality", "food",
          "sentul", "indonesia", "komen", "jakarta", "rugi"}
P6 = "../assets/footage/f0611/"


def n3():
    c, segs, sp, w, A = base("n3", "n3-dolomites-review")

    # hook: his own line, plus the review title
    h0, h1 = sp["hook"]
    c.hook2("Kontraktor review kafe", "9.5/10<br>untuk design", "tapi makanan…?", 0.05, 3.1)
    ts = find(w, "stay", h0)
    c.chip("Location kat hujung video", ts - 0.1, h1 - ts + 0.1, x=70, y=300, yellow=True)

    # wow: the view
    o0, o1 = sp["wow"]
    c.whip(o0)
    c.broll(F + "IMG_6006.mp4", o0, o1 - o0, media_start=5.5, zoom=(1.1, 1.0))

    # "New Zealand?" -> neighbour country built like Europe
    n0, n1 = sp["nz"]
    c.whip(n0)
    tz = find(w, "zealand", n0)
    c.chip("New Zealand?", tz - 0.6, 1.8, x=70, y=300)
    tj = find(w, "jiran", n0)
    c.chip("Negara jiran je", tj - 0.3, 2.0, x=70, y=300, yellow=True)
    te = find(w, "eropah", n0)
    t = te - 0.3
    for img in ["IMG_6123", "IMG_6022", "IMG_6089", "IMG_6014"]:
        c.image(P6 + img + ".jpg", t, 0.9, zoom=(1.0, 1.08))
        c.whip(t)
        t += 0.9
    c.broll(F + "IMG_6081.mp4", t, 2.4, media_start=1.0, zoom=(1.0, 1.06))
    tc = find(w, "english", n0)
    c.broll(F + "IMG_5954.mp4", tc - 0.8, n1 - tc + 0.8, media_start=2.0, zoom=(1.0, 1.06))
    c.chip("English cottage", tc - 0.2, n1 - tc + 0.1, x=70, y=300, yellow=True)

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

    # back outside: food should match the place
    g0, g1 = sp["gempak"]
    c.whip(g0)
    tq = find(w, "quality", g0)
    c.glass("Tempat gempak, kena jaga", ["Quality of food", "Food presentation"], tq - 0.3, g1 - tq + 0.3,
            at=[tq, find(w, "presentation", g0)], icons=[("!", "w"), ("!", "w")], top=420)

    # ending on the walk: location reveal, then the follow card
    e0, e1 = sp["end"]
    c.whip(e0)
    tl = find(w, "sentul", e0)
    c.pin("The Dolomites", "Sentul, Indonesia", tl - 0.3, 4.0, top=420)
    c.sfx("sparkle", tl - 0.2, 0.4)
    tk = find(w, "komen", e0)
    c.pill("Location kat komen", tk - 0.2, 2.2, y=1480)
    c.sfx("pop", tk - 0.2, 0.35)
    c.follow_end(A, END)
    finish(c, w, A, "n3-dolomites-review.html", "6/11: Kontraktor review The Dolomites, Sentul", end=None,
           bg=F + "IMG_6081.mp4", bg_ms=2.0)


if __name__ == "__main__":
    n3()
