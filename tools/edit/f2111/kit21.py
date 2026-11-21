"""21/11 kit: graphics for the two edits (bekal isteri, cat Jotun) on top of the 20/11 V class."""
import sys
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2011")
sys.path.insert(0, "/home/user/Hyperframes/tools/edit/f2810")
import build as b20                       # 20/11 V class, icons, captions_box, cta, flash, nametag, foundation...
from build import V, ICON, esc
import gen

Y = "#f5c22e"; G = "#20b26b"; R = "#ff3b3b"

ICON.update({
    "box3": '<svg viewBox="0 0 24 24"><rect x="3" y="9" width="18" height="11" rx="2" fill="currentColor"/><rect x="2" y="5" width="20" height="4" rx="1.5" fill="currentColor" opacity="0.7"/></svg>',
    "chili": '<svg viewBox="0 0 24 24"><path d="M15 6c3 1 5 4 4 8-1 5-7 8-13 8 4-2 7-5 7-9 0-3 0-5 2-7z" fill="currentColor"/><path d="M15 6c0-2 1-3 3-4" stroke="#20b26b" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24"><path d="M13 2L4 14h6l-1 8 9-12h-6z" fill="currentColor"/></svg>',
    "tag": '<svg viewBox="0 0 24 24"><path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z" fill="currentColor"/><circle cx="8" cy="8" r="1.8" fill="#15171a"/></svg>',
    "bucket": '<svg viewBox="0 0 24 24"><path d="M5 7h14l-1.5 13a2 2 0 0 1-2 2h-7a2 2 0 0 1-2-2z" fill="currentColor"/><ellipse cx="12" cy="7" rx="7" ry="2.2" fill="#15171a" opacity="0.35"/><path d="M6 7c0-4 12-4 12 0" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>',
    "chat": '<svg viewBox="0 0 24 24"><path d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" fill="currentColor"/></svg>',
    "down": '<svg viewBox="0 0 24 24"><path d="M12 4v14M5 12l7 7 7-7" stroke="currentColor" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
})

