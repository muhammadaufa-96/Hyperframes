"""Assemble a talking A-roll from source ranges, dropping pauses.

usage: python3 assemble.py SPEC.json OUT.mp4 SEGMENTS.json

SPEC: {"pieces": [{"clip": "IMG_5105", "in": 1.25, "out": 16.95, "tag": "setup",
                    "drop": [[a, b], ...]}, ...],
       "min_gap": 0.35, "pad": 0.1}
Video comes from raw/blur/<clip>.mp4 when present, else raw/sdr/<clip>.mp4.
Silences longer than min_gap (from silencedetect on the clip) are removed,
keeping `pad` seconds of air on each side. `drop` ranges are always removed.
"""
import json, os, re, subprocess, sys

RAW = "/home/user/Hyperframes/dc"
spec = json.load(open(sys.argv[1])); out = sys.argv[2]; seg_out = sys.argv[3]
min_gap = spec.get("min_gap", 0.35); pad = spec.get("pad", 0.1)

_sil = {}
def silences(clip):
    if clip not in _sil:
        r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"{RAW}/wavp/{clip}.wav", "-af",
                            f"silencedetect=noise=-36dB:d={min_gap}", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
        st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
        en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
        _sil[clip] = list(zip(st, en + [1e9] * (len(st) - len(en))))
    return _sil[clip]

def src(clip):
    p = f"{RAW}/blur/{clip}.mp4"
    return p if os.path.exists(p) else f"{RAW}/sdr/{clip}.mp4"

ranges = []  # (clip, a, b, tag, piece_index)
for pi, p in enumerate(spec["pieces"]):
    cuts = [(max(s + pad, p["in"]), min(e - pad, p["out"])) for s, e in silences(p["clip"])]
    cuts = [(a, b) for a, b in cuts if b - a > 0.05]
    cuts += [tuple(d) for d in p.get("drop", [])]
    cuts.sort()
    keep = [[p["in"], p["out"]]]
    for a, b in cuts:
        nxt = []
        for k0, k1 in keep:
            if b <= k0 or a >= k1:
                nxt.append([k0, k1]); continue
            if a > k0: nxt.append([k0, a])
            if b < k1: nxt.append([b, k1])
        keep = nxt
    for k0, k1 in keep:
        if k1 - k0 >= 0.3:
            ranges.append((p["clip"], round(k0, 3), round(k1, 3), p.get("tag", ""), pi))

fc, labels, t, segs, inputs = [], [], 0.0, [], []
for i, (c, a, b, tag, pi) in enumerate(ranges):
    d = b - a
    inputs.append((src(c), a, d))
    fc.append(f"[{i}:v]setpts=PTS-STARTPTS[v{i}]")
    fc.append(f"[{i}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={d-0.012:.3f}:d=0.012[a{i}]")
    labels.append(f"[v{i}][a{i}]")
    segs.append({"clip": c, "src_in": a, "src_out": b, "out_in": round(t, 3), "out_out": round(t + d, 3), "tag": tag, "piece": pi})
    t += d
fc.append("".join(labels) + f"concat=n={len(ranges)}:v=1:a=1[v][a]")
cmd = ["ffmpeg", "-v", "error", "-y"]
for p, a, d in inputs: cmd += ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", p]
cmd += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "18",
        "-preset", "fast", "-g", "30", "-keyint_min", "30", "-pix_fmt", "yuv420p", "-r", "30",
        "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", out]
subprocess.run(cmd, check=True)
json.dump({"duration": round(t, 3), "segments": segs}, open(seg_out, "w"), indent=1)
print(f"{out}: {t:.2f}s from {len(ranges)} cuts")
