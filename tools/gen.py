"""Build a 1080x1920 HyperFrames composition from a Python plan.

Used by build_v1.py / build_v2.py / build_v3.py. Writes compositions/<id>.html.
All media paths are relative to compositions/.
"""
import html as _html
import json

CSS = r"""
@font-face { font-family: "Montserrat"; font-weight: 800; src: url("../assets/fonts/montserrat-latin-800-normal.woff2") format("woff2"); }
@font-face { font-family: "Montserrat"; font-weight: 600; src: url("../assets/fonts/montserrat-latin-600-normal.woff2") format("woff2"); }
@font-face { font-family: "Share Tech Mono"; font-weight: 400; src: url("../assets/fonts/share-tech-mono-latin-400-normal.woff2") format("woff2"); }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { margin: 0; overflow: hidden; background: #0d0f12; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "Montserrat", sans-serif; color: #fff; background: #0d0f12; }
.clip { position: absolute; inset: 0; }
.cam { position: absolute; inset: 0; transform-origin: 50% 40%; }
.cam video, .cam img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0) 28%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.45) 100%); }

/* Hook title (top safe area) */
.hook { position: absolute; left: 70px; right: 70px; top: 250px; display: flex; flex-direction: column; align-items: flex-start; gap: 14px; }
.hook-line { display: block; background: #f5c22e; color: #15171a; font-weight: 800; font-size: 72px; line-height: 1.02; text-transform: uppercase; white-space: nowrap; padding: 10px 22px 12px; border-radius: 8px; }
.hook-line.alt { background: #ffffff; }

/* Kicker / info chips */
.chip { position: absolute; display: flex; align-items: center; gap: 12px; background: rgba(15,17,20,0.82); color: #fff; font-weight: 800; font-size: 46px; text-transform: uppercase; padding: 14px 26px; border-radius: 999px; border: 3px solid #f5c22e; }
.chip.yellow { background: #f5c22e; color: #15171a; border-color: #f5c22e; }

/* Numbered checklist card */
.card { position: absolute; left: 70px; right: 70px; top: 300px; display: flex; align-items: center; gap: 26px; background: rgba(15,17,20,0.86); border-radius: 22px; padding: 26px 30px; border-left: 14px solid #f5c22e; }
.card-num { flex: none; width: 120px; height: 120px; border-radius: 50%; background: #f5c22e; color: #15171a; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 76px; }
.card-text { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.card-title { font-weight: 800; font-size: 70px; line-height: 1; text-transform: uppercase; }
.card-sub { font-weight: 600; font-size: 38px; line-height: 1.2; color: #d9dadc; }

/* Captions */
.cap { position: absolute; left: 60px; right: 60px; top: 1240px; text-align: center; font-weight: 800; font-size: 74px; line-height: 1.12; text-transform: uppercase; }
.cap .w { display: inline-block; margin: 0 10px; color: #fff; text-shadow: 0 5px 0 rgba(0,0,0,0.6), 0 0 26px rgba(0,0,0,0.75); }

/* Minimal captions (two speakers) */
.capm { position: absolute; left: 90px; right: 90px; top: 1330px; text-align: center; font-weight: 600; font-size: 44px; line-height: 1.25; }
.capm .w { display: inline-block; margin: 0 6px; opacity: 0.72; text-shadow: 0 2px 10px rgba(0,0,0,0.85), 0 1px 2px rgba(0,0,0,0.9); }
.capm.me .w { color: #ffffff; }
.capm.cl .w { color: #ffd34d; }
.name { position: absolute; left: 70px; top: 1190px; display: flex; flex-direction: column; gap: 2px; background: rgba(15,17,20,0.78); border-left: 6px solid #ffd34d; padding: 12px 20px; border-radius: 8px; }
.name b { font-weight: 800; font-size: 38px; }
.name span { font-weight: 600; font-size: 28px; color: #d9dadc; }
.label { position: absolute; left: 70px; top: 300px; font-weight: 600; font-size: 36px; letter-spacing: 0.08em; text-transform: uppercase; color: #fff; padding: 10px 18px; background: rgba(15,17,20,0.55); border-radius: 6px; }
.shot { position: absolute; left: 140px; right: 140px; top: 260px; border-radius: 26px; overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,0.6); }
.shot img { display: block; width: 100%; }
.hl { position: absolute; border: 6px solid #ffd34d; border-radius: 14px; box-shadow: 0 0 0 9999px rgba(0,0,0,0); }

/* Comparison */
.vs { position: absolute; left: 60px; right: 60px; top: 300px; display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
.vs-box { background: rgba(15,17,20,0.86); border-radius: 22px; padding: 26px 22px; display: flex; flex-direction: column; gap: 8px; align-items: center; text-align: center; border-top: 12px solid #f5c22e; }
.vs-box b { font-size: 54px; font-weight: 800; line-height: 1.02; text-transform: uppercase; }
.vs-box span { font-size: 34px; font-weight: 600; color: #d9dadc; }

/* Strike words (Gucci / LV) */
.strike { position: absolute; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 120px; text-transform: uppercase; color: #fff; }
.strike i { position: absolute; left: -10%; right: -10%; top: 50%; height: 16px; margin-top: -8px; background: #ff3b3b; border-radius: 8px; transform-origin: left center; }

/* End card */
.end { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 40px; background: rgba(10,11,13,0.72); padding: 0 80px; text-align: center; }
.end-q { font-weight: 800; font-size: 96px; line-height: 1.05; text-transform: uppercase; }
.end-q em { font-style: normal; color: #f5c22e; }
.end-q .ln { display: block; }
.end-sub { font-weight: 600; font-size: 46px; color: #e7e7e7; }
.end-logo { width: 560px; }

/* Arrow label (site callouts) */
.tag { position: absolute; display: flex; align-items: center; gap: 14px; background: #ffffff; color: #15171a; font-weight: 800; font-size: 50px; text-transform: uppercase; padding: 14px 26px; border-radius: 14px; box-shadow: 0 12px 30px rgba(0,0,0,0.45); }
.tag .ic { width: 58px; height: 58px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 36px; color: #fff; background: #20b26b; }
.tag .ic.warn { background: #ff8a00; }

/* Laser block */
.lz-bgwrap { position: absolute; inset: -60px; filter: blur(16px) brightness(0.42) saturate(1.1); }
.lz-bgwrap video { width: 100%; height: 100%; object-fit: cover; }
.lz-title { position: absolute; left: 80px; right: 80px; top: 300px; display: flex; flex-direction: column; gap: 18px; }
.lz-kicker { align-self: flex-start; background: #f5c22e; color: #15171a; font-weight: 800; font-size: 40px; letter-spacing: 0.04em; padding: 10px 20px; border-radius: 6px; }
.lz-main { font-weight: 800; font-size: 104px; line-height: 0.98; text-transform: uppercase; }
.lz-wall { position: absolute; top: 760px; height: 560px; right: 0; width: 110px; background: linear-gradient(90deg, #8a8d91, #b9bcc0 40%, #9a9da1); }
.lz-device { position: absolute; left: 70px; top: 950px; width: 400px; height: 190px; border-radius: 34px; background: linear-gradient(180deg, #2c5fa8 0%, #1d4380 100%); box-shadow: 0 30px 60px rgba(0,0,0,0.55), inset 0 2px 0 rgba(255,255,255,0.25); }
.lz-grip { position: absolute; left: 0; top: 0; bottom: 0; width: 120px; border-radius: 34px 0 0 34px; background: #17191d; }
.lz-screen { position: absolute; left: 140px; top: 34px; width: 200px; height: 122px; border-radius: 12px; background: #0f1a12; display: flex; flex-direction: column; align-items: flex-end; justify-content: center; padding: 0 16px; font-family: "Share Tech Mono", monospace; color: #9dff9a; }
.lz-glow { position: absolute; inset: 0; border-radius: 12px; background: rgba(157,255,154,0.18); }
.lz-read { font-size: 52px; line-height: 1; position: relative; }
.lz-unit { font-size: 24px; opacity: 0.8; position: relative; }
.lz-emit { position: absolute; right: -10px; top: 70px; width: 26px; height: 50px; border-radius: 8px; background: #111; }
.lz-beam { position: absolute; left: 486px; top: 1043px; width: 484px; height: 6px; background: #ff3b3b; box-shadow: 0 0 18px 4px rgba(255,40,40,0.55); transform-origin: left center; border-radius: 3px; }
.lz-dot { position: absolute; left: 948px; top: 1024px; width: 44px; height: 44px; border-radius: 50%; background: radial-gradient(circle, #fff 0 18%, #ff3b3b 30%, rgba(255,40,40,0) 70%); }
.lz-dim { position: absolute; left: 486px; width: 484px; top: 1190px; height: 40px; }
.lz-dline { position: absolute; left: 0; right: 0; top: 19px; height: 3px; background: #f5c22e; transform-origin: left center; }
.lz-cap { position: absolute; top: 0; width: 3px; height: 40px; background: #f5c22e; }
.lz-dlabel { position: absolute; left: 0; right: 0; top: 54px; text-align: center; font-family: "Share Tech Mono", monospace; font-size: 46px; color: #f5c22e; }
.lz-badge { position: absolute; left: 70px; top: 1330px; display: flex; align-items: center; gap: 16px; background: #fff; color: #15171a; border-radius: 999px; padding: 16px 30px 16px 18px; font-weight: 800; font-size: 40px; }
.lz-check { width: 54px; height: 54px; border-radius: 50%; background: #20b26b; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 34px; }
"""


