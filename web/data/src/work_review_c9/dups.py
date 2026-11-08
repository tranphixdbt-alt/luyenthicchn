import json, re, sys
qs = json.load(open('../../questions.json'))
c9 = json.load(open('../cm_9.json'))
others = [q for q in qs if not q['id'].startswith('C9-')]
W = lambda s: set(re.findall(r'\w+', s.lower()))
for q in c9:
    a = W(q['q'] + ' ' + ' '.join(q['o']))
    sc = sorted(((len(a & W(o['q'] + ' ' + ' '.join(o['o']))) / len(a | W(o['q'] + ' ' + ' '.join(o['o']))), o) for o in others), key=lambda t: -t[0])[:3]
    print(q['id'], ' | '.join(f"{o['id']}({s:.2f})" for s, o in sc))
