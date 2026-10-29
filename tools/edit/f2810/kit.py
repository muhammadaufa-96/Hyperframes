"""Folder 28/10/26 kit: reference-style graphics (two-tone hook, numbered section label,
glass cards, journey line, door diagram, rating meter, location pin, service and name cards,
Luma and bangfasz end cards, reference-style captions) on top of the ads Ad class."""
import re, sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/ads")
sys.path.insert(0, "/home/user/Hyperframes/tools")
import gen
from adkit import Ad, align, esc, LOGO

Y = "#f5c22e"

gen.CSS += r"""
/* two-tone hook (reference style) */
.h2 { position: absolute; left: 50px; right: 50px; top: 270px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 6px; }
.h2-k { font-weight: 600; font-size: 40px; letter-spacing: 0.06em; text-transform: uppercase; color: #fff; text-shadow: 0 3px 14px rgba(0,0,0,0.7); }
.h2-b { font-weight: 800; font-size: 118px; line-height: 0.98; text-transform: uppercase; color: #f5c22e; text-shadow: 0 6px 0 rgba(0,0,0,0.35), 0 0 40px rgba(0,0,0,0.55); }
.h2-s { font-weight: 600; font-style: italic; font-size: 46px; color: #fff; text-shadow: 0 3px 14px rgba(0,0,0,0.75); }
.h2-sh { position: absolute; left: 0; right: 0; top: 0; height: 900px; background: linear-gradient(180deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.25) 60%, rgba(0,0,0,0) 100%); }

/* numbered section label + progress */
.sec { position: absolute; left: 0; right: 0; top: 230px; display: flex; flex-direction: column; align-items: center; gap: 10px; }
.sec-p { display: flex; align-items: center; gap: 14px; background: rgba(15,17,20,0.78); border: 2px solid rgba(255,255,255,0.18); border-radius: 999px; padding: 10px 26px 10px 12px; }
.sec-n { background: #f5c22e; color: #15171a; font-weight: 800; font-size: 30px; border-radius: 999px; padding: 4px 16px; }
.sec-t { font-weight: 800; font-size: 36px; text-transform: uppercase; color: #fff; letter-spacing: 0.03em; white-space: nowrap; }
.sec-bar { width: 420px; height: 8px; border-radius: 4px; background: rgba(255,255,255,0.25); overflow: hidden; }
.sec-bar i { display: block; height: 100%; background: #f5c22e; transform-origin: left center; }

/* glass card */
.gc { position: absolute; left: 90px; right: 90px; background: rgba(14,16,20,0.78); border: 2px solid rgba(255,255,255,0.16); border-radius: 28px; padding: 26px 30px; box-shadow: 0 24px 60px rgba(0,0,0,0.45); }
.gc-h { display: flex; align-items: center; gap: 12px; font-weight: 800; font-size: 28px; letter-spacing: 0.08em; text-transform: uppercase; color: #f5c22e; }
.gc-r { display: flex; align-items: center; gap: 16px; margin-top: 16px; font-weight: 800; font-size: 44px; color: #fff; }
.gc-r i { width: 52px; height: 52px; flex: none; border-radius: 50%; background: #20b26b; color: #fff; font-style: normal; display: flex; align-items: center; justify-content: center; font-size: 30px; }
.gc-r i.w { background: #ff8a00; }
.gc-r i.n { background: #f5c22e; color: #15171a; }

/* journey line */
.jy { position: absolute; left: 50px; right: 50px; top: 300px; height: 200px; background: rgba(14,16,20,0.78); border-radius: 26px; border: 2px solid rgba(255,255,255,0.14); }
.jy-l { position: absolute; left: 80px; right: 80px; top: 70px; height: 6px; background: rgba(255,255,255,0.2); border-radius: 3px; }
.jy-f { position: absolute; left: 80px; right: 80px; top: 70px; height: 6px; background: #f5c22e; border-radius: 3px; transform-origin: left center; transform: scaleX(0); }
.jy-d { position: absolute; top: 52px; width: 42px; height: 42px; margin-left: -21px; border-radius: 50%; background: #2a2d33; border: 5px solid rgba(255,255,255,0.4); }
.jy-t { position: absolute; top: 112px; width: 200px; margin-left: -100px; text-align: center; font-weight: 800; font-size: 25px; text-transform: uppercase; color: rgba(255,255,255,0.5); line-height: 1.1; }

/* door diagram */
.dd { position: absolute; left: 90px; right: 90px; top: 300px; background: rgba(14,16,20,0.82); border-radius: 28px; padding: 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.dd-c { display: flex; flex-direction: column; align-items: center; gap: 10px; }
.dd-c b { font-weight: 800; font-size: 36px; text-transform: uppercase; }
.dd-c span { font-weight: 600; font-size: 28px; }
.dd svg { width: 380px; height: 300px; }

/* rating */
.rt2 { position: absolute; left: 90px; right: 90px; top: 280px; background: rgba(14,16,20,0.82); border-radius: 28px; padding: 26px 32px; border: 2px solid rgba(255,255,255,0.16); }
.rt2-big { text-align: center; font-weight: 800; font-size: 150px; line-height: 1; color: #f5c22e; }
.rt2-big small { font-size: 60px; color: #fff; }
.rt2-r { margin-top: 18px; }
.rt2-r b { display: flex; justify-content: space-between; font-weight: 800; font-size: 34px; text-transform: uppercase; }
.rt2-bar { margin-top: 8px; height: 22px; border-radius: 11px; background: rgba(255,255,255,0.15); overflow: hidden; }
.rt2-bar i { display: block; height: 100%; border-radius: 11px; background: linear-gradient(90deg, #f5c22e, #ff8a00); transform-origin: left center; transform: scaleX(0); }

/* location pin */
.pin { position: absolute; left: 0; right: 0; display: flex; justify-content: center; }
.pin div { display: flex; align-items: center; gap: 14px; background: #fff; color: #15171a; border-radius: 999px; padding: 14px 30px 14px 16px; font-weight: 800; font-size: 40px; box-shadow: 0 16px 40px rgba(0,0,0,0.45); white-space: nowrap; }
.pin i { width: 56px; height: 56px; border-radius: 50%; background: #ff3b3b; color: #fff; font-style: normal; display: flex; align-items: center; justify-content: center; font-size: 32px; }
.pin span { font-weight: 600; color: #555; }

/* service cards */
.sv { position: absolute; left: 60px; right: 60px; top: 300px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.sv div { background: rgba(14,16,20,0.82); border: 2px solid rgba(255,255,255,0.16); border-radius: 24px; padding: 22px 10px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; }
.sv i { font-style: normal; font-size: 64px; }
.sv b { font-weight: 800; font-size: 32px; text-transform: uppercase; line-height: 1.05; }

/* name card */
.nc { position: absolute; left: 90px; right: 90px; top: 300px; display: flex; align-items: center; gap: 22px; background: rgba(14,16,20,0.82); border-left: 12px solid #f5c22e; border-radius: 22px; padding: 22px 28px; }
.nc i { width: 96px; height: 96px; flex: none; border-radius: 50%; background: #f5c22e; color: #15171a; font-style: normal; display: flex; align-items: center; justify-content: center; font-size: 52px; }
.nc b { display: block; font-weight: 800; font-size: 48px; }
.nc span { display: block; font-weight: 600; font-size: 32px; color: #d9dadc; margin-top: 4px; }

/* end cards */
.lc { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 26px; background: rgba(10,11,13,0.78); padding: 0 70px 200px; text-align: center; }
.lc-k { font-weight: 600; font-size: 38px; letter-spacing: 0.14em; color: #d9dadc; text-transform: uppercase; }
.lc-q { font-weight: 800; font-size: 112px; line-height: 1; text-transform: uppercase; }
.lc-q em { display: block; font-style: normal; color: #f5c22e; font-size: 70px; margin-top: 10px; }
.lc-s { font-weight: 600; font-style: italic; font-size: 40px; color: #e7e7e7; }
.lc-b { background: #f5c22e; color: #15171a; border-radius: 999px; padding: 20px 46px; font-weight: 800; font-size: 44px; text-transform: uppercase; }
.lc-l { width: 300px; opacity: 0.9; }
.lc-f { font-weight: 600; font-size: 28px; color: #bbb; }

/* reference-style captions */
.cr { position: absolute; left: 70px; right: 70px; top: 1250px; text-align: center; font-weight: 800; font-size: 54px; line-height: 1.15; }
.cr .w { display: inline-block; margin: 0 8px; color: #fff; text-shadow: 0 4px 0 rgba(0,0,0,0.45), 0 0 22px rgba(0,0,0,0.7); }
.cr .w.hot { color: #f5c22e; }

/* flash for whip cuts */
.fl2 { position: absolute; inset: 0; background: #fff; opacity: 0; }
"""


