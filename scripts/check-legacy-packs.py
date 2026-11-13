"""Check the evergreen Premium showcase against the selected Legacy catalog."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
catalog = json.loads((ROOT / 'assets/legacy-packs/catalog.json').read_text(encoding='utf-8'))
packs = catalog['packs']
expected = {'md-estelar':95, 'nm-numero':59, 'md-zodiaco':13,
            'nm-zodiaco-pixel':13, 'nm-zodiaco-chibi':13}
assert {p['id']:p['count'] for p in packs} == expected
assert sum(p['count'] for p in packs) == 193
for pack in packs:
    assert pack['shelf'] == 'legacy' and not pack['season']
    assert len(pack['samples']) == 3
    for sample in pack['samples']:
        assert (ROOT / 'assets/legacy-packs' / sample['src']).is_file()
    if pack['cover']:
        assert (ROOT / 'assets/legacy-packs' / pack['cover']).is_file()
for file in ['r-zen.html', 'r-zen-es.html']:
    page = (ROOT / file).read_text(encoding='utf-8')
    section = page.split('id="collections"',1)[1].split('</section>',1)[0]
    assert set(re.findall(r'data-pack-id="([^"]+)"', section)) == set(expected)
    assert len(re.findall(r'data-pack-id=', section)) == 5
    assert not re.search(r'Noir|Halloween|Muertos|Day of the Dead|Primavera Zen|Autumn Zen', section)
    assert '193' in section and 'Legacy' in section
print('PASS: Premium shows only the 5 evergreen Legacy packs (193 designs), in both languages; all covers and artwork samples exist.')
