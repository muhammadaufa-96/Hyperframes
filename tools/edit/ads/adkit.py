"""Ad-specific graphics on top of gen.Comp: question cards, step timeline,
blueprint intro, room route, flow lines, keyword captions, CTA button and end card."""
import json, re, sys
sys.path.insert(0, "/home/user/Hyperframes/raw/scripts")
import gen
from gen import Comp, esc

gen.CSS += r"""
/* Question cards that flip from ? to a tick */
.qg { position: absolute; left: 70px; right: 70px; top: 300px; display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.qc { background: rgba(15,17,20,0.88); border-radius: 20px; padding: 22px 22px; display: flex; align-items: center; gap: 18px; border: 3px solid rgba(255,255,255,0.14); }
.qc .ic { position: relative; width: 66px; height: 66px; flex: none; }
.qc .ic i { position: absolute; inset: 0; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-style: normal; font-weight: 800; font-size: 40px; color: #fff; }
.qc .ic .q { background: #ff4d4d; }
.qc .ic .k { background: #20b26b; opacity: 0; }
.qc b { font-weight: 800; font-size: 38px; text-transform: uppercase; white-space: nowrap; }

/* Four-step timeline */
.st { position: absolute; left: 60px; right: 60px; top: 300px; height: 190px; background: rgba(15,17,20,0.86); border-radius: 22px; }
.st-line { position: absolute; left: 120px; right: 120px; top: 60px; height: 6px; border-radius: 3px; background: rgba(255,255,255,0.2); }
.st-fill { position: absolute; left: 120px; right: 120px; top: 60px; height: 6px; border-radius: 3px; background: #f5c22e; transform-origin: left center; transform: scaleX(0); }
.st-row { position: absolute; inset: 0; display: grid; grid-template-columns: repeat(4, 1fr); }
.st-n { display: flex; flex-direction: column; align-items: center; padding-top: 30px; gap: 14px; }
.st-dot { width: 66px; height: 66px; border-radius: 50%; background: #2a2d33; border: 5px solid rgba(255,255,255,0.35); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 30px; }
.st-lab { font-weight: 800; font-size: 27px; text-transform: uppercase; color: rgba(255,255,255,0.55); white-space: nowrap; }

/* Blueprint intro */
.bp { position: absolute; inset: 0; background-color: #0c3560; background-image: linear-gradient(rgba(255,255,255,0.07) 2px, transparent 2px), linear-gradient(90deg, rgba(255,255,255,0.07) 2px, transparent 2px); background-size: 60px 60px; }
.bp svg { position: absolute; left: 220px; top: 440px; width: 640px; height: 896px; overflow: visible; }
.bp .w { fill: none; stroke: #e8f1ff; stroke-width: 10; stroke-linecap: square; stroke-dasharray: 1; stroke-dashoffset: 1; }
.bp .p { fill: none; stroke: #8fc3ff; stroke-width: 5; stroke-dasharray: 1; stroke-dashoffset: 1; }
.bp .t { font-family: "Share Tech Mono", monospace; font-size: 30px; fill: #bcd9ff; opacity: 0; }
.bp-k { position: absolute; left: 70px; top: 1720px; font-family: "Share Tech Mono", monospace; font-size: 34px; color: #bcd9ff; letter-spacing: 0.08em; opacity: 0; }
.wipe { position: absolute; top: 0; bottom: 0; width: 40px; left: -40px; background: #f5c22e; box-shadow: 0 0 40px rgba(245,194,46,0.8); }

/* Room route (layout tour) */
.rt { position: absolute; left: 50px; top: 290px; width: 430px; background: rgba(15,17,20,0.78); border-radius: 20px; padding: 18px 22px 20px; display: flex; flex-direction: column; gap: 6px; }
.rt-h { font-weight: 800; font-size: 26px; letter-spacing: 0.1em; color: #f5c22e; margin-bottom: 6px; }
.rt-i { display: flex; align-items: center; gap: 14px; font-weight: 600; font-size: 30px; color: rgba(255,255,255,0.5); transform-origin: left center; white-space: nowrap; }
.rt-i i { width: 18px; height: 18px; border-radius: 50%; background: rgba(255,255,255,0.35); flex: none; font-style: normal; }

/* Flow lines */
.fl svg { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }
.fl path { fill: none; stroke-width: 14; stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: 1; }
.fl .pa { stroke: #4fb3ff; }
.fl .sf { stroke: #f5c22e; }
.fl-leg { position: absolute; left: 70px; top: 300px; display: flex; flex-direction: column; gap: 14px; }
.fl-leg div { display: flex; align-items: center; gap: 14px; background: rgba(15,17,20,0.84); padding: 12px 22px; border-radius: 999px; font-weight: 800; font-size: 36px; text-transform: uppercase; }
.fl-leg span { width: 40px; height: 12px; border-radius: 6px; }

/* Keyword captions */
.capm .w.hot { color: #ffd34d; }

/* CTA button */
.btn { position: absolute; left: 90px; right: 90px; top: 1120px; display: flex; align-items: center; justify-content: center; gap: 16px; background: #f5c22e; color: #15171a; border-radius: 999px; padding: 26px 30px; font-weight: 800; font-size: 44px; text-transform: uppercase; box-shadow: 0 16px 40px rgba(0,0,0,0.45); white-space: nowrap; }

/* CTA end card */
.ce { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 34px; background: rgba(10,11,13,0.8); padding: 0 70px 200px; text-align: center; }
.ce-k { background: #20b26b; color: #fff; font-weight: 800; font-size: 40px; letter-spacing: 0.08em; padding: 10px 26px; border-radius: 8px; text-transform: uppercase; }
.ce-q { font-weight: 800; font-size: 100px; line-height: 1.02; text-transform: uppercase; }
.ce-q span { display: block; }
.ce-q em { display: block; font-style: normal; color: #f5c22e; }
.ce-b { background: #fff; color: #15171a; border-radius: 999px; padding: 22px 44px; font-weight: 800; font-size: 44px; text-transform: uppercase; }
.ce-l { width: 460px; margin-top: 10px; }
"""

