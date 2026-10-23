"""Klinik gigi Kepong (folder "21/10/26 raw untuk video ads"): six 9:16 ads.

usage: python3 build_ads.py [1 2 3 4 5 6]
A-rolls come from ads/edit/aroll_adN.mp4 (assemble.py); all footage is linked into assets/footage/ads/.
Music: "Best Morning" bed, ducked under the voice (client asked for it on 23/10).
"""
import json, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/ads")
from adkit import Ad, align, music_bed
from script import SCRIPT

ADS = "/home/user/Hyperframes/ads/"
F = "../assets/footage/ads/"
OUT = "/home/user/Hyperframes/compositions/"
HOT = {"klinik", "sendiri", "pertama", "shoplot", "free", "ckaps", "initial", "assessment", "percuma", "planning",
       "renovate", "selesa", "mahal", "kepong", "layout", "contractor", "lokasi", "site", "impian", "kosong", "siap"}
END = 3.6


def load(n):
    segs = json.load(open(f"{ADS}edit/ad{n}_segs.json"))
    asr = json.load(open(f"{ADS}edit/chk/ad{n}/words.json"))
    spans = {}
    for x in segs["segments"]:
        a, b = spans.get(x["tag"], (x["out_in"], x["out_out"]))
        spans[x["tag"]] = (min(a, x["out_in"]), max(b, x["out_out"]))
    return segs, align(asr, SCRIPT[n], spans)


def span(segs, tag):
    s = [x for x in segs["segments"] if x["tag"] == tag]
    return s[0]["out_in"], s[-1]["out_out"]


def find(words, token, after=0.0, before=1e9):
    for w in words:
        if after - 0.05 <= w[1] < before and w[0].lower().strip(".,?!") == token.lower():
            return w[1]
    raise KeyError(f"{token} after {after:.2f}")


def punch(c, segs, offset=0.0):
    """Alternate a gentle punch-in on jump cuts inside one take; reset on a new take."""
    prev, z = None, 1.0
    for s in segs["segments"]:
        z = (1.12 if z == 1.0 else 1.0) if s["piece"] == prev else 1.0
        prev = s["piece"]
        c.js.append(f'tl.set("#acam", {{ scale: {z}, transformOrigin: "50% 40%" }}, {s["out_in"] + offset:.3f});')


def base(n, cid, lead=0.0):
    segs, words = load(n)
    A = segs["duration"]
    c = Ad(cid, lead + A + END)
    c.aroll(F + f"aroll_ad{n}.mp4", [(lead, A, 0.0)])
    c.voice = (f"{ADS}edit/aroll_ad{n}.mp4", lead)
    punch(c, segs, lead)
    c.shade(0, lead + A + END)
    if lead:
        words = [[w, a + lead, b + lead] for w, a, b in words]
    return c, segs, words, lead + A


def finish(c, words, A, bg, path, title, bg_ms=0.0):
    c.broll(F + bg, A, END, media_start=bg_ms, zoom=(1.0, 1.08))
    c.cta_end(A, END)
    c.captions_hot(words, HOT, hide=[(A, A + END)])
    bed = f"bed_{c.cid}.m4a"
    music_bed(f"/home/user/Hyperframes/assets/dc/{bed}", c.duration, *c.voice)
    c.music(f"../assets/dc/{bed}", 0.0, c.duration, vol=1.0)
    c.write(OUT + path, title)


