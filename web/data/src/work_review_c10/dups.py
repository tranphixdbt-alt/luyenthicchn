import json, re, sys
qs = json.load(open('/home/user/cchn_moi/web/data/questions.json'))
new = [q for q in qs if q['id'][:3] in ('C10', 'C11')]
old = [q for q in qs if q['id'][:3] not in ('C10', 'C11')]
W = lambda q: set(re.findall(r'\w+', (q['q'] + ' ' + ' '.join(q['o'])).lower()))
for n in new:
    wn = W(n)
    best = sorted(((len(wn & W(o)) / len(wn | W(o)), o['id']) for o in old), reverse=True)[:3]
    print(n['id'], ' '.join(f'{i}:{s:.2f}' for s, i in best))
