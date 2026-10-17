"""Blur faces in a 1080x1920 proxy.

usage: python3 blur.py IN.mp4 OUT.mp4 [--keep-largest-frac 0.14] [--range start end]

--keep-largest-frac F : leave faces wider than F*frame-width untouched (the host's own
                        selfie face); everything smaller gets blurred.
Writes OUT with the input's audio stream copied.
"""
import sys, subprocess, json
import cv2
import numpy as np

args = sys.argv[1:]
src, dst = args[0], args[1]
keep_frac = None
if "--keep-largest-frac" in args:
    keep_frac = float(args[args.index("--keep-largest-frac") + 1])

cap = cv2.VideoCapture(src)
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30
DW, DH = 540, 960
det = cv2.FaceDetectorYN.create("/root/models/yunet.onnx", "", (DW, DH), 0.8, 0.3, 5000)
sx, sy = W / DW, H / DH

ff = subprocess.Popen([
    "ffmpeg", "-v", "error", "-y",
    "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
    "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
    "-g", "30", "-keyint_min", "30", "-pix_fmt", "yuv420p",
    "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
    "-c:a", "copy", "-movflags", "+faststart", dst], stdin=subprocess.PIPE)

tracks = []  # [x, y, w, h, ttl, hits]
TTL = 10
n = 0; blurred_frames = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    small = cv2.resize(frame, (DW, DH))
    _, faces = det.detect(small)
    boxes = []
    if faces is not None:
        for f in faces:
            x, y, w, h = f[:4] * [sx, sy, sx, sy]
            if keep_frac and w > keep_frac * W:
                continue
            boxes.append([x, y, w, h])
    # age tracks, refresh with matches
    for t in tracks:
        t[4] -= 1
    for b in boxes:
        cx, cy = b[0] + b[2] / 2, b[1] + b[3] / 2
        for t in tracks:
            tx, ty = t[0] + t[2] / 2, t[1] + t[3] / 2
            if abs(cx - tx) < max(b[2], t[2]) and abs(cy - ty) < max(b[3], t[3]):
                t[:4] = b; t[4] = TTL; t[5] += 1; break
        else:
            tracks.append(b + [TTL, 1])
    tracks = [t for t in tracks if t[4] > 0]
    live = [t for t in tracks if t[5] >= 3]
    if live:
        blurred_frames += 1
        out = frame.copy()
        heavy = cv2.GaussianBlur(cv2.resize(frame, (W // 8, H // 8)), (0, 0), 6)
        heavy = cv2.resize(heavy, (W, H))
        mask = np.zeros((H, W), np.uint8)
        for x, y, w, h, _, _ in live:
            cx, cy = int(x + w / 2), int(y + h / 2)
            cv2.ellipse(mask, (cx, cy), (int(w * 0.8), int(h * 0.95)), 0, 0, 360, 255, -1)
        mask = cv2.GaussianBlur(mask, (31, 31), 0)[..., None] / 255.0
        frame = (heavy * mask + out * (1 - mask)).astype(np.uint8)
    ff.stdin.write(frame.tobytes())
    n += 1
ff.stdin.close(); ff.wait()
print(json.dumps({"src": src, "frames": n, "blurred_frames": blurred_frames}))
