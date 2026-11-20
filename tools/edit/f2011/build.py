"""20/11/26 vlog "Enjoy proses yang Tuhan susun" — built on the user's own cut (Drive: Dah siap cut.mov).
usage: python3 build.py   (needs f2011/wincut/words.json + assets/footage/f2011/cut.mp4, last.jpg)
Writes compositions/v2011-enjoy-proses.html"""
import json, re, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
from kit import K, Y, esc
import gen

W = "/home/user/Hyperframes/f2011"
F = "../assets/footage/f2011/"
OUT = "/home/user/Hyperframes/compositions/v2011-enjoy-proses.html"
A = 103.567          # length of the user's cut
END = 3.2            # follow card after the last word
CUTS = [7.2, 20.833, 22.033, 27.367, 41.6, 78.433, 80.5, 91.0, 98.333]   # jump cuts in the user's edit
BIG = {41.6, 80.5, 98.333}                                              # cuts that change place / topic
G = "#20b26b"; R = "#ff3b3b"

# ---------------------------------------------------------------- words
FIX = {  # (rounded start) -> text; None drops the word
    3.00: "tu,", 4.70: "buat", 5.84: "tu,", 10.31: "adalah", 12.49: "straight", 13.51: "sebenarnya", 14.83: "dia",
    16.96: "jalan", 18.10: "serong", 26.04: "tauhid", 27.34: "kita", 36.78: "korang", 37.76: "tahu", 45.38: "tiba-tiba",
    45.71: "hiccup,", 53.49: "betul-betul", 53.88: None, 55.23: "betul-betul", 56.04: None, 60.55: "dah", 61.76: "tu",
    65.22: "kita", 67.08: "enjoy", 83.45: "journey", 90.16: "korang", 92.04: "and", 94.24: "for", 96.37: "dalam", 99.74: "okay,",
}


def words():
    out = []
    for x in json.load(open(f"{W}/wincut/words.json")):
        k = round(x["start"], 2)
        t = FIX.get(k, x["text"]) if k in FIX else x["text"]
        if t is None:
            out[-1][2] = x["end"]
            continue
        out.append([t, x["start"], x["end"]])
    for i in range(len(out) - 1):            # whisper stretches words over pauses
        out[i][2] = min(out[i][2], out[i + 1][1])
    return out


def at(w, token, after=0.0):
    for x in w:
        if x[1] >= after and re.sub(r"[^\w'-]", "", x[0]).lower() == token.lower():
            return x[1]
    raise KeyError(token)


HOT = {"rancang", "bayangkan", "straight", "tuhan", "serong", "kanan", "kiri", "track", "dalaman", "tauhid", "asas", "hidup",
       "loading", "selangor", "hiccup", "masalah", "baru", "terjun", "tukang", "okay", "enjoy", "proses", "susun", "jantan",
       "journey", "2027", "target", "like", "share", "follow", "renovation", "business", "kehidupan"}

