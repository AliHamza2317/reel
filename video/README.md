# Reel video source

This folder builds `../output/nuovadev-reel.mp4`, the animated, no-presenter version of the script in `../nuovadev-reel-before-your-next-hire.md`.

| File | What it does |
|---|---|
| `reel.html` | Every scene, caption and animation. `render(t)` draws the frame at second `t`. |
| `render.cjs` | Opens `reel.html` in headless Chromium and saves all 1,320 frames (30 fps × 44 s). `--at 0,12.5` saves review stills instead. |
| `audio.py` | Synthesises the music bed and sound effects, timed to the same cues. Writes `mix.wav` and `sfx_only.wav`. |
| `cover.html` | The reel cover image (the text sits inside the 3:4 profile-grid crop). |
| `build.sh` | Runs everything and writes the MP4s and cover to `../output`. |

Rebuild with `./build.sh`. It needs Node with Playwright, Python 3 with NumPy, and ffmpeg.

**Common edits:**

- **Caption wording and timing:** `HL_DEFS` near the top of the script in `reel.html`. `s` and `e` are the seconds over which each line's words light up.
- **Matching a recorded voiceover:** shift those `s`/`e` values to your recording, then re-run `./build.sh`.
- **Brand colours:** the `:root` tokens in `reel.html`. They currently match `styles/globals.css` on the website.

Fonts (Poppins, Inter, JetBrains Mono) are the website's own typefaces, from Fontsource, under the SIL Open Font License. The N monogram is `public/images/logo-mark-dark.png` from the website repository.
