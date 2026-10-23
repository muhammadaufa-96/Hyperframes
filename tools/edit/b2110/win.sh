#!/bin/bash
# usage: win.sh CLIP START DUR -> word times (source time) from transcribing just that window
d=/home/user/Hyperframes/b2110/chk/win/$1_$2; mkdir -p $d
ffmpeg -v error -y -ss $2 -t $3 -i /home/user/Hyperframes/b2110/wav/$1.wav -ac 1 -ar 16000 $d/a.wav
cd $d && npx hyperframes transcribe a.wav -m large-v3-turbo -l ms --json > log.txt 2>&1
python3 -c "
import json; w=json.load(open('transcript.json')); print(' '.join(f\"{x['text']}@{x['start']+$2:.2f}-{x['end']+$2:.2f}\" for x in w))"
