"""Tìm câu cũ gần giống nhất với từng câu C6 (Jaccard trên từ của q + đáp án đúng)."""
import json, re
qs = json.load(open('/home/user/cchn_moi/web/data/questions.json', encoding='utf-8'))
c6 = json.load(open('/home/user/cchn_moi/web/data/src/cm_6.json', encoding='utf-8'))
old = [q for q in qs if not q['id'].startswith(('C6-', 'C7-'))]
W = lambda q: set(re.findall(r'\w+', (q['q'] + ' ' + q['o'][q['a']]).lower()))
for q in c6:
    w = W(q)
    best = sorted(((len(w & W(o)) / len(w | W(o)), o['id']) for o in old), reverse=True)[:3]
    print(q['id'], ' '.join(f'{i}:{s:.2f}' for s, i in best))
