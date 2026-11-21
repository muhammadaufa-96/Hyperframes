"""21/11 edits: (a) Unboxing bekal isteri, (b) Cat Jotun colour mahal.
usage: python3 build21.py a|b   (needs f2111/winA/<w>/words.json, f2111/edit/segs_<w>.json, assets/footage/f2111/aroll_<w>.mp4)"""
import json, re, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2111")
from kit21 import V21, ICON, esc, Y, G, R
import gen

W = "/home/user/Hyperframes/f2111"
F = "../assets/footage/f2111/"
END = 3.2

FIX = {
    "a": {13.16: "bini", 13.49: "masakkan.", 13.75: None, 22.54: "Kat", 36.41: None, 39.18: "chicken", 39.72: "wrap", 41.32: "jealous", 41.76: None,
          42.62: "lelaki-lelaki", 43.22: "bujang", 44.49: "jealous.", 56.98: "Uish.", 66.22: "sekarang", 68.07: None, 68.12: "Dipping.", 70.12: None,
          94.05: None, 94.35: "Limpah-limpah!", 106.58: "bapak-bapak", 117.74: None, 118.10: "mood", 118.70: "But", 119.62: "anyway,", 120.19: None,
          125.34: "masakan", 129.98: None, 131.36: "Cuba"},
    "b": {7.49: "colour-colour", 10.46: "site", 11.49: "Setia", 11.91: "Alam", 13.58: "colour-colour", 19.04: "colour,", 19.54: "kualiti", 33.51: "dua",
          33.81: "colour.", 35.16: "Colour", 35.55: None, 38.15: "pink.", 42.37: "colour", 42.74: "grey.", 47.03: "check", 47.60: "colour,",
          54.11: "Jotun", 61.47: "bancuh", 64.07: "bancuh", 66.99: "bancuhkan", 69.51: "memang", 74.91: None, 75.00: "Haa,", 75.38: "nampak",
          76.32: "akak", 76.48: "tengah", 76.75: "bancuh.", 84.74: "electrical", 102.76: "dalam"},
}
EXTRA = {"b": [["life.", 105.12, 105.45]]}
HOT = {
    "a": {"site", "lori", "bekal", "bini", "unboxing", "3", "tiga", "bekas", "chicken", "wrap", "jealous", "sayang", "lauk", "ayam", "merah",
          "nasi", "sedap", "lapar", "homemade", "dipping", "pedas", "ngam-ngam", "manis", "nice", "sendiri", "penuh", "limpah-limpah",
          "bapak-bapak", "bujang", "setuju", "statement", "air", "tangan", "mood", "okay", "wife", "komen"},
    "b": {"lain", "expensive", "setia", "alam", "terkenal", "contractors", "kualiti", "power", "cantik", "harga", "client", "dua", "pink", "grey",
          "check", "supplier-supplier", "besar", "jotun", "subang", "bancuh", "bancuhkan", "experience", "ambil", "electrical", "hasil", "komen",
          "like", "share", "follow", "renovation", "business", "life"},
}

gen.CSS += r"""
.lc2 { position: absolute; left: 70px; top: 300px; display: flex; align-items: center; gap: 18px; background: #fff; color: #15171a; border-radius: 22px; padding: 14px 30px 14px 14px; box-shadow: 0 18px 44px rgba(0,0,0,0.45); }
.lc2 .ico { width: 76px; height: 76px; border-radius: 50%; background: #ff3b3b; color: #fff; padding: 16px; }
.lc2 b { display: block; font-weight: 800; font-size: 50px; text-transform: uppercase; line-height: 1; }
.lc2 span { display: block; font-weight: 600; font-size: 28px; color: #555; margin-top: 4px; }
"""


def words(w):
    out = []
    for x in json.load(open(f"{W}/winA/{w}/words.json")):
        k = round(x["start"], 2)
        t = FIX[w].get(k, x["text"]) if k in FIX[w] else x["text"]
        if t is None:
            continue
        if re.sub(r"[^\w]", "", t).lower() == "gang":
            t = t.lower().replace("gang", "geng")
        out.append([t, x["start"], x["end"]])
    out += [list(e) for e in EXTRA.get(w, [])]
    out.sort(key=lambda v: v[1])
    for i in range(len(out) - 1):
        out[i][2] = min(out[i][2], out[i + 1][1])
    return out


def at(ws, tok, after=0.0):
    for x in ws:
        if x[1] >= after and re.sub(r"[^\w'-]", "", x[0]).lower() == tok.lower():
            return x[1]
    raise KeyError(f"{tok} after {after}")