class K(Ad):
    def hook2(self, kicker, big, sub, start, dur, shade=True):
        h = self.uid("h2")
        sh = '<div class="h2-sh"></div>' if shade else ""
        self.layers.append(f'<section id="{h}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="5">{sh}'
                           f'<div class="h2"><div class="h2-k" id="{h}k">{esc(kicker)}</div><div class="h2-b" id="{h}b">{big}</div>'
                           f'<div class="h2-s" id="{h}s">{esc(sub)}</div></div></section>')
        self.js.append(f'tl.fromTo("#{h}k", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.25 }}, {start + 0.02:.3f});')
        self.js.append(f'tl.fromTo("#{h}b", {{ scale: 1.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "power4.out" }}, {start + 0.15:.3f});')
        self.js.append(f'tl.fromTo("#{h}s", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, {start + 0.45:.3f});')
        self.js.append(f'tl.to("#{h} > *", {{ opacity: 0, duration: 0.25 }}, {start + dur - 0.25:.3f});')
        self.sfx("whoosh", start, 0.45)
        self.sfx("impact-bass-1", start + 0.15, 0.5)

    def counter(self, n_to, start, dur, label_html, top=560):
        """Big number counting up from 1 (e.g. 9 rooms)."""
        c = self.uid("ct")
        self.layers.append(f'<section id="{c}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="h2" style="top:{top}px"><div class="h2-b" id="{c}n" style="font-size:300px">1</div><div class="h2-s" id="{c}l">{label_html}</div></div></section>')
        self.js.append(f'const {c}o = {{ v: 1 }}; const {c}e = document.getElementById("{c}n");')
        self.js.append(f'tl.fromTo({c}o, {{ v: 1 }}, {{ v: {n_to}, duration: 0.8, ease: "power2.out", onUpdate: () => {{ {c}e.textContent = Math.round({c}o.v); }} }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{c}n", {{ scale: 0.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{c}l", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, {start + 0.6:.3f});')
        self.js.append(f'tl.to("#{c} .h2", {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')
        self.sfx("riser", start, 0.25, dur=0.8)
        self.sfx("impact-bass-2", start + 0.8, 0.45)

    def section(self, i, total, title, start, dur):
        s = self.uid("sc")
        self.layers.append(f'<section id="{s}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="6">'
                           f'<div class="sec"><div class="sec-p" id="{s}p"><span class="sec-n">{i:02d} / {total:02d}</span><span class="sec-t">{esc(title)}</span></div>'
                           f'<div class="sec-bar"><i id="{s}b" style="transform:scaleX({(i - 1) / total:.3f})"></i></div></div></section>')
        self.js.append(f'tl.fromTo("#{s}p", {{ y: -30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {start:.3f});')
        self.js.append(f'tl.to("#{s}b", {{ scaleX: {i / total:.3f}, duration: 0.5, ease: "power2.out" }}, {start + 0.1:.3f});')
        self.js.append(f'tl.to("#{s} .sec", {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')
        self.sfx("click", start, 0.4)

    def glass(self, head, rows, start, dur, top=430, at=None, icons=None):
        """rows: list of text; at: per-row reveal times; icons: per-row icon char + class ('', 'w', 'n')."""
        g = self.uid("gc")
        at = at or [start + 0.25 + k * 0.35 for k in range(len(rows))]
        icons = icons or [("✓", "")] * len(rows)
        rr = "".join(f'<div class="gc-r" id="{g}r{k}"><i class="{ic[1]}">{esc(ic[0])}</i>{esc(t)}</div>' for k, (t, ic) in enumerate(zip(rows, icons)))
        self.layers.append(f'<section id="{g}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="gc" id="{g}m" style="top:{top}px"><div class="gc-h">{esc(head)}</div>{rr}</div></section>')
        self.js.append(f'tl.fromTo("#{g}m", {{ y: 40, scale: 0.92, opacity: 0 }}, {{ y: 0, scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {start:.3f});')
        for k, t in enumerate(at):
            self.js.append(f'tl.fromTo("#{g}r{k}", {{ x: -30, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.25, ease: "power2.out" }}, {t:.3f});')
            self.sfx("ping", t, 0.35)
        self.js.append(f'tl.to("#{g}m", {{ opacity: 0, y: -20, duration: 0.25 }}, {start + dur - 0.25:.3f});')

    def journey(self, stops, at, end, top=300):
        j = self.uid("jy")
        n = len(stops)
        xs = [80 + k * (820 / (n - 1)) for k in range(n)]
        dots = "".join(f'<div class="jy-d" id="{j}d{k}" style="left:{x:.0f}px"></div><div class="jy-t" id="{j}t{k}" style="left:{x:.0f}px">{esc(t)}</div>' for k, (x, t) in enumerate(zip(xs, stops)))
        st = at[0] - 0.3
        self.layers.append(f'<section id="{j}" class="clip" data-start="{st:.3f}" data-duration="{end - st:.3f}" data-track-index="6">'
                           f'<div class="jy" id="{j}m" style="top:{top}px"><div class="jy-l"></div><div class="jy-f" id="{j}f"></div>{dots}</div></section>')
        self.js.append(f'tl.fromTo("#{j}m", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, {st:.3f});')
        for k, t in enumerate(at):
            self.js.append(f'tl.to("#{j}d{k}", {{ backgroundColor: "{Y}", borderColor: "{Y}", scale: 1.25, duration: 0.2 }}, {t:.3f});')
            self.js.append(f'tl.to("#{j}t{k}", {{ color: "#ffffff", duration: 0.2 }}, {t:.3f});')
            if k:
                self.js.append(f'tl.to("#{j}f", {{ scaleX: {k / (n - 1):.3f}, duration: 0.35, ease: "power2.out" }}, {t - 0.25:.3f});')
            self.sfx("ping", t, 0.3)
        self.js.append(f'tl.to("#{j}m", {{ opacity: 0, duration: 0.25 }}, {end - 0.25:.3f});')

    def doors(self, start, dur, t_swing, t_slide):
        d = self.uid("dd")
        swing = ('<svg viewBox="0 0 380 300"><rect x="20" y="20" width="340" height="260" fill="none" stroke="#fff" stroke-width="8"/>'
                 '<rect x="140" y="12" width="100" height="16" fill="#15171a"/>'
                 f'<path id="{d}a" d="M140 20 A100 100 0 0 1 240 120 L140 20 Z" fill="rgba(255,59,59,0.45)" stroke="#ff3b3b" stroke-width="5"/>'
                 '<line x1="140" y1="20" x2="140" y2="120" stroke="#fff" stroke-width="8"/></svg>')
        slide = ('<svg viewBox="0 0 380 300"><rect x="20" y="20" width="340" height="260" fill="none" stroke="#fff" stroke-width="8"/>'
                 '<rect x="140" y="12" width="100" height="16" fill="#15171a"/>'
                 f'<rect id="{d}s" x="140" y="30" width="100" height="10" fill="#f5c22e"/>'
                 f'<rect id="{d}g" x="30" y="44" width="320" height="226" fill="rgba(32,178,107,0.25)"/></svg>')
        self.layers.append(f'<section id="{d}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="dd" id="{d}m"><div class="dd-c" id="{d}c1">{swing}<b>Swing</b><span style="color:#ff6b6b">ruang terbuang</span></div>'
                           f'<div class="dd-c" id="{d}c2">{slide}<b>Sliding</b><span style="color:#3ad08a">ruang jimat</span></div></div></section>')
        self.js.append(f'tl.fromTo("#{d}m", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{d}c2", {{ opacity: 0.15 }}, {{ opacity: 0.15, duration: 0.01 }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{d}a", {{ scale: 0, transformOrigin: "0% 0%" }}, {{ scale: 1, duration: 0.6, ease: "power2.out" }}, {t_swing:.3f});')
        self.js.append(f'tl.to("#{d}c1", {{ opacity: 0.35, duration: 0.3 }}, {t_slide:.3f});')
        self.js.append(f'tl.to("#{d}c2", {{ opacity: 1, duration: 0.3 }}, {t_slide:.3f});')
        self.js.append(f'tl.fromTo("#{d}s", {{ x: 0 }}, {{ x: 110, duration: 0.6, ease: "power2.inOut" }}, {t_slide + 0.2:.3f});')
        self.js.append(f'tl.fromTo("#{d}g", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4 }}, {t_slide + 0.5:.3f});')
        self.js.append(f'tl.to("#{d}m", {{ opacity: 0, duration: 0.25 }}, {start + dur - 0.25:.3f});')
        self.sfx("whoosh-short", t_swing, 0.4); self.sfx("error", t_swing + 0.4, 0.25)
        self.sfx("whoosh", t_slide + 0.2, 0.4); self.sfx("ping", t_slide + 0.6, 0.4)

    def rating(self, rows, total, start, dur, top=280):
        r = self.uid("rt")
        rr = "".join(f'<div class="rt2-r"><b><span>{esc(n)}</span><span id="{r}v{k}">0</span></b><div class="rt2-bar"><i id="{r}b{k}"></i></div></div>' for k, (n, v) in enumerate(rows))
        self.layers.append(f'<section id="{r}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="rt2" id="{r}m"><div class="rt2-big"><span id="{r}n">0.0</span><small>/10</small></div>{rr}</div></section>')
        self.js.append(f'tl.fromTo("#{r}m", {{ y: 40, scale: 0.9, opacity: 0 }}, {{ y: 0, scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {start:.3f});')
        self.js.append(f'const {r}o = {{ v: 0 }}; const {r}e = document.getElementById("{r}n");')
        self.js.append(f'tl.fromTo({r}o, {{ v: 0 }}, {{ v: {total}, duration: 1.4, ease: "power2.out", onUpdate: () => {{ {r}e.textContent = {r}o.v.toFixed(1); }} }}, {start + 0.3:.3f});')
        for k, (n, v) in enumerate(rows):
            t = start + 0.5 + k * 0.3
            self.js.append(f'tl.to("#{r}b{k}", {{ scaleX: {v / 10:.3f}, duration: 0.8, ease: "power2.out" }}, {t:.3f});')
            self.js.append(f'const {r}o{k} = {{ v: 0 }}; const {r}e{k} = document.getElementById("{r}v{k}");')
            self.js.append(f'tl.fromTo({r}o{k}, {{ v: 0 }}, {{ v: {v}, duration: 0.8, ease: "power2.out", onUpdate: () => {{ {r}e{k}.textContent = {r}o{k}.v.toFixed(1); }} }}, {t:.3f});')
        self.js.append(f'tl.to("#{r}m", {{ opacity: 0, duration: 0.25 }}, {start + dur - 0.25:.3f});')
        self.sfx("riser", start + 0.3, 0.25, dur=1.3)
        self.sfx("sparkle", start + 1.7, 0.45)

    def pin(self, place, area, start, dur, top=470):
        p = self.uid("pn")
        self.layers.append(f'<section id="{p}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="pin" style="top:{top}px"><div id="{p}b"><i>📍</i>{esc(place)}<span>· {esc(area)}</span></div></div></section>')
        self.js.append(f'tl.fromTo("#{p}b", {{ y: -80, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "bounce.out" }}, {start:.3f});')
        self.js.append(f'tl.to("#{p}b", {{ opacity: 0, duration: 0.2 }}, {start + dur - 0.2:.3f});')
        self.sfx("pop", start + 0.25, 0.45)

    def services(self, items, at, end):
        s = self.uid("sv")
        cards = "".join(f'<div id="{s}c{k}"><i>{ic}</i><b>{esc(t)}</b></div>' for k, (ic, t) in enumerate(items))
        st = at[0] - 0.05
        self.layers.append(f'<section id="{s}" class="clip" data-start="{st:.3f}" data-duration="{end - st:.3f}" data-track-index="7"><div class="sv" id="{s}m">{cards}</div></section>')
        for k, t in enumerate(at):
            self.js.append(f'tl.fromTo("#{s}c{k}", {{ y: 40, scale: 0.6, opacity: 0 }}, {{ y: 0, scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.2)" }}, {t:.3f});')
            self.sfx("pop", t, 0.4)
        self.js.append(f'tl.to("#{s}m", {{ opacity: 0, duration: 0.25 }}, {end - 0.25:.3f});')

    def namecard(self, icon, title, sub, start, dur, top=300):
        n = self.uid("nc")
        self.layers.append(f'<section id="{n}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="nc" id="{n}m" style="top:{top}px"><i>{icon}</i><div><b>{esc(title)}</b><span>{esc(sub)}</span></div></div></section>')
        self.js.append(f'tl.fromTo("#{n}m", {{ x: -900 }}, {{ x: 0, duration: 0.45, ease: "power3.out" }}, {start:.3f});')
        self.js.append(f'tl.to("#{n}m", {{ x: 900, duration: 0.3, ease: "power2.in" }}, {start + dur - 0.3:.3f});')
        self.sfx("whoosh-short", start, 0.45)

    def whip(self, t):
        """Reference-style cut accent: quick punch on the footage and a white flash."""
        f = self.uid("wf")
        self.layers.append(f'<section id="{f}" class="clip" data-start="{t - 0.06:.3f}" data-duration="0.3" data-track-index="7"><div class="fl2" id="{f}x"></div></section>')
        self.js.append(f'tl.fromTo("#{f}x", {{ opacity: 0.55 }}, {{ opacity: 0, duration: 0.24, ease: "power2.out" }}, {t - 0.06:.3f});')
        self.sfx("whoosh-short", t - 0.12, 0.35)

    def end_card(self, kicker, big, sub, btn, start, dur, logo=LOGO, foot=""):
        e = self.uid("lc")
        logo_html = f'<img class="lc-l" id="{e}l" src="{logo}" alt="logo">' if logo else ""
        foot_html = f'<div class="lc-f">{esc(foot)}</div>' if foot else ""
        self.layers.append(f'<section id="{e}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="lc" id="{e}m"><div class="lc-k" id="{e}k">{esc(kicker)}</div><div class="lc-q" id="{e}q">{big}</div>'
                           f'<div class="lc-s" id="{e}s">{esc(sub)}</div><div class="lc-b" id="{e}b">{esc(btn)}</div>{logo_html}{foot_html}</div></section>')
        self.js.append(f'tl.fromTo("#{e}m", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, {start:.3f});')
        self.js.append(f'tl.fromTo("#{e}k", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, {start + 0.1:.3f});')
        self.js.append(f'tl.fromTo("#{e}q", {{ scale: 1.3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "power4.out" }}, {start + 0.2:.3f});')
        self.js.append(f'tl.fromTo("#{e}s", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, {start + 0.5:.3f});')
        self.js.append(f'tl.fromTo("#{e}b", {{ scale: 0.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2)" }}, {start + 0.7:.3f});')
        self.js.append(f'tl.to("#{e}b", {{ scale: 1.06, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: {max(1, int((dur - 1.3) / 0.6)) * 2 - 1} }}, {start + 1.1:.3f});')
        if logo:
            self.js.append(f'tl.fromTo("#{e}l", {{ opacity: 0 }}, {{ opacity: 0.9, duration: 0.4 }}, {start + 0.9:.3f});')
        self.sfx("whoosh-cinematic", start - 0.1, 0.45)
        self.sfx("chime", start + 0.2, 0.4)

    def ckaps_end(self, start, dur):
        self.end_card("Enoxin.Fitout · Klinik A to Z", 'Nak setup<em>klinik estetik?</em>', "Dapatkan Free CKAPS Initial Assessment", "👇 Klik link di bawah", start, dur)

    def captions_ref(self, words, hot=(), hide=()):
        """Bold reference-style captions: up to 4 words, keywords in Enoxin yellow, each group pops."""
        hot = {h.lower() for h in hot}
        words = [w for w in words if not any(a <= w[1] < b for a, b in hide)]
        groups, cur = [], []
        for w in words:
            if cur and (len(cur) >= 4 or sum(len(x[0]) + 1 for x in cur) + len(w[0]) > 22 or w[1] - cur[-1][2] > 0.45):
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
            cid = self.uid("cr")
            spans = "".join(f'<span class="w{" hot" if re.sub(r"[^\w-]", "", w[0]).lower() in hot else ""}" id="{cid}w{i}">{esc(w[0])}</span>' for i, w in enumerate(g))
            self.layers.append(f'<section id="{cid}" class="clip" data-start="{st:.3f}" data-duration="{en - st:.3f}" data-track-index="8"><div class="cr">{spans}</div></section>')
            self.js.append(f'tl.fromTo("#{cid} .cr", {{ scale: 0.88, y: 14 }}, {{ scale: 1, y: 0, duration: 0.14, ease: "back.out(2)" }}, {st:.3f});')
            for i, w in enumerate(g):
                self.js.append(f'tl.fromTo("#{cid}w{i}", {{ opacity: 0.55 }}, {{ opacity: 1, duration: 0.05 }}, {max(w[1], st):.3f});')
