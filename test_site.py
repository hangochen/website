"""Dependency-free checks: python3 -m unittest -v test_site.py."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def contrast(a, b):
    def luminance(value):
        c = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
        c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
        return sum(x * y for x, y in zip(c, (.2126, .7152, .0722)))
    values = sorted((luminance(a), luminance(b)))
    return (values[1] + .05) / (values[0] + .05)


class SiteChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / 'index.html').read_text()
        cls.page = Page(cls.html)

    def test_section_anchors_resolve_and_ids_are_unique(self):
        ids = [a['id'] for _, a in self.page.elements if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        for tag, attrs in self.page.elements:
            if tag == 'a' and attrs.get('href', '').startswith('#'):
                self.assertIn(attrs['href'][1:], ids)
        self.assertTrue({'about', 'research', 'teaching', 'conferences', 'contact'} <= set(ids))

    def test_content_available_without_javascript(self):
        sections = [a for t, a in self.page.elements if t == 'section']
        self.assertTrue(sections)
        self.assertTrue(all('hidden' not in a for a in sections))
        self.assertIn('<noscript><p id="email-fallback">Email: hangu.chen [at] du [dot] edu.', self.html)
        self.assertIn('href="#email-fallback"', self.html)

    def test_assets_and_external_links(self):
        for tag, attrs in self.page.elements:
            for key in ('src', 'href'):
                ref = attrs.get(key, '')
                if ref and not ref.startswith(('https:', 'http:', '#', 'mailto:', 'data:')):
                    self.assertTrue((ROOT / ref.split('?', 1)[0]).is_file(), ref)
            if tag == 'a' and attrs.get('target') == '_blank':
                self.assertIn('noopener', attrs.get('rel', '').split())
        for expected in (
            'https://papers.ssrn.com/Sol3/Cf_Dev/AbsByAuth.cfm?per_id=4823658',
            'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4544083',
            'https://www.linkedin.com/in/hangu-chen-649a55129/',
        ):
            self.assertIn(expected, self.html)

    def test_meaningful_text_color_pairs_pass_aa(self):
        for fg, bg in (
            ('#000000', '#FFFFFF'), ('#54565B', '#FFFFFF'),
            ('#BA0C2F', '#FFFFFF'), ('#FFFFFF', '#BA0C2F'),
            ('#F7F5F0', '#141414'), ('#C5C2BA', '#141414'),
            ('#EF8C9F', '#141414'), ('#C5C2BA', '#1D1D1D'),
            ('#EF8C9F', '#1D1D1D'),
        ):
            with self.subTest(fg=fg, bg=bg):
                self.assertGreaterEqual(contrast(fg, bg), 4.5)


if __name__ == '__main__':
    unittest.main()
