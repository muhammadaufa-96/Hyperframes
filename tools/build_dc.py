"""Klinik Rasa Sihat (folder DC): four short-form edits.

usage: python3 build_dc.py [1|2|3|4 ...]
Footage lives in assets/footage/dc/ (SDR proxies, A-rolls); music in assets/dc/.
"""
import json, subprocess, sys
sys.path.insert(0, "/home/user/Hyperframes/raw/scripts")
from gen import Comp
from common import load_words_dc, map_words

DC = "/home/user/Hyperframes/dc/"
F = "../assets/footage/dc/"
LOGO = "../assets/brand/enoxin-logo-white.png"
MUSIC = "../assets/dc/music_best_morning.m4a"
BEAT0, BEAT = 6.27, 0.86  # first strong beat in the track and beat length (s)
END_Q = '<span class="ln">Nak set up klinik</span><span class="ln">GP / estetik / dental?</span><em class="ln">DM kami</em>'
END_SUB = "Konsultasi percuma"


def music_bed(name, dur):
    """Trim the track from the first strong beat, fade in/out, return the composition path."""
    out = f"/home/user/Hyperframes/assets/dc/{name}.m4a"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{BEAT0}", "-t", f"{dur:.3f}", "-i",
                    "/home/user/Hyperframes/assets/dc/music_best_morning.m4a", "-af",
                    f"afade=t=in:d=0.3,afade=t=out:st={dur - 2.0:.3f}:d=2.0", "-c:a", "aac", "-b:a", "192k", out], check=True)
    return f"../assets/dc/{name}.m4a"


def tag_span(segs, tag):
    s = [x for x in segs["segments"] if x["tag"].split(":")[0] == tag]
    return s[0]["out_in"], s[-1]["out_out"]


def find(words, token, after=0.0):
    for w in words:
        if w[1] >= after and w[0].lower().strip(".,?!") == token.lower():
            return w[1]
    raise KeyError(token)


def punch(c, segs, origins, offset=0.0):
    """One framing per cut: talking speaker gets a gentle punch-in toward where they stand."""
    for s in segs["segments"]:
        key = s["tag"].split(":")[0]
        scale, origin = origins.get(key, origins.get("*", (1.0, "50% 50%")))
        c.js.append(f'tl.set("#acam", {{ scale: {scale}, transformOrigin: "{origin}" }}, {s["out_in"] + offset:.3f});')


def v1():
    segs = json.load(open(DC + "edit/v1_segs.json"))
    words = map_words({
        "fb": load_words_dc(DC + "tx/IMG_4935_tail/transcript.json", offset=405 - 515),
        "IMG_4945": load_words_dc(DC + "tx/IMG_4945/transcript.json"),
    }, segs)
    A = segs["duration"]; END = 3.6
    c = Comp("dc1-feedback", A + END)
    c.aroll(F + "aroll_dc1.mp4", [(0.0, A, 0.0)])
    cl, me = (1.35, "82% 40%"), (1.35, "48% 40%")
    origins = {k: cl for k in ("hook", "a1", "a1b", "a2", "a3", "a4")}
    origins.update({k: me for k in ("q1", "r1", "q2", "q3", "r4", "doa")})
    origins["cta"] = (1.0, "50% 50%")
    punch(c, segs, origins)
    c.shade(0, A + END)

    h0, h1 = tag_span(segs, "hook")
    # camera was panned to the waiting area while he said this: show what he is praising
    c.broll(F + "IMG_4944.mp4", h0, h1 - h0, media_start=0.2, zoom=(1.0, 1.1))
    c.hook(["Apa kata klien", "lepas klinik siap? 🏥"], 0.05, max(3.0, h1 + 0.6))
    a0, a1e = tag_span(segs, "a1")
    c.name("Dr. Rafhan", "Klinik Rasa Sihat", a0, 3.2)
    # quiet cutaways while the client praises the result
    c.broll(F + "IMG_4944.mp4", a1e - 1.8, 1.8, media_start=0.3, zoom=(1.0, 1.08))
    b0, b1 = tag_span(segs, "a2")
    c.broll(F + "IMG_4940.mp4", b0, b1 - b0, media_start=0.3, zoom=(1.08, 1.0))
    l0, l1 = tag_span(segs, "a3")
    try:
        lj = find(words, "laju", l0)
        c.label("Laju ⚡", lj, l1 - lj + 0.3, top=300)
    except KeyError:
        pass
    p0, p1 = tag_span(segs, "a4")
    c.label("Puas hati ✅", p0 + 0.3, p1 - p0 + 0.6, top=300)
    k0, k1 = tag_span(segs, "cta")
    c.label("Konsultasi percuma", k0 + 0.3, k1 - k0 - 0.3, top=300)

    c.broll(F + "IMG_4944.mp4", A, END, media_start=0.5, zoom=(1.0, 1.08))
    c.endcard(A, END, END_Q, END_SUB, logo=LOGO)
    c.captions_min(words, hide=[(A, A + END)])
    c.write("/home/user/Hyperframes/compositions/dc1-feedback.html", "DC 1: Feedback Dr. Rafhan")


