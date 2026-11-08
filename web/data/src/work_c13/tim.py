# Tìm câu theo regex trong ngân hàng. Dùng: python3 -I tim.py 'regex' [môn,môn] [số dòng tối đa]
import json, re, sys
qs = json.load(open('/home/user/cchn_moi/web/data/questions.json', encoding='utf-8'))
pat = re.compile(sys.argv[1], re.I)
subj = set(sys.argv[2].split(',')) if len(sys.argv) > 2 and sys.argv[2] else None
n = int(sys.argv[3]) if len(sys.argv) > 3 else 15
for q in qs:
    if subj and q['subject'] not in subj: continue
    if pat.search(q['q'] + ' ' + ' '.join(q['o']) + ' ' + q['e']):
        print(f"{q['id']} [{q['subject']}] {q['q'][:200]}\n   => {q['o'][q['a']][:150]}"); n -= 1
        if n == 0: break
