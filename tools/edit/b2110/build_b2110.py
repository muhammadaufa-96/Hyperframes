"""Folder 21/10/26: three 9:16 videos.
usage: python3 build_b2110.py [1 2 3]
1  IMG_5296  founder talk: cabaran utama bisnes design & build
2  IMG_5308  3D interaktif butik (screen recording, cropped in screen.sh)
3  IMG_7835  "semuanya mesti ikut standard" reel
Music: "Best Morning" bed ducked under the voice. CTA: Follow for more tips."""
import json, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/ads")
from adkit import Ad, align, music_bed

B = "/home/user/Hyperframes/b2110/"
F = "../assets/footage/b2110/"
FA = "../assets/footage/ads/"
OUT = "/home/user/Hyperframes/compositions/"
HOT = {"cabaran", "utama", "lingkup", "risk", "activity", "parties", "cash", "flow", "komen", "standard", "ckaps", "kabinet", "layout", "3d"}
BEAT = 0.86
END = 3.4


def bed(c, voice, at=0.0, vol=0.6):
    name = f"bed_{c.cid}.m4a"
    music_bed(f"/home/user/Hyperframes/assets/dc/{name}", c.duration, voice, at, vol=vol)
    c.music(f"../assets/dc/{name}", 0.0, c.duration, vol=1.0)

V1_SCRIPT = {
 "hook": "Ada orang tanya aku, apa cabaran utama dalam bisnes untuk design and build ni?",
 "prob": "Bagi aku, cabaran utama dia, apabila kita melibatkan dengan banyak parties, dia punya tu high activity and then dia punya tu high risk jugalah.",
 "impact": "So kalau kita salah susun atur, management project, cash flow, kat situ dia akan jadi isu, dan benda tu yang akan membuatkan sama ada company kita tu lingkup ataupun tak boleh bertahan lama.",
 "agree": "Dan aku yakin kepada kontraktor-kontraktor kat luar sana yang macam aku, diorang pun setujulah dengan apa yang aku cuba sampaikan.",
 "cta": "Untuk korang punya bisnes, apa cabaran utama korang? Cuba korang komen kat bawah. Mungkin kita sama-sama boleh belajar ke?",
}


def find(words, token, after=0.0):
    for w in words:
        if w[1] >= after - 0.05 and w[0].lower().strip(".,?!") == token.lower():
            return w[1]
    raise KeyError(token)


def v1():
    segs = json.load(open(B + "edit/v1_segs.json"))
    spans = {}
    for x in segs["segments"]:
        a, b = spans.get(x["tag"], (x["out_in"], x["out_out"]))
        spans[x["tag"]] = (min(a, x["out_in"]), max(b, x["out_out"]))
    w = align(json.load(open(B + "edit/chk/v1/words.json")), V1_SCRIPT, spans)
    A = segs["duration"]
    c = Ad("b1-cabaran-design-build", A + END)
    c.aroll(F + "aroll_v1.mp4", [(0.0, A, 0.0)])
    prev, z = None, 1.0
    for s in segs["segments"]:
        z = (1.12 if z == 1.0 else 1.0) if s["piece"] == prev else 1.0
        prev = s["piece"]
        c.js.append(f'tl.set("#acam", {{ scale: {z}, transformOrigin: "50% 40%" }}, {s["out_in"]:.3f});')
    c.shade(0, A + END)
    h0, h1 = spans["hook"]
    c.hook(["3 benda ni boleh", "buat company", "LINGKUP 💥"], 0.05, h1 - 0.1)
    p0, p1 = spans["prob"]
    ml, hi1 = find(w, "melibatkan", p0), find(w, "high", p0)
    hi2 = find(w, "high", hi1 + 0.3)
    c.broll(FA + "IMG_5236.mp4", ml - 0.3, hi1 - ml + 0.3, media_start=2.6, zoom=(1.0, 1.08))
    c.broll(FA + "IMG_5243.mp4", hi1, p1 - hi1, media_start=6.6, zoom=(1.08, 1.0))
    nodes = ["Client", "Designer", "Contractor", "Supplier", "Subcon", "PBT"]
    c.network(nodes, ml - 0.3, hi1, [find(w, "banyak", p0) - 0.3 + i * 0.22 for i in range(len(nodes))])
    c.meters(["High activity", "High risk"], [hi1, hi2], p1 + 0.1)
    i0, i1 = spans["impact"]
    for k, (tok, lab) in enumerate((("susun", "Susun atur"), ("management", "Project management"), ("cash", "Cash flow"))):
        t = find(w, tok, i0)
        c.tag(lab, t, find(w, "dan", t) - t + 0.3, 70, 300 + k * 120, icon="!", warn=True)
    lk = find(w, "lingkup", i0)
    c.stamp("Lingkup", lk - 0.05, i1 - lk + 0.2, y=1060)
    g0, g1 = spans["agree"]
    sj = find(w, "setujulah", g0)
    c.chip("Setuju? 👍", sj, g1 - sj, y=300, yellow=True)
    k0, k1 = spans["cta"]
    cb = find(w, "cabaran", k0)
    c.comment("Apa cabaran utama bisnes korang?", cb - 0.2, k1 - cb + 0.2, find(w, "komen", k0))
    c.captions_hot(w, HOT, hide=[(A, A + END)])
    c.broll(FA + "IMG_5277.mp4", A, END, media_start=1.0, zoom=(1.0, 1.08))
    c.follow_end(A, END)
    bed(c, B + "edit/aroll_v1.mp4")
    c.write(OUT + "b1-cabaran-design-build.html", "21/10 Video 1: Cabaran design & build")


