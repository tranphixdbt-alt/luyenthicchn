# Print questions readably: python3 -I dump.py START END
import json, sys, pathlib
d = json.loads((pathlib.Path(__file__).resolve().parent.parent / "luat_1.json").read_text(encoding="utf-8"))
s, e = int(sys.argv[1]), int(sys.argv[2])
for x in d[s - 1:e]:
    print(f"== {x['id']} L{x['level']} [{x['topic']}] key={'ABCD'[x['a']]}")
    print("Q:", x["q"])
    for i, o in enumerate(x["o"]):
        print(f"  {'ABCD'[i]}{'*' if i == x['a'] else ' '} ({len(o)}) {o}")
    print("E:", x["e"])
    print("B:", x["basis"])
    print("QT:", x["quote"], "|", x["src"][:20])
