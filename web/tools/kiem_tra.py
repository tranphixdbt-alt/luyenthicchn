"""Gộp các file câu hỏi trong data/src/, kiểm tra tự động rồi ghi data/questions.json.

Kiểm tra: đúng cấu trúc, 4 phương án, một đáp án; không có phương án kiểu "A và B"/"Tất cả";
không trùng câu; câu Luật phải có trích dẫn khớp nguyên văn văn bản gốc. Sau đó xoay thứ tự phương án
để vị trí đáp án đúng chia đều A/B/C/D (an toàn vì không phương án nào tham chiếu phương án khác).
Chạy: python3 -I tools/kiem_tra.py   (thoát mã 1 nếu có lỗi chặn)
"""
import json, re, sys, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "src"
DOCS = ROOT.parent / "tai_lieu_phap_ly"
FILES = ["luat_1.json", "luat_2.json", "luat_3.json", "luat_4.json", "luat_5.json", "luat_6.json", "cm_1.json", "cm_2.json", "cm_3.json", "cm_4.json", "cm_5.json", "cm_6.json", "cm_7.json", "cm_8.json", "cm_9.json", "cm_10.json", "cm_11.json", "cm_12.json"]
SUBJ = {"LU", "CB", "PT", "MG", "BC", "BL", "QU", "PS"}
REF = re.compile(r"(\b[A-Da-d]\s*(và|,|&)\s*[A-Da-d]\b)|tất cả (các )?(phương án|đáp án|ý|câu) (trên|đều)|cả (hai|ba|bốn) (phương án|ý|đáp án)|không (có )?(phương án|đáp án|ý|câu) nào", re.I)
LETTER_IN_E = re.compile(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b")

def norm_ws(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()

_doc_cache = {}
def doc_text(name):
    if name not in _doc_cache:
        p = next((d / name for d in [DOCS / "van_ban_txt", DOCS] if (d / name).exists()), None)
        if not p:
            _doc_cache[name] = None
        else:
            raw = p.read_text(encoding="utf-8")
            clean = "\n".join(l for l in raw.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
            _doc_cache[name] = norm_ws(clean) + " \x00 " + norm_ws(raw)   # bản bỏ đầu trang + bản gốc
    return _doc_cache[name]

def loose(s):   # chỉ giữ chữ và số, bỏ số chú thích dính sau chữ
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"(?<=[^\W\d_])\d{1,3}(?=\W|$)", "", s)
    return re.sub(r"[\W_]+", "", s)

def main():
    qs, errors, warns = [], [], []
    for f in FILES:
        p = SRC / f
        if not p.exists():
            warns.append(f"thiếu file {f}"); continue
        for q in json.loads(p.read_text(encoding="utf-8")):
            q["_file"] = f; qs.append(q)
    ids = Counter(q.get("id") for q in qs)
    for k, v in ids.items():
        if v > 1: errors.append(f"trùng id {k}")
    seen = {}
    for q in qs:
        i = q.get("id", "?")
        for k in ["id", "part", "subject", "topic", "level", "q", "o", "a", "e", "basis"]:
            if q.get(k) in (None, "", []): errors.append(f"{i}: thiếu {k}")
        o = q.get("o", [])
        if len(o) != 4 or len(set(map(str.strip, o))) != 4: errors.append(f"{i}: cần đúng 4 phương án khác nhau")
        if not isinstance(q.get("a"), int) or not 0 <= q["a"] < len(o): errors.append(f"{i}: đáp án không hợp lệ")
        if q.get("subject") not in SUBJ: errors.append(f"{i}: môn {q.get('subject')} không hợp lệ")
        if (q.get("part") == "LUAT") != (q.get("subject") == "LU"): errors.append(f"{i}: phần và môn không khớp")
        if q.get("level") not in (1, 2, 3): errors.append(f"{i}: mức độ phải là 1–3")
        for x in o:
            if REF.search(x): errors.append(f"{i}: phương án tham chiếu phương án khác: {x[:60]}")
        key = loose(q.get("q", ""))
        if key in seen: errors.append(f"{i}: trùng nội dung với {seen[key]}")
        seen[key] = i
        if q.get("part") == "LUAT":
            src, quote = q.get("src", ""), q.get("quote", "")
            text = doc_text(src) if src else None
            if not quote: errors.append(f"{i}: câu Luật thiếu trích dẫn")
            elif text is None: errors.append(f"{i}: không tìm thấy văn bản nguồn {src}")
            elif norm_ws(quote) not in text and loose(quote) not in loose(text): errors.append(f"{i}: trích dẫn không khớp nguyên văn {src}")
    # cảnh báo câu gần trùng (Jaccard từ > 0.8)
    words = [(q["id"], set(re.findall(r"\w+", q.get("q", "").lower()))) for q in qs]
    for a in range(len(words)):
        for b in range(a + 1, len(words)):
            x, y = words[a][1], words[b][1]
            if len(x) > 8 and len(y) > 8 and len(x & y) / len(x | y) > 0.8:
                warns.append(f"gần trùng: {words[a][0]} ~ {words[b][0]}")
    if errors:
        print("LỖI CHẶN:", len(errors)); print("\n".join(errors[:80])); sys.exit(1)
    # xoay phương án để đáp án đúng chia đều A–D (bỏ qua câu có giải thích nhắc tên phương án)
    out, cnt = [], Counter()
    for n, q in enumerate(sorted(qs, key=lambda q: q["id"])):
        target = n % 4
        if LETTER_IN_E.search(q["e"]) or target == q["a"]:
            target = q["a"]
        else:
            o = q["o"][:]; correct = o.pop(q["a"]); o.insert(target, correct); q["o"] = o; q["a"] = target
        cnt[q["a"]] += 1
        out.append({k: q.get(k, "") for k in ["id", "part", "subject", "topic", "level", "q", "o", "a", "e", "basis", "quote", "src", "as_of"]})
    (ROOT / "data" / "questions.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    by = Counter((q["part"], q["subject"]) for q in out)
    print(f"OK: {len(out)} câu → data/questions.json")
    print("theo môn:", dict(sorted(Counter(q['subject'] for q in out).items())))
    print("vị trí đáp án:", dict(sorted(cnt.items())), "| mức độ:", dict(sorted(Counter(q['level'] for q in out).items())))
    # chủ đề Luật/Môi giới phải được gán vào một chuyên đề SRTC trong app.js (SYL), nếu không đề thi thử từng môn sẽ bỏ sót
    js = (ROOT / "app.js").read_text(encoding="utf-8"); syl = js[js.index("const SYL = {"):js.index("\n};", js.index("const SYL = {"))]
    for t in sorted({q["topic"] for q in out if q["subject"] in ("LU", "MG")}):
        if f"'{t}'" not in syl: warns.append(f"chủ đề chưa gán chuyên đề SRTC (SYL trong app.js): {t}")
    if warns: print("CẢNH BÁO:", len(warns)); print("\n".join(warns[:30]))

if __name__ == "__main__":
    main()
