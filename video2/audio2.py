"""Music bed and sound design for reel 2, cued from timeline.json.

Reuses the synth voices in ../video/audio.py. Writes 48 kHz stereo WAVs:
  <out>/mix.wav     music + effects at full level (the finished, voiceover-free reel)
  <out>/vo_bed.wav  the same, about 9 dB lower, for laying a recorded voiceover on top
Usage: python3 audio2.py <outDir>
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'video'))
import audio as A  # noqa: E402  (synth voices only; its own buffers are unused)

SR, DUR = A.SR, 45.0
N = int(SR * DUR)
music = np.zeros((N, 2))
sfx = np.zeros((N, 2))
TL = json.load(open(Path(__file__).with_name('timeline.json')))
CH = TL['chunks']
SC = {s['scene']: s for s in TL['scenes']}
ct = lambda txt: next(c for c in CH if c['text'].startswith(txt))['t0']
wt = lambda txt, w: next(x for x in next(c for c in CH if c['text'].startswith(txt))['words'] if x['text'].startswith(w))['t0']


def place(buf, t0, sig, gain=1.0, pan=0.0):
    i0 = int(round(t0 * SR))
    if not 0 <= i0 < N:
        return
    sig = sig[: N - i0] * gain
    a = (pan + 1) * np.pi / 4
    buf[i0:i0 + len(sig), 0] += sig * np.cos(a) * np.sqrt(2)
    buf[i0:i0 + len(sig), 1] += sig * np.sin(a) * np.sqrt(2)


def env_gain(buf, points):
    """Multiply the bus by a piecewise-linear gain curve [(t, g), ...]."""
    ts, gs = zip(*points)
    buf *= np.interp(np.arange(N) / SR, ts, gs)[:, None]


def impact():
    t = A.tt(1.6)
    boom = np.sin(2 * np.pi * np.cumsum(28 + 40 * np.exp(-t * 6)) / SR) * np.exp(-t * 2.6)
    body = A.filt(A.rng.standard_normal(len(t)), hi=400) * np.exp(-t * 7) * 0.5
    crack = A.filt(A.rng.standard_normal(len(t)), lo=3000) * np.exp(-t * 60) * 0.25
    return A.fade(boom + body + crack, 0.002, 0.3)


BEAT = 60 / 96
CH_MIN = {'Am': ([110.0], [220.0, 261.63, 329.63]), 'F': ([87.31], [174.61, 220.0, 261.63]),
          'Dm': ([73.42], [146.83, 220.0, 293.66]), 'E': ([82.41], [164.81, 207.65, 246.94])}
CH_MAJ = {'C': ([65.41], [261.63, 329.63, 392.0, 493.88]), 'G': ([98.0], [196.0, 246.94, 293.66, 392.0]),
          'Am': ([110.0], [220.0, 261.63, 329.63, 392.0]), 'F': ([87.31], [174.61, 220.0, 261.63, 329.63])}


def build_music():
    s3, s4, s5, s6, s7 = (SC[i]['start'] for i in (3, 4, 5, 6, 7))
    q = wt('will anyone', 'will')
    # 0 – s4: dark, restrained: a filtered minor pad, a sub drone and a slow pulse
    place(music, 0, A.pad([110.0, 164.81, 261.63], s4 + 0.4, cutoff=650, attack=0.02, release=0.4), 0.6)
    place(music, 0, A.fade(np.sin(2 * np.pi * 55 * A.tt(s4 + 0.4)), 0.02, 0.4), 0.07)
    for k in range(int(s3 / (2 * BEAT))):
        place(music, 0.6 + k * 2 * BEAT, A.kick(0.35))
    # s3: the problem builds: pulse on every beat, a ticking hat, a darker progression
    bar = 4 * BEAT
    for b, name in enumerate(['Am', 'F', 'Dm', 'E']):
        st = s3 + b * bar * 1.0
        if st >= q:
            break
        bf, pf = CH_MIN[name]
        place(music, st, A.pad(pf, min(bar + 0.05, q - st + 0.3), cutoff=900 + 250 * b, attack=0.2, release=0.25), 0.5)
        place(music, st, A.bass(bf[0], min(bar, q - st)), 0.22)
    t = s3
    while t < q - 0.05:
        place(music, t, A.kick(0.5))
        place(music, t + BEAT / 2, A.hat(), 0.04, pan=0.2)
        t += BEAT
    # s4: it opens up: brighter major chords and soft plucks, no drums yet
    prog = ['C', 'G', 'Am', 'F', 'C', 'G', 'Am', 'F', 'C', 'G', 'C']
    t, i = s4, 0
    while t < DUR - 0.1:
        name = prog[i % len(prog)] if t < s7 + 4 * BEAT * 1.0 else 'C'
        last = t >= ct("Let's figure") - 0.6
        d = (DUR - t) if last else bar + 0.05
        bf, pf = CH_MAJ[name]
        notes = pf + ([587.33] if last else [])
        place(music, t, A.pad(notes, d, cutoff=1500, attack=0.05 if i == 0 else 0.25, release=1.0 if last else 0.3), 0.7)
        if t >= s5 - 0.05:
            place(music, t, A.bass(bf[0], d), 0.26)
        soft = t < s5 or t >= s7
        for j, p in enumerate([0, 1, 2, 3, 2, 1, 2, 3]):
            if t + j * BEAT / 2 < DUR - 1.0 and not last:
                place(music, t + j * BEAT / 2, A.pluck(pf[p % len(pf)] * 2), 0.035 if soft else 0.05, pan=(-0.3 if j % 2 else 0.3))
        if last:
            break
        t += bar
        i += 1
    # s5–s7: a light groove under the solution and the brand
    t = s5
    while t < s7 - 0.05:
        place(music, t, A.kick(0.65 if t >= s6 else 0.55))
        place(music, t + BEAT / 2, A.hat(), 0.045, pan=0.2)
        t += BEAT
    # level shape: dip for "people actually want it?", near-silence for "will anyone use it?"
    a2 = wt('that people', 'actually')
    env_gain(music, [(0, 1), (a2 - 0.2, 1), (a2 + 0.2, 0.45), (SC[3]['start'], 0.45), (SC[3]['start'] + 0.3, 1),
                     (q - 0.25, 1), (q, 0.12), (s4 - 0.05, 0.12), (s4 + 0.1, 1), (DUR - 0.7, 1), (DUR, 0)])


def build_sfx():
    s2, s3, s4, s5, s6, s7 = (SC[i]['start'] for i in (2, 3, 4, 5, 6, 7))
    place(sfx, 0.0, impact(), 0.55)                                         # restrained opening impact
    place(sfx, s2, A.whoosh(0.35, 300, 3000), 0.06)
    for k in range(10):                                                     # pencil on paper
        place(sfx, s2 + 0.1 + k * 0.17, A.fade(A.filt(A.rng.standard_normal(int(0.12 * SR)), lo=2500, hi=6000), 0.01, 0.04), 0.03)
    mc = ct('But have you') - 0.25
    place(sfx, mc, A.whoosh(0.3, 600, 5000), 0.08)                          # match cut
    for i in range(38):                                                     # backlog rows typed in
        place(sfx, s3 + 0.1 + i * 0.07, A.key_click(), A.rng.uniform(0.07, 0.12), pan=A.rng.uniform(-0.3, 0.3))
    tB = ct('before getting') + 0.3
    for i in range(6):                                                      # board cards
        place(sfx, tB + 0.1 + i * 0.22, A.pop(500, 700), 0.05)
    tC = ct('Months')
    for i in range(9):                                                      # months ticking by
        place(sfx, tC + 0.05 + i * (ct('A growing') - 0.25 - tC) / 9, A.mouse_click(), 0.16)
    place(sfx, ct('A growing') + 0.05, A.riser(1.0), 0.07)                  # budget creeping up
    place(sfx, wt('will anyone', 'will'), A.thud(), 0.55)                   # low accent on the question
    place(sfx, s4, A.whoosh(0.7, 300, 6000), 0.12)                          # the clutter clears
    demo = ct('Build only') - 0.1
    for at in (demo + 0.35, demo + 1.8):                                    # taps in the prototype
        place(sfx, at, A.mouse_click(), 0.2)
    for i in range(20):
        place(sfx, demo + 0.65 + i * 0.045, A.key_click(), 0.07)
    place(sfx, wt('one real', 'one') + 0.05, A.chime(), 0.09)               # task done
    beats = [s5, wt('of real users', 'real') - 0.2, ct('Learn'), ct('Improve')]
    for i, b in enumerate(beats):                                          # build / test / learn / improve
        place(sfx, b, A.pop(700 + 120 * i, 1100 + 150 * i), 0.1)
        place(sfx, b, A.pluck([523.25, 587.33, 659.25, 783.99][i]), 0.06)
    for at in (beats[1] + 0.05, beats[1] + 0.4, beats[1] + 0.75):
        place(sfx, at, A.mouse_click(), 0.16)
    place(sfx, s6, A.whoosh(0.45, 400, 5000), 0.08)
    place(sfx, wt('At NuovaDev', 'NuovaDev') - 0.1, A.chime(), 0.06)        # logo
    for txt in ('with a focused', 'clear milestones', 'and working'):      # three cards
        place(sfx, ct(txt) - 0.05, A.pop(600, 950), 0.08)
    for w in ('every', 'two', 'weeks.'):
        place(sfx, wt('every two', w) - 0.1, A.pop(900, 1300), 0.06)
    place(sfx, ct('Build smarter') - 0.05, impact()[: int(0.8 * SR)] * 0.5, 0.35)
    place(sfx, ct('Book a free') - 0.15, A.whoosh(0.4, 400, 5000), 0.08)
    place(sfx, ct('Book a free') - 0.15 + 1.55, A.mouse_click(), 0.2)       # "Schedule a meeting"
    place(sfx, ct("Let's figure") - 0.15, A.chime(), 0.09)                  # end frame


def write(path, x):
    A.write(path, x)


if __name__ == '__main__':
    out = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    out.mkdir(parents=True, exist_ok=True)
    build_music()
    build_sfx()
    limit = lambda x: np.tanh(1.3 * x) / np.tanh(1.3)
    mix = limit(0.8 * music + sfx)
    g = 0.8 / np.max(np.abs(mix))
    write(out / 'mix.wav', mix * g)
    write(out / 'vo_bed.wav', limit(0.8 * 0.35 * music + 0.6 * sfx) * g)
    print('wrote', out / 'mix.wav', 'and', out / 'vo_bed.wav')
