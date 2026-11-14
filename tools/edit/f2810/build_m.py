"""13/11/26: five edits from the Setia Alam boutique site (storyboard: Claude Docs "Storyboard Content - Folder 13/11").
m1 timeline (IMG_6375) · m2 butik mahal (IMG_6377) · m3 5 fasa (IMG_6363) · m4 layout + bilik live (IMG_6365) · m5 progress reel (no voice)
Commercial renovation: CTA is "Follow for more tips" (CKAPS is for clinics only); m2 ends on free consultation for boutique set-up.
usage: python3 build_m.py [1..5]"""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build_2810 as b
from build_2810 import base, find, finish, F, END, OUT
from kit import K

b.HOT |= {"aircon", "fasa", "6", "cassette", "kaset", "butik", "design", "structure", "finishing", "id", "carpentry",
          "warehouse", "surau", "live", "fitting", "staff", "bos", "luxury", "minimalis", "bali", "cahaya", "lampu",
          "kusam", "siling", "3000mm", "5", "kaki", "bernafas", "mahal", "eksklusif", "percuma", "timeline", "gantt",
          "klien", "vo", "material", "curving", "payment", "hold", "stop", "workflow", "confirmkan", "1200", "setia",
          "alam", "follow"}


def bcut(c, src, t, d, ms, zoom=(1.0, 1.06)):
    c.broll(F + src, t, d, media_start=ms, zoom=zoom)
    c.whip(t)


def m1():
    c, segs, sp, w, A = base("m1", "m1-renovate-lambat-siap")
    h0, h1 = sp["hook"]
    c.hook2("3 benda yang buat", "Renovate<br>lambat siap", "berapa lama nak siap?", 0.05, min(3.4, h1 - 0.1))
    v0, v1 = sp["save"]
    c.whip(v0)
    c.stamp("SAVE dulu 🔖", find(w, "panjang", v0) - 0.3, v1 - find(w, "panjang", v0) + 0.5, y=900, ok=True)
    c.sfx("pop", find(w, "panjang", v0) - 0.3, 0.45)
    s0, s1 = sp["site"]
    c.whip(s0)
    c.pin("Setia Alam", "± 1,200 sqft", find(w, "setia", s0) - 0.2, s1 - s0, top=420)
    bcut(c, "IMG_6371.mp4", find(w, "1200", s0) - 0.3, 2.4, 2.0)
    k0, k1 = sp["cabaran"]
    bcut(c, "IMG_6372.mp4", find(w, "konsep", k0) - 0.2, 2.6, 2.0)
    c.chip("Cabaran: konsep & design", find(w, "cabaran", k0) - 0.2, k1 - find(w, "cabaran", k0), x=70, y=300, yellow=True)
    g0, g1 = sp["gantt"]
    c.whip(g0)
    c.chip("Gantt chart", find(w, "gantt", g0) - 0.2, g1 - find(w, "gantt", g0) + 0.2, x=70, y=300)
    u0, u1 = sp["ubah"]
    c.whip(u0)
    c.chip("Timeline berubah", u0 + 0.2, u1 - u0, x=70, y=300, yellow=True)
    f1a, f1b = sp["f1"]
    c.whip(f1a)
    c.section(1, 3, "Perubahan klien", f1a, f1b - f1a)
    bcut(c, "IMG_6372.mp4", find(w, "tukar", f1a) - 0.3, 2.4, 8.0)
    tv = find(w, "vo", f1a)
    c.stamp("Kena VO", tv - 0.1, 1.8, y=900)
    tt = find(w, "toleransi", f1a)
    ta = find(w, "awal", f1a)
    c.glass("Dengan kami", ["Ubah di fasa awal: tiada VO", "Dah siap baru ubah: ada VO", "Kami bantu serap costing"], ta - 0.6, f1b - ta + 0.6,
            at=[ta, ta + 0.9, find(w, "serapkan", f1a)], icons=[("✓", ""), ("!", "w"), ("✓", "")], top=420)
    f2a, f2b = sp["f2"]
    c.whip(f2a)
    c.section(2, 3, "Design & material", f2a, f2b - f2a)
    bcut(c, "V9230.mp4", find(w, "curving", f2a) - 0.4, 2.6, 3.4, zoom=(1.0, 1.1))
    f3a, f3b = sp["f3"]
    c.whip(f3a)
    c.section(3, 3, "Payment progress", f3a, f3b - f3a)
    c.stamp("Kerja hold", find(w, "hold", f3a) - 0.1, 1.8, y=900)
    o0, o1 = sp["moral"]
    c.whip(o0)
    c.glass("Sebelum renovate", ["Tahu apa korang nak", "Design & workflow", "Confirm semua dulu", "Baru cari kontraktor"], o0 + 0.6, o1 - o0 - 0.5,
            at=[find(w, "tahu", o0), find(w, "workflow", o0), find(w, "confirmkan", o0), find(w, "someone", o0)], top=420)
    q0, q1 = sp["cta"]
    c.whip(q0)
    c.pill("Like · Share", find(w, "like", q0) - 0.1, 2.0, y=1480)
    c.follow_end(A, END)
    finish(c, w, A, "m1-renovate-lambat-siap.html", "13/11: 3 benda yang buat renovate lambat siap", end=None,
           bg=F + "IMG_6371.mp4", bg_ms=4.0)


