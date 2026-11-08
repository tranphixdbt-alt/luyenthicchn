"""Usage: python3 -I find.py REGEX  -- search q+options+basis in cm_1, luat_1, luat_2"""
import json,re,sys
D='/home/user/cchn_moi/web/data/src/'
for f in ('cm_1.json','luat_1.json','luat_2.json'):
    for x in json.load(open(D+f,encoding='utf-8')):
        s=x['q']+' | '+' / '.join(x['o'])+' | '+x['basis']
        if re.search(sys.argv[1],s,re.I):
            print(x['id'],'['+x.get('subject','')+']',x['q'][:200]); print('   key:',x['o'][x['a']][:150],'|',x['basis'][:100])
