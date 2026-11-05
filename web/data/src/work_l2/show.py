"""Print article(s) of a gazette txt file. Usage: python3 -I show.py FILE ART [ART...] (ART like 175 or 106a)."""
import re, sys
D = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
f, arts = sys.argv[1], sys.argv[2:]
lines = open(D + f, encoding='utf-8').read().split('\n')
head = re.compile(r'^\s*Điều (\d+[a-zđ]?)\. ')
for a in arts:
    on = False
    for i, l in enumerate(lines):
        m = head.match(l)
        if m:
            if on and m.group(1) != a:
                break
            if m.group(1) == a:
                on = True
        if on:
            print(f'{i+1}: {l}')
    print('-' * 40)