def m2():
    c, segs, sp, w, A = base("m2", "m2-butik-nampak-mahal")
    # cold open: he trips over the pipes -> "OPPS!" -> TV colour bars + beep (baked into the OOPS2 clip)
    o0, o1 = sp["oops"]
    c.stamp("OPPS!", o0 + 0.75, 0.6, y=760)
    c.sfx("impact-bass-2", o0 + 0.75, 0.5)
    c.sfx("glitch-2", o1 - 1.15, 0.45)
    l0, l1 = sp["lampu"]
    c.hook2("Nak buka butik?", "Nampak mahal?<br>2 benda ni", "design gempak pun boleh nampak kusam", l0 + 0.05, 3.4)
    tc = find(w, "cahaya", l0)
    c.section(1, 2, "Lampu", tc - 0.3, l1 - tc + 0.3)
    bcut(c, "IMG_6371.mp4", tc - 0.2, 2.4, 1.0)
    tk = find(w, "kusam", l0)
    c.glass("Lampu salah", ["Nampak kusam", "Tak menarik, tak hidup"], tk - 0.3, l1 - tk + 0.3,
            at=[tk, find(w, "hidup", l0)], icons=[("✕", "w"), ("✕", "w")], top=420)
    s0, s1 = sp["siling"]
    c.whip(s0)
    c.section(2, 2, "Tinggi siling", s0, s1 - s0)
    bcut(c, "IMG_6370.mp4", find(w, "ketinggian", s0) - 0.2, 2.6, 8.0, zoom=(1.0, 1.1))
    t3 = find(w, "3000mm", s0)
    c.counter(3000, t3 - 0.4, s1 - t3 + 0.4, "mm · lantai ke siling", top=560)
    k0, k1 = sp["contoh"]
    c.whip(k0)
    c.pin("Setia Alam", "Siling 3000mm", find(w, "setia", k0) - 0.2, k1 - k0, top=420)
    g0, g1 = sp["tinggi"]
    c.whip(g0)
    t5 = find(w, "5", g0)
    c.chip("+5 kaki", t5 - 0.2, 2.2, x=70, y=300, yellow=True)
    tf = find(w, "fitting", g0)
    bcut(c, "IMG_6373.mp4", tf - 0.3, 2.6, 4.0)
    c.pill("Fitting area", tf - 0.1, 2.3, y=1480)
    tb = find(w, "bernafas", g0)
    c.glass("Siling tinggi = ", ["Rasa bernafas", "Rasa mahal", "Eksklusif", "Harga berpatutan"], tb - 0.4, g1 - tb + 0.4,
            at=[tb, find(w, "mahal", tb - 0.1), find(w, "eksklusif", tb), find(w, "berpatutan", tb)], top=420)
    q0, q1 = sp["cta"]
    c.whip(q0)
    c.pill("Free consultation", find(w, "bantu", q0) - 0.2, 2.4, y=1480)
    c.end_card("Enoxin.Fitout", "Nak setup<em>butik?</em>", "Free consultation untuk setup butik", "👇 Klik link di bawah", A, END)
    finish(c, w, A, "m2-butik-nampak-mahal.html", "13/11: Butik nampak mahal, 2 benda ni", end=None,
           bg=F + "IMG_6372.mp4", bg_ms=3.0)


def m3():
    c, segs, sp, w, A = base("m3", "m3-5-fasa-renovate")
    i0, i1 = sp["intro"]
    bcut(c, "IMG_6362.mp4", 0.0, 3.2, 0.5)
    c.hook2("Kontraktor share", "5 fasa<br>renovate kedai", "fasa 1 dah nak siap", 0.05, 3.1)
    t6 = find(w, "6", i0)
    c.counter(6, t6 - 0.3, i1 - t6 + 0.2, "unit aircon · 2 cassette + 4 wall mounted", top=560)
    u0, u1 = sp["butik"]
    c.whip(u0)
    tf = find(w, "fasa", u0)
    c.pin("Setia Alam", "Projek baru", u0 + 0.1, 2.6, top=420)
    c.chip("Fasa 1 hampir siap", tf - 0.2, 2.6, x=70, y=300, yellow=True)
    bcut(c, "IMG_6370.mp4", find(w, "finishing", u0) - 0.2, u1 - find(w, "finishing", u0) + 0.2, 8.0)
    f0, f1 = sp["fasa"]
    c.whip(f0)
    marks = [find(w, "pertama", f0), find(w, "kedua", f0), find(w, "ketiga", f0), find(w, "keempat", f0), find(w, "last", f0)]
    c.glass("5 fasa kerja kita", ["Design & struktur", "Finishing struktur", "Kerja ID: warna, lantai, tiles", "Kabinet & carpentry",
                                  "Finishing touch-up"], marks[0] - 0.4, f1 - marks[0] + 0.4, at=marks, top=420)
    for t, (src, ms) in zip(marks[1:], [("IMG_6372.mp4", 8.0), ("IMG_6371.mp4", 9.0), ("IMG_6373.mp4", 4.0), ("V9230.mp4", 3.4)]):
        bcut(c, src, t - 0.2, 2.2, ms)
    r0, r1 = sp["rooms"]
    c.whip(r0)
    c.chip("Warehouse", find(w, "warehouse", r0) - 0.3, 1.8, x=70, y=300)
    c.chip("Surau", find(w, "surau", r0) - 0.4, r1 - find(w, "surau", r0) + 0.3, x=70, y=300, yellow=True)
    q0, q1 = sp["cta"]
    c.whip(q0)
    c.pill("Nantikan next video", find(w, "nantikan", q0) - 0.2, 2.2, y=1480)
    c.follow_end(A, END)
    finish(c, w, A, "m3-5-fasa-renovate.html", "13/11: 5 fasa kontraktor renovate kedai", end=None,
           bg=F + "IMG_6371.mp4", bg_ms=4.0)


