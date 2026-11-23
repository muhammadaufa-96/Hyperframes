"""Windowed whisper transcription (7-12 s windows split at pauses) -> f2111/win/<clip>/words.json in clip seconds."""
import json, re, subprocess, sys, os
W = "/home/user/Hyperframes/f2311"
for b in sys.argv[1:]:
    wav = f"{W}/wav/{b}_c16.wav"; d = f"{W}/win/{b}"; os.makedirs(d, exist_ok=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", wav], capture_output=True, text=True).stdout)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", "silencedetect=noise=-30dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    cuts = [0.0]
    for a, e in zip(st, en):
        m = (a + e) / 2
        if m - cuts[-1] >= 7: cuts.append(m)
    if dur - cuts[-1] < 2 and len(cuts) > 1: cuts.pop()
    cuts.append(dur)
    allw = []
    for i in range(len(cuts) - 1):
        wd = f"{d}/{i}"; os.makedirs(wd, exist_ok=True)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(cuts[i]), "-t", str(cuts[i + 1] - cuts[i]), "-i", wav, f"{wd}/a.wav"], check=True)
        subprocess.run(f"cd {wd} && npx hyperframes transcribe a.wav -m large-v3-turbo -l ms --json > log.txt 2>&1", shell=True)
        try:
            for x in json.load(open(f"{wd}/transcript.json")):
                allw.append({"text": x["text"], "start": round(x["start"] + cuts[i], 3), "end": round(x["end"] + cuts[i], 3)})
        except Exception:
            print("window fail", b, i)
    json.dump(allw, open(f"{d}/words.json", "w"), indent=0)
    print(b, len(allw), "words")