LOGO = "../assets/brand/enoxin-logo-white.png"


class Ad(Comp):
    def write(self, path, title):
        """Footage first (A-roll, then b-roll in call order), every graphic above it."""
        media = [l for l in self.layers if l.startswith('<div class="cam"')]
        rest = [l for l in self.layers if not l.startswith('<div class="cam"')]
        self.layers = media + rest
        super().write(path, title)

    def qgrid(self, items, pops, flip_at, end, flip_step=0.35):
        g = self.uid("qg")
        cards = "".join(f'<div class="qc" id="{g}c{i}"><div class="ic"><i class="q" id="{g}q{i}">?</i><i class="k" id="{g}k{i}">✓</i></div><b>{esc(t)}</b></div>'
                        for i, t in enumerate(items))
        self.layers.append(f'<section id="{g}" class="clip" data-start="{pops[0]:.3f}" data-duration="{end - pops[0]:.3f}" data-track-index="6"><div class="qg">{cards}</div></section>')
        for i, t in enumerate(pops):
            self.js.append(f'tl.fromTo("#{g}c{i}", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.4)" }}, {t:.3f});')
            self.sfx("pop", t, 0.4)
        for i in range(len(items)):
            t = flip_at + i * flip_step
            self.js.append(f'tl.to("#{g}q{i}", {{ opacity: 0, duration: 0.12 }}, {t:.3f});')
            self.js.append(f'tl.fromTo("#{g}k{i}", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.25, ease: "back.out(3)" }}, {t:.3f});')
            self.js.append(f'tl.to("#{g}c{i}", {{ borderColor: "#20b26b", duration: 0.2 }}, {t:.3f});')
            self.sfx("ping", t, 0.35)
        self.js.append(f'tl.to("#{g} .qg", {{ opacity: 0, y: -30, duration: 0.25 }}, {end - 0.25:.3f});')

    def steps(self, labels, at, end):
        s = self.uid("st")
        nodes = "".join(f'<div class="st-n"><div class="st-dot" id="{s}d{i}">{i + 1}</div><div class="st-lab" id="{s}l{i}">{esc(t)}</div></div>' for i, t in enumerate(labels))
        start = at[0] - 0.3
        self.layers.append(f'<section id="{s}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="st" id="{s}b"><div class="st-line"></div><div class="st-fill" id="{s}f"></div><div class="st-row">{nodes}</div></div></section>')
        self.js.append(f'tl.fromTo("#{s}b", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {start:.3f});')
        n = len(labels)
        for i, t in enumerate(at):
            self.js.append(f'tl.to("#{s}d{i}", {{ backgroundColor: "#f5c22e", borderColor: "#f5c22e", color: "#15171a", duration: 0.15 }}, {t:.3f});')
            self.js.append(f'tl.fromTo("#{s}d{i}", {{ scale: 1.35 }}, {{ scale: 1, duration: 0.3, ease: "back.out(2)" }}, {t:.3f});')
            self.js.append(f'tl.to("#{s}l{i}", {{ color: "#ffffff", duration: 0.15 }}, {t:.3f});')
            if i:
                self.js.append(f'tl.to("#{s}f", {{ scaleX: {i / (n - 1):.3f}, duration: 0.3, ease: "power2.out" }}, {t - 0.2:.3f});')
            self.sfx("ping", t, 0.3)
        self.js.append(f'tl.to("#{s}b", {{ opacity: 0, duration: 0.25 }}, {end - 0.25:.3f});')

    def blueprint(self, start, wipe_at, kicker="DULU · RUANG KOSONG"):
        """Empty shell draws in, interior walls get planned, then a yellow wipe reveals the footage."""
        b = self.uid("bp")
        walls = ["M0 0 H800 V1120 H0 Z"]
        plan = ["M0 300 H330 V0", "M470 0 V300 H800", "M0 640 H300 V420", "M500 420 V640 H800", "M0 900 H260", "M540 900 H800 V1120",
                "M330 300 V360", "M470 300 V360"]
        texts = [(40, 160, "SURGERY 1"), (520, 160, "SURGERY 2"), (40, 540, "X-RAY"), (540, 540, "STERILISE"), (300, 800, "WAITING"),
                 (40, 1020, "KAUNTER"), (580, 1020, "TOILET")]
        svg = ('<svg viewBox="0 0 800 1120">' + "".join(f'<path class="w" pathLength="1" d="{d}"></path>' for d in walls)
               + "".join(f'<path class="p" pathLength="1" id="{b}p{i}" d="{d}"></path>' for i, d in enumerate(plan))
               + "".join(f'<text class="t" id="{b}t{i}" x="{x}" y="{y}">{esc(s)}</text>' for i, (x, y, s) in enumerate(texts)) + "</svg>")
        dur = wipe_at + 0.6 - start
        self.layers.append(f'<section id="{b}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="4">'
                           f'<div class="bp" id="{b}m">{svg}<div class="bp-k" id="{b}k">{esc(kicker)}</div></div><div class="wipe" id="{b}x"></div></section>')
        self.js.append(f'tl.to("#{b} .w", {{ strokeDashoffset: 0, duration: 0.9, ease: "power2.inOut" }}, {start + 0.1:.3f});')
        self.js.append(f'tl.to("#{b}k", {{ opacity: 1, duration: 0.3 }}, {start + 0.4:.3f});')
        span = max(0.6, wipe_at - start - 1.4)
        for i in range(len(plan)):
            self.js.append(f'tl.to("#{b}p{i}", {{ strokeDashoffset: 0, duration: 0.35, ease: "power1.out" }}, {start + 1.0 + i * span / len(plan):.3f});')
        for i in range(len(texts)):
            self.js.append(f'tl.to("#{b}t{i}", {{ opacity: 1, duration: 0.2 }}, {start + 1.2 + i * span / len(texts):.3f});')
        self.js.append(f'tl.fromTo("#{b}m", {{ clipPath: "inset(0% 0% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 100%)", duration: 0.55, ease: "power2.inOut" }}, {wipe_at:.3f});')
        self.js.append(f'tl.fromTo("#{b}x", {{ x: 0 }}, {{ x: 1120, duration: 0.55, ease: "power2.inOut" }}, {wipe_at:.3f});')
        self.sfx("typing", start + 1.0, 0.25, dur=min(2.0, span))
        self.sfx("whoosh", wipe_at, 0.5)

    def route(self, rooms, start, end, title="LAYOUT KLINIK"):
        """rooms: [(name, t)] lights up the room being shown."""
        r = self.uid("rt")
        items = "".join(f'<div class="rt-i" id="{r}i{i}"><i id="{r}o{i}"></i>{esc(n)}</div>' for i, (n, _) in enumerate(rooms))
        self.layers.append(f'<section id="{r}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="rt" id="{r}b"><div class="rt-h">{esc(title)}</div>{items}</div></section>')
        self.js.append(f'tl.fromTo("#{r}b", {{ x: -500 }}, {{ x: 0, duration: 0.4, ease: "power3.out" }}, {start:.3f});')
        for i, (_, t) in enumerate(rooms):
            self.js.append(f'tl.to("#{r}i{i}", {{ color: "#ffd34d", scale: 1.08, duration: 0.18 }}, {t:.3f});')
            self.js.append(f'tl.to("#{r}o{i}", {{ backgroundColor: "#ffd34d", scale: 1.3, duration: 0.18 }}, {t:.3f});')
            if i + 1 < len(rooms):
                nxt = rooms[i + 1][1]
                self.js.append(f'tl.to("#{r}i{i}", {{ color: "rgba(255,255,255,0.85)", scale: 1, duration: 0.18 }}, {nxt:.3f});')
                self.js.append(f'tl.to("#{r}o{i}", {{ backgroundColor: "#20b26b", scale: 1, duration: 0.18 }}, {nxt:.3f});')
            self.sfx("click-soft", t, 0.35)
        self.js.append(f'tl.to("#{r}b", {{ x: -500, duration: 0.3, ease: "power2.in" }}, {end - 0.3:.3f});')

    def flow(self, start, dur, patient_at, staff_at):
        f = self.uid("fl")
        self.layers.append(f'<section id="{f}" class="clip fl" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<svg viewBox="0 0 1080 1920"><path class="pa" pathLength="1" id="{f}a" d="M120 1250 C 300 1000, 420 900, 560 820 S 820 700, 900 560"></path>'
                           f'<path class="sf" pathLength="1" id="{f}s" d="M200 1500 C 480 1420, 700 1300, 960 1000"></path></svg>'
                           f'<div class="fl-leg"><div id="{f}la"><span style="background:#4fb3ff"></span>Pesakit selesa</div>'
                           f'<div id="{f}ls"><span style="background:#f5c22e"></span>Staf tak berlaga</div></div></section>')
        self.js.append(f'tl.fromTo("#{f}la", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3 }}, {patient_at:.3f});')
        self.js.append(f'tl.to("#{f}a", {{ strokeDashoffset: 0, duration: 1.0, ease: "power2.inOut" }}, {patient_at:.3f});')
        self.js.append(f'tl.fromTo("#{f}ls", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3 }}, {staff_at:.3f});')
        self.js.append(f'tl.to("#{f}s", {{ strokeDashoffset: 0, duration: 1.0, ease: "power2.inOut" }}, {staff_at:.3f});')
        self.js.append(f'tl.to("#{f} > *", {{ opacity: 0, duration: 0.25 }}, {start + dur - 0.25:.3f});')
        self.sfx("whoosh-short", patient_at, 0.35)
        self.sfx("whoosh-short", staff_at, 0.35)

    def button(self, text, start, dur, top=1120, pulses=3):
        b = self.uid("bt")
        self.layers.append(f'<section id="{b}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="btn" id="{b}b" style="top:{top}px">{esc(text)}</div></section>')
        self.js.append(f'tl.fromTo("#{b}b", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2.2)" }}, {start:.3f});')
        self.js.append(f'tl.to("#{b}b", {{ scale: 1.06, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: {pulses * 2 - 1} }}, {start + 0.5:.3f});')
        self.js.append(f'tl.to("#{b}b", {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')
        self.sfx("click", start, 0.45)

    def cta_end(self, start, dur, logo=LOGO):
        e = self.uid("ce")
        self.layers.append(f'<section id="{e}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="ce" id="{e}m"><div class="ce-k" id="{e}k">Percuma</div>'
                           f'<div class="ce-q" id="{e}q"><span>Dapatkan</span><em>Free CKAPS</em><span>Initial</span><span>Assessment</span></div>'
                           f'<div class="ce-b" id="{e}b">👇 Klik link di bawah</div><img class="ce-l" id="{e}l" src="{logo}" alt="Enoxin"></div></section>')
        self.js.append(f'tl.fromTo("#{e}m", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{e}k", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.5)" }}, {start + 0.1:.3f});')
        self.js.append(f'tl.fromTo("#{e}q span, #{e}q em", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, stagger: 0.08, ease: "back.out(1.8)" }}, {start + 0.2:.3f});')
        self.js.append(f'tl.fromTo("#{e}b", {{ scale: 0.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {start + 0.7:.3f});')
        self.js.append(f'tl.to("#{e}b", {{ scale: 1.06, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: {max(1, int((dur - 1.4) / 0.6)) * 2 - 1} }}, {start + 1.1:.3f});')
        self.js.append(f'tl.fromTo("#{e}l", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4 }}, {start + 0.9:.3f});')
        self.sfx("chime", start + 0.1, 0.4)

    def captions_hot(self, words, hot=(), hide=()):
        """Minimal one-line white captions; words whose lowercase core is in `hot` turn yellow."""
        hot = {h.lower() for h in hot}
        words = [w for w in words if not any(a <= w[1] < b for a, b in hide)]
        groups, cur = [], []
        for w in words:
            if cur and (len(cur) >= 5 or sum(len(x[0]) + 1 for x in cur) + len(w[0]) > 26 or w[1] - cur[-1][2] > 0.45):
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
            cid = self.uid("cm")
            spans = "".join(f'<span class="w{" hot" if re.sub(r"[^\w-]", "", w[0]).lower() in hot else ""}" id="{cid}w{i}">{esc(w[0])}</span>' for i, w in enumerate(g))
            self.layers.append(f'<section id="{cid}" class="clip" data-start="{st:.3f}" data-duration="{en - st:.3f}" data-track-index="8"><div class="capm me">{spans}</div></section>')
            self.js.append(f'tl.fromTo("#{cid} .capm", {{ y: 10, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.12 }}, {st:.3f});')
            for i, w in enumerate(g):
                self.js.append(f'tl.fromTo("#{cid}w{i}", {{ opacity: 0.72 }}, {{ opacity: 1, duration: 0.05 }}, {max(w[1], st):.3f});')


