"""20/11 vlog (IMG_6723): keep-list in source seconds, snapped to energy minima, -> rough cut + segs json."""
import json, subprocess, sys, numpy as np
W = "/home/user/Hyperframes/f2011"
KEEP = [  # (start, end, label) source seconds, from windowed transcript win/words.json
    (0.00, 3.62, "A apa yang kita rancang, apa yang kita buat tu, kadang-kadang"),
    (7.00, 8.86, "A tak setiap mana yang kita nak"),
    (9.22, 22.22, "B kadang-kadang jalan ... belok ke kiri"),
    (22.55, 23.73, "C sebab tu"),
    (24.58, 26.05, "C aku perasan"),
    (28.40, 30.68, "C untuk memastikan yang kita betul-betul on track"),
    (30.82, 33.92, "C kita kena kuat dalaman kita, tauhid kita dengan Tuhan"),
    (37.15, 42.35, "C kita kena kuatkan asas kita, cara jalani hidup kita"),
    (47.15, 53.20, "D korang nak tahu ni, aku tengah loading barang ... dekat site"),
    (53.97, 56.58, "D dekat area-area Selangor ni jugalah"),
    (56.78, 60.95, "E macam biasa lah, kita rancang, tiba-tiba ada hiccup, ada masalah"),
    (64.80, 67.86, "E aku terpaksa kena betul-betul terjun"),
    (69.68, 70.92, "E jadi tukang terus"),
    (71.80, 73.78, "E walaupun aku dah lama tak jadi tukang"),
    (77.45, 78.92, "F tapi it's okay lah"),
    (81.92, 85.00, "F kena enjoy dengan proses yang Tuhan susun"),
    (85.20, 87.72, "G ni nama dia Jantan"),
    (104.55, 105.08, "I nanti"),
    (107.35, 110.24, "I aku rasa aku nak share dengan korang satu lagi journey baru aku"),
    (111.05, 114.55, "I dan benda ni akan jadi masuk dalam target untuk tahun 2027"),
    (116.15, 118.52, "J korang boleh like and share video ni"),
    (118.97, 121.06, "J dan tekan button follow"),
    (121.36, 121.80, "J untuk more"),
    (122.57, 125.62, "J tips dalam renovation, dalam business, dalam life"),
    (128.66, 131.40, "J see you in the next video, Assalamualaikum"),
]
sr = 16000
wav = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{W}/wav/IMG_6723.wav", "-f", "s16le", "-"], capture_output=True).stdout
a = np.frombuffer(wav, np.int16).astype(np.float32)
hop = 160; rms = np.sqrt(np.convolve(a**2, np.ones(400)/400, "same"))[::hop]
def snap(t, r=0.08):
    i0, i1 = max(0, int((t-r)*100)), min(len(rms)-1, int((t+r)*100))
    return (i0 + int(np.argmin(rms[i0:i1+1]))) / 100
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{W}/sdr/IMG_6723.mp4"], capture_output=True, text=True).stdout)
segs, out = [], 0.0
for s, e, lab in KEEP:
    s2, e2 = snap(s), min(snap(e), dur)
    segs.append({"src_in": s2, "src_out": e2, "out_in": round(out, 3), "out_out": round(out + e2 - s2, 3), "label": lab})
    out += e2 - s2
json.dump({"segments": segs, "duration": round(out, 3)}, open(f"{W}/edit/segs.json", "w"), indent=1)
print(f"total {out:.2f}s from {dur:.2f}s")
if "--render" in sys.argv:
    v = "".join(f"[0:v]trim={x['src_in']}:{x['src_out']},setpts=PTS-STARTPTS,scale=540:960[v{i}];[0:a]atrim={x['src_in']}:{x['src_out']},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={x['src_out']-x['src_in']-0.04:.3f}:d=0.04[a{i}];" for i, x in enumerate(segs))
    v += "".join(f"[v{i}][a{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=1[v][a]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/sdr/IMG_6723.mp4", "-filter_complex", v, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "24", "-preset", "veryfast", "-c:a", "aac", "-b:a", "128k", f"{W}/edit/roughcut.mp4"], check=True)
    print("rendered")