def ad1():
    c, segs, w, A = base(1, "ad1-painpoint")
    h0, h1 = span(segs, "hook")
    c.hook(["Doktor, nak buka", "klinik sendiri?"], 0.05, h1 + 0.2)
    p0, p1 = span(segs, "prob")
    c.broll(F + "IMG_5231.mp4", p0, (p1 - p0) / 2, media_start=3.0, zoom=(1.0, 1.1))
    c.broll(F + "IMG_5243.mp4", p0 + (p1 - p0) / 2, (p1 - p0) / 2, media_start=0.2, zoom=(1.08, 1.0))
    pops = [find(w, t, p0) for t in ("lokasi", "layout", "site", "contractor")]
    s0, s1 = span(segs, "same")
    r0, r1 = span(segs, "proof")
    c.qgrid(["Lokasi?", "Layout?", "Site?", "Contractor?"], pops, flip_at=r0 + 0.3, end=r1)
    c.name("Klinik gigi", "Kepong · hampir siap", s0 + 0.2, min(3.0, s1 - s0))
    third = (r1 - r0) / 3
    for i, (clip, ms) in enumerate((("IMG_5235", 0.0), ("IMG_5233", 0.2), ("IMG_5247", 0.3))):
        c.broll(F + clip + ".mp4", r0 + i * third, third, media_start=ms, zoom=(1.0, 1.1))
    c.chip("Hampir siap ✅", find(w, "hampir", r0), r1 - find(w, "hampir", r0), y=640, yellow=True)
    t0, t1 = span(segs, "step")
    c.card("1", "Bercakap", "dengan orang yang dah biasa buat", find(w, "bercakap", t0) - 0.2, t1 - find(w, "bercakap", t0) + 0.2)
    k0, k1 = span(segs, "cta")
    sv = find(w, "serius", k0)
    c.chip("Dah ada shoplot?", sv, find(w, "tekan", k0) - sv, y=300, yellow=True)
    tk = find(w, "tekan", k0)
    c.button("👇 Tekan link di bawah", tk, k1 - tk)
    z0, z1 = span(segs, "az")
    c.broll(F + "IMG_5277.mp4", z0, (z1 - z0) / 2, media_start=1.0, zoom=(1.0, 1.08))
    c.broll(F + "IMG_5278.mp4", z0 + (z1 - z0) / 2, (z1 - z0) / 2, media_start=0.5, zoom=(1.08, 1.0))
    c.steps(["Planning", "Design", "Renovation", "Handover"], [z0 + 0.4 + i * 0.5 for i in range(4)], z1)
    finish(c, w, A, "IMG_5276.mp4", "ad1-painpoint.html", "Iklan 1: Doktor, tak tahu nak mula dari mana?")


def ad2():
    c, segs, w, A = base(2, "ad2-transform")
    sek = find(w, "sekarang")
    # real "before renovate" footage of the empty shop (client upload 23/10); skip 5-7 s, a man walks in
    c.broll(F + "KOSONG.mp4", 0.0, 2.1, media_start=1.2, zoom=(1.0, 1.08))
    c.broll(F + "KOSONG.mp4", 2.1, sek - 2.1, media_start=9.0, zoom=(1.0, 1.08))
    c.chip("Sebelum renovate", 0.4, sek - 0.6, y=470)
    c.wipe(sek)
    c.hook(["Dari ruang kosong", "→ klinik gigi"], 0.05, sek - 0.15)
    c.chip("Sekarang ✨", sek + 0.2, 1.6, y=300, yellow=True)
    d0, d1 = span(segs, "d1")
    pk, lt, ka = find(w, "pintu", d0), find(w, "lantai", d0), find(w, "kaunter", d0)
    c.broll(F + "IMG_5275.mp4", pk, lt - pk, media_start=0.3, zoom=(1.0, 1.08))
    c.broll(F + "IMG_5234.mp4", lt, min(2.6, ka - lt), media_start=0.0, zoom=(1.0, 1.1))
    c.tag("Pintu kaca", pk, d1 - pk, 70, 300)
    c.tag("Lantai", lt, d1 - lt, 70, 420)
    c.tag("Kaunter & pintu", ka, d1 - ka, 70, 540, icon="⏳", warn=True)
    c.name("Klinik gigi", "Kepong", sek + 1.9, 2.6)
    e0, e1 = span(segs, "d2")
    st = find(w, "satu", e0)
    c.broll(F + "KOSONG.mp4", e0, find(w, "alhamdulillah", e0) - e0, media_start=12.0, zoom=(1.0, 1.1))
    c.chip("Ruang kosong + impian", st, find(w, "alhamdulillah", e0) - st, y=300, yellow=True)
    wf, de, rn, ho = (find(w, t, e0) for t in ("workflow", "design", "renovation", "handover"))
    c.broll(F + "IMG_5236.mp4", rn - 0.2, ho - rn + 0.2, media_start=2.6, zoom=(1.0, 1.08))
    c.broll(F + "IMG_5243.mp4", ho, e1 - ho, media_start=6.6, zoom=(1.0, 1.08))
    c.steps(["Workflow", "Design", "Renovation", "Handover"], [wf, de, rn, ho], e1)
    f0, f1 = span(segs, "d3")
    rv, pl = find(w, "renovate", f0), find(w, "planning", f0)
    c.chip("Tips 💡", f0 + 0.1, rv - f0 - 0.3, y=300)
    c.strike("Renovate", rv - 0.25, pl - rv + 0.1, rv + 0.35, y=520)
    c.chip("Planning ✓", pl, f1 - pl, y=520, yellow=True)
    k0, k1 = span(segs, "cta")
    fr = find(w, "free", k0)
    c.button("👇 Klik link di bawah", fr - 0.3, k1 - fr + 0.3)
    finish(c, w, A, "IMG_5279.mp4", "ad2-transform.html", "Iklan 2: Dari ruang kosong ke klinik gigi")


