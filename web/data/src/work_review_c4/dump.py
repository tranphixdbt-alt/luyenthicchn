import json,sys
d=json.load(open('/home/user/cchn_moi/web/data/src/cm_4.json'))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for x in d[lo:hi]:
    print(f"## {x['id']} [{x['subject']} L{x['level']}] {x['topic']}")
    print("Q:",x['q'])
    for i,o in enumerate(x['o']): print(f"  {'*' if i==x['a'] else ' '}{'ABCD'[i]}. {o}")
    print("E:",x['e'])
    print("B:",x['basis'])
    if x.get('quote'): print("QT:",x['quote'],"|",x['src'])
    extra=set(x)-{'id','part','subject','topic','level','q','o','a','e','basis','quote','src','as_of'}
    if extra: print("EXTRA",extra)
    print()
