#!/bin/bash
# Folder 28/10/26: download each raw from Drive one at a time, keep a small analysis copy
# (540-wide SDR, 15 fps) + 16 kHz wav, then remove the downloaded raw (originals stay on Drive).
cd /home/user/Hyperframes/f2810
while read id name; do
  b=${name%.*}
  [ -f ana/$b.mp4 ] && continue
  gdown -q "$id" -O dl/$name || { echo "FAIL dl $name"; continue; }
  if ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer -of csv=p=0 dl/$name | grep -q arib-std-b67; then
    TM=",zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv"
  else TM=""; fi
  ffmpeg -nostdin -v error -y -i dl/$name -map 0:v:0 -map 0:a:0? -vf "scale='if(gt(iw,ih),960,540)':-2$TM,format=yuv420p,fps=15" \
    -c:v libx264 -crf 26 -preset veryfast -c:a aac -b:a 96k ana/$b.mp4 && \
  ffmpeg -nostdin -v error -y -i dl/$name -vn -ac 1 -ar 16000 wav/$b.wav
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 dl/$name)
  echo "$b $d $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 ana/$b.mp4)"
  rm -f dl/$name
done < list.txt
echo FETCHDONE
