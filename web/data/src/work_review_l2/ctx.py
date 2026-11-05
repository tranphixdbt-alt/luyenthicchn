# Show quote context in src: python3 -I ctx.py N BEFORE AFTER id...
import json, re, sys, pathlib
D = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
qs = {x['id']: x for x in json.loads((pathlib.Path(__file__).resolve().parent.parent / 'luat_2.json').read_text(encoding='utf-8'))}
b, a = int(sys.argv[1]), int(sys.argv[2])
cache = {}
for i in sys.argv[3:]:
    x = qs['L2-%03d' % int(i)]
    t = cache.setdefault(x['src'], ' '.join(open(D + x['src'], encoding='utf-8').read().split()))
    q = ' '.join(x['quote'].split())
    k = t.find(q)
    print(f"== {x['id']} [{x['src'][:20]}] pos={k}")
    if k >= 0: print(t[max(0, k - b):k + len(q) + a])
    print()
