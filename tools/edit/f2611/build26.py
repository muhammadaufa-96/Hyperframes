"""26/11 edit: hari anugerah anak, "akhlak ibarat bunga" (pesan arwah atuk). Soft style: fades, slow zooms, no glitch.
usage: python3 build26.py   (needs f2611/winA/a/words.json, f2611/edit/segs_a.json, assets/footage/f2611/*)"""
import json, re, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2111")
from kit21 import V21, ICON, esc, Y, G, R
import gen

W = "/home/user/Hyperframes/f2611"
F = "../assets/footage/f2611/"
END = 3.2
P = "#ff8ab0"   # petal pink

FIX = {12.60: "cemerlang", 22.01: "kan.", 26.52: "terkesan", 42.02: "atuk", 73.95: None, 97.24: "Korang", 100.51: "korang",
       108.29: "life,", 109.80: "Okay,"}
HOT = {"alhamdulillah", "anugerah", "kecemerlangan", "cemerlang", "sulung", "bangga", "happy", "guru", "besar", "sekolah", "ilmu",
       "akhlak", "baik", "atuk", "bunga", "indah", "mata", "hati", "senang", "seronok", "sisi", "benchmark", "bertikam-tikam",
       "boyfriend", "girlfriend", "anak-anak", "manfaat", "komen", "like", "share", "follow"}

gen.CSS += r"""
.ph-b { position: absolute; left: 70px; top: 300px; display: flex; align-items: center; gap: 14px; background: #f5c22e; color: #15171a; border-radius: 999px; padding: 12px 30px 12px 14px; font-weight: 800; font-size: 40px; text-transform: uppercase; box-shadow: 0 16px 40px rgba(0,0,0,0.45); }
.ph-b .ico { width: 56px; height: 56px; border-radius: 50%; background: #15171a; color: #f5c22e; padding: 11px; }
.qq { position: absolute; left: 60px; right: 60px; top: 260px; background: rgba(12,13,16,0.86); border-radius: 30px; padding: 34px 40px 30px; box-shadow: 0 24px 60px rgba(0,0,0,0.5); }
.qq-m { position: absolute; left: 30px; top: -40px; font-family: Georgia, serif; font-weight: 800; font-size: 200px; line-height: 1; color: #f5c22e; }
.qq-t { font-weight: 800; font-size: 52px; line-height: 1.18; color: #fff; }
.qq-t span { display: inline-block; margin-right: 12px; }
.qq-t span.y { color: #f5c22e; }
.qq-a { margin-top: 18px; font-weight: 600; font-size: 32px; color: #d9dadc; letter-spacing: 0.06em; text-transform: uppercase; }
.at { position: absolute; left: 0; right: 0; top: 300px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
.at-k { font-weight: 600; font-size: 38px; letter-spacing: 0.22em; text-transform: uppercase; color: #fff; text-shadow: 0 3px 14px rgba(0,0,0,0.8); }
.at-t { font-weight: 800; font-size: 96px; line-height: 1; text-transform: uppercase; color: #f5c22e; text-shadow: 0 6px 0 rgba(0,0,0,0.35), 0 0 40px rgba(0,0,0,0.6); }
.at-l { width: 420px; height: 6px; transform-origin: 50% 50%; border-radius: 3px; background: #f5c22e; }
.fw { position: absolute; left: 60px; right: 60px; top: 250px; height: 470px; background: rgba(12,13,16,0.84); border-radius: 30px; box-shadow: 0 24px 60px rgba(0,0,0,0.5); }
.fw svg { position: absolute; left: 30px; top: 30px; }
.fw-t { position: absolute; left: 470px; right: 30px; top: 60px; display: flex; flex-direction: column; gap: 18px; }
.fw-h { font-weight: 800; font-size: 34px; letter-spacing: 0.08em; text-transform: uppercase; color: #f5c22e; }
.fw-b { font-weight: 800; font-size: 76px; line-height: 0.95; text-transform: uppercase; color: #fff; }
.fw-r { display: flex; align-items: center; gap: 12px; font-weight: 800; font-size: 34px; line-height: 1.1; color: #fff; }
.fw-r i { width: 18px; height: 18px; flex: none; border-radius: 50%; background: #ff8ab0; }
.qn { position: absolute; left: 70px; right: 70px; top: 270px; background: rgba(12,13,16,0.86); border-left: 12px solid #f5c22e; border-radius: 22px; padding: 24px 30px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }
.qn-k { font-weight: 800; font-size: 30px; letter-spacing: 0.1em; text-transform: uppercase; color: #f5c22e; }
.qn-t { margin-top: 10px; font-weight: 800; font-size: 58px; line-height: 1.08; color: #fff; }
"""


