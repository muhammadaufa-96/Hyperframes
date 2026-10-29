#!/bin/bash
# Full-quality pass for the approved edits: download a raw, make a 1080x1920 30 fps graded SDR proxy, drop the raw.
# Downloads run one at a time; encodes run two at a time.
cd /home/user/Hyperframes/f2810
enc() {
  name=$1; b=${name%.*}
  GRADE="eq=contrast=1.05:saturation=1.08,unsharp=5:5:0.3"
  if ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer -of csv=p=0 dlhq/$name | grep -q arib-std-b67; then
    VF="scale=1080:1920:flags=lanczos,zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,$GRADE,fps=30"
  else
    VF="scale=1080:1920:flags=lanczos,format=yuv420p,$GRADE,fps=30"
  fi
  ffmpeg -nostdin -v error -y -i dlhq/$name -map 0:v:0 -map 0:a:0? -vf "$VF" -c:v libx264 -crf 19 -preset fast -g 30 -keyint_min 30 \
    -color_primaries bt709 -color_trc bt709 -colorspace bt709 -c:a aac -b:a 192k -ar 48000 -movflags +faststart sdr/$b.tmp.mp4 \
    && mv sdr/$b.tmp.mp4 sdr/$b.mp4 && echo "done $b"
  rm -f dlhq/$name
}
export -f enc
while read id name; do
  b=${name%.*}; [ -f sdr/$b.mp4 ] && continue
  while [ $(ls dlhq | grep -c MOV) -ge 2 ]; do sleep 5; done
  gdown -q "$id" -O dlhq/$name.part && mv dlhq/$name.part dlhq/$name || { echo "FAIL $name"; continue; }
  enc $name &
done < listhq.txt
wait
echo HQDONE
