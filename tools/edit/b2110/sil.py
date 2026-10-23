"""print silences of a clip: python3 sil.py IMG_5274 [noise_db] [min]"""
import re, subprocess, sys
c = sys.argv[1]; n = sys.argv[2] if len(sys.argv) > 2 else "-36"; d = sys.argv[3] if len(sys.argv) > 3 else "0.25"
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"/home/user/Hyperframes/b2110/wav/{c}.wav", "-af", f"silencedetect=noise={n}dB:d={d}", "-f", "null", "-"], capture_output=True, text=True).stderr
st = re.findall(r"silence_start: ([\d.]+)", r); en = re.findall(r"silence_end: ([\d.]+)", r)
print(c, " ".join(f"[{float(a):.2f}-{float(b):.2f}]" for a, b in zip(st, en)))
