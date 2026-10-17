#!/bin/bash
# usage: proxy.sh <input> [max_seconds]
# writes raw/sdr/<base>.mp4: 1080x1920, 30fps, SDR (HLG tonemapped), graded, keyframe every 1s
cd /home/user/Hyperframes/raw || exit 1
in="$1"; b=$(basename "${in%.*}"); out=/home/user/Hyperframes/raw/sdr/$b.mp4
T=(); [ -n "$2" ] && T=(-t "$2")
[ -f "$out" ] && exit 0
GRADE="eq=contrast=1.06:saturation=1.15,colorbalance=rs=0.03:bs=-0.03:rm=0.02:bm=-0.02,unsharp=5:5:0.4"
if ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer -of csv=p=0 "$in" | grep -q arib-std-b67; then
  VF="zscale=w=1080:h=1920:f=lanczos,zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,$GRADE,fps=30"
else
  VF="scale=1080:1920:flags=lanczos,$GRADE,fps=30,format=yuv420p"
fi
ffmpeg -v error -y "${T[@]}" -i "$in" -map 0:v:0 -map 0:a:0? -vf "$VF" -c:v libx264 -crf 18 -preset fast -g 30 -keyint_min 30 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$out.tmp.mp4" \
  && mv "$out.tmp.mp4" "$out" && echo "done $b"
