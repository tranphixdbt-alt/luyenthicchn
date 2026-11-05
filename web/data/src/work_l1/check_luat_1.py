# Validate luat_1.json: schema, answer balance, verbatim quotes (whitespace-collapsed).
# Usage: python3 -I check_luat_1.py [path/to/luat_1.json]
import json, re, sys, pathlib
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
JSON = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "luat_1.json"
DOCS = HERE.parents[3] / "tai_lieu_phap_ly"
SRC_DIRS = [DOCS / "van_ban_txt", DOCS]
KEYS = ["id", "part", "subject", "topic", "level", "q", "o", "a", "e",
        "basis", "quote", "src", "as_of"]
BAD_OPT = re.compile(r"tất cả (các )?(phương án|đáp án)|các phương án trên|không phương án nào|"
                     r"phương án [A-D]\b|đáp án [A-D]\b|\b[A-D] và [A-D]\b|cả [A-D] và", re.I)


def norm(s):
    return " ".join(s.split())


_cache = {}


def src_text(name):
    if name not in _cache:
        path = next((d / name for d in SRC_DIRS if (d / name).is_file()), None)
        assert path, f"source file not found: {name}"
        _cache[name] = norm(path.read_text(encoding="utf-8"))
    return _cache[name]


def main():
    data = json.loads(JSON.read_text(encoding="utf-8"))
    errs = []
    seen_q, seen_id = set(), set()
    for i, it in enumerate(data):
        tag = it.get("id", f"#{i}")
        if list(it.keys()) != KEYS:
            errs.append(f"{tag}: keys {list(it.keys())}")
            continue
        if it["id"] != f"L1-{i + 1:03d}" or it["id"] in seen_id:
            errs.append(f"{tag}: bad/duplicate id")
        seen_id.add(it["id"])
        if it["part"] != "LUAT" or it["subject"] != "LU" or it["as_of"] != "2026-11":
            errs.append(f"{tag}: part/subject/as_of")
        if it["level"] not in (1, 2, 3):
            errs.append(f"{tag}: level")
        o = it["o"]
        if not (isinstance(o, list) and len(o) == 4 and all(isinstance(x, str) and x.strip() for x in o)):
            errs.append(f"{tag}: options must be 4 non-empty strings")
        elif len({norm(x).lower() for x in o}) != 4:
            errs.append(f"{tag}: duplicate options")
        if not (isinstance(it["a"], int) and 0 <= it["a"] <= 3):
            errs.append(f"{tag}: a out of range")
        for x in o:
            if BAD_OPT.search(x):
                errs.append(f"{tag}: option references other options: {x}")
        key = norm(it["q"]).lower()
        if key in seen_q:
            errs.append(f"{tag}: duplicate question")
        seen_q.add(key)
        for f in ("q", "e", "basis", "topic"):
            if not it[f].strip():
                errs.append(f"{tag}: empty {f}")
        qt = norm(it["quote"])
        if not qt or len(qt) > 300:
            errs.append(f"{tag}: quote length {len(qt)}")
        try:
            if qt not in src_text(it["src"]):
                errs.append(f"{tag}: quote NOT found verbatim in {it['src']}: {qt[:80]}...")
        except AssertionError as ex:
            errs.append(f"{tag}: {ex}")
    n = len(data)
    print(f"questions: {n}")
    print("levels:", dict(sorted(Counter(x["level"] for x in data).items())))
    print("answers:", dict(sorted(Counter(x["a"] for x in data).items())))
    print("topics:")
    for t, c in Counter(x["topic"] for x in data).most_common():
        print(f"  {c:3d}  {t}")
    quotes_ok = n - sum(1 for e in errs if "quote NOT found" in e)
    print(f"quotes verbatim: {quotes_ok}/{n}")
    if errs:
        print("ERRORS:")
        print("\n".join("  " + e for e in errs))
        sys.exit(1)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
