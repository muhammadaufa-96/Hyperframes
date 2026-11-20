"""Map the user's cut (cut.wav) back to the raw take (IMG_6723.wav): per 0.25 s block, best source offset."""
import subprocess, numpy as np, json
def load(p, sr=4000):
    b = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(b, np.float32)
sr = 4000
src, cut = load("wav/IMG_6723.wav"), load("wav/cut.wav")
n = 1 << int(np.ceil(np.log2(len(src) + sr)))
S = np.fft.rfft(src, n)
step, win = 0.25, 0.75
res = []
t = 0.0
while t + win <= len(cut) / sr:
    seg = cut[int(t * sr):int((t + win) * sr)]
    if np.sqrt((seg ** 2).mean()) < 0.004:
        res.append((t, None)); t += step; continue
    c = np.fft.irfft(S * np.conj(np.fft.rfft(seg, n)), n)[:len(src)]
    e = np.sqrt(np.convolve(src ** 2, np.ones(len(seg)), "valid"))[:len(c)] + 1e-6
    k = int(np.argmax(c[:len(e)] / e))
    res.append((t, round(k / sr - t, 3)))
    t += step
json.dump(res, open("edit/align.json", "w"))
prev = None
for t, o in res:
    if o is None: continue
    if prev is None or abs(o - prev) > 0.08:
        print(f"cut {t:7.2f}  src {t + o:7.2f}  offset {o:7.2f}")
        prev = o
