# In đầy đủ câu theo id. Dùng: python3 -I show.py ID1 ID2 ...
import json, sys
qs = {q['id']: q for q in json.load(open('/home/user/cchn_moi/web/data/questions.json', encoding='utf-8'))}
for i in sys.argv[1:]:
    q = qs[i]
    print(f"== {i} [{q['subject']}/{q['topic']}] L{q['level']}\n{q['q']}")
    for k, o in enumerate(q['o']): print(('  *' if k == q['a'] else '   ') + f" {o}")
    print("  e:", q['e']); print("  basis:", q['basis'], '|', q.get('src',''))
