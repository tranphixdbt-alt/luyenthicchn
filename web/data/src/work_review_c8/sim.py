"""Độ gần (Jaccard từ của đề + phương án) giữa câu C8 với đề công khai của đối thủ và với ngân hàng câu của ta.
Chạy: python3 -I sim.py <public_bank.json>"""
import json, re, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
W = lambda s: set(re.findall(r"\w+", s.lower()))
c8 = json.loads((D / "cm_8.json").read_text())
pb = json.loads(Path(sys.argv[1]).read_text())
comp = list(pb["LAW"]) + [q for v in pb["CC"].values() for q in v]
comp = [(q["id"], W(q["cau_hoi"] + " " + " ".join(q.get(k, "") for k in "ABCDE"))) for q in comp]
bank = [q for q in json.loads((D.parent / "questions.json").read_text()) if not q["id"].startswith("C8-")]
bank = [(q["id"], W(q["q"] + " " + " ".join(q["o"]))) for q in bank]
j = lambda a, b: len(a & b) / len(a | b)
for q in c8:
    w = W(q["q"] + " " + " ".join(q["o"]))
    c = max(comp, key=lambda x: j(w, x[1])); b = max(bank, key=lambda x: j(w, x[1]))
    print(q["id"], f"đối thủ {c[0]} {j(w, c[1]):.2f} | ngân hàng {b[0]} {j(w, b[1]):.2f}")
