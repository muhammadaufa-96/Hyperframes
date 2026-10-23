#!/bin/bash
# usage: cut.sh N  -> assemble ads/edit/adN.json into aroll_adN.mp4, then re-transcribe it to check the cuts
set -e
cd /home/user/Hyperframes/ads/edit
python3 /home/user/Hyperframes/tools/edit/ads/assemble.py ad$1.json aroll_ad$1.mp4 ad$1_segs.json
mkdir -p chk/ad$1 && ffmpeg -v error -y -i aroll_ad$1.mp4 -ac 1 -ar 16000 chk/ad$1/a.wav
cd chk/ad$1 && npx hyperframes transcribe a.wav -m large-v3-turbo -l ms --json > log.txt 2>&1
python3 -c "
import json; w=json.load(open('transcript.json')); print(' '.join(f\"{x['text']}@{x['start']:.1f}\" for x in w))"
