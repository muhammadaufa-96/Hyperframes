"""Folder 28/10/26: eight 9:16 edits.
usage: python3 build_2810.py [1..8]
1 tour 9 bilik · 2 dimensi lain · 3 rasa mahal · 4 projek mencabar · 5 syarat klinik
6 pintu sliding (Kepong) · 7 Peria Restoran (bangfasz) · 8 promosi Luma Clinic
Audio: voice + sound effects only (no music)."""
import json, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
from kit import K, align, esc
from script2810 import SCRIPT

E = "/home/user/Hyperframes/f2810/edit/"
F = "../assets/footage/f2810/"
PH = F + "photos/"
OUT = "/home/user/Hyperframes/compositions/"
END = 3.6
HOT = {"9", "bilik", "1,500", "expensive", "l-box", "blockboard", "melamin", "ot", "hair", "transplant", "syarat", "utility",
       "double", "janitor", "renovate", "planning", "workflow", "design", "selesa", "berbeza", "experience", "crucial",
       "texture", "susah", "luas", "frosted", "sliding", "aluminium", "kepong", "subhanallah", "sedap", "peria", "lomak",
       "sambal", "apong", "9.5", "luma", "gp", "estetik", "dimensi", "lain", "mahal", "a", "z", "free", "rembayung"}


def load(v):
    segs = json.load(open(f"{E}{v}_segs.json"))
    spans = {}
    for x in segs["segments"]:
        a, b = spans.get(x["tag"], (x["out_in"], x["out_out"]))
        spans[x["tag"]] = (min(a, x["out_in"]), max(b, x["out_out"]))
    asr = json.load(open(f"{E}chk/{v}/words.json"))
    script = {k: t for k, t in SCRIPT[v].items() if k in spans}
    return segs, spans, align(asr, script, spans)


def find(w, token, after=0.0, nth=1):
    n = 0
    for x in w:
        if x[1] >= after - 0.05 and x[0].lower().strip(".,?!…") == token.lower():
            n += 1
            if n == nth:
                return x[1]
    raise KeyError(f"{token} after {after:.2f}")


def base(v, cid):
    segs, spans, w = load(v)
    A = segs["duration"]
    c = K(cid, A + END)
    c.aroll(F + f"aroll_{v}.mp4", [(0.0, A, 0.0)])
    prev, z = None, 1.0
    for s in segs["segments"]:
        z = (1.1 if z == 1.0 else 1.0) if s["piece"] == prev else 1.0
        prev = s["piece"]
        c.js.append(f'tl.set("#acam", {{ scale: {z}, transformOrigin: "50% 40%" }}, {s["out_in"]:.3f});')
    c.shade(0, A + END)
    return c, segs, spans, w, A


def brate(c, src, start, dur, media_start, rate, zoom=(1.0, 1.06)):
    """B-roll played faster (constant playback rate)."""
    wid = c.uid("bw"); vid = c.uid("bv")
    c.layers.append(f'<div class="cam" id="{wid}"><video id="{vid}" class="clip" src="{src}" muted playsinline data-start="{start:.3f}" '
                    f'data-duration="{dur:.3f}" data-media-start="{media_start:.3f}" data-playback-rate="{rate}" data-track-index="1"></video></div>')
    c.js.append(f'tl.fromTo("#{wid}", {{ scale: {zoom[0]} }}, {{ scale: {zoom[1]}, duration: {dur:.3f}, ease: "none" }}, {start:.3f});')


def finish(c, w, A, path, title, end="ckaps", bg=None, bg_ms=0.0):
    if bg:
        (c.image if bg.endswith(".jpg") else c.broll)(bg, A, END, **({"media_start": bg_ms} if not bg.endswith(".jpg") else {}))
    if end == "ckaps":
        c.ckaps_end(A, END)
    c.captions_ref(w, HOT, hide=[(A, A + END)])
    c.write(OUT + path, title)


