"""23/11 edit: kabinet kena hiccup, semua dibuat di site.
usage: python3 build23.py   (needs f2311/winA/a/words.json, f2311/edit/segs_a.json, assets/footage/f2311/aroll_a.mp4 + broll_*.mp4)"""
import json, re, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2111")
from kit21 import V21, ICON, esc, Y, G, R
import gen

W = "/home/user/Hyperframes/f2311"
F = "../assets/footage/f2311/"
END = 3.2

FIX = {0.06: "Okay,", 0.43: "mesti", 20.79: None, 26.45: "selesaikan.", 36.28: "Edging", 39.11: "Ui,", 41.99: "itulah", 42.18: "geng.",
       52.65: "walau bagaimanapun.", 53.28: None, 54.87: "korang", 68.68: "sinki."}
EXTRA = [["Assalamualaikum.", 73.45, 74.1]]
HOT = {"kabinet", "hiccup", "settlekan", "spot", "edging", "laminate", "site", "isu", "alhamdulillah", "fully", "potong", "gila",
       "boleh", "control", "tak", "track", "kreatif", "sinki", "like", "share"}

gen.CSS += r"""
.cv2 { position: absolute; left: 60px; right: 60px; top: 270px; display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.cv2-c { background: rgba(14,16,20,0.88); border-radius: 24px; padding: 20px 18px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; border-top: 10px solid; box-shadow: 0 20px 50px rgba(0,0,0,0.5); }
.cv2-c .ico { width: 84px; height: 84px; border-radius: 50%; padding: 16px; color: #fff; }
.cv2-c b { font-weight: 800; font-size: 40px; line-height: 1.02; text-transform: uppercase; }
.cv2-c span { font-weight: 600; font-size: 26px; color: #d9dadc; }
.cv2-x { position: absolute; left: 60px; right: 60px; top: 560px; display: flex; justify-content: center; }
.cv2-x div { display: flex; align-items: center; gap: 14px; background: rgba(14,16,20,0.9); border: 3px solid #20b26b; border-radius: 999px; padding: 10px 30px 10px 12px; font-weight: 800; font-size: 40px; text-transform: uppercase; }
.cv2-x .ico { width: 56px; height: 56px; border-radius: 50%; background: #20b26b; padding: 10px; color: #fff; }
"""


def words():
    out = []
    for x in json.load(open(f"{W}/winA/a/words.json")):
        k = round(x["start"], 2)
        t = FIX.get(k, x["text"]) if k in FIX else x["text"]
        if t is None:
            continue
        if re.sub(r"[^\w]", "", t).lower() == "side":
            t = re.sub(r"(?i)side", "site", t)
        out.append([t, x["start"], x["end"]])
    out += [list(e) for e in EXTRA]
    out.sort(key=lambda v: v[1])
    for i in range(len(out) - 1):
        out[i][2] = min(out[i][2], out[i + 1][1])
    return out


def at(ws, tok, after=0.0):
    for x in ws:
        if x[1] >= after and re.sub(r"[^\w'-]", "", x[0]).lower() == tok.lower():
            return x[1]
    raise KeyError(f"{tok} after {after}")


def broll_snd(c, name, start, dur, media_start, label=None, vol=0.14, zoom=(1.04, 1.12)):
    """B-roll with its own work sound kept low under the voice."""
    w = c.uid("bw"); v = c.uid("bv")
    c.layers.append(f'<div class="cam" id="{w}"><video id="{v}" class="clip" src="{F}broll_{name}.mp4" playsinline data-has-audio="true" '
                    f'data-volume="{vol}" data-start="{start:.3f}" data-duration="{dur:.3f}" data-media-start="{media_start:.3f}" data-track-index="1"></video></div>')
    c.js.append(f'tl.fromTo("#{w}", {{ scale: {zoom[0]} }}, {{ scale: {zoom[1]}, duration: {dur:.3f}, ease: "none" }}, {start:.3f});')
    if label:
        c.chip(label, start + 0.15, dur - 0.2, x=70, y=320, yellow=True)


