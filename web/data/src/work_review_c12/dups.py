# Find bank items overlapping each C12 item (keyword hits + word Jaccard on q+o).
import json, re, sys
qs = json.load(open('/home/user/cchn_moi/web/data/questions.json'))
c12 = json.load(open('/home/user/cchn_moi/web/data/src/cm_12.json'))
def w(q): return set(re.findall(r"\w+", (q['q'] + ' ' + ' '.join(q['o'])).lower()))
others = [q for q in qs if not q['id'].startswith('C12-')]
for c in c12:
    cw = w(c)
    sc = sorted(((len(cw & w(o)) / len(cw | w(o)), o['id']) for o in others), reverse=True)[:4]
    print(c['id'], ' '.join(f"{i}:{s:.2f}" for s, i in sc))
for kw in sys.argv[1:]:
    hits = [q['id'] for q in others if kw.lower() in (q['q'] + ' '.join(q['o']) + q['e']).lower()]
    print(f"[{kw}] {len(hits)}: {' '.join(hits[:40])}")
