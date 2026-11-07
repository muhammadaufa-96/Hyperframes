"""7/11/26 Reel: Pagi Sore, Indonesia. Business lesson from a nasi padang chain (IMG_6221),
cut hook-first: the conflict line opens on the best interior shot, then the 3 basics with b-roll.
usage: python3 build_0711.py   (needs f0711/edit/aroll_r1.mp4 + r1_segs.json + chk/r1/words.json)"""
import json, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
from kit import K, align
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f0711")
from script0711 import SCRIPT

E = "/home/user/Hyperframes/f0711/edit/"
F = "../assets/footage/f0711/"
OUT = "/home/user/Hyperframes/compositions/"
END = 3.4
HOT = {"inovatif", "grow", "indonesia", "pagi", "sore", "padang", "tiga", "servis", "laju", "hospitality", "food",
       "sedap", "berebut", "environment", "ambience", "five", "star", "gap", "pelik-pelik", "pelanggan",
       "kelemahan-kelemahan", "competitors", "win", "stand"}


def find(w, token, after=0.0, nth=1):
    n = 0
    for x in w:
        if x[1] >= after - 0.05 and x[0].lower().strip(".,?!…") == token.lower():
            n += 1
            if n == nth:
                return x[1]
    raise KeyError(f"{token} after {after:.2f}")


def load(v):
    segs = json.load(open(f"{E}{v}_segs.json"))
    spans = {}
    for x in segs["segments"]:
        a, b = spans.get(x["tag"], (x["out_in"], x["out_out"]))
        spans[x["tag"]] = (min(a, x["out_in"]), max(b, x["out_out"]))
    asr = json.load(open(f"{E}chk/{v}/words.json"))
    script = {k: t for k, t in SCRIPT[v].items() if k in spans}
    return segs, spans, align(asr, script, spans)


def r1():
    segs, sp, w = load("r1")
    A = segs["duration"]
    c = K("p1-pagi-sore", A + END)
    c.aroll(F + "aroll_r1.mp4", [(0.0, A, 0.0)])
    # punch-in on jump cuts inside the same piece, reset on a new piece
    prev, z = None, 1.0
    for s in segs["segments"]:
        z = (1.1 if z == 1.0 else 1.0) if s["piece"] == prev else 1.0
        prev = s["piece"]
        c.js.append(f'tl.set("#acam", {{ scale: {z}, transformOrigin: "50% 40%" }}, {s["out_in"]:.3f});')

    # HOOK: best interior shot first, the conflict line over it, his face on the payoff
    a0, a1 = sp["hookA"]
    b0, b1 = sp["hookB"]
    c.broll(F + "IMG_6178.mp4", 0.0, a1, media_start=1.6, zoom=(1.12, 1.0))
    c.shade(0, A + END)
    c.hook2("Kedai nasi padang ni", "TAK ADA<br>INOVASI PELIK", "tapi dah grow satu Indonesia", 0.05, b1 - 0.1)
    c.whip(b0)

    # who: Pagi Sore
    i0, i1 = sp["intro"]
    c.whip(i0)
    tp = find(w, "pagi", i0)
    c.chip("Pagi Sore · Indonesia", tp - 0.1, i1 - tp + 0.1, x=70, y=300, yellow=True)
    tn = find(w, "nasi", i0)
    c.broll(F + "IMG_6180.mp4", tn - 0.2, i1 - tn + 0.2, media_start=3.2, zoom=(1.0, 1.08))

    # the 3 basics
    k0, k1 = sp["basic"]
    c.whip(k0)
    tt = find(w, "tiga", k0)
    c.counter(3, tt - 0.3, k1 - tt + 0.3, "perkara asas je", top=520)

    s0, s1 = sp["s1"]
    c.whip(s0)
    c.section(1, 3, "Servis", s0, s1 - s0)
    ts = find(w, "servis", s0, nth=2)
    c.broll(F + "IMG_6180.mp4", ts - 0.1, s1 - ts + 0.1, media_start=0.0, zoom=(1.0, 1.06))

    m0, _ = sp["s2a"]
    _, m1 = sp["s2b"]
    c.whip(m0)
    c.section(2, 3, "Makanan", m0, m1 - m0)
    tm = find(w, "makanan", m0)
    c.broll(F + "IMG_6180.mp4", tm - 0.1, m1 - tm + 0.1, media_start=2.6, zoom=(1.0, 1.12))

    e0, _ = sp["s3a"]
    _, e1 = sp["s3b"]
    c.whip(e0)
    c.section(3, 3, "Environment", e0, e1 - e0)
    te = find(w, "environment", e0)
    shots = [("IMG_6178.mp4", 9.6), ("IMG_6179.mp4", 2.4), ("IMG_6218.mp4", 5.2), ("IMG_6219.mp4", 0.6)]
    d = (e1 - te + 0.2) / len(shots)
    for k, (clip, ms) in enumerate(shots):
        t = te - 0.2 + k * d
        c.broll(F + clip, t, d, media_start=ms, zoom=(1.0, 1.1))
        if k:
            c.sfx("whoosh-short", t - 0.05, 0.3)
    tf = find(w, "five", e0)
    c.chip("Rasa hotel 5 bintang", tf - 0.3, e1 - tf + 0.6, x=70, y=470, yellow=True)

    # the lesson
    l0, _ = sp["l1"]
    _, l3 = sp["l3"]
    c.whip(l0)
    c.glass("Pengajaran", ["Tak perlu inovasi pelik", "Fokus servis", "Ikut kehendak pelanggan"], l0, l3 - l0,
            at=[find(w, "pelik-pelik", l0), find(w, "servis", l0), find(w, "permintaan", l0)], top=420)

    # his own niche: renovation
    n0, n1 = sp["niche"]
    c.whip(n0)
    c.chip("Dalam bisnes renovation", n0 + 0.05, 2.4, x=70, y=300, yellow=True)
    c.glass("Cari gap", ["Kelemahan pesaing", "Gap yang kita boleh menang"], n0, n1 - n0,
            at=[find(w, "kelemahan-kelemahan", n0), find(w, "win", n0)], icons=[("!", "w"), ("✓", "")], top=420)

    # close: everyone sells nasi padang, they won on the 3 basics
    q0, q1 = sp["c1"]
    c.whip(q0)
    c.broll(F + "IMG_6178.mp4", q0, q1 - q0, media_start=0.0, zoom=(1.0, 1.08))
    r0, r1_ = sp["c2"]
    tg = find(w, "tiga", r0)
    c.glass("3 benda je", ["Servis", "Makanan", "Environment"], tg - 0.2, r1_ - tg + 0.2,
            at=[tg + 0.2, tg + 0.5, tg + 0.8], top=420)

    # end card on the garden walkway
    c.broll(F + "IMG_6218.mp4", A, END, media_start=5.0, zoom=(1.0, 1.06))
    c.end_card("@bangfasz", "Follow<em>cerita bisnes kontraktor</em>", "Renovation · klinik · bisnes", "Follow", A, END)
    c.captions_ref(w, HOT, hide=[(A, A + END)])
    c.write(OUT + "p1-pagi-sore.html", "7/11: Pagi Sore, pengajaran bisnes")


if __name__ == "__main__":
    r1()
