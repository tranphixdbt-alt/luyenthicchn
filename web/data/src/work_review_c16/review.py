"""Soát chéo C16-001..015 và C9-033: tính lại số, sửa tại chỗ, kiểm trích dẫn nguyên văn.
Chạy: python3 -I web/data/src/work_review_c16/review.py (từ thư mục gốc dự án)."""
import json, math, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "web/data/src"
VB = ROOT / "tai_lieu_phap_ly/van_ban_txt"
TT120 = "TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt"
TT121 = "VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt"
B120 = "Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC/2026, hợp nhất TT 68/2024, TT 18/2025, TT 08/2026)"
GT = "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC)"

def loose(s):
    return re.sub(r"[^\w]", "", unicodedata.normalize("NFC", s).lower())

def check_quote(q):
    if not q.get("quote"): return
    text = (VB / q["src"]).read_text(encoding="utf-8")
    assert loose(q["quote"]) in loose(text), (q["id"], "quote")

def assert_key(q, val):
    assert q["o"][q["a"]] == val, (q["id"], q["o"][q["a"]], val)

# ---- tính lại ----
# C16-003: loại Z (k6 Đ9 TT120); tổng tài sản gồm tiền + tiền bán chờ về + CK được ký quỹ (đề nêu rõ)
ta = 40 + 60 + 700; r003 = (ta - 450) / ta
assert f"{r003*100:.2f}" == "43.75"
assert round((1000 - 450) / 1000 * 100, 2) == 55.0 and round((740 - 450) / 740 * 100, 2) == 39.19 and 350 / 700 == .5

# C16-005: giả định 200% / 3% / 10%
room, cust = 2 * 2400 - 4700, 0.03 * 2400
assert min(90, room, cust) == 72 and room == 100 and 0.10 * 2400 == 240

# C16-011
debt = 20000 * 30000 + 30000 * 20000 - 600e6
v = 20000 * 24000 + 30000 * 23000
assert f"{(v - debt) / v * 100:.2f}" == "48.72"
assert f"{(v - debt) / 1200e6 * 100:.2f}" == "47.50" and f"{debt / v * 100:.2f}" == "51.28"
assert f"{(480e6 - 300e6) / 480e6 * 100:.2f}" == "37.50"

# C16-012
d = 0.4 * 3000 * 40000; Pth = d / (3000 * 0.65)
n = next(k for k in range(1, 20) if 40000 * 0.93 ** k < Pth)
assert n == 7 and math.ceil((1 - Pth / 40000) / 0.07) == 6 and next(k for k in range(1, 20) if 0.93 ** k < 0.65) == 6

# C16-013
cash = 2000 * 60000 * 1.5; liab = 2000 * 72000; eq = cash - liab
assert eq / liab == 0.25
x = 0.30 * liab - eq; assert round(x) == 7_200_000
assert round((0.3 * liab - eq) / 0.7) == 10_285_714          # công thức vị thế mua
assert 2000 * 12000 == 24_000_000 and 0.05 * 120e6 == 6_000_000   # lỗ; thiếu 5 điểm % × giá trị bán

# C16-014
val, dbt = 10000 * 34000, 250e6; eq = val - dbt
assert round(eq / val, 4) == 0.2647
eq2 = eq + 0  # nộp 20 tr trả nợ: vốn tự có = giá trị − nợ mới
dbt2 = dbt - 20e6; eq2 = val - dbt2
S = val - eq2 / 0.35; sh = math.ceil(S / 34000); assert sh == 757
rem = 10000 - sh; assert (rem * 34000 - (dbt2 - sh * 34000)) / (rem * 34000) >= 0.35
assert math.ceil((0.35 * val - eq - 20e6) / 34000) == 265
assert math.ceil((360e6 - 110e6 / 0.35) / 34000) == 1345
assert math.ceil((val - eq / 0.35) / 34000) == 2437

# C9-033 (đổi số để không trùng số liệu với C9-032)
assert 360e6 / 0.6 / 30000 == 20000 and 360e6 / 30000 == 12000
assert round(360e6 * 1.6 / 30000) == 19200 and round(360e6 / 0.4 / 30000) == 30000

