import json, re
P='/home/user/cchn_moi/web/data/src/cm_1.json'
d=json.load(open(P,encoding='utf-8'))
req=['id','part','subject','topic','level','q','o','a','e','basis','quote','src','as_of']
ids=[x['id'] for x in d]
assert len(d)==80 and len(set(ids))==80, 'ids'
bad=re.compile(r'(?i:tất cả các phương án|không phương án nào|phương án [A-D]\b)|\b[A-D] (và|hoặc) [A-D]\b')
for x in d:
    for k in req: assert k in x, (x['id'],k)
    assert x['part']=='CM' and x['subject'] in ('CB','MG'), x['id']
    assert x['level'] in (1,2,3)
    assert isinstance(x['o'],list) and len(x['o'])==4 and len(set(x['o']))==4, x['id']
    assert isinstance(x['a'],int) and 0<=x['a']<=3, x['id']
    assert all(o.strip() for o in x['o']) and x['q'].strip() and x['e'].strip() and x['basis'].strip()
    for o in x['o']: assert not bad.search(o), (x['id'],o)
    L=[len(o) for o in x['o']]
    if max(L)>1.6*min(L): print('length spread',x['id'],L)
print('valid', len(d))