# ---------------------------------------------------------------------------
def v1():
    c, segs, sp, w, A = base("v1", "c1-tour-9-bilik")
    M = 7.2  # closing montage of the other rooms, after the outro line
    c.duration = A + M + END
    c.shade(A + END, M)
    n0, n1 = sp["nine"]
    c.broll(F + "IMG_5530.mp4", 0.0, 2.2, media_start=1.0, zoom=(1.12, 1.0))
    c.hook2("Live tour klinik estetik", "9 BILIK", "dalam 1,500 sqft?", 0.05, n1 - 0.1)
    i0, i1 = sp["intro"]
    c.whip(i0)
    c.pin("Luma Clinic", "Petaling Jaya", i0 + 0.3, i1 - i0 - 0.3, top=300)
    rooms = [("r1", "Waiting area"), ("r2", "Kaunter"), ("r3", "Dispensary"), ("r4", "Waiting area 2"), ("r5", "Laluan"),
             ("r6", "Treatment / OT"), ("r7", "Toilet pesakit"), ("r8", "Utility sink"), ("r9", "Pantry staf")]
    for k, (tag, title) in enumerate(rooms):
        a, b = sp[tag]
        c.whip(a)
        c.section(k + 1, 9, title, a, b - a)
    G = dict(top=420)
    a, b = sp["r1"]; c.glass("Konsep", ["Nature + minimalis", "Texture paint"], a, b - a, at=[find(w, "nature", a), find(w, "texture", a)], **G)
    a, b = sp["r2"]; tk = find(w, "kayu", a)
    c.glass("Finishing kaunter", ["Blockboard", "Bukan melamin", "Curving elemen kayu"], a, b - a,
            at=[find(w, "blockboard", a), find(w, "melamin", a), tk], icons=[("✓", ""), ("✕", "w"), ("✓", "")], **G)
    c.broll(F + "IMG_5559.mp4", tk - 0.6, b - tk + 0.6, media_start=25.0, zoom=(1.0, 1.12))
    a, b = sp["r3"]; c.glass("Dispensary", ["Tulis & simpan barang", "Konsep pigeon hole"], a, b - a, at=[find(w, "tulis-tulis", a), find(w, "pigeon", a)], **G)
    a, b = sp["r4"]; c.glass("Waiting area 2", ["Lantai two-tone", "Siling L-box", "Rasa expensive"], a, b - a,
                              at=[find(w, "two", a), find(w, "l-box", a), find(w, "expensive", a)], **G)
    c.image(PH + "IMG_5540.jpg", find(w, "l-box", a) + 0.3, 1.4, zoom=(1.0, 1.1))
    a, b = sp["r5"]; t = find(w, "dimensi", a); c.pill("✨ Dimensi lain", t, b - t, y=1500)
    c.image(PH + "IMG_5542.jpg", b - 1.3, 1.3, zoom=(1.0, 1.12))
    a, b = sp["r6"]; tkab = find(w, "kabinet-kabinet", a)
    c.glass("Treatment room", ["Mini OT", "Hair transplant"], a, tkab - a - 0.2, at=[find(w, "ot", a), find(w, "hair", a)], **G)
    c.glass("Kabinet", ["Custom made", "Top quartz stone", "Soft close"], tkab - 0.1, b - tkab + 0.1,
            at=[find(w, "custom", a), find(w, "quartz", a), find(w, "soft", a)], **G)
    a, b = sp["r7"]; c.glass("Toilet pesakit", ["Tertutup, tak berbau", "Tiles two-tone", "Tempat pegang"], a, b - a,
                              at=[find(w, "tutup", a), find(w, "two", a), find(w, "pegang", a)], **G)
    a, b = sp["r8"]; c.glass("Syarat klinik estetik", ["Utility sink (double)", "Janitor", "Bilik cuci rambut"], a, b - a,
                              at=[find(w, "double", a), find(w, "janitor", a), find(w, "cuci", a)], **G)
    a, b = sp["r9"]; c.glass("Pantry staf", ["Top quartz stone", "Staff flexible"], a, b - a, at=[find(w, "quartz", a), find(w, "flexible", a)], **G)
    o0, o1 = sp["outro"]
    c.whip(o0)
    shots = [("IMG_5566.jpg", "Bilik OT"), ("IMG_5544.jpg", "Bilik treatment"), ("IMG_5570.jpg", "Bilik konsultasi"),
             ("IMG_5569.jpg", "Bilik doktor"), ("IMG_5568.jpg", "Feature slat kayu")]
    d = M / len(shots)
    c.chip("Bilik-bilik lain 👇", A + 0.05, M - 0.1, y=300, yellow=True)
    for k, (img, lab) in enumerate(shots):
        c.image(PH + img, A + k * d, d, zoom=(1.0, 1.1))
        c.pill(lab, A + k * d + 0.1, d - 0.1, y=1500)
        c.sfx("whoosh-short", A + k * d, 0.35)
    finish(c, w, A + M, "c1-tour-9-bilik.html", "28/10 Video 1: Tour penuh klinik estetik", bg=PH + "IMG_5537.jpg")