# ---- sửa ----
p16 = SRC / "cm_16.json"; L = json.loads(p16.read_text(encoding="utf-8")); Q = {q["id"]: q for q in L}

q = Q["C16-003"]
q["q"] = ("Tài khoản giao dịch ký quỹ của khách hàng có: tiền 40 triệu đồng; tiền bán chứng khoán chờ về 60 triệu đồng; "
          "chứng khoán thuộc danh sách được giao dịch ký quỹ trị giá 700 triệu đồng; cổ phiếu Z trị giá 200 triệu đồng "
          "(vừa bị Sở giao dịch đưa ra khỏi danh sách được giao dịch ký quỹ); dư nợ 450 triệu đồng. Hợp đồng quy định "
          "tỷ lệ ký quỹ = (Tổng tài sản − Dư nợ)/Tổng tài sản, trong đó tổng tài sản gồm tiền, tiền bán chứng khoán chờ về "
          "và giá trị chứng khoán được tính làm tài sản bảo đảm theo quy định. Theo Thông tư 120/2020/TT-BTC, tỷ lệ ký quỹ của tài khoản là")
q["e"] = ("Khoản 6 Điều 9 TT 120/2020: chứng khoán không được phép giao dịch ký quỹ không được tính vào tài sản bảo đảm khi xác định "
          "tỷ lệ ký quỹ ban đầu và duy trì ⇒ loại cổ phiếu Z. Tổng tài sản = 40 + 60 + 700 = 800 triệu đồng; tài sản thực có = "
          "800 − 450 = 350 ⇒ tỷ lệ = 350/800 = 43,75%. Lỗi thường gặp: vẫn tính Z ((1.000 − 450)/1.000 = 55,00%), bỏ tiền bán "
          "chờ về ((740 − 450)/740 = 39,19%), chia tài sản thực có cho riêng giá trị chứng khoán (350/700 = 50,00%).")
q["basis"] = "Khoản 6 Điều 9 " + B120

q = Q["C16-005"]
q["q"] = ("Giả sử quy chế hạn mức cho vay giao dịch ký quỹ áp dụng như sau: tổng dư nợ cho vay ký quỹ của công ty không vượt quá "
          "200% vốn chủ sở hữu; cho vay một khách hàng không vượt quá 3% vốn chủ sở hữu; dư nợ đối với một loại chứng khoán không "
          "vượt quá 10% vốn chủ sở hữu. Công ty chứng khoán K có vốn chủ sở hữu 2.400 tỷ đồng, tổng dư nợ cho vay ký quỹ hiện là "
          "4.700 tỷ đồng. Khách hàng M chưa có dư nợ, đề nghị vay ký quỹ 90 tỷ đồng để mua một mã cổ phiếu mà K còn dư hạn mức "
          "theo mã. K được cho M vay tối đa")
q["o"] = ["72 tỷ đồng", "100 tỷ đồng", "240 tỷ đồng", "90 tỷ đồng"]; q["a"] = 0
q["e"] = ("Hạn mức tổng: 200% × 2.400 = 4.800 tỷ ⇒ còn 4.800 − 4.700 = 100 tỷ; hạn mức một khách hàng: 3% × 2.400 = 72 tỷ. "
          "Mức cho vay tối đa = min(90; 100; 72) = 72 tỷ đồng. Lỗi thường gặp: chỉ xét hạn mức tổng (100), đáp ứng đủ đề nghị (90), "
          "dùng nhầm hạn mức theo một loại chứng khoán 10% (240). Các tỷ lệ là giả định của đề (theo quy chế giao dịch ký quỹ của "
          "UBCKNN ban hành theo khoản 8 Điều 9 TT 120/2020; UBCKNN có thể điều chỉnh).")
q["basis"] = GT + " – Hạn mức cho vay giao dịch ký quỹ (tỷ lệ là giả định của đề)"
q["quote"] = q["src"] = ""

