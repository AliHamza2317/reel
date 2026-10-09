"""Downloads the generated photos listed in photos.json and prepares them for the reel
(cropped and resized to 1080x1920 JPEGs in assets/photos/). Needs network access to www.figma.com."""
import io, json, urllib.request
from pathlib import Path
from PIL import Image

here = Path(__file__).resolve().parent
out = here / 'assets' / 'photos'
out.mkdir(parents=True, exist_ok=True)
for name, url in json.load(open(here / 'photos.json')).items():
    if name.startswith('_'):
        continue
    data = urllib.request.urlopen(url, timeout=60).read()
    im = Image.open(io.BytesIO(data)).convert('RGB')
    s = max(1080 / im.width, 1920 / im.height)          # cover 1080x1920, centred
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l, t = (im.width - 1080) // 2, (im.height - 1920) // 2
    im.crop((l, t, l + 1080, t + 1920)).save(out / f'{name}.jpg', quality=92)
    print('saved', name)
