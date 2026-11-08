import json,sys
d=json.load(open('/home/user/cchn_moi/web/data/questions.json'))
terms=sys.argv[1:]
for x in d:
    if x['id'].startswith('C14'): continue
    t=(x['q']+' '+' '.join(x['o'])+' '+x.get('e','')).lower()
    hits=[k for k in terms if k.lower() in t]
    if hits:
        print('==',x['id'],hits,'|',x['q'][:260].replace('\n',' / '),'| KEY:',x['o'][x['a']][:120])
