"""6/11/26 (v4): The Dolomites / Valley Market, Sentul. The v2 walk-and-views structure with the
IMG_5981 hook up front, and more scenery / walking / house b-roll. Earlier cuts: build_n3_v2.py, build_n3_v3.py.
usage: python3 build_n3.py   (needs f2810/edit/aroll_n3.mp4 + n3_segs.json + chk/n3/words.json)"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build_2810 as b
from build_2810 import base, find, finish, F, END

b.HOT |= {"percaya", "masyaallah", "pemandangan", "indah", "valley", "market", "spot", "restoran", "wow", "pergunungan",
          "english", "cottage", "view", "makanan", "sirloin", "environment", "workflow", "9.5", "7", "kurang", "win",
          "konsep", "design", "description", "location", "like", "share"}
P6 = "../assets/footage/f0611/"


def cuts(c, t, items):
    """Back-to-back b-roll with a whip on each cut. items: (src, media_start, dur) or (photo.jpg, None, dur)."""
    for src, ms, d in items:
        if ms is None:
            c.image(P6 + src, t, d, zoom=(1.0, 1.08))
        else:
            c.broll(F + src, t, d, media_start=ms, zoom=(1.0, 1.06))
        c.whip(t)
        t += d
    return t


def n3():
    c, segs, sp, w, A = base("n3", "n3-dolomites-review")

    # hook (IMG_5981) + review title
    h0, h1 = sp["hook"]
    c.hook2("Kontraktor review kafe", "9.5/10<br>untuk design", "tapi makanan…?", 0.05, 3.1)
    tp = find(w, "pemandangan", h0)
    cuts(c, tp - 0.2, [("IMG_6006.mp4", 5.5, 1.6), ("IMG_5953.mp4", 23.0, h1 - tp - 1.4)])

    # walking in: "kita dekat mana? Valley Market"
    i0, i1 = sp["intro"]
    c.whip(i0)
    tv = find(w, "valley", i0)
    c.pin("The Dolomites", "Valley Market · Sentul", tv - 0.2, i1 - tv + 0.1, top=420)
    ts = find(w, "spot", i0)
    cuts(c, ts - 0.2, [("IMG_6009.mp4", 1.5, 1.6), ("IMG_6004.jpg", None, 1.0), ("IMG_6081.mp4", 1.0, i1 - ts - 2.4)])

    # the views
    o0, o1 = sp["wow"]
    c.whip(o0)
    cuts(c, o0 + 0.9, [("IMG_6006.mp4", 1.0, o1 - o0 - 0.9)])
    v0, v1 = sp["view2"]
    c.whip(v0)
    tg = find(w, "pergunungan", v0)
    c.broll(F + "IMG_5953.mp4", tg - 0.3, 2.2, media_start=27.0, zoom=(1.1, 1.0))
    c.chip("Pemandangan gunung", tg - 0.1, 2.0, x=70, y=300, yellow=True)
    tr = find(w, "restoran", v0)
    cuts(c, tr - 0.1, [("IMG_6007.mp4", 2.5, v1 - tr + 0.1)])

    # English cottage + photo montage
    k0, k1 = sp["cottage"]
    c.whip(k0)
    te = find(w, "english", k0)
    c.broll(F + "IMG_5954.mp4", te - 0.3, 2.6, media_start=2.0, zoom=(1.0, 1.06))
    c.chip("English cottage", te, 2.2, x=70, y=300, yellow=True)
    tw = find(w, "view", k0)
    t = cuts(c, tw - 0.2, [("IMG_6123.jpg", None, 0.85), ("IMG_6022.jpg", None, 0.85), ("IMG_6089.jpg", None, 0.85),
                           ("IMG_6014.jpg", None, 0.85)])
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
    tn = find(w, "win", r0)
    c.glass("Kenapa dia win", ["Workflow lancar", "Konsep design kuat"], tn - 0.2, r1 - tn + 0.2,
            at=[find(w, "workflow", tn - 0.1), find(w, "konsep", tn)], top=420)

    # ending over the outdoor walk: path, houses, windmill, mountains
    q0, q1 = sp["cta"]
    c.whip(q0)
    seq = [("IMG_6005.mp4", 0.5, 3.6), ("IMG_6009.mp4", 3.0, 2.4), ("IMG_6007.mp4", 2.0, 2.6), ("IMG_6081.mp4", 0.5, 2.4),
           ("IMG_5981.mp4", 21.0, 2.6)]
    used = sum(d for _, _, d in seq)
    seq.append(("IMG_6005.mp4", 33.5, max(0.8, q1 - q0 - used)))
    cuts(c, q0, seq)
    tl = find(w, "location", q0)
    c.pill("Location dalam description", tl - 0.4, 2.4, y=1480)
    c.sfx("pop", tl - 0.4, 0.35)
    tk = find(w, "like", q0)
    c.pill("Like · Share", tk - 0.1, 2.0, y=1480)
    c.sfx("pop", tk - 0.1, 0.35)
    c.follow_end(A, END)
    finish(c, w, A, "n3-dolomites-review.html", "6/11: Kontraktor review The Dolomites, Sentul", end=None,
           bg=F + "IMG_6081.mp4", bg_ms=2.0)


if __name__ == "__main__":
    n3()