def loc(c, title, sub, start, dur, top=300):
    n = c.uid("lc")
    c.layers.append(f'<section id="{n}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                    f'<div class="lc2" id="{n}m" style="top:{top}px">{c.ico("pin")}<div><b>{esc(title)}</b><span>{esc(sub)}</span></div></div></section>')
    c.js.append(f'tl.fromTo("#{n}m", {{ y: -120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "bounce.out" }}, {start:.3f});')
    c.js.append(f'tl.to("#{n}m", {{ x: -900, duration: 0.3, ease: "power3.in" }}, {start + dur - 0.3:.3f});')
    c.sfx("pop", start + 0.35, 0.4)


def base(w, cid):
    segs = json.load(open(f"{W}/edit/segs_{w}.json"))
    A = segs["duration"]
    c = V21(cid, A + END)
    c.setup(A, segs)
    c.aroll(F + f"aroll_{w}.mp4", [(0.0, A, 0.0)])
    c.shade(0, A)
    return c, A, words(w)


def build_a():
    c, A, ws = base("a", "v2111a-bekal-isteri")
    T = lambda tok, after=0.0: at(ws, tok, after)
    c.camera21(punches=[(T("god"), 1.0), (T("jealous"), 1.2), (T("merah"), 1.0), (T("sedap"), 1.0), (T("sedap", 78), 0.9),
                        (T("penuh", 93), 0.9), (T("bujang", 100), 0.9), (T("okay", 118), 0.6)], shakes=[T("jealous")])
    for t, same in c.cuts:
        if not same:
            c.flash(t)
    c.hook21("Sambil tunggu lori sampai", "Unboxing", "bekal isteri", 0.0, 3.4, icon="box3")
    c.boxes(T("total") - 0.25, 64.9, steps=[(T("chicken"), "Chicken wrap", "box3"), (T("lauk", 51), "Ayam masak merah", "box3"),
                                            (T("nasi"), "Nasi", "box3")])
    c.stamp2("Bujang,<br>jangan jealous!", T("jealous") - 0.2, 3.5, top=640)
    c.hearts("Thank you sayang", T("thank") - 0.1, 2.6, top=600)
    c.stamp2("Homemade", T("homemade") - 0.1, 1.9, top=600, cls="g", shake=False)
    c.taste(T("rasa", 74) - 0.3, T("just") + 0.9, t_pedas=T("pedas", 79), t_manis=T("manis", 81), t_ok=T("just"))
    c.overflow(T("letak") - 0.3, 96.5, t_full=T("penuh", 92), t_limpah=T("limpah-limpah"))
    c.question(T("tanya") - 0.5, 109.6, t_bujang=T("bujang", 100))
    c.mood(T("the", 109) - 0.15, T("but", 118) + 0.2, t_bad=T("tak", 116.5), t_good=T("jadi", 117.5))
    c.hearts("Thank you, wife!", T("thank", 120) - 0.1, 3.2, top=600)
    c.comment_poll(T("yang", 126.5) - 0.1, 136.0, t_poll=T("setuju", 129), t_type=T("komen", 131), text="Setuju!", t_arrow=T("bawah", 131))
    c.image(F + "last_a.jpg", A, END, zoom=(1.0, 1.06))
    c.end_card("bangfasz", 'Follow<em>for more</em>', "Renovation · Business · Life", "+ Follow bangfasz", A, END, logo=None)
    c.captions_box(ws, HOT["a"], hide=[(A, A + END)])
    c.write("/home/user/Hyperframes/compositions/v2111a-bekal-isteri.html", "21/11: Unboxing bekal isteri")


def build_b():
    c, A, ws = base("b", "v2111b-cat-jotun")
    T = lambda tok, after=0.0: at(ws, tok, after)
    c.camera21(punches=[(T("expensive"), 1.0), (T("power"), 0.9), (T("harga"), 1.1), (T("pink"), 0.9), (T("jotun"), 1.0),
                        (T("electrical"), 1.0)])
    for t, same in c.cuts:
        if not same:
            c.flash(t)
    c.price_hook(0.0, 4.9)
    loc(c, "Site Setia Alam", "projek kita", T("setia") - 0.3, 2.6)
    c.glass("Kenapa colour ni?", ["Terkenal among contractors", "Kualiti power", "Cantik", "Harga pun “cantik”"], T("terkenal") - 0.6,
            T("so", 27.5) - T("terkenal") + 0.6, top=270,
            at=[T("terkenal"), T("power"), T("cantik", 22), T("harga")], icons=[("✓", ""), ("✓", ""), ("✓", ""), ("$", "w")])
    c.sfx("error", T("harga") + 0.05, 0.2, dur=0.5)
    c.swatches(T("pakai") - 0.2, T("by") - 0.1, t_pink=T("pink") - 0.3, t_grey=T("grey"))
    c.glass("Tip: nak check colour?", ["Pergi supplier besar", "Contoh: Jotun"], T("by") + 0.05, T("subang") - T("by") - 0.1, top=270,
            at=[T("supplier-supplier"), T("jotun")], icons=[("1", "n"), ("2", "n")])
    loc(c, "Jotun · Subang", "supplier cat", T("subang") - 0.1, T("kalau", 58) - T("subang") + 0.1)
    c.bancuh(T("tempat", 60) - 0.3, T("so", 77) - 0.1, t_go=T("tolong"), t_done=T("haa", 74.5))
    # b-roll: loading the pickup while he says "so kita ambil"
    c.broll(F + "broll_6752.mp4", T("so", 77) - 0.1, T("okay", 78) - T("so", 77) + 0.9, media_start=12.0, zoom=(1.05, 1.12), track=1)
    c.chip("Angkut ke site", T("so", 77) + 0.2, T("okay", 78) - T("so", 77) + 0.4, x=70, y=320, yellow=True)
    c.nextup(T("cari") - 0.3, T("kalau", 86) - 0.1, "Next", "Barang elektrikal")
    c.comment_ask(T("kalau", 86), T("korang", 95.5) - 0.1, "Nak tengok hasil!", T("komen", 90))
    c.cta(T("korang", 95.5), A - 2.3, t_like=T("like"), t_share=T("share", 97), t_follow=T("follow"),
          topics=[("Renovation", T("renovation")), ("Business", T("business")), ("Life", T("life"))])
    c.image(F + "last_b.jpg", A, END, zoom=(1.0, 1.06))
    c.end_card("bangfasz", 'Follow<em>for more</em>', "Renovation · Business · Life", "+ Follow bangfasz", A, END, logo=None)
    c.captions_box(ws, HOT["b"], hide=[(A, A + END)])
    c.write("/home/user/Hyperframes/compositions/v2111b-cat-jotun.html", "21/11: Cat Jotun colour mahal")


if __name__ == "__main__":
    {"a": build_a, "b": build_b}[sys.argv[1]]()
