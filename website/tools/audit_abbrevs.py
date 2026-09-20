#!/usr/bin/env python3
"""
For every PS chapter, find ALL-CAPS abbreviations that are used but never
spelled out *in that chapter* — candidates for a past exam question along
the lines of "the acronym X means...".

Method: collect every "(ABBR)" the chapter already writes out somewhere
(e.g. "Pension Fund Administrator (PFA)") — that's a defined abbreviation.
Then collect every bare use of an all-caps 2-6 letter token. Anything used
bare that was never defined *anywhere in that chapter* is flagged.

Common cross-chapter abbreviations that are conventionally assumed known
throughout the site (IPSAS, VAT, etc. — defined once, early, used site-wide)
are excluded via a fixed allow-list rather than flagged in every chapter
that merely uses them.
"""
import importlib.util, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'website' / 'content' / 'ps'

ALLOW = set('''IPSAS IPSASB IFAC IASB IFRS VAT GDP PDF ATSWA CIT PPT PAYE PII NASS
FCT ICAN ANAN CBN SEC NDIC NCC NAICOM DVEA MDA MDAs LGA LGAs FRN NGO NGOs
FGN CRF USD GBP NGN CAP LFN FR ATC OK CEO CFO MD PLC USA UK UN AI IT ID
NOT EXCEPT ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ALL ANY NO YES
AND OR IN ON AT BY FOR FROM THE DO BE IS AS TO OF IF SO UP GO NEW OLD OWN
CASH ASSETS ASSET EQUITY NET TOTAL YEAR FLOWS NIL XX XXX XXXX DR CR NGN
I II III IV V VI VII VIII IX X TV UV PV DF BB US TB PS DG HQ CS
'''.split())

RE_ABBR_TOKEN = re.compile(r'\b([A-Z]{2,6})s?\b')
RE_DEFINED = re.compile(r'\(([A-Z]{2,6})s?\)')


def bag_of(node, acc):
    if node is None:
        return
    if isinstance(node, str):
        acc.append(node)
    elif isinstance(node, list):
        for v in node:
            bag_of(v, acc)
    elif isinstance(node, dict):
        for v in node.values():
            bag_of(v, acc)


def def_terms(node, acc):
    """A def block's own 't' (e.g. {'def': {'t': 'GIFMIS', 'd': '...'}}) also
    counts as defining that term, even with no "(ABBR)" in sight."""
    if isinstance(node, list):
        for v in node:
            def_terms(v, acc)
    elif isinstance(node, dict):
        if 'def' in node and isinstance(node['def'], dict) and 't' in node['def']:
            acc.append(node['def']['t'])
        for v in node.values():
            def_terms(v, acc)


def load_chapter(n):
    path = CONTENT / f'ch{n:02d}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f'PS_{n}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CH


def main():
    for n in range(1, 24):
        ch = load_chapter(n)
        if not ch:
            continue
        words = []
        bag_of(ch.get('t'), words)
        bag_of(ch.get('secs'), words)
        text = ' '.join(words)
        defs = []
        def_terms(ch.get('secs'), defs)
        defined = set(RE_DEFINED.findall(text))
        for t in defs:
            defined |= set(RE_ABBR_TOKEN.findall(t))
        used = set(RE_ABBR_TOKEN.findall(text)) - ALLOW
        undefined = sorted(used - defined)
        if undefined:
            print(f'ch{n:02d} ({ch.get("t","")[:40]}): undefined -> {undefined}')


if __name__ == '__main__':
    main()
