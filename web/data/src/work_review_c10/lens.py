import json, sys
for f in sys.argv[1:]:
    for q in json.load(open(f)):
        L = [len(o) for o in q['o']]
        print(q['id'], q['a'], L, 'key=%d' % L[q['a']], 'max/min=%.2f' % (max(L) / min(L)))
