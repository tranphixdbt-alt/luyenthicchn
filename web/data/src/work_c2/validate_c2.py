# Kiểm tra cm_2.json theo SCHEMA.md
import json, re, collections

D = json.load(open('/home/user/cchn_moi/web/data/src/cm_2.json', encoding='utf-8'))
KEYS = {"id", "part", "subject", "topic", "level", "q", "o", "a", "e", "basis", "quote", "src", "as_of"}
REF = re.compile(r"tất cả|cả hai|cả ba|phương án|đáp án|\b[A-D] và [A-D]\b|không có .* nào|các câu trên|nêu trên", re.I)
LETTER = re.compile(r"\b(phương án|đáp án|câu) [A-D]\b")

assert len(D) == 90
ids, qs = set(), set()
for x in D:
    assert set(x) == KEYS, x['id']
    assert x['part'] == 'CM' and x['subject'] in ('PT', 'BC') and x['level'] in (1, 2, 3)
    assert x['quote'] == '' and x['src'] == 'Giáo trình SRTC (khung chương trình)' and x['as_of'] == '2026-11'
    assert isinstance(x['o'], list) and len(x['o']) == 4 and len(set(x['o'])) == 4
    assert all(isinstance(s, str) and s.strip() for s in x['o'])
    assert isinstance(x['a'], int) and 0 <= x['a'] <= 3
    assert not any(REF.search(s) for s in x['o']), (x['id'], x['o'])
    assert not LETTER.search(x['e']), x['id']
    assert x['e'] and x['basis'] and x['topic']
    assert x['id'] not in ids and x['q'] not in qs, x['id']
    ids.add(x['id']); qs.add(x['q'])
    if x['level'] == 3:  # bài tính: đáp án đúng phải xuất hiện trong lời giải
        core = re.sub(r"^(RSI = |MACD = |Tăng lên |Tăng |Lợi suất yêu cầu )", "", x['o'][x['a']])
        num = re.match(r"[−\d][\d.,]*", core).group(0).rstrip('.,')
        assert num in x['e'], (x['id'], num)
assert [x['id'] for x in D] == [f"C2-{i:03d}" for i in range(1, 91)]

C = collections.Counter
print("subject:", dict(C(x['subject'] for x in D)))
print("level:", dict(sorted(C(x['level'] for x in D).items())))
print("a:", dict(sorted(C(x['a'] for x in D).items())))
for s in ('PT', 'BC'):
    print(s, "levels:", dict(sorted(C(x['level'] for x in D if x['subject'] == s).items())))
    for t, n in C(x['topic'] for x in D if x['subject'] == s).items():
        print("  ", n, t)
print("OK")
