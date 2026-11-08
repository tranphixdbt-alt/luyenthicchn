"""Validate cm_5.json. Run: python3 -I validate.py"""
import json, re, collections

D = '/home/user/cchn_moi/web/data/src/'
data = json.load(open(D + 'cm_5.json', encoding='utf-8'))
nums = json.load(open(D + 'work_c5/num_answers.json', encoding='utf-8'))
KEYS = ['id', 'part', 'subject', 'topic', 'level', 'q', 'o', 'a', 'e', 'basis', 'quote', 'src', 'as_of']
TOPICS = ['Giao dịch cổ phiếu trên thị trường chứng khoán', 'Giao dịch trái phiếu trên thị trường chứng khoán']
REF = re.compile(r'(tất cả|cả hai|cả ba|các phương án|phương án (trên|nào|[A-D])|đáp án|câu trên|không có .*nào|\b[A-D] (và|hoặc) [A-D]\b)', re.I)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
words = lambda s: set(re.findall(r'\w+', s.lower()))


def parse(s):
    m = re.search(r'[−+-]?\d[\d.]*(,\d+)?%?', s)
    t = m.group(0).replace('−', '-').replace('.', '').replace(',', '.')
    return float(t[:-1]) / 100 if t.endswith('%') else float(t), m.group(0)


err = []
assert len(data) == 40
for i, r in enumerate(data):
    rid = r.get('id')
    if list(r) != KEYS: err.append((rid, 'keys'))
    if rid != f'C5-{i+1:03d}': err.append((rid, 'id seq'))
    if r['part'] != 'CM' or r['subject'] != 'MG' or r['as_of'] != '2026-11': err.append((rid, 'part/subject/as_of'))
    if r['topic'] not in TOPICS: err.append((rid, 'topic'))
    if r['level'] not in (1, 2, 3): err.append((rid, 'level'))
    o = r['o']
    if not (isinstance(o, list) and len(o) == 4 and len(set(o)) == 4 and all(isinstance(x, str) and x.strip() for x in o)):
        err.append((rid, 'options'))
    if not (isinstance(r['a'], int) and 0 <= r['a'] <= 3): err.append((rid, 'a'))
    for x in o:
        if REF.search(x): err.append((rid, 'ref option: ' + x))
    if not r['e'].strip() or not r['basis'].strip(): err.append((rid, 'e/basis'))
    if r['quote'] != '' or r['src'] != 'Giáo trình SRTC (khung chương trình)': err.append((rid, 'quote/src'))
    if re.search(r'(sau đây|nào) (không|ngoại trừ)|không (phải|đúng)', r['q']):
        print('check negation wording:', rid)
    if rid in nums:
        val, s = nums[rid]
        if s != o[r['a']]: err.append((rid, 'numeric answer string mismatch'))
        pv, tok = parse(s)
        dec = len(tok.rstrip('%').split(',')[1]) if ',' in tok else 0
        tol = 0.51 * 10 ** -dec * (0.01 if tok.endswith('%') else 1)
        if abs(pv - val) > tol: err.append((rid, f'numeric {pv} vs {val}'))
        if r['level'] != 3: err.append((rid, 'calc not at L3'))
    elif r['level'] == 3 and r['id'] not in nums:
        err.append((rid, 'L3 without numeric check'))
if len({norm(r['q']) for r in data}) != len(data): err.append(('-', 'duplicate questions'))
if len({r['id'] for r in data}) != len(data): err.append(('-', 'duplicate ids'))

# near-duplicate check (word Jaccard) against existing banks and within this file
old = []
for f in ['cm_1.json', 'cm_2.json', 'cm_3.json']:
    old += json.load(open(D + f, encoding='utf-8'))
maxj = (0, None, None)
for r in data:
    wq, wqo = words(r['q']), words(r['q'] + ' ' + ' '.join(r['o']))
    for x in old + [y for y in data if y['id'] != r['id']]:
        jq = len(wq & words(x['q'])) / len(wq | words(x['q']))
        xo = words(x['q'] + ' ' + ' '.join(x['o']))
        jqo = len(wqo & xo) / len(wqo | xo)
        j = max(jq, jqo)
        if j > maxj[0]: maxj = (j, r['id'], x['id'])
        if j > 0.7: err.append((r['id'], f'near-duplicate of {x["id"]} J={j:.2f}'))

print('ERRORS:', err or 'none')
C = collections.Counter
print('max Jaccard %.2f (%s vs %s)' % maxj)
print('topic', dict(C(r['topic'] for r in data)))
print('level', dict(sorted(C(r['level'] for r in data).items())))
print('level by topic', {t[:22]: dict(sorted(C(r['level'] for r in data if r['topic'] == t).items())) for t in TOPICS})
print('answer idx', dict(sorted(C(r['a'] for r in data).items())))
print('numeric items asserted', len(nums))
for r in data:
    L = [len(x) for x in r['o']]
    if max(L) > 1.6 * min(L) and min(L) > 12: print('len warn', r['id'], L)
    if L[r['a']] == max(L) and sorted(L)[-1] - sorted(L)[-2] > 8: print('correct clearly longest', r['id'], L)
run = 1
for k in range(1, len(data)):
    run = run + 1 if data[k]['a'] == data[k - 1]['a'] else 1
    if run >= 4: print('run warn at', data[k]['id'])
