"""Copy presentation-only animations from a read-only app snapshot into this website.

Never writes to the supplied source or asset root. No app runtime, saves or purchase code
is imported. Supply a stable snapshot so concurrent app edits cannot change the export.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent.parent

def balanced(text, start):
    opening = text.index('{', start)
    depth = 1
    cursor = opening + 1
    while depth:
        depth += (text[cursor] == '{') - (text[cursor] == '}')
        cursor += 1
    return text[start:cursor]

def div_at(text, start):
    depth = 0
    for token in re.finditer(r'</?div\b[^>]*>', text[start:]):
        depth += -1 if token.group().startswith('</') else 1
        if depth == 0:
            return text[start:start + token.end()]
    raise ValueError('Unclosed preview div')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--asset-root', type=Path, required=True)
    args = parser.parse_args()
    source_bytes = args.source.read_bytes()
    source = source_bytes.decode('utf-8')
    dest = ROOT / 'assets/app-previews'
    dest.mkdir(exist_ok=True)
    styles = '\n'.join(re.findall(r'<style\b[^>]*>(.*?)</style>', source, re.S))
    selectors = ['.md-family-thumb', '.md-family-thumb::after',
                 '.md-thumb-trad', '.md-thumb-trad::before',
                 '.md-thumb-illustration', '.md-thumb-illustration::before',
                 '.md-thumb-reveal', '.md-thumb-reveal::before', '.md-thumb-reveal::after',
                 '.md-magic-thumb', '.md-magic-thumb::before', '.md-magic-thumb::after',
                 '.md-thumb-pbn', '.md-thumb-pbn::before',
                 '.md-thumb-vida', '.md-thumb-vida::before',
                 '.md-family-free-glyph', '.md-family-free-glyph svg',
                 '.md-family-free-glyph path:first-child', '.md-family-free-glyph path:last-child']
    rules = []
    # Copy the first base rule for each selector. Later app media-query overrides
    # must not be flattened into unconditional rules in the website export.
    for selector in selectors:
        match = re.search(re.escape(selector) + r'\s*\{', styles)
        if not match:
            raise ValueError('Missing original selector: ' + selector)
        rules.append(balanced(styles, match.start()))
    names = ['mdMandalaTurn', 'mdIllustrationFloat', 'mdSparkle', 'mdVidaFloat',
             'mdMagicCover', 'mdPbnArtSweep', 'mdFamilyReveal', 'mdFamilyRevealSpark',
             'mdVidaShine', 'mdFreeStroke', 'mdFreeWiggle', 'asmTL', 'asmTR', 'asmBL',
             'asmBR', 'slideRt', 'slideDn', 'swapTileA', 'swapTileB', 'swapSelect',
             'pzGlowPulse', 'pzSpark']
    for name in names:
        match = re.search(r'@keyframes\s+' + name + r'\s*\{', styles)
        if not match:
            raise ValueError('Missing original animation: ' + name)
        rules.append(balanced(styles, match.start()))
    css = '\n'.join(rules).replace('assets/ui/families/', './app-previews/')
    files = []
    for name in sorted(set(re.findall(r'app-previews/([\w-]+\.webp)', css))):
        content = (args.asset_root / 'ui/families' / name).read_bytes()
        (dest / name).write_bytes(content)
        files.append({'file': name, 'sha256': hashlib.sha256(content).hexdigest()})
    (ROOT / 'assets/app-previews.css').write_text(
        '/* Presentation animations copied from the app snapshot; see app-previews/provenance.json. */\n' + css + '\n', encoding='utf-8')
    previews = {}
    for key, cls in [('traditional','md-thumb-trad'), ('illustrations','md-thumb-illustration'),
                     ('reveal','md-thumb-reveal'), ('magic-color','md-magic-thumb'),
                     ('by-number','md-thumb-pbn'), ('comes-alive','md-thumb-vida')]:
        previews[key] = '<span class="md-family-thumb ' + cls + '"></span>'
    glyph_start = source.index('<span class="md-family-free-glyph">', source.index('<!--'))
    glyph_end = source.index('</svg></span>', glyph_start) + len('</svg></span>')
    previews['free'] = source[glyph_start:glyph_end]
    for key, action in [('classic','chooseClassic'), ('slide','chooseSlide'), ('swap','chooseSwap')]:
        action_start = source.index('onClick="{{ ' + action + ' }}"')
        start = source.index('<div data-deco="1"', action_start)
        markup = div_at(source, start)
        markup = markup.replace('data-deco="1"', 'class="app-puzzle-demo" data-puzzle-kind="' + key + '"' + ('' if key == 'classic' else ' hidden'))
        markup = markup.replace('{{ modeAnimBox }}', '190').replace('{{ pzModeArtFilter }}', 'none')
        markup = markup.replace('{{ modeAnimScale }}', 'var(--puzzle-scale,1.15)')
        if '{{' in markup or re.search(r'on\w+=', markup):
            raise ValueError('App-specific binding in copied presentation')
        previews['puzzle-' + key] = markup
    (dest / 'markup.json').write_text(json.dumps(previews, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    provenance = {'source':'R-Zen app index.html (local read-only snapshot)',
                  'sourceSha256':hashlib.sha256(source_bytes).hexdigest(),
                  'animationNames':names,'assets':files,
                  'changes':'Presentation only; website wrapper sizing and local asset URLs. App files were read, never written.'}
    (dest / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
    print(f'Copied {len(names)} original keyframes, {len(files)} images and {len(previews)} previews into website assets.')

if __name__ == '__main__':
    main()
