"""Shared helpers for the ATSWA extraction pipeline."""
import re, unicodedata

# ── page furniture ────────────────────────────────────────────────────────
FURNITURE = [
    re.compile(r'^\s*\d{1,3}\s*$'),                       # bare page number
    re.compile(r'^\s*0{1,3}\s*$'),                        # stray artefacts in QA text
    re.compile(r'^\s*AT/\d+/PII\.\d+\s*$', re.I),
    re.compile(r'^\s*Examination No\.', re.I),
    re.compile(r'^\s*(THE )?ASSOCIATION OF ACCOUNTANCY BODIES', re.I),
    re.compile(r'^\s*ACCOUNTING TECHNICIANS SCHEME', re.I),
    re.compile(r'^\s*THE INSTITUTE OF CHARTERED\s*$', re.I),
    re.compile(r'^\s*ACCOUNTANTS OF NIGERIA\s*$', re.I),
    re.compile(r'^\s*ATSWA\s+PART\s+II\s*$', re.I),
    re.compile(r'^\s*Time Allowed:', re.I),
]

def strip_furniture(lines):
    return [l for l in lines if not any(p.match(l) for p in FURNITURE)]

# ── Adobe Symbol font ─────────────────────────────────────────────────────
# pdftotext emits Symbol-font glyphs in the private-use area (U+F0xx = Symbol
# char 0xXX). Decoding them is what turns the QA papers back into mathematics.
SYMBOL = {
    0x28: '(', 0x29: ')', 0x2B: '+', 0x2D: '\u2212', 0x3C: '<', 0x3D: '=',
    0x3E: '>', 0x5B: '[', 0x5C: '\u2234', 0x5D: ']', 0x7B: '{', 0x7D: '}',
    0x44: '\u0394', 0x4C: '\u039b', 0x53: '\u03a3', 0x54: '\u03a4',
    0x55: '\u03a5', 0x57: '\u03a9',
    0x61: '\u03b1', 0x62: '\u03b2', 0x63: '\u03c7', 0x64: '\u03b4',
    0x65: '\u03b5', 0x66: '\u03c6', 0x67: '\u03b3', 0x68: '\u03b7',
    0x69: '\u03b9', 0x6C: '\u03bb', 0x6D: '\u03bc', 0x6E: '\u03bd',
    0x6F: '\u03bf', 0x70: '\u03c0', 0x71: '\u03b8', 0x72: '\u03c1',
    0x73: '\u03c3', 0x74: '\u03c4', 0x75: '\u03c5', 0x77: '\u03c9',
    0x78: '\u03be', 0x79: '\u03c8', 0x7A: '\u03b6',
    0xA3: '\u2264', 0xA5: '\u221e', 0xA7: '\u2022', 0xAC: '\u2190',
    0xAE: '\u2192', 0xB0: '\u00b0', 0xB1: '\u00b1', 0xB3: '\u2265',
    0xB4: '\u00d7', 0xB5: '\u221d', 0xB6: '\u2202', 0xB7: '\u00b7',
    0xB8: '\u00f7', 0xB9: '\u2260', 0xBA: '\u2261', 0xBB: '\u2248',
    0xC7: '\u2229', 0xC8: '\u222a', 0xCD: '\u21d1', 0xCE: '\u2286',
    0xCF: '\u2282', 0xD0: '\u2208', 0xD1: '\u2209', 0xD6: '\u221a',
    0xD7: '', 0xDE: '\u21d2', 0xDF: '\u21d4',
    0xE5: '\u2211', 0xE6: '(', 0xE7: '', 0xE8: '', 0xE9: '[', 0xEA: '',
    0xEB: '', 0xF2: '\u222b', 0xF3: '', 0xF5: '', 0xF6: ')', 0xF7: '',
    0xF8: '', 0xF9: ']', 0xFA: '', 0xFB: '',
}
_PUA = {0xF000 + k: v for k, v in SYMBOL.items()}


def desymbol(s):
    """Map Symbol-font private-use codepoints back to real Unicode maths."""
    if not any(0xE000 <= ord(c) <= 0xF8FF for c in s):
        return s
    out = []
    for c in s:
        o = ord(c)
        if 0xE000 <= o <= 0xF8FF:
            out.append(_PUA.get(o, _PUA.get(0xF000 + (o & 0xFF), '')))
        else:
            out.append(c)
    return ''.join(out)


# ── typography ────────────────────────────────────────────────────────────
LIG = {'ﬁ': 'fi', 'ﬂ': 'fl', 'ﬀ': 'ff', 'ﬃ': 'ffi', 'ﬄ': 'ffl'}

def tidy(s):
    """Normalise the typographic noise pdftotext leaves behind."""
    s = desymbol(s)
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '—')
    s = s.replace(' ', ' ')
    s = re.sub(r'\s+([,;:.])', r'\1', s)          # space before punctuation
    s = re.sub(r'[ \t]{2,}', ' ', s)
    return s.strip()

def money(s):
    """N5000 / N5,000 -> naira sign with thousands separators kept as written."""
    s = re.sub(r'\bN(?=[\d(])', '₦', s)
    s = re.sub(r'\bGH¢', 'GH¢', s)
    return s

def squeeze(lines):
    """Collapse runs of blank lines to one."""
    out, blank = [], False
    for l in lines:
        if l.strip():
            out.append(l.rstrip()); blank = False
        elif not blank:
            out.append(''); blank = True
    while out and not out[0]:
        out.pop(0)
    while out and not out[-1]:
        out.pop()
    return out

def slug(s, n=64):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s[:n].rstrip('-')
