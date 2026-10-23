#!/bin/bash
# Video 2: crop the monitor content out of the phone recording (hide URL bar, taskbar, bezel),
# lay it over a blurred fill, cut the furniture beats, export muted 1080x1920 + the voice line.
cd /home/user/Hyperframes/b2110/edit
IN=../sdr/IMG_5308.mp4
# src_start dur
SEG="0 9.46
9.0 2.58
15.2 2.58
20.0 2.58
28.0 0.86
29.0 0.86
30.0 1.72"
i=0; : > v2_list.txt
while read s d; do
  ffmpeg -nostdin -v error -y -ss $s -t $d -i $IN -filter_complex \
   "[0:v]crop=1080:1100:0:470,split[a][b];[a]scale=-2:1920,crop=1080:1920,boxblur=40:2,eq=brightness=-0.12[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2-40,fps=30,format=yuv420p[v]" \
   -map "[v]" -an -c:v libx264 -crf 18 -preset fast -g 30 v2_s$i.mp4 && echo "file v2_s$i.mp4" >> v2_list.txt
  i=$((i+1))
done <<< "$SEG"
ffmpeg -v error -y -f concat -safe 0 -i v2_list.txt -c copy v2_screen.mp4
ffmpeg -v error -y -t 7.7 -i $IN -vn -af "afade=t=out:st=7.3:d=0.4" -c:a aac -b:a 192k v2_voice.m4a
ffprobe -v error -show_entries format=duration -of csv=p=0 v2_screen.mp4