def words():
    out = []
    for x in json.load(open(f"{W}/winA/a/words.json")):
        k = round(x["start"], 2)
        t = FIX.get(k, x["text"]) if k in FIX else x["text"]
        if t is None:
            continue
        out.append([t, x["start"], x["end"]])
    for i in range(len(out) - 1):
        out[i][2] = min(out[i][2], out[i + 1][1])
    return out


def at(ws, tok, after=0.0):
    for x in ws:
        if x[1] >= after and re.sub(r"[^\w'-]", "", x[0]).lower() == tok.lower():
            return x[1]
    raise KeyError(f"{tok} after {after}")


def broll_snd(c, name, start, dur, media_start, vol=0.18, zoom=(1.03, 1.1)):
    w = c.uid("bw"); v = c.uid("bv")
    c.layers.append(f'<div class="cam" id="{w}"><video id="{v}" class="clip" src="{F}broll_{name}.mp4" playsinline data-has-audio="true" '
                    f'data-volume="{vol}" data-start="{start:.3f}" data-duration="{dur:.3f}" data-media-start="{media_start:.3f}" data-track-index="1"></video></div>')
    c.js.append(f'tl.fromTo("#{w}", {{ scale: {zoom[0]} }}, {{ scale: {zoom[1]}, duration: {dur:.3f}, ease: "none" }}, {start:.3f});')


def photo(c, name, start, dur, zoom=(1.0, 1.1), origin="50% 40%"):
    c.image(F + name, start, dur, zoom=zoom, origin=origin)
    d = c.uid("pd")    # soft dip into the photo
    c.layers.append(f'<section id="{d}" class="clip" data-start="{start - 0.15:.3f}" data-duration="0.45" data-track-index="7"><div class="tdip" id="{d}x" style="background:#fff"></div></section>')
    c.js.append(f'tl.fromTo("#{d}x", {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 0.6, duration: 0.15 }}, {{ opacity: 0, duration: 0.3 }}] }}, {start - 0.15:.3f});')


