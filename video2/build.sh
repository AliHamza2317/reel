#!/usr/bin/env bash
# Rebuilds reel 2 from source: timeline -> frames -> audio -> MP4s, captions and cover.
# Usage: ./build.sh [workDir]   (frames and WAVs go to workDir, finished files to ../output)
set -euo pipefail
cd "$(dirname "$0")"
WORK="${1:-/tmp/nuovadev-reel2-build}"
OUT="../output"
mkdir -p "$WORK" "$OUT"
rm -rf "$WORK/frames"

python3 timeline.py timeline.json captions.srt
node render2.cjs "$WORK/frames"
python3 audio2.py "$WORK/audio"

encode() { # $1 = audio wav, $2 = output mp4
  ffmpeg -y -hide_banner -loglevel error -framerate 30 -i "$WORK/frames/f_%05d.jpg" -i "$1" \
    -c:v libx264 -preset slow -crf 17 -tune animation -pix_fmt yuv420p -profile:v high -r 30 \
    -c:a aac -b:a 192k -ar 48000 -movflags +faststart -shortest "$2"
}
encode "$WORK/audio/mix.wav"    "$OUT/nuovadev-reel-2.mp4"
encode "$WORK/audio/vo_bed.wav" "$OUT/nuovadev-reel-2-vo-bed.mp4"
cp captions.srt "$OUT/nuovadev-reel-2-captions.srt"

node -e "
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve('cover2.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:'$OUT/nuovadev-reel-2-cover.png'});await b.close();})()"
echo "done: $OUT"
