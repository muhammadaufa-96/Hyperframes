"""Transcribe each piece of an assembled A-roll separately (accurate word times, catches repeats).
usage: python3 chk.py N  -> ads/edit/chk/adN/words.json  [[text, t0, t1, tag], ...] in A-roll time"""
import json, os, subprocess, sys
n = sys.argv[1]
E = "/home/user/Hyperframes/b2110/edit/"
segs = json.load(open(f"{E}v{n}_segs.json"))
pieces = {}
for s in segs["segments"]:
    p = pieces.setdefault(s["piece"], [s["out_in"], s["out_out"], s["tag"]])
    p[1] = s["out_out"]
out = []
for pi, (a, b, tag) in sorted(pieces.items()):
    d = f"{E}chk/v{n}/p{pi}"
    os.makedirs(d, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{b - a:.3f}", "-i", f"{E}aroll_v{n}.mp4", "-ac", "1", "-ar", "16000", f"{d}/a.wav"], check=True)
    subprocess.run(f"cd {d} && npx hyperframes transcribe a.wav -m large-v3-turbo -l ms --json > log.txt 2>&1", shell=True)
    ws = json.load(open(f"{d}/transcript.json")) if os.path.exists(f"{d}/transcript.json") else []
    print(f"[{tag} {a:.2f}-{b:.2f}]", " ".join(f"{w['text']}@{w['start'] + a:.2f}" for w in ws))
    out += [[w["text"], round(w["start"] + a, 3), round(w["end"] + a, 3), tag] for w in ws]
json.dump(out, open(f"{E}chk/v{n}/words.json", "w"), indent=0)
