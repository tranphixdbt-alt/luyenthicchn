"""Tìm câu gần trùng trong questions.json (trừ C8) và cm_9.json theo từ khóa: python3 -I grep_bank.py kw1 kw2 ..."""
import json, sys, re
from pathlib import Path
D = Path(__file__).resolve().parent.parent.parent
qs = [q for q in json.loads((D / "questions.json").read_text()) if not q["id"].startswith("C8-")]
ids = {q["id"] for q in qs}
qs += [q for q in json.loads((D / "src" / "cm_9.json").read_text()) if q["id"] not in ids]
for kw in sys.argv[1:]:
    print("==", kw)
    for q in qs:
        t = q["q"] + " | " + " / ".join(q["o"])
        if re.search(kw, t, re.I):
            print(" ", q["id"], q["q"][:160].replace("\n", " "), "||", " / ".join(q["o"])[:200])
