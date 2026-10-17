"""Video 2: Datin nak buat klinik 3 tingkat (vlog, one complete story)."""
import sys
sys.path.insert(0, "/home/user/Hyperframes/raw/scripts")
from gen import Comp
from common import load_words, load_segs, find

E = "/home/user/Hyperframes/raw/edit/"
F = "../assets/footage/"
segs = load_segs(E + "v2_segs.json")
raw_words = load_words(E + "v2_tx/transcript.json")

# Pure b-roll gaps inserted after a tag (seconds)
GAP_AFTER = {"jom": 0.0, "pitstop": 3.6, "site": 9.0}
END = 3.0

# Place every A-roll cut on the composition timeline
place, t, last_tag = [], 0.0, None
tag_start = {}
for s in segs["segments"]:
    if last_tag is not None and s["tag"] != last_tag:
        t += GAP_AFTER.get(last_tag, 0.0)
    d = s["out_out"] - s["out_in"]
    tag_start.setdefault(s["tag"], t)
    place.append((t, d, s["out_in"], s))
    t += d
    last_tag = s["tag"]
A = t
tag_end = {}
for st, d, ms, s in place:
    tag_end[s["tag"]] = st + d

def to_comp(at):
    for st, d, ms, s in place:
        if ms - 1e-3 <= at < ms + d + 1e-3:
            return st + (at - ms)
    return None

fixed = []
for i, w in enumerate(raw_words):  # "on the way" heard as "orang dua"
    if w[0].lower() == "dua" and i and raw_words[i - 1][0].lower() == "orang":
        continue
    if w[0].lower() == "orang" and i + 1 < len(raw_words) and raw_words[i + 1][0].lower() == "dua":
        w = ["on the way", w[1], raw_words[i + 1][2]]
    fixed.append(w)
words = []
for w, a, b in fixed:
    ca = to_comp(a)
    if ca is not None:
        words.append([w, ca, ca + (b - a)])

c = Comp("v2-klinik", A + END)

# A-roll with punch-in alternation on jump cuts
cuts, scale, prev = [], 1.0, None
for st, d, ms, s in place:
    same = prev is not None and prev["piece"] == s["piece"] and abs(st - (prev_end)) < 1e-3
    scale = (1.12 if scale == 1.0 else 1.0) if same else 1.0
    cuts.append((st, scale)); prev = s; prev_end = st + d
c.aroll(F + "aroll_v2.mp4", [(st, d, ms) for st, d, ms, s in place], cuts_scale=cuts)
c.shade(0.0, A + END)

# Hook: on site
h0, h1 = tag_start["hook"], tag_end["hook"]
c.hook(["Datin nak buat", "klinik 3 tingkat 🏥"], 0.05, max(3.0, h1 - 0.1))

# Intro
i0, i1 = tag_start["intro"], tag_end["intro"]
jr = find(words, "jerebu", i0)
c.chip("Jerebu teruk 😷", jr, 2.4, x=70, y=330)
sb = find(words, "Subang", i0)
c.chip("📍 Subang", sb, 2.2, x=70, y=330, yellow=True)
dt = find(words, "Datin", i0)
c.broll(F + "IMG_5111.mp4", dt, 3.2, media_start=0.3, zoom=(1.12, 1.0))
c.chip("Klinik · 3 tingkat", dt + 0.6, 2.6, x=70, y=330, yellow=True)
j0 = tag_start["jom"]
c.chip("Pit stop dulu 🔧", j0, 1.6, x=70, y=330, yellow=True)

# Pit stop montage over the voice + gap
p0 = tag_start["pitstop"]; pend = tag_end["pitstop"] + GAP_AFTER["pitstop"]
shots = [("IMG_5103.mp4", 0.5), ("IMG_5104.mp4", 1.0), ("IMG_5105.mp4", 20.0), ("IMG_5107.mp4", 9.0), ("IMG_5108.mp4", 0.3)]
seg_len = (tag_end["pitstop"] - p0) / len(shots)
for i, (f, ms) in enumerate(shots):
    c.broll(F + f, p0 + i * seg_len, seg_len, media_start=ms, zoom=(1.0, 1.1))
    if i:
        c.sfx("whoosh-short", p0 + i * seg_len, 0.35)
c.sfx("chime", tag_end["pitstop"] - seg_len + 0.3, 0.35)
# Arrival (gap after pitstop)
g0 = tag_end["pitstop"]
c.broll(F + "IMG_5111.mp4", g0, 2.2, media_start=4.5, zoom=(1.0, 1.08))
c.broll(F + "IMG_5118.mp4", g0 + 2.2, 1.4, media_start=0.5, zoom=(1.0, 1.08))
c.chip("Sampai site 📍", g0 + 0.1, 3.3, x=70, y=330, yellow=True, sfx="whoosh")

# Site visit callouts
s0, s1 = tag_start["site"], tag_end["site"]
c.chip("Tingkat 1", s0 + 0.2, 2.0, x=70, y=330, yellow=True)
lf = find(words, "lift", s0)
c.tag("Ada lift", lf, 2.0, 70, 1480)
wr = find(words, "wiring", s0)
c.image(F + "db_box.jpg", wr, 2.4, zoom=(1.0, 1.12))
c.tag("Wiring: full rewire", wr + 0.2, 3.4, 70, 1480, icon="!", warn=True)
em = find(words, "Emergency", s0)
c.tag("Emergency exit", em, 1.8, 70, 1480)
tl_ = find(words, "toilet", em)
c.tag("2 toilet", tl_, s1 - tl_ + 0.2, 70, 1480)

# Upper floors and finished-result montage (gap after site)
u0 = s1
c.broll(F + "IMG_5128.mp4", u0, 1.8, media_start=1.5, zoom=(1.0, 1.08))
c.broll(F + "IMG_5122.mp4", u0 + 1.8, 2.2, media_start=14.0, zoom=(1.0, 1.1))
c.chip("Tingkat 2 & 3", u0 + 0.1, 3.8, x=70, y=330, yellow=True, sfx="whoosh")
r0 = u0 + 4.0
res = [("7695A0AD.mp4", 1.0), ("IMG_4940.mp4", 0.5), ("b6f67f16.mp4", 3.0), ("IMG_2531.mp4", 2.0)]
for i, (f, ms) in enumerate(res):
    c.broll(F + f, r0 + i * 1.25, 1.25, media_start=ms, zoom=(1.08, 1.0))
    c.sfx("whoosh-short", r0 + i * 1.25, 0.3)
c.chip("Contoh projek kami ✨", r0 + 0.1, 4.8, x=70, y=330, yellow=True, sfx="sparkle")

# End card
c.broll(F + "7695A0AD.mp4", A, END, media_start=3.0, zoom=(1.0, 1.08))
c.endcard(A, END, '<span class="ln">Nak renovate klinik?</span><em class="ln">DM aku</em>', "Follow untuk projek seterusnya")

c.captions(words, hide=[(A, A + END)])
c.write("/home/user/Hyperframes/compositions/v2-klinik.html", "Video 2: Datin nak buat klinik 3 tingkat")