def ad3():
    c, segs, w, A = base(3, "ad3-layout")
    h0, h1 = span(segs, "hook")
    mh = find(w, "mahal", h0)
    c.hook(["Klinik selesa", "tak semestinya mahal"], 0.05, mh + 0.6)
    for i, (tok, lab) in enumerate((("susun", "Susun atur"), ("design", "Design"), ("gerak", "Gerak kerja"))):
        t = find(w, tok, mh)
        c.tag(lab, t, h1 - t + 0.2, 70, 300 + i * 120)
    t0, t1 = span(segs, "tour")
    rooms = [("Ruang kerusi", "kerusi"), ("Pintu masuk", "pintu"), ("Kabinet", "kabinet"), ("Waiting area", "waiting"),
             ("Sterilise", "sterilise"), ("Surgery 3", "surgery"), ("X-ray", "x-ray"), ("Toilet pesakit", "patient"),
             ("Compressor", "compressor"), ("Bilik doktor", "doktor"), ("Pintu exit", "exit")]
    marks, after = [], t0
    for name, tok in rooms:
        t = find(w, tok, after)
        marks.append((name, t)); after = t + 0.05
    c.route(marks, t0 + 0.05, t1 + 0.3)
    c.sfx("whoosh", t0, 0.45)
    f0, f1 = span(segs, "flow")
    c.flow(f0, f1 - f0, find(w, "selesa", f0) - 0.2, find(w, "staff", f0) - 0.2)
    k0, k1 = span(segs, "cta")
    hb = find(w, "hubungi", k0)
    c.button("👇 Klik link di bawah", hb, k1 - hb)
    finish(c, w, A, "IMG_5277.mp4", "ad3-layout.html", "Iklan 3: Layout klinik gigi yang betul")


