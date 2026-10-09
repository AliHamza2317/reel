# Reel 2 source: "Before you build your app"

This folder builds `../output/nuovadev-reel-2*.*`, the motion version of `../nuovadev-reel-2-before-you-build.md`.

| File | What it does |
|---|---|
| `timeline.py` | The single source of timing. It turns the Version B narration into word-level times at a natural read and writes `timeline.json`, `timeline.js` (for the renderer) and `captions.srt`. |
| `reel2.html` | Every scene. Every animation beat is anchored to a word in the timeline, so changing the timeline moves the picture with it. |
| `render2.cjs` | Saves all 1,350 frames (30 fps × 45 s) with headless Chromium. `--at 4.97,20.1` saves review stills instead. |
| `audio2.py` | Music bed and sound effects, cued from `timeline.json`. Reuses the synth voices in `../video/audio.py`. |
| `cover2.html` | The cover. Its text sits inside the 3:4 profile-grid crop. |
| `assets/` | The website's logo marks, plus clean captures of the real nuovadev.com MVP and Contact pages, rendered from the website source. |
| `build.sh` | Rebuilds everything into `../output`. |
| `photos.json`, `fetch_photos.py` | Links to the six generated photographic backgrounds, and a script that downloads them into `assets/photos/` as 1080×1920 JPEGs. Each photo is optional; a scene without its photo falls back to the plain brand background. |

**Matching a recorded voiceover:** adjust the pauses in `CHUNKS` inside `timeline.py`, or swap in measured word times, then run `./build.sh`. The captions, scene cuts, on-screen text and sound cues all follow.

**Re-capturing the website screens:** if the live pages change, replace `assets/site-mvp.png` and `assets/site-contact.png` with fresh 1170 px-wide mobile captures (390 px viewport at 3× scale), taken from the top of each page.

The fonts are loaded from `../video/assets/fonts` (Poppins, Inter and JetBrains Mono, the website's typefaces, under the SIL Open Font License).