def control_vs(c, start, end, t_boleh, t_tak, t_track, t_kreatif):
    k = c.uid("cv")
    c.layers.append(f'<section id="{k}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                    f'<div class="cv2"><div class="cv2-c" id="{k}a" style="border-color:{G}"><span class="ico" style="background:{G}">{ICON["check"]}</span><b>Boleh<br>control</b><span>urus ikut plan</span></div>'
                    f'<div class="cv2-c" id="{k}b" style="border-color:{R}"><span class="ico" style="background:{R}">{ICON["plus"]}</span><b>Tak boleh<br>control</b><span>hiccup di site</span></div></div>'
                    f'<div class="cv2-x" id="{k}t"><div><span class="ico">{ICON["check"]}</span>Pastikan on track</div></div>'
                    f'<div class="st2 y" style="top:700px"><span id="{k}k" style="font-size:96px">Kena kreatif!</span></div></section>')
    J = c.js.append
    J(f'tl.fromTo("#{k}a", {{ x: -600, rotation: -8, opacity: 0 }}, {{ x: 0, rotation: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, {t_boleh:.3f});')
    J(f'tl.fromTo("#{k}b", {{ x: 600, rotation: 8, opacity: 0 }}, {{ x: 0, rotation: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, {t_tak:.3f});')
    J(f'tl.fromTo("#{k}b .ico", {{ rotation: 0 }}, {{ rotation: 45, duration: 0.3, ease: "back.out(3)" }}, {t_tak + 0.3:.3f});')
    J(f'tl.to("#{k}a", {{ opacity: 0.4, scale: 0.94, duration: 0.3 }}, {t_track - 0.1:.3f});')
    J(f'tl.to("#{k}b", {{ scale: 1.05, duration: 0.3, ease: "back.out(2)" }}, {t_track - 0.1:.3f});')
    J(f'tl.fromTo("#{k}t", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, {t_track:.3f});')
    J(f'tl.fromTo("#{k}k", {{ scale: 0.2, opacity: 0, rotation: 12 }}, {{ scale: 1, opacity: 1, rotation: -4, duration: 0.55, ease: "elastic.out(1, 0.5)" }}, {t_kreatif:.3f});')
    J(f'tl.to(["#{k} .cv2", "#{k}t", "#{k}k"], {{ opacity: 0, y: -30, duration: 0.25, stagger: 0.04 }}, {end - 0.3:.3f});')
    c.sfx("whoosh-short", t_boleh, 0.4); c.sfx("whoosh", t_tak, 0.4); c.sfx("pop", t_track, 0.35)
    c.sfx("riser", t_kreatif - 0.6, 0.15, dur=0.6); c.sfx("impact-bass-1", t_kreatif, 0.45, dur=1.0); c.sfx("sparkle", t_kreatif + 0.1, 0.35)


def build():
    segs = json.load(open(f"{W}/edit/segs_a.json"))
    A = segs["duration"]
    ws = words()
    T = lambda tok, after=0.0: at(ws, tok, after)
    c = V21("v2311-kabinet-hiccup", A + END)
    c.setup(A, segs)
    c.aroll(F + "aroll_a.mp4", [(0.0, A, 0.0)])
    c.shade(0, A)
    c.camera21(punches=[(T("hiccup"), 1.0), (T("spot"), 0.8), (T("isu"), 0.9), (T("gila"), 1.2), (T("kreatif"), 0.9)],
               shakes=[T("gila")])

    # sections: intro -> di site -> pengajaran -> update -> CTA
    c.trans(27.66, "wipe", "Part 2", "Semua<br>di site")
    c.trans(42.30, "zoom")
    c.trans(54.50, "wipe", "Update", "Sekarang")
    c.trans(69.10, "dip")
    c.trans(20.79, "whip")

    c.hook21("Kerja kabinet di site", "Kena", "hiccup?", 0.0, 3.3, icon="hammer")
    c.stamp2("Settle on<br>the spot!", T("settlekan") - 0.1, 2.0, top=560)

    broll_snd(c, "6786", T("edging") - 0.4, 2.2, 2.0, "Edging di site")
    broll_snd(c, "6784", T("potong") - 0.3, T("video") - T("potong") + 0.2, 0.5, "Potong laminate")
    c.glass("Semua buat di site", ["Fully laminate", "Potong di site", "Edging di site"], T("fully") - 0.4, T("gila") - T("fully") + 0.1,
            top=270, at=[T("fully"), T("potong", 34), T("edging", 36)])
    broll_snd(c, "6784", T("fully") - 0.2, 1.95, 14.0)
    broll_snd(c, "6767", T("potong", 32) - 0.1, 2.9, 0.3)
    c.stamp2("Gila ke apa?!", T("gila") - 0.05, 2.2, top=560)
    control_vs(c, T("ada", 42) - 0.3, T("kita", 53.5) + 0.9, t_boleh=T("boleh", 43.5), t_tak=T("tak", 45), t_track=T("make", 48),
               t_kreatif=T("kreatif"))

    broll_snd(c, "6781", T("tengah", 56) - 0.2, 2.6, 0.3, "Potong top kaunter")
    broll_snd(c, "6786", T("edging", 59) - 0.3, 1.9, 6.5)
    broll_snd(c, "6786", T("laminate", 61) - 0.3, 1.6, 12.0)
    broll_snd(c, "6781", T("ruangan") - 0.3, T("korang", 68.5) - T("ruangan") + 0.2, 5.4, "Ruang sinki")

    c.cta(T("korang", 68.5), A - 0.3, t_like=T("like"), t_share=T("share", 70), t_follow=T("share", 70) + 0.7, topics=[])
    c.image(F + "last_a.jpg", A, END, zoom=(1.0, 1.06))
    c.end_card("bangfasz", 'Follow<em>for more</em>', "Renovation · Business · Life", "+ Follow bangfasz", A, END, logo=None)
    c.captions_box(ws, HOT, hide=[(A, A + END)])
    c.write("/home/user/Hyperframes/compositions/v2311-kabinet-hiccup.html", "23/11: Kabinet kena hiccup, semua di site")


if __name__ == "__main__":
    build()
