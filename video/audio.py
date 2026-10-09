"""Synthesises the reel's sound: a minimal music bed plus UI sound effects.

Every cue is timed to the same seconds as reel.html, so the picture and the
sound stay locked. Writes two 48 kHz stereo WAVs:
  <out>/mix.wav       music + effects (the finished reel)
  <out>/sfx_only.wav  effects only, for adding your own music or voiceover
Usage: python3 audio.py <outDir>
"""
import sys
import wave
from pathlib import Path

import numpy as np

SR = 48000
DUR = 44.0
N = int(SR * DUR)
rng = np.random.default_rng(7)
music = np.zeros((N, 2))
sfx = np.zeros((N, 2))


def tt(d):
    return np.arange(int(d * SR)) / SR


def place(buf, t0, sig, gain=1.0, pan=0.0):
    i0 = int(round(t0 * SR))
    if i0 >= N or i0 < 0:
        return
    sig = sig[: N - i0] * gain
    a = (pan + 1) * np.pi / 4
    buf[i0 : i0 + len(sig), 0] += sig * np.cos(a) * np.sqrt(2)
    buf[i0 : i0 + len(sig), 1] += sig * np.sin(a) * np.sqrt(2)


def filt(x, lo=None, hi=None, order=2):
    """Zero-phase Butterworth-magnitude filter in the frequency domain."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    H = np.ones_like(f)
    if hi:
        H /= np.sqrt(1 + (f / hi) ** (2 * order))
    if lo:
        H *= 1 - 1 / np.sqrt(1 + (np.maximum(f, 1e-9) / lo) ** (2 * order))
    return np.fft.irfft(X * H, len(x))


def sweep_lp(x, f0, f1):
    """One-pole low-pass whose cutoff glides from f0 to f1 (short signals only)."""
    fc = np.geomspace(f0, f1, len(x))
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a[i]) * x[i] + a[i] * acc
        y[i] = acc
    return y


def fade(sig, a=0.003, r=0.01):
    n_a, n_r = int(a * SR), int(r * SR)
    env = np.ones(len(sig))
    if n_a:
        env[:n_a] = np.linspace(0, 1, n_a)
    if n_r:
        env[-n_r:] *= np.linspace(1, 0, n_r)
    return sig * env


# ----------------------------------------------------------------- effects
def ding(pitch=1.0):
    t = tt(0.45)
    s = np.zeros(len(t))
    for i, (f, g) in enumerate([(1975.5, 0.6), (2637.0, 0.4)]):
        d = 0.075 * i
        tm = np.clip(t - d, 0, None)
        s += g * np.sin(2 * np.pi * f * pitch * tm) * np.exp(-tm * 22) * (t >= d)
    s += 0.25 * np.sin(2 * np.pi * 987.8 * pitch * t) * np.exp(-t * 30)
    return fade(s, 0.002, 0.05)


def key_click():
    t = tt(0.025)
    n = rng.standard_normal(len(t)) * np.exp(-t * 320)
    return fade(filt(n, lo=1800, hi=7000), 0.0005, 0.005)


def mouse_click():
    t = tt(0.012)
    s = filt(rng.standard_normal(len(t)), lo=2500) * np.exp(-t * 600)
    s += 0.5 * np.sin(2 * np.pi * 3200 * t) * np.exp(-t * 900)
    return fade(s, 0.0003, 0.003)


def whoosh(d=0.4, f0=400, f1=5000, reverse=False):
    t = tt(d)
    u = t / d
    s = sweep_lp(rng.standard_normal(len(t)), f0, f1) * np.sin(np.pi * u) ** 2
    s = filt(s, lo=150)
    return s[::-1] if reverse else s


def thud():
    t = tt(1.0)
    f = 38 + 55 * np.exp(-t * 10)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 4.5)
    s += 0.3 * filt(rng.standard_normal(len(t)), hi=180) * np.exp(-t * 9)
    return fade(s, 0.004, 0.1)


def pop(f0=650, f1=1100):
    t = tt(0.09)
    f = np.linspace(f0, f1, len(t))
    return fade(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 45), 0.001, 0.02)


def message():
    out = np.zeros(int(0.35 * SR))
    for i, f in enumerate([1318.5, 1760.0]):
        t = tt(0.25)
        s = np.sin(2 * np.pi * f * t) * np.exp(-t * 18)
        i0 = int(i * 0.085 * SR)
        out[i0 : i0 + len(s)] += s
    return fade(out, 0.002, 0.05)


def chime():
    out = np.zeros(int(0.9 * SR))
    for i, f in enumerate([1046.5, 1318.5, 1568.0]):
        t = tt(0.7)
        s = (np.sin(2 * np.pi * f * t) + 0.2 * np.sin(4 * np.pi * f * t)) * np.exp(-t * 6)
        i0 = int(i * 0.07 * SR)
        out[i0 : i0 + len(s)] += s
    return fade(out, 0.002, 0.1)


def snap():
    t = tt(0.25)
    s = filt(rng.standard_normal(len(t)), lo=2000) * np.exp(-t * 260)
    s += 0.6 * np.sin(2 * np.pi * 3500 * t) * np.exp(-t * 300)
    s += 0.9 * np.sin(2 * np.pi * np.cumsum(70 + 90 * np.exp(-t * 40)) / SR) * np.exp(-t * 18)
    return fade(s, 0.0005, 0.03)


def riser(d):
    t = tt(d)
    u = t / d
    s = sweep_lp(rng.standard_normal(len(t)), 300, 7000) * u ** 2
    s += 0.35 * np.sin(2 * np.pi * np.cumsum(np.geomspace(220, 880, len(t))) / SR) * u ** 3
    return fade(filt(s, lo=120), 0.01, 0.006)


# ------------------------------------------------------------------- music
BEAT = 60 / 105
BAR = 4 * BEAT


def kick(vel=1.0):
    t = tt(0.5)
    f = 46 + 95 * np.exp(-t * 32)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5)
    s += 0.15 * filt(rng.standard_normal(len(t)), lo=1500) * np.exp(-t * 400)
    return fade(s, 0.0005, 0.05) * vel


def hat():
    t = tt(0.06)
    return fade(filt(rng.standard_normal(len(t)), lo=7000) * np.exp(-t * 90), 0.0005, 0.01)


def bass(f, d):
    t = tt(d)
    s = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t)
    return fade(s * np.exp(-t * 0.6), 0.008, min(0.15, d / 3))


def pad(freqs, d, cutoff=1200, attack=0.6, release=0.8):
    t = tt(d)
    s = np.zeros(len(t))
    for f in freqs:
        for det in (-0.0018, 0.0018):
            ph = rng.uniform(0, 2 * np.pi)
            for k in range(1, 8):
                s += np.sin(2 * np.pi * k * f * (1 + det) * t + ph * k) / k
    s = filt(s, hi=cutoff, order=2) / (len(freqs) * 4)
    s *= 1 + 0.08 * np.sin(2 * np.pi * 0.23 * t)
    return fade(s, attack, release)


def pluck(f):
    t = tt(0.7)
    s = np.sin(2 * np.pi * f * t) * np.exp(-t * 7) + 0.3 * np.sin(4 * np.pi * f * t) * np.exp(-t * 13)
    return fade(s, 0.002, 0.08)


def gate(buf, a, b, fade_s=0.02):
    """Silence the music bus between a and b, with short fades at the edges."""
    i0, i1 = int(a * SR), int(b * SR)
    nf = int(fade_s * SR)
    buf[i0 - nf : i0] *= np.linspace(1, 0, nf)[:, None]
    buf[i0:i1] = 0
    buf[i1 : i1 + nf] *= np.linspace(0, 1, nf)[:, None]


F = dict(F=([87.31], [174.61, 220.0, 261.63, 329.63]),
         G=([98.0], [196.0, 246.94, 293.66, 329.63]),
         Am=([110.0], [220.0, 261.63, 329.63, 392.0]),
         C=([65.41], [261.63, 329.63, 392.0, 493.88]))


def build_music():
    # 0–11.6 s: a low heartbeat pulse under a dark, filtered chord
    for k in range(int(11.55 / BEAT) + 1):
        place(music, k * BEAT, kick(0.55))
    place(music, 0, pad([110.0, 164.81, 246.94, 261.63], 11.8, cutoff=700, attack=0.05), 0.55)
    place(music, 0, fade(np.sin(2 * np.pi * 55 * tt(11.8)), 0.05, 0.3), 0.06)
    # 15–20.85 s: an open fifth returns under the "glue" graphic
    place(music, 15.0, pad([110.0, 164.81, 220.0], 6.0, cutoff=900, attack=1.2, release=0.05), 0.6)
    # 20.9 s onward: the drop, then the resolve
    t0 = 20.9
    chords = ['F', 'G', 'Am', 'C', 'F', 'G', 'Am', 'G', 'F', 'C']
    for b, name in enumerate(chords):
        start = t0 + b * BAR
        last = b == len(chords) - 1
        d = (DUR - start) if last else BAR + 0.05
        bf, pf = F[name]
        notes = pf + ([587.33] if last else [])
        place(music, start, pad(notes, d, cutoff=1600 if start < 31 else 1300, attack=0.04 if b == 0 else 0.25,
                                release=1.2 if last else 0.3), 0.75)
        place(music, start, bass(bf[0], d), 0.30)
        if last:
            continue
        soft = start >= 31.0 and start < 38.0
        pattern = [0, 1, 2, 3, 2, 1, 2, 3]
        for i, p in enumerate(pattern):
            place(music, start + i * BEAT / 2, pluck(pf[p] * 2), 0.035 if soft else 0.055, pan=(-0.35 if i % 2 else 0.35))
        for beat in range(4):
            bt = start + beat * BEAT
            if soft:
                if beat % 2 == 0:
                    place(music, bt, kick(0.45))
            else:
                place(music, bt, kick(0.8))
                place(music, bt + BEAT / 2, hat(), 0.05 if start < 31 else 0.035, pan=0.2)
    # a final, soft kick to land the resolve
    place(music, t0 + 9 * BAR, kick(0.6))
    gate(music, 11.6, 15.0)
    gate(music, 20.86, 20.9, fade_s=0.01)
    # fade out the tail
    nf = int(0.5 * SR)
    music[-nf:] *= np.linspace(1, 0, nf)[:, None] ** 2


def build_sfx():
    # hook: notifications landing
    for i, t in enumerate([0.0, 0.6, 1.2, 1.8]):
        place(sfx, t, ding(1.0 + 0.03 * (i % 2)), 0.22, pan=0.1 * (-1) ** i)
    place(sfx, 3.3, ding(), 0.24)                                      # the 9:47 PM enquiry
    place(sfx, 5.45, mouse_click(), 0.25); place(sfx, 5.95, mouse_click(), 0.22)
    for t in (6.0, 6.06):                                              # cmd + C
        place(sfx, t, key_click(), 0.2)
    for t in (6.45, 6.51):                                             # cmd + V
        place(sfx, t, key_click(), 0.2)
    for t in np.arange(6.6, 7.8, 0.075):                               # typing into the sheet
        place(sfx, t + rng.uniform(-0.015, 0.015), key_click(), rng.uniform(0.09, 0.16), pan=rng.uniform(-0.3, 0.3))
    for t in np.arange(8.02, 8.95, 0.055):                             # retyping into the CRM
        place(sfx, t + rng.uniform(-0.01, 0.01), key_click(), rng.uniform(0.09, 0.16), pan=rng.uniform(-0.3, 0.3))
    place(sfx, 9.5, whoosh(0.35, 500, 6000), 0.14)                     # the late reply goes out
    place(sfx, 11.15, message(), 0.09)                                 # "we've gone with someone else"
    place(sfx, 11.6, thud(), 0.75)                                     # music drops out
    place(sfx, 11.9, fade(filt(rng.standard_normal(int(3.4 * SR)), lo=200, hi=2500), 0.4, 0.4), 0.004)  # faint room tone
    for t in (15.1, 15.5, 15.9):                                       # tool cards appear
        place(sfx, t, pop(), 0.12)
    place(sfx, 19.6, riser(1.25), 0.16)                                # tension before the snap
    place(sfx, 20.9, snap(), 0.5)                                      # "Better systems"
    place(sfx, 22.0, whoosh(0.45, 600, 6000, reverse=True), 0.16)      # rewind
    place(sfx, 22.6, ding(), 0.24)                                     # same enquiry, same time
    place(sfx, 24.05, pop(500, 800), 0.08)
    place(sfx, 24.3, pop(900, 1200), 0.07)                             # typing dots
    place(sfx, 24.8, message(), 0.12)                                  # assistant replies
    place(sfx, 25.3, pop(700, 900), 0.07)
    place(sfx, 25.8, mouse_click(), 0.25)                              # slot tapped
    place(sfx, 26.05, chime(), 0.11)                                   # call booked
    place(sfx, 26.8, whoosh(0.3, 800, 7000), 0.1)
    place(sfx, 26.95, pop(800, 1300), 0.08)                            # CRM updated
    for t in (28.25, 28.45, 28.65):                                    # agenda items
        place(sfx, t, pop(600, 950), 0.06)
    place(sfx, 31.05, whoosh(0.5, 300, 4000), 0.1)                     # brand reveal
    place(sfx, 33.1, whoosh(0.35, 400, 5000), 0.08)                    # document slides in
    for t in (36.33, 36.72, 37.44):                                    # scope / timeline / price ticks
        place(sfx, t, pop(900, 1400), 0.07)
    place(sfx, 39.6, whoosh(0.4, 400, 5000), 0.09)                     # end card
    place(sfx, 41.15, chime(), 0.09)                                   # nuovadev.com
    place(sfx, 43.82, ding(), 0.2)                                     # loops into the opening


def write(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype('<i2').tobytes())


if __name__ == '__main__':
    out = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    out.mkdir(parents=True, exist_ok=True)
    build_music()
    build_sfx()
    mix = 0.8 * music + sfx
    limit = lambda x: np.tanh(1.3 * x) / np.tanh(1.3)
    g = 0.8 / np.max(np.abs(limit(mix)))                               # about -2 dBFS peak
    write(out / 'mix.wav', limit(mix) * g)
    write(out / 'sfx_only.wav', limit(sfx) * g)
    print('wrote', out / 'mix.wav', 'and', out / 'sfx_only.wav')