def v2():
    segs = json.load(open(DC + "edit/v2_segs.json"))
    words = map_words({
        "IMG_4924": load_words_dc(DC + "tx/IMG_4924/transcript.json"),
        "IMG_4945": load_words_dc(DC + "tx/IMG_4945/transcript.json"),
    }, segs)
    H = 4.3  # car hook before the A-roll starts
    A = segs["duration"]; END = 3.6
    c = Comp("dc2-sitevisit", H + A + END)
    c.aroll(F + "aroll_dc2.mp4", [(H, A, 0.0)])
    c.broll(F + "IMG_4917.mp4", 0.0, H, media_start=0.3, zoom=(1.0, 1.06))
    c.shade(0, H + A + END)
    c.hook(["Klinik ni dah siap", "Jom tengok hasilnya 👀"], 0.1, H - 0.2)
    words = [[w, a + H, b + H, s] for w, a, b, s in words]
    T = lambda tag: tuple(x + H for x in tag_span(segs, tag))

    i0, i1 = T("intro")
    c.label("📍 Klinik Rasa Sihat", i0 + 0.3, 3.5)
    try:
        ins = find(words, "inspection", i0)
        c.label("Inspection lulus ✅", ins, i1 - ins)
    except KeyError:
        pass
    w0, _ = T("waiting"); c.label("Ruang menunggu", w0 + 0.2, 4.0)
    k0, k1 = T("cabinet"); c.label("Kabinet & dispenser", k0 + 0.2, 4.0)
    c.broll(F + "IMG_4948.mp4", k0 + 4.0, min(3.0, k1 - k0 - 4.0), media_start=2.5, zoom=(1.0, 1.1))
    d0, d1 = T("doctor"); c.label("Bilik doktor", d0 + 0.2, d1 - d0)
    c.broll(F + "IMG_4949.mp4", d0 + 1.0, d1 - d0 - 0.8, media_start=0.5, zoom=(1.0, 1.08))
    u0, _ = T("utility"); c.label("Utility & staff toilet", u0 + 0.2, 4.0)
    t0, t1 = T("toilet"); c.label("Toilet pesakit", t0 + 0.2, t1 - t0)
    c.broll(F + "IMG_4950.mp4", t0 + 1.5, t1 - t0 - 1.2, media_start=1.0, zoom=(1.0, 1.08))
    o0, o1 = T("outside")
    try:
        ss = find(words, "screenshot", o0) - 0.2
    except KeyError:
        ss = o1 - 4.0
    c.screenshot("../assets/dc/whatsapp_crop.jpg", ss, o1 - ss + 0.6,
                 highlights=[(81, 171, 585, 70, ss + 0.7), (81, 728, 547, 164, ss + 1.6), (81, 1134, 616, 242, ss + 2.5)])
    q0, q1 = T("cta"); c.label("Konsultasi percuma", q0 + 0.3, q1 - q0 - 0.3)

    c.broll(F + "IMG_4944.mp4", H + A, END, media_start=0.5, zoom=(1.0, 1.08))
    c.endcard(H + A, END, END_Q, END_SUB, logo=LOGO)
    c.captions_min(words, hide=[(H + A, H + A + END), (ss, o1 + 0.6)])
    c.write("/home/user/Hyperframes/compositions/dc2-sitevisit.html", "DC 2: Dari kereta ke klinik siap")


