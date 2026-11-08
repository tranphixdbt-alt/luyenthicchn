"""Dựng luat_3.json (chuyên đề 4 Giao dịch CK & 6 Đăng ký, lưu ký, bù trừ, thanh toán) và tự kiểm.
Chạy: python3 -I build_l3.py  -> ghi work_l3/luat_3.json (chưa chép sang src)."""
import json, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parents[2].parent / "tai_lieu_phap_ly" / "van_ban_txt"
LUAT = "VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt"
ND155 = "ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt"
ND245 = "ND_245_2025_ND-CP_Cong_bao_so_1403-1408_2025.txt"
TT119 = "TT_119_2020_TT-BTC_hop_nhat_VBHN_45_VBHN-BTC_2025.txt"
TT120 = "TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt"
GD, LK = "Giao dịch chứng khoán", "Đăng ký, lưu ký, bù trừ & thanh toán"
V120 = "Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC năm 2026)"
V119 = "Thông tư 119/2020/TT-BTC (VBHN 45/VBHN-BTC năm 2025)"

# (topic, level, q, options, a, e, basis, quote, src)
ITEMS = [
# ---------------- Chuyên đề 4: giao dịch ----------------
(GD, 1, "Theo Thông tư 120/2020/TT-BTC, trong điều kiện thị trường bình thường, biên độ dao động giá chứng khoán do chủ thể nào quyết định?",
 ["Sở giao dịch chứng khoán Việt Nam quyết định, sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận",
  "Ủy ban Chứng khoán Nhà nước quyết định, Sở giao dịch chứng khoán Việt Nam chỉ công bố thông tin",
  "Bộ trưởng Bộ Tài chính quyết định theo đề nghị của Chủ tịch Ủy ban Chứng khoán Nhà nước",
  "Từng Sở giao dịch chứng khoán Hà Nội, TP. Hồ Chí Minh tự quyết định cho thị trường của mình"], 0,
 "Khoản 1 Điều 4: SGDCK Việt Nam quyết định biên độ dao động giá sau khi được UBCKNN chấp thuận. Chỉ khi cần thiết để ổn định thị trường, UBCKNN mới quyết định điều chỉnh biên độ và công bố trên cổng thông tin điện tử của UBCKNN (khoản 2 Điều 4). Con số biên độ cụ thể nằm trong quy chế của Sở nên có thể thay đổi.",
 f"Khoản 1, 2 Điều 4 {V120}",
 "Sở giao dịch chứng khoán Việt Nam quyết định biên độ dao động giá sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận.", TT120),

(GD, 1, "Theo Thông tư 120/2020/TT-BTC, căn cứ điều kiện thực tiễn của thị trường, chủ thể nào quyết định áp dụng cơ chế ngắt mạch thị trường hoặc ngắt mạch thị trường kết hợp với biên độ dao động giá?",
 ["Sở giao dịch chứng khoán Việt Nam", "Ủy ban Chứng khoán Nhà nước", "Bộ trưởng Bộ Tài chính", "Thủ tướng Chính phủ"], 1,
 "Điều 5: SGDCK Việt Nam quyết định cơ chế ngắt mạch (cách thức vận hành) sau khi UBCKNN chấp thuận; còn việc áp dụng ngắt mạch, hoặc ngắt mạch kết hợp biên độ dao động giá, do UBCKNN quyết định căn cứ điều kiện thực tiễn. Ngắt mạch là cơ chế tạm dừng giao dịch tự động trong phiên khi giá hoặc chỉ số chạm ngưỡng xác định (khoản 2 Điều 2).",
 f"Khoản 2 Điều 5 {V120}",
 "Căn cứ điều kiện thực tiễn của thị trường, Ủy ban Chứng khoán Nhà nước quyết định áp dụng cơ chế ngắt mạch thị trường hoặc cơ chế ngắt mạch thị trường kết hợp với biên độ dao động giá.", TT120),

(GD, 2, "Theo Thông tư 120/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), nhà đầu tư nước ngoài không cư trú được đặt lệnh giao dịch chứng khoán theo cách nào?",
 ["Chỉ qua ngân hàng lưu ký nơi mở tài khoản, dùng số hiệu tài khoản tiền gửi thanh toán của chính nhà đầu tư",
  "Chỉ qua văn phòng đại diện tại Việt Nam của tổ chức kinh doanh chứng khoán nước ngoài đã được cấp phép",
  "Tự đặt bằng tài khoản giao dịch của mình, hoặc qua tổ chức KDCK nước ngoài đại diện bằng số hiệu tài khoản lưu ký",
  "Qua bất kỳ cá nhân được ủy quyền bằng lời nói, sử dụng tài khoản giao dịch của chính người được ủy quyền"], 2,
 "Điểm a khoản 1 Điều 6 (sửa đổi bởi khoản 1 Điều 4 TT 08/2026, hiệu lực 03/02/2026): nhà đầu tư nước ngoài không cư trú đặt lệnh thông qua tổ chức kinh doanh chứng khoán nước ngoài đại diện bằng số hiệu tài khoản lưu ký của nhà đầu tư, hoặc tự đặt bằng tài khoản giao dịch của mình. CTCK phải ký hợp đồng với tổ chức đại diện và nhận biết cả nhà đầu tư lẫn tổ chức đại diện (Điều 15a TT 121/2020).",
 f"Điểm a khoản 1 Điều 6 {V120} (sửa đổi bởi khoản 1 Điều 4 Thông tư 08/2026/TT-BTC)",
 "đối với nhà đầu tư nước ngoài không cư trú, việc đặt lệnh giao dịch chứng khoán được thực hiện thông qua tổ chức kinh doanh chứng khoán nước ngoài đại diện bằng số hiệu tài khoản lưu ký của nhà đầu tư nước ngoài", TT120),

(GD, 3, "Công ty chứng khoán nước ngoài F mở tại công ty chứng khoán V một tài khoản giao dịch để quản lý giao dịch cho khách hàng của F. Trong cùng một đợt khớp lệnh định kỳ, F đặt lệnh mua cổ phiếu X cho khách hàng P và lệnh bán cổ phiếu X cho khách hàng Q (P, Q là hai nhà đầu tư nước ngoài khác nhau). Theo Thông tư 120/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), việc đặt lệnh này:",
 ["Không được, vì mọi tài khoản đều bị cấm cùng mua, cùng bán một mã trong một đợt khớp lệnh định kỳ",
  "Được, vì lệnh mua và lệnh bán không phải của cùng một nhà đầu tư nước ngoài",
  "Chỉ được trong khớp lệnh liên tục, không được trong đợt khớp lệnh định kỳ",
  "Chỉ được khi F mở thêm tại V một tài khoản giao dịch riêng cho từng khách hàng"], 1,
 "Khoản 7 Điều 6: CTCK nước ngoài, CTQLQ nước ngoài được mở 02 tài khoản giao dịch tại mỗi CTCK (01 cho chính công ty, 01 để quản lý giao dịch của khách hàng). Khoản 6 Điều 7 (sửa đổi bởi TT 08/2026) cho phép dùng tài khoản khách hàng để vừa mua vừa bán cùng một mã trong từng đợt khớp lệnh (định kỳ hoặc liên tục) hoặc giao dịch thỏa thuận, miễn lệnh mua và lệnh bán không của cùng một nhà đầu tư nước ngoài.",
 f"Khoản 7 Điều 6, khoản 6 Điều 7 {V120} (sửa đổi bởi khoản 3 Điều 4, khoản 3 Điều 5 Thông tư 08/2026/TT-BTC)",
 "để đặt lệnh vừa mua vừa bán cùng một mã chứng khoán trong từng đợt khớp lệnh (định kỳ hoặc liên tục) hoặc giao dịch thỏa thuận, nhưng phải đảm bảo nguyên tắc lệnh mua và lệnh bán chứng khoán không phải của cùng một nhà đầu tư nước ngoài.", TT120),

(GD, 3, "Trong phiên khớp lệnh liên tục buổi sáng, nhà đầu tư H đặt lệnh giới hạn mua 1.000 cổ phiếu X; lệnh chưa khớp và vẫn còn hiệu lực. Trong đợt khớp lệnh định kỳ đóng cửa cùng ngày, H muốn đặt lệnh bán 500 cổ phiếu X đang có sẵn trên tài khoản. Theo Thông tư 120/2020/TT-BTC, H:",
 ["Không được đặt, phải hủy lệnh mua còn hiệu lực trước khi đặt lệnh bán trong đợt định kỳ",
  "Không được đặt, vì nhà đầu tư không được bán một mã chứng khoán trong ngày đã đặt lệnh mua mã đó",
  "Chỉ được đặt nếu lệnh bán có mức giá cao hơn mức giá của lệnh mua đang chờ khớp",
  "Được đặt, vì lệnh mua nhập từ đợt trước, chưa khớp, còn hiệu lực không thuộc phạm vi bị cấm"], 3,
 "Khoản 4 Điều 7: nhà đầu tư không được đặt các lệnh cùng mua, cùng bán đồng thời một mã trong cùng một đợt khớp lệnh định kỳ, trừ các lệnh đã nhập vào hệ thống tại đợt giao dịch trước đó, chưa khớp nhưng còn hiệu lực. Lệnh mua của H thuộc trường hợp loại trừ nên H được đặt lệnh bán. CTCK có trách nhiệm kiểm soát việc đặt lệnh này khi nhận và nhập lệnh (khoản 5 Điều 7, sửa đổi bởi TT 08/2026).",
 f"Khoản 4, 5 Điều 7 {V120} (khoản 5 sửa đổi bởi khoản 2 Điều 5 Thông tư 08/2026/TT-BTC)",
 "Nhà đầu tư không được đặt các lệnh giao dịch cùng mua, cùng bán đồng thời cùng một mã chứng khoán trong cùng một đợt khớp lệnh định kỳ, trừ các lệnh đã được nhập vào hệ thống giao dịch chứng khoán tại đợt giao dịch trước đó, chưa được khớp nhưng vẫn còn hiệu lực.", TT120),

(GD, 2, "Theo Thông tư 120/2020/TT-BTC, nhà đầu tư chỉ được đặt lệnh bán chứng khoán đã có sẵn trên tài khoản lưu ký tại ngày giao dịch. Các trường hợp sau là ngoại lệ, NGOẠI TRỪ:",
 ["Thành viên lập quỹ ETF bán chứng chỉ quỹ ETF khi bảo đảm đủ để chuyển giao trước thời hạn thanh toán",
  "Giao dịch trong ngày theo hợp đồng giao dịch trong ngày đã ký với công ty chứng khoán",
  "Bán chứng khoán chờ về, khi hoạt động này được Ủy ban Chứng khoán Nhà nước triển khai",
  "Bán trước số cổ phiếu thưởng đã chốt danh sách nhưng chưa được phân bổ vào tài khoản"], 3,
 "Khoản 3 Điều 7 chỉ cho phép ba ngoại lệ: thành viên lập quỹ ETF bán chứng chỉ quỹ/chứng khoán cơ cấu khi bảo đảm đủ để chuyển giao trước thời hạn thanh toán; giao dịch trong ngày (Điều 10); bán chứng khoán chờ về (do UBCKNN triển khai tùy tình hình thị trường). Chứng khoán chờ về là chứng khoán đã mua trên hệ thống tại các ngày trước đó, đang hoàn tất chuyển quyền sở hữu (khoản 12 Điều 2) – cổ phiếu thưởng chưa phân bổ không thuộc khái niệm này.",
 f"Khoản 3 Điều 7, khoản 12 Điều 2 {V120}",
 "giao dịch trong ngày theo quy định tại Điều 10 Thông tư này; bán chứng khoán chờ về.", TT120),

(GD, 2, "Theo Thông tư 120/2020/TT-BTC (sửa đổi bởi Thông tư 68/2024/TT-BTC), trong thời gian chưa triển khai cơ chế đối tác bù trừ trung tâm, ngoài giao dịch ký quỹ, trường hợp nào được đặt lệnh mua cổ phiếu mà không yêu cầu có đủ tiền khi đặt lệnh?",
 ["Nhà đầu tư cá nhân nước ngoài mở tài khoản lưu ký tại ngân hàng lưu ký",
  "Nhà đầu tư chứng khoán chuyên nghiệp là tổ chức thành lập theo pháp luật Việt Nam",
  "Quỹ đầu tư chứng khoán trong nước do công ty quản lý quỹ quản lý",
  "Nhà đầu tư nước ngoài là tổ chức, theo đánh giá rủi ro thanh toán của công ty chứng khoán"], 3,
 "Điểm a khoản 1 Điều 7 (sửa đổi bởi TT 68/2024, hiệu lực 02/11/2024): nhà đầu tư phải có đủ tiền khi đặt lệnh mua, trừ giao dịch ký quỹ và nhà đầu tư nước ngoài là tổ chức mua cổ phiếu không yêu cầu có đủ tiền (non-prefunding) theo Điều 9a. CTCK đánh giá rủi ro thanh toán của tổ chức này để xác định mức tiền phải có khi đặt lệnh (khoản 1 Điều 9a). Câu \"mua phải có đủ tiền\" không kèm ngoại lệ này là quy định cũ.",
 f"Điểm a khoản 1 Điều 7, khoản 1 Điều 9a {V120} (sửa đổi, bổ sung bởi khoản 1, 2 Điều 1 Thông tư 68/2024/TT-BTC)",
 "Tổ chức thành lập theo pháp luật nước ngoài tham gia đầu tư trên thị trường chứng khoán Việt Nam (sau đây gọi là nhà đầu tư nước ngoài là tổ chức) mua cổ phiếu không yêu cầu có đủ tiền khi đặt lệnh theo quy định tại Điều 9a Thông tư này.", TT120),

(GD, 3, "Trong vòng 30 ngày giao dịch liên tục, quỹ nước ngoài F (nhà đầu tư nước ngoài là tổ chức) phát sinh vi phạm nghĩa vụ thanh toán lần thứ ba đối với giao dịch mua cổ phiếu không yêu cầu có đủ tiền khi đặt lệnh. Theo Thông tư 120/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), F không được đặt loại lệnh mua này trong thời hạn:",
 ["07 ngày giao dịch liên tục kể từ ngày liền kề sau ngày vi phạm",
  "30 ngày giao dịch liên tục kể từ ngày liền kề sau ngày vi phạm lần thứ ba",
  "180 ngày liên tục kể từ ngày giao dịch liền kề sau ngày vi phạm lần thứ ba",
  "12 tháng kể từ ngày Tổng công ty lưu ký và bù trừ chứng khoán thông báo vi phạm"], 2,
 "Khoản 1a Điều 9a (bổ sung bởi Điều 6 TT 08/2026): mỗi lần không thanh toán, tổ chức nước ngoài bị cấm đặt lệnh mua không cần đủ tiền 07 ngày giao dịch liên tục; nếu trong 30 ngày giao dịch liên tục vi phạm lần thứ ba thì bị cấm 180 ngày liên tục kể từ ngày giao dịch liền kề sau ngày vi phạm lần thứ ba. SGDCK Việt Nam thông báo cho các CTCK thành viên sau khi nhận thông báo của VSDC; trong thời gian bị cấm, F phải có đủ tiền khi đặt lệnh mua.",
 f"Điểm a, b, c khoản 1a Điều 9a {V120} (bổ sung bởi Điều 6 Thông tư 08/2026/TT-BTC)",
 "nhà đầu tư nước ngoài là tổ chức không được đặt lệnh giao dịch mua cổ phiếu không yêu cầu có đủ tiền khi đặt lệnh trong thời hạn 180 ngày liên tục kể từ ngày giao dịch liền kề sau ngày nhà đầu tư nước ngoài là tổ chức phát sinh vi phạm nghĩa vụ thanh toán lần thứ ba", TT120),

(GD, 3, "Ngày D, công ty chứng khoán S dùng tiền của mình thanh toán thay cho quỹ nước ngoài F khoản mua cổ phiếu không yêu cầu có đủ tiền khi đặt lệnh. F đã xác nhận sẽ thanh toán nhưng đến khi kết thúc phiên giao dịch buổi chiều ngày D+1 vẫn chưa chuyển đủ tiền cho S. Theo Thông tư 119/2020/TT-BTC (sửa đổi bởi Thông tư 18/2025/TT-BTC), S được:",
 ["Đề nghị VSDC chuyển quyền sở hữu số cổ phiếu đã thanh toán thay về tài khoản tự doanh của S trong ngày D+1",
  "Đề nghị VSDC loại bỏ thanh toán giao dịch và yêu cầu F bồi thường 20% giá trị giao dịch cho bên bán",
  "Chuyển số tiền đã thanh toán thay thành khoản cho vay giao dịch ký quỹ của F, tính lãi theo hợp đồng",
  "Đề nghị VSDC dùng quỹ hỗ trợ thanh toán của các thành viên khác bù đắp, F hoàn trả trong 01 ngày"], 0,
 "Khoản 6, 8 Điều 40k: tổ chức nước ngoài phải thanh toán đủ cho CTCK chậm nhất khi kết thúc phiên giao dịch buổi chiều ngày liền kề sau ngày CTCK thanh toán thay; nếu đã xác nhận mà không trả đủ, CTCK được đề nghị VSDC chuyển quyền sở hữu số cổ phiếu (và quyền phát sinh) về tài khoản tự doanh ngay trong ngày liền kề đó (điểm q2 khoản 2 Điều 6), rồi được bán trên hệ thống (khoản 9). Việc CTCK thanh toán thay không phải là cho vay giao dịch ký quỹ (khoản 3 Điều 40k).",
 f"Khoản 3, 6, 8, 9 Điều 40k, điểm q2 khoản 2 Điều 6 {V119} (bổ sung bởi khoản 3, khoản 10 Điều 1 Thông tư 18/2025/TT-BTC)",
 "công ty chứng khoán được đề nghị Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam hoàn tất việc chuyển quyền sở hữu số cổ phiếu được hạch toán trên tài khoản của nhà đầu tư nước ngoài là tổ chức mà công ty chứng khoán đã thanh toán thay", TT119),

(GD, 3, "Công ty đại chúng Z đã báo cáo UBCKNN và công bố thông tin mua lại 2.000.000 cổ phiếu của chính mình qua phương thức khớp lệnh. Giả định ngày giao dịch có giá tham chiếu 40.000 đồng/cổ phiếu và biên độ dao động giá ±7%. Theo Thông tư 120/2020/TT-BTC, giá đặt mua cao nhất và tổng khối lượng đặt mua tối đa của Z trong ngày đó là:",
 ["42.800 đồng; 200.000 cổ phiếu", "41.400 đồng; 60.000 cổ phiếu", "41.400 đồng; 200.000 cổ phiếu", "40.000 đồng; 100.000 cổ phiếu"], 2,
 "Điểm b khoản 1 Điều 8: giá đặt mua ≤ giá tham chiếu + giá tham chiếu × 50% biên độ = 40.000 + 40.000 × 3,5% = 41.400 đồng. Tổng khối lượng đặt mua mỗi ngày tối thiểu 3% và tối đa 10% khối lượng đã đăng ký: tối đa 10% × 2.000.000 = 200.000 cổ phiếu (tối thiểu 60.000; miễn yêu cầu tối thiểu khi khối lượng còn lại dưới 3%). 42.800 là lỗi dùng cả biên độ 7%.",
 f"Điểm b khoản 1 Điều 8 {V120}",
 "Giá đặt mua ≤ Giá tham chiếu + (Giá tham chiếu x 50% Biên độ dao động giá cổ phiếu)", TT120),

(GD, 2, "Theo Thông tư 120/2020/TT-BTC, quy định giá đặt bán không thấp hơn giá tham chiếu trừ 50% biên độ dao động giá và khối lượng đặt bán mỗi ngày từ 3% đến 10% khối lượng đã đăng ký áp dụng cho trường hợp nào?",
 ["Mọi công ty đại chúng bán cổ phiếu quỹ trên hệ thống giao dịch, không phân biệt thời điểm mua lại",
  "Công ty đại chúng bán cổ phiếu quỹ đã mua lại trước ngày 01/01/2021",
  "Cổ đông lớn bán cổ phiếu của công ty đại chúng theo phương thức thỏa thuận",
  "Công ty chứng khoán bán cổ phiếu tự doanh nhận về từ nhà đầu tư nước ngoài không thanh toán"], 1,
 "Khoản 3 Điều 8 chỉ áp dụng giới hạn giá, khối lượng đặt bán cho cổ phiếu quỹ mua lại trước ngày 01/01/2021. Cổ phiếu mua lại từ ngày Luật Chứng khoán 2019 có hiệu lực được bán ra theo khoản 7 Điều 36 Luật Chứng khoán, trên hệ thống theo quy chế của SGDCK Việt Nam hoặc ngoài hệ thống theo pháp luật về đăng ký, lưu ký (khoản 2 Điều 8).",
 f"Khoản 2, 3 Điều 8 {V120}",
 "công ty đại chúng mua lại cổ phiếu của chính mình trước ngày 01/01/2021 bán ra cổ phiếu đã mua lại theo phương thức khớp lệnh hoặc thỏa thuận như sau", TT120),

(GD, 2, "Ông J (quốc tịch Nhật Bản, đã có mã số giao dịch chứng khoán) mở tài khoản giao dịch tại công ty chứng khoán A và muốn vay tiền của A để mua cổ phiếu niêm yết theo hình thức giao dịch ký quỹ. Theo Thông tư 120/2020/TT-BTC:",
 ["Được, nếu cổ phiếu nằm trong danh sách chứng khoán được giao dịch ký quỹ của A",
  "Được, nếu tỷ lệ sở hữu nước ngoài của cổ phiếu đó chưa đạt mức tối đa",
  "Không được, vì nhà đầu tư nước ngoài không được thực hiện giao dịch ký quỹ",
  "Chỉ được nếu ông J là nhà đầu tư chứng khoán chuyên nghiệp theo quy định"], 2,
 "Khoản 2 Điều 9: nhà đầu tư nước ngoài không được thực hiện giao dịch ký quỹ. Với nhà đầu tư trong nước, tại mỗi CTCK chỉ được mở 01 tài khoản giao dịch ký quỹ (khoản 3 Điều 9); chứng khoán ký quỹ là cổ phiếu niêm yết, đăng ký giao dịch, chứng chỉ quỹ niêm yết đáp ứng tiêu chí của UBCKNN (khoản 4 Điều 9).",
 f"Khoản 2 Điều 9 {V120}",
 "Nhà đầu tư nước ngoài không được thực hiện giao dịch ký quỹ.", TT120),

("Tổ chức & hoạt động CTCK", 2, "Theo Nghị định 155/2020/NĐ-CP, để được cung cấp dịch vụ cho khách hàng vay tiền mua chứng khoán (giao dịch ký quỹ), công ty chứng khoán phải đáp ứng điều kiện nào về tỷ lệ vốn khả dụng?",
 ["Trên 150% trong 03 tháng gần nhất tính đến thời điểm báo cáo UBCKNN",
  "Tối thiểu 180% liên tục trong 06 tháng gần nhất tính đến thời điểm nộp hồ sơ",
  "Tối thiểu 220% liên tục trong 06 tháng gần nhất tính đến thời điểm đăng ký",
  "Tối thiểu 260% liên tục trong 12 tháng gần nhất trước tháng nộp hồ sơ"], 1,
 "Điểm d khoản 1 Điều 198: tỷ lệ vốn khả dụng tối thiểu 180% liên tục 06 tháng gần nhất; ngoài ra phải có nghiệp vụ môi giới, không trong tình trạng cảnh báo, kiểm soát, đình chỉ…, nợ/VCSH theo quy định của Bộ Tài chính, có hệ thống và quy trình quản lý rủi ro. Mức \"150% trong 3 tháng\" là quy định cũ; 220% là điều kiện cho vay chứng khoán (Điều 199); 260% là điều kiện cung cấp dịch vụ bù trừ, thanh toán (Điều 151). Nghị định 245/2025 không sửa Điều 198.",
 "Điểm d khoản 1 Điều 198 Nghị định 155/2020/NĐ-CP (không bị Nghị định 245/2025/NĐ-CP sửa đổi)",
 "Tỷ lệ vốn khả dụng đạt tối thiểu 180% liên tục trong 06 tháng gần nhất tính đến thời điểm công ty chứng khoán nộp hồ sơ đăng ký cung cấp dịch vụ cho khách hàng vay tiền mua chứng khoán", ND155),

(GD, 2, "Công ty chứng khoán X không còn đáp ứng điều kiện được cung cấp dịch vụ cho khách hàng vay tiền mua chứng khoán. Theo Thông tư 120/2020/TT-BTC, X phải:",
 ["Thu hồi ngay toàn bộ dư nợ ký quỹ hiện có của khách hàng và báo cáo VSDC trong vòng 24 giờ",
  "Ngừng ký mới trong 30 ngày, vẫn được gia hạn hợp đồng cũ và báo cáo SGDCK trong 05 ngày làm việc",
  "Ngừng ngay ký mới, gia hạn hợp đồng, cho vay ký quỹ; báo cáo UBCKNN bằng văn bản trong 48 giờ",
  "Tiếp tục cho vay khách hàng cũ, ngừng ký mới và báo cáo UBCKNN trong kỳ báo cáo quý gần nhất"], 2,
 "Khoản 7 Điều 9: CTCK không còn đáp ứng điều kiện phải ngừng ngay việc ký mới, gia hạn hợp đồng mở tài khoản giao dịch ký quỹ, ngừng cho vay để giao dịch ký quỹ và báo cáo bằng văn bản cho UBCKNN trong vòng 48 giờ kể từ khi xảy ra sự kiện. Ngoài ra, khi cần thiết để ổn định thị trường, UBCKNN có quyền yêu cầu tạm ngừng giao dịch ký quỹ (khoản 9 Điều 9).",
 f"Khoản 7, 9 Điều 9 {V120}",
 "phải ngừng ngay việc ký mới, gia hạn hợp đồng mở tài khoản giao dịch ký quỹ, ngừng cho vay vốn để thực hiện giao dịch ký quỹ và báo cáo bằng văn bản cho Ủy ban Chứng khoán Nhà nước trong vòng 48 giờ kể từ khi xảy ra sự kiện trên", TT120),

(GD, 2, "Theo Thông tư 120/2020/TT-BTC, nhận định nào sau đây ĐÚNG về giao dịch trong ngày?",
 ["Nhà đầu tư được mở nhiều tài khoản giao dịch trong ngày tại cùng một công ty chứng khoán",
  "Được áp dụng cả với giao dịch chứng khoán lô lẻ và giao dịch thỏa thuận",
  "Không thực hiện trong 05 ngày làm việc trước ngày đăng ký cuối cùng thực hiện quyền của mã đó",
  "Mọi công ty chứng khoán có nghiệp vụ môi giới đều được cung cấp, không cần thêm điều kiện"], 2,
 "Khoản 3 Điều 10: không thực hiện giao dịch trong ngày trong 05 ngày làm việc trước ngày đăng ký cuối cùng để thực hiện quyền cho cổ đông gắn với mã đó. Mỗi CTCK chỉ được mở 01 tài khoản giao dịch trong ngày cho một nhà đầu tư; không áp dụng với lô lẻ và giao dịch thỏa thuận (khoản 2 Điều 10). CTCK chỉ được cung cấp dịch vụ này khi đáp ứng điều kiện cho vay chứng khoán (khoản 2 Điều 199 NĐ 155/2020); UBCKNN triển khai tùy tình hình thị trường.",
 f"Khoản 2, 3, 6 Điều 10 {V120}; khoản 2 Điều 199 Nghị định 155/2020/NĐ-CP",
 "Hoạt động giao dịch trong ngày không được thực hiện trong khoảng thời gian năm (05) ngày làm việc, trước ngày đăng ký cuối cùng để thực hiện quyền cho cổ đông gắn với mã chứng khoán được giao dịch trong ngày.", TT120),

("SGDCK & VSDC", 2, "Theo Nghị định 155/2020/NĐ-CP, công ty chứng khoán đăng ký làm thành viên giao dịch (không phải thành viên giao dịch công cụ nợ) của Sở giao dịch chứng khoán phải đáp ứng điều kiện nào sau đây?",
 ["Có vốn điều lệ tối thiểu 1.000 tỷ đồng và hoạt động kinh doanh có lãi trong 02 năm gần nhất",
  "Là thành viên bù trừ, hoặc là thành viên lưu ký có hợp đồng ủy thác bù trừ với thành viên bù trừ chung",
  "Được cấp phép đủ các nghiệp vụ môi giới, tự doanh, bảo lãnh phát hành và tư vấn đầu tư chứng khoán",
  "Có thể đang trong tình trạng kiểm soát nếu đã được UBCKNN chấp thuận phương án khắc phục"], 1,
 "Điều 97: CTCK phải là thành viên bù trừ hoặc thành viên lưu ký có hợp đồng ủy thác bù trừ, thanh toán với thành viên bù trừ chung; đáp ứng hạ tầng CNTT, quy trình, nhân sự theo quy chế của Sở; không trong tình trạng kiểm soát, kiểm soát đặc biệt. Yêu cầu là thành viên lưu ký và được cấp phép đầy đủ các nghiệp vụ theo khoản 1 Điều 72 Luật Chứng khoán chỉ áp dụng khi đăng ký làm thành viên giao dịch công cụ nợ. SGDCK chấp thuận, hủy bỏ tư cách thành viên (điểm e khoản 1 Điều 46 Luật).",
 "Khoản 1, 3 Điều 97 Nghị định 155/2020/NĐ-CP",
 "Công ty chứng khoán là thành viên bù trừ hoặc thành viên lưu ký có hợp đồng ủy thác bù trừ, thanh toán với thành viên bù trừ chung", ND155),

("SGDCK & VSDC", 2, "Ngân hàng thương mại H được Sở giao dịch chứng khoán chấp thuận là thành viên giao dịch đặc biệt. Theo Nghị định 155/2020/NĐ-CP, phạm vi giao dịch của H là:",
 ["Giao dịch cổ phiếu và công cụ nợ cho chính mình và cho khách hàng của ngân hàng",
  "Giao dịch công cụ nợ cho chính mình và cho khách hàng là tổ chức tín dụng khác",
  "Giao dịch mọi loại chứng khoán niêm yết nhưng chỉ cho chính mình",
  "Chỉ giao dịch công cụ nợ cho chính mình"], 3,
 "Khoản 3 Điều 99: thành viên giao dịch đặc biệt, Kho bạc Nhà nước chỉ được giao dịch công cụ nợ cho chính mình. Điều kiện làm thành viên giao dịch đặc biệt: NHTM, chi nhánh NHNNg có vốn điều lệ thực góp/được cấp tối thiểu bằng vốn pháp định, không bị kiểm soát đặc biệt; là thành viên lưu ký hoặc tổ chức mở tài khoản trực tiếp tại VSDC; đáp ứng hạ tầng, quy trình, nhân sự (khoản 1 Điều 99).",
 "Khoản 1, 3 Điều 99 Nghị định 155/2020/NĐ-CP",
 "Thành viên giao dịch đặc biệt, Kho bạc Nhà nước chỉ được phép thực hiện giao dịch công cụ nợ cho chính mình.", ND155),

("SGDCK & VSDC", 2, "Hệ thống giao dịch của Sở giao dịch chứng khoán Việt Nam gặp sự cố làm ảnh hưởng đến hoạt động giao dịch bình thường của thị trường. Theo Luật Chứng khoán, chủ thể có thẩm quyền tạm ngừng một phần hoặc toàn bộ hoạt động giao dịch của Sở giao dịch chứng khoán Việt Nam là:",
 ["Bộ trưởng Bộ Tài chính", "Thủ tướng Chính phủ", "Ủy ban Chứng khoán Nhà nước", "Hội đồng quản trị Sở giao dịch chứng khoán Việt Nam"], 2,
 "Điều 49: UBCKNN tạm ngừng, đình chỉ một phần hoặc toàn bộ hoạt động giao dịch của SGDCK Việt Nam và công ty con khi có chiến tranh, thiên tai, biến động lớn của nền kinh tế, sự cố hệ thống giao dịch, sự kiện bất khả kháng hoặc thị trường biến động bất thường; UBCKNN cũng quyết định khôi phục. Còn SGDCK có quyền tạm ngừng, đình chỉ giao dịch đối với một hoặc một số chứng khoán cụ thể (điểm d khoản 1 Điều 46).",
 "Khoản 1 Điều 49, điểm d khoản 1 Điều 46 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH)",
 "Ủy ban Chứng khoán Nhà nước thực hiện tạm ngừng, đình chỉ một phần hoặc toàn bộ hoạt động giao dịch của Sở giao dịch chứng khoán Việt Nam và công ty con trong trường hợp sau đây: a) Khi xảy ra chiến tranh, thảm họa tự nhiên, biến động lớn của nền kinh tế, sự cố hệ thống giao dịch", LUAT),

(LK, 2, "Theo Thông tư 120/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), kể từ khi triển khai bù trừ, thanh toán theo cơ chế đối tác bù trừ trung tâm, nhận định nào sau đây ĐÚNG về tài khoản của nhà đầu tư?",
 ["Nhà đầu tư mở tài khoản ký quỹ bù trừ trực tiếp tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam",
  "Mỗi nhà đầu tư chỉ được mở 01 tài khoản ký quỹ bù trừ trên toàn thị trường, tại một thành viên bù trừ",
  "Nhà đầu tư chỉ cần có tài khoản ký quỹ bù trừ khi đặt lệnh mua, không cần khi đặt lệnh bán",
  "Phải mở trước tại thành viên bù trừ 01 tài khoản ký quỹ bù trừ cho mỗi tài khoản giao dịch"], 3,
 "Điểm b khoản 1 Điều 6: từ khi triển khai cơ chế đối tác bù trừ trung tâm, nhà đầu tư phải có tài khoản ký quỹ bù trừ tại thành viên bù trừ trước khi giao dịch. Khoản 3 Điều 6: chỉ được mở 01 tài khoản ký quỹ bù trừ tại thành viên bù trừ tương ứng với mỗi tài khoản giao dịch, trừ trường hợp luật định. Khi đó CTCK chỉ nhập lệnh khi nhà đầu tư đã đáp ứng ký quỹ bù trừ (điểm b khoản 2 Điều 7). Các khoản này đều được sửa đổi bởi TT 08/2026; quy định cũ về tài khoản tại ngân hàng lưu ký đã bỏ.",
 f"Điểm b khoản 1, khoản 3 Điều 6; điểm b khoản 2 Điều 7 {V120} (sửa đổi bởi khoản 1, 2 Điều 4 và khoản 1 Điều 5 Thông tư 08/2026/TT-BTC)",
 "Nhà đầu tư chỉ được mở 01 tài khoản ký quỹ bù trừ tại thành viên bù trừ tương ứng với mỗi tài khoản giao dịch chứng khoán, ngoại trừ một số trường hợp theo pháp luật về bù trừ, thanh toán giao dịch chứng khoán.", TT120),

(LK, 2, "Theo Nghị định 155/2020/NĐ-CP (sửa đổi bởi Nghị định 245/2025/NĐ-CP), cơ chế đối tác bù trừ trung tâm áp dụng cho bù trừ, thanh toán giao dịch chứng khoán niêm yết, đăng ký giao dịch trên hệ thống giao dịch, NGOẠI TRỪ giao dịch:",
 ["Cổ phiếu niêm yết", "Chứng chỉ quỹ ETF", "Chứng quyền có bảo đảm", "Trái phiếu doanh nghiệp"], 3,
 "Khoản 1 Điều 150 (sửa đổi bởi khoản 65 Điều 1 NĐ 245/2025): cơ chế đối tác bù trừ trung tâm không áp dụng cho bù trừ, thanh toán giao dịch công cụ nợ và trái phiếu doanh nghiệp. Trong cơ chế này VSDC (hoặc công ty con được VSDC phân công) thế vị, bù trừ và xác định nghĩa vụ thanh toán cho thành viên bù trừ dựa trên kết quả giao dịch hợp lệ do SGDCK cung cấp.",
 "Khoản 1 Điều 150 Nghị định 155/2020/NĐ-CP (sửa đổi bởi điểm a khoản 65 Điều 1 Nghị định 245/2025/NĐ-CP)",
 "ngoại trừ hoạt động bù trừ, thanh toán giao dịch công cụ nợ, trái phiếu doanh nghiệp", ND245),

# ---------------- Chuyên đề 6: đăng ký, lưu ký, bù trừ, thanh toán ----------------
("SGDCK & VSDC", 1, "Theo Luật Chứng khoán, thẩm quyền đối với Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam (VSDC) được phân định như thế nào?",
 ["Thủ tướng quyết định thành lập, cơ cấu tổ chức; Bộ trưởng Bộ Tài chính phê chuẩn Điều lệ",
  "Bộ trưởng Bộ Tài chính quyết định thành lập; Chủ tịch UBCKNN phê chuẩn hoặc ban hành Điều lệ",
  "Thủ tướng quyết định thành lập và trực tiếp phê chuẩn Điều lệ theo đề nghị của UBCKNN",
  "UBCKNN quyết định thành lập; Hội đồng thành viên VSDC tự ban hành, sửa đổi Điều lệ"], 0,
 "Điều 52–54: Thủ tướng quyết định thành lập, giải thể, mô hình hoạt động, hình thức sở hữu và cơ cấu tổ chức quản lý của VSDC theo đề nghị của Bộ trưởng Bộ Tài chính; Chủ tịch HĐTV/HĐQT, Tổng giám đốc và Điều lệ VSDC do Bộ trưởng Bộ Tài chính phê chuẩn hoặc ban hành theo đề nghị của HĐTV/HĐQT và ý kiến Chủ tịch UBCKNN. VSDC do Nhà nước nắm trên 50% vốn điều lệ, chịu sự quản lý, giám sát của UBCKNN.",
 "Khoản 2 Điều 52, Điều 53, khoản 1 Điều 54 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH)",
 "Điều lệ Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam được Bộ trưởng Bộ Tài chính phê chuẩn hoặc ban hành, sửa đổi, bổ sung theo đề nghị của Hội đồng thành viên hoặc Hội đồng quản trị", LUAT),

(LK, 1, "Theo Nghị định 155/2020/NĐ-CP, công ty chứng khoán đề nghị cấp Giấy chứng nhận đủ điều kiện cung cấp dịch vụ bù trừ, thanh toán giao dịch chứng khoán để làm thành viên bù trừ chung phải có vốn điều lệ, vốn chủ sở hữu tối thiểu là:",
 ["250 tỷ đồng", "900 tỷ đồng", "1.000 tỷ đồng", "7.000 tỷ đồng"], 1,
 "Khoản 2 Điều 151: thành viên bù trừ trực tiếp cần tối thiểu 250 tỷ đồng (CTCK) hoặc 1.000 tỷ đồng (NHTM, chi nhánh NHNNg); thành viên bù trừ chung cần 900 tỷ đồng (CTCK) hoặc 7.000 tỷ đồng (NHTM, chi nhánh NHNNg). CTCK còn phải có nợ/VCSH không quá 05 lần và tỷ lệ vốn khả dụng tối thiểu 260% liên tục 12 tháng gần nhất (điểm a khoản 3 Điều 151). Đây là điều kiện của thị trường cơ sở, khác với thị trường phái sinh (Nghị định 158/2020).",
 "Điểm b khoản 2, điểm a khoản 3 Điều 151 Nghị định 155/2020/NĐ-CP (khoản 2, 3 không bị Nghị định 245/2025/NĐ-CP sửa đổi)",
 "Đối với thành viên bù trừ chung: Có vốn điều lệ, vốn chủ sở hữu tối thiểu 7.000 tỷ đồng (đối với ngân hàng thương mại, chi nhánh ngân hàng nước ngoài) hoặc tối thiểu 900 tỷ đồng (đối với công ty chứng khoán).", ND155),

(LK, 2, "Theo Nghị định 155/2020/NĐ-CP, tổ chức nào sau đây KHÔNG thuộc đối tượng được mở tài khoản trực tiếp tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam?",
 ["Tổng công ty đầu tư và kinh doanh vốn Nhà nước", "Kho bạc Nhà nước", "Trung tâm lưu ký chứng khoán nước ngoài", "Công ty quản lý quỹ đầu tư chứng khoán trong nước"], 3,
 "Khoản 1 Điều 165: tổ chức mở tài khoản trực tiếp gồm SCIC; tổ chức tín dụng, bảo hiểm tham gia giao dịch công cụ nợ do SGDCK tổ chức; NHNN, Kho bạc Nhà nước, trung tâm lưu ký chứng khoán nước ngoài. VSDC cung cấp dịch vụ cho các tổ chức này trên cơ sở hợp đồng hoặc văn bản thỏa thuận. Công ty quản lý quỹ lưu ký chứng khoán qua thành viên lưu ký (ngân hàng lưu ký, CTCK).",
 "Khoản 1, 4 Điều 165 Nghị định 155/2020/NĐ-CP",
 "a) Tổng công ty đầu tư và kinh doanh vốn Nhà nước; b) Các tổ chức tín dụng, bảo hiểm tham gia giao dịch công cụ nợ do Sở giao dịch chứng khoán tổ chức; c) Ngân hàng Nhà nước Việt Nam, Kho bạc Nhà nước, Trung tâm lưu ký chứng khoán nước ngoài.", ND155),

(LK, 2, "Theo Nghị định 155/2020/NĐ-CP, ngân hàng thương mại làm ngân hàng thanh toán có nghĩa vụ nào sau đây?",
 ["Đóng góp vào quỹ hỗ trợ thanh toán do Tổng công ty lưu ký và bù trừ chứng khoán quản lý",
  "Cho thành viên bù trừ vay hỗ trợ thanh toán khi thành viên đó mất khả năng thanh toán",
  "Bảo lãnh thanh toán cho mọi giao dịch mua cổ phiếu của nhà đầu tư nước ngoài là tổ chức",
  "Thực hiện bù trừ đa phương nghĩa vụ chứng khoán giữa các thành viên lưu ký"], 1,
 "Khoản 2 Điều 166: NHTM làm ngân hàng thanh toán phải duy trì điều kiện tại khoản 2 Điều 69 Luật (vốn điều lệ trên 10.000 tỷ đồng, có lãi 02 năm gần nhất…), cho thành viên bù trừ vay để hỗ trợ thanh toán khi mất khả năng thanh toán, bồi thường cho VSDC, thành viên bù trừ nếu thanh toán sai do lỗi của mình, báo cáo và công bố thông tin. Quỹ hỗ trợ thanh toán do thành viên lưu ký đóng góp; bù trừ do VSDC thực hiện.",
 "Điểm b khoản 2 Điều 166 Nghị định 155/2020/NĐ-CP; khoản 2 Điều 69 Luật Chứng khoán 2019",
 "Thực hiện cho thành viên bù trừ vay để hỗ trợ thanh toán giao dịch chứng khoán trong trường hợp thành viên bù trừ mất khả năng thanh toán giao dịch chứng khoán", ND155),

(LK, 2, "Theo Nghị định 155/2020/NĐ-CP (sửa đổi bởi Nghị định 245/2025/NĐ-CP), nhận định nào sau đây ĐÚNG về đăng ký chứng khoán tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam?",
 ["Việc đăng ký chứng khoán tại VSDC đồng thời là chấp thuận cho chứng khoán đó được niêm yết",
  "Phải hoàn tất trước khi đưa vào giao dịch, không thể hiện chứng khoán đủ điều kiện niêm yết",
  "Có thể hoàn tất trong 30 ngày sau ngày giao dịch đầu tiên trên Sở giao dịch chứng khoán",
  "Chỉ bắt buộc với cổ phiếu niêm yết, không bắt buộc với cổ phiếu đăng ký giao dịch UPCoM"], 1,
 "Khoản 3a, 3b Điều 149 (bổ sung bởi khoản 64 Điều 1 NĐ 245/2025): công ty đại chúng, tổ chức phát hành phải hoàn tất đăng ký chứng khoán tại VSDC trước khi đưa vào giao dịch; việc đăng ký này không thể hiện chứng khoán đủ điều kiện niêm yết, đăng ký giao dịch. Cổ phiếu niêm yết, đăng ký giao dịch và chứng khoán của công ty đại chúng đều phải đăng ký tại VSDC (khoản 1 Điều 149); việc chấp thuận niêm yết thuộc SGDCK.",
 "Khoản 1, 3a, 3b Điều 149 Nghị định 155/2020/NĐ-CP (bổ sung bởi điểm a khoản 64 Điều 1 Nghị định 245/2025/NĐ-CP)",
 "Việc đăng ký chứng khoán tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam không thể hiện chứng khoán đó đủ điều kiện niêm yết, đăng ký giao dịch tại Sở giao dịch chứng khoán.", ND245),

(LK, 2, "Theo Thông tư 119/2020/TT-BTC, Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam hủy đăng ký chứng khoán trong các trường hợp sau, NGOẠI TRỪ:",
 ["Trái phiếu doanh nghiệp đến thời gian đáo hạn theo phương án phát hành",
  "Chứng quyền có bảo đảm đã đến thời gian đáo hạn theo bản cáo bạch",
  "Tổ chức phát hành giải thể, phá sản hoặc chấm dứt tồn tại",
  "Cổ phiếu bị hủy niêm yết bắt buộc, công ty vẫn là công ty đại chúng"], 3,
 "Khoản 1 Điều 7: VSDC hủy đăng ký khi trái phiếu, chứng quyền đáo hạn hoặc được mua lại trước hạn; tổ chức phát hành giảm vốn, giải thể, phá sản, chấm dứt tồn tại; hoán đổi; công ty đại chúng không còn đáp ứng điều kiện công ty đại chúng và có yêu cầu hủy… Công ty còn là công ty đại chúng thì chứng khoán vẫn phải đăng ký tập trung tại VSDC (khoản 1 Điều 61 Luật), cổ phiếu bị hủy niêm yết được chuyển sang đăng ký giao dịch.",
 f"Khoản 1 Điều 7 {V119}; khoản 1 Điều 61 Luật Chứng khoán 2019",
 "Chứng khoán của các công ty đại chúng đã đăng ký tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam nhưng không còn đáp ứng điều kiện là công ty đại chúng và công ty có yêu cầu huỷ đăng ký", TT119),

(LK, 2, "Nhà đầu tư N có cổ phiếu Y đã lưu ký tại công ty chứng khoán A. Y chia cổ tức bằng cổ phiếu, phát sinh phần lẻ cổ phần. Theo Thông tư 119/2020/TT-BTC (sửa đổi bởi Thông tư 18/2025/TT-BTC), N nhận quyền như thế nào?",
 ["Nhận toàn bộ quyền trực tiếp tại tổ chức phát hành, kể cả phần cổ phiếu chẵn",
  "Qua VSDC và thành viên lưu ký A; riêng phần lẻ cổ phần nhận tại tổ chức phát hành",
  "Nhận qua Sở giao dịch chứng khoán nơi cổ phiếu Y niêm yết, kể cả phần lẻ cổ phần",
  "Nhận qua ngân hàng thanh toán nơi thành viên lưu ký A mở tài khoản tiền gửi thanh toán"], 1,
 "Khoản 3 Điều 8 (sửa đổi bởi khoản 5 Điều 1 TT 18/2025): người sở hữu chứng khoán đã lưu ký nhận quyền, lợi ích qua VSDC và thành viên lưu ký nơi mở tài khoản (trừ khi pháp luật chuyên ngành quy định khác), phần lẻ cổ phần nhận tại tổ chức phát hành, công ty đại chúng hoặc tổ chức được ủy quyền; người chưa lưu ký nhận toàn bộ tại tổ chức phát hành. Chỉ người có tên trong danh sách tại ngày đăng ký cuối cùng mới được nhận quyền (khoản 5 Điều 61 Luật).",
 f"Khoản 3 Điều 8 {V119} (sửa đổi bởi khoản 5 Điều 1 Thông tư 18/2025/TT-BTC); khoản 5 Điều 61 Luật Chứng khoán 2019",
 "các thành viên lưu ký nơi người sở hữu chứng khoán mở tài khoản lưu ký chứng khoán ngoại trừ trường hợp pháp luật chuyên ngành có quy định khác và nhận phần lẻ cổ phần phát sinh (nếu có) tại tổ chức phát hành, công ty đại chúng", TT119),

(LK, 2, "Theo Thông tư 119/2020/TT-BTC, mỗi thành viên lưu ký chỉ được mở 01 tài khoản lưu ký chứng khoán tại VSDC và không được mở tài khoản lưu ký tại thành viên lưu ký khác, trừ một số trường hợp. Trường hợp nào sau đây là một ngoại lệ cho phép mở tại thành viên lưu ký khác?",
 ["Công ty chứng khoán là nhà tạo lập thị trường cần tài khoản riêng để thực hiện hoạt động tạo lập thị trường",
  "Công ty chứng khoán phát hành chứng quyền có bảo đảm cần tài khoản riêng để phòng ngừa rủi ro",
  "CTCK đã chấm dứt tư cách thành viên SGDCK Việt Nam, cần xử lý chứng khoán còn lại trên tài khoản tự doanh",
  "Thành viên lưu ký muốn quản lý riêng chứng khoán của khách hàng nước ngoài tại một thành viên khác"], 2,
 "Khoản 1 Điều 14: ngoại lệ mở tài khoản tại thành viên lưu ký khác gồm mở tại thành viên lập quỹ để giao dịch ETF; CTCK đã chấm dứt tư cách thành viên SGDCK Việt Nam để xử lý chứng khoán còn lại trên tài khoản tự doanh; thành viên lưu ký không phải thành viên bù trừ mở tại thành viên bù trừ. Với chứng quyền (phòng ngừa rủi ro) và tạo lập thị trường, thành viên mở thêm 01 tài khoản tại chính VSDC, không phải tại thành viên khác. Khách hàng nước ngoài được quản lý trên tài khoản riêng thuộc tài khoản của thành viên tại VSDC (khoản 2 Điều 15).",
 f"Khoản 1 Điều 14, khoản 2 Điều 15 {V119}",
 "Thành viên lưu ký là công ty chứng khoán đã chấm dứt tư cách thành viên tại Sở giao dịch chứng khoán Việt Nam được phép mở tài khoản lưu ký chứng khoán tại các thành viên lưu ký khác để xử lý số chứng khoán còn lại trên tài khoản tự doanh", TT119),

(LK, 2, "Nhà đầu tư M chuyển toàn bộ cổ phiếu từ tài khoản lưu ký của mình tại công ty chứng khoán A sang tài khoản lưu ký của chính M tại công ty chứng khoán B. Theo Thông tư 119/2020/TT-BTC, nhận định nào ĐÚNG?",
 ["Đây là chuyển quyền sở hữu ngoài hệ thống, phải có ý kiến chấp thuận của UBCKNN",
  "M phải bán cổ phiếu trên hệ thống qua A rồi mua lại qua B, do không được chuyển khoản lưu ký",
  "Là chuyển khoản không gắn với chuyển quyền sở hữu; VSDC xử lý trong 01 ngày làm việc",
  "Là chuyển khoản không gắn với chuyển quyền sở hữu; VSDC xử lý trong tối đa 10 ngày làm việc"], 2,
 "Điểm a khoản 2 Điều 22: VSDC thực hiện chuyển khoản chứng khoán (và quyền phát sinh kèm theo) giữa các tài khoản của chính khách hàng tại các thành viên lưu ký khác nhau, không gắn với chuyển quyền sở hữu. Thành viên lưu ký chuyển hồ sơ cho VSDC trong 01 ngày làm việc (khoản 4) và VSDC xử lý trong 01 ngày làm việc (khoản 5); thời hạn tối đa 05 ngày làm việc chỉ áp dụng cho các trường hợp tại điểm e, g khoản 2 và khoản 3.",
 f"Điểm a khoản 2, khoản 4, 5 Điều 22 {V119}",
 "Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam có trách nhiệm xử lý hồ sơ chuyển khoản chứng khoán trong thời hạn 01 ngày làm việc đối với các trường hợp chuyển khoản quy định tại các điểm a, b, c, d, đ, h khoản 2 Điều này", TT119),

(LK, 3, "Thành viên lưu ký M thiếu chứng khoán cho một giao dịch có giá trị 2 tỷ đồng nên bị VSDC lùi thời hạn thanh toán 02 ngày làm việc; sau đó M thanh toán đủ. Theo Thông tư 119/2020/TT-BTC (sửa đổi bởi Thông tư 18/2025/TT-BTC), khoản bồi thường M phải trả cho bên đối ứng là:",
 ["100 triệu đồng", "200 triệu đồng", "400 triệu đồng", "800 triệu đồng"], 1,
 "Điều 40h: thời hạn lùi thanh toán tối đa 03 ngày làm việc; thành viên lưu ký có giao dịch bị lùi phải bồi thường bên đối ứng 5% giá trị giao dịch lùi thanh toán cho mỗi ngày lùi: 5% × 2 tỷ × 2 ngày = 200 triệu đồng. 100 triệu là tính 1 ngày; 400 triệu là áp nhầm mức 20% (mức bồi thường khi giao dịch bị loại bỏ thanh toán, Điều 40i); 800 triệu là 20% × 2 ngày.",
 f"Khoản 2, 4 Điều 40h {V119} (bổ sung bởi khoản 10 Điều 1 Thông tư 18/2025/TT-BTC)",
 "Thành viên lưu ký có giao dịch bị lùi thời hạn thanh toán phải bồi thường cho tổ chức, cá nhân đối ứng liên quan theo mức 5% giá trị giao dịch lùi thanh toán trên 01 ngày lùi thanh toán.", TT119),

(LK, 2, "Giao dịch của thành viên lưu ký K bị lùi thời hạn thanh toán do thiếu chứng khoán, nhưng hết thời hạn lùi tối đa K vẫn không đủ chứng khoán. Theo Thông tư 119/2020/TT-BTC (sửa đổi bởi Thông tư 18/2025/TT-BTC), xử lý nào sau đây ĐÚNG?",
 ["VSDC tiếp tục lùi thêm 03 ngày làm việc, K bồi thường 5% giá trị cho mỗi ngày lùi thêm",
  "VSDC dùng quỹ hỗ trợ thanh toán mua chứng khoán thay, K hoàn trả quỹ trong 01 ngày",
  "VSDC hủy giao dịch, không bên nào phải bồi thường do đã áp dụng lùi thanh toán",
  "VSDC loại bỏ thanh toán giao dịch; K bồi thường bên đối ứng 20% giá trị giao dịch bị loại bỏ"], 3,
 "Điểm k khoản 1 Điều 40i: VSDC loại bỏ thanh toán giao dịch đã lùi thời hạn mà hết hạn vẫn không đủ chứng khoán; khoản 2 Điều 40i: thành viên lưu ký có giao dịch bị loại bỏ (trường hợp a, b, c, h, i, k, l, m) bồi thường bên đối ứng 20% giá trị giao dịch bị loại bỏ, và bị xử lý nếu có vi phạm. Thời hạn lùi tối đa chỉ 03 ngày làm việc (Điều 40h); quỹ hỗ trợ thanh toán chỉ dùng khi thành viên mất khả năng thanh toán tiền.",
 f"Điểm k khoản 1, khoản 2 Điều 40i; khoản 2 Điều 40h {V119} (bổ sung bởi khoản 10 Điều 1 Thông tư 18/2025/TT-BTC)",
 "thành viên lưu ký có giao dịch bị loại bỏ thanh toán phải bồi thường cho tổ chức, cá nhân có giao dịch đối ứng liên quan theo mức 20% giá trị giao dịch bị loại bỏ thanh toán", TT119),

(LK, 2, "Thành viên lưu ký Z tạm thời mất khả năng thanh toán tiền giao dịch chứng khoán. Theo Thông tư 119/2020/TT-BTC (sửa đổi bởi Thông tư 18/2025/TT-BTC), VSDC sử dụng quỹ hỗ trợ thanh toán như thế nào?",
 ["Dùng ngay khoản đóng góp của các thành viên lưu ký khác, sau đó mới dùng khoản đóng góp của chính Z",
  "Trước hết dùng phần đóng góp của Z; thiếu mà không vay đủ ngân hàng thanh toán mới dùng phần thành viên khác",
  "Chỉ dùng khoản đóng góp của Z; phần còn thiếu thì VSDC loại bỏ thanh toán các giao dịch mua tương ứng",
  "Chia đều số tiền thiếu cho tất cả thành viên lưu ký theo tỷ lệ đóng góp quỹ của từng thành viên"], 1,
 "Điểm b khoản 1 Điều 40l: VSDC dùng khoản đóng góp quỹ của chính thành viên (sau khi trừ khoản đã dùng chưa hoàn trả); nếu không đủ và ngân hàng thanh toán không cho vay hoặc chỉ cho vay một phần, mới dùng khoản đóng góp của thành viên khác (trên 50 tỷ đồng/ngày phải báo cáo UBCKNN). Z phải hoàn trả số tiền đã dùng trong 01 ngày và trả lãi sử dụng quỹ (điểm a khoản 2 Điều 40l). Thành viên mất khả năng thanh toán tiền còn được vay ngân hàng thanh toán (khoản 1 Điều 40g).",
 f"Điểm b khoản 1, điểm a khoản 2 Điều 40l; khoản 1 Điều 40g {V119} (bổ sung bởi khoản 10 Điều 1 Thông tư 18/2025/TT-BTC)",
 "Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam sử dụng khoản đóng góp quỹ hỗ trợ thanh toán của chính thành viên lưu ký để hỗ trợ thanh toán sau khi trừ đi các khoản sử dụng chưa hoàn trả quỹ hỗ trợ thanh toán.", TT119),

(LK, 2, "Theo Nghị định 155/2020/NĐ-CP, chứng khoán được đăng ký biện pháp bảo đảm tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam phải tuân thủ nguyên tắc nào?",
 ["Có thể là chứng khoán đang bị tạm giữ, nếu bên nhận bảo đảm đồng ý bằng văn bản",
  "Không cần lưu ký, chỉ cần đã đăng ký tập trung tại VSDC là đủ để đăng ký",
  "Vẫn được giao dịch bình thường trên hệ thống trong suốt thời hạn đăng ký biện pháp bảo đảm",
  "Phải tự do chuyển nhượng, không dùng để ký quỹ, không bị phong tỏa, tạm giữ và phải lưu ký trước"], 3,
 "Điểm a khoản 2 Điều 169: chứng khoán đăng ký biện pháp bảo đảm phải tự do chuyển nhượng, không dùng để ký quỹ giao dịch, không bị phong tỏa, tạm giữ và phải lưu ký trước; trong thời hạn đăng ký bị phong tỏa tại VSDC, xóa đăng ký thì được giải tỏa. Hiệu lực đăng ký là thời điểm VSDC ghi vào sổ đăng ký thông tin biện pháp bảo đảm. Khi chứng khoán bị hủy đăng ký tập trung mà các bên không xóa đăng ký, VSDC tự động xóa biện pháp bảo đảm để hủy đăng ký (khoản 4, sửa đổi bởi NĐ 245/2025).",
 "Điểm a, c khoản 2, khoản 4 Điều 169 Nghị định 155/2020/NĐ-CP (khoản 4 sửa đổi bởi khoản 69 Điều 1 Nghị định 245/2025/NĐ-CP)",
 "Chứng khoán được đăng ký biện pháp bảo đảm phải là loại chứng khoán tự do chuyển nhượng, không dùng để ký quỹ trong các giao dịch chứng khoán, không bị phong tỏa, tạm giữ và phải lưu ký trước khi thực hiện.", ND155),

(LK, 3, "Cổ phiếu X đã đạt mức tối đa về tỷ lệ sở hữu nước ngoài. Quỹ nước ngoài A thỏa thuận bán cho quỹ nước ngoài B 1 triệu cổ phiếu X với giá cao hơn giá trần trên hệ thống giao dịch tại thời điểm giao dịch. Theo Thông tư 119/2020/TT-BTC, giao dịch này:",
 ["Phải thực hiện bằng giao dịch thỏa thuận trên hệ thống, với giá không vượt giá trần",
  "Được chuyển quyền sở hữu ngoài hệ thống giao dịch qua VSDC theo trường hợp luật định",
  "Chỉ được thực hiện ngoài hệ thống sau khi có văn bản chấp thuận riêng của UBCKNN",
  "Không được thực hiện vì cổ phiếu X đã hết tỷ lệ sở hữu dành cho nhà đầu tư nước ngoài"], 1,
 "Điểm q khoản 2 Điều 6: chuyển quyền sở hữu cổ phiếu giữa các nhà đầu tư nước ngoài khi cổ phiếu đã đạt tỷ lệ sở hữu nước ngoài tối đa và giá thỏa thuận cao hơn giá trần là trường hợp chuyển quyền sở hữu ngoài hệ thống do VSDC thực hiện; chỉ các trường hợp không được liệt kê mới cần ý kiến chấp thuận của UBCKNN (điểm r). Giao dịch giữa hai nhà đầu tư nước ngoài không làm tăng tổng sở hữu nước ngoài.",
 f"Điểm q, r khoản 2 Điều 6 {V119}",
 "Chuyển quyền sở hữu cổ phiếu giữa các nhà đầu tư nước ngoài với nhau trong trường hợp đã đạt mức tối đa về tỷ lệ sở hữu nước ngoài đối với cổ phiếu đó và mức giá thỏa thuận giữa các bên cao hơn giá trần của cổ phiếu trên hệ thống giao dịch chứng khoán", TT119),

(LK, 2, "Theo Thông tư 119/2020/TT-BTC, bên chuyển quyền sở hữu phải lưu ký chứng khoán trước khi chuyển quyền sở hữu ngoài hệ thống giao dịch. Trường hợp nào sau đây được miễn yêu cầu lưu ký trước?",
 ["Tặng cho chứng khoán giữa hai cá nhân còn sống, đang liên lạc được",
  "Giao dịch chứng khoán lô lẻ theo quy định pháp luật chứng khoán",
  "Chuyển quyền sở hữu theo bản án, quyết định của tòa án",
  "Phân chia tài sản chung của vợ chồng trong thời kỳ hôn nhân"], 2,
 "Khoản 5 Điều 6: miễn lưu ký trước khi chuyển quyền sở hữu khi bên chuyển nhượng mất tích, chết, định cư ở nước ngoài không liên lạc được; tổ chức phát hành mua lại cổ phiếu của người lao động/cán bộ công nhân viên; chuyển quyền theo bản án, quyết định của tòa án, trọng tài, cơ quan thi hành án; tổ chức lại, giải thể mà bên chuyển không còn tồn tại; trường hợp khác được UBCKNN chấp thuận. Tặng cho, lô lẻ, chia tài sản vợ chồng vẫn phải lưu ký trước.",
 f"Khoản 5 Điều 6 {V119}",
 "Chuyển quyền sở hữu theo bản án, quyết định của tòa án, quyết định của trọng tài hoặc quyết định của cơ quan thi hành án", TT119),
]

