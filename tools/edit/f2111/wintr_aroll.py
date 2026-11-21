"""Word timings on the assembled A-roll: whisper per window, windows built from cut points (6-12 s)."""
import json, os, subprocess, sys
W = "/home/user/Hyperframes/f2111"
for w in sys.argv[1:]:
    segs = json.load(open(f"{W}/edit/segs_{w}.json")); dur = segs["duration"]
    wav = f"{W}/wav/aroll_{w}.wav"
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", f"/home/user/Hyperframes/assets/footage/f2111/aroll_{w}.mp4", "-ac", "1", "-ar", "16000", wav], check=True)
    pts = [s["out_in"] for s in segs["segments"]] + [dur]
    cuts = [0.0]
    for p in pts[1:]:
        if p - cuts[-1] >= 6:
            cuts.append(p)
    # split windows still longer than 12 s at their middle quietest 10 ms
    if dur - cuts[-1] < 1: cuts[-1] = dur
    elif cuts[-1] != dur: cuts.append(dur)
    d = f"{W}/winA/{w}"; os.makedirs(d, exist_ok=True); allw = []
    for i in range(len(cuts) - 1):
        wd = f"{d}/{i}"; os.makedirs(wd, exist_ok=True)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(cuts[i]), "-t", str(cuts[i + 1] - cuts[i]), "-i", wav, f"{wd}/a.wav"], check=True)
        subprocess.run(f"cd {wd} && npx hyperframes transcribe a.wav -m large-v3-turbo -l ms --json > log.txt 2>&1", shell=True)
        for x in json.load(open(f"{wd}/transcript.json")):
            allw.append({"text": x["text"], "start": round(x["start"] + cuts[i], 3), "end": round(x["end"] + cuts[i], 3)})
    json.dump(allw, open(f"{d}/words.json", "w"), indent=0)
    print(w, len(allw), "words", [round(c, 1) for c in cuts])