# ---------------------------------------------------------------- icons (inline SVG, no emoji)
ICON = {
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z" fill="currentColor"/></svg>',
    "box": '<svg viewBox="0 0 24 24"><path d="M3 7l9-4 9 4v10l-9 4-9-4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M3 7l9 4 9-4M12 11v10" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    "hammer": '<svg viewBox="0 0 24 24"><path d="M14 3l7 7-3 3-2-2-8.5 8.5a2.1 2.1 0 0 1-3-3L13 8l-2-2z" fill="currentColor"/></svg>',
    "heart": '<svg viewBox="0 0 24 24"><path d="M12 21s-8-5.2-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 5.8-8 11-8 11z" fill="currentColor"/></svg>',
    "share": '<svg viewBox="0 0 24 24"><path d="M14 4l7 7-7 7v-4c-5 0-8 1.5-11 5 1-5 4-10 11-11z" fill="currentColor"/></svg>',
    "plus": '<svg viewBox="0 0 24 24"><path d="M12 4v16M4 12h16" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/></svg>',
    "paw": '<svg viewBox="0 0 24 24"><circle cx="6" cy="9" r="2.2" fill="currentColor"/><circle cx="10" cy="5.5" r="2.2" fill="currentColor"/><circle cx="14" cy="5.5" r="2.2" fill="currentColor"/><circle cx="18" cy="9" r="2.2" fill="currentColor"/><path d="M12 11c-3 0-6 4-6 6.5 0 2 2 2.5 3 2.2 1.2-.3 2-.7 3-.7s1.8.4 3 .7c1 .3 3-.2 3-2.2 0-2.5-3-6.5-6-6.5z" fill="currentColor"/></svg>',
    "lock": '<svg viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="currentColor"/><path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>',
    "check": '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

gen.CSS += r"""
/* ---------- 20/11 kit ---------- */
.pnl { position: absolute; left: 60px; right: 60px; top: 290px; background: rgba(14,16,20,0.84); border: 2px solid rgba(255,255,255,0.14); border-radius: 30px; box-shadow: 0 26px 70px rgba(0,0,0,0.5); overflow: hidden; }
.pnl-h { position: absolute; left: 32px; top: 24px; font-weight: 800; font-size: 30px; letter-spacing: 0.1em; text-transform: uppercase; color: #f5c22e; }
.ico { display: inline-flex; align-items: center; justify-content: center; flex: none; }
.ico svg { width: 100%; height: 100%; }

/* hook */
.hk { position: absolute; left: 0; right: 0; top: 285px; display: flex; flex-direction: column; align-items: center; gap: 4px; }
.hk-k { font-weight: 600; font-size: 40px; letter-spacing: 0.16em; text-transform: uppercase; color: #fff; text-shadow: 0 3px 14px rgba(0,0,0,0.7); }
.hk-row { display: flex; align-items: baseline; gap: 26px; }
.hk-a, .hk-b { font-weight: 800; font-size: 132px; line-height: 1; text-transform: uppercase; text-shadow: 0 6px 0 rgba(0,0,0,0.35), 0 0 40px rgba(0,0,0,0.5); }
.hk-a { color: #fff; } .hk-b { color: #f5c22e; }
.hk-a span, .hk-b span { display: inline-block; }
.hk-vs { font-weight: 800; font-size: 54px; color: #fff; background: #ff3b3b; border-radius: 14px; padding: 4px 16px; transform: rotate(-6deg); }
.hk-l { width: 820px; height: 90px; }

/* road */
.rd svg { position: absolute; left: 0; top: 0; }
.rd-lab { position: absolute; font-weight: 800; font-size: 34px; text-transform: uppercase; padding: 6px 16px; border-radius: 10px; white-space: nowrap; }
.rd-lab.g { background: rgba(255,255,255,0.14); color: #d9dadc; }
.rd-lab.y { background: #f5c22e; color: #15171a; }
.rd-car { position: absolute; width: 44px; height: 44px; margin: -22px 0 0 -22px; will-change: transform; border-radius: 50%; background: #fff; box-shadow: 0 0 0 8px rgba(245,194,46,0.45), 0 0 24px rgba(245,194,46,0.9); }
.rd-x { position: absolute; font-weight: 800; font-size: 110px; color: #ff3b3b; line-height: 1; }

/* foundation stack */
.fd-b { position: absolute; left: 32px; right: 32px; height: 104px; border-radius: 20px; display: flex; align-items: center; gap: 20px; padding: 0 24px; }
.fd-b b { font-weight: 800; font-size: 44px; text-transform: uppercase; line-height: 1; }
.fd-b span { display: block; font-weight: 600; font-size: 28px; margin-top: 4px; opacity: 0.85; text-transform: none; }
.fd-n { width: 66px; height: 66px; border-radius: 50%; background: #15171a; color: #f5c22e; font-weight: 800; font-size: 38px; display: flex; align-items: center; justify-content: center; flex: none; }
.fd-1 { background: #f5c22e; color: #15171a; }
.fd-2 { background: #ffffff; color: #15171a; }
.fd-ok { position: absolute; right: 30px; top: 18px; display: flex; align-items: center; gap: 10px; background: #20b26b; color: #fff; border-radius: 999px; padding: 8px 22px 8px 10px; font-weight: 800; font-size: 32px; text-transform: uppercase; }
.fd-ok .ico { width: 44px; height: 44px; background: rgba(255,255,255,0.22); border-radius: 50%; padding: 6px; }

/* route */
.rt-n { position: absolute; top: 96px; width: 150px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; }
.rt-n .ico { width: 104px; height: 104px; border-radius: 50%; padding: 22px; }
.rt-n b { font-weight: 800; font-size: 30px; text-transform: uppercase; line-height: 1.05; }
.rt-d { position: absolute; top: 146px; height: 0; border-top: 6px dashed rgba(255,255,255,0.35); }
.rt-f { position: absolute; top: 143px; height: 12px; border-radius: 6px; background: #f5c22e; transform-origin: left center; }
.rt-t { position: absolute; top: 120px; width: 60px; height: 60px; margin-left: -30px; border-radius: 14px; background: #fff; color: #15171a; padding: 10px; }

/* hiccup */
.plan { position: absolute; left: 0; right: 0; top: 330px; display: flex; justify-content: center; }
.plan div { display: flex; align-items: center; gap: 16px; background: #fff; color: #15171a; border-radius: 999px; padding: 14px 34px 14px 14px; font-weight: 800; font-size: 50px; text-transform: uppercase; box-shadow: 0 16px 40px rgba(0,0,0,0.45); }
.plan .ico { width: 64px; height: 64px; border-radius: 50%; background: #20b26b; color: #fff; padding: 12px; }
.hic { position: absolute; left: 0; right: 0; top: 470px; display: flex; justify-content: center; }
.hic span { display: inline-block; font-weight: 800; font-size: 150px; line-height: 1; text-transform: uppercase; color: #fff; background: #ff3b3b; border: 8px solid #fff; border-radius: 22px; padding: 6px 30px 12px; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
.rgb { position: absolute; inset: 0; mix-blend-mode: screen; }
.nw { position: absolute; left: 0; right: 0; top: 380px; display: flex; justify-content: center; }
.nw span { font-weight: 800; font-size: 76px; text-transform: uppercase; color: #15171a; background: #f5c22e; border-radius: 18px; padding: 10px 30px; box-shadow: 0 16px 40px rgba(0,0,0,0.45); }

/* tukang mode switch */
.md { position: absolute; left: 0; right: 0; top: 300px; display: flex; flex-direction: column; align-items: center; gap: 18px; }
.md-row { display: flex; align-items: center; gap: 26px; background: rgba(14,16,20,0.86); border: 2px solid rgba(255,255,255,0.16); border-radius: 999px; padding: 18px 26px 18px 22px; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
.md-row .ico { width: 92px; height: 92px; border-radius: 50%; background: #f5c22e; color: #15171a; padding: 18px; }
.md-t { font-weight: 800; font-size: 54px; text-transform: uppercase; white-space: nowrap; }
.md-sw { position: relative; width: 150px; height: 78px; border-radius: 999px; background: rgba(255,255,255,0.22); }
.md-k { position: absolute; left: 7px; top: 7px; width: 64px; height: 64px; border-radius: 50%; background: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.4); }
.md-on { position: absolute; inset: 0; border-radius: 999px; background: #20b26b; opacity: 0; }
.md-s { font-weight: 600; font-style: italic; font-size: 40px; color: #fff; background: rgba(14,16,20,0.75); border-radius: 14px; padding: 8px 22px; }

/* quote */
.qt-bg { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 45%, rgba(10,11,13,0.35) 0%, rgba(10,11,13,0.82) 75%); }
.qt { position: absolute; left: 50px; right: 50px; top: 360px; display: flex; flex-direction: column; align-items: center; text-align: center; }
.qt-s { font-weight: 600; font-size: 46px; letter-spacing: 0.08em; text-transform: uppercase; color: #d9dadc; }
.qt-b { font-weight: 800; font-size: 210px; line-height: 0.95; text-transform: uppercase; color: #f5c22e; text-shadow: 0 10px 0 rgba(0,0,0,0.35); }
.qt-m { font-weight: 800; font-size: 104px; line-height: 1; text-transform: uppercase; color: #fff; margin-top: 10px; }
.qt-u { width: 700px; height: 14px; margin-top: 18px; border-radius: 7px; background: #f5c22e; transform-origin: left center; }
.qt-e { font-weight: 800; font-size: 64px; line-height: 1.05; text-transform: uppercase; color: #fff; margin-top: 22px; }
.qt-e em { font-style: normal; color: #f5c22e; }

/* name tag */
.nt { position: absolute; left: 70px; top: 330px; display: flex; align-items: center; gap: 20px; background: #fff; color: #15171a; border-radius: 26px; padding: 18px 34px 18px 18px; box-shadow: 0 20px 50px rgba(0,0,0,0.45); }
.nt .ico { width: 96px; height: 96px; border-radius: 50%; background: #f5c22e; color: #15171a; padding: 18px; }
.nt b { display: block; font-weight: 800; font-size: 64px; text-transform: uppercase; line-height: 1; }
.nt span { display: block; font-weight: 600; font-size: 32px; color: #555; margin-top: 6px; }

/* teaser */
.ts { position: absolute; left: 0; right: 0; top: 290px; display: flex; flex-direction: column; align-items: center; gap: 14px; }
.ts-k { display: flex; align-items: center; gap: 12px; background: rgba(14,16,20,0.86); border: 2px solid rgba(255,255,255,0.18); border-radius: 999px; padding: 10px 26px 10px 12px; font-weight: 800; font-size: 34px; letter-spacing: 0.08em; text-transform: uppercase; }
.ts-k .ico { width: 52px; height: 52px; border-radius: 50%; background: #f5c22e; color: #15171a; padding: 11px; }
.ts-j { font-weight: 800; font-size: 104px; line-height: 1; text-transform: uppercase; color: #fff; text-shadow: 0 6px 0 rgba(0,0,0,0.35), 0 0 30px rgba(0,0,0,0.6); }
.ts-y { display: flex; align-items: center; gap: 20px; }
.ts-yl { font-weight: 800; font-size: 40px; text-transform: uppercase; color: #fff; background: rgba(14,16,20,0.8); border-radius: 12px; padding: 8px 18px; }
.ts-win { position: relative; height: 170px; width: 470px; overflow: hidden; border-radius: 22px; background: #f5c22e; box-shadow: 0 20px 50px rgba(0,0,0,0.45); }
.ts-reel { position: absolute; left: 0; right: 0; top: 0; }
.ts-reel div { height: 170px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 150px; color: #15171a; }

/* CTA */
.ct { position: absolute; left: 0; right: 0; top: 300px; display: flex; justify-content: center; gap: 26px; }
.ct-b { display: flex; flex-direction: column; align-items: center; gap: 10px; }
.ct-b .ico { width: 150px; height: 150px; border-radius: 50%; background: rgba(14,16,20,0.86); border: 3px solid rgba(255,255,255,0.22); color: #fff; padding: 38px; box-shadow: 0 18px 44px rgba(0,0,0,0.45); }
.ct-b b { font-weight: 800; font-size: 34px; text-transform: uppercase; text-shadow: 0 3px 12px rgba(0,0,0,0.8); }
.ct-r { position: absolute; left: 50%; top: 75px; width: 150px; height: 150px; margin: -75px 0 0 -75px; border-radius: 50%; border: 6px solid #f5c22e; opacity: 0; }
.tp { position: absolute; left: 0; right: 0; top: 560px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
.tp div { font-weight: 800; font-size: 50px; text-transform: uppercase; color: #15171a; background: #f5c22e; border-radius: 14px; padding: 8px 26px; }
.tp div.w { background: #fff; }

/* captions with a dark backing: white shirt in most shots */
.cv { position: absolute; left: 50px; right: 50px; top: 1300px; display: flex; justify-content: center; }
.cv-p { display: inline-block; max-width: 980px; text-align: center; background: rgba(12,13,16,0.72); border-radius: 22px; padding: 12px 26px 16px; }
.cv .w { display: inline-block; margin: 0 9px; font-weight: 800; font-size: 56px; line-height: 1.12; color: #fff; }
.cv .w.hot { color: #f5c22e; }

/* edge flash */
.ef { position: absolute; inset: 0; background: linear-gradient(90deg, rgba(245,194,46,0) 0%, rgba(245,194,46,0.85) 45%, rgba(255,255,255,0.95) 50%, rgba(245,194,46,0.85) 55%, rgba(245,194,46,0) 100%); }
"""


class V(K):
    def ico(self, name, cls="", style=""):
        return f'<span class="ico {cls}" style="{style}">{ICON[name]}</span>'

    # -- camera: alternate zoom on every jump cut, quick punch-ins on emphasis words, shake on the hiccup
    def camera(self, punches, shakes):
        z = 1.0
        base = []
        for t in CUTS:
            z = 1.0 if z != 1.0 else 1.08
            base.append((t, z))
        def zoom_at(t):
            zz = 1.0
            for c, v in base:
                if c <= t:
                    zz = v
            return zz
        self.js.append('tl.set("#acam", { scale: 1, transformOrigin: "50% 42%" }, 0);')
        for t, v in base:
            self.js.append(f'tl.set("#acam", {{ scale: {v} }}, {t:.3f});')
        for t, hold in punches:
            z0 = zoom_at(t)
            nxt = min([c for c in CUTS if c > t] + [A])
            back = min(t + hold, nxt - 0.35)
            self.js.append(f'tl.to("#acam", {{ scale: {z0 + 0.13:.3f}, duration: 0.28, ease: "power3.out" }}, {t - 0.05:.3f});')
            self.js.append(f'tl.to("#acam", {{ scale: {z0}, duration: 0.45, ease: "power2.inOut" }}, {back:.3f});')
        for t in shakes:
            self.js.append(f'tl.to("#acam", {{ keyframes: [{{ x: -26, rotation: -1.2 }}, {{ x: 22, rotation: 1 }}, {{ x: -14, rotation: -0.6 }}, {{ x: 8, rotation: 0.3 }}, {{ x: 0, rotation: 0 }}], duration: 0.42, ease: "none" }}, {t:.3f});')

    def flash(self, t):
        f = self.uid("ef")
        self.layers.append(f'<section id="{f}" class="clip" data-start="{t - 0.2:.3f}" data-duration="0.45" data-track-index="7"><div class="ef" id="{f}x"></div></section>')
        self.js.append(f'tl.fromTo("#{f}x", {{ x: -1200, opacity: 1 }}, {{ x: 1200, duration: 0.4, ease: "power2.inOut" }}, {t - 0.2:.3f});')
        self.sfx("whoosh-short", t - 0.2, 0.4)

    # -- 1. hook: PLAN vs REALITI, letters drop in, a scribble line draws from straight to winding
    def hook(self, start, dur):
        h = self.uid("hk")
        a = "".join(f'<span id="{h}a{i}">{c}</span>' for i, c in enumerate("PLAN"))
        b = "".join(f'<span id="{h}b{i}">{c}</span>' for i, c in enumerate("REALITI"))
        path = "M10 45 L300 45 C360 45 360 10 420 10 S 480 80 540 80 S 600 10 660 10 S 720 80 810 45"
        self.layers.append(f'<section id="{h}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="5">'
                           f'<div class="h2-sh"></div><div class="hk"><div class="hk-k" id="{h}k">Apa yang kita rancang...</div>'
                           f'<div class="hk-row"><div class="hk-a">{a}</div><div class="hk-vs" id="{h}v">VS</div></div><div class="hk-b">{b}</div>'
                           f'<svg class="hk-l" viewBox="0 0 820 90"><path id="{h}p" d="{path}" fill="none" stroke="{Y}" stroke-width="12" stroke-linecap="round" stroke-dasharray="1200" stroke-dashoffset="1200"/></svg></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{h}k", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {start:.3f});')
        for i in range(4):
            J(f'tl.fromTo("#{h}a{i}", {{ y: -140, opacity: 0, rotation: -12 }}, {{ y: 0, opacity: 1, rotation: 0, duration: 0.45, ease: "back.out(2.2)" }}, {start + 0.12 + i * 0.05:.3f});')
        J(f'tl.fromTo("#{h}v", {{ scale: 0, rotation: -40 }}, {{ scale: 1, rotation: -6, duration: 0.35, ease: "back.out(3)" }}, {start + 0.45:.3f});')
        for i in range(7):
            J(f'tl.fromTo("#{h}b{i}", {{ y: 140, opacity: 0, scale: 1.6 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "power4.out" }}, {start + 0.6 + i * 0.045:.3f});')
        J(f'tl.to("#{h}p", {{ strokeDashoffset: 0, duration: 1.1, ease: "power2.inOut" }}, {start + 0.9:.3f});')
        J(f'tl.to("#{h} .hk > *", {{ opacity: 0, y: -30, filter: "blur(8px)", duration: 0.25, stagger: 0.04, ease: "power2.in" }}, {start + dur - 0.35:.3f});')
        J(f'tl.to("#{h} .h2-sh", {{ opacity: 0, duration: 0.3 }}, {start + dur - 0.3:.3f});')
        self.sfx("whoosh", start, 0.45)
        self.sfx("impact-bass-1", start + 0.2, 0.5)
        self.sfx("pop", start + 0.45, 0.4)
        self.sfx("impact-bass-2", start + 0.65, 0.4)
        self.sfx("whoosh-short", start + 0.9, 0.3)

    # -- 2. road: straight plan crossed out, then the real winding road draws while a dot drives it
    def road(self, start, end, t_plan, t_no, t_real, turns):
        r = self.uid("rd")
        H = 360
        straight = "M80 200 L880 200"
        pts = [(80, 300), (230, 300), (330, 230), (430, 190), (560, 120), (650, 120), (760, 230), (880, 120)]
        real = f"M{pts[0][0]} {pts[0][1]} L{pts[1][0]} {pts[1][1]} Q300 300 {pts[2][0]} {pts[2][1]} T{pts[3][0]} {pts[3][1]} L{pts[4][0]} {pts[4][1]} L{pts[5][0]} {pts[5][1]} Q720 120 {pts[6][0]} {pts[6][1]} Q800 280 {pts[7][0]} {pts[7][1]}"
        labs = [("Serong", 350, 255), ("Kanan", 545, 50), ("Kiri", 720, 250)]
        lab_html = "".join(f'<div class="rd-lab y" id="{r}l{i}" style="left:{x}px;top:{y}px">{t}</div>' for i, (t, x, y) in enumerate(labs))
        self.layers.append(f'<section id="{r}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="pnl rd" id="{r}m" style="height:{H}px"><div class="pnl-h">Jalan hidup</div>'
                           f'<svg width="960" height="{H}" viewBox="0 0 960 {H}">'
                           f'<path id="{r}s" d="{straight}" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="12" stroke-linecap="round" stroke-dasharray="20 18"/>'
                           f'<path id="{r}rb" d="{real}" fill="none" stroke="rgba(245,194,46,0.25)" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1400" stroke-dashoffset="1400"/>'
                           f'<path id="{r}r" d="{real}" fill="none" stroke="{Y}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1400" stroke-dashoffset="1400"/></svg>'
                           f'<div class="rd-lab g" id="{r}pl" style="left:330px;top:120px">Yang kita bayang</div>'
                           f'<div class="rd-x" id="{r}x" style="left:440px;top:140px">✕</div>{lab_html}'
                           f'<div class="rd-car" id="{r}c" style="left:0;top:0"></div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{r}m", {{ y: -60, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.6)" }}, {start:.3f});')
        J(f'tl.fromTo("#{r}s", {{ strokeDashoffset: 800, opacity: 1 }}, {{ strokeDashoffset: 0, duration: 0.8, ease: "power2.out" }}, {t_plan:.3f});')
        J(f'tl.fromTo("#{r}pl", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {t_plan + 0.3:.3f});')
        J(f'tl.fromTo("#{r}x", {{ scale: 3, opacity: 0, rotation: -30 }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.25, ease: "power4.in" }}, {t_no:.3f});')
        J(f'tl.to(["#{r}s", "#{r}pl", "#{r}x"], {{ opacity: 0.18, duration: 0.4 }}, {t_real - 0.2:.3f});')
        draw_end = turns[-1] + 0.25
        J(f'tl.to(["#{r}r", "#{r}rb"], {{ strokeDashoffset: 0, duration: {draw_end - t_real:.3f}, ease: "none" }}, {t_real:.3f});')
        # dot follows the polyline knots on the same clock
        seg = (draw_end - t_real) / (len(pts) - 1)
        kf = ", ".join(f'{{ x: {x}, y: {y}, duration: {seg:.3f} }}' for x, y in pts[1:])
        J(f'tl.fromTo("#{r}c", {{ x: {pts[0][0]}, y: {pts[0][1]}, scale: 0 }}, {{ scale: 1, duration: 0.2 }}, {t_real - 0.15:.3f});')
        J(f'tl.to("#{r}c", {{ keyframes: [{kf}], ease: "none" }}, {t_real:.3f});')
        for i, t in enumerate(turns):
            J(f'tl.fromTo("#{r}l{i}", {{ scale: 0, rotation: -12 }}, {{ scale: 1, rotation: 0, duration: 0.3, ease: "back.out(3)" }}, {t:.3f});')
            self.sfx("pop", t, 0.4)
        J(f'tl.to("#{r}m", {{ y: -40, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4)
        self.sfx("click-soft", t_plan, 0.4)
        self.sfx("error", t_no, 0.35)
        self.sfx("riser", t_real, 0.2, dur=draw_end - t_real)

    # -- 3. foundation: two blocks drop and stack, then ON TRACK badge stamps on top
    def foundation(self, start, end, t1, t2, t_ok):
        f = self.uid("fd")
        H = 380
        self.layers.append(f'<section id="{f}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="pnl" id="{f}m" style="height:{H}px"><div class="pnl-h">Nak kekal on track</div>'
                           f'<div class="fd-ok" id="{f}ok">{self.ico("check")}On track</div>'
                           f'<div class="fd-b fd-2" id="{f}b2" style="top:{H - 250}px"><div class="fd-n">2</div><div><b>Kuatkan asas</b><span>cara kita jalani hidup</span></div></div>'
                           f'<div class="fd-b fd-1" id="{f}b1" style="top:{H - 130}px"><div class="fd-n">1</div><div><b>Kuat dalaman</b><span>tauhid kita dengan Tuhan</span></div></div>'
                           f'</div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{f}m", {{ x: -1100 }}, {{ x: 0, duration: 0.5, ease: "expo.out" }}, {start:.3f});')
        J(f'tl.fromTo("#{f}ok", {{ scale: 0, opacity: 0 }}, {{ scale: 0, opacity: 0, duration: 0.01 }}, {start:.3f});')
        J(f'tl.fromTo("#{f}b1", {{ y: -420, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.55, ease: "bounce.out" }}, {t1:.3f});')
        J(f'tl.fromTo("#{f}b2", {{ y: -300, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.55, ease: "bounce.out" }}, {t2:.3f});')
        J(f'tl.to("#{f}m", {{ y: 6, duration: 0.08, yoyo: true, repeat: 1 }}, {t1 + 0.3:.3f});')
        J(f'tl.to("#{f}m", {{ y: 6, duration: 0.08, yoyo: true, repeat: 1 }}, {t2 + 0.3:.3f});')
        J(f'tl.to("#{f}ok", {{ scale: 1, opacity: 1, rotation: -4, duration: 0.3, ease: "back.out(3)" }}, {t_ok:.3f});')
        J(f'tl.to("#{f}m", {{ borderColor: "{G}", duration: 0.3 }}, {t_ok:.3f});')
        J(f'tl.to("#{f}m", {{ x: 1100, duration: 0.35, ease: "power3.in" }}, {end - 0.35:.3f});')
        self.sfx("whoosh-short", start, 0.4)
        self.sfx("impact-bass-1", t1 + 0.3, 0.45)
        self.sfx("impact-bass-2", t2 + 0.3, 0.45)
        self.sfx("chime", t_ok, 0.45)

    # -- 4. route: box -> dashed road -> pin drop (Selangor)
    def route(self, start, end, t_box, t_go, t_pin):
        r = self.uid("rt")
        H = 330
        self.layers.append(f'<section id="{r}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="pnl" id="{r}m" style="height:{H}px"><div class="pnl-h">On the way ke site</div>'
                           f'<div class="rt-d" style="left:200px;right:200px"></div><div class="rt-f" id="{r}f" style="left:200px;right:200px"></div>'
                           f'<div class="rt-n" id="{r}a" style="left:40px">{self.ico("box", style="background:#fff;color:#15171a")}<b>Loading barang</b></div>'
                           f'<div class="rt-n" id="{r}b" style="right:40px">{self.ico("pin", style="background:#ff3b3b;color:#fff")}<b>Site<br>Selangor</b></div>'
                           f'<div class="rt-t ico" id="{r}t" style="left:200px">{ICON["box"]}</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{r}m", {{ y: -60, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.6)" }}, {start:.3f});')
        J(f'tl.fromTo("#{r}a", {{ scale: 0, rotation: -20 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.4)" }}, {t_box:.3f});')
        J(f'tl.fromTo("#{r}f", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {t_pin - t_go:.3f}, ease: "power1.inOut" }}, {t_go:.3f});')
        J(f'tl.fromTo("#{r}t", {{ x: 0, opacity: 0 }}, {{ x: 620, opacity: 1, duration: {t_pin - t_go:.3f}, ease: "power1.inOut" }}, {t_go:.3f});')
        J(f'tl.to("#{r}t", {{ opacity: 0, duration: 0.15 }}, {t_pin:.3f});')
        J(f'tl.fromTo("#{r}b", {{ y: -260, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "bounce.out" }}, {t_pin - 0.1:.3f});')
        J(f'tl.to("#{r}m", {{ y: -40, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4)
        self.sfx("pop", t_box, 0.45)
        self.sfx("riser", t_go, 0.18, dur=t_pin - t_go)
        self.sfx("impact-bass-2", t_pin + 0.25, 0.4)

    # -- 5. plan -> HICCUP glitch stamp -> "benda baru"
    def hiccup(self, t_plan, t_hic, t_new, end):
        h = self.uid("hc")
        self.layers.append(f'<section id="{h}" class="clip" data-start="{t_plan:.3f}" data-duration="{end - t_plan:.3f}" data-track-index="6">'
                           f'<div class="plan" id="{h}p"><div>{self.ico("check")}<span id="{h}pt">Plan</span></div></div>'
                           f'<div class="hic" id="{h}hw"><span id="{h}h">Hiccup!</span></div>'
                           f'<div class="rgb" id="{h}g" style="background:linear-gradient(0deg, rgba(255,0,60,0.35) 0 12%, transparent 12% 40%, rgba(0,255,255,0.3) 40% 46%, transparent 46% 70%, rgba(255,0,60,0.3) 70% 74%, transparent 74%)"></div>'
                           f'<div class="nw" id="{h}n"><span>Benda baru</span></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{h}p div", {{ scale: 0.3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2.4)" }}, {t_plan:.3f});')
        J(f'tl.fromTo("#{h}g", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, {t_plan:.3f});')
        J(f'tl.fromTo("#{h}hw", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, {t_plan:.3f});')
        J(f'tl.fromTo("#{h}n", {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, {t_plan:.3f});')
        # glitch: rgb bands jump for ~0.3 s, plan pill turns red and drops
        J(f'tl.to("#{h}g", {{ keyframes: [{{ opacity: 1, y: -40 }}, {{ opacity: 0.2, y: 60 }}, {{ opacity: 1, y: -120 }}, {{ opacity: 0.5, y: 20 }}, {{ opacity: 0, y: 0 }}], duration: 0.36, ease: "none" }}, {t_hic - 0.05:.3f});')
        J(f'tl.to("#{h}p div", {{ backgroundColor: "{R}", color: "#ffffff", rotation: 8, y: 30, duration: 0.2 }}, {t_hic:.3f});')
        J(f'tl.to("#{h}p", {{ y: 900, rotation: 25, opacity: 0, duration: 0.6, ease: "power3.in" }}, {t_hic + 0.6:.3f});')
        J(f'tl.to("#{h}hw", {{ opacity: 1, duration: 0.01 }}, {t_hic:.3f});')
        J(f'tl.fromTo("#{h}h", {{ scale: 2.6, rotation: -16, opacity: 0 }}, {{ scale: 1, rotation: -6, opacity: 1, duration: 0.22, ease: "power4.in" }}, {t_hic:.3f});')
        J(f'tl.to("#{h}h", {{ keyframes: [{{ x: -14 }}, {{ x: 12 }}, {{ x: -8 }}, {{ x: 0 }}], duration: 0.24 }}, {t_hic + 0.22:.3f});')
        J(f'tl.to("#{h}hw", {{ y: -60, opacity: 0, duration: 0.25, ease: "power2.in" }}, {t_new - 0.3:.3f});')
        J(f'tl.to("#{h}n", {{ opacity: 1, duration: 0.01 }}, {t_new:.3f});')
        J(f'tl.fromTo("#{h}n span", {{ scale: 0.2, rotation: 10 }}, {{ scale: 1, rotation: -3, duration: 0.45, ease: "elastic.out(1, 0.5)" }}, {t_new:.3f});')
        J(f'tl.to("#{h}n", {{ opacity: 0, y: -30, duration: 0.25 }}, {end - 0.25:.3f});')
        self.sfx("pop", t_plan, 0.4)
        self.sfx("glitch-short", t_hic - 0.05, 0.4)                # 0.7 s glitch with the RGB bands; never the 3.5 s glitch-2 static
        self.sfx("pop", t_hic + 0.18, 0.4)
        self.sfx("impact-bass-2", t_hic + 0.2, 0.35, dur=0.8)
        self.sfx("sparkle", t_new, 0.45)

    # -- 6. "mode tukang" switch flips ON, hammer swings
    def tukang(self, start, t_on, t_sub, end):
        m = self.uid("md")
        self.layers.append(f'<section id="{m}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="md"><div class="md-row" id="{m}r"><span class="ico" id="{m}i" style="width:92px;height:92px;border-radius:50%;background:{Y};color:#15171a;padding:18px">{ICON["hammer"]}</span>'
                           f'<div class="md-t">Mode tukang</div><div class="md-sw"><div class="md-on" id="{m}on"></div><div class="md-k" id="{m}k"></div></div></div>'
                           f'<div class="md-s" id="{m}s">dah lama tak buat sendiri</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{m}r", {{ y: -80, opacity: 0, scale: 0.8 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2)" }}, {start:.3f});')
        J(f'tl.to("#{m}k", {{ x: 72, duration: 0.3, ease: "back.out(2.5)" }}, {t_on:.3f});')
        J(f'tl.to("#{m}on", {{ opacity: 1, duration: 0.2 }}, {t_on:.3f});')
        J(f'tl.fromTo("#{m}i", {{ rotation: 0 }}, {{ keyframes: [{{ rotation: -50, duration: 0.15 }}, {{ rotation: 20, duration: 0.12 }}, {{ rotation: -35, duration: 0.15 }}, {{ rotation: 10, duration: 0.12 }}, {{ rotation: 0, duration: 0.15 }}], transformOrigin: "80% 80%" }}, {t_on + 0.1:.3f});')
        J(f'tl.fromTo("#{m}s", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {t_sub:.3f});')
        J(f'tl.to("#{m} .md", {{ y: -40, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4)
        self.sfx("click", t_on, 0.55)
        self.sfx("impact-bass-1", t_on + 0.2, 0.35)
        self.sfx("key-press", t_on + 0.35, 0.3)

    # -- 7. key message, kinetic: it's okay / ENJOY / proses / yang Tuhan susun
    def quote(self, start, end, t_ok, t_enjoy, t_proses, t_tuhan):
        q = self.uid("qt")
        letters = "".join(f'<span id="{q}e{i}" style="display:inline-block">{c}</span>' for i, c in enumerate("ENJOY"))
        self.layers.append(f'<section id="{q}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="qt-bg" id="{q}bg"></div><div class="qt"><div class="qt-s" id="{q}s">Tapi it\'s okay</div>'
                           f'<div class="qt-b">{letters}</div><div class="qt-m" id="{q}m">proses</div><div class="qt-u" id="{q}u"></div>'
                           f'<div class="qt-e" id="{q}t">yang <em>Tuhan</em> susun</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{q}bg", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5, ease: "power2.inOut" }}, {start:.3f});')
        J(f'tl.fromTo("#{q}s", {{ opacity: 0, filter: "blur(8px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.2 }}, {t_ok:.3f});')
        for i in range(5):
            J(f'tl.fromTo("#{q}e{i}", {{ y: 160, opacity: 0, scale: 0.4 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2.2)" }}, {t_enjoy + i * 0.06:.3f});')
        J(f'tl.fromTo("#{q}m", {{ opacity: 0, filter: "blur(10px)", scale: 1.3 }}, {{ opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.3, ease: "power3.out" }}, {t_proses:.3f});')
        J(f'tl.fromTo("#{q}u", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.5, ease: "expo.out" }}, {t_proses + 0.1:.3f});')
        J(f'tl.fromTo("#{q}t", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }}, {t_tuhan:.3f});')
        J(f'tl.to("#{q} .qt > *", {{ opacity: 0, filter: "blur(8px)", duration: 0.25, stagger: 0.04 }}, {end - 0.4:.3f});')
        J(f'tl.to("#{q}bg", {{ opacity: 0, duration: 0.35 }}, {end - 0.35:.3f});')
        self.sfx("whoosh-cinematic", t_enjoy - 0.25, 0.45)
        self.sfx("impact-bass-1", t_enjoy + 0.1, 0.5)
        self.sfx("whoosh-short", t_proses, 0.35)
        self.sfx("sparkle", t_tuhan, 0.45)

    # -- 8. cat name tag
    def nametag(self, start, end, title, sub):
        n = self.uid("nt")
        self.layers.append(f'<section id="{n}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="nt" id="{n}m"><span class="ico" id="{n}i" style="width:96px;height:96px;border-radius:50%;background:{Y};color:#15171a;padding:18px">{ICON["paw"]}</span>'
                           f'<div><b id="{n}b">{esc(title)}</b><span>{esc(sub)}</span></div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{n}m", {{ x: -900, rotation: -8 }}, {{ x: 0, rotation: -2, duration: 0.55, ease: "back.out(1.6)" }}, {start:.3f});')
        J(f'tl.fromTo("#{n}i", {{ scale: 0, rotation: -90 }}, {{ scale: 1, rotation: 0, duration: 0.4, ease: "back.out(3)" }}, {start + 0.25:.3f});')
        J(f'tl.to("#{n}m", {{ x: -900, duration: 0.3, ease: "power3.in" }}, {end - 0.3:.3f});')
        self.sfx("whoosh-short", start, 0.4)
        self.sfx("pop", start + 0.3, 0.45)

    # -- 9. teaser: journey baru, year reel rolls 2025 -> 2027
    def teaser(self, start, end, t_j, t_target, t_year):
        s = self.uid("ts")
        reel = "".join(f"<div>{y}</div>" for y in (2024, 2025, 2026, 2027))
        self.layers.append(f'<section id="{s}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="ts"><div class="ts-k" id="{s}k">{self.ico("lock")}Coming soon</div>'
                           f'<div class="ts-j" id="{s}j">Journey baru</div>'
                           f'<div class="ts-y" id="{s}y"><div class="ts-yl">Target</div><div class="ts-win"><div class="ts-reel" id="{s}r">{reel}</div></div></div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{s}k", {{ y: -60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, {start:.3f});')
        J(f'tl.fromTo("#{s}j", {{ opacity: 0, scaleX: 1.6, filter: "blur(10px)" }}, {{ opacity: 1, scaleX: 1, filter: "blur(0px)", duration: 0.6, ease: "expo.out" }}, {t_j:.3f});')
        J(f'tl.fromTo("#{s}y", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, {t_target:.3f});')
        J(f'tl.fromTo("#{s}r", {{ y: 0 }}, {{ y: -510, duration: {max(0.5, t_year - t_target):.3f}, ease: "power3.inOut" }}, {t_target + 0.05:.3f});')
        J(f'tl.fromTo("#{s} .ts-win", {{ scale: 1 }}, {{ scale: 1.12, duration: 0.12, yoyo: true, repeat: 1 }}, {t_year + 0.05:.3f});')
        J(f'tl.to("#{s} .ts", {{ y: -40, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4)
        self.sfx("sparkle", t_j, 0.4)
        self.sfx("typing", t_target, 0.25, dur=max(0.5, t_year - t_target))
        self.sfx("impact-bass-2", t_year + 0.05, 0.5)

    # -- 10. CTA: like / share / follow buttons get tapped, topics stack
    def cta(self, start, end, t_like, t_share, t_follow, topics):
        c = self.uid("ct")
        btns = [("heart", "Like", t_like, R), ("share", "Share", t_share, "#2f8cff"), ("plus", "Follow", t_follow, Y)]
        bh = "".join(f'<div class="ct-b" id="{c}b{i}" style="position:relative">{self.ico(ic)}<b>{lab}</b><div class="ct-r" id="{c}r{i}"></div></div>' for i, (ic, lab, t, col) in enumerate(btns))
        tp = "".join(f'<div id="{c}t{i}" class="{"w" if i % 2 else ""}">{esc(t)}</div>' for i, (t, _) in enumerate(topics))
        self.layers.append(f'<section id="{c}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="ct">{bh}</div><div class="tp">{tp}</div></section>')
        J = self.js.append
        for i, (ic, lab, t, col) in enumerate(btns):
            J(f'tl.fromTo("#{c}b{i}", {{ y: -120, opacity: 0, scale: 0.5 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2.2)" }}, {start + i * 0.08:.3f});')
            J(f'tl.to("#{c}b{i} .ico", {{ backgroundColor: "{col}", borderColor: "{col}", color: "{"#15171a" if col == Y else "#ffffff"}", scale: 1.18, duration: 0.15, ease: "power2.out" }}, {t:.3f});')
            J(f'tl.to("#{c}b{i} .ico", {{ scale: 1, duration: 0.3, ease: "back.out(3)" }}, {t + 0.15:.3f});')
            J(f'tl.fromTo("#{c}r{i}", {{ scale: 0.8, opacity: 1 }}, {{ scale: 1.8, opacity: 0, duration: 0.5, ease: "power2.out" }}, {t:.3f});')
            self.sfx("click", t, 0.5)
            self.sfx("pop", t + 0.05, 0.35)
        for i, (t, when) in enumerate(topics):
            J(f'tl.fromTo("#{c}t{i}", {{ x: {600 if i % 2 else -600}, opacity: 0, rotation: {6 if i % 2 else -6} }}, {{ x: 0, opacity: 1, rotation: 0, duration: 0.45, ease: "back.out(1.8)" }}, {when:.3f});')
            self.sfx("whoosh-short", when - 0.05, 0.35)
        J(f'tl.to(["#{c} .ct", "#{c} .tp"], {{ y: -40, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')

    # -- captions: dark backing, active word pops
    def captions_box(self, words, hot, hide=()):
        hot = {h.lower() for h in hot}
        words = [w for w in words if not any(a <= w[1] < b for a, b in hide)]
        groups, cur = [], []
        for w in words:
            if cur and (len(cur) >= 4 or sum(len(x[0]) + 1 for x in cur) + len(w[0]) > 24 or w[1] - cur[-1][2] > 0.45):
                groups.append(cur); cur = []
            cur.append(w)
        if cur:
            groups.append(cur)
        for gi, g in enumerate(groups):
            st = g[0][1]
            nxt = groups[gi + 1][0][1] if gi + 1 < len(groups) else g[-1][2] + 0.4
            en = min(nxt, g[-1][2] + 0.5)
            for a, b in hide:
                if st < a < en:
                    en = a
            if en - st < 0.15:
                continue
            cid = self.uid("cv")
            spans = "".join(f'<span class="w{" hot" if re.sub(r"[^\w-]", "", w[0]).lower() in hot else ""}" id="{cid}w{i}">{esc(w[0])}</span>' for i, w in enumerate(g))
            self.layers.append(f'<section id="{cid}" class="clip" data-start="{st:.3f}" data-duration="{en - st:.3f}" data-track-index="8"><div class="cv"><div class="cv-p">{spans}</div></div></section>')
            self.js.append(f'tl.fromTo("#{cid} .cv-p", {{ scale: 0.86, y: 16 }}, {{ scale: 1, y: 0, duration: 0.16, ease: "back.out(2)" }}, {st:.3f});')
            for i, w in enumerate(g):
                t = max(w[1], st)
                self.js.append(f'tl.fromTo("#{cid}w{i}", {{ opacity: 0.6, scale: 1 }}, {{ opacity: 1, scale: 1.08, duration: 0.08 }}, {t:.3f});')
                self.js.append(f'tl.to("#{cid}w{i}", {{ scale: 1, duration: 0.12 }}, {t + 0.08:.3f});')


def build():
    w = words()
    c = V("v2011-enjoy-proses", A + END)
    c.aroll(F + "cut.mp4", [(0.0, A, 0.0)])
    c.shade(0, A)

    T = lambda tok, after=0.0: at(w, tok, after)
    # camera: punch-ins on the words that carry the point; shake on the hiccup
    c.camera(punches=[(T("straight"), 0.9), (T("tauhid"), 1.2), (T("hiccup"), 1.1), (T("terjun"), 1.0),
                      (T("2027"), 1.0)],
             shakes=[T("hiccup")])
    for t in sorted(BIG):
        c.flash(t)

    c.hook(0.0, 3.0)
    c.road(9.05, 21.0, t_plan=T("bayangkan", 9), t_no=T("tak", 13.0), t_real=T("jalan", 16.5),
           turns=[T("serong"), T("kanan"), T("kiri")])
    c.foundation(T("track", 23) - 0.25, 36.0, t1=T("dalaman") - 0.2, t2=T("asas") - 0.4, t_ok=T("always"))
    c.route(T("loading") - 0.35, 43.0, t_box=T("loading"), t_go=T("hantar"), t_pin=T("selangor"))
    c.hiccup(T("rancang", 43) - 0.1, T("hiccup"), T("benda", 49), 51.4)
    c.tukang(T("terjun") - 0.3, T("tukang", 56), T("dah", 60.4), 62.3)
    c.quote(T("it's") - 0.25, 71.45, t_ok=T("it's") - 0.1, t_enjoy=T("enjoy", 66), t_proses=T("proses"), t_tuhan=T("tuhan", 69.5))
    c.nametag(T("jantan") - 0.4, 78.3, "Jantan", "kucing Bengal kami")
    c.teaser(T("share", 80) - 0.1, 89.0, t_j=T("journey"), t_target=T("target"), t_year=T("2027"))
    c.cta(90.0, 100.9, t_like=T("like"), t_share=T("share", 90.5), t_follow=T("follow"),
          topics=[("Renovation", T("renovation")), ("Business", T("business")), ("Kehidupan", T("kehidupan"))])

    # follow card over the last frame
    c.image(F + "last.jpg", A, END, zoom=(1.0, 1.06))
    c.end_card("bangfasz", 'Follow<em>for more</em>', "Renovation · Business · Life", "+ Follow bangfasz", A, END, logo=None)

    c.captions_box(w, HOT, hide=[(T("it's") - 0.25, 71.45), (75.3, 78.4), (A, A + END)])
    c.write(OUT, "20/11: Enjoy proses yang Tuhan susun (vlog loading barang)")


if __name__ == "__main__":
    build()