def v2():
    c, segs, sp, w, A = base("v2", "c2-dimensi-lain")
    h0, h1 = sp["hook"]
    c.hook2("Bahagian paling", "SAYA SUKA 👇", "dalam klinik ni", 0.05, h1 - 0.1)
    t0, t1 = sp["tada"]
    c.whip(t0)
    c.hook2("Masuk", "DIMENSI LAIN", "", find(w, "dimensi", t0) - 0.2, t1 - find(w, "dimensi", t0) + 0.2, shade=False)
    c.sfx("sparkle", find(w, "dimensi", t0), 0.45)
    w0, w1 = sp["world"]
    c.whip(w0)
    c.broll(F + "IMG_5565.mp4", w0, min(3.0, w1 - w0), media_start=0.0, zoom=(1.0, 1.15))
    c.image(PH + "IMG_5542.jpg", w0 + min(3.0, w1 - w0), max(0.5, w1 - w0 - 3.0), zoom=(1.0, 1.12))
    finish(c, w, A, "c2-dimensi-lain.html", "28/10 Video 2: Dimensi lain", bg=PH + "IMG_5554.jpg")


def v3():
    c, segs, sp, w, A = base("v3", "c3-rasa-mahal")
    p0, p1 = sp["p1"]
    c.hook2("Kenapa klinik ni", "RASA MAHAL?", "", 0.05, 3.2)
    t = find(w, "selesa", p0)
    c.glass("Rahsia 01", ["Selesa setiap flow"], t - 0.3, p1 - t + 0.3, top=430)
    q0, q1 = sp["p2"]
    c.whip(q0)
    c.glass("Rahsia 02", ["Experience berbeza setiap ruang"], q0 + 0.2, 3.0, top=430)
    stops = [("Consult", "consultation", 1, "IMG_5569.jpg"), ("Waiting 1", "waiting", 1, "IMG_5534.jpg"), ("Waiting 2", "waiting", 2, "IMG_5540.jpg"),
             ("Laluan", "laluan", 1, "IMG_5542.jpg"), ("Treatment", "treatment", 1, "IMG_5544.jpg"), ("Toilet", "toilet", 1, "IMG_5549.jpg")]
    at = [find(w, tok, q0, nth) for _, tok, nth, _ in stops]
    c.journey([s[0] for s in stops], at, q1 + 0.2, top=300)
    for k, (_, _, _, img) in enumerate(stops):
        nxt = at[k + 1] if k + 1 < len(at) else min(q1, at[k] + 1.6)
        c.image(PH + img, at[k], max(0.8, nxt - at[k]), zoom=(1.0, 1.08))
    r0, r1 = sp["p3"]
    c.whip(r0)
    c.pin("Luma Clinic", "Petaling Jaya", r0 + 0.3, r1 - r0 - 0.3, top=470)
    finish(c, w, A, "c3-rasa-mahal.html", "28/10 Video 3: Kenapa klinik ni rasa mahal", bg=PH + "IMG_5536.jpg")


def v4():
    c, segs, sp, w, A = base("v4", "c4-projek-mencabar")
    c.hook2("Projek klinik estetik", "PALING MENCABAR", "salah sikit, kena buat semula", 0.05, 3.4)
    o0, o1 = sp["ops"]
    t = find(w, "borang", o0)
    c.chip("✓ Borang B lulus", t, o1 - t, y=300, yellow=True)
    k0, k1 = sp["cab"]
    c.whip(k0)
    tc, tt = find(w, "crucial", k0), find(w, "texture", k0)
    c.glass("Cabaran", ["Design crucial", "Texture paint susah"], tc - 0.3, k1 - tc + 0.3, at=[tc, tt], icons=[("!", "w"), ("!", "w")], top=430)
    c.image(PH + "IMG_5536.jpg", tt - 0.1, 1.6, zoom=(1.15, 1.0), origin="30% 40%")
    sl = find(w, "salah", k0)
    c.stamp("Buat semula!", sl + 0.2, k1 - sl, y=1000)
    d0, d1 = sp["done"]
    c.whip(d0)
    t = find(w, "almost", d0)
    c.stamp("✓ Almost done", t, d1 - t, y=1000, ok=True)
    finish(c, w, A, "c4-projek-mencabar.html", "28/10 Video 4: Projek paling mencabar", bg=PH + "IMG_5535.jpg")


