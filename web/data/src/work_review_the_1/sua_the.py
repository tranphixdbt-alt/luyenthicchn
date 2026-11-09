# Áp các sửa đổi sau soát xét lần 2 vào the_nho/{PT,BC,BL,QU}.json (giữ id). Chạy: python3 -I sua_the.py
import json, pathlib
D = pathlib.Path(__file__).resolve().parents[1] / "the_nho"
GPT = "Giáo trình Phân tích và đầu tư chứng khoán (UBCKNN/SRTC) – "
GBC = "Giáo trình Phân tích báo cáo tài chính doanh nghiệp (UBCKNN/SRTC) – "
GBL = "Giáo trình Tư vấn tài chính & bảo lãnh phát hành (UBCKNN/SRTC) – "
GQU = "Giáo trình Quản lý quỹ & tài sản (UBCKNN/SRTC) – "
LUAT = "Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH 2026)"
T121 = "TT 121/2020/TT-BTC (VBHN 09/VBHN-BTC 2026)"

EDITS = {
 "PT-05": dict(front="Giá trị hiện tại của niên kim vĩnh viễn (dòng tiền đều mãi mãi)",
   back="Nhận C cuối mỗi kỳ, mãi mãi: PV = C/r (r: lãi suất mỗi kỳ). Khoản đầu tiên ở cuối kỳ k + 1: PV = (C/r)/(1 + r)^k. VD cổ tức ưu đãi cố định 1.200 đ/năm, r = 10% ⇒ PV = 12.000 đ."),
 "PT-11": dict(back="Cov(A,B) = Σ pᵢ[R_Ai − E(R_A)][R_Bi − E(R_B)] (pᵢ: xác suất kịch bản i). Cov > 0: lợi suất biến động cùng chiều; Cov < 0: ngược chiều; Cov = 0: không có quan hệ tuyến tính."),
 "PT-37": dict(front="P/B hợp lý theo mô hình tăng trưởng cổ tức đều (justified P/B)",
   back="P₀/B₀ = (ROE − g)/(r − g) (B₀: giá trị sổ sách mỗi cổ phiếu, r: lợi suất yêu cầu, g = ROE × b). ROE > r ⇒ P/B > 1; ROE = r ⇒ P/B = 1. Hay dùng cho ngân hàng, CTCK.",
   basis=GPT + "Định giá theo hệ số P/B"),
 "PT-39": dict(back="FCFF = EBIT × (1 − t) + khấu hao − CAPEX − tăng vốn lưu động (= FCFE + lãi vay × (1 − t) − vay ròng). Chiết khấu bằng WACC ⇒ giá trị DN; giá trị vốn chủ = giá trị DN − giá trị nợ vay."),
 "BC-05": dict(front="Bộ báo cáo tài chính năm của doanh nghiệp gồm những báo cáo nào (chế độ kế toán áp dụng từ năm 2026)?",
   back="Báo cáo tình hình tài chính (trước đây gọi là Bảng cân đối kế toán), Báo cáo kết quả hoạt động kinh doanh, Báo cáo lưu chuyển tiền tệ, Thuyết minh báo cáo tài chính.",
   basis="Điều 17 TT 99/2025/TT-BTC hướng dẫn Chế độ kế toán doanh nghiệp (hiệu lực 01/01/2026, thay TT 200/2014/TT-BTC); VAS 21 – Trình bày báo cáo tài chính"),
 "BC-08": dict(front="Doanh nghiệp (không phải ngân hàng, tổ chức tài chính): lãi vay đã trả, lãi và cổ tức nhận được, cổ tức đã trả thuộc luồng tiền nào?",
   basis="VAS 24 – Báo cáo lưu chuyển tiền tệ, đoạn 22 (đoạn 23: quy định riêng cho ngân hàng, TCTD, tổ chức tài chính)"),
 "BC-09": dict(back="LN + chi phí không bằng tiền (khấu hao, dự phòng) − lãi (+ lỗ) từ HĐ đầu tư − tăng (+ giảm) phải thu, hàng tồn kho + tăng (− giảm) phải trả HĐKD. Ở Việt Nam, điểm xuất phát là LN trước thuế."),
 "BC-27": dict(front="Tỷ suất sinh lời trên vốn chủ sở hữu (ROE): công thức và lưu ý khi dùng",
   back="ROE = LNST/VCSH bình quân (BCTC hợp nhất: phần của cổ đông công ty mẹ): mỗi đồng vốn chủ tạo ra bao nhiêu đồng LNST. VCSH âm hoặc quá nhỏ thì ROE mất ý nghĩa."),
 "BC-32": dict(back="P/E = giá thị trường mỗi cổ phiếu/EPS: số đồng nhà đầu tư trả cho một đồng lợi nhuận. P/E trượt dùng EPS 4 quý gần nhất, P/E dự phóng dùng EPS kỳ tới; EPS âm thì P/E không có ý nghĩa."),
 "BL-07": dict(front="Chào bán cổ phiếu lần đầu ra công chúng (IPO): cổ đông lớn trước đợt chào bán phải cam kết nắm giữ thế nào?",
   back="Cùng nhau nắm giữ ít nhất 20% vốn điều lệ của tổ chức phát hành, tối thiểu 01 năm kể từ ngày kết thúc đợt chào bán.",
   basis="Điểm đ khoản 1 Điều 15 " + LUAT),
 "BL-08": dict(basis="Điểm a khoản 2 Điều 23 " + T121),
 "BL-09": dict(basis="Điểm c khoản 2 Điều 23 " + T121),
 "BL-10": dict(basis="Điểm b khoản 2 Điều 23 " + T121),
 "BL-11": dict(basis="Khoản 3 Điều 23 " + T121),
 "BL-13": dict(basis="Khoản 2, 4 Điều 42 NĐ 155/2020/NĐ-CP (không bị NĐ 245/2025/NĐ-CP sửa đổi)"),
 "BL-18": dict(back="Chi phí giám sát của cổ đông (kiểm toán, HĐQT độc lập), chi phí ràng buộc người quản lý tự chịu để cam kết hành động vì cổ đông, và tổn thất còn lại khi lợi ích hai bên vẫn lệch nhau."),
 "BL-20": dict(basis="Khoản 2 Điều 25 " + T121),
 "BL-34": dict(front="Giá trị lý thuyết của một quyền mua cổ phần",
   back="= (P₀ − S)/(N + 1) = (Pₓ − S)/N (N: số quyền để mua 1 CP mới; P₀, Pₓ: giá trước, sau ngày không hưởng quyền; S: giá phát hành). VD 5 quyền mua 2 CP (N = 2,5), P₀ = 25.000, S = 18.000 ⇒ 2.000 đ.",
   basis=GBL + "Phát hành quyền mua cổ phần: giá trị quyền"),
 "BL-38": dict(front="Trả cổ tức bằng cổ phiếu tỷ lệ k: ảnh hưởng tới VCSH, số cổ phiếu và tỷ lệ sở hữu",
   back="Tổng VCSH không đổi (chỉ chuyển LNST chưa phân phối sang vốn góp của chủ sở hữu); số cổ phiếu tăng (1 + k) lần; tỷ lệ sở hữu không đổi; EPS, giá trị sổ sách mỗi CP giảm còn 1/(1 + k)."),
 "BL-45": dict(front="Định giá DN theo phương pháp tài sản: cách tính giá trị vốn chủ sở hữu và hạn chế",
   back="= Giá trị thực tế tài sản (đánh giá lại theo giá thị trường) − Nợ thực tế phải trả. Dễ kiểm chứng, nhưng không phản ánh khả năng sinh lời tương lai và lợi thế kinh doanh của DN."),
 "QU-09": dict(back="Tổng lệnh bán − tổng lệnh mua (kể cả chuyển đổi) tại ngày giao dịch ≥ 5% NAV (từ 12/02/2026; trước là trên 10%); hoặc thực hiện hết lệnh làm NAV quỹ < 50 tỷ đồng."),
 "QU-13": dict(basis="Khoản 3, 4 Điều 110 " + LUAT + "; khoản 6, 7 Điều 24 TT 98/2020/TT-BTC (quỹ mở: khoản 5, 6 Điều 35 dẫn chiếu)"),
 "QU-14": dict(back="50% / 20% tổng giá trị giao dịch chứng khoán trong năm của quỹ (không áp dụng: quỹ hoạt động chưa đủ 06 tháng, tính đến hết năm thành lập; quỹ mở trái phiếu có giá trị giao dịch năm dưới 300 tỷ đồng)",
   basis="Điểm a khoản 7 Điều 10 TT 99/2020/TT-BTC (bản tiếng Việt; TT 88/2025/TT-BTC chỉ sửa khoản 4 Điều 29)"),
 "QU-46": dict(topic="Một số sản phẩm đầu tư thay thế",
   front="Cơ cấu phí “2 và 20” của quỹ phòng hộ tính thế nào?",
   back="Phí quản lý 2%/năm trên tài sản quản lý (thu cả khi lỗ) + phí thưởng 20% lợi nhuận (thường sau phí quản lý). VD tài sản 100, lãi gộp 18: phí = 2 + 20% × 16 = 5,2 ⇒ NĐT còn 12,8%.",
   basis=GQU + "Quỹ phòng hộ – cơ cấu phí"),
}

for sj in ["PT", "BC", "BL", "QU"]:
    p = D / f"{sj}.json"
    cards = json.loads(p.read_text(encoding="utf-8"))
    for c in cards:
        for k, v in EDITS.get(c["id"], {}).items():
            c[k] = v
    for c in cards:
        assert len(c["front"]) <= 160 and len(c["back"]) <= 220, (c["id"], len(c["front"]), len(c["back"]))
    p.write_text(json.dumps(cards, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("đã sửa", len(EDITS), "thẻ")
