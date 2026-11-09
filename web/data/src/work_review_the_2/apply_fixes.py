# Apply second-pass review fixes to the_nho/CB.json, MG.json, PS.json in place, keeping each file's layout.
# Each change replaces one JSON-encoded field value inside the card with the given id (asserts a single match).
import json, sys, pathlib
D = pathlib.Path(sys.argv[1])  # .../web/data/src/the_nho
VBHN16 = "NĐ 158/2020/NĐ-CP (VBHN 16/VBHN-BTC năm 2026; không bị sửa đổi bởi NĐ 306/2025/NĐ-CP)"
CH = {
 "CB-01": {"front": "Các chức năng cơ bản của thị trường chứng khoán (theo giáo trình)?",
           "back": "Huy động vốn cho nền kinh tế; cung cấp môi trường đầu tư cho công chúng; tạo tính thanh khoản cho chứng khoán; đánh giá hoạt động, giá trị doanh nghiệp; tạo môi trường giúp Chính phủ thực hiện chính sách vĩ mô"},
 "CB-07": {"back": "Chứng khoán phát hành cùng trái phiếu hoặc cổ phiếu ưu đãi, cho người sở hữu quyền mua một số cổ phiếu phổ thông nhất định theo giá định trước, trong khoảng thời gian xác định",
           "basis": "Khoản 5 Điều 4 Luật Chứng khoán (VBHN 102/VBHN-VPQH năm 2026)"},
 "CB-36": {"front": "Người nội bộ (và người có liên quan) giao dịch cổ phiếu dự kiến từ 50 triệu đồng/ngày hoặc 200 triệu đồng/tháng theo mệnh giá: phải làm gì, trong hạn nào?",
           "basis": "Phần mở đầu, điểm a, b, đ khoản 1 Điều 33 TT 96/2020/TT-BTC (ngưỡng 50/200 triệu đồng có từ văn bản gốc; điểm a sửa đổi bởi TT 68/2024, TT 18/2025, TT 08/2026, vẫn giữ 03 ngày làm việc)"},
 "CB-43": {"front": "Luật CK liệt kê 6 nhóm hành vi thao túng TTCK; 3 hành vi giao dịch đầu tiên là gì?"},
 "MG-09": {"basis": "Khoản 1 Điều 97 Luật Chứng khoán (VBHN 102/VBHN-VPQH năm 2026); điểm a khoản 2 Điều 216 NĐ 155/2020/NĐ-CP (không bị sửa đổi bởi NĐ 245/2025/NĐ-CP)"},
 "MG-11": {"basis": "Khoản 3, điểm c khoản 5 Điều 216 NĐ 155/2020/NĐ-CP (không bị sửa đổi bởi NĐ 245/2025/NĐ-CP)"},
 "MG-38": {"back": "Tổng tài sản trên TK ký quỹ (tiền, tiền bán CK chờ về, giá trị CK được phép ký quỹ) − Dư nợ vay ký quỹ: phần vốn thực của nhà đầu tư. CK không được phép ký quỹ không tính vào",
           "basis": "Giáo trình Môi giới & tư vấn đầu tư CK (UBCKNN/SRTC) – Giao dịch ký quỹ; khoản 6 Điều 9 TT 120/2020/TT-BTC (VBHN 08/VBHN-BTC năm 2026): CK không được giao dịch ký quỹ không tính vào tài sản bảo đảm"},
 "MG-39": {"front": "Tỷ lệ ký quỹ (thực tế) trên TK ký quỹ = ? Khi nào CTCK gọi ký quỹ bổ sung?",
           "back": "Tài sản thực có / Tổng tài sản trên TK ký quỹ. Thấp hơn tỷ lệ ký quỹ duy trì trong hợp đồng: CTCK gọi ký quỹ bổ sung; nhà đầu tư không bổ sung thì CTCK được bán CK là tài sản bảo đảm",
           "basis": "Khoản 6 Điều 9 TT 120/2020/TT-BTC (VBHN 08/VBHN-BTC năm 2026); Giáo trình Môi giới & tư vấn đầu tư CK (UBCKNN/SRTC) – Giao dịch ký quỹ (công thức tỷ lệ ký quỹ)"},
 "MG-40": {"front": "TK ký quỹ chỉ có một mã cổ phiếu, không có tiền: giá cổ phiếu làm phát sinh lệnh gọi ký quỹ = ?",
           "back": "P* = Dư nợ / [Số cổ phiếu × (1 − Tỷ lệ ký quỹ duy trì)], suy từ (Giá trị CK − Dư nợ) / Giá trị CK = Tỷ lệ ký quỹ duy trì"},
 "MG-42": {"front": "Công thức tổng quát (theo giáo trình) giá tham chiếu điều chỉnh tại ngày giao dịch không hưởng quyền?"},
 "MG-47": {"back": "Là khoản vay tiền ngắn hạn có bảo đảm bằng trái phiếu. Lượt về = Lượt đi × (1 + r × n / 365); r: lãi suất repo năm, n: số ngày thực tế của kỳ repo (lãi đơn, quy ước 365 ngày như bài tập)",
           "basis": "Giáo trình Môi giới & tư vấn đầu tư CK (UBCKNN/SRTC) – Giao dịch mua bán lại; điểm b khoản 1 Điều 13, Điều 19 TT 30/2019/TT-BTC (lãi tính theo ngày thực tế; cách tính cụ thể theo quy chế SGDCK)"},
 "PS-07": {"front": "Thành viên giao dịch đặc biệt trên thị trường CKPS là ai, được giao dịch gì?",
           "back": "Ngân hàng thương mại, chi nhánh ngân hàng nước ngoài được SGDCK chấp thuận; chỉ được đầu tư CKPS có tài sản cơ sở là trái phiếu Chính phủ cho chính mình",
           "basis": "Khoản 8 Điều 3; điểm a khoản 2 Điều 25 " + VBHN16},
 "PS-14": {"front": "Ký quỹ ban đầu và ký quỹ duy trì của vị thế hợp đồng tương lai",
           "back": "Ban đầu: mức phải nộp khi mở vị thế. Duy trì: mức tối thiểu phải giữ; tài sản ký quỹ xuống dưới mức này thì bị gọi bổ sung ký quỹ; không bổ sung đủ, kịp thời thì thành viên bù trừ được đóng vị thế bắt buộc",
           "basis": "Giáo trình Chứng khoán phái sinh và TTCK phái sinh (UBCKNN/SRTC) – Ký quỹ ban đầu, ký quỹ duy trì; khoản 3 Điều 34, điểm b khoản 1 Điều 31 " + VBHN16},
 "PS-15": {"front": "Mô hình giáo trình (gọi ký quỹ khi số dư ký quỹ < ký quỹ duy trì): vị thế HĐTL mở ở giá F0 bị gọi ký quỹ khi giá thanh toán vượt ngưỡng nào?"},
 "PS-21": {"back": "Quy ước giáo trình: Basis = Giá giao ngay − Giá tương lai (S − F); có tài liệu dùng F − S. Gần đáo hạn F hội tụ về S nên basis tiến về 0; biến động không lường trước của basis là rủi ro cơ sở"},
 "PS-22": {"back": "Contango: giá tương lai cao hơn giá giao ngay (F > S; basis âm theo quy ước S − F), thường khi chi phí lưu giữ lớn hơn thu nhập từ tài sản. Backwardation: F < S (basis dương)"},
 "PS-41": {"front": "Thành viên giao dịch CKPS chỉ được thực hiện lệnh của nhà đầu tư khi nào?",
           "back": "Sau khi bảo đảm nhà đầu tư đã có tài khoản giao dịch, tài khoản ký quỹ và đã ký quỹ đầy đủ theo yêu cầu của thành viên bù trừ",
           "basis": "Điểm a khoản 1 Điều 25 " + VBHN16},
 "PS-45": {"back": "Trực tiếp: chỉ bù trừ, thanh toán giao dịch CKPS của chính mình hoặc của mình và khách hàng của mình. Chung: thêm dịch vụ cho thành viên không bù trừ và khách hàng của họ (qua hợp đồng ủy thác bù trừ, thanh toán)",
           "basis": "Khoản 11, 12, 13, 15 Điều 3 " + VBHN16},
}
enc = lambda s: json.dumps(s, ensure_ascii=False)
for sj in ["CB", "MG", "PS"]:
    p = D / f"{sj}.json"; txt = p.read_text(encoding="utf-8"); cards = {c["id"]: c for c in json.loads(txt)}
    for cid, ch in CH.items():
        if not cid.startswith(sj): continue
        start = txt.index(enc(cid)); end = txt.index("}", start)  # values contain no '}'
        seg = txt[start:end]
        for k, v in ch.items():
            old = enc(cards[cid][k]); assert seg.count(old) == 1, (cid, k)
            assert len(v) <= (160 if k == "front" else 220 if k == "back" else 10**6), (cid, k, len(v))
            seg = seg.replace(old, enc(v))
        txt = txt[:start] + seg + txt[end:]
    new = json.loads(txt); assert [c["id"] for c in new] == list(cards)  # ids and order kept
    p.write_text(txt, encoding="utf-8")
print("applied", len(CH), "cards")
