"""21/11 rough cuts: keep-lists over several clips -> segs json + 540p preview (picture from sdr/, sound from audio/*_clean.wav).
usage: python3 rough.py a|b [--render]"""
import json, subprocess, sys
import numpy as np

W = "/home/user/Hyperframes/f2111"

# (clip, start, end, label) in clip seconds; boundaries sit in pauses found by silencedetect
CUTS = {
    "a": [  # Unboxing bekal isteri
        ("6726", 0.30, 8.62, "Aku dah sampai site ... aku nak share dengan korang"),
        ("6726", 8.90, 11.98, "apa yang bekal aku bawa hari ni"),
        ("6726", 12.86, 16.35, "Aku pun tak tahu apa bini aku masakkan. So jom kita"),
        ("6726", 17.25, 19.40, "unboxing sama-sama, let's go"),
        ("6726", 19.44, 29.27, "Tapi maklumlah bekas biasa je. Dalam bag ni total ada 3 bekas"),
        ("6726", 29.63, 43.07, "Yang pertama... oh my god, ada chicken wrap lah geng"),
        ("6726", 44.70, 51.10, "jangan jealous ... thank you sayang"),
        ("6726", 58.40, 61.17, "Yang second one. Wow. Ok geng"),
        ("6726", 62.32, 64.12, "Ni adalah lauk. Apa ni?"),
        ("6726", 70.15, 77.27, "Wow, lauk ayam masak merah geng ... sampai ke malam"),
        ("6726", 77.73, 79.99, "Dengan satu lagi, nasi lah macam biasa"),
        ("6726", 84.21, 86.08, "sedap lah"),
        ("6726", 87.24, 89.11, "tu jadi lapar"),
        ("6728", 0.86, 8.24, "Bismillah, kita nak cuba sendiri. Dipping. Homemade"),
        ("6728", 9.31, 11.01, "(makan)"),
        ("6728", 20.73, 23.07, "Ok, rasa dia"),
        ("6728", 24.30, 26.15, "ini bukan nak bias lah"),
        ("6728", 27.23, 28.62, "tapi memang sedap"),
        ("6728", 29.55, 30.79, "pedas dia ngam-ngam"),
        ("6728", 31.66, 33.14, "ada manis sikit"),
        ("6728", 35.36, 39.10, "pedas-pedas je, just nice"),
        ("6728", 44.12, 51.91, "itulah kelebihan bila masak sendiri ... penuh, limpah-limpah"),
        ("6728", 53.38, 55.40, "(makan, hmm)"),
        ("6726", 93.83, 95.83, "Aku nak tanya semua lelaki-lelaki"),
        ("6726", 96.75, 100.78, "bapak-bapak yang dah kahwin, yang bujang ke tepi sikit"),
        ("6726", 101.43, 110.20, "korang setuju tak dengan statement aku ... the moment kita dapat makan"),
        ("6726", 110.75, 114.22, "air tangan bini kita, especially bila sedap"),
        ("6726", 115.83, 118.64, "dia boleh mood tak okay jadi mood okay"),
        ("6726", 121.95, 129.76, "But anyway, thank you so much to my wife"),
        ("6727", 2.80, 15.30, "Betul tak geng ... setuju tak? Komen di bawah. See you, Assalamualaikum"),
    ],
    "b": [],  # filled from json once 6753 is cut
}


def load(clip, sr=16000):
    b = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{W}/wav/{clip}_c16.wav", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(b, np.int16).astype(np.float32)
    return np.sqrt(np.convolve(a ** 2, np.ones(400) / 400, "same"))[::160]   # 10 ms rms


def main(which, render):
    cuts = CUTS[which] or [tuple(x) for x in json.load(open(f"{W}/edit/cuts_{which}.json"))]
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