def norm_ws(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
def loose(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"(?<=[^\W\d_])\d{1,3}(?=\W|$)", "", s)
    return re.sub(r"[\W_]+", "", s)
_cache = {}
def text(name):
    if name not in _cache:
        raw = (DOCS / name).read_text(encoding="utf-8")
        clean = "\n".join(l for l in raw.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
        _cache[name] = norm_ws(clean) + " \x00 " + norm_ws(raw)
    return _cache[name]

out, problems = [], []
for n, (topic, lvl, q, o, a, e, basis, quote, src) in enumerate(ITEMS, 1):
    i = f"L3-{n:03d}"
    t = text(src)
    if not (norm_ws(quote) in t or loose(quote) in loose(t)): problems.append(f"{i}: quote không khớp {src}")
    if len(quote) > 300: problems.append(f"{i}: quote dài {len(quote)}")
    if len(o) != 4 or len(set(o)) != 4: problems.append(f"{i}: phương án")
    lens = [len(x) for x in o]
    if max(lens) > 2.2 * min(lens) and min(lens) > 20: problems.append(f"{i}: độ dài phương án lệch {lens}")
    if re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", e): problems.append(f"{i}: e nhắc tên phương án")
    target = (n - 1) % 4  # xoay để đáp án đúng chia đều; an toàn vì không phương án nào tham chiếu phương án khác
    o = o[:]; c = o.pop(a); o.insert(target, c); a = target
    out.append({"id": i, "part": "LUAT", "subject": "LU", "topic": topic, "level": lvl, "q": q, "o": o, "a": a,
                "e": e, "basis": basis, "quote": quote, "src": src, "as_of": "2026-11"})
from collections import Counter
print(len(out), "câu; đáp án:", dict(sorted(Counter(x["a"] for x in out).items())), "; mức:", dict(sorted(Counter(x["level"] for x in out).items())))
print("chủ đề:", dict(Counter(x["topic"] for x in out)))
if problems: print("VẤN ĐỀ:\n" + "\n".join(problems)); sys.exit(1)
(HERE / "luat_3.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("ghi", HERE / "luat_3.json")