gen.CSS += r"""
/* ---------- 21/11 kit ---------- */
.bx-tr { position: absolute; left: 70px; right: 70px; top: 270px; background: rgba(14,16,20,0.86); border: 2px solid rgba(255,255,255,0.14); border-radius: 26px; padding: 18px 26px 22px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }
.bx-h { display: flex; align-items: center; justify-content: space-between; }
.bx-k { font-weight: 800; font-size: 30px; letter-spacing: 0.1em; text-transform: uppercase; color: #f5c22e; }
.bx-n { font-weight: 800; font-size: 34px; color: #fff; }
.bx-bar { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 14px; }
.bx-bar i { display: block; height: 12px; border-radius: 6px; background: rgba(255,255,255,0.18); overflow: hidden; }
.bx-bar i b { display: block; height: 100%; background: #f5c22e; transform-origin: left center; transform: scaleX(0); }
.bx-lab { position: relative; height: 64px; margin-top: 14px; }
.bx-lab div { position: absolute; left: 0; top: 0; display: flex; align-items: center; gap: 16px; font-weight: 800; font-size: 54px; line-height: 1.1; text-transform: uppercase; white-space: nowrap; opacity: 0; }
.bx-lab .ico { width: 58px; height: 58px; border-radius: 14px; background: #f5c22e; color: #15171a; padding: 10px; }

.st2 { position: absolute; left: 0; right: 0; display: flex; justify-content: center; }
.st2 span { display: inline-block; font-weight: 800; font-size: 74px; line-height: 1.02; text-align: center; text-transform: uppercase; color: #fff; background: #ff3b3b; border: 7px solid #fff; border-radius: 20px; padding: 10px 28px 14px; box-shadow: 0 18px 50px rgba(0,0,0,0.5); }
.st2.g span { background: #20b26b; }
.st2.y span { background: #f5c22e; color: #15171a; }

.hr { position: absolute; width: 120px; height: 120px; color: #ff3b5c; filter: drop-shadow(0 8px 18px rgba(0,0,0,0.45)); }
.hr-t { position: absolute; left: 0; right: 0; display: flex; justify-content: center; }
.hr-t span { font-weight: 800; font-size: 62px; text-transform: uppercase; color: #fff; background: #ff3b5c; border-radius: 999px; padding: 12px 36px; box-shadow: 0 16px 40px rgba(0,0,0,0.45); }

.tt { position: absolute; left: 70px; right: 70px; top: 270px; background: rgba(14,16,20,0.86); border: 2px solid rgba(255,255,255,0.14); border-radius: 26px; padding: 20px 28px 24px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }
.tt-r { display: flex; align-items: center; gap: 20px; margin-top: 14px; }
.tt-r b { width: 170px; font-weight: 800; font-size: 40px; text-transform: uppercase; }
.tt-c { display: flex; gap: 8px; }
.tt-c .ico { width: 62px; height: 62px; color: rgba(255,255,255,0.18); }
.tt-bar { flex: 1; height: 30px; border-radius: 15px; background: rgba(255,255,255,0.15); overflow: hidden; }
.tt-bar i { display: block; height: 100%; border-radius: 15px; background: linear-gradient(90deg, #ffd34d, #ff8ab0); transform-origin: left center; transform: scaleX(0); }
.tt-v { font-weight: 800; font-size: 34px; color: #f5c22e; text-transform: uppercase; white-space: nowrap; min-width: 210px; text-align: right; }
.tt-ok { position: absolute; right: 26px; top: 18px; display: flex; align-items: center; gap: 8px; background: #20b26b; border-radius: 999px; padding: 6px 20px 6px 8px; font-weight: 800; font-size: 30px; text-transform: uppercase; }
.tt-ok .ico { width: 40px; height: 40px; padding: 5px; }

.ov { position: absolute; left: 90px; right: 90px; top: 290px; }
.ov-k { display: inline-block; font-weight: 800; font-size: 34px; letter-spacing: 0.1em; text-transform: uppercase; color: #fff; background: rgba(14,16,20,0.84); border-radius: 10px; padding: 6px 16px; }
.ov-t { position: relative; margin-top: 12px; height: 64px; border-radius: 32px; background: rgba(14,16,20,0.82); border: 3px solid rgba(255,255,255,0.25); overflow: visible; }
.ov-f { position: absolute; left: 6px; top: 6px; bottom: 6px; width: calc(100% - 12px); border-radius: 26px; background: linear-gradient(90deg, #20b26b, #f5c22e 70%, #ff3b3b); transform-origin: left center; transform: scaleX(0); }
.ov-p { position: absolute; right: -10px; top: -78px; font-weight: 800; font-size: 64px; color: #f5c22e; text-shadow: 0 4px 0 rgba(0,0,0,0.4); }

.qs { position: absolute; left: 70px; right: 70px; top: 270px; display: flex; flex-direction: column; align-items: flex-start; gap: 14px; }
.qs-k { display: flex; align-items: center; gap: 12px; background: #f5c22e; color: #15171a; border-radius: 999px; padding: 10px 26px 10px 12px; font-weight: 800; font-size: 34px; text-transform: uppercase; }
.qs-k .ico { width: 50px; height: 50px; border-radius: 50%; background: #15171a; color: #f5c22e; padding: 10px; }
.qs-t { font-weight: 800; font-size: 76px; line-height: 1.02; text-transform: uppercase; color: #fff; background: rgba(14,16,20,0.84); border-radius: 22px; padding: 14px 26px 18px; }
.qs-c { font-weight: 800; font-size: 36px; text-transform: uppercase; color: #fff; background: rgba(14,16,20,0.85); border: 2px dashed rgba(255,255,255,0.4); border-radius: 14px; padding: 8px 20px; }

.mg { position: absolute; left: 140px; right: 140px; top: 260px; height: 420px; background: rgba(14,16,20,0.86); border: 2px solid rgba(255,255,255,0.14); border-radius: 30px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }
.mg svg { position: absolute; left: 0; top: 0; }
.mg-l { position: absolute; bottom: 26px; font-weight: 800; font-size: 30px; text-transform: uppercase; }
.mg-h { position: absolute; left: 0; right: 0; top: 22px; text-align: center; font-weight: 800; font-size: 32px; letter-spacing: 0.1em; text-transform: uppercase; color: #f5c22e; }

.pl { position: absolute; left: 70px; right: 70px; top: 270px; background: rgba(14,16,20,0.88); border: 2px solid rgba(255,255,255,0.14); border-radius: 26px; padding: 22px 28px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }
.pl-q { font-weight: 800; font-size: 40px; line-height: 1.15; }
.pl-o { position: relative; margin-top: 16px; height: 74px; border-radius: 16px; background: rgba(255,255,255,0.1); overflow: hidden; }
.pl-o i { position: absolute; left: 0; top: 0; bottom: 0; width: 100%; transform-origin: left center; transform: scaleX(0); }
.pl-o span { position: absolute; left: 22px; right: 22px; top: 0; bottom: 0; display: flex; align-items: center; justify-content: space-between; font-weight: 800; font-size: 38px; text-transform: uppercase; }
.cm { position: absolute; left: 70px; top: 760px; display: flex; align-items: center; gap: 14px; background: #fff; color: #15171a; border-radius: 26px 26px 26px 6px; padding: 16px 28px 16px 16px; box-shadow: 0 16px 40px rgba(0,0,0,0.45); font-weight: 800; font-size: 40px; }
.cm .ico { width: 56px; height: 56px; border-radius: 50%; background: #f5c22e; color: #15171a; padding: 12px; }
.cm-c { display: inline-block; width: 4px; height: 40px; background: #15171a; margin-left: 4px; }
.dn { position: absolute; left: 0; right: 0; top: 1560px; display: flex; justify-content: center; }
.dn .ico { width: 110px; height: 110px; color: #f5c22e; filter: drop-shadow(0 6px 14px rgba(0,0,0,0.6)); }

.sw { position: absolute; left: 0; right: 0; top: 270px; height: 470px; }
.sw-c { position: absolute; left: 50%; top: 0; width: 300px; height: 420px; margin-left: -150px; border-radius: 22px; background: #fff; box-shadow: 0 22px 60px rgba(0,0,0,0.5); padding: 16px; transform-origin: 50% 100%; }
.sw-c i { display: block; height: 290px; border-radius: 14px; }
.sw-c b { display: block; margin-top: 16px; font-weight: 800; font-size: 46px; text-transform: uppercase; color: #15171a; text-align: center; }
.sw-c span { display: block; font-weight: 600; font-size: 22px; color: #666; text-align: center; }

.bc { position: absolute; left: 70px; right: 70px; top: 270px; display: flex; align-items: center; gap: 26px; background: rgba(14,16,20,0.88); border: 2px solid rgba(255,255,255,0.14); border-radius: 26px; padding: 22px 28px; box-shadow: 0 22px 60px rgba(0,0,0,0.5); }
.bc-b { position: relative; width: 150px; height: 150px; flex: none; }
.bc-b .ico { width: 150px; height: 150px; color: #fff; }
.bc-sw { position: absolute; left: 34px; top: 52px; width: 82px; height: 82px; border-radius: 50%; background: conic-gradient(#ff8ab0, #f5c22e, #9aa0a6, #ff8ab0); opacity: 0.9; }
.bc-r { flex: 1; }
.bc-t { font-weight: 800; font-size: 50px; text-transform: uppercase; line-height: 1.05; }
.bc-s { font-weight: 600; font-size: 30px; color: #d9dadc; margin-top: 6px; }
.bc-p { margin-top: 14px; height: 22px; border-radius: 11px; background: rgba(255,255,255,0.15); overflow: hidden; }
.bc-p i { display: block; height: 100%; border-radius: 11px; background: linear-gradient(90deg, #ff8ab0, #f5c22e); transform-origin: left center; transform: scaleX(0); }
.bc-ok { position: absolute; right: 22px; top: -24px; display: flex; align-items: center; gap: 8px; background: #20b26b; border-radius: 999px; padding: 6px 20px 6px 8px; font-weight: 800; font-size: 30px; text-transform: uppercase; }
.bc-ok .ico { width: 40px; height: 40px; padding: 5px; }

.nx { position: absolute; left: 0; right: 0; top: 290px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
.nx-k { font-weight: 800; font-size: 34px; letter-spacing: 0.14em; text-transform: uppercase; color: #15171a; background: #f5c22e; border-radius: 10px; padding: 6px 18px; }
.nx-t { display: flex; align-items: center; gap: 18px; font-weight: 800; font-size: 78px; line-height: 1; text-transform: uppercase; color: #fff; text-shadow: 0 6px 0 rgba(0,0,0,0.35), 0 0 30px rgba(0,0,0,0.6); }
.nx-t .ico { width: 96px; height: 96px; color: #f5c22e; }

.pt { position: absolute; left: 0; right: 0; top: 280px; display: flex; flex-direction: column; align-items: center; }
.pt-tag { position: relative; display: flex; align-items: center; gap: 14px; background: #f5c22e; color: #15171a; border-radius: 16px 60px 60px 16px; padding: 14px 40px 14px 24px; font-weight: 800; font-size: 60px; text-transform: uppercase; transform-origin: 0% 50%; box-shadow: 0 18px 44px rgba(0,0,0,0.45); }
.pt-tag i { width: 26px; height: 26px; border-radius: 50%; background: #15171a; }
"""


