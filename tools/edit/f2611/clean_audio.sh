#!/bin/bash
# 26/11: RNNoise chain (no mic assumed until checked) -> audio/<b>_clean.wav (48k) + wav/<b>_c16.wav
cd /home/user/Hyperframes/f2611
HEAVY="highpass=f=90,lowpass=f=11000,arnndn=m=/root/models/sh.rnnn:mix=0.92,afftdn=nr=8:nf=-42:tn=1,equalizer=f=200:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1.2:g=3,acompressor=threshold=-22dB:ratio=3:attack=8:release=120:makeup=3,loudnorm=I=-16:TP=-1.5:LRA=9"
LIGHT="highpass=f=80,afftdn=nr=6:nf=-45:tn=1,equalizer=f=3000:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=150:makeup=2,loudnorm=I=-16:TP=-1.5:LRA=9"
while read b a; do
  af=$HEAVY; [ "${MODE:-heavy}" = light ] && af=$LIGHT
  ffmpeg -nostdin -v error -y -i dl/IMG_$b.MOV -map 0:$a -ac 1 -ar 48000 -af "$af" audio/${b}_clean.wav && ffmpeg -nostdin -v error -y -i audio/${b}_clean.wav -ar 16000 wav/${b}_c16.wav && echo "audio $b"
done < astream.txt
