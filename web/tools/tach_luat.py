"""Tách Luật Chứng khoán hợp nhất (VBHN 24/2025, bản Công báo) thành từng Điều -> data/luat_ck.json.
Bỏ dòng đầu trang Công báo và phần chú thích cuối trang; giữ đánh dấu điều được sửa đổi theo chú thích."""
import json, re, sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(sys.argv[2])
lines = src.splitlines()
start = next(i for i, l in enumerate(lines) if re.match(r"^\s*Chương I\b", l) or re.match(r"^\s+Điều 1\. ", l))
body, notes, in_note = [], {}, False
cur_note = None
for l in lines[start:]:
    if re.search(r"CÔNG BÁO/Số", l):            # đầu trang mới: hết vùng chú thích
        in_note = False; continue
    m = re.match(r"^\s{2,}(\d{1,3})\s*$", l)     # dòng chỉ có số = bắt đầu một chú thích
    if m:
        in_note = True; cur_note = int(m.group(1)); notes[cur_note] = ""; continue
    if in_note:
        notes[cur_note] += " " + l.strip(); continue
    body.append(l)

arts, chap, chap_open = [], "", False
for l in body:
    s = l.strip()
    if re.match(r"^Chương [IVXLC]+\b", s):
        chap = s; chap_open = True; continue
    if chap_open and s and s.isupper() and not re.match(r"^Điều \d", s):
        chap += (". " if chap_open is True else " ") + s.title() if False else (". " if chap_open is True else " ") + s; chap_open = "more"; continue
    if s: chap_open = False
    m = re.match(r"^\s+Điều (\d+[a-z]?)\.\s+(.*)$", l)
    if m:
        arts.append({"so": m.group(1), "ten": m.group(2).strip(), "chuong": chap, "noi_dung": []}); continue
    if arts and s:
        a = arts[-1]
        a["noi_dung"].append(s)

FN = re.compile(r"(?:(?<=[^\W\d_])|(?<=[^\W\d_][.:;”)]))(\d{1,3})(?=\s|$)")   # số chú thích dính sau chữ, vd "từ ngữ12", "như sau:5" (không đụng "1.000")
LEAD = re.compile(r"^(\d+[a-z]?\.|[a-zđ]\))(\d{1,3})(?=\s)")
def clean(t):
    return FN.sub("", LEAD.sub(lambda m: m.group(1) if int(m.group(2)) in notes else m.group(0), t))
def marks(t):
    m = LEAD.match(t.strip())
    return [int(x) for x in FN.findall(t)] + ([int(m.group(2))] if m and int(m.group(2)) in notes else [])

res = []
for a in arts:
    # nối dòng: dòng mới bắt đầu bằng "1." "a)" "-" "+" là đoạn mới
    paras = []
    for s in a["noi_dung"]:
        if paras and not re.match(r"^(\d+[a-z]?\.|[a-zđ]\)|-|\+|“\d|“[a-zđ]\))", s):
            paras[-1] += " " + s
        else:
            paras.append(s)
    title = clean(a["ten"])
    if paras and paras[0][:1].islower() and not re.match(r"^[a-zđ]\)", paras[0]) and len(paras[0]) < 90:
        title += " " + clean(paras.pop(0))
    res.append({"so": a["so"], "ten": title.strip(), "chuong": clean(a["chuong"]), "doan": [clean(p) for p in paras]})
# điều có số chú thích trỏ tới ghi chú "sửa đổi/bổ sung/bãi bỏ" -> gắn cờ và giữ ghi chú
for a, raw in zip(res, arts):
    ns = [n for t in [raw["ten"], *raw["noi_dung"]] for n in marks(t) if n in notes]
    ghi = [re.sub(r"(Luật số 56/2024/QH15) sửa đổi, bổ sung một số điều của Luật Chứng khoán.*?Luật Xử lý vi phạm hành chính,", r"\1,",
                  re.sub(r"\s+", " ", notes[n]).strip()) for n in ns if re.search(r"sửa đổi|bổ sung|bãi bỏ", notes[n])]
    a["sua_doi"] = bool(ghi); a["ghi_chu"] = ghi[:3]
seen = set(); uniq = []
for a in res:                     # giữ lần xuất hiện đầu của mỗi số điều
    if a["so"] in seen: continue
    seen.add(a["so"]); uniq.append(a)
out.write_text(json.dumps({"van_ban": "Luật Chứng khoán số 54/2019/QH14, hợp nhất theo VBHN 24/VBHN-VPQH năm 2025 (đã gồm sửa đổi của Luật 56/2024/QH15)",
                           "nguon": "Công báo số 531+532 ngày 18/3/2025", "dieu": uniq}, ensure_ascii=False), encoding="utf-8")
print(len(uniq), "điều;", sum(a["sua_doi"] for a in uniq), "điều có chú thích sửa đổi;", len(notes), "chú thích")