def ad4():
    c, segs, w, A = base(4, "ad4-jangan-renovate")
    h0, h1 = span(segs, "hook")
    rv, pl = find(w, "renovate", h0), find(w, "planning", h0)
    c.hook(["Nak buka klinik?", "Jangan renovate dulu!"], 0.05, rv - 0.1)
    c.strike("Renovate", rv - 0.05, pl - rv + 0.05, rv + 0.3, y=520)
    c.chip("Planning ✓", pl, h1 - pl + 0.2, y=520, yellow=True)
    y0, y1 = span(segs, "why")
    mh = find(w, "mahal", y0)
    c.chip("Tak semestinya mahal", mh - 0.4, 1.8, y=300, yellow=True)
    tp = find(w, "tapi", mh)
    cuts = [("IMG_5236", 2.6), ("IMG_5243", 6.6), ("IMG_5232", 0.0)]
    seg = (y1 - tp) / 3
    for i, (clip, ms) in enumerate(cuts):
        c.broll(F + clip + ".mp4", tp + i * seg, seg if clip != "IMG_5232" else min(seg, 1.35), media_start=ms, zoom=(1.0, 1.1))
    for i, (tok, lab) in enumerate((("susun", "Susun atur"), ("design", "Design"), ("gerak", "Gerak kerja"))):
        t = find(w, tok, tp)
        c.tag(lab, t, y1 - t + 0.2, 70, 300 + i * 120)
    k0, k1 = span(segs, "cta1")
    pc = find(w, "percuma", k0)
    c.chip("Konsult percuma", pc - 0.3, k1 - pc + 0.3, y=300, yellow=True)
    q0, q1 = span(segs, "cta2")
    c.button("👇 Klik link di bawah", q0, q1 - q0 + 0.1, pulses=1)
    finish(c, w, A, "IMG_5275.mp4", "ad4-jangan-renovate.html", "Iklan 4: Jangan renovate dulu")


def ad5():
    shots = [("IMG_5231", 0.2, "Pintu kaca"), ("IMG_5235", 0.3, "Cove light"), ("IMG_5233", 0.3, "Skirting kemas"),
             ("IMG_5247", 0.5, "Aircond cassette"), ("IMG_5237", 0.6, "Toilet pesakit"), ("IMG_5278", 0.0, "Koridor luas"),
             ("IMG_5279", 4.0, "Bilik rawatan")]
    D = 1.05
    M = D * len(shots)
    c, segs, w, A = base(5, "ad5-retarget", lead=M)
    for i, (clip, ms, lab) in enumerate(shots):
        t = i * D
        c.broll(F + clip + ".mp4", t, D, media_start=ms, zoom=(1.0, 1.12))
        if i >= 2:
            c.tag(lab, t + 0.05, D - 0.05, 70, 1100)
        else:
            c.sfx("whoosh-short", t, 0.35)
    c.hook(["Klinik gigi ni", "kami setup A to Z"], 0.05, 2.0)
    k0, k1 = span(segs, "cta")
    c.button("👇 Klik link di bawah", M + k0 + 1.0, A - (M + k0 + 1.0))
    finish(c, w, A, "IMG_5235.mp4", "ad5-retarget.html", "Iklan 5: Retargeting 15 saat")


def ad6():
    c, segs, w, A = base(6, "ad6-pesakit-pertama")
    h0, h1 = span(segs, "hook")
    c.hook(["Jom jadi pesakit", "pertama klinik ni!"], 0.05, h1 + 0.3)
    kp = find(w, "kepong", h0)
    c.chip("📍 Kepong", kp, h1 - kp + 0.3, y=470)
    t0, t1 = span(segs, "tour")
    marks = [(n, find(w, tok, t0)) for n, tok in (("Pintu masuk", "pintu"), ("Kaunter", "kaunter"), ("Dispensary", "dispensary"), ("Surgery 1", "surgery"))]
    for i, (n, t) in enumerate(marks):
        end = marks[i + 1][1] if i + 1 < len(marks) else t1 + 0.2
        c.chip(f"0{i + 1}  {n}", t, end - t, y=300, yellow=True, sfx="click-soft")
    f0, f1 = span(segs, "flow")
    c.flow(f0, f1 - f0, find(w, "selesa", f0) - 0.2, find(w, "staff", f0) - 0.2)
    k0, k1 = span(segs, "cta")
    c.hook(["Doktor,", "nak klinik macam ni?"], k0, 3.2)
    ck = find(w, "click", k0)
    c.button("👇 Klik link di bawah", ck, k1 - ck)
    finish(c, w, A, "IMG_5276.mp4", "ad6-pesakit-pertama.html", "Iklan 6: Jom jadi pesakit pertama")


if __name__ == "__main__":
    for a in sys.argv[1:] or "123456":
        globals()[f"ad{a}"]()