def v2():
    segs = [("Kabinet", 9.46), ("Kaunter bayaran", 2.58), ("Cermin + LED", 2.58), ("Rak display", 2.58),
            ("Rak simpanan", 0.86), ("Bangku + storan", 0.86), ("Podium mannequin", 1.72)]
    A = sum(d for _, d in segs)
    c = Ad("b2-3d-interaktif", A + END)
    c.broll(F + "v2_screen.mp4", 0.0, A, media_start=0.0, zoom=(1.0, 1.04))
    c.layers.append(f'<audio id="vo" src="{F}v2_voice.m4a" data-start="0" data-duration="7.700" data-track-index="9" data-volume="1"></audio>')
    c.hook(["Sebelum renovate,", "client dah 'masuk'", "kedai dalam 3D 👆"], 0.05, 2.6)
    c.pill("Layout ke-2 ✓", 2.8, 2.1)
    t = 0.0
    for i, (lab, d) in enumerate(segs):
        at = t + (5.0 if i == 0 else 0.0)
        c.tap(560, 900, at)
        c.pill(lab, at + 0.15, (t + d) - at - 0.15)
        if i:
            c.sfx("whoosh-short", t, 0.3)
        t += d
    asr = [[w["text"], w["start"], w["end"], "vo"] for w in json.load(open(B + "chk/win/IMG_5308_0/transcript.json"))]
    words = align(asr, {"vo": "Ini tuan, konsep kita dah siapkan. Kita dah second layout, kabinet pun kita dah siapkan."}, {"vo": (0.0, 7.6)})
    c.captions_hot(words, HOT, hide=[(A, A + END)])
    c.broll(F + "v2_screen.mp4", A, END, media_start=0.5, zoom=(1.08, 1.0))
    c.follow_end(A, END)
    bed(c, B + "edit/v2_voice.m4a", vol=0.75)
    c.write(OUT + "b2-3d-interaktif.html", "21/10 Video 2: 3D interaktif butik")


def v3():
    S = 8.28
    BR = 4.5
    A = S + BR
    c = Ad("b3-ikut-standard", A + END)
    c.aroll(F + "IMG_7835.mp4", [(0.0, S, 0.0)])
    c.shade(0, A + END)
    c.broll(F + "IMG_7835.mp4", S, BR, media_start=10.3, zoom=(1.0, 1.08))
    c.hook(["4 benda ni WAJIB", "ikut standard"], 0.05, 2.3)
    c.wordstack(["Flow", "Layout", "Sistem", "Material"], [2.4, 3.05, 3.85, 4.35], 5.4, top=290)
    c.stamp("Standard CKAPS ✓", 7.25, 1.6, y=1000, ok=True)
    words = [["Semuanya", 5.25, 5.75], ["mesti", 5.75, 6.0], ["kena", 6.0, 6.2], ["mengikut", 6.2, 6.62],
             ["CKAPS", 6.65, 7.0], ["punya", 7.0, 7.25], ["standard", 7.25, 8.0]]
    c.captions_hot(words, HOT)
    c.broll(F + "IMG_7835.mp4", A, END, media_start=11.0, zoom=(1.08, 1.0))
    c.follow_end(A, END)
    bed(c, B + "edit/v3_voice.m4a")
    c.write(OUT + "b3-ikut-standard.html", "21/10 Video 3: Ikut standard")


if __name__ == "__main__":
    for a in sys.argv[1:] or "123":
        globals()[f"v{a}"]()
