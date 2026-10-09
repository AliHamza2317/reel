#!/usr/bin/env bash
# Rebuilds the reel from source: frames -> audio -> MP4s and cover.
# Usage: ./build.sh [workDir]   (frames and WAVs go to workDir, finished files to ../output)
set -euo pipefail
cd "$(dirname "$0")"
WORK="${1:-/tmp/nuovadev-reel-build}"
OUT="../output"
mkdir -p "$WORK" "$OUT"
rm -rf "$WORK/frames"

node render.cjs "$WORK/frames"
python3 audio.py "$WORK/audio"

encode() { # $1 = audio wav, $2 = output mp4
  ffmpeg -y -hide_banner -loglevel error -framerate 30 -i "$WORK/frames/f_%05d.jpg" -i "$1" \
    -c:v libx264 -preset slow -crf 17 -tune animation -pix_fmt yuv420p -profile:v high -r 30 \
    -c:a aac -b:a 192k -ar 48000 -movflags +faststart -shortest "$2"
}
encode "$WORK/audio/mix.wav"      "$OUT/nuovadev-reel.mp4"
encode "$WORK/audio/sfx_only.wav" "$OUT/nuovadev-reel-sfx-only.mp4"

node -e "
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+require('path').resolve('cover.html'));await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:'$OUT/nuovadev-reel-cover.png'});await b.close();})()"
echo "done: $OUT"
