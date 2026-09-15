#!/usr/bin/env python3
"""Print the chapter/section outline of a study text, to ground the syllabus tree."""
import re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import tidy

ROOT = Path(__file__).resolve().parents[2]
ST = ROOT / 'materials' / 'study-texts'
FILES = {
    'FA': 'FA - Financial Accounting (Study Text, 5th ed, 2025).pdf',
    'PS': 'PS - Public Sector Accounting (Study Text, 5th ed, 2025).pdf',
    'QA': 'QA - Quantitative Analysis (Study Text, 5th ed, 2025).pdf',
    'IT': 'IT - Information Technology (Study Text, 5th ed, 2025).pdf',
}
WORDS = ('ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE THIRTEEN '
         'FOURTEEN FIFTEEN SIXTEEN SEVENTEEN EIGHTEEN NINETEEN TWENTY').split()
NUM = {w: i + 1 for i, w in enumerate(WORDS)}
NUM.update({'TWENTY-ONE': 21, 'TWENTY-TWO': 22, 'TWENTY-THREE': 23})

# study texts print "TWENTY-ONE"/"TWENTY-TWO" with inconsistent spacing around the
# hyphen (e.g. "CHAPTER TWENTY- ONE"); match loosely and canonicalise before NUM lookup
RE_CH = re.compile(r'^\s*CHAPTER\s+(TWENTY[\s-]+(?:ONE|TWO|THREE)|'
                    + '|'.join(WORDS) + r'|\d{1,2})\s*$', re.I)
RE_SEC = re.compile(r'^\s{0,12}(\d{1,2})[.,](\d{1,2})(?:\.(\d))?\s+(\S.{2,90})$')


def chapters(code):
    txt = subprocess.run(['pdftotext', '-layout', str(ST / FILES[code]), '-'],
                         capture_output=True, text=True, check=True).stdout
    lines = txt.replace('\f', '\n').split('\n')
    # skip the table of contents: start at the first chapter heading that is
    # followed within a few lines by a title in capitals and no dot leaders
    marks = []
    for i, l in enumerate(lines):
        m = RE_CH.match(l)
        if not m:
            continue
        tail = [x for x in lines[i + 1:i + 8] if x.strip()][:4]
        if any('....' in x for x in tail):
            continue
        g = re.sub(r'[\s-]+', '-', m.group(1).upper().strip())
        n = NUM.get(g) or int(m.group(1))
        marks.append((n, i, tidy(tail[0]) if tail else ''))
    # keep the last run where chapter numbers ascend from 1
    best = []
    for n, i, t in marks:
        if n == 1:
            best = []
        if not best or n >= best[-1][0]:
            best.append((n, i, t))
    out = []
    for j, (n, i, t) in enumerate(best):
        end = best[j + 1][1] if j + 1 < len(best) else len(lines)
        secs, seen = [], set()
        for l in lines[i:end]:
            ms = RE_SEC.match(l)
            if not ms or int(ms.group(1)) != n:
                continue
            key = (ms.group(2), ms.group(3))
            if key in seen:
                continue
            seen.add(key)
            title = tidy(ms.group(4))
            if '....' in title or len(title) < 4:
                continue
            secs.append(f'{n}.{ms.group(2)}' + (f'.{ms.group(3)}' if ms.group(3) else '')
                        + '  ' + title)
        out.append((n, t, secs, end - i))
    return out


if __name__ == '__main__':
    for code in (sys.argv[1:] or ['FA', 'PS', 'QA', 'IT']):
        print('#' * 70); print('#', code)
        for n, t, secs, ln in chapters(code):
            print(f'\n== CH {n}: {t}   ({ln} lines)')
            for s in secs[:40]:
                print('   ', s)
