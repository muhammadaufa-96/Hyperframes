"""21/11 rough cuts: keep-lists over several clips -> segs json + 540p preview (picture from sdr/, sound from audio/*_clean.wav).
usage: python3 rough.py a|b [--render]"""
import json, subprocess, sys
import numpy as np

W = "/home/user/Hyperframes/f2311"

# (clip, start, end, label) in clip seconds; boundaries sit in pauses found by silencedetect
CUTS = {
    "a": [  # 23/11 kabinet: hiccup di site
        ("6783", 0.55, 10.63, "Korang mesti tertanya ... tiba-tiba ada hiccup ... settlekan on the spot"),
        ("6783", 11.98, 12.95, "dekat site juga"),
        ("6783", 14.90, 21.25, "Contoh macam mana kita buat edging dekat site, potong laminate dekat site"),
        ("6783", 21.70, 24.80, "Video kali ni aku share macam mana cara kita buat"),
        ("6783", 26.06, 32.89, "ini sebenarnya kerja ada sedikit isu, tapi Alhamdulillah manage selesaikan"),
        ("6783", 33.95, 42.95, "macam korang tengok, fully laminate ... semua potong dekat site, edging pun"),
        ("6783", 43.30, 49.36, "orang biasa buat kabinet: macam mana kau buat kat site, gila ke apa? Haa itulah geng"),
        ("6783", 52.60, 55.95, "Kadang-kadang ada benda kita boleh control, ada yang tak boleh control"),
        ("6783", 56.75, 63.88, "bila yang tak boleh control, make sure everything on track"),
        ("6783", 64.22, 65.18, "kita kena kreatif lah"),
        ("6783", 66.00, 74.35, "macam korang tengok, sekarang tengah potong, baru siap edging dan laminate"),
        ("6783", 75.41, 81.78, "dan kita buat potongan untuk ruangan kabinet, letak sinki"),
        ("6783", 86.76, 91.44, "Korang boleh like and share ... see you in the next video, Assalamualaikum"),
    ],
}


def load(clip, sr=16000):
    b = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{W}/wav/{clip}_c16.wav", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(b, np.int16).astype(np.float32)
    return np.sqrt(np.convolve(a ** 2, np.ones(400) / 400, "same"))[::160]   # 10 ms rms


def main(which, render):
    cuts = CUTS[which]
    env, segs, out = {}, [], 0.0
    for clip, s, e, lab in cuts:
        if clip not in env:
            env[clip] = load(clip)
        r = env[clip]
        def snap(t, rad=0.06):
            i0, i1 = max(0, int((t - rad) * 100)), min(len(r) - 1, int((t + rad) * 100))
            return (i0 + int(np.argmin(r[i0:i1 + 1]))) / 100
        s2, e2 = snap(s), min(snap(e), len(r) / 100)
        segs.append({"clip": clip, "src_in": s2, "src_out": e2, "out_in": round(out, 3), "out_out": round(out + e2 - s2, 3), "label": lab})
        out += e2 - s2
    json.dump({"segments": segs, "duration": round(out, 3)}, open(f"{W}/edit/segs_{which}.json", "w"), indent=1)
    print(f"{which}: {len(segs)} pieces, {out:.2f}s")
    if not render:
        return
    import os
    tmp = f"{W}/edit/parts_{which}"; os.makedirs(tmp, exist_ok=True)
    lst = []
    for i, x in enumerate(segs):
        d = x["src_out"] - x["src_in"]; p = f"{tmp}/{i:03d}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{x['src_in']:.3f}", "-t", f"{d:.3f}", "-i", f"{W}/sdr/IMG_{x['clip']}.mp4",
                        "-ss", f"{x['src_in']:.3f}", "-t", f"{d:.3f}", "-i", f"{W}/audio/{x['clip']}_clean.wav",
                        "-map", "0:v", "-map", "1:a", "-vf", "scale=540:960,fps=30",
                        "-af", f"aformat=sample_rates=48000:channel_layouts=mono,afade=t=in:d=0.02,afade=t=out:st={max(0, d - 0.03):.3f}:d=0.03",
                        "-c:v", "libx264", "-crf", "24", "-preset", "veryfast", "-c:a", "aac", "-b:a", "128k", "-ar", "48000", p], check=True)
        lst.append(f"file '{p}'")
    open(f"{tmp}/list.txt", "w").write("\n".join(lst) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{tmp}/list.txt", "-c", "copy", "-movflags", "+faststart",
                    f"{W}/edit/draft/rough_{which}.mp4"], check=True)
    print("rendered", f"{W}/edit/draft/rough_{which}.mp4")


if __name__ == "__main__":
    main(sys.argv[1], "--render" in sys.argv)
