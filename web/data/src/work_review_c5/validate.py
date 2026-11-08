# Structural validation + key check against independent recomputation.
import json, re, sys, collections
d = json.load(open(sys.argv[1], encoding='utf-8'))
REQ = ['id', 'part', 'subject', 'topic', 'level', 'q', 'o', 'a', 'e', 'basis', 'quote', 'src', 'as_of']
ids = [q['id'] for q in d]
assert len(d) == 40 and len(set(ids)) == 40, 'ids'
for q in d:
    for k in REQ: assert k in q, (q['id'], k)
    assert q['part'] == 'CM' and q['subject'] == 'MG' and q['level'] in (1, 2, 3), q['id']
    assert len(q['o']) == 4 and len(set(q['o'])) == 4, q['id']
    assert q['a'] in (0, 1, 2, 3), q['id']
    for o in q['o']:
        assert not re.search(r'(tất cả|cả .*phương án|không phương án|phương án (A|B|C|D)|\bA và B\b)', o, re.I), (q['id'], o)
    L = [len(o) for o in q['o']]
    if max(L) > 1.8 * min(L) and min(L) > 12: print('length spread', q['id'], L)

# expected keys from verify.py (independent computation)
K = {'C5-014': '39.050 đồng', 'C5-015': '60.100 đồng; 2.000 cổ phiếu', 'C5-016': '500 cổ phiếu', 'C5-017': '92.350.000 đồng',
     'C5-018': '32.400 đồng', 'C5-019': '4.998 cổ phiếu', 'C5-020': '31.350 đồng', 'C5-021': '1.796.970 đồng',
     'C5-022': '35.769 đồng', 'C5-023': '36.000.000 đồng', 'C5-024': '13,04%', 'C5-034': '10.925.000 đồng',
     'C5-035': '100.650 đồng', 'C5-036': '515.716.500 đồng', 'C5-037': '90.000 đồng', 'C5-038': '8,76%',
     'C5-039': '96.370 đồng', 'C5-040': '−2,58%'}
Q = {q['id']: q for q in d}
ranks = collections.Counter()
for i, k in K.items():
    q = Q[i]; assert q['o'][q['a']] == k, (i, q['o'][q['a']], k)
    num = lambda s: float(re.match(r'[−+]?[\d.,]+', s).group().replace('−', '-').replace('.', '').replace(',', '.'))
    vals = [num(o) for o in q['o']]
    assert vals == sorted(vals), (i, 'not ascending')
    ranks[sorted(vals).index(num(k))] += 1
print('numeric key value-rank:', dict(sorted(ranks.items())))
print('a distribution:', dict(sorted(collections.Counter(q['a'] for q in d).items())))
print('OK', len(d))
