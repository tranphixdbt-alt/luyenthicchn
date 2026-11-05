import json,sys
d=json.load(open('/home/user/cchn_moi/web/data/src/cm_2.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for x in d[a:b]:
    print(f"=== {x['id']} [{x['subject']} L{x['level']}] {x['topic']}")
    print("Q:",x['q'])
    for i,o in enumerate(x['o']): print(f"  {'*' if i==x['a'] else ' '}{'ABCD'[i]}. {o}")
    print("E:",x['e'])
    print("B:",x['basis'], "| quote:",repr(x['quote'])[:60], "| src:",x['src'], x['as_of'], x['part'])
