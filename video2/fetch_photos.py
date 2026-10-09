"""Prepares the six reel photos listed in photos.json as 1080x1920 JPEGs in assets/photos/.

For each photo it uses, in order:
  1. a file already in assets/photos/ named <name>.png / .jpg / .jpeg / .webp (e.g. uploaded to GitHub), or
  2. a download from the link in photos.json (needs network access to www.figma.com).
"""
import io, json, urllib.request
from pathlib import Path
from PIL import Image

here = Path(__file__).resolve().parent
out = here / 'assets' / 'photos'
out.mkdir(parents=True, exist_ok=True)
for name, url in json.load(open(here / 'photos.json')).items():
    if name.startswith('_'):
        continue
    src = next((p for ext in ('png', 'jpeg', 'webp', 'jpg') for p in [out / f'{name}.{ext}'] if p.exists()), None)
    try:
        im = Image.open(src) if src else Image.open(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
    except Exception as e:  # keep going: a missing photo just falls back to the brand background
        print('skipped', name, '-', e)
        continue
    im = im.convert('RGB')
    s = max(1080 / im.width, 1920 / im.height)          # cover 1080x1920, centred
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - 1080) // 2, (im.height - 1920) // 2
    im.crop((l, t, l + 1080, t + 1920)).save(out / f'{name}.jpg', quality=92)
    print('ready', name, '(from', 'upload)' if src else 'download)')
