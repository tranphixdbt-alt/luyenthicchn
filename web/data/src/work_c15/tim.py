# Tìm câu trong ngân hàng theo từ khóa (regex, không phân biệt hoa thường). Dùng: python3 -I tim.py 'regex' [môn,môn]
import json, re, sys
qs = json.load(open('/home/user/cchn_moi/web/data/questions.json', encoding='utf-8'))
pat = re.compile(sys.argv[1], re.I)
subj = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else None
for q in qs:
    if subj and q['subject'] not in subj: continue
    txt = q['q'] + ' ' + ' '.join(q['o'])
    if pat.search(txt):
        print(f"{q['id']} [{q['subject']}] {q['q'][:260]}\n   => {q['o'][q['a']][:160]}")