# ---- transcript clean-up --------------------------------------------------
ADS_FIX = {"tersangkau": "tersangkut", "setakkan": "setupkan", "setak": "setup", "konsep": "konsult", "konsert": "konsult",
           "kepung": "Kepong", "pucong": "Kepong", "segeri": "surgery", "sejerian": "surgery", "wangan": "ruangan",
           "pesen": "pesakit", "atau": "atur", "short": "shop", "lot": "lot"}
ADS_DROP = {"casting", "eh", "oh", "hmm"}


def load_words(path, clip):
    raw = json.load(open(path))
    out = []
    for i, w in enumerate(raw):
        core = re.sub(r"[^\w\-']", "", w["text"]).lower()
        if core in ADS_DROP:
            continue
        nxt = re.sub(r"[^\w]", "", raw[i + 1]["text"]).lower() if i + 1 < len(raw) else ""
        prv = re.sub(r"[^\w]", "", raw[i - 1]["text"]).lower() if i else ""
        punct = re.search(r"[.,!?]+$", w["text"])
        p = punct.group(0) if punct else ""
        if core == "sikit":
            t = "CKAPS" if nxt == "initial" else "Site"
        elif core == "atau" and prv != "susun":
            t = re.sub(r"[.,!?]+$", "", w["text"])
        elif core == "short" and nxt.startswith("lot"):
            t = "shoplot"
        elif core == "lot" and prv == "short":
            continue
        elif core in ADS_FIX:
            t = ADS_FIX[core]
        else:
            t = re.sub(r"[.,!?]+$", "", w["text"])
        out.append([t + ("?" if p.startswith("?") else ""), w["start"], w["end"]])
    return out