def esc(s):
    return _html.escape(s, quote=True)


class Comp:
    def __init__(self, cid, duration):
        self.cid = cid
        self.duration = duration
        self.layers = []   # markup in z-order
        self.js = []
        self.n = 0

    def uid(self, p):
        self.n += 1
        return f"{p}{self.n}"

    # ---- media -----------------------------------------------------------
    def aroll(self, src, placements, cuts_scale=None, track=0):
        """placements: list of (start, dur, media_start). One cam wrapper for all."""
        vids = []
        for st, d, ms in placements:
            vid = self.uid("ar")
            vids.append(f'<video id="{vid}" class="clip" src="{src}" playsinline data-has-audio="true" '
                        f'data-start="{st:.3f}" data-duration="{d:.3f}" data-media-start="{ms:.3f}" '
                        f'data-track-index="{track}" data-volume="1"></video>')
        self.layers.append('<div class="cam" id="acam">' + "".join(vids) + '</div>')
        for t, s in (cuts_scale or []):
            self.js.append(f'tl.set("#acam", {{ scale: {s} }}, {t:.3f});')

    def broll(self, src, start, dur, media_start=0.0, zoom=(1.0, 1.08), track=1, origin="50% 50%"):
        w = self.uid("bw"); v = self.uid("bv")
        self.layers.append(f'<div class="cam" id="{w}" style="transform-origin:{origin}">'
                           f'<video id="{v}" class="clip" src="{src}" muted playsinline '
                           f'data-start="{start:.3f}" data-duration="{dur:.3f}" data-media-start="{media_start:.3f}" '
                           f'data-track-index="{track}"></video></div>')
        self.js.append(f'tl.fromTo("#{w}", {{ scale: {zoom[0]} }}, {{ scale: {zoom[1]}, duration: {dur:.3f}, ease: "none" }}, {start:.3f});')
        return w

    def image(self, src, start, dur, zoom=(1.0, 1.12), track=1, origin="50% 50%", fit="cover", bg=None):
        w = self.uid("iw"); i = self.uid("im")
        style = f"object-fit:{fit};" + (f"background:{bg};" if bg else "")
        self.layers.append(f'<div class="cam" id="{w}" style="transform-origin:{origin}">'
                           f'<img id="{i}" class="clip" src="{src}" style="{style}" alt="" '
                           f'data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="{track}"></div>')
        self.js.append(f'tl.fromTo("#{w}", {{ scale: {zoom[0]} }}, {{ scale: {zoom[1]}, duration: {dur:.3f}, ease: "none" }}, {start:.3f});')

    def sfx(self, name, t, vol=0.6, dur=None):
        a = self.uid("sfx")
        d = f' data-duration="{dur:.3f}"' if dur else ""
        self.layers.append(f'<audio id="{a}" src="../assets/sfx/{name}.mp3" data-start="{t:.3f}"{d} data-track-index="9" data-volume="{vol}"></audio>')

    def shade(self, start, dur):
        s = self.uid("sh")
        self.layers.append(f'<div id="{s}" class="clip shade" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="2"></div>')

    # ---- graphics --------------------------------------------------------
    def hook(self, lines, start, dur, sfx=True):
        sid = self.uid("hk")
        spans = "".join(f'<span class="hook-line{" alt" if i % 2 else ""}" id="{sid}l{i}" style="font-size:{72 if len(l) <= 19 else 60}px">{esc(l)}</span>' for i, l in enumerate(lines))
        self.layers.append(f'<section id="{sid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="5"><div class="hook">{spans}</div></section>')
        for i in range(len(lines)):
            self.js.append(f'tl.fromTo("#{sid}l{i}", {{ x: -80, opacity: 0, rotation: -3 }}, {{ x: 0, opacity: 1, rotation: 0, duration: 0.35, ease: "back.out(2)" }}, {start + 0.05 + i * 0.12:.3f});')
            self.js.append(f'tl.to("#{sid}l{i}", {{ x: 60, opacity: 0, duration: 0.25, ease: "power2.in" }}, {start + dur - 0.3:.3f});')
        if sfx:
            self.sfx("whoosh", start, 0.5)
            self.sfx("impact-bass-1", start + 0.12, 0.45)

    def chip(self, text, start, dur, x=70, y=300, yellow=False, sfx="pop"):
        cid = self.uid("ch")
        cls = "chip yellow" if yellow else "chip"
        self.layers.append(f'<section id="{cid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="{cls}" id="{cid}b" style="left:{x}px;top:{y}px">{esc(text)}</div></section>')
        self.js.append(f'tl.fromTo("#{cid}b", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.5)" }}, {start:.3f});')
        self.js.append(f'tl.to("#{cid}b", {{ scale: 0.8, opacity: 0, duration: 0.2, ease: "power2.in" }}, {start + dur - 0.22:.3f});')
        if sfx:
            self.sfx(sfx, start, 0.45)

    def tag(self, text, start, dur, x, y, icon="✓", warn=False):
        tid = self.uid("tg")
        ic = f'<span class="ic{" warn" if warn else ""}">{esc(icon)}</span>'
        self.layers.append(f'<section id="{tid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="tag" id="{tid}b" style="left:{x}px;top:{y}px">{ic}{esc(text)}</div></section>')
        self.js.append(f'tl.fromTo("#{tid}b", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {start:.3f});')
        self.js.append(f'tl.to("#{tid}b", {{ y: -20, opacity: 0, duration: 0.2 }}, {start + dur - 0.22:.3f});')
        self.sfx("ping", start, 0.4)

    def card(self, num, title, sub, start, dur, top=300):
        cid = self.uid("cd")
        self.layers.append(f'<section id="{cid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="card" id="{cid}b" style="top:{top}px"><div class="card-num">{esc(num)}</div>'
                           f'<div class="card-text"><div class="card-title">{esc(title)}</div><div class="card-sub">{esc(sub)}</div></div></div></section>')
        self.js.append(f'tl.fromTo("#{cid}b", {{ x: -1100 }}, {{ x: 0, duration: 0.4, ease: "power3.out" }}, {start:.3f});')
        self.js.append(f'tl.to("#{cid}b", {{ x: 1100, duration: 0.3, ease: "power2.in" }}, {start + dur - 0.3:.3f});')
        self.sfx("whoosh-short", start, 0.5)

    def strike(self, text, start, dur, strike_at, x=0, y=520, w=1080):
        sid = self.uid("st")
        self.layers.append(f'<section id="{sid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="strike" id="{sid}b" style="left:{x}px;top:{y}px;width:{w}px"><span style="position:relative">{esc(text)}<i id="{sid}i"></i></span></div></section>')
        self.js.append(f'tl.fromTo("#{sid}b", {{ scale: 1.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "power3.out" }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{sid}i", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.18, ease: "power2.out" }}, {strike_at:.3f});')
        self.js.append(f'tl.to("#{sid}b", {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')
        self.sfx("pop", start, 0.4)
        self.sfx("error", strike_at, 0.35)

    def vs(self, left, right, start, dur):
        vid = self.uid("vs")
        box = lambda i, b, s: f'<div class="vs-box" id="{vid}{i}"><b>{esc(b)}</b><span>{esc(s)}</span></div>'
        self.layers.append(f'<section id="{vid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="vs">{box("a", *left)}{box("b", *right)}</div></section>')
        self.js.append(f'tl.fromTo("#{vid}a", {{ y: -60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{vid}b", {{ y: -60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {start + 0.2:.3f});')
        self.js.append(f'tl.to(["#{vid}a", "#{vid}b"], {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')
        self.sfx("whoosh-short", start, 0.45)

    def endcard(self, start, dur, q_html, sub, logo=None):
        eid = self.uid("en")
        logo_html = f'<img class="end-logo" id="{eid}l" src="{logo}" alt="Enoxin">' if logo else ""
        self.layers.append(f'<section id="{eid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="end" id="{eid}b"><div class="end-q" id="{eid}q">{q_html}</div>'
                           f'<div class="end-sub" id="{eid}s">{esc(sub)}</div>{logo_html}</div></section>')
        self.js.append(f'tl.fromTo("#{eid}b", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{eid}q", {{ y: 60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.45, ease: "back.out(1.8)" }}, {start + 0.1:.3f});')
        self.js.append(f'tl.fromTo("#{eid}s", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35 }}, {start + 0.45:.3f});')
        if logo:
            self.js.append(f'tl.fromTo("#{eid}l", {{ scale: 0.8, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start + 0.7:.3f});')
        self.sfx("chime", start + 0.1, 0.4)

    def captions(self, words, hide=()):
        """words: [(text, start, end)] in composition time. hide: [(a,b)] windows without captions."""
        def hidden(t):
            return any(a <= t < b for a, b in hide)
        words = [w for w in words if not hidden(w[1])]
        groups, cur = [], []
        for w in words:
            if cur and (len(cur) >= 3 or sum(len(x[0]) for x in cur) + len(w[0]) > 16 or w[1] - cur[-1][2] > 0.35):
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
            cid = self.uid("cp")
            spans = "".join(f'<span class="w" id="{cid}w{i}">{esc(w[0])}</span>' for i, w in enumerate(g))
            self.layers.append(f'<section id="{cid}" class="clip" data-start="{st:.3f}" data-duration="{en - st:.3f}" data-track-index="8"><div class="cap">{spans}</div></section>')
            self.js.append(f'tl.fromTo("#{cid} .cap", {{ scale: 0.85, y: 20 }}, {{ scale: 1, y: 0, duration: 0.14, ease: "back.out(2)" }}, {st:.3f});')
            for i, w in enumerate(g):
                self.js.append(f'tl.fromTo("#{cid}w{i}", {{ color: "#ffffff" }}, {{ color: "#f5c22e", duration: 0.04 }}, {max(w[1], st):.3f});')
                if i + 1 < len(g):
                    self.js.append(f'tl.to("#{cid}w{i}", {{ color: "#ffffff", duration: 0.04 }}, {g[i + 1][1]:.3f});')

    def captions_min(self, words, hide=()):
        """words: [(text, start, end, speaker)] speaker in {"me","cl"}; minimal one-line captions."""
        words = [w for w in words if not any(a <= w[1] < b for a, b in hide)]
        groups, cur = [], []
        for w in words:
            if cur and (cur[-1][3] != w[3] or len(cur) >= 5 or sum(len(x[0]) + 1 for x in cur) + len(w[0]) > 26 or w[1] - cur[-1][2] > 0.45):
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
            spans = "".join(f'<span class="w" id="{cid}w{i}">{esc(w[0])}</span>' for i, w in enumerate(g))
            self.layers.append(f'<section id="{cid}" class="clip" data-start="{st:.3f}" data-duration="{en - st:.3f}" data-track-index="8"><div class="capm {g[0][3]}">{spans}</div></section>')
            self.js.append(f'tl.fromTo("#{cid} .capm", {{ y: 10, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.12 }}, {st:.3f});')
            for i, w in enumerate(g):
                self.js.append(f'tl.fromTo("#{cid}w{i}", {{ opacity: 0.72 }}, {{ opacity: 1, duration: 0.05 }}, {max(w[1], st):.3f});')

    def name(self, title, sub, start, dur):
        nid = self.uid("nm")
        self.layers.append(f'<section id="{nid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="name" id="{nid}b"><b>{esc(title)}</b><span>{esc(sub)}</span></div></section>')
        self.js.append(f'tl.fromTo("#{nid}b", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {start:.3f});')
        self.js.append(f'tl.to("#{nid}b", {{ x: -40, opacity: 0, duration: 0.25 }}, {start + dur - 0.25:.3f});')

    def label(self, text, start, dur, top=300):
        lid = self.uid("lb")
        self.layers.append(f'<section id="{lid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="label" id="{lid}b" style="top:{top}px">{esc(text)}</div></section>')
        self.js.append(f'tl.fromTo("#{lid}b", {{ y: 16, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "power2.out" }}, {start + 0.1:.3f});')
        self.js.append(f'tl.to("#{lid}b", {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')

    def screenshot(self, src, start, dur, highlights=()):
        """highlights: [(x, y, w, h, at)] in screenshot-display pixels (width 800)."""
        sid = self.uid("ss")
        hls = "".join(f'<div class="hl" id="{sid}h{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>' for i, (x, y, w, h, at) in enumerate(highlights))
        self.layers.append(f'<section id="{sid}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="clip" style="background:rgba(10,11,13,0.72)" id="{sid}bg"></div>'
                           f'<div class="shot" id="{sid}b"><img src="{src}" alt="Feedback klien di WhatsApp">{hls}</div></section>')
        self.js.append(f'tl.fromTo("#{sid}bg", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25 }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{sid}b", {{ y: 900 }}, {{ y: 0, duration: 0.5, ease: "power3.out" }}, {start:.3f});')
        for i, (x, y, w, h, at) in enumerate(highlights):
            self.js.append(f'tl.fromTo("#{sid}h{i}", {{ scale: 1.25, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {at:.3f});')
            self.sfx("ping", at, 0.4)
        self.js.append(f'tl.to(["#{sid}b", "#{sid}bg"], {{ opacity: 0, duration: 0.3 }}, {start + dur - 0.3:.3f});')
        self.sfx("whoosh", start, 0.45)

    def music(self, src, start, dur, media_start=0.0, vol=0.8, fade=1.5):
        mid = self.uid("mu")
        auto = json.dumps({"volume": [[0, 0], [0.4, vol], [max(0.5, dur - fade), vol], [dur, 0]]})
        self.layers.append(f"<audio id=\"{mid}\" src=\"{src}\" data-start=\"{start:.3f}\" data-duration=\"{dur:.3f}\" data-media-start=\"{media_start:.3f}\" data-track-index=\"10\" data-volume=\"{vol}\"></audio>")

    def laser(self, start, dur=5.0, bg_src="../assets/footage/IMG_5104.mp4", kicker="UPGRADE 🔧", title="Laser measure", badge="Ukur dalam 1 saat"):
        p = self.uid("lz")
        T = lambda x: f"{start + x:.3f}"
        self.layers.append(
            f'<div class="lz-bgwrap"><video id="{p}v" class="clip" src="{bg_src}" muted playsinline data-start="{start:.3f}" data-duration="{dur:.3f}" data-media-start="0" data-track-index="3"></video></div>'
            f'<section id="{p}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="4">'
            f'<div class="lz-title"><div class="lz-kicker" id="{p}k">{esc(kicker)}</div><div class="lz-main" id="{p}t">{esc(title)}</div></div>'
            f'<div class="lz-wall" id="{p}wall"></div><div class="lz-beam" id="{p}beam"></div><div class="lz-dot" id="{p}dot"></div>'
            f'<div class="lz-device" id="{p}dev"><div class="lz-grip"></div><div class="lz-screen" id="{p}scr"><div class="lz-glow" id="{p}glow"></div>'
            f'<div class="lz-read" id="{p}read">0.000</div><div class="lz-unit">m</div></div><div class="lz-emit"></div></div>'
            f'<div class="lz-dim"><div class="lz-cap" id="{p}c1" style="left:0"></div><div class="lz-dline" id="{p}dl"></div><div class="lz-cap" id="{p}c2" style="right:0"></div>'
            f'<div class="lz-dlabel" id="{p}lab">4.785 m</div></div>'
            f'<div class="lz-badge" id="{p}bdg"><div class="lz-check">✓</div>{esc(badge)}</div></section>')
        js = [
            f'tl.fromTo("#{p}k", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {T(0.05)});',
            f'tl.fromTo("#{p}t", {{ y: 80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power3.out" }}, {T(0.15)});',
            f'tl.fromTo("#{p}wall", {{ x: 140 }}, {{ x: 0, duration: 0.45, ease: "power3.out" }}, {T(0.2)});',
            f'tl.fromTo("#{p}dev", {{ x: -520, rotation: -6 }}, {{ x: 0, rotation: 0, duration: 0.5, ease: "power3.out" }}, {T(0.3)});',
            f'tl.fromTo("#{p}glow", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.12 }}, {T(0.85)});',
            f'tl.fromTo("#{p}beam", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.3, ease: "power2.in" }}, {T(1.0)});',
            f'tl.fromTo("#{p}dot", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.18, ease: "back.out(3)" }}, {T(1.28)});',
            f'const {p}c = {{ v: 0 }}; const {p}r = document.getElementById("{p}read");',
            f'tl.fromTo({p}c, {{ v: 0 }}, {{ v: 4.785, duration: 0.85, ease: "power2.out", onUpdate: () => {{ {p}r.textContent = {p}c.v.toFixed(3); }} }}, {T(1.3)});',
            f'tl.fromTo("#{p}dl", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.85, ease: "power2.out" }}, {T(1.3)});',
            f'tl.fromTo(["#{p}c1", "#{p}c2"], {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.18, stagger: 0.67 }}, {T(1.3)});',
            f'tl.fromTo("#{p}lab", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {T(2.1)});',
            f'tl.fromTo("#{p}scr", {{ scale: 1 }}, {{ scale: 1.08, duration: 0.1, yoyo: true, repeat: 1 }}, {T(2.15)});',
            f'tl.fromTo("#{p}bdg", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {T(2.3)});',
        ]
        self.js += js
        self.sfx("whoosh", start + 0.25, 0.45)
        self.sfx("click", start + 0.85, 0.5)
        self.sfx("riser", start + 1.0, 0.25, dur=1.1)
        self.sfx("ping", start + 2.15, 0.5)

    # ---- output ----------------------------------------------------------
    def write(self, path, title):
        doc = f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>{esc(title)}</title>
    <script src="../assets/vendor/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="{self.cid}" data-start="0" data-width="1080" data-height="1920" data-duration="{self.duration:.3f}">
      {chr(10).join("      " + l for l in self.layers).lstrip()}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join("      " + l for l in self.js).lstrip()}
      window.__timelines["{self.cid}"] = tl;
    </script>
  </body>
</html>
"""
        open(path, "w").write(doc)
        print("wrote", path, f"{self.duration:.2f}s", len(self.layers), "layers")
