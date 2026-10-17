"""Video 1: Beg Gucci versi contractor."""
import sys
sys.path.insert(0, "/home/user/Hyperframes/raw/scripts")
from gen import Comp
from common import load_words, load_segs, tag_span, jump_cuts, find

E = "/home/user/Hyperframes/raw/edit/"
F = "../assets/footage/"
segs = load_segs(E + "v1_segs.json")
words = load_words(E + "v1_tx/transcript.json")
for i, w in enumerate(words):  # whisper slips: "So kali ni" heard as "So kalau ni"
    if w[0].lower() == "kalau" and 0 < i < len(words) - 1 and words[i - 1][0].lower() == "so" and words[i + 1][0].lower() == "ni":
        w[0] = "kali"
A = segs["duration"]
END = 3.2
c = Comp("v1-gucci", A + END)

# A-roll, with alternating punch-in on every jump cut inside a piece
scale, cuts = 1.0, [(0.0, 1.0)]
for t, same_piece in jump_cuts(segs):
    scale = (1.12 if scale == 1.0 else 1.0) if same_piece else 1.0
    cuts.append((t, scale))
c.aroll(F + "aroll_v1.mp4", [(0.0, A, 0.0)], cuts_scale=cuts)

h0, h1 = tag_span(segs, "hook")
s0, s1 = tag_span(segs, "setup")
p0, p1 = tag_span(segs, "problem")
l0, l1 = tag_span(segs, "lostlaser")
u0, u1 = tag_span(segs, "upgrade")
b0, b1 = tag_span(segs, "bosch")
t0, t1 = tag_span(segs, "types")
k0, k1 = tag_span(segs, "keep")

c.shade(0.0, A + END)

# Hook
c.hook(["Beg Gucci", "versi contractor 😍"], 0.05, max(3.0, h1 - 0.1))
c.sfx("glitch-1", 0.0, 0.35)

# Setup: GUCCI / LV struck out, then tools
g = find(words, "Gucci", s0)
lv = find(words, "LV", s0)
c.strike("GUCCI", g - 0.1, lv - g + 0.1, strike_at=g + 0.5, y=330)
c.strike("LV", lv, 1.5, strike_at=lv + 0.45, y=330)
con = find(words, "contractor", s0)
# "...terliur tengok apa tau, benda ni guys": cut to the Milwaukee close-up he points at
tr = find(words, "terliur", con)
c.broll(F + "IMG_5105.mp4", tr, s1 - tr + 0.4, media_start=16.8, zoom=(1.0, 1.12))
c.chip("🔧 Contractor terliur tengok ni", con, s1 - con + 0.2, x=70, y=330, yellow=True)

# Problem: tape b-roll and counter
tp = find(words, "tape", p0)
c.broll(F + "IMG_5107.mp4", tp - 0.1, 2.6, media_start=2.0, zoom=(1.0, 1.12))
hl = find(words, "hilang", p0)
c.chip("Tape hilang lagi 😩", hl, p1 - hl + 0.1, x=70, y=330, yellow=True, sfx="error")
hl2 = find(words, "hilang", l0)
c.chip("Laser pun hilang 🤦", hl2, l1 - hl2 + 0.1, x=70, y=330, sfx="error")

# Upgrade: laser measure graphic
LZ = min(5.2, u1 - u0 + 0.6)
c.laser(u0, LZ)

# Bosch pick
bo = find(words, "Bosch", b0)
c.chip("Pilihan aku: Bosch ✅", bo, b1 - bo + 0.2, x=70, y=330, yellow=True)

# Types comparison
c.vs(("Tape + laser", "Tape biasa ada laser"), ("Laser je", "Ukur jarak terus"), t0 + 0.2, min(6.0, t1 - t0 - 0.2))

# Bought
c.broll(F + "IMG_5108.mp4", k0, k1 - k0 + 0.4, media_start=0.3, zoom=(1.0, 1.1))
c.chip("Dah beli ✅", k0 + 0.1, k1 - k0 + 0.2, x=70, y=330, yellow=True, sfx="chime")

# CTA end card over the tool wall
c.broll(F + "IMG_5105.mp4", A, END, media_start=19.5, zoom=(1.05, 1.15))
c.endcard(A, END, '<span class="ln">Korang team</span><em class="ln">tape</em><span class="ln">atau</span><em class="ln">laser?</em>',
          "Komen bawah 👇")

c.captions(words, hide=[(A, A + END), (u0, u0 + LZ)])
c.write("/home/user/Hyperframes/compositions/v1-gucci.html", "Video 1: Beg Gucci versi contractor")
