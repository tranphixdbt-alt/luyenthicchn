"""Validate cm_3.json. Run: python3 -I validate.py"""
import json, re, collections

D = '/home/user/cchn_moi/web/data/src/'
LAWDIR = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
data = json.load(open(D + 'cm_3.json', encoding='utf-8'))
nums = json.load(open(D + 'work_c3/num_answers.json', encoding='utf-8'))
KEYS = ['id', 'part', 'subject', 'topic', 'level', 'q', 'o', 'a', 'e', 'basis', 'quote', 'src', 'as_of']
TOPICS = {
    'BL': ['Tổng quan về tư vấn tài chính doanh nghiệp', 'Lập dự toán ngân sách vốn đầu tư',
           'Tài trợ vốn cho hoạt động của doanh nghiệp', 'Chính sách cổ tức và mua lại cổ phiếu của doanh nghiệp',
           'Tái cấu trúc doanh nghiệp, sáp nhập và mua lại doanh nghiệp', 'Bảo lãnh phát hành chứng khoán',
           'Tư vấn cổ phần hóa doanh nghiệp'],
    'QU': ['Tổng quan về ngành quản lý tài sản và hoạt động quản lý danh mục đầu tư', 'Các lý thuyết về danh mục đầu tư',
           'Phân bổ tài sản', 'Quản lý danh mục đầu tư cổ phiếu', 'Quản lý danh mục đầu tư trái phiếu',
           'Một số sản phẩm đầu tư thay thế', 'Quản lý rủi ro danh mục đầu tư', 'Đánh giá hiệu quả danh mục đầu tư',
           'Thực tiễn công tác quản lý danh mục đầu tư'],
    'PS': ['Tổng quan về chứng khoán phái sinh và thị trường chứng khoán phái sinh',
           'Giới thiệu khung pháp lý cho thị trường chứng khoán phái sinh', 'Những vấn đề cơ bản về hợp đồng tương lai',
           'Định giá và sử dụng hợp đồng tương lai', 'Những vấn đề cơ bản về hợp đồng quyền chọn',
           'Định giá và sử dụng hợp đồng quyền chọn', 'Sở Giao dịch CKPS và giao dịch CKPS trên sở giao dịch',
           'Một số công cụ phái sinh giao dịch trên thị trường OTC', 'Hoạt động bù trừ và thanh toán trong giao dịch CKPS']}
REF = re.compile(r'(tất cả|cả hai|cả ba|các phương án|phương án (trên|nào|[A-D])|đáp án|câu trên|không có .*nào|\b[A-D] (và|hoặc) [A-D]\b)', re.I)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
texts = {}


def parse(s):
    m = re.search(r'[−-]?\d[\d.]*(,\d+)?%?', s)
    t = m.group(0).replace('−', '-').replace('.', '').replace(',', '.')
    return float(t[:-1]) / 100 if t.endswith('%') else float(t), m.group(0)


err = []
assert len(data) == 95
for i, r in enumerate(data):
    rid = r.get('id')
    if list(r) != KEYS: err.append((rid, 'keys'))
    if rid != f'C3-{i+1:03d}': err.append((rid, 'id seq'))
    if r['part'] != 'CM' or r['as_of'] != '2026-11': err.append((rid, 'part/as_of'))
    if r['topic'] not in TOPICS.get(r['subject'], []): err.append((rid, 'topic'))
    if r['level'] not in (1, 2, 3): err.append((rid, 'level'))
    o = r['o']
    if not (isinstance(o, list) and len(o) == 4 and len(set(o)) == 4 and all(isinstance(x, str) and x.strip() for x in o)):
        err.append((rid, 'options'))
    if not (isinstance(r['a'], int) and 0 <= r['a'] <= 3): err.append((rid, 'a'))
    for x in o:
        if REF.search(x): err.append((rid, 'ref option: ' + x))
    if not r['e'].strip() or not r['basis'].strip(): err.append((rid, 'e/basis'))
    if re.search(r'\bkhông\b.*\?$|ngoại trừ', r['q']) and 'KHÔNG' not in r['q']:
        pass  # kiểm tra tay các câu phủ định
    if r['quote']:
        if len(r['quote']) > 300: err.append((rid, 'quote>300'))
        if r['src'] not in texts:
            texts[r['src']] = norm(open(LAWDIR + r['src'], encoding='utf-8').read())
        if norm(r['quote']) not in texts[r['src']]: err.append((rid, 'quote not verbatim'))
    elif r['src'] != 'Giáo trình SRTC (khung chương trình)':
        err.append((rid, 'src'))
    if rid in nums:
        val, s = nums[rid]
        if s != o[r['a']]: err.append((rid, 'numeric answer string mismatch'))
        pv, tok = parse(s)
        dec = len(tok.rstrip('%').split(',')[1]) if ',' in tok else 0
        tol = 0.51 * 10 ** -dec * (0.01 if tok.endswith('%') else 1)
        if abs(pv - val) > tol: err.append((rid, f'numeric {pv} vs {val}'))
        if r['level'] == 1: err.append((rid, 'calc at L1'))
qs = [norm(r['q']) for r in data]
if len(set(qs)) != len(qs): err.append(('-', 'duplicate questions'))
if len({r['id'] for r in data}) != len(data): err.append(('-', 'duplicate ids'))

print('ERRORS:', err or 'none')
C = collections.Counter
print('subject', dict(C(r['subject'] for r in data)))
print('level', dict(sorted(C(r['level'] for r in data).items())))
print('level by subject', {s: dict(sorted(C(r['level'] for r in data if r['subject'] == s).items())) for s in TOPICS})
print('answer idx', dict(sorted(C(r['a'] for r in data).items())))
print('numeric items', len(nums), '| with quote', sum(1 for r in data if r['quote']))
for s in TOPICS:
    print(s, [(t, n) for t, n in C(r['topic'] for r in data if r['subject'] == s).items()])
# cảnh báo độ dài phương án chênh lệch lớn
for r in data:
    L = [len(x) for x in r['o']]
    if max(L) > 2.2 * min(L) and min(L) > 15: print('len warn', r['id'], L)
# chuỗi đáp án lặp quá 3 lần liên tiếp
run = 1
for k in range(1, len(data)):
    run = run + 1 if data[k]['a'] == data[k - 1]['a'] else 1
    if run >= 4: print('run warn at', data[k]['id'])
