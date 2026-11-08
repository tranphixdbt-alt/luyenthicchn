"""Kiểm tra quote của cm_6 có nguyên văn trong src (cùng chuẩn hoá với kiem_tra.py)."""
import json, re, sys, unicodedata
from pathlib import Path
sys.path.insert(0, '/home/user/cchn_moi/web/tools')
import kiem_tra as K
d = json.loads(Path('/home/user/cchn_moi/web/data/src/cm_6.json').read_text(encoding='utf-8'))
for q in d:
    if not q.get('quote'):
        continue
    t = K.doc_text(q['src'])
    ok = t is not None and (K.norm_ws(q['quote']) in t or K.loose(q['quote']) in K.loose(t))
    print(q['id'], 'OK' if ok else 'MISMATCH', q['src'])
