#!/bin/bash
# usage: proxy2.sh <input> <out_name> [start] [dur]   -> dc/sdr/<out_name>.mp4 (1080x1920 30fps SDR graded)
cd /home/user/Hyperframes/dc || exit 1
in="$1"; out=/home/user/Hyperframes/dc/sdr/$2.mp4
SS=(); [ -n "$3" ] && SS=(-ss "$3"); T=(); [ -n "$4" ] && T=(-t "$4")
[ -f "$out" ] && exit 0
GRADE="eq=contrast=1.05:saturation=1.1,colorbalance=rs=0.02:bs=-0.02,unsharp=5:5:0.3"
VF="zscale=w=1080:h=1920:f=lanczos,zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,$GRADE,fps=30"
ffmpeg -v error -y "${SS[@]}" "${T[@]}" -i "$in" -map 0:v:0 -map 0:a:0? -vf "$VF" -c:v libx264 -crf 20 -preset fast -g 30 -keyint_min 30 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$out.tmp.mp4" \
  && mv "$out.tmp.mp4" "$out" && echo "done $2"