def v5():
    c, segs, sp, w, A = base("v5", "c5-syarat-klinik")
    c.hook2("Nak buka klinik estetik?", "1 SYARAT", "yang ramai terlepas", 0.05, 3.2)
    s0, s1 = sp["syarat"]
    td, tj = find(w, "double", s0), find(w, "janitor", s0)
    c.glass("Syarat klinik estetik", ["Utility sink (double)", "Janitor"], td - 0.3, s1 - td + 0.3, at=[td, tj], top=430)
    t0, t1 = sp["tips"]
    c.whip(t0)
    rv, pl = find(w, "renovate", t0), find(w, "planning", t0)
    c.strike("Renovate", rv - 0.2, pl - rv + 0.2, rv + 0.3, y=520)
    c.glass("Tips", ["Planning dulu", "Workflow → Design"], pl, t1 - pl + 0.2, at=[pl, find(w, "design", pl)], top=430)
    k0, k1 = sp["cta"]
    c.whip(k0)
    c.button("👇 Free CKAPS Initial Assessment", find(w, "hubungi", k0), k1 - find(w, "hubungi", k0), top=1100)
    finish(c, w, A, "c5-syarat-klinik.html", "28/10 Video 5: 1 syarat klinik estetik", bg=PH + "IMG_5561.jpg")


def v6():
    c, segs, sp, w, A = base("v6", "c6-pintu-sliding")
    h0, h1 = sp["hook"]
    c.hook2("Salah pilih pintu?", "RUANG SEMPIT", "", 0.05, 3.0)
    t = find(w, "luas", h0)
    c.chip("Nampak luas ✓", t, h1 - t, y=300, yellow=True)
    p0, p1 = sp["pick"]
    e0, e1 = sp["eg"]
    c.doors(p0, e0 - p0 + 2.4, p0 + 0.4, e0 + 0.2)
    c.whip(e0 + 2.6)
    ta = find(w, "frosted", e0)
    c.broll(F + "IMG_5594.mp4", ta - 0.2, 2.6, media_start=0.5, zoom=(1.0, 1.08))
    tc = find(w, "connecting", e0)
    c.broll(F + "IMG_5597.mp4", tc - 0.3, e1 - tc + 0.3, media_start=8.0, zoom=(1.0, 1.08))
    c.glass("Site Kepong", ["Aluminium sliding", "Frosted, tak nampak dalam", "Connecting door"], e0 + 2.6, e1 - e0 - 2.4,
            at=[find(w, "aluminium", e0), ta, tc], top=430)
    i0, i1 = sp["inst"]
    c.whip(i0)
    seg = (i1 - i0) / 3
    for k, (clip, ms) in enumerate((("IMG_5593", 0.0), ("IMG_5596", 0.0), ("IMG_5595", 0.0))):
        brate(c, F + clip + ".mp4", i0 + k * seg, seg, ms, 2)
        c.sfx("key-press", i0 + k * seg + 0.2, 0.3)
    c.chip("⏩ Proses pasang", i0 + 0.1, i1 - i0 - 0.1, y=300)
    finish(c, w, A, "c6-pintu-sliding.html", "28/10 Video 6: Pintu sliding", bg=F + "IMG_5594.mp4", bg_ms=9.0)


