"""Validate cm_6.json. Run: python3 -I validate.py"""
import json, re, sys, collections, importlib.util

D = '/home/user/cchn_moi/web/data/src/'
spec = importlib.util.spec_from_file_location('kt', '/home/user/cchn_moi/web/tools/kiem_tra.py')
kt = importlib.util.module_from_spec(spec); spec.loader.exec_module(kt)

data = json.load(open(D + 'cm_6.json', encoding='utf-8'))
nums = json.load(open(D + 'work_c6/num_answers.json', encoding='utf-8'))
KEYS = ['id', 'part', 'subject', 'topic', 'level', 'q', 'o', 'a', 'e', 'basis', 'quote', 'src', 'as_of']
TOPICS = ['Tổng quan về thị trường chứng khoán', 'Các công cụ tài chính trên thị trường chứng khoán',
          'Thị trường chứng khoán sơ cấp', 'Thị trường chứng khoán thứ cấp', 'Công ty chứng khoán']
words = lambda s: set(re.findall(r'\w+', s.lower()))
err = []
assert len(data) == 40
for i, r in enumerate(data):
    rid = r['id']
    if list(r) != KEYS: err.append((rid, 'keys'))
    if rid != f'C6-{i+1:03d}': err.append((rid, 'id seq'))
    if (r['part'], r['subject'], r['as_of']) != ('CM', 'CB', '2026-11'): err.append((rid, 'part/subject/as_of'))
    if r['topic'] not in TOPICS: err.append((rid, 'topic'))
    o = r['o']
    if len(o) != 4 or len(set(o)) != 4: err.append((rid, 'options'))
    for x in o:
        if kt.REF.search(x): err.append((rid, 'ref option ' + x))
    if kt.LETTER_IN_E.search(r['e']): err.append((rid, 'letter in e'))
    if bool(r['quote']) != bool(r['src']): err.append((rid, 'quote/src pair'))
    if r['quote']:
        if len(r['quote']) > 300: err.append((rid, f'quote len {len(r["quote"])}'))
        text = kt.doc_text(r['src'])
        if text is None: err.append((rid, 'src missing'))
        elif kt.norm_ws(r['quote']) not in text: err.append((rid, 'quote not verbatim (strict)'))
    if re.search(r'\b(không|ngoại trừ)\b', r['q']) and not re.search(r'KHÔNG|NGOẠI TRỪ', r['q']):
        print('check negation:', rid, r['q'][:80])
    if rid in nums:
        if nums[rid][1] != o[r['a']]: err.append((rid, 'numeric key mismatch'))
        if r['level'] != 3: err.append((rid, 'calc not L3'))
    L = [len(x) for x in o]
    if min(L) > 12 and max(L) > 1.6 * min(L): print('len warn', rid, L)
    if L[r['a']] == max(L) and sorted(L)[-1] - sorted(L)[-2] > 10: print('key clearly longest', rid, L)

bank = [q for q in json.load(open('/home/user/cchn_moi/web/data/questions.json', encoding='utf-8')) if not q['id'].startswith('C6-')]
mx = (0, '', '')
for r in data:
    w = words(r['q'])
    for x in bank + [y for y in data if y['id'] != r['id']]:
        wx = words(x['q'])
        j = len(w & wx) / len(w | wx)
        if j > mx[0]: mx = (j, r['id'], x['id'])
        if j > 0.6: print(f'similar {r["id"]} ~ {x["id"]} J={j:.2f}')
print('ERRORS:', err or 'none')
C = collections.Counter
print('max Jaccard %.2f %s %s' % mx)
print('topic/level', {t[:14]: dict(sorted(C(r['level'] for r in data if r['topic'] == t).items())) for t in TOPICS})
print('level', dict(sorted(C(r['level'] for r in data).items())))
print('a', dict(sorted(C(r['a'] for r in data).items())))
print('quoted', sum(1 for r in data if r['quote']), '| calcs', len(nums))
sys.exit(1 if err else 0)
