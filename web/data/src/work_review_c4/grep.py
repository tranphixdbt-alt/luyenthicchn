"""Usage: python3 -I grep.py FILE_SUBSTR REGEX [ctx]  -- searches whitespace-normalised text"""
import re,sys,glob
B='/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
fs=[f for f in glob.glob(B+'*.txt') if sys.argv[1] in f]
ctx=int(sys.argv[3]) if len(sys.argv)>3 else 300
for f in fs:
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
    for m in re.finditer(sys.argv[2],t):
        print('==',f.split('/')[-1],m.start()); print(t[max(0,m.start()-ctx):m.end()+ctx]); print()
