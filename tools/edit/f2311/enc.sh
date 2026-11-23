#!/bin/bash
# 21/11: HLG raw -> 1080x1920 SDR 30fps working copy (keyframe every second), one clip per call.
# usage: enc.sh 6726   (reads f2111/dl/IMG_6726.MOV, writes f2111/sdr/IMG_6726.mp4; audio = raw, replaced later)
cd /home/user/Hyperframes/f2311
b=$1
VF="scale=1080:1920:flags=lanczos,zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,eq=contrast=1.05:saturation=1.08,unsharp=5:5:0.3,fps=30"
ffmpeg -nostdin -v error -y -i dl/IMG_$b.MOV -map 0:v:0 -an -vf "$VF" -c:v libx264 -crf 19 -preset fast -g 30 -keyint_min 30 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -movflags +faststart sdr/IMG_$b.mp4 && echo "enc $b done"
