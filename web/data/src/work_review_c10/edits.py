"""Second-pass review edits for cm_10.json / cm_11.json. Reads the *.orig.json backups, writes ../cm_10.json, ../cm_11.json."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GT = "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC)"
TT120 = "Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC/2026)"

E = {}

# ---------- cm_10 ----------
E["C10-002"] = dict(o={3: "Công cụ tài chính dạng hợp đồng, xác nhận quyền, nghĩa vụ thanh toán tiền, chuyển giao tài sản cơ sở theo giá xác định cho tương lai"})

E["C10-004"] = dict(
    q="Ông H yêu cầu mọi việc phải làm đúng quy trình, thủ tục; trước khi quyết định, ông muốn có đầy đủ thông tin chi tiết, chính xác bằng văn bản và cần thời gian cân nhắc. Cách làm việc phù hợp nhất của nhân viên môi giới với ông H là:",
    o=["Trình bày ngắn gọn vài điểm chính rồi đề nghị ông H quyết định ngay trong buổi gặp",
       "Chuẩn bị tài liệu đầy đủ, chính xác, làm đúng thủ tục và để ông H có thời gian cân nhắc",
       "Nhấn mạnh rằng nhiều nhà đầu tư quen biết đã mua để ông H yên tâm làm theo số đông",
       "Linh động bỏ qua một số bước thủ tục để rút ngắn thời gian mở tài khoản cho ông H"],
    a=1,
    e="Cách ứng xử phải xuất phát từ hành vi của khách hàng: ông H coi trọng quy trình, thủ tục, cần thông tin chi tiết, chính xác và cần thời gian tự đánh giá (bài giảng xếp kiểu khách hàng này vào nhóm “quan liêu”). Vì vậy nhân viên môi giới nên chuẩn bị tài liệu đầy đủ, số liệu có nguồn rõ ràng, làm đúng thủ tục và không gây áp lực thời gian. Thúc ép quyết định ngay hay dựa vào hiệu ứng đám đông không hợp với cách ra quyết định của ông H; bỏ qua thủ tục vừa làm mất lòng tin của khách hàng, vừa vi phạm quy trình mở tài khoản của công ty.",
    basis=GT + " – Ứng xử với khách hàng theo phong cách hành vi (khách hàng coi trọng quy trình, thủ tục, thông tin chi tiết)")

E["C10-005"] = dict(
    q="Một khách hàng thích chi phối cuộc trao đổi, muốn áp đặt quan điểm của mình, ra quyết định nhanh và thiếu kiên nhẫn khi nghe giải thích dài dòng. Cách ứng xử phù hợp nhất của nhân viên môi giới là:",
    o=["Im lặng, nhượng bộ mọi ý kiến và làm đúng theo ý khách hàng để tránh làm khách hàng phật ý",
       "Tranh luận trực diện đến cùng để khách hàng thấy rõ chuyên môn và vị thế của nhân viên môi giới",
       "Tôn trọng, lắng nghe nhưng tự tin nêu quan điểm có căn cứ, trình bày ngắn gọn, đi thẳng vào vấn đề",
       "Gửi thật nhiều tài liệu chi tiết rồi để khách hàng tự nghiên cứu trong một thời gian dài"],
    a=2,
    e="Khách hàng được mô tả muốn kiểm soát cuộc trao đổi, quyết định nhanh và không thích nghe dài (bài giảng gọi là nhóm “độc tài”). Nhượng bộ hoàn toàn làm nhân viên môi giới mất vai trò tư vấn; tranh luận đối đầu dễ làm đổ vỡ quan hệ. Cách phù hợp là khẳng định một cách thân thiện: tôn trọng, lắng nghe nhưng tự tin nêu quan điểm có căn cứ, trình bày ngắn gọn, tập trung vào kết quả và để khách hàng thấy mình là người quyết định. Gửi nhiều tài liệu chi tiết và cho thời gian cân nhắc dài hợp với khách hàng coi trọng thủ tục, chi tiết hơn là với khách hàng này.",
    basis=GT + " – Ứng xử với khách hàng theo phong cách hành vi (khách hàng thích chi phối, quyết định nhanh: khẳng định thân thiện)")

E["C10-006"] = dict(o={3: "Song song: hai bên linh hoạt đổi vai trò dẫn dắt, giao tiếp tích cực, hiệu quả"})

E["C10-009"] = dict(
    q="Anh P thường mua bán theo biến động hằng ngày của thị trường, nghe tin là muốn đổi danh mục ngay và lo bỏ lỡ cơ hội hơn là lo thua lỗ; vòng quay tài khoản và tổng phí giao dịch của anh rất cao. Cách tư vấn phù hợp nhất của nhân viên môi giới là:",
    o=["Gửi thêm khuyến nghị lướt sóng mỗi ngày để anh P không bỏ lỡ cơ hội nào trên thị trường",
       "Đề nghị anh P dùng thêm giao dịch ký quỹ để tăng quy mô vốn mỗi lần nắm bắt cơ hội",
       "Chỉ ra chi phí của việc giao dịch dồn dập, cùng anh P lập kế hoạch đầu tư có kỷ luật",
       "Khuyên anh P chuyển toàn bộ vốn sang tiền gửi tiết kiệm để khỏi phải theo dõi thị trường"],
    a=2,
    e="Anh P giao dịch theo cảm hứng, chạy theo biến động ngắn hạn và sợ bỏ lỡ cơ hội (một số tài liệu gọi là nhà đầu tư “tự phát”); hệ quả là vòng quay cao và chi phí giao dịch bào mòn lợi nhuận. Ví dụ, giả sử mỗi vòng mua – bán tốn khoảng 0,4% giá trị (phí hai chiều và thuế), vòng quay 20 lần/năm làm mất khoảng 20 × 0,4% = 8% vốn mỗi năm. Nhân viên môi giới cần giúp khách hàng thấy rõ chi phí và rủi ro đó, rồi cùng khách hàng thống nhất mục tiêu, phân bổ tài sản và nguyên tắc mua bán. Gửi thêm khuyến nghị ngắn hạn hay khuyến khích dùng đòn bẩy chỉ làm tăng phí, rủi ro và tạo xung đột lợi ích (phí môi giới tăng); chuyển toàn bộ sang tiền gửi thì bỏ qua mục tiêu và nhu cầu đầu tư của khách hàng.",
    basis=GT + " – Tìm hiểu tâm lý, hành vi của nhà đầu tư cá nhân và cách tư vấn phù hợp (nhà đầu tư giao dịch theo cảm hứng, vòng quay cao)")

E["C10-010"] = dict(o={3: "Mục tiêu, ràng buộc đầu tư xác định rõ theo chức năng, điều lệ và quy định áp dụng"})

E["C10-011"] = dict(o={0: "Công khai mối quan hệ, cơ chế hoa hồng và chỉ giới thiệu khi sản phẩm phù hợp với khách hàng",
                       1: "Ưu tiên giới thiệu sản phẩm cùng tập đoàn cho mọi khách hàng vì nhân viên hiểu rõ hơn",
                       3: "Chỉ giới thiệu sản phẩm cùng tập đoàn cho những khách hàng có khẩu vị rủi ro cao"})

E["C10-012"] = dict(e="Khoản 2 Điều 14 TT 121/2020 (sửa đổi bởi khoản 1 Điều 10 TT 08/2026/TT-BTC): công ty chứng khoán có nghĩa vụ cập nhật các thông tin thay đổi của khách hàng khi khách hàng hoặc tổ chức kinh doanh chứng khoán nước ngoài đại diện có yêu cầu (bản gốc năm 2020 chỉ ghi “khi khách hàng có yêu cầu”). Khoản 7 Điều 89 Luật Chứng khoán cũng yêu cầu CTCK cập nhật, lưu giữ đầy đủ hồ sơ thông tin khách hàng; còn khách hàng chịu trách nhiệm cung cấp đầy đủ, chính xác thông tin nhận biết khách hàng khi mở tài khoản (khoản 1 Điều 15 TT 121/2020, sửa đổi bởi Điều 11 TT 08/2026). Thông tư không gắn nghĩa vụ này với yêu cầu của UBCKNN, thông báo của VSDC hay giá trị giao dịch.")

# ---------- cm_11 ----------
E["C11-001"] = dict(
    q="Đặc điểm nào sau đây mô tả đúng giao dịch ký quỹ (giao dịch bảo chứng) mua chứng khoán tại công ty chứng khoán?",
    o=["Công ty cho vay toàn bộ tiền mua, nhà đầu tư không phải góp phần vốn tự có nào",
       "Lệnh mua chỉ được thực hiện trong phạm vi số tiền nhà đầu tư đã có sẵn trên tài khoản",
       "Nhà đầu tư được vay tiền mua và được tự do rút chứng khoán ra khi vẫn còn dư nợ",
       "Nhà đầu tư vay một phần tiền mua, chứng khoán mua được làm tài sản bảo đảm khoản vay"],
    a=3,
    e="Khoản 10 Điều 2 TT 120/2020: giao dịch ký quỹ là giao dịch mua chứng khoán có sử dụng tiền vay của công ty chứng khoán, trong đó chứng khoán có được từ giao dịch này và các chứng khoán khác được giao dịch ký quỹ của nhà đầu tư được dùng làm tài sản bảo đảm cho khoản vay. Nhà đầu tư góp phần vốn tự có theo tỷ lệ ký quỹ ban đầu trong hợp đồng, phần còn lại vay công ty; vì chứng khoán là tài sản bảo đảm nên không được tự do rút, chuyển khi còn dư nợ. Khoản tiền vay (cộng lãi cộng dồn) là dư nợ; giá trị chứng khoán thực có = giá trị thị trường hiện hành − dư nợ. Giao dịch chỉ trong phạm vi tiền có sẵn là tài khoản giao dịch thông thường; vay toàn bộ thì không còn phần ký quỹ của nhà đầu tư.",
    basis="Khoản 10 Điều 2 " + TT120 + "; điểm b khoản 1 Điều 86 Luật Chứng khoán 2019 (dịch vụ cho khách hàng vay tiền mua chứng khoán); " + GT + " – Khái niệm giao dịch ký quỹ (bảo chứng), dư nợ",
    src="TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt")

E["C11-002"] = dict(o={0: "Tăng sức mua của nhà đầu tư, qua đó tăng cầu và tính thanh khoản cho thị trường",
                       1: "Giảm tỷ lệ lỗ tính trên vốn tự có của nhà đầu tư khi giá chứng khoán giảm",
                       2: "Chuyển rủi ro giảm giá của chứng khoán ký quỹ sang công ty chứng khoán cho vay"})

E["C11-003"] = dict(
    e="Với đòn bẩy, bỏ qua lãi vay, tỷ lệ lỗ trên vốn tự có = tỷ lệ giảm giá/tỷ lệ ký quỹ ban đầu. Ví dụ, giả sử ký quỹ 50% (mua 100 triệu đồng, tự có 50, vay 50) và giá giảm 60%: chứng khoán còn 40 triệu đồng, không đủ trả 50 triệu đồng nợ ⇒ lỗ 60 triệu đồng = 120% vốn tự có. Nếu giá giảm sâu, liên tục (giảm sàn nhiều phiên, thiếu thanh khoản) trước khi kịp bán giải chấp, tiền bán chứng khoán không đủ trả nợ: khách hàng mất hết vốn mà vẫn còn nợ công ty. Hợp đồng giao dịch ký quỹ phải nêu rõ các rủi ro, thiệt hại có thể phát sinh và chi phí khách hàng phải trả; khi tỷ lệ ký quỹ thấp hơn tỷ lệ duy trì, công ty gọi ký quỹ bổ sung, khách hàng không bổ sung thì công ty có quyền bán chứng khoán bảo đảm theo hợp đồng mà không chờ giá phục hồi (khoản 1, 6 Điều 9 TT 120/2020). Lãi vay tính trên dư nợ theo thời gian vay, không phụ thuộc giá tăng hay giảm.",
    basis="Khoản 1, khoản 6 Điều 9 " + TT120 + "; " + GT + " – Rủi ro của giao dịch ký quỹ cần giải thích cho khách hàng (lỗ vượt vốn ký quỹ, gọi ký quỹ, bán giải chấp)",
    src="TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt")

E["C11-004"] = dict(
    o=["Tỷ lệ ký quỹ, lãi suất vay, thời hạn vay và mức lợi nhuận tối thiểu cam kết cho khách hàng vay",
       "Tỷ lệ ký quỹ, lãi suất vay, thời hạn vay, danh sách khách hàng đang vay và dư nợ của từng người",
       "Tỷ lệ ký quỹ, lãi suất vay, thời hạn vay, phương thức gọi ký quỹ bổ sung, danh mục chứng khoán ký quỹ",
       "Lãi suất vay, thời hạn vay, phương thức gọi ký quỹ bổ sung và cam kết mua lại chứng khoán khi giá giảm"],
    e="Khoản 3 Điều 123 Luật Chứng khoán: trường hợp cung cấp dịch vụ giao dịch ký quỹ, công ty chứng khoán phải thông báo điều kiện cung cấp dịch vụ gồm yêu cầu về tỷ lệ ký quỹ, lãi suất vay, thời hạn vay, phương thức thực hiện lệnh gọi ký quỹ bổ sung, danh mục chứng khoán thực hiện giao dịch ký quỹ. Danh mục này do công ty lựa chọn trên cơ sở danh sách Sở giao dịch chứng khoán công bố (khoản 5 Điều 9 TT 120/2020), nên khách hàng chỉ ký quỹ hoặc bổ sung ký quỹ bằng chứng khoán thuộc danh mục công ty chấp nhận. Công ty không được cam kết lợi nhuận hay cam kết mua lại chứng khoán cho khách hàng, và phải bảo mật thông tin tài khoản của khách hàng khác.",
    basis="Khoản 3 Điều 123 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH/2025); khoản 5 Điều 9 " + TT120)

E["C11-005"] = dict(
    o=["Gọi ban đầu phát sinh khi tỷ lệ thực tế giảm dưới tỷ lệ duy trì; gọi duy trì yêu cầu nộp đủ vốn tự có theo tỷ lệ ký quỹ ban đầu khi mua",
       "Gọi ban đầu chỉ áp dụng cho vị thế bán khống; gọi duy trì chỉ áp dụng cho vị thế mua chứng khoán bằng tiền vay công ty chứng khoán",
       "Gọi ban đầu yêu cầu nộp đủ vốn tự có theo tỷ lệ ký quỹ ban đầu khi mua; gọi duy trì phát sinh khi tỷ lệ thực tế giảm dưới tỷ lệ duy trì",
       "Gọi ban đầu do Sở giao dịch chứng khoán gửi trực tiếp cho nhà đầu tư; gọi duy trì do công ty chứng khoán gửi cho khách hàng của mình"],
    e="Lệnh gọi ký quỹ ban đầu: khi khách hàng mua chứng khoán trên tài khoản ký quỹ, công ty yêu cầu nộp phần vốn tự có tối thiểu theo tỷ lệ ký quỹ ban đầu trong hợp đồng (ví dụ, giả sử tỷ lệ ban đầu 50% thì mua 100 triệu đồng phải có 50 triệu đồng). Lệnh gọi ký quỹ duy trì (bổ sung): sau khi mua, nếu giá giảm làm tỷ lệ ký quỹ thực tế = (giá trị chứng khoán − dư nợ)/giá trị chứng khoán thấp hơn tỷ lệ duy trì, công ty yêu cầu bổ sung tiền, chứng khoán hoặc bán bớt chứng khoán. Khoản 6 Điều 9 TT 120/2020: nhà đầu tư phải bảo đảm tỷ lệ ký quỹ ban đầu, tỷ lệ ký quỹ duy trì theo hợp đồng; khi tỷ lệ ký quỹ thấp hơn tỷ lệ duy trì, công ty chứng khoán phát hành lệnh gọi ký quỹ bổ sung. Cả hai đều do công ty chứng khoán (bên cho vay) thực hiện với khách hàng và về nguyên tắc áp dụng cho cả vị thế mua ký quỹ lẫn bán khống (nơi được phép).",
    basis="Khoản 6 Điều 9 " + TT120 + "; " + GT + " – Các loại lệnh gọi ký quỹ: gọi ký quỹ ban đầu và gọi ký quỹ duy trì",
    src="TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt")

E["C11-006"] = dict(
    o={0: "Bảo đảm nhà đầu tư không bao giờ lỗ quá một tỷ lệ nhất định trên vốn tự có ban đầu",
       1: "Bảo vệ công ty cho vay trước rủi ro giá trị tài sản bảo đảm không đủ để thu hồi nợ"},
    basis="Khoản 6 Điều 9 " + TT120 + "; " + GT + " – Mục đích của ký quỹ duy trì và gọi ký quỹ duy trì",
    src="TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt")

E["C11-007"] = dict(
    q="Ngày giao dịch thứ nhất, khách hàng mua 2.000 cổ phiếu K giá 30.000 đồng trên tài khoản giao dịch ký quỹ, dùng 42.000.000 đồng vốn tự có, phần còn lại vay công ty chứng khoán. Giá đóng cửa của K vào ngày giao dịch thứ nhất, thứ hai và thứ ba lần lượt là 31.500; 29.000 và 27.500 đồng. Giả sử: tài khoản chỉ có số cổ phiếu K và khoản vay này, trong ba ngày khách hàng chưa nộp, rút tiền hay mua bán thêm; giá trị thị trường hiện hành của chứng khoán trong mỗi ngày tính theo giá đóng cửa của ngày giao dịch liền trước; giá trị chứng khoán thực có = giá trị thị trường hiện hành − dư nợ; bỏ qua lãi vay và phí. Giá trị chứng khoán thực có trên tài khoản vào ngày giao dịch thứ ba là",
    o=["37.000.000 đồng", "45.000.000 đồng", "42.000.000 đồng", "40.000.000 đồng"],
    a=3,
    e="Dư nợ = 2.000 × 30.000 − 42.000.000 = 60.000.000 − 42.000.000 = 18.000.000 đồng (không đổi vì bỏ qua lãi). Ngày thứ ba dùng giá đóng cửa ngày thứ hai: giá trị thị trường hiện hành = 2.000 × 29.000 = 58.000.000 đồng ⇒ giá trị chứng khoán thực có = 58.000.000 − 18.000.000 = 40.000.000 đồng. Lỗi thường gặp: dùng giá đóng cửa của chính ngày thứ ba (2.000 × 27.500 − 18.000.000 = 37.000.000), dùng giá đóng cửa ngày thứ nhất – tức kết quả của ngày thứ hai (2.000 × 31.500 − 18.000.000 = 45.000.000), dùng giá mua (60.000.000 − 18.000.000 = 42.000.000).",
    basis=GT + " – Giá trị thị trường hiện hành, dư nợ và giá trị chứng khoán thực có trên tài khoản ký quỹ (quy ước định giá nêu trong đề)")

E["C11-008"] = dict(
    q="Công ty chứng khoán trả cho nhân viên môi giới lương cố định 6,3 triệu đồng/tháng (12 tháng/năm). Một năm có 252 ngày làm việc; mỗi ngày nhân viên dự kiến thực hiện 120 cuộc điện thoại tìm kiếm khách hàng (bỏ qua cước điện thoại). Giả sử toàn bộ chi phí lương trong năm được phân bổ đều cho các cuộc gọi này, giá trị (chi phí lương) của một cuộc gọi tìm kiếm khách hàng là")

E["C11-008"]["e"] = "Lương năm = 6,3 triệu × 12 = 75.600.000 đồng; số cuộc gọi/năm = 252 × 120 = 30.240 ⇒ giá trị một cuộc gọi = 75.600.000/30.240 = 2.500 đồng. Con số này giúp nhân viên môi giới ý thức chi phí thời gian, sàng lọc danh sách gọi và đo hiệu quả tìm kiếm khách hàng. Lỗi thường gặp: chia cho 365 ngày lịch (75.600.000/43.800 ≈ 1.726), lấy lương một tháng chia số cuộc gọi cả năm (6.300.000/30.240 ≈ 208), nhầm sang chi phí lương một ngày (75.600.000/252 = 300.000)."

FILES = {"cm_10.json": "cm_10.orig.json", "cm_11.json": "cm_11.orig.json"}
used = set()
for out, orig in FILES.items():
    qs = json.loads((HERE / orig).read_text(encoding="utf-8"))
    for q in qs:
        ch = E.get(q["id"])
        if not ch:
            continue
        used.add(q["id"])
        for k, v in ch.items():
            if k == "o" and isinstance(v, dict):
                for i, s in v.items():
                    q["o"][i] = s
            else:
                q[k] = v
    (HERE.parent / out).write_text(json.dumps(qs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
assert used == set(E), set(E) - used
print("edited:", sorted(used))