TOUR = [  # (clip, media_start, label or None)
    ("IMG_4924", 7.0, "Klinik Rasa Sihat"),
    ("IMG_4924", 14.5, None),
    ("IMG_4940", 0.3, "Kaunter registration"),
    ("IMG_4944", 0.0, "Ruang menunggu"),
    ("IMG_4940", 5.0, None),
    ("IMG_4949", 0.5, "Bilik konsultasi"),
    ("IMG_4940", 12.0, "Bilik rawatan"),
    ("IMG_4943", 0.2, "Dispensary"),
    ("IMG_4943", 11.0, None),
    ("IMG_4950", 2.5, "Toilet pesakit"),
    ("IMG_4951", 3.0, "Pantry staf"),
    ("IMG_4948", 2.0, "Kabinet custom"),
]


def v3():
    shot = 3 * BEAT
    END = 5 * BEAT
    total = len(TOUR) * shot + END
    c = Comp("dc3-tour", total)
    for i, (clip, ms, lab) in enumerate(TOUR):
        t = i * shot
        z = (1.0, 1.1) if i % 2 == 0 else (1.1, 1.0)
        c.broll(F + clip + ".mp4", t, shot, media_start=ms, zoom=z)
        if lab and i:
            c.label(lab, t + 0.1, shot - 0.1, top=1500)
        if i:
            c.sfx("whoosh-short", t, 0.25)
    c.shade(0, total)
    c.hook(["Shoplot → klinik siap", "Tengok hasilnya ✨"], 0.1, 2 * shot - 0.2, sfx=False)
    c.broll(F + "IMG_4944.mp4", len(TOUR) * shot, END, media_start=0.5, zoom=(1.0, 1.08))
    c.endcard(len(TOUR) * shot, END, END_Q, END_SUB, logo=LOGO)
    c.music(music_bed("music_dc3", total), 0.0, total, vol=0.85)
    c.write("/home/user/Hyperframes/compositions/dc3-tour.html", "DC 3: Tour Klinik Rasa Sihat")


TEASER = [  # (clip, media_start, beats)
    ("greet", 0.0, 4),
    ("IMG_4948", 3.0, 2),
    ("IMG_4951", 3.5, 2),
    ("IMG_4949", 1.0, 2),
    ("IMG_4950", 0.8, 2),
    ("IMG_4951", 8.0, 2),
    ("IMG_4944", 0.5, 3),
    ("IMG_4943", 11.0, 2),
]


def v4():
    END = 5 * BEAT
    t, cuts = 0.0, []
    for clip, ms, n in TEASER:
        cuts.append((clip, ms, t, n * BEAT)); t += n * BEAT
    total = t + END
    c = Comp("dc4-teaser", total)
    for i, (clip, ms, st, d) in enumerate(cuts):
        z = (1.0, 1.12) if i % 2 == 0 else (1.12, 1.0)
        c.broll(F + clip + ".mp4", st, d, media_start=ms, zoom=z)
    c.shade(0, total)
    c.label("Klinik Rasa Sihat ✅ siap", cuts[6][2] + 0.1, cuts[6][3] + cuts[7][3] - 0.1, top=1500)
    c.broll(F + "IMG_4944.mp4", t, END, media_start=1.2, zoom=(1.0, 1.08))
    c.endcard(t, END, '<span class="ln">Nak klinik</span><span class="ln">macam ni?</span><em class="ln">DM kami</em>', END_SUB, logo=LOGO)
    c.music(music_bed("music_dc4", total), 0.0, total, vol=0.9)
    c.write("/home/user/Hyperframes/compositions/dc4-teaser.html", "DC 4: Teaser")


if __name__ == "__main__":
    for a in sys.argv[1:] or ["1", "2", "3", "4"]:
        {"1": v1, "2": v2, "3": v3, "4": v4}[a]()