class V21(V):
    def setup(self, A, segs):
        self.A = A
        self.cuts = []        # (t, same_clip)
        ss = segs["segments"]
        for a, b in zip(ss, ss[1:]):
            self.cuts.append((b["out_in"], a["clip"] == b["clip"]))

    def camera21(self, punches, shakes=()):
        z = 1.0; base = []
        for t, same in self.cuts:
            z = (1.08 if z == 1.0 else 1.0) if same else 1.0
            base.append((t, z))
        def zoom_at(t):
            zz = 1.0
            for c, v in base:
                if c <= t:
                    zz = v
            return zz
        J = self.js.append
        J('tl.set("#acam", { scale: 1, transformOrigin: "50% 42%" }, 0);')
        for t, v in base:
            J(f'tl.set("#acam", {{ scale: {v} }}, {t:.3f});')
        for t, hold in punches:
            z0 = zoom_at(t)
            nxt = min([c for c, _ in self.cuts if c > t] + [self.A])
            back = min(t + hold, nxt - 0.52)
            if back - t < 0.4:
                continue
            J(f'tl.to("#acam", {{ scale: {z0 + 0.12:.3f}, duration: 0.28, ease: "power3.out" }}, {t - 0.05:.3f});')
            J(f'tl.to("#acam", {{ scale: {z0}, duration: 0.45, ease: "power2.inOut" }}, {back:.3f});')
        for t in shakes:
            J(f'tl.to("#acam", {{ keyframes: [{{ x: -24, rotation: -1 }}, {{ x: 20, rotation: 0.8 }}, {{ x: -12, rotation: -0.5 }}, {{ x: 6 }}, {{ x: 0, rotation: 0 }}], duration: 0.4, ease: "none" }}, {t:.3f});')

    # ---- shared ------------------------------------------------------------
    def hook21(self, kicker, l1, l2, start, dur, icon="box3", sub=None):
        h = self.uid("hk")
        a = "".join(f'<span id="{h}a{i}">{c if c != " " else "&nbsp;"}</span>' for i, c in enumerate(l1))
        b = "".join(f'<span id="{h}b{i}">{c if c != " " else "&nbsp;"}</span>' for i, c in enumerate(l2))
        subh = f'<div class="h2-s" id="{h}s">{esc(sub)}</div>' if sub else ""
        self.layers.append(f'<section id="{h}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="5">'
                           f'<div class="h2-sh"></div><div class="hk"><div class="hk-k" id="{h}k">{esc(kicker)}</div>'
                           f'<div class="hk-row"><span class="ico" id="{h}i" style="width:120px;height:120px;color:{Y}">{ICON[icon]}</span><div class="hk-a" style="font-size:112px">{a}</div></div>'
                           f'<div class="hk-b" style="font-size:112px">{b}</div>{subh}</div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{h}k", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {start:.3f});')
        J(f'tl.fromTo("#{h}i", {{ scale: 0, rotation: -40 }}, {{ scale: 1, rotation: 0, duration: 0.5, ease: "back.out(3)" }}, {start + 0.1:.3f});')
        J(f'tl.to("#{h}i", {{ keyframes: [{{ rotation: -14, duration: 0.12 }}, {{ rotation: 12, duration: 0.12 }}, {{ rotation: -6, duration: 0.1 }}, {{ rotation: 0, duration: 0.1 }}] }}, {start + 0.7:.3f});')
        for i in range(len(l1)):
            J(f'tl.fromTo("#{h}a{i}", {{ y: -140, opacity: 0, rotation: -12 }}, {{ y: 0, opacity: 1, rotation: 0, duration: 0.45, ease: "back.out(2.2)" }}, {start + 0.15 + i * 0.04:.3f});')
        for i in range(len(l2)):
            J(f'tl.fromTo("#{h}b{i}", {{ y: 140, opacity: 0, scale: 1.6 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "power4.out" }}, {start + 0.55 + i * 0.035:.3f});')
        if sub:
            J(f'tl.fromTo("#{h}s", {{ opacity: 0, filter: "blur(8px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.25 }}, {start + 1.1:.3f});')
        J(f'tl.to("#{h} .hk > *", {{ opacity: 0, y: -30, filter: "blur(8px)", duration: 0.25, stagger: 0.04, ease: "power2.in" }}, {start + dur - 0.35:.3f});')
        J(f'tl.to("#{h} .h2-sh", {{ opacity: 0, duration: 0.3 }}, {start + dur - 0.3:.3f});')
        self.sfx("whoosh", start, 0.45); self.sfx("pop", start + 0.15, 0.4)
        self.sfx("impact-bass-1", start + 0.55, 0.45, dur=1.0); self.sfx("sparkle", start + 1.1, 0.35)

    def stamp2(self, text_html, t, dur, top=560, cls="", shake=True):
        s = self.uid("s2")
        self.layers.append(f'<section id="{s}" class="clip" data-start="{t:.3f}" data-duration="{dur:.3f}" data-track-index="7">'
                           f'<div class="st2 {cls}" style="top:{top}px"><span id="{s}b">{text_html}</span></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{s}b", {{ scale: 2.4, rotation: -14, opacity: 0 }}, {{ scale: 1, rotation: -5, opacity: 1, duration: 0.22, ease: "power4.in" }}, {t:.3f});')
        if shake:
            J(f'tl.to("#{s}b", {{ keyframes: [{{ x: -12 }}, {{ x: 10 }}, {{ x: -6 }}, {{ x: 0 }}], duration: 0.24 }}, {t + 0.22:.3f});')
        J(f'tl.to("#{s}b", {{ scale: 0.6, opacity: 0, duration: 0.2, ease: "power2.in" }}, {t + dur - 0.2:.3f});')
        self.sfx("glitch-short" if cls == "" else "pop", t - 0.02, 0.3)
        self.sfx("impact-bass-2", t + 0.2, 0.3, dur=0.8)

    def hearts(self, text, t, dur, top=560):
        h = self.uid("ht")
        pos = [(160, 0, 1.0), (820, 40, 0.8), (480, -40, 1.25), (300, 120, 0.6), (700, 150, 0.7)]
        hs = "".join(f'<span class="hr ico" id="{h}h{i}" style="left:{x}px;top:{top + y}px">{ICON["heart"]}</span>' for i, (x, y, s) in enumerate(pos))
        self.layers.append(f'<section id="{h}" class="clip" data-start="{t:.3f}" data-duration="{dur:.3f}" data-track-index="7">{hs}'
                           f'<div class="hr-t" style="top:{top + 260}px"><span id="{h}t">{esc(text)}</span></div></section>')
        J = self.js.append
        for i, (x, y, s) in enumerate(pos):
            J(f'tl.fromTo("#{h}h{i}", {{ scale: 0, opacity: 0, y: 60 }}, {{ scale: {s}, opacity: 1, y: 0, duration: 0.45, ease: "back.out(3)" }}, {t + i * 0.07:.3f});')
            J(f'tl.to("#{h}h{i}", {{ y: -140 - {i * 20}, opacity: 0, duration: {dur - 0.6:.3f}, ease: "power1.in" }}, {t + 0.5 + i * 0.07:.3f});')
        J(f'tl.fromTo("#{h}t", {{ scale: 0.3, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "elastic.out(1, 0.55)" }}, {t + 0.15:.3f});')
        J(f'tl.to("#{h}t", {{ opacity: 0, y: -20, duration: 0.25 }}, {t + dur - 0.25:.3f});')
        self.sfx("pop", t, 0.35); self.sfx("sparkle", t + 0.15, 0.4)

    def comment_poll(self, start, end, t_poll, t_type, text, t_arrow):
        p = self.uid("pl")
        typed = "".join(f'<span id="{p}c{i}" style="opacity:0">{c if c != " " else "&nbsp;"}</span>' for i, c in enumerate(text))
        self.layers.append(f'<section id="{p}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="7">'
                           f'<div class="pl" id="{p}m"><div class="pl-q">Air tangan isteri = mood terus okay?</div>'
                           f'<div class="pl-o"><i id="{p}y" style="background:{G}"></i><span><b>Setuju</b><b id="{p}yv">0%</b></span></div>'
                           f'<div class="pl-o"><i id="{p}n" style="background:{R}"></i><span><b>Tak setuju</b><b id="{p}nv">0%</b></span></div></div>'
                           f'<div class="cm" id="{p}cm">{self.ico("chat")}<span>{typed}<i class="cm-c" id="{p}cu"></i></span></div>'
                           f'<div class="dn" id="{p}dn">{self.ico("down")}</div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{p}m", {{ y: -60, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.6)" }}, {start:.3f});')
        J(f'tl.fromTo("#{p}y", {{ scaleX: 0 }}, {{ scaleX: 0.9, duration: 1.0, ease: "power2.out" }}, {t_poll:.3f});')
        J(f'tl.fromTo("#{p}n", {{ scaleX: 0 }}, {{ scaleX: 0.1, duration: 1.0, ease: "power2.out" }}, {t_poll:.3f});')
        J(f'const {p}o = {{ v: 0 }}; const {p}e1 = document.getElementById("{p}yv"); const {p}e2 = document.getElementById("{p}nv");')
        J(f'tl.fromTo({p}o, {{ v: 0 }}, {{ v: 1, duration: 1.0, ease: "power2.out", onUpdate: () => {{ {p}e1.textContent = Math.round({p}o.v * 90) + "%"; {p}e2.textContent = Math.round({p}o.v * 10) + "%"; }} }}, {t_poll:.3f});')
        J(f'tl.fromTo("#{p}cm", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2.4)", transformOrigin: "0% 100%" }}, {t_type - 0.3:.3f});')
        for i in range(len(text)):
            J(f'tl.set("#{p}c{i}", {{ opacity: 1 }}, {t_type + i * 0.06:.3f});')
        J(f'tl.fromTo("#{p}dn", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "bounce.out" }}, {t_arrow:.3f});')
        J(f'tl.to("#{p}dn", {{ y: 26, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {t_arrow + 0.4:.3f});')
        J(f'tl.to(["#{p}m", "#{p}cm", "#{p}dn"], {{ opacity: 0, y: -30, duration: 0.25 }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4); self.sfx("riser", t_poll, 0.18, dur=1.0)
        self.sfx("typing", t_type, 0.3, dur=len(text) * 0.06); self.sfx("ping", t_arrow, 0.4)

    # ---- konten 1 ------------------------------------------------------------
    def boxes(self, start, end, steps):
        """steps: [(t, label, icon)] for bekas 1..3"""
        x = self.uid("bx")
        labs = "".join(f'<div id="{x}l{i}">{self.ico(ic)}{esc(t)}</div>' for i, (_, t, ic) in enumerate(steps))
        self.layers.append(f'<section id="{x}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="bx-tr" id="{x}m"><div class="bx-h"><span class="bx-k">Unboxing bekal</span><span class="bx-n" style="position:relative;display:inline-block;min-width:170px;height:44px;text-align:right">'
                           + "".join(f'<span id="{x}n{k}" style="position:absolute;right:0;top:0;white-space:nowrap">{lab}</span>' for k, lab in enumerate(["3 bekas", "1/3", "2/3", "3/3"]))
                           + '</span></div>'
                           f'<div class="bx-bar"><i><b id="{x}b0"></b></i><i><b id="{x}b1"></b></i><i><b id="{x}b2"></b></i></div>'
                           f'<div class="bx-lab">{labs}</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{x}m", {{ y: -80, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }}, {start:.3f});')
        J(f'tl.fromTo("#{x}n0", {{ scale: 2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(3)" }}, {start + 0.2:.3f});')
        J(f'tl.fromTo(["#{x}n1", "#{x}n2", "#{x}n3"], {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, {start:.3f});')
        for i, (t, lab, ic) in enumerate(steps):
            J(f'tl.to("#{x}b{i}", {{ scaleX: 1, duration: 0.45, ease: "power2.out" }}, {t:.3f});')
            J(f'tl.set("#{x}n{i}", {{ opacity: 0 }}, {t:.3f});')
            J(f'tl.fromTo("#{x}n{i + 1}", {{ scale: 1.6, opacity: 1 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(3)", immediateRender: false }}, {t:.3f});')
            if i:
                J(f'tl.to("#{x}l{i - 1}", {{ y: -50, opacity: 0, duration: 0.2, ease: "power2.in" }}, {t - 0.05:.3f});')
            J(f'tl.fromTo("#{x}l{i}", {{ y: 60, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, {t + 0.1:.3f});')
            self.sfx("pop", t, 0.4); self.sfx("ping", t + 0.15, 0.3)
        J(f'tl.to("#{x}m", {{ y: -60, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4)

    def taste(self, start, end, t_pedas, t_manis, t_ok):
        m = self.uid("tt")
        chil = "".join(f'<span class="ico" id="{m}c{i}">{ICON["chili"]}</span>' for i in range(5))
        self.layers.append(f'<section id="{m}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="tt" id="{m}m"><div class="bx-k">Taste test · homemade</div><div class="tt-ok" id="{m}ok">{self.ico("check")}Just nice</div>'
                           f'<div class="tt-r"><b>Pedas</b><div class="tt-c">{chil}</div><div class="tt-v" id="{m}pv">ngam-ngam</div></div>'
                           f'<div class="tt-r"><b>Manis</b><div class="tt-bar"><i id="{m}mb"></i></div><div class="tt-v" id="{m}mv">sikit</div></div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{m}m", {{ x: -1000 }}, {{ x: 0, duration: 0.5, ease: "expo.out" }}, {start:.3f});')
        J(f'tl.fromTo(["#{m}pv", "#{m}mv", "#{m}ok"], {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, {start:.3f});')
        for i in range(3):
            J(f'tl.to("#{m}c{i}", {{ color: "#ff3b3b", scale: 1.25, duration: 0.12 }}, {t_pedas + i * 0.12:.3f});')
            J(f'tl.to("#{m}c{i}", {{ scale: 1, duration: 0.15 }}, {t_pedas + i * 0.12 + 0.12:.3f});')
            self.sfx("click-soft", t_pedas + i * 0.12, 0.35)
        J(f'tl.to("#{m}pv", {{ opacity: 1, duration: 0.2 }}, {t_pedas + 0.4:.3f});')
        J(f'tl.to("#{m}mb", {{ scaleX: 0.3, duration: 0.6, ease: "power2.out" }}, {t_manis:.3f});')
        J(f'tl.to("#{m}mv", {{ opacity: 1, duration: 0.2 }}, {t_manis + 0.3:.3f});')
        J(f'tl.fromTo("#{m}ok", {{ scale: 0 }}, {{ scale: 1, opacity: 1, rotation: -4, duration: 0.35, ease: "back.out(3)" }}, {t_ok:.3f});')
        J(f'tl.to("#{m}m", {{ x: 1000, duration: 0.35, ease: "power3.in" }}, {end - 0.35:.3f});')
        self.sfx("whoosh-short", start, 0.4); self.sfx("whoosh-short", t_manis, 0.3); self.sfx("chime", t_ok, 0.4)

    def overflow(self, start, end, t_full, t_limpah):
        f = self.uid("ov")
        self.layers.append(f'<section id="{f}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="ov" id="{f}m"><div class="ov-k">Isi wrap</div><div class="ov-t"><div class="ov-f" id="{f}f"></div><div class="ov-p" id="{f}p">0%</div></div></div>'
                           f'<div class="st2 y" style="top:500px"><span id="{f}s">Limpah-limpah!</span></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{f}m", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {start:.3f});')
        J(f'tl.fromTo("#{f}f", {{ scaleX: 0 }}, {{ scaleX: 1.12, duration: {max(0.6, t_limpah - t_full):.3f}, ease: "power2.in" }}, {t_full:.3f});')
        J(f'const {f}o = {{ v: 0 }}; const {f}e = document.getElementById("{f}p");')
        J(f'tl.fromTo({f}o, {{ v: 0 }}, {{ v: 120, duration: {max(0.6, t_limpah - t_full):.3f}, ease: "power2.in", onUpdate: () => {{ {f}e.textContent = Math.round({f}o.v) + "%"; }} }}, {t_full:.3f});')
        J(f'tl.fromTo("#{f}s", {{ scale: 0.2, opacity: 0, rotation: 10 }}, {{ scale: 1, opacity: 1, rotation: -4, duration: 0.5, ease: "elastic.out(1, 0.5)" }}, {t_limpah:.3f});')
        J(f'tl.to("#{f}m", {{ keyframes: [{{ x: -10 }}, {{ x: 10 }}, {{ x: -6 }}, {{ x: 0 }}], duration: 0.25 }}, {t_limpah:.3f});')
        J(f'tl.to(["#{f}m", "#{f}s"], {{ opacity: 0, y: -30, duration: 0.25 }}, {end - 0.25:.3f});')
        self.sfx("riser", t_full, 0.2, dur=max(0.6, t_limpah - t_full)); self.sfx("impact-bass-1", t_limpah, 0.4, dur=0.9); self.sfx("pop", t_limpah + 0.05, 0.4)

    def question(self, start, end, t_bujang):
        q = self.uid("qs")
        self.layers.append(f'<section id="{q}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="qs"><div class="qs-k" id="{q}k">{self.ico("chat")}Soalan</div><div class="qs-t" id="{q}t">Untuk<br>bapak-bapak</div>'
                           f'<div class="qs-c" id="{q}c">Bujang, ke tepi sikit</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{q}k", {{ x: -400, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, {start:.3f});')
        J(f'tl.fromTo("#{q}t", {{ opacity: 0, filter: "blur(10px)", y: 30 }}, {{ opacity: 1, filter: "blur(0px)", y: 0, duration: 0.4, ease: "power3.out" }}, {start + 0.2:.3f});')
        J(f'tl.fromTo("#{q}c", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.5)" }}, {t_bujang:.3f});')
        J(f'tl.to("#{q}c", {{ x: 700, rotation: 12, opacity: 0, duration: 0.6, ease: "power3.in" }}, {t_bujang + 1.4:.3f});')
        J(f'tl.to("#{q} .qs > *", {{ opacity: 0, y: -30, duration: 0.25, stagger: 0.04 }}, {end - 0.3:.3f});')
        self.sfx("whoosh-short", start, 0.4); self.sfx("pop", t_bujang, 0.4); self.sfx("whoosh", t_bujang + 1.4, 0.35)

    def mood(self, start, end, t_bad, t_good):
        m = self.uid("mg")
        # semicircle gauge 0 (red, left) .. 180 (green, right); needle pivot at (400, 330)
        cx, cy, r = 400, 300, 210
        arc = f"M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}"
        self.layers.append(f'<section id="{m}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="mg" id="{m}m"><div class="mg-h">Mood meter</div><svg width="800" height="420" viewBox="0 0 800 420">'
                           f'<defs><linearGradient id="{m}g" x1="0" x2="1"><stop offset="0" stop-color="{R}"/><stop offset="0.5" stop-color="{Y}"/><stop offset="1" stop-color="{G}"/></linearGradient></defs>'
                           f'<path d="{arc}" fill="none" stroke="url(#{m}g)" stroke-width="38" stroke-linecap="round"/>'
                           f'<g id="{m}n"><line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 180}" stroke="#fff" stroke-width="12" stroke-linecap="round"/></g>'
                           f'<circle cx="{cx}" cy="{cy}" r="24" fill="#fff"/></svg>'
                           f'<div class="mg-l" style="left:40px;color:{R}">Tak okay</div><div class="mg-l" style="right:40px;color:{G}">Okay!</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{m}m", {{ y: -80, opacity: 0, scale: 0.85 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.8)" }}, {start:.3f});')
        J(f'tl.fromTo("#{m}n", {{ rotation: -20, svgOrigin: "{cx} {cy}" }}, {{ rotation: -75, duration: 0.5, ease: "power2.out", svgOrigin: "{cx} {cy}" }}, {t_bad:.3f});')
        J(f'tl.to("#{m}n", {{ rotation: 72, duration: 0.9, ease: "elastic.out(1, 0.45)", svgOrigin: "{cx} {cy}" }}, {t_good:.3f});')
        J(f'tl.to("#{m}m", {{ borderColor: "{G}", duration: 0.3 }}, {t_good + 0.3:.3f});')
        J(f'tl.to("#{m}m", {{ y: -60, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4); self.sfx("error", t_bad, 0.2, dur=0.5)
        self.sfx("riser", t_good - 0.2, 0.18, dur=0.4); self.sfx("chime", t_good + 0.2, 0.45)

    # ---- konten 2 ------------------------------------------------------------
    def price_hook(self, start, dur):
        h = self.uid("ph")
        self.layers.append(f'<section id="{h}" class="clip" data-start="{start:.3f}" data-duration="{dur:.3f}" data-track-index="5">'
                           f'<div class="h2-sh"></div><div class="hk"><div class="hk-k" id="{h}k">Lain dari yang lain</div>'
                           f'<div class="hk-a" id="{h}a" style="font-size:120px">Cuba colour</div>'
                           f'<div class="pt" style="position:relative;top:0;margin-top:10px"><div class="pt-tag" id="{h}t"><i></i>Mahal</div></div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{h}k", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.3 }}, {start:.3f});')
        J(f'tl.fromTo("#{h}a", {{ scale: 1.5, opacity: 0, filter: "blur(10px)" }}, {{ scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.35, ease: "power4.out" }}, {start + 0.15:.3f});')
        J(f'tl.fromTo("#{h}t", {{ rotation: -70, y: -200, opacity: 0 }}, {{ rotation: 0, y: 0, opacity: 1, duration: 0.9, ease: "elastic.out(1, 0.35)" }}, {start + 0.5:.3f});')
        J(f'tl.to("#{h} .hk > *", {{ opacity: 0, y: -30, filter: "blur(8px)", duration: 0.25, stagger: 0.05 }}, {start + dur - 0.35:.3f});')
        J(f'tl.to("#{h} .h2-sh", {{ opacity: 0, duration: 0.3 }}, {start + dur - 0.3:.3f});')
        self.sfx("whoosh", start, 0.45); self.sfx("impact-bass-1", start + 0.2, 0.45, dur=1.0); self.sfx("click", start + 0.55, 0.4)

    def swatches(self, start, end, t_pink, t_grey, cols=(("Pink", "#f2a7bd"), ("Grey", "#8e9399"))):
        s = self.uid("sw")
        cards = "".join(f'<div class="sw-c" id="{s}c{i}"><i style="background:{c}"></i><b>{n}</b><span>Jotun</span></div>' for i, (n, c) in enumerate(cols))
        self.layers.append(f'<section id="{s}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="sw">{cards}<div class="st2 y" style="top:-10px"><span id="{s}k" style="font-size:40px;padding:6px 20px;border-width:4px">2 colour</span></div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{s}k", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, rotation: -3, duration: 0.35, ease: "back.out(3)" }}, {start:.3f});')
        J(f'tl.fromTo("#{s}c0", {{ y: 600, rotation: 0, opacity: 0 }}, {{ y: 30, rotation: -12, x: -110, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }}, {t_pink:.3f});')
        J(f'tl.fromTo("#{s}c1", {{ y: 600, rotation: 0, opacity: 0 }}, {{ y: 30, rotation: 12, x: 110, opacity: 1, duration: 0.6, ease: "back.out(1.6)" }}, {t_grey:.3f});')
        J(f'tl.to(["#{s}c0", "#{s}c1", "#{s}k"], {{ y: 700, opacity: 0, duration: 0.4, ease: "power3.in", stagger: 0.05 }}, {end - 0.45:.3f});')
        self.sfx("pop", start, 0.35); self.sfx("whoosh-short", t_pink, 0.4); self.sfx("whoosh-short", t_grey, 0.4)

    def bancuh(self, start, end, t_go, t_done):
        c = self.uid("bc")
        self.layers.append(f'<section id="{c}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="bc" id="{c}m"><div class="bc-b"><span class="ico">{ICON["bucket"]}</span><div class="bc-sw" id="{c}s"></div></div>'
                           f'<div class="bc-r"><div class="bc-t">Proses bancuh cat</div><div class="bc-s">Tinting machine · Jotun Subang</div>'
                           f'<div class="bc-p"><i id="{c}p"></i></div></div><div class="bc-ok" id="{c}ok">{self.ico("check")}Settle</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{c}m", {{ y: -80, opacity: 0, scale: 0.9 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.45, ease: "back.out(1.8)" }}, {start:.3f});')
        J(f'tl.fromTo("#{c}s", {{ rotation: 0 }}, {{ rotation: {int((t_done - t_go) * 360)}, duration: {t_done - t_go:.3f}, ease: "none" }}, {t_go:.3f});')
        J(f'tl.fromTo("#{c}p", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {t_done - t_go:.3f}, ease: "power1.inOut" }}, {t_go:.3f});')
        J(f'tl.fromTo("#{c}ok", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, rotation: -4, duration: 0.35, ease: "back.out(3)" }}, {t_done:.3f});')
        J(f'tl.to("#{c}m", {{ y: -60, opacity: 0, duration: 0.25, ease: "power2.in" }}, {end - 0.25:.3f});')
        self.sfx("whoosh-short", start, 0.4); self.sfx("riser", t_go, 0.15, dur=min(2.5, t_done - t_go)); self.sfx("chime", t_done, 0.45)

    def nextup(self, start, end, kicker, title, icon="bolt"):
        n = self.uid("nx")
        self.layers.append(f'<section id="{n}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="6">'
                           f'<div class="nx"><div class="nx-k" id="{n}k">{esc(kicker)}</div><div class="nx-t" id="{n}t"><span class="ico" id="{n}i">{ICON[icon]}</span>{esc(title)}</div></div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{n}k", {{ x: -600 }}, {{ x: 0, duration: 0.4, ease: "expo.out" }}, {start:.3f});')
        J(f'tl.fromTo("#{n}t", {{ opacity: 0, scaleX: 1.5, filter: "blur(10px)" }}, {{ opacity: 1, scaleX: 1, filter: "blur(0px)", duration: 0.45, ease: "expo.out" }}, {start + 0.15:.3f});')
        J(f'tl.to("#{n}i", {{ keyframes: [{{ opacity: 0.2 }}, {{ opacity: 1 }}, {{ opacity: 0.3 }}, {{ opacity: 1 }}], duration: 0.4, ease: "none" }}, {start + 0.5:.3f});')
        J(f'tl.to("#{n} .nx > *", {{ opacity: 0, y: -30, duration: 0.25, stagger: 0.05 }}, {end - 0.3:.3f});')
        self.sfx("whoosh-short", start, 0.4); self.sfx("click", start + 0.5, 0.35)

    def comment_ask(self, start, end, text, t_type):
        p = self.uid("ca")
        typed = "".join(f'<span id="{p}c{i}" style="opacity:0">{c if c != " " else "&nbsp;"}</span>' for i, c in enumerate(text))
        self.layers.append(f'<section id="{p}" class="clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="7">'
                           f'<div class="cm" id="{p}cm" style="top:300px">{self.ico("chat")}<span>{typed}<i class="cm-c"></i></span></div>'
                           f'<div class="dn" id="{p}dn">{self.ico("down")}</div></section>')
        J = self.js.append
        J(f'tl.fromTo("#{p}cm", {{ scale: 0, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.35, ease: "back.out(2.4)", transformOrigin: "0% 100%" }}, {start:.3f});')
        for i in range(len(text)):
            J(f'tl.set("#{p}c{i}", {{ opacity: 1 }}, {t_type + i * 0.06:.3f});')
        J(f'tl.fromTo("#{p}dn", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "bounce.out" }}, {t_type + len(text) * 0.06:.3f});')
        J(f'tl.to("#{p}dn", {{ y: 26, duration: 0.3, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {t_type + len(text) * 0.06 + 0.4:.3f});')
        J(f'tl.to(["#{p}cm", "#{p}dn"], {{ opacity: 0, y: -30, duration: 0.25 }}, {end - 0.25:.3f});')
        self.sfx("pop", start, 0.35); self.sfx("typing", t_type, 0.3, dur=len(text) * 0.06); self.sfx("ping", t_type + len(text) * 0.06, 0.35)


gen.CSS += r"""
/* transitions */
.tw { position: absolute; top: -40px; bottom: -40px; left: 0; width: 1400px; background: #f5c22e; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; }
.tw-k { font-weight: 800; font-size: 44px; letter-spacing: 0.2em; text-transform: uppercase; color: #15171a; opacity: 0.7; padding-right: 320px; }
.tw-t { font-weight: 800; font-size: 120px; line-height: 0.95; text-transform: uppercase; color: #15171a; text-align: center; padding-right: 320px; }
.tw2 { position: absolute; top: -40px; bottom: -40px; left: 0; width: 1400px; background: #15171a; }
.tdip { position: absolute; inset: 0; background: #000; }
.tzf { position: absolute; inset: 0; background: radial-gradient(circle at 50% 45%, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.6) 35%, rgba(255,255,255,0) 70%); }
.trgb { position: absolute; inset: 0; mix-blend-mode: screen; background: linear-gradient(0deg, rgba(255,0,60,0.35) 0 9%, transparent 9% 33%, rgba(0,255,255,0.3) 33% 39%, transparent 39% 64%, rgba(255,0,60,0.3) 64% 69%, transparent 69% 86%, rgba(0,255,255,0.25) 86% 90%, transparent 90%); }
"""


def _trans(self, t, kind, kicker=None, title=None):
    """Section transition centred on cut time t. kinds: wipe (yellow panel + label), zoom (zoom through), whip, glitch, dip."""
    k = self.uid("tr")
    J = self.js.append
    if kind == "wipe":
        lab = f'<div class="tw-k">{esc(kicker or "")}</div><div class="tw-t">{title or ""}</div>' if title else ""
        self.layers.append(f'<section id="{k}" class="clip" data-start="{t - 0.45:.3f}" data-duration="1.55" data-track-index="7">'
                           f'<div class="tw2" id="{k}b"></div><div class="tw" id="{k}p">{lab}</div></section>')
        J(f'tl.fromTo("#{k}b", {{ x: -1450 }}, {{ x: 0, duration: 0.4, ease: "power3.in" }}, {t - 0.45:.3f});')
        J(f'tl.fromTo("#{k}p", {{ x: -1450 }}, {{ x: 0, duration: 0.42, ease: "power3.in" }}, {t - 0.4:.3f});')
        if title:
            J(f'tl.fromTo("#{k} .tw-t", {{ scale: 1.4, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {t - 0.05:.3f});')
            J(f'tl.fromTo("#{k} .tw-k", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 0.7, duration: 0.25 }}, {t:.3f});')
        J(f'tl.to("#{k}p", {{ x: 1450, duration: 0.42, ease: "power3.in" }}, {t + 0.6:.3f});')
        J(f'tl.to("#{k}b", {{ x: 1450, duration: 0.42, ease: "power3.in" }}, {t + 0.66:.3f});')
        self.sfx("whoosh-cinematic", t - 0.5, 0.45)
        self.sfx("impact-bass-1", t - 0.02, 0.45, dur=1.0)
        self.sfx("whoosh", t + 0.6, 0.35)
    elif kind == "zoom":
        self.layers.append(f'<section id="{k}" class="clip" data-start="{t - 0.25:.3f}" data-duration="0.6" data-track-index="7"><div class="tzf" id="{k}f"></div></section>')
        J(f'tl.to("#acam", {{ scale: 1.55, duration: 0.25, ease: "power3.in" }}, {t - 0.25:.3f});')
        J(f'tl.fromTo("#acam", {{ scale: 1.4 }}, {{ scale: 1, duration: 0.4, ease: "expo.out", immediateRender: false }}, {t:.3f});')
        J(f'tl.fromTo("#{k}f", {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.25 }}, {{ opacity: 0, duration: 0.35 }}], ease: "none" }}, {t - 0.25:.3f});')
        self.sfx("whoosh-short", t - 0.3, 0.4)
        self.sfx("impact-bass-2", t, 0.4, dur=0.9)
    elif kind == "whip":
        self.layers.append(f'<section id="{k}" class="clip" data-start="{t - 0.2:.3f}" data-duration="0.45" data-track-index="7"><div class="ef" id="{k}x"></div></section>')
        J(f'tl.to("#acam", {{ x: -700, duration: 0.18, ease: "power2.in" }}, {t - 0.18:.3f});')
        J(f'tl.fromTo("#acam", {{ x: 700 }}, {{ x: 0, duration: 0.26, ease: "power3.out", immediateRender: false }}, {t:.3f});')
        J(f'tl.fromTo("#{k}x", {{ x: -1200 }}, {{ x: 1200, duration: 0.4, ease: "power2.inOut" }}, {t - 0.2:.3f});')
        self.sfx("whoosh", t - 0.22, 0.45)
    elif kind == "glitch":
        self.layers.append(f'<section id="{k}" class="clip" data-start="{t - 0.1:.3f}" data-duration="0.5" data-track-index="7"><div class="trgb" id="{k}g"></div></section>')
        J(f'tl.fromTo("#{k}g", {{ opacity: 0, y: 0 }}, {{ keyframes: [{{ opacity: 1, y: -50 }}, {{ opacity: 0.3, y: 70 }}, {{ opacity: 1, y: -110 }}, {{ opacity: 0.4, y: 30 }}, {{ opacity: 0, y: 0 }}], duration: 0.45, ease: "none" }}, {t - 0.1:.3f});')
        J(f'tl.to("#acam", {{ keyframes: [{{ x: -30, rotation: -1.4 }}, {{ x: 26, rotation: 1.1 }}, {{ x: -16, rotation: -0.6 }}, {{ x: 8, rotation: 0.2 }}, {{ x: 0, rotation: 0 }}], duration: 0.42, ease: "none" }}, {t - 0.05:.3f});')
        self.sfx("glitch-short", t - 0.1, 0.35)
        self.sfx("impact-bass-2", t + 0.05, 0.35, dur=0.8)
    elif kind == "dip":
        self.layers.append(f'<section id="{k}" class="clip" data-start="{t - 0.22:.3f}" data-duration="0.55" data-track-index="7"><div class="tdip" id="{k}d"></div></section>')
        J(f'tl.fromTo("#{k}d", {{ opacity: 0 }}, {{ keyframes: [{{ opacity: 1, duration: 0.22, ease: "power2.in" }}, {{ opacity: 0, duration: 0.33, ease: "power2.out" }}] }}, {t - 0.22:.3f});')
        self.sfx("whoosh-short", t - 0.25, 0.3)


V21.trans = _trans
