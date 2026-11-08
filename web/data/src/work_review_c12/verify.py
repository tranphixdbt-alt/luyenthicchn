# Second-pass checks for cm_12.json: recompute numbers, replay C12-007, verify quotes, style.
import json, re, unicodedata
from fractions import Fraction as F
P = '/home/user/cchn_moi/web/data/src/'
DOC = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
Q = {q['id']: q for q in json.load(open(P + 'cm_12.json', encoding='utf-8'))}
key = lambda i: Q[i]['o'][Q[i]['a']]
vn = lambda x: f"{x:,.0f}".replace(',', '.')

# C12-001: dividend per outstanding share
auth, issued, treas, npat, div = 10_000_000, 6_000_000, 1_500_000, 12_000_000_000, 9_000_000_000
out = issued - treas
assert key('C12-001') == f"{vn(F(div, out))} đồng" == '2.000 đồng'
wrong = {f"{vn(F(div, issued))} đồng", f"{vn(F(div, auth))} đồng", f"{vn(round(F(npat, out)))} đồng"}
assert wrong == set(Q['C12-001']['o']) - {key('C12-001')}, wrong
nums = sorted(int(o.split()[0].replace('.', '')) for o in Q['C12-001']['o'])
print('C12-001 key rank (ascending):', nums.index(2000) + 1, 'of', nums)

# C12-002: short sale stop-buy level and loss
stop = 60_000 * F(115, 100); assert stop == 69_000 and 60_000 * F(85, 100) == 51_000
assert (stop - 60_000) * 2_000 == 18_000_000
assert key('C12-002') == 'Lệnh dừng để mua 2.000 cổ phiếu, giá dừng 69.000 đồng'

# C12-003: stop-sell below market, profit locked
assert 45_000 < 48_000 and 45_000 - 40_000 == 5_000 and key('C12-003').startswith('Lệnh dừng để bán, giá dừng 45.000')
assert 48_000 * F(93, 100) < 45_000  # the limit-sell distractor at 45.000 would be within a ±7% band, so it would fill at once

# C12-007: independent continuous-matching replay (price-time priority, trade at resting price, MP sweeps)
ref, tick = 45_000, 50
ceil_, floor_ = ref * 107 // 100 // tick * tick, -(-ref * 93 // 100 // tick) * tick
assert (ceil_, floor_) == (48_150, 41_850)
orders = [('P', 'B', 2000, 44800), ('Q', 'S', 1500, 45300), ('R', 'B', 1000, 45000),
          ('S', 'B', 500, None), ('T', 'S', 2500, None), ('U', 'B', 1200, 45500)]
book = {'B': [], 'S': []}; trades = []; seq = 0
for who, side, qty, px in orders:
    if px is not None: assert px % tick == 0 and floor_ <= px <= ceil_
    opp = book['S' if side == 'B' else 'B']
    opp.sort(key=lambda o: ((o[3] if side == 'B' else -o[3]), o[0]))  # best price, then time
    while qty and opp and (px is None or (opp[0][3] <= px if side == 'B' else opp[0][3] >= px)):
        o = opp[0]; n = min(qty, o[2]); trades.append((who, o[1], n, o[3])); qty -= n; o[2] -= n
        if not o[2]: opp.pop(0)
    if qty:
        assert px is not None, f'MP {who} left {qty}'  # both MPs must fill fully, so no MP-remainder rule is needed
        seq += 1; book[side].append([seq, who, qty, px])
u = [(n, p) for w, c, n, p in trades if w == 'U']
rest_u = [o for o in book['B'] if o[1] == 'U']
print('C12-007 trades:', trades, '| U rests:', rest_u)
assert u == [(1000, 45300)] and rest_u[0][2:] == [200, 45500]
assert key('C12-007') == 'Khớp 1.000 cổ phiếu giá 45.300 đồng; 200 cổ phiếu chờ mua giá 45.500 đồng'

# Quotes verbatim
def norm(s): return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).strip()
for i, q in Q.items():
    if q.get('quote'):
        assert norm(q['quote']) in norm(open(DOC + q['src'], encoding='utf-8').read()), i
assert Q['C12-006']['part'] == 'LUAT' and Q['C12-006']['quote']

# Style: negative words, option references, length ratio
bank = json.load(open('/home/user/cchn_moi/web/data/questions.json', encoding='utf-8'))
topics = {(q['subject'], q['topic']) for q in bank if not q['id'].startswith('C12-')}
for i, q in Q.items():
    assert (q['subject'], q['topic']) in topics, (i, q['topic'])
    assert not re.search(r'\b(không|ngoại trừ|trừ)\b(?=[^.]*\?$)', q['q']) or 'KHÔNG' in q['q']
    L = [len(o) for o in q['o']]
    assert max(L) / min(L) < 1.35, (i, L)
    assert not re.search(r'phương án [A-D]\b|\b[A-D] và [A-D]\b', ' '.join(q['o']))
    print(i, 'lens', L, 'key len rank', sorted(L).index(L[q['a']]) + 1)
print('verify OK')
