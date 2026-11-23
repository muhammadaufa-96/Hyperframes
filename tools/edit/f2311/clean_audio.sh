#!/bin/bash
# 23/11: no mic on any clip -> RNNoise + presence EQ + compressor + loudnorm (same chain as 21/11 IMG_6753).
cd /home/user/Hyperframes/f2311
HEAVY="highpass=f=90,lowpass=f=11000,arnndn=m=/root/models/sh.rnnn:mix=0.92,afftdn=nr=8:nf=-42:tn=1,equalizer=f=200:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1.2:g=3,acompressor=threshold=-22dB:ratio=3:attack=8:release=120:makeup=3,loudnorm=I=-16:TP=-1.5:LRA=9"
while read b a; do
  ffmpeg -nostdin -v error -y -i dl/IMG_$b.MOV -map 0:$a -ac 1 -ar 48000 -af "$HEAVY" audio/${b}_clean.wav && ffmpeg -nostdin -v error -y -i audio/${b}_clean.wav -ar 16000 wav/${b}_c16.wav && echo "audio $b"
done < astream.txt
