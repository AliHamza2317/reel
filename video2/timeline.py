"""Builds the 45-second timeline (Version B narration) shared by the video,
the captions (.srt) and the production blueprint.

Word times come from syllable counts at a natural read (~4.5 syllables/s,
roughly 165-170 words per minute) plus the pauses marked below, then scaled so
the final word ends 0.8 s before 45.0 s.  Usage: python3 timeline.py <out.json> <out.srt>
"""
import json, re, sys

TOTAL, END_HOLD, START = 45.0, 0.7, 0.15
# (scene, caption chunk, pause AFTER this chunk in seconds, highlighted words)
CHUNKS = [
    (1, "Before you spend thousands", 0.0, ["thousands"]),
    (1, "building your app,", 0.0, []),
    (1, "watch this.", 0.35, ["watch", "this."]),
    (2, "Your idea might be brilliant.", 0.3, ["brilliant."]),
    (2, "But have you proven", 0.0, []),
    (2, "that people actually want it?", 0.4, ["actually", "want", "it?"]),
    (3, "Too many founders build", 0.0, []),
    (3, "dozens of features", 0.0, ["dozens", "of", "features"]),
    (3, "before getting real feedback.", 0.15, ["real", "feedback."]),
    (3, "Months of development.", 0.12, ["Months"]),
    (3, "A growing budget.", 0.12, ["budget."]),
    (3, "And one question:", 0.28, []),
    (3, "will anyone use it?", 0.42, ["will", "anyone", "use", "it?"]),
    (4, "Start with an MVP.", 0.22, ["MVP."]),
    (4, "Build only the core features", 0.0, ["core"]),
    (4, "needed to solve", 0.0, []),
    (4, "one real problem.", 0.3, ["one", "real", "problem."]),
    (5, "Put it in front", 0.0, []),
    (5, "of real users.", 0.18, ["real", "users."]),
    (5, "Learn what works.", 0.18, ["Learn"]),
    (5, "Improve what doesn't.", 0.32, ["Improve"]),
    (6, "At NuovaDev,", 0.05, ["NuovaDev,"]),
    (6, "we turn ideas", 0.0, []),
    (6, "into working products —", 0.1, ["working", "products"]),
    (6, "with a focused scope,", 0.0, ["focused", "scope,"]),
    (6, "clear milestones,", 0.0, ["milestones,"]),
    (6, "and working software", 0.0, ["working", "software"]),
    (6, "every two weeks.", 0.32, ["every", "two", "weeks."]),
    (7, "Don't just build more.", 0.12, []),
    (7, "Build smarter.", 0.3, ["smarter."]),
    (7, "Book a free", 0.0, ["free"]),
    (7, "30-minute consultation.", 0.18, ["30-minute"]),
    (7, "Let's figure out", 0.0, []),
    (7, "what your first version", 0.0, ["first", "version"]),
    (7, "actually needs.", 0.0, ["needs."]),
]
SPECIAL = {'mvp': 3, 'nuovadev': 4, '30-minute': 4, 'actually': 4, 'development': 4, 'consultation': 4, 'anyone': 3,
           'idea': 3, 'ideas': 3, 'every': 2, "doesn't": 2, "let's": 1, 'business': 2}

def syl(w):
    w = w.lower().strip(".,?!:—'")
    if w in SPECIAL: return SPECIAL[w]
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1 and not w.endswith(('le', 'ee')): n -= 1
    return max(1, n)

words = []
for ci, (sc, text, pause, keys) in enumerate(CHUNKS):
    toks = [t for t in text.split(' ') if t != '—']
    for j, t in enumerate(toks):
        words.append(dict(chunk=ci, scene=sc, text=t, key=t in keys, syl=syl(t), pause=pause if j == len(toks) - 1 else 0.0))
pauses = sum(w['pause'] for w in words)
speech = TOTAL - END_HOLD - START - pauses
per_syl = speech / sum(w['syl'] for w in words)
t = START
for w in words:
    w['t0'] = round(t, 3); t += w['syl'] * per_syl; w['t1'] = round(t, 3); t += w['pause']

chunks = []
for ci, (sc, text, pause, keys) in enumerate(CHUNKS):
    ws = [w for w in words if w['chunk'] == ci]
    chunks.append(dict(scene=sc, text=text, t0=ws[0]['t0'], t1=ws[-1]['t1'], words=[dict(text=w['text'], t0=w['t0'], key=w['key']) for w in ws]))
# a scene starts 0.12 s before its first word (cut on the breath); scene 1 starts at 0
scenes = []
for sc in range(1, 8):
    cs = [c for c in chunks if c['scene'] == sc]
    scenes.append(dict(scene=sc, start=0.0 if sc == 1 else round(cs[0]['t0'] - 0.12, 2), vo_start=cs[0]['t0'], vo_end=cs[-1]['t1']))
for i, s in enumerate(scenes):
    s['end'] = scenes[i + 1]['start'] if i + 1 < len(scenes) else TOTAL

rate_wpm = len(words) / (speech / 60)
json.dump(dict(total=TOTAL, wpm=round(rate_wpm), syl_per_s=round(1 / per_syl, 2), scenes=scenes, chunks=chunks), open(sys.argv[1], 'w'), indent=1)

def ts(x):
    ms = int(round(x * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
with open(sys.argv[2], 'w') as f:
    for i, c in enumerate(chunks, 1):
        end = min(c['t1'] + 0.25, chunks[i]['t0'] - 0.02) if i < len(chunks) else TOTAL - 0.1
        f.write(f"{i}\n{ts(c['t0'])} --> {ts(end)}\n{c['text']}\n\n")
print(f"{len(words)} words, {rate_wpm:.0f} wpm, {1/per_syl:.2f} syl/s, pauses {pauses:.1f}s")
for s in scenes: print(f"Scene {s['scene']}: {s['start']:5.2f}–{s['end']:5.2f}  (VO {s['vo_start']:.2f}–{s['vo_end']:.2f})")

# the renderer reads the same data as a script (file:// pages cannot fetch JSON)
import os
with open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'timeline.js'), 'w') as f:
    f.write('window.TL = ' + json.dumps(dict(total=TOTAL, scenes=scenes, chunks=chunks)) + ';\n')
