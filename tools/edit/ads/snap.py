"""Snap piece in/out points to the nearest real silence so word endings are not clipped.
usage: python3 snap.py adN.json"""
import json, re, subprocess, sys
p = sys.argv[1]; d = json.load(open(p))
_s = {}
def sil(c):
    if c not in _s:
        r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"/home/user/Hyperframes/ads/wav/{c}.wav", "-af", "silencedetect=noise=-36dB:d=0.2", "-f", "null", "-"], capture_output=True, text=True).stderr
        _s[c] = list(zip(map(float, re.findall(r"silence_start: ([\d.]+)", r)), map(float, re.findall(r"silence_end: ([\d.]+)", r))))
    return _s[c]
ps = d["pieces"]
for i, x in enumerate(ps):
    contig_next = i + 1 < len(ps) and ps[i + 1]["clip"] == x["clip"] and abs(ps[i + 1]["in"] - x["out"]) < 0.01
    contig_prev = i and ps[i - 1]["clip"] == x["clip"] and abs(ps[i - 1]["out"] - x["in"]) < 0.01
    S = sil(x["clip"])
    if not contig_next:
        nxt = [a for a, b in S if a >= x["out"] - 0.02 and a - x["out"] <= 0.7]
        inside = [a for a, b in S if a < x["out"] < b]
        if not inside and nxt:
            print(f'{x["tag"]}: out {x["out"]} -> {nxt[0] + 0.03:.2f}'); x["out"] = round(nxt[0] + 0.03, 2)
    if not contig_prev:
        prv = [b for a, b in S if b <= x["in"] + 0.02 and x["in"] - b <= 0.5]
        inside = [a for a, b in S if a < x["in"] < b]
        if not inside and prv:
            print(f'{x["tag"]}: in {x["in"]} -> {prv[-1] - 0.03:.2f}'); x["in"] = round(prv[-1] - 0.03, 2)
json.dump(d, open(p, "w"), indent=1)
