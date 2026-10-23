#!/bin/bash
# usage: sheet.sh NAME [cols] -> scratchpad/qa/NAME.jpg, 15 evenly spaced frames of renders/NAME.mp4
S=/tmp/claude-0/-home-user-Hyperframes/7a1190b6-db46-56b9-84eb-018afdc4f501/scratchpad/qa/$1; rm -rf $S; mkdir -p $S
f=/home/user/Hyperframes/renders/$1.mp4; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
for i in $(seq 0 14); do t=$(python3 -c "print(round(0.4+$i*($D-0.8)/14,2))"); ffmpeg -v error -y -ss $t -i $f -frames:v 1 -vf "scale=270:480,drawtext=text='$t':x=6:y=6:fontsize=20:fontcolor=red" $S/o_$(printf %02d $i).jpg; done
ffmpeg -v error -y -i $S/o_%02d.jpg -vf tile=5x3 $S/../$1.jpg && echo $S/../$1.jpg
