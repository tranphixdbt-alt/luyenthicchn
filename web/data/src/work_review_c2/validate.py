import json,re,sys
D=json.load(open('/home/user/cchn_moi/web/data/src/cm_2.json',encoding='utf-8'))
K={"id","part","subject","topic","level","q","o","a","e","basis","quote","src","as_of"}
REF=re.compile(r"tất cả|cả hai|cả ba|phương án|đáp án|\b[A-D] và [A-D]\b|không có .* nào|các câu trên|nêu trên",re.I)
ids=set(); bad=[]
for x in D:
    if set(x)!=K: bad.append((x.get('id'),'keys'))
    if not(isinstance(x['o'],list) and len(x['o'])==4 and len(set(x['o']))==4 and all(s.strip() for s in x['o'])): bad.append((x['id'],'options'))
    if not(type(x['a']) is int and 0<=x['a']<=3): bad.append((x['id'],'a'))
    if x['id'] in ids: bad.append((x['id'],'dup'))
    ids.add(x['id'])
    if not all(str(x[f]).strip() for f in K-{'quote'}): bad.append((x['id'],'empty'))
    if any(REF.search(s) for s in x['o']): bad.append((x['id'],'ref'))
    if x['level'] not in (1,2,3) or x['part']!='CM' or x['subject'] not in('PT','BC'): bad.append((x['id'],'meta'))
    L=[len(o) for o in x['o']]
    if L[x['a']]==max(L) and max(L)-sorted(L)[-2]>12: print('long key',x['id'],L)
print(len(D),'questions;',len(ids),'ids; problems:',bad or 'none')
sys.exit(bool(bad))
