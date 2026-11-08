"""Validate cm_4.json. Run: python3 -I validate.py"""
import json, re, collections

D = '/home/user/cchn_moi/web/data/src/'
LAW = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
GT = 'Giáo trình SRTC (khung chương trình)'
data = json.load(open(D + 'cm_4.json', encoding='utf-8'))
KEYS = ['id', 'part', 'subject', 'topic', 'level', 'q', 'o', 'a', 'e', 'basis', 'quote', 'src', 'as_of']
WANT = {'Tổng quan về môi giới và tư vấn đầu tư chứng khoán': 6,
        'Kiến thức và kỹ năng cần thiết của người môi giới chứng khoán và tư vấn đầu tư chứng khoán': 8,
        'Xây dựng mạng lưới khách hàng và chăm sóc khách hàng': 8,
        'Xung đột lợi ích và giải quyết xung đột lợi ích trong hoạt động môi giới và tư vấn đầu tư chứng khoán': 8,
        'Quản lý Nhà nước đối với hoạt động môi giới và tư vấn đầu tư chứng khoán': 10}
REF = re.compile(r'tất cả|cả hai|cả ba|phương án|đáp án|câu trên|nêu trên|\b[A-D] (và|hoặc) [A-D]\b|không có .* nào', re.I)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
words = lambda s: set(re.findall(r'\w+', s.lower()))
jac = lambda a, b: len(a & b) / len(a | b) if a | b else 0
texts, err = {}, []

for i, r in enumerate(data):
    rid = r['id']
    if list(r) != KEYS: err.append((rid, 'keys'))
    if rid != f'C4-{i + 1:03d}': err.append((rid, 'id seq'))
    if (r['part'], r['subject'], r['as_of']) != ('CM', 'MG', '2026-11'): err.append((rid, 'part/subject/as_of'))
    if r['topic'] not in WANT: err.append((rid, 'topic'))
    if r['level'] not in (1, 2, 3): err.append((rid, 'level'))
    o = r['o']
    if not (len(o) == 4 and len({norm(x) for x in o}) == 4 and all(x.strip() for x in o)): err.append((rid, 'options'))
    if not (isinstance(r['a'], int) and 0 <= r['a'] <= 3): err.append((rid, 'a'))
    err += [(rid, 'ref option: ' + x) for x in o if REF.search(x)]
    if not (r['e'].strip() and r['basis'].strip() and r['q'].strip()): err.append((rid, 'empty field'))
    if re.search(r'\b(không|ngoại trừ)\b', r['q']) and not re.search(r'KHÔNG|NGOẠI TRỪ', r['q']):
        print('  check negation wording:', rid)
    ln = [len(x) for x in o]
    if ln[r['a']] == max(ln) and max(ln) > 1.25 * sorted(ln)[-2]: err.append((rid, f'correct option much longest {ln}'))
    if r['quote']:
        if len(r['quote']) > 300: err.append((rid, f'quote {len(r["quote"])}>300'))
        if r['src'] not in texts: texts[r['src']] = norm(open(LAW + r['src'], encoding='utf-8').read())
        if norm(r['quote']) not in texts[r['src']]: err.append((rid, 'quote not verbatim'))
    elif r['src'] != GT: err.append((rid, 'src without quote'))
if len({r['id'] for r in data}) != len(data): err.append(('-', 'dup ids'))
if len({norm(r['q']) for r in data}) != len(data): err.append(('-', 'dup questions'))

# near-duplicate vs existing banks (stem, and stem + correct option)
old = [x for f in ('cm_1.json', 'luat_1.json', 'luat_2.json') for x in json.load(open(D + f, encoding='utf-8'))]
top = []
for r in data:
    for x in old:
        js = jac(words(r['q']), words(x['q']))
        jf = jac(words(r['q'] + ' ' + r['o'][r['a']]), words(x['q'] + ' ' + x['o'][x['a']]))
        m = max(js, jf)
        if m > 0.7: err.append((r['id'], f'near-dup {x["id"]} {m:.2f}'))
        top.append((m, r['id'], x['id']))
top.sort(reverse=True)

C = collections.Counter
print('ERRORS:', err or 'none')
print('n =', len(data))
print('topic:', {t[:30]: n for t, n in C(r['topic'] for r in data).items()}, 'want', list(WANT.values()))
print('level:', dict(sorted(C(r['level'] for r in data).items())))
for t in WANT:
    print('  ', t[:40], dict(sorted(C(r['level'] for r in data if r['topic'] == t).items())))
print('answer idx:', dict(sorted(C(r['a'] for r in data).items())))
print('with quote:', sum(1 for r in data if r['quote']), '| src:', dict(C(r['src'][:20] for r in data)))
print('max Jaccard vs existing (top 5):', [(f'{m:.2f}', a, b) for m, a, b in top[:5]])
assert [n for n in C(r['topic'] for r in data).values()] and all(
    C(r['topic'] for r in data)[t] == n for t, n in WANT.items()), 'topic counts'
