"""Check copied presentation assets and animation references without opening the app."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets/app-previews'
provenance = json.loads((ASSETS / 'provenance.json').read_text())
markup = json.loads((ASSETS / 'markup.json').read_text(encoding='utf-8'))
css = (ROOT / 'assets/app-previews.css').read_text(encoding='utf-8')
layout = (ROOT / 'assets/app-preview-layout.css').read_text(encoding='utf-8')
names = set(re.findall(r'@keyframes\s+([\w-]+)', css))
assert names == set(provenance['animationNames'])
assert len(markup) == 10
assert '{{' not in css + ''.join(markup.values())
assert not re.search(r'\bon\w+\s*=', ''.join(markup.values()), re.I)
assert 'animation:none' not in css.replace(' ', ''), 'App media overrides must not become unconditional'
for item in provenance['assets']:
    data = (ASSETS / item['file']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256'], item['file']
for reference in re.findall(r'url\([\'"]?(\./[^\'"\)]+)', css):
    assert (ROOT / 'assets' / reference).is_file(), reference
for text in [css, *markup.values()]:
    for name in re.findall(r'animation\s*:\s*([a-zA-Z][\w-]*)', text):
        assert name in names, 'Undefined copied animation: ' + name
assert 'prefers-reduced-motion:reduce' in layout
assert 'animation-play-state:paused!important' in layout
for file in ['r-zen.html', 'r-zen-es.html']:
    page = (ROOT / file).read_text(encoding='utf-8')
    assert page.count('data-app-mode=') == 8
    assert page.count('data-puzzle-choice=') == 3
    assert 'data-preview-motion' in page
    assert not re.search(r'<script[^>]+src=["\'][^"\']*(?:data/|support\.js)', page)
print(f'PASS: {len(names)} original keyframes, {len(provenance["assets"])} exact asset copies, 10 previews, 8 mode cards in both languages; no app handlers or runtime imported.')
