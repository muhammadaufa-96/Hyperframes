#!/bin/bash
# For every analysis copy: contact sheet (fps scaled to ~16 frames) + whisper transcript of clips with speech.
cd /home/user/Hyperframes/f2810; mkdir -p sheets tx
for f in ana/*.mp4; do
  b=$(basename $f .mp4)
  D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
  [ -f sheets/$b.jpg ] || ffmpeg -nostdin -v error -y -i $f -vf "fps=16/$D,scale=150:-2,drawtext=text='%{pts\:hms}':x=3:y=3:fontsize=11:fontcolor=red,tile=8x2" -frames:v 1 sheets/$b.jpg
  if [ ! -f tx/$b/transcript.json ]; then
    mkdir -p tx/$b; (cd tx/$b && npx hyperframes transcribe ../../wav/$b.wav -m large-v3-turbo -l ms --json > log.txt 2>&1)
  fi
done
echo SURVEYDONE