Q["C16-006"].update({
    "q": "Theo Thông tư 120/2020/TT-BTC, chứng khoán được giao dịch ký quỹ phải đáp ứng các tiêu chí cơ bản sau, NGOẠI TRỪ:",
    "o": ["Thời gian niêm yết, đăng ký giao dịch của chứng khoán",
          "Tính thanh khoản và biến động giá của chứng khoán (nếu có)",
          "Tỷ lệ chi trả cổ tức bằng tiền tối thiểu trong năm gần nhất",
          "Quy mô vốn và kết quả kinh doanh của tổ chức phát hành"],
    "a": 2,
    "e": ("Khoản 4 Điều 9: chứng khoán được giao dịch ký quỹ là cổ phiếu niêm yết, đăng ký giao dịch, chứng chỉ quỹ niêm yết "
          "đáp ứng các tiêu chí cơ bản: thời gian niêm yết, đăng ký giao dịch; quy mô vốn và kết quả hoạt động kinh doanh của tổ "
          "chức phát hành; tính thanh khoản và biến động giá (nếu có); minh bạch thông tin và tiêu chí khác theo quy chế của UBCKNN. "
          "Không có tiêu chí về tỷ lệ chi trả cổ tức bằng tiền."),
    "basis": "Khoản 4 Điều 9 " + B120,
    "quote": ("đáp ứng các tiêu chí cơ bản sau: thời gian niêm yết, đăng ký giao dịch; quy mô vốn và kết quả hoạt động kinh doanh "
              "của tổ chức phát hành; tính thanh khoản và biến động giá (nếu có); minh bạch thông tin"),
    "src": TT120})

Q["C16-007"].update({
    "q": ("Xét các việc sau tại công ty chứng khoán P (đã được cung cấp dịch vụ giao dịch ký quỹ):\n"
          "I. Cho thành viên Ban kiểm soát của P vay tiền mua chứng khoán trên tài khoản giao dịch ký quỹ\n"
          "II. Ký hợp đồng giao dịch ký quỹ với cá nhân nước ngoài đã có mã số giao dịch chứng khoán\n"
          "III. Cho vay ký quỹ mua cổ phiếu đăng ký giao dịch có trong danh sách Sở giao dịch công bố và được P lựa chọn\n"
          "IV. Tiếp tục ký mới hợp đồng giao dịch ký quỹ khi P không còn đáp ứng điều kiện cung cấp dịch vụ cho vay tiền mua chứng khoán\n"
          "Những việc nào P KHÔNG được thực hiện?"),
    "o": ["I và II", "II, III và IV", "I, II, III và IV", "I, II và IV"],
    "a": 3,
    "e": ("I: khoản 3 Điều 27 TT 121/2020 – công ty chứng khoán không được cho vay dưới bất kỳ hình thức nào đối với chủ sở hữu, "
          "cổ đông lớn, thành viên Ban kiểm soát, HĐQT, HĐTV, Ban Giám đốc, kế toán trưởng… và người có liên quan. II: khoản 2 Điều 9 "
          "TT 120/2020 – nhà đầu tư nước ngoài không được thực hiện giao dịch ký quỹ. IV: khoản 7 Điều 9 TT 120/2020 – phải ngừng ngay "
          "việc ký mới, gia hạn hợp đồng, ngừng cho vay và báo cáo UBCKNN trong 48 giờ. III được phép: khoản 4, 5 Điều 9 TT 120/2020 – "
          "chứng khoán được giao dịch ký quỹ gồm cả cổ phiếu đăng ký giao dịch đáp ứng tiêu chí; công ty lựa chọn trên cơ sở danh sách "
          "Sở giao dịch công bố."),
    "basis": "Khoản 3 Điều 27 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026); khoản 2, 4, 5, 7 Điều 9 " + B120,
    "quote": ("Công ty chứng khoán không được cho vay dưới bất kỳ hình thức nào đối với Chủ sở hữu, cổ đông lớn, thành viên Ban "
              "Kiểm soát, thành viên Hội đồng quản trị"),
    "src": TT121})

q = Q["C16-008"]
q["e"] = q["e"].replace(" Công ty không được cam kết lợi nhuận cho khách hàng.", " Lợi nhuận kỳ vọng không phải nội dung bắt buộc của hợp đồng.")
q["o"] = [q["o"][3]] + q["o"][:3]; q["a"] = 0