def v7():
    c, segs, sp, w, A = base("v7", "c7-peria-restoran")
    h0, h1 = sp["hook"]
    c.hook2("Tak hype macam Rembayung…", "SUBHANALLAH SEDAP", "", 0.05, 3.4)
    t = find(w, "subhanallah", h0)
    c.broll(F + "IMG_5186.mp4", t - 0.1, h1 - t + 0.1, media_start=0.0, zoom=(1.0, 1.1))
    n0, n1 = sp["name"]
    c.whip(n0)
    c.pin("Peria Restoran", "Bukit Jelutong", n0 + 0.4, n1 - n0 + 2.0, top=300)
    m0, m1 = sp["walk"]
    c.pill("Masakan Negeri Sembilan", m0 + 0.2, m1 - m0 + 1.8, y=1500)
    for tag in ("walk", "drink", "serve", "lomak", "apong"):
        c.whip(sp[tag][0])
    s0, s1 = sp["serve"]
    c.pill("Masak Lomak Cili Api", s0 + 1.0, s1 - s0 - 1.0, y=1500)
    l0, l1 = sp["lomak"]
    tl, ts = find(w, "lomak", l0, 2), find(w, "sambal", l0)
    c.broll(F + "IMG_5186.mp4", tl - 0.2, ts - tl + 0.2, media_start=2.2, zoom=(1.0, 1.1))
    c.pill("Masak Lomak Cili Api", tl - 0.1, ts - tl + 0.1, y=1500)
    c.broll(F + "IMG_5186.mp4", ts, 1.8, media_start=0.0, zoom=(1.1, 1.0))
    c.pill("Sambal Petai 🔥", ts, 1.8, y=1500)
    a0, a1 = sp["apong"]
    c.pill("Gula Apong 🍧", a0 + 0.3, a1 - a0 + 1.5, y=1500)
    r0, r1 = sp["rate"]
    tr = find(w, "overall", r0)
    t95 = find(w, "9.5", tr) - 1.5
    c.chip("Food · Environment · Workflow", find(w, "food", tr) - 0.1, t95 - find(w, "food", tr) + 0.1, y=330)
    c.rating([], 9.5, t95, find(w, "you", tr) - t95 + 0.3, top=330)
    c.end_card("bangfasz", 'Follow<em>untuk review seterusnya</em>', "Peria Restoran · Bukit Jelutong", "＋ Follow bangfasz", A, END, logo=None)
    finish(c, w, A, "c7-peria-restoran.html", "28/10 Video 7: Peria Restoran", end=None, bg=F + "IMG_5435.mp4", bg_ms=4.0)


def v8():
    c, segs, sp, w, A = base("v8", "c8-promosi-luma")
    h0, h1 = sp["hook"]
    c.broll(F + "IMG_5530.mp4", 0.0, h1, media_start=0.5, zoom=(1.12, 1.0))
    c.hook2("Duduk area PJ?", "HAIR TRANSPLANT", "& rawatan estetik", 0.05, h1 - 0.1)
    c.pin("Luma Clinic", "Petaling Jaya", h1 - 1.6, 1.6 + 2.0, top=760)
    s0, s1 = sp["svc"]
    c.whip(s0)
    c.services([("🩺", "GP"), ("✨", "Estetik"), ("💇", "Hair transplant")], [find(w, "gp", s0), find(w, "estetik", s0), find(w, "hair", s0)], s1 + 0.2)
    d0, d1 = sp["doc"]
    c.whip(d0)
    t = find(w, "dr.", d0) if any(x[0].lower() == "dr." for x in w) else d0 + 1.0
    c.namecard("👨‍⚕️", "Dr. Lim & Miss Michelle", "Pakar estetik & hair transplant", t - 0.2, d1 - t + 0.2)
    e0, e1 = sp["sel"]
    c.whip(e0)
    tsu = find(w, "set", e0)
    c.pill("Design & renovate oleh Enoxin", tsu, 3.0, y=1500)
    stops = [("Register", "register", "IMG_5534.jpg"), ("Waiting", "waiting", "IMG_5540.jpg"), ("Treatment", "treatment", "IMG_5544.jpg")]
    at = [find(w, tok, e0) for _, tok, _ in stops]
    c.journey([s[0] for s in stops], at, e1, top=300)
    for k, (_, _, img) in enumerate(stops):
        c.image(PH + img, at[k], 1.6, zoom=(1.0, 1.08))
    k0, k1 = sp["cta"]
    c.whip(k0)
    c.end_card("Luma Clinic · Petaling Jaya", 'Luma<em>Clinic</em>', "Where confidence is restored", "📍 Petaling Jaya", A, END,
               foot="Design & renovate: Enoxin.Fitout")
    finish(c, w, A, "c8-promosi-luma.html", "28/10 Video 8: Promosi Luma Clinic", end=None, bg=F + "IMG_5530.mp4", bg_ms=3.0)


if __name__ == "__main__":
    for a in sys.argv[1:] or "12345678":
        globals()[f"v{a}"]()
