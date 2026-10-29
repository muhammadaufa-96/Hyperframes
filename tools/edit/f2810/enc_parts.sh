#!/bin/bash
# Encode one long HDR clip as 4 parallel chunks, then join them losslessly.
# usage: enc_parts.sh NAME (raw at dlhq/NAME.MOV)
cd /home/user/Hyperframes/f2810
n=$1; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 dlhq/$n.MOV)
L=$(python3 -c "print($D/4)")
GRADE="eq=contrast=1.05:saturation=1.08,unsharp=5:5:0.3"
VF="scale=1080:1920:flags=lanczos,zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,$GRADE,fps=30"
for i in 0 1 2 3; do
  ss=$(python3 -c "print($i*$L)")
  ffmpeg -nostdin -v error -y -ss $ss -t $L -i dlhq/$n.MOV -map 0:v:0 -map 0:a:0? -vf "$VF" -c:v libx264 -crf 19 -preset fast -g 30 -keyint_min 30 \
    -color_primaries bt709 -color_trc bt709 -colorspace bt709 -c:a aac -b:a 192k -ar 48000 parts/${n}_$i.mp4 &
done
wait
printf "file '%s'\n" parts/${n}_0.mp4 parts/${n}_1.mp4 parts/${n}_2.mp4 parts/${n}_3.mp4 > parts/$n.txt
ffmpeg -nostdin -v error -y -f concat -safe 0 -i parts/$n.txt -c copy -movflags +faststart sdr/$n.mp4 && echo "done $n $(ffprobe -v error -show_entries format=duration -of csv=p=0 sdr/$n.mp4)"