def m4():
    c, segs, sp, w, A = base("m4", "m4-layout-butik-bilik-live")
    l0, l1 = sp["load"]
    c.hook2("Butik 1,200 sqft", "Ada 2<br>bilik live?", "tour layout butik", 0.05, 3.1)
    c.pin("Setia Alam", "Barang mechanical", find(w, "setia", l0) - 0.2, 2.6, top=420)
    t6 = find(w, "6", l0)
    c.counter(6, t6 - 0.3, l1 - t6 + 0.2, "unit aircon · 2 kaset", top=560)
    k0, k1 = sp["cassette"]
    c.whip(k0)
    c.chip("Kaset 1", find(w, "satu", k0) - 0.1, 2.0, x=70, y=300, yellow=True)
    c.chip("Kaset 2", find(w, "satu", k0, nth=2) - 0.1, k1 - find(w, "satu", k0, nth=2), x=70, y=300, yellow=True)
    labels = [("rooms1", "pertama", "Bilik live 1"), ("rooms1", "kedua", "Bilik live 2"), ("rooms1", "fitting", "Fitting"),
              ("rooms2", "staff", "Ruang staf"), ("rooms2", "bos", "Bilik bos"), ("rooms2", "toilet", "Toilet & surau"),
              ("rooms2", "warehouse", "Warehouse")]
    ts = [find(w, tok, sp[tag][0]) - 0.3 for tag, tok, _ in labels]
    ends = ts[1:] + [sp["rooms2"][1]]
    for k, ((tag, tok, title), t, e) in enumerate(zip(labels, ts, ends)):
        if tag == "rooms2" and tok == "staff":
            c.whip(sp["rooms2"][0])
        c.section(k + 1, 7, title, t, max(1.0, e - t))
    p0, p1 = sp["concept"]
    c.whip(p0)
    bcut(c, "IMG_6372.mp4", find(w, "konsep", p0) - 0.3, 2.6, 2.0)
    c.glass("Konsep", ["Luxury minimalis", "Elemen Bali"], find(w, "konsep", p0) - 0.2, p1 - find(w, "konsep", p0) + 0.2,
            at=[find(w, "luxury", p0), find(w, "bali", p0)], top=420)
    q0, q1 = sp["cta"]
    c.whip(q0)
    c.pill("Follow for more tips", find(w, "follow", q0) - 0.2, 2.0, y=1480)
    c.follow_end(A, END)
    finish(c, w, A, "m4-layout-butik-bilik-live.html", "13/11: Layout butik 1,200 sqft dengan 2 bilik live", end=None,
           bg=F + "IMG_6371.mp4", bg_ms=4.0)


def m5():
    """15 s progress reel: no voice, chips + SFX."""
    shots = [("IMG_6362.mp4", 0.5, 2.2, "Progress site · Setia Alam"), ("IMG_6370.mp4", 1.0, 2.6, "Fasa 2 bermula"),
             ("V9230.mp4", 0.6, 2.6, "Detail: corner bead"), ("IMG_6373.mp4", 2.0, 2.8, "Fitting area"),
             ("IMG_6371.mp4", 2.0, 2.8, "Nantikan hasilnya")]
    A = sum(d for _, _, d, _ in shots)
    c = K("m5-progress-site", A + END)
    t = 0.0
    for k, (src, ms, d, label) in enumerate(shots):
        c.broll(F + src, t, d, media_start=ms, zoom=(1.0, 1.08))
        if k:
            c.whip(t)
        c.chip(label, t + 0.15, d - 0.25, x=70, y=300, yellow=(k in (0, 4)))
        t += d
    c.shade(0, A + END)
    c.sfx("whoosh-cinematic", 0.0, 0.4)
    c.broll(F + "IMG_6371.mp4", A, END, media_start=6.0)
    c.follow_end(A, END)
    c.write(OUT + "m5-progress-site.html", "13/11: Progress site Setia Alam")
    print(f"total {A + END:.2f}s")


if __name__ == "__main__":
    for a in sys.argv[1:] or "12345":
        globals()[f"m{a}"]()
