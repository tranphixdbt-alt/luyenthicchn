import json,re,glob,difflib
B='/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
n=lambda s:re.sub(r'\s+',' ',s).strip()
d=json.load(open('/home/user/cchn_moi/web/data/src/cm_3.json',encoding='utf-8'))
REQ=['id','part','subject','topic','level','q','o','a','e','basis','quote','src','as_of']
err=[]
ids=[x['id'] for x in d]
if len(ids)!=len(set(ids)): err.append('dup ids')
assert len(d)==95
for x in d:
    i=x['id']
    for k in REQ:
        if k not in x: err.append(f'{i} missing {k}')
    if set(x)-set(REQ): err.append(f'{i} extra {set(x)-set(REQ)}')
    o=x['o']
    if len(o)!=4 or len(set(map(n,o)))!=4: err.append(f'{i} options')
    if not (isinstance(x['a'],int) and 0<=x['a']<=3): err.append(f'{i} a')
    if x['level'] not in (1,2,3) or x['part']!='CM' or x['subject'] not in ('BL','QU','PS'): err.append(f'{i} meta')
    for k in ('q','e','basis'):
        if not x[k].strip(): err.append(f'{i} empty {k}')
    if any(re.search(r'tất cả các phương án|phương án [A-D]\b|\b[A-D] và [A-D]\b|không phương án nào',s,re.I) for s in o): err.append(f'{i} refers to options')
    if x['quote']:
        if len(x['quote'])>300: err.append(f'{i} quote>300')
        if n(x['quote']) not in n(open(B+x['src'],encoding='utf-8').read()): err.append(f'{i} quote not verbatim')
    elif x['src'].endswith('.txt'): err.append(f'{i} txt src w/o quote')
    L=[len(s) for s in o]; c=L[x['a']]; oth=max(L[:x['a']]+L[x['a']+1:])
    if c>1.25*oth: print('WARN long key',i,L)
others=[(f,y) for f in glob.glob('/home/user/cchn_moi/web/data/src/*.json') if not f.endswith('cm_3.json') for y in json.load(open(f,encoding='utf-8')) if isinstance(y,dict) and 'q' in y]
for x in d:
    for f,y in others:
        if difflib.SequenceMatcher(None,x['q'],y['q']).quick_ratio()>0.8 and difflib.SequenceMatcher(None,x['q'],y['q']).ratio()>0.7:
            print('NEAR-DUP',x['id'],y['id'])
import collections; print(collections.Counter(x['a'] for x in d))
print('ERRORS:',err if err else 'none')
