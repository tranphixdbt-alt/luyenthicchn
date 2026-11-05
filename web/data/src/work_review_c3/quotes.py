import json,re
B='/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
n=lambda s:re.sub(r'\s+',' ',s).strip()
d=json.load(open('/home/user/cchn_moi/web/data/src/cm_3.json'))
for x in d:
    if x.get('quote'):
        t=n(open(B+x['src'],encoding='utf-8').read())
        print(x['id'], n(x['quote']) in t)
