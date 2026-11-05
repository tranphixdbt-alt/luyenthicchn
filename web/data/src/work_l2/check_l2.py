"""Validate luat_2.json (+ so_lieu.json): schema, quote ⊂ src after whitespace collapse. Run: python3 -I check_l2.py"""
import json, re, sys, collections
D = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
SRC = '/home/user/cchn_moi/web/data/src/'
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
BAN = re.compile(r'(tất cả các phương án|cả hai phương án|không phương án nào|phương án [A-D]\b|\b[A-D] và [A-D]\b|đáp án [A-D]\b)', re.I)
KEYS = ['id', 'part', 'subject', 'topic', 'level', 'q', 'o', 'a', 'e', 'basis', 'quote', 'src', 'as_of']

qs = json.load(open(SRC + 'luat_2.json', encoding='utf-8'))
cache, errs = {}, []
for i, x in enumerate(qs, 1):
    tag = x.get('id', f'#{i}')
    if list(x) != KEYS: errs.append(f'{tag}: keys {list(x)}')
    if x['id'] != f'L2-{i:03d}': errs.append(f'{tag}: id out of sequence')
    if (x['part'], x['subject'], x['as_of']) != ('LUAT', 'LU', '2026-11'): errs.append(f'{tag}: part/subject/as_of')
    if x['level'] not in (1, 2, 3): errs.append(f'{tag}: level')
    o = x['o']
    if len(o) != 4 or len({norm(s).lower() for s in o}) != 4 or not all(s.strip() for s in o): errs.append(f'{tag}: options not 4 distinct')
    if not (isinstance(x['a'], int) and 0 <= x['a'] <= 3): errs.append(f'{tag}: a')
    if any(BAN.search(s) for s in o): errs.append(f'{tag}: option references other options')
    if not x['e'].strip() or not x['basis'].strip(): errs.append(f'{tag}: empty e/basis')
    if len(x['quote']) > 300: errs.append(f'{tag}: quote {len(x["quote"])} chars > 300')
    if x['src'] not in cache:
        try: cache[x['src']] = norm(open(D + x['src'], encoding='utf-8').read())
        except OSError: errs.append(f'{tag}: src missing {x["src"]}'); continue
    if norm(x['quote']) not in cache[x['src']]: errs.append(f'{tag}: QUOTE NOT FOUND in {x["src"]}: {x["quote"][:90]}')
dup = [k for k, v in collections.Counter(norm(x['q']) for x in qs).items() if v > 1]
if dup: errs.append(f'duplicate questions: {dup}')

# flashcards
try:
    fc = json.load(open(SRC + 'so_lieu.json', encoding='utf-8'))
    for j, c in enumerate(fc, 1):
        if sorted(c) != ['back', 'basis', 'front', 'topic'] or not all(str(v).strip() for v in c.values()):
            errs.append(f'so_lieu #{j}: bad card')
    if len({c['front'] for c in fc}) != len(fc): errs.append('so_lieu: duplicate fronts')
    print('so_lieu cards:', len(fc))
except FileNotFoundError:
    print('so_lieu.json not found')

print('questions:', len(qs))
print('by src:', dict(collections.Counter(x['src'] for x in qs)))
print('by topic:', dict(collections.Counter(x['topic'] for x in qs)))
print('by level:', dict(sorted(collections.Counter(x['level'] for x in qs).items())))
print('answer idx:', dict(sorted(collections.Counter(x['a'] for x in qs).items())))
print('\n'.join(errs) or 'ALL CHECKS PASS')
sys.exit(1 if errs else 0)
