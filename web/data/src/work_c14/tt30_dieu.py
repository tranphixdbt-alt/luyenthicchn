# In các điều của TT 30/2019 (bản caselaw, chỉ để đọc; trích dẫn chính thức lấy từ Công báo)
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
t = t[t.find("Theo đề nghị"):]
parts = re.split(r"(?=Điều \d+\. )", t)
want = set(sys.argv[2].split(","))
for p in parts:
    m = re.match(r"Điều (\d+)\. ", p)
    if m and m.group(1) in want:
        print(p[:6000]); print("=" * 40)