q = Q["C16-009"]
q["e"] = q["e"].replace(" Công ty không được tự chuyển chứng khoán của khách hàng sang tài khoản của mình.",
                        " Khoản 6 không cho phép công ty chuyển chứng khoán của khách hàng sang tài khoản tự doanh thay cho việc bán.")

q = Q["C16-010"]
q["e"] = q["e"].replace("(hiện là Quy chế kèm Quyết định 87/QĐ-UBCK)", "(các kết luận thanh tra của UBCKNN năm 2024–2025 dẫn chiếu Quy chế kèm Quyết định 87/QĐ-UBCK)")
q["e"] = q["e"].replace(" (không thấp hơn mức tối thiểu của quy chế)", "")

q = Q["C16-013"]
q["o"] = ["6.000.000 đồng", "24.000.000 đồng", "10.285.714 đồng", "7.200.000 đồng"]; q["a"] = 3
q["e"] = q["e"].replace("đưa về tỷ lệ ban đầu 50% (72 − 36 = 36 triệu)", "chỉ bù 5 điểm phần trăm thiếu hụt trên giá trị bán ban đầu (5% × 120 = 6 triệu)")

q = Q["C16-015"]
q["o"] = [q["o"][1], q["o"][0]] + q["o"][2:]; q["a"] = 0
q["e"] = ("Giáo trình: giá trị thị trường hiện hành thường tính theo giá đóng cửa ngày giao dịch liền trước; ngày mua là tổng số tiền "
          "phải trả cho chứng khoán (gồm hoa hồng, phí); ngày bán là số tiền thực nhận sau khi trừ hoa hồng, phí và thuế (không phải "
          "giá trị gộp, càng không phải giá vốn). Cách định giá cụ thể do hợp đồng giao dịch ký quỹ giữa công ty và khách hàng quy định.")
q["basis"] = GT + " – Giá trị thị trường hiện hành trên tài khoản giao dịch ký quỹ"

for q in L:
    assert q["topic"] == "Giao dịch cổ phiếu trên thị trường chứng khoán" and len(q["o"]) == 4
    assert "87/QĐ-UBCK" not in q["basis"] + q.get("quote", ""), q["id"]
    check_quote(q)
assert_key(Q["C16-003"], "43,75%"); assert_key(Q["C16-005"], "72 tỷ đồng"); assert_key(Q["C16-011"], "48,72%")
assert_key(Q["C16-012"], "7"); assert_key(Q["C16-013"], "7.200.000 đồng"); assert_key(Q["C16-014"], "757 cổ phiếu")
assert_key(Q["C16-007"], "I, II và IV"); assert_key(Q["C16-015"], "I và II"); assert_key(Q["C16-004"], "I và II")
p16.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

p9 = SRC / "cm_9.json"; L9 = json.loads(p9.read_text(encoding="utf-8"))
q = next(x for x in L9 if x["id"] == "C9-033")
q["q"] = ("Giả sử quy chế của công ty chứng khoán quy định tỷ lệ ký quỹ ban đầu 60% (vốn tự có/giá trị chứng khoán mua). Khách hàng "
          "có 360 triệu đồng tiền mặt, muốn dùng tối đa sức mua ký quỹ để mua cổ phiếu giá 30.000 đồng. Bỏ qua phí giao dịch, khối "
          "lượng tối đa khách hàng có thể mua là")
q["e"] = ("Sức mua = vốn tự có/tỷ lệ ký quỹ ban đầu = 360/0,6 = 600 triệu đồng (vay tối đa 240 triệu) ⇒ 600.000.000/30.000 = 20.000 "
          "cổ phiếu. Lỗi thường gặp: chỉ dùng tiền mặt (12.000), lấy 360 × (1 + 60%) (19.200), chia cho phần vay 40% thay vì tỷ lệ ký "
          "quỹ 60% (30.000). Tỷ lệ ký quỹ ban đầu là giả định của đề; công ty quy định trong hợp đồng theo quy chế của UBCKNN.")
q["basis"] = GT + " – Sức mua trong giao dịch ký quỹ (tỷ lệ là giả định của đề)"
assert_key(q, "20.000 cổ phiếu")
p9.write_text(json.dumps(L9, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("OK")
