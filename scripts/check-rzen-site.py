"""Validate the generated landing pages, local links/assets, SEO and text contrast."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

def check_page(filename, lang):
    text = (ROOT / filename).read_text(encoding='utf-8')
    page = Page(text)
    assert '{{' not in text, f'{filename}: unresolved template expressions'
    assert '<html lang="' + lang + '">' in text
    assert sum(tag == 'h1' for tag, _ in page.tags) == 1
    assert '3.0.1' in text and '2027' in text
    title = re.search(r'<title>(.*?)</title>', text).group(1)
    assert '3.2' in title, 'Upcoming release must lead the page title'
    assert '2026-12' in text, 'Upcoming release month must be explicit'
    assert any(a.get('id') == 'next-release' for _, a in page.tags)
    assert 'ARRIVING OCTOBER' not in text
    ids = [attrs['id'] for _, attrs in page.tags if 'id' in attrs]
    assert len(ids) == len(set(ids)), f'{filename}: duplicate IDs'
    for tag, attrs in page.tags:
        if tag == 'img':
            assert 'alt' in attrs, f'{filename}: image missing alt'
        if tag == 'a' and attrs.get('target') == '_blank':
            assert 'noopener' in attrs.get('rel', '')
        for key in ['href', 'src']:
            raw = attrs.get(key)
            if not raw:
                continue
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            target = (ROOT / unquote(url.path)) if url.path else ROOT / filename
            assert target.is_file(), f'{filename}: missing file {raw}'
            if url.fragment and target.suffix == '.html':
                target_page = Page(target.read_text(encoding='utf-8'))
                assert any(a.get('id') == url.fragment for _, a in target_page.tags), f'{filename}: missing anchor {raw}'
    canonical = [a['href'] for t, a in page.tags if t == 'link' and a.get('rel') == 'canonical']
    assert canonical == ['https://rnxgames.com/' + filename]
    alternates = [a.get('hreflang') for t, a in page.tags if t == 'link' and a.get('rel') == 'alternate']
    assert set(alternates) == {'es', 'en', 'x-default'}
    schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', text, re.S).group(1))
    assert schema['softwareVersion'] == '3.0.1'
    assert len(schema['inLanguage']) == 8
    for prop in ['og:title', 'og:description', 'og:image', 'og:url']:
        assert any(t == 'meta' and a.get('property') == prop and a.get('content') for t, a in page.tags)
    print(f'PASS {filename}: static content, language, metadata, schema, images, local links and anchors')

def luminance(value):
    rgb = [int(value[i:i+2], 16) / 255 for i in [1, 3, 5]]
    linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
    return sum(a * b for a, b in zip(linear, [.2126, .7152, .0722]))

def check_contrast():
    css = (ROOT / 'assets/rzen-holiday.css').read_text(encoding='utf-8')
    for name, block in [('light', css.split(':root{', 1)[1].split('}', 1)[0]), ('dark', css.split(':root[data-theme=dark]{', 1)[1].split('}', 1)[0])]:
        colors = dict(re.findall(r'--([a-z-]+):(#[0-9a-f]{6})(?=;)', block))
        for fg, bg in [('ink', 'bg'), ('muted', 'bg'), ('gold', 'bg'), ('muted', 'surface'), ('gold', 'surface'), ('on-accent', 'accent')]:
            a, b = sorted([luminance(colors[fg]), luminance(colors[bg])])
            ratio = (b + .05) / (a + .05)
            assert ratio >= 4.5, f'{name}: {fg}/{bg} contrast {ratio:.2f}'
            print(f'PASS {name} {fg}/{bg}: {ratio:.2f}:1')
    for source in re.findall(r'url\([\'"]?(\./[^\'"\)]+)', css):
        assert (ROOT / 'assets' / source).is_file(), source

if __name__ == '__main__':
    check_page('r-zen.html', 'en')
    check_page('r-zen-es.html', 'es')
    check_contrast()