# ---- caption text: hand-corrected script aligned to per-piece ASR word times ----
from difflib import SequenceMatcher


def _n(s):
    return re.sub(r"[^\w]", "", s.lower())


def align(asr, script, spans):
    """asr: [[text, t0, t1, tag]] from chk.py; script: {tag: "corrected text"}; spans: {tag: (a, b)}.
    Returns [[text, t0, t1]] using the corrected words with the ASR timing."""
    out = []
    for tag, text in script.items():
        a0, a1 = spans[tag]
        A = [w for w in asr if w[3] == tag]
        T = text.split()
        tm = [None] * len(T)
        sm = SequenceMatcher(None, [_n(w[0]) for w in A], [_n(t) for t in T], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal" or (op == "replace" and i2 - i1 == j2 - j1):
                for k in range(j2 - j1):
                    tm[j1 + k] = [A[i1 + k][1], A[i1 + k][2]]
            elif op == "replace":
                s0, s1 = A[i1][1], A[i2 - 1][2]
                tot = sum(len(t) for t in T[j1:j2]); acc = 0
                for k in range(j1, j2):
                    x0 = s0 + (s1 - s0) * acc / tot; acc += len(T[k])
                    tm[k] = [x0, s0 + (s1 - s0) * acc / tot]
        # fill gaps (inserted words) between neighbours
        i = 0
        while i < len(T):
            if tm[i] is None:
                j = i
                while j < len(T) and tm[j] is None:
                    j += 1
                lo = tm[i - 1][1] if i else a0
                hi = tm[j][0] if j < len(T) else min(a1, lo + 0.35 * (j - i))
                if hi <= lo:
                    hi = lo + 0.2 * (j - i)
                tot = sum(len(t) for t in T[i:j]); acc = 0
                for k in range(i, j):
                    x0 = lo + (hi - lo) * acc / tot; acc += len(T[k])
                    tm[k] = [x0, lo + (hi - lo) * acc / tot]
                i = j
            else:
                i += 1
        prev = a0
        for t, (x0, x1) in zip(T, tm):
            x0 = min(max(x0, prev, a0), a1 - 0.05)
            x1 = min(max(x1, x0 + 0.08), a1)
            out.append([re.sub(r"[.,!]+$", "", t), round(x0, 3), round(x1, 3)])
            prev = x0
    out.sort(key=lambda w: w[1])
    return out