def badge(c, text, start, dur, icon="check"):
    b = c.uid("pb")
    c.layers.append(f'<section id="{b}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                    f'<div class="ph-b" id="{b}m">{c.ico(icon)}{esc(text)}</div></section>')
    c.js.append(f'tl.fromTo("#{b}m", {{ scale: 0.3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.5, ease: "back.out(2.2)" }}, {start:.3f});')
    c.js.append(f'tl.to("#{b}m", {{ opacity: 0, y: -20, duration: 0.25 }}, {start + dur - 0.25:.3f});')
    c.sfx("sparkle", start, 0.4)


def quote(c, ws, start, end, words_at, hot=()):
    """words_at: [(word, t)] revealed one by one as they are spoken."""
    q = c.uid("qq")
    sp = "".join(f'<span id="{q}w{i}" class="{"y" if w.lower() in hot else ""}">{esc(w)}</span>' for i, (w, t) in enumerate(words_at))
    c.layers.append(f'<section id="{q}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                    f'<div class="qq" id="{q}m"><div class="qq-m">“</div><div class="qq-t">{sp}</div><div class="qq-a" id="{q}a">Kata-kata guru besar</div></div></section>')
    J = c.js.append
    J(f'tl.fromTo("#{q}m", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start:.3f});')
    for i, (w, t) in enumerate(words_at):
        J(f'tl.fromTo("#{q}w{i}", {{ opacity: 0.12, filter: "blur(6px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.18 }}, {t:.3f});')
    J(f'tl.fromTo("#{q}a", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4 }}, {words_at[-1][1] + 0.3:.3f});')
    J(f'tl.to("#{q}m", {{ opacity: 0, y: -30, duration: 0.3 }}, {end - 0.3:.3f});')
    c.sfx("whoosh-short", start, 0.3); c.sfx("chime", words_at[-1][1] + 0.2, 0.35)


def atuk(c, start, end):
    a = c.uid("at")
    c.layers.append(f'<section id="{a}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                    f'<div class="at"><div class="at-k" id="{a}k">Pesan</div><div class="at-t" id="{a}t">Arwah atuk</div><div class="at-l" id="{a}l"></div></div></section>')
    J = c.js.append
    J(f'tl.fromTo("#{a}k", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, {start:.3f});')
    J(f'tl.fromTo("#{a}t", {{ opacity: 0, filter: "blur(12px)", scale: 1.1 }}, {{ opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.8, ease: "power2.out" }}, {start + 0.2:.3f});')
    J(f'tl.fromTo("#{a}l", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.8, ease: "power2.inOut" }}, {start + 0.6:.3f});')
    J(f'tl.to("#{a} .at > *", {{ opacity: 0, duration: 0.4 }}, {end - 0.4:.3f});')
    c.sfx("sparkle", start + 0.2, 0.3)


def flower(c, start, end, t_bunga, t_indah, t_hati):
    f = c.uid("fw")
    cx, cy = 200, 205
    petals = "".join(f'<ellipse id="{f}p{i}" cx="{cx}" cy="{cy - 78}" rx="46" ry="82" fill="{P}" stroke="#fff" stroke-width="3" transform="rotate({i * 45} {cx} {cy})" opacity="0.95"/>' for i in range(8))
    svg = (f'<svg width="400" height="410" viewBox="0 0 400 410">'
           f'<path id="{f}s" d="M{cx} {cy + 30} C {cx - 10} 300, {cx + 20} 340, {cx} 400" stroke="{G}" stroke-width="12" fill="none" stroke-linecap="round" stroke-dasharray="240" stroke-dashoffset="240"/>'
           f'<path id="{f}lf" d="M{cx + 4} 330 C 250 300, 290 310, 300 330 C 280 350, 240 350, {cx + 4} 330 Z" fill="{G}"/>'
           f'{petals}<circle id="{f}c" cx="{cx}" cy="{cy}" r="44" fill="{Y}" stroke="#fff" stroke-width="4"/></svg>')
    c.layers.append(f'<section id="{f}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                    f'<div class="fw" id="{f}m">{svg}<div class="fw-t"><div class="fw-h">Akhlak ibarat</div><div class="fw-b" id="{f}b">Bunga</div>'
                    f'<div class="fw-r" id="{f}r1"><i></i>Indah dilihat mata</div><div class="fw-r" id="{f}r2"><i></i>Senang dirasa hati</div></div></div></section>')
    J = c.js.append
    J(f'tl.fromTo("#{f}m", {{ y: 50, opacity: 0, scale: 0.94 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.6, ease: "power3.out" }}, {start:.3f});')
    J(f'tl.to("#{f}s", {{ strokeDashoffset: 0, duration: 0.7, ease: "power2.out" }}, {start + 0.2:.3f});')
    J(f'tl.fromTo("#{f}lf", {{ scale: 0, transformOrigin: "0% 50%" }}, {{ scale: 1, duration: 0.5, ease: "back.out(2)" }}, {start + 0.7:.3f});')
    J(f'tl.fromTo("#{f}c", {{ scale: 0, svgOrigin: "{cx} {cy}" }}, {{ scale: 1, duration: 0.4, ease: "back.out(3)", svgOrigin: "{cx} {cy}" }}, {t_bunga - 0.3:.3f});')
    for i in range(8):
        J(f'tl.fromTo("#{f}p{i}", {{ scale: 0, svgOrigin: "{cx} {cy}" }}, {{ scale: 1, duration: 0.55, ease: "back.out(2.2)", svgOrigin: "{cx} {cy}" }}, {t_bunga - 0.15 + i * 0.07:.3f});')
    J(f'tl.fromTo("#{f}b", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "back.out(2)" }}, {t_bunga:.3f});')
    J(f'tl.fromTo("#{f}r1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4 }}, {t_indah:.3f});')
    J(f'tl.fromTo("#{f}r2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.4 }}, {t_hati:.3f});')
    J(f'tl.to("#{f}m", {{ opacity: 0, y: -30, duration: 0.35 }}, {end - 0.35:.3f});')
    c.sfx("whoosh-short", start, 0.3); c.sfx("sparkle", t_bunga, 0.45); c.sfx("pop", t_indah, 0.3); c.sfx("pop", t_hati, 0.3)


def ask(c, start, end, text):
    q = c.uid("qn")
    c.layers.append(f'<section id="{q}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                    f'<div class="qn" id="{q}m"><div class="qn-k">Soalan untuk parents</div><div class="qn-t">{text}</div></div></section>')
    c.js.append(f'tl.fromTo("#{q}m", {{ x: -900 }}, {{ x: 0, duration: 0.6, ease: "expo.out" }}, {start:.3f});')
    c.js.append(f'tl.to("#{q}m", {{ x: 900, duration: 0.35, ease: "power3.in" }}, {end - 0.35:.3f});')
    c.sfx("whoosh-short", start, 0.35)


def build():
    segs = json.load(open(f"{W}/edit/segs_a.json"))
    A = segs["duration"]
    ws = words()
    T = lambda tok, after=0.0: at(ws, tok, after)
    c = V21("v2611-akhlak-ibarat-bunga", A + END)
    c.setup(A, segs)
    c.aroll(F + "aroll_a.mp4", [(0.0, A, 0.0)])
    c.shade(0, A)
    c.camera21(punches=[(T("bangga"), 0.9), (T("akhlak", 34), 0.9), (T("benchmark"), 1.0), (T("bertikam-tikam"), 0.9)])

    # opening: the event footage under the title, then the award moment
    broll_snd(c, "6945", 0.0, T("hari", 5.8) - 0.05, 2.0)
    c.hook21("Hari anugerah anak aku", "Akhlak", "ibarat bunga", 0.0, 4.2, icon="heart")
    broll_snd(c, "6945", T("hari", 5.8) - 0.05, T("dan", 10) - T("hari", 5.8) + 0.4, 40.5)
    photo(c, "IMG_6973.jpg", T("salah") - 0.1, T("aku", 16) - T("salah") + 0.3, origin="50% 45%")
    badge(c, "Pelajar cemerlang", T("anak", 13) - 0.2, 2.6, icon="check")
    photo(c, "IMG_6947.jpg", T("of") - 0.1, T("kita", 20.6) - T("of") + 0.1, zoom=(1.08, 1.0))
    photo(c, "IMG_6968.jpg", T("kita", 20.6), T("kan") - T("kita", 20.6) + 0.5, origin="50% 55%")
    photo(c, "IMG_6967.jpg", T("kan") + 0.5, T("guru") - T("kan") - 0.5, zoom=(1.0, 1.08))
    broll_snd(c, "6945", T("guru"), T("dia", 25) - T("guru") + 0.4, 44.0, vol=0.12)

    quote(c, ws, T("sekolah", 27) - 0.4, T("jadi", 35.5) + 0.1,
          [("Sekolah", T("sekolah", 27)), ("bukan", T("bukan", 30)), ("sekadar", T("sekadar", 30)), ("tempat", T("tempat", 31.5)),
           ("menuntut", T("menuntut")), ("ilmu,", T("ilmu")), ("tapi", T("tapi", 33)), ("membina", T("membina", 33.9)),
           ("akhlak", T("akhlak", 34)), ("yang", T("yang", 34.5)), ("baik.", T("baik", 34.8))], hot={"akhlak", "ilmu,"})
    atuk(c, T("teringat") - 0.3, T("dengan", 44.5) - 0.1)
    c.trans(T("dengan", 44.5), "dip")
    flower(c, T("dengan", 44.5) + 0.2, T("maksudnya") + 0.2, t_bunga=T("bunga"), t_indah=T("indah"), t_hati=T("hati"))
    c.glass("Tanda akhlak yang baik", ["Orang senang tengok kita", "Seronok lihat kita", "Selesa di sisi kita"], T("maksudnya") + 0.3,
            T("zaman") - T("maksudnya") - 0.5, top=270, at=[T("senang", 56.8), T("seronok"), T("sisi")],
            icons=[("✓", ""), ("✓", ""), ("✓", "")])
    c.trans(T("zaman") - 0.6, "zoom")
    c.glass("Zaman sekarang", ["Budak sanggup bertikam", "Gaduh sebab boyfriend, girlfriend", "Nilai akhlak tak diterapkan"],
            T("macam-macam") - 0.3, T("dan", 85) - T("macam-macam") + 0.2, top=270,
            at=[T("bertikam-tikam"), T("boyfriend"), T("diterapkan")], icons=[("!", "w"), ("!", "w"), ("!", "w")])
    c.sfx("error", T("bertikam-tikam") + 0.05, 0.15, dur=0.4)
    c.trans(T("dan", 85), "dip")
    ask(c, T("dan", 85) + 0.2, T("korang", 96.9) - 0.1, "Macam mana nak pastikan <em style='font-style:normal;color:#f5c22e'>anak-anak</em> kita berakhlak baik?")
    c.comment_ask(T("korang", 96.9), T("and", 100.3) - 0.1, "Pandangan korang?", T("komen"))
    c.trans(T("and", 100.3), "whip")
    c.cta(T("and", 100.3) + 0.1, A - 2.0, t_like=T("like"), t_share=T("share", 101), t_follow=T("follow"),
          topics=[("Renovation", T("tips")), ("Life", T("life")), ("Business", T("business"))])
    c.image(F + "IMG_6970.jpg", A, END, zoom=(1.0, 1.06))
    c.end_card("bangfasz", 'Follow<em>for more</em>', "Renovation · Business · Life", "+ Follow bangfasz", A, END, logo=None)
    c.captions_box(ws, HOT, hide=[(A, A + END)])
    c.write("/home/user/Hyperframes/compositions/v2611-akhlak-ibarat-bunga.html", "26/11: Akhlak ibarat bunga (hari anugerah anak)")


if __name__ == "__main__":
    build()
