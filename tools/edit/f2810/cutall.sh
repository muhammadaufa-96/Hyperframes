#!/bin/bash
# For each video: wait until every clip it uses has a full-quality proxy, then assemble + per-piece ASR check.
cd /home/user/Hyperframes/f2810/edit
for v in "$@"; do
  clips=$(python3 -c "import json;print(' '.join(sorted({p['clip'] for p in json.load(open('$v.json'))['pieces']})))")
  for c in $clips; do until [ -f ../sdr/$c.mp4 ]; do sleep 20; done; done
  python3 -u /home/user/Hyperframes/tools/edit/f2810/assemble.py $v.json aroll_$v.mp4 ${v}_segs.json && python3 -u /home/user/Hyperframes/tools/edit/f2810/chk.py $v
done
echo CUTDONE
