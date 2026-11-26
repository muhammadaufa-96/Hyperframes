"""21/11 rough cuts: keep-lists over several clips -> segs json + 540p preview (picture from sdr/, sound from audio/*_clean.wav).
usage: python3 rough.py a|b [--render]"""
import json, subprocess, sys
import numpy as np

W = "/home/user/Hyperframes/f2611"

# (clip, start, end, label) in clip seconds; boundaries sit in pauses found by silencedetect
CUTS = {
    "a": [  # 26/11: hari anugerah anak, akhlak ibarat bunga
        ("6998", 0.89, 16.91, "Alhamdulillah ... hari anugerah kecemerlangan ... anak sulung aku"),
        ("6998", 17.61, 24.31, "bukan nak cerita pasal anugerah ... kita bangga, kita happy"),
        ("6998", 26.42, 39.33, "Tapi aku terkesan dengan kata-kata guru besar: sekolah membina akhlak"),
        ("6998", 39.71, 42.15, "Jadi bila disebut pasal akhlak yang baik ni kan"),
        ("6998", 43.40, 47.57, "aku tiba-tiba teringat kata-kata arwah atuk aku"),
        ("6998", 48.26, 50.24, "Dia kupas mengenai akhlak"),
        ("6998", 99.68, 103.45, "Dengan bahasa mudah, akhlak ibarat bunga. Bunga diri kita"),
        ("6998", 107.57, 112.08, "dia indah dilihat oleh mata dan senang dirasa oleh hati"),
        ("6998", 112.45, 133.30, "Maksudnya orang sekeliling senang tengok kita ... benchmark ... zaman sekarang"),
        ("6998", 135.25, 146.13, "budak sanggup bertikam sebab gaduh boyfriend girlfriend ... akhlak tak diterapkan"),
        ("6998", 146.84, 158.74, "Menurut korang macam mana nak pastikan anak berakhlak baik"),
        ("6998", 162.00, 165.15, "korang boleh komen kat bawah, share pandangan korang"),
        ("6998", 169.80, 177.43, "like and share kepada yang memerlukan ... follow untuk more tips"),
        ("6998", 178.13, 179.48, "dalam life, business"),
        ("6998", 181.45, 184.20, "see you in next video, Assalamualaikum"),
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
