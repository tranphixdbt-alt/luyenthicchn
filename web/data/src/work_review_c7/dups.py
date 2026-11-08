"""Tìm câu C7 gần trùng (Jaccard từ của q+đáp án) với questions.json (bỏ C7) và cm_6.json."""
import json, re
from pathlib import Path
D = Path('/home/user/cchn_moi/web/data')
c7 = json.loads((D / 'src/cm_7.json').read_text(encoding='utf-8'))
others = [q for q in json.loads((D / 'questions.json').read_text(encoding='utf-8')) if not q['id'].startswith('C7-')]
others += json.loads((D / 'src/cm_6.json').read_text(encoding='utf-8'))
seen = {q['id']: q for q in others}
W = lambda q: set(re.findall(r'\w+', (q['q'] + ' ' + q['o'][q['a']]).lower()))
for q in c7:
    a = W(q)
    best = sorted(((len(a & W(o)) / len(a | W(o)), o['id']) for o in seen.values()), reverse=True)[:2]
    flag = '  <<<' if best[0][0] > 0.4 else ''
    print(q['id'], ' '.join(f'{i}:{s:.2f}' for s, i in best), flag)
