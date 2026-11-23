"""21/11: full-quality A-roll from edit/segs_<a|b>.json -> assets/footage/f2311/aroll_<w>.mp4 (1080x1920, 30 fps, clean audio)."""
import json, os, subprocess, sys
W = "/home/user/Hyperframes/f2311"; OUT = "/home/user/Hyperframes/assets/footage/f2311"
os.makedirs(OUT, exist_ok=True)
for w in sys.argv[1:]:
    segs = json.load(open(f"{W}/edit/segs_{w}.json"))["segments"]
    tmp = f"{W}/edit/hq_{w}"; os.makedirs(tmp, exist_ok=True); lst = []
    for i, x in enumerate(segs):
        d = x["src_out"] - x["src_in"]; p = f"{tmp}/{i:03d}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{x['src_in']:.3f}", "-t", f"{d:.3f}", "-i", f"{W}/sdr/IMG_{x['clip']}.mp4",
                        "-ss", f"{x['src_in']:.3f}", "-t", f"{d:.3f}", "-i", f"{W}/audio/{x['clip']}_clean.wav", "-map", "0:v", "-map", "1:a",
                        "-af", f"aformat=sample_rates=48000:channel_layouts=mono,afade=t=in:d=0.02,afade=t=out:st={max(0, d - 0.03):.3f}:d=0.03",
                        "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-g", "30", "-keyint_min", "30", "-r", "30",
                        "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
                        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", p], check=True)
        lst.append(f"file '{p}'")
    open(f"{tmp}/list.txt", "w").write("\n".join(lst) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{tmp}/list.txt", "-c", "copy", "-movflags", "+faststart",
                    f"{OUT}/aroll_{w}.mp4"], check=True)
    print(w, subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{OUT}/aroll_{w}.mp4"], capture_output=True, text=True).stdout.strip())
