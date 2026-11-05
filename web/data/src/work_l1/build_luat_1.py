# Build luat_1.json. Each question is authored with the correct option first;
# the script moves it to a balanced, deterministic answer position.
import json, random, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "luat_1.json"
LAW = "VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt"
TT135 = "TT_135_2025_TT-BTC_English_SSC.txt"
UBCK = "UBCK_thong_bao_thi_sat_hach_2026_va_gioi_thieu_TT135_ND245.md"
ND245 = "ND_245_2025_ND-CP_Cong_bao_so_1403-1408_2025.txt"
LCK = "Luật Chứng khoán 2019"
SD = " (sửa đổi, bổ sung bởi Luật 56/2024/QH15)"

T_DN = "Giải thích từ ngữ"
T_NDT = "Nhà đầu tư chuyên nghiệp"
T_CAM = "Hành vi bị cấm"
T_CB = "Chào bán ra công chúng"
T_RL = "Chào bán riêng lẻ"
T_DC = "Công ty đại chúng"
T_SG = "SGDCK & VSDC"
T_CT = "CTCK & CTQLQ"
T_HN = "Chứng chỉ hành nghề & quy chế thi 2026"
T_QUY = "Quỹ đầu tư"
T_CB2 = "Công bố thông tin"
T_TT = "Thanh tra & xử lý vi phạm"

Q = []


def q(topic, level, text, correct, wrong, e, basis, quote, src=LAW):
    assert len(wrong) == 3
    Q.append(dict(topic=topic, level=level, q=text, o=[correct] + wrong, e=e,
                  basis=basis, quote=quote, src=src))


# ---------------- Giải thích từ ngữ (6) ----------------
q(T_DN, 1,
  "Theo khoản 19 Điều 4 Luật Chứng khoán, chào bán chứng khoán cho bao nhiêu nhà đầu tư (không kể nhà đầu tư chứng khoán chuyên nghiệp) thì thuộc trường hợp chào bán ra công chúng?",
  "Từ 100 nhà đầu tư trở lên",
  ["Trên 100 nhà đầu tư", "Từ 50 nhà đầu tư trở lên", "Từ 200 nhà đầu tư trở lên"],
  "Chào bán ra công chúng gồm: chào bán qua phương tiện thông tin đại chúng; chào bán cho từ 100 nhà đầu tư trở lên (không kể nhà đầu tư chứng khoán chuyên nghiệp); chào bán cho nhà đầu tư không xác định. Ngưỡng là 'từ 100' (bao gồm 100), không phải 'trên 100'.",
  f"Điểm b khoản 19 Điều 4 {LCK}",
  "Chào bán cho từ 100 nhà đầu tư trở lên, không kể nhà đầu tư chứng khoán chuyên nghiệp")

q(T_DN, 1,
  "Theo Luật Chứng khoán, cổ đông lớn là cổ đông sở hữu:",
  "Từ 5% trở lên số cổ phiếu có quyền biểu quyết của một tổ chức phát hành",
  ["Từ 5% trở lên vốn điều lệ đã góp của một tổ chức phát hành",
   "Trên 10% số cổ phiếu có quyền biểu quyết của một tổ chức phát hành",
   "Từ 10% trở lên tổng số cổ phiếu đã phát hành của một tổ chức phát hành"],
  "Cổ đông lớn được xác định theo tỷ lệ từ 5% trở lên số cổ phiếu có quyền biểu quyết (không tính theo vốn điều lệ hay tổng số cổ phiếu đã phát hành). Mốc trên 10% là tiêu chí xác định người có liên quan giữa doanh nghiệp và người sở hữu.",
  f"Khoản 18 Điều 4 {LCK}",
  "Cổ đông lớn là cổ đông sở hữu từ 5% trở lên số cổ phiếu có quyền biểu quyết của một tổ chức phát hành.")

q(T_DN, 2,
  "Theo Luật Chứng khoán, đặc điểm phân biệt quỹ đóng với quỹ mở là gì?",
  "Chứng chỉ quỹ đóng không được mua lại theo yêu cầu của nhà đầu tư",
  ["Quỹ đóng chỉ được chào bán cho nhà đầu tư chứng khoán chuyên nghiệp",
   "Chứng chỉ quỹ đóng không được niêm yết trên hệ thống giao dịch chứng khoán",
   "Quỹ đóng có tối đa 99 nhà đầu tư, quỹ mở có tối thiểu 100 nhà đầu tư"],
  "Cả quỹ mở và quỹ đóng đều là quỹ đại chúng. Chứng chỉ quỹ mở phải được mua lại theo yêu cầu của nhà đầu tư; chứng chỉ quỹ đóng thì không được mua lại theo yêu cầu và phải niêm yết sau đợt chào bán. Giới hạn 02–99 thành viên là đặc điểm của quỹ thành viên.",
  f"Khoản 39, 40 Điều 4 {LCK}",
  "Quỹ đóng là quỹ đại chúng mà chứng chỉ quỹ đã chào bán ra công chúng không được mua lại theo yêu cầu của nhà đầu tư.")

q(T_DN, 1,
  "Quỹ đầu tư bất động sản đầu tư chủ yếu vào bất động sản và chứng khoán của tổ chức kinh doanh bất động sản có doanh thu từ việc sở hữu và kinh doanh bất động sản tối thiểu bằng bao nhiêu phần trăm tổng doanh thu (theo báo cáo tài chính năm gần nhất)?",
  "65%",
  ["50%", "51%", "80%"],
  "Khoản 43 Điều 4 Luật Chứng khoán: tổ chức kinh doanh bất động sản có doanh thu từ sở hữu và kinh doanh bất động sản tối thiểu 65% tổng doanh thu tính trên báo cáo tài chính năm gần nhất.",
  f"Khoản 43 Điều 4 {LCK}",
  "có doanh thu từ việc sở hữu và kinh doanh bất động sản tối thiểu là 65% tổng doanh thu tính trên báo cáo tài chính năm gần nhất")

q(T_DN, 2,
  "Bà H sở hữu 12% số cổ phiếu có quyền biểu quyết của Công ty cổ phần A nhưng không giữ chức vụ nào tại A. Theo Luật Chứng khoán, quan hệ giữa bà H và Công ty A được xác định thế nào?",
  "Bà H và Công ty A là người có liên quan của nhau",
  ["Bà H chỉ là cổ đông lớn, chưa phải người có liên quan vì tỷ lệ dưới 20%",
   "Bà H là người nội bộ của Công ty A",
   "Bà H chỉ là người có liên quan nếu được bầu vào Hội đồng quản trị"],
  "Doanh nghiệp và tổ chức, cá nhân sở hữu trên 10% số cổ phiếu có quyền biểu quyết hoặc vốn góp của doanh nghiệp đó là người có liên quan. Bà H (12%) đồng thời là cổ đông lớn (từ 5%) nhưng không phải người nội bộ vì không giữ chức danh quản trị, điều hành.",
  f"Điểm b khoản 46 Điều 4 {LCK}",
  "Doanh nghiệp và tổ chức, cá nhân sở hữu trên 10% số cổ phiếu có quyền biểu quyết hoặc vốn góp của doanh nghiệp đó")

q(T_DN, 2,
  "Theo khoản 45 Điều 4 Luật Chứng khoán, đối tượng nào sau đây KHÔNG phải là người nội bộ của doanh nghiệp?",
  "Cổ đông nắm 4% cổ phần, không giữ chức danh nào",
  ["Người phụ trách quản trị công ty do HĐQT bổ nhiệm", "Thành viên Ban kiểm toán nội bộ của công ty",
   "Người được ủy quyền công bố thông tin của công ty"],
  "Người nội bộ của doanh nghiệp gồm Chủ tịch, thành viên HĐQT/HĐTV, người đại diện theo pháp luật, Tổng giám đốc, Phó Tổng giám đốc, Giám đốc tài chính, Kế toán trưởng, Ban kiểm soát, thành viên Ban kiểm toán nội bộ, thư ký công ty, người phụ trách quản trị công ty, người được ủy quyền công bố thông tin. Tư cách cổ đông (nhất là dưới 5%) không làm phát sinh tư cách người nội bộ.",
  f"Điểm a khoản 45 Điều 4 {LCK}",
  "thành viên Ban kiểm toán nội bộ; thư ký công ty, người phụ trách quản trị công ty, người được ủy quyền công bố thông tin")

# ---------------- Nhà đầu tư chuyên nghiệp (5) ----------------
q(T_NDT, 1,
  "Theo Điều 11 Luật Chứng khoán, công ty (không phải tổ chức niêm yết, đăng ký giao dịch) được xác định là nhà đầu tư chứng khoán chuyên nghiệp khi có vốn điều lệ đã góp:",
  "Trên 100 tỷ đồng",
  ["Từ 50 tỷ đồng trở lên", "Từ 30 tỷ đồng trở lên", "Từ 200 tỷ đồng trở lên"],
  "Điểm b khoản 1 Điều 11: công ty có vốn điều lệ đã góp đạt trên 100 tỷ đồng hoặc tổ chức niêm yết, tổ chức đăng ký giao dịch là nhà đầu tư chứng khoán chuyên nghiệp. Mốc 30 tỷ đồng là điều kiện vốn của công ty đại chúng/chào bán ra công chúng.",
  f"Điểm b khoản 1 Điều 11 {LCK}",
  "Công ty có vốn điều lệ đã góp đạt trên 100 tỷ đồng hoặc tổ chức niêm yết, tổ chức đăng ký giao dịch")

q(T_NDT, 3,
  "Ông K có danh mục cổ phiếu niêm yết trị giá 1,8 tỷ đồng (theo xác nhận của công ty chứng khoán), có thu nhập chịu thuế năm gần nhất 1,2 tỷ đồng theo hồ sơ khai thuế đã nộp và không có chứng chỉ hành nghề chứng khoán. Ông K có đủ tư cách nhà đầu tư chứng khoán chuyên nghiệp không?",
  "Có, vì đáp ứng tiêu chí thu nhập chịu thuế năm gần nhất tối thiểu 01 tỷ đồng",
  ["Không, vì giá trị danh mục chứng khoán chưa đạt 02 tỷ đồng",
   "Không, vì cá nhân phải đáp ứng đồng thời tiêu chí danh mục và thu nhập",
   "Có, nhưng chỉ khi được Ủy ban Chứng khoán Nhà nước xác nhận bằng văn bản"],
  "Các tiêu chí tại điểm c, d, đ khoản 1 Điều 11 là độc lập: có CCHN; hoặc danh mục chứng khoán niêm yết, đăng ký giao dịch tối thiểu 02 tỷ đồng; hoặc thu nhập chịu thuế năm gần nhất tối thiểu 01 tỷ đồng. Ông K chưa đạt tiêu chí danh mục nhưng đạt tiêu chí thu nhập (1,2 tỷ ≥ 01 tỷ) nên đủ tư cách.",
  f"Điểm d, đ khoản 1 Điều 11 {LCK}",
  "Cá nhân có thu nhập chịu thuế năm gần nhất tối thiểu là 01 tỷ đồng tính đến thời điểm cá nhân đó được xác định tư cách là nhà đầu tư chứng khoán chuyên nghiệp")

q(T_NDT, 1,
  "Luật số 56/2024/QH15 bổ sung nhóm đối tượng nào sau đây vào danh sách nhà đầu tư chứng khoán chuyên nghiệp?",
  "Nhà đầu tư nước ngoài thực hiện hoạt động đầu tư kinh doanh tại Việt Nam",
  ["Cá nhân có danh mục chứng khoán niêm yết, đăng ký giao dịch từ 01 tỷ đồng",
   "Hộ kinh doanh có doanh thu năm gần nhất từ 10 tỷ đồng trở lên tại Việt Nam",
   "Cá nhân có chứng chỉ chuyên môn chứng khoán do Trung tâm đào tạo của UBCKNN cấp"],
  "Điểm e khoản 1 Điều 11 được bổ sung bởi điểm a khoản 3 Điều 1 Luật 56/2024/QH15 (hiệu lực 01/01/2025): nhà đầu tư nước ngoài là cá nhân có quốc tịch nước ngoài, tổ chức thành lập theo pháp luật nước ngoài thực hiện hoạt động đầu tư kinh doanh tại Việt Nam là nhà đầu tư chứng khoán chuyên nghiệp.",
  f"Điểm e khoản 1 Điều 11 {LCK}{SD}",
  "Nhà đầu tư nước ngoài là cá nhân có quốc tịch nước ngoài, tổ chức thành lập theo pháp luật nước ngoài thực hiện hoạt động đầu tư kinh doanh tại Việt Nam.")

q(T_NDT, 3,
  "Tháng 10/2026, bà M (nhà đầu tư chứng khoán chuyên nghiệp là cá nhân) muốn mua trái phiếu doanh nghiệp phát hành riêng lẻ. Theo Luật Chứng khoán hiện hành, bà M được mua loại trái phiếu nào sau đây?",
  "Trái phiếu có xếp hạng tín nhiệm và có bảo lãnh thanh toán của tổ chức tín dụng",
  ["Trái phiếu không có xếp hạng tín nhiệm nhưng có tài sản bảo đảm",
   "Trái phiếu có xếp hạng tín nhiệm nhưng không có tài sản bảo đảm hay bảo lãnh",
   "Mọi loại trái phiếu riêng lẻ, vì bà M đã là nhà đầu tư chuyên nghiệp"],
  "Từ 01/01/2026, khoản 1b Điều 11 (bổ sung bởi Luật 56/2024) chỉ cho phép nhà đầu tư chuyên nghiệp là cá nhân mua, giao dịch, chuyển nhượng trái phiếu doanh nghiệp riêng lẻ khi trái phiếu có xếp hạng tín nhiệm VÀ có tài sản bảo đảm hoặc có bảo lãnh thanh toán của tổ chức tín dụng. Nhà đầu tư chuyên nghiệp là tổ chức không bị giới hạn này (khoản 1a).",
  f"Khoản 1b Điều 11 {LCK}{SD}; hiệu lực từ 01/01/2026",
  "Trái phiếu doanh nghiệp riêng lẻ có xếp hạng tín nhiệm và có bảo lãnh thanh toán của tổ chức tín dụng đối với trái phiếu đó.")

q(T_NDT, 2,
  "Đối tượng nào sau đây là nhà đầu tư chứng khoán chuyên nghiệp theo khoản 1 Điều 11 Luật Chứng khoán?",
  "Cá nhân có chứng chỉ hành nghề chứng khoán",
  ["Cá nhân có chứng chỉ chuyên môn về chứng khoán",
   "Cá nhân nắm giữ cổ phiếu chưa đăng ký giao dịch trị giá 03 tỷ đồng",
   "Công ty chưa niêm yết có vốn điều lệ đã góp 80 tỷ đồng"],
  "Người có chứng chỉ hành nghề chứng khoán là nhà đầu tư chuyên nghiệp (điểm c). Chứng chỉ chuyên môn không thay thế CCHN; danh mục chỉ tính chứng khoán niêm yết, đăng ký giao dịch (điểm d); công ty phải có vốn điều lệ đã góp trên 100 tỷ đồng hoặc là tổ chức niêm yết, đăng ký giao dịch (điểm b).",
  f"Điểm c khoản 1 Điều 11 {LCK}",
  "Người có chứng chỉ hành nghề chứng khoán;")

# ---------------- Hành vi bị cấm (5) ----------------
q(T_CAM, 1,
  "Hành vi nào sau đây thuộc các hành vi bị nghiêm cấm theo Điều 12 Luật Chứng khoán?",
  "Cho người khác mượn tài khoản, đứng tên sở hữu chứng khoán hộ dẫn đến thao túng giá",
  ["Nhà đầu tư đặt lệnh giới hạn mua cổ phiếu tại mức giá trần trong phiên",
   "Cổ đông lớn bán cổ phiếu sau khi đã công bố thông tin theo quy định",
   "Công ty chứng khoán mua, bán chứng khoán cho chính mình trên tài khoản tự doanh"],
  "Khoản 6 Điều 12 nghiêm cấm cho người khác mượn tài khoản để giao dịch chứng khoán, đứng tên sở hữu chứng khoán hộ người khác dẫn đến hành vi thao túng giá chứng khoán. Các phương án còn lại là hoạt động hợp pháp (tự doanh là nghiệp vụ được cấp phép).",
  f"Khoản 6 Điều 12 {LCK}",
  "Cho người khác mượn tài khoản để giao dịch chứng khoán, đứng tên sở hữu chứng khoán hộ người khác dẫn đến hành vi thao túng giá chứng khoán.")

q(T_CAM, 3,
  "Ông T là Kế toán trưởng của công ty niêm yết X, biết trước kết quả kinh doanh quý III giảm mạnh khi thông tin này chưa được công bố. Ông T không giao dịch nhưng khuyên em ruột bán toàn bộ cổ phiếu X trước ngày công bố. Nhận định nào đúng?",
  "Ông T vi phạm quy định cấm về thông tin nội bộ dù không trực tiếp giao dịch",
  ["Ông T không vi phạm vì bản thân không trực tiếp mua, bán cổ phiếu X",
   "Chỉ người em vi phạm vì là người trực tiếp đặt lệnh bán",
   "Không ai vi phạm nếu giao dịch được thực hiện qua phương thức khớp lệnh"],
  "Khoản 2 Điều 12 nghiêm cấm cả việc sử dụng thông tin nội bộ để giao dịch và việc tiết lộ, cung cấp thông tin nội bộ hoặc tư vấn cho người khác mua, bán chứng khoán trên cơ sở thông tin nội bộ. Kế toán trưởng là người nội bộ; kết quả kinh doanh chưa công bố là thông tin nội bộ.",
  f"Khoản 2 Điều 12; khoản 44, 45 Điều 4 {LCK}",
  "tiết lộ, cung cấp thông tin nội bộ hoặc tư vấn cho người khác mua, bán chứng khoán trên cơ sở thông tin nội bộ")

q(T_CAM, 2,
  "Theo khoản 49 Điều 4 Luật Chứng khoán (bổ sung bởi Luật 56/2024/QH15), hành vi nào sau đây là thao túng thị trường chứng khoán?",
  "Đặt lệnh mua và bán cùng loại chứng khoán trong ngày nhằm tạo cung cầu giả tạo",
  ["Đặt lệnh bán cổ phiếu tại giá sàn để cắt lỗ khi thị trường giảm mạnh",
   "Đăng ký mua cổ phiếu phát hành thêm theo quyền mua của cổ đông hiện hữu",
   "Mua cổ phiếu khối lượng lớn sau khi đã đăng ký và công bố chào mua công khai"],
  "Điểm b khoản 49 Điều 4 liệt kê hành vi đặt lệnh mua và bán cùng loại chứng khoán trong cùng ngày giao dịch hoặc thông đồng giao dịch mà không dẫn đến chuyển nhượng thực sự quyền sở hữu (hoặc chỉ luân chuyển trong nhóm) nhằm tạo giá, cung cầu giả tạo. Các phương án còn lại là giao dịch thông thường, hợp pháp.",
  f"Điểm b khoản 49 Điều 4 {LCK}{SD}",
  "Đặt lệnh mua và bán cùng loại chứng khoán trong cùng ngày giao dịch hoặc thông đồng với nhau giao dịch mua, bán chứng khoán mà không dẫn đến chuyển nhượng thực sự quyền sở hữu")

q(T_CAM, 3,
  "Anh P mua 2 triệu cổ phiếu Y, sau đó liên tục đăng bài trên mạng xã hội khẳng định Y sắp bị thâu tóm (không có căn cứ) để kéo giá lên, rồi bán toàn bộ khi giá tăng. Hành vi của anh P được xác định là:",
  "Thao túng thị trường chứng khoán",
  ["Sử dụng thông tin nội bộ để giao dịch chứng khoán",
   "Hành vi hợp pháp vì thuộc quyền tự do bày tỏ ý kiến",
   "Chỉ vi phạm nghĩa vụ công bố thông tin của cổ đông lớn"],
  "Điểm đ khoản 49 Điều 4: đưa ra ý kiến trực tiếp hoặc gián tiếp qua phương tiện thông tin đại chúng về một loại chứng khoán nhằm tạo ảnh hưởng đến giá sau khi đã giao dịch và nắm giữ vị thế là thao túng thị trường; khoản 3 Điều 12 nghiêm cấm hành vi này. Thông tin bịa đặt không phải thông tin nội bộ.",
  f"Điểm đ khoản 49 Điều 4; khoản 3 Điều 12 {LCK}{SD}",
  "Đưa ra ý kiến một cách trực tiếp hoặc gián tiếp thông qua phương tiện thông tin đại chúng về một loại chứng khoán, về tổ chức phát hành chứng khoán nhằm tạo ảnh hưởng đến giá của loại chứng khoán đó sau khi đã thực hiện giao dịch và nắm giữ vị thế")

q(T_CAM, 1,
  "Nhân viên môi giới tự ý đặt lệnh mua, bán trên tài khoản của khách hàng khi chưa được khách hàng ủy thác. Theo Luật Chứng khoán, hành vi này là:",
  "Hành vi bị nghiêm cấm trong hoạt động về chứng khoán",
  ["Hành vi được phép nếu giao dịch mang lại lợi nhuận cho khách hàng",
   "Vi phạm nội quy công ty, không thuộc hành vi bị nghiêm cấm",
   "Hành vi được phép đối với tài khoản giao dịch ký quỹ"],
  "Khoản 5 Điều 12 nghiêm cấm sử dụng tài khoản, tài sản của khách hàng khi không được khách hàng ủy thác hoặc trái quy định của pháp luật hoặc lạm dụng tín nhiệm để chiếm đoạt tài sản của khách hàng; kết quả lãi hay lỗ không làm thay đổi tính chất vi phạm.",
  f"Khoản 5 Điều 12 {LCK}",
  "Sử dụng tài khoản, tài sản của khách hàng khi không được khách hàng ủy thác hoặc trái quy định của pháp luật hoặc lạm dụng tín nhiệm để chiếm đoạt tài sản của khách hàng.")

# ---------------- Chào bán ra công chúng (13) ----------------
q(T_CB, 1,
  "Điều kiện về vốn để công ty cổ phần chào bán cổ phiếu lần đầu ra công chúng (IPO) là mức vốn điều lệ đã góp tại thời điểm đăng ký chào bán:",
  "Từ 30 tỷ đồng trở lên tính theo giá trị ghi trên sổ kế toán",
  ["Từ 10 tỷ đồng trở lên tính theo giá trị ghi trên sổ kế toán",
   "Từ 50 tỷ đồng trở lên tính theo giá thị trường",
   "Trên 100 tỷ đồng tính theo báo cáo tài chính hợp nhất"],
  "Điểm a khoản 1 Điều 15: vốn điều lệ đã góp tại thời điểm đăng ký chào bán từ 30 tỷ đồng trở lên tính theo giá trị ghi trên sổ kế toán. Mức 10 tỷ đồng là quy định của Luật Chứng khoán 2006 đã hết hiệu lực.",
  f"Điểm a khoản 1 Điều 15 {LCK}",
  "Mức vốn điều lệ đã góp tại thời điểm đăng ký chào bán từ 30 tỷ đồng trở lên tính theo giá trị ghi trên sổ kế toán")

q(T_CB, 2,
  "Điều kiện về kết quả kinh doanh đối với công ty cổ phần chào bán cổ phiếu lần đầu ra công chúng là gì?",
  "02 năm liền trước năm đăng ký có lãi, không có lỗ lũy kế",
  ["Năm liền trước năm đăng ký chào bán có lãi và không có lỗ lũy kế",
   "03 năm liên tục liền trước năm đăng ký chào bán có lãi",
   "02 năm liền trước có lãi, lỗ lũy kế không vượt quá 10% vốn điều lệ"],
  "IPO cổ phiếu đòi hỏi 02 năm liên tục liền trước năm đăng ký chào bán có lãi, đồng thời không có lỗ lũy kế tính đến năm đăng ký chào bán (điểm b khoản 1 Điều 15). Điều kiện 'năm liền trước có lãi' áp dụng cho chào bán thêm cổ phiếu và chào bán trái phiếu ra công chúng.",
  f"Điểm b khoản 1 Điều 15 {LCK}",
  "Hoạt động kinh doanh của 02 năm liên tục liền trước năm đăng ký chào bán phải có lãi, đồng thời không có lỗ lũy kế tính đến năm đăng ký chào bán")

q(T_CB, 2,
  "Công ty cổ phần B có vốn điều lệ 1.200 tỷ đồng đăng ký chào bán cổ phiếu lần đầu ra công chúng. Tỷ lệ tối thiểu số cổ phiếu có quyền biểu quyết của B phải được bán cho ít nhất 100 nhà đầu tư không phải là cổ đông lớn là:",
  "10%",
  ["15%", "20%", "25%"],
  "Điểm d khoản 1 Điều 15: tối thiểu 15% số cổ phiếu có quyền biểu quyết phải được bán cho ít nhất 100 nhà đầu tư không phải cổ đông lớn; nếu vốn điều lệ từ 1.000 tỷ đồng trở lên thì tỷ lệ tối thiểu là 10%. B có vốn điều lệ 1.200 tỷ đồng nên áp dụng 10%.",
  f"Điểm d khoản 1 Điều 15 {LCK}",
  "trường hợp vốn điều lệ của tổ chức phát hành từ 1.000 tỷ đồng trở lên, tỷ lệ tối thiểu là 10% số cổ phiếu có quyền biểu quyết của tổ chức phát hành")

q(T_CB, 2,
  "Khi chào bán cổ phiếu lần đầu ra công chúng, cổ đông lớn trước thời điểm chào bán của tổ chức phát hành phải cam kết:",
  "Cùng nắm giữ ít nhất 20% vốn điều lệ tối thiểu 01 năm từ ngày kết thúc chào bán",
  ["Mỗi cổ đông lớn nắm giữ toàn bộ cổ phần trong 03 năm kể từ ngày niêm yết",
   "Cùng nhau nắm giữ ít nhất 30% vốn điều lệ tối thiểu 06 tháng kể từ ngày chào bán",
   "Cùng nhau nắm giữ ít nhất 20% vốn điều lệ tối thiểu 01 năm kể từ ngày niêm yết"],
  "Điểm đ khoản 1 Điều 15: cổ đông lớn trước IPO phải cam kết cùng nhau nắm giữ ít nhất 20% vốn điều lệ tối thiểu 01 năm kể từ ngày kết thúc đợt chào bán (mốc tính là ngày kết thúc đợt chào bán, không phải ngày niêm yết).",
  f"Điểm đ khoản 1 Điều 15 {LCK}",
  "phải cam kết cùng nhau nắm giữ ít nhất 20% vốn điều lệ của tổ chức phát hành tối thiểu là 01 năm kể từ ngày kết thúc đợt chào bán")

q(T_CB, 3,
  "Công ty đại chúng C có 50 triệu cổ phiếu đang lưu hành (mệnh giá 10.000 đồng). C dự kiến chào bán thêm ra công chúng 60 triệu cổ phiếu để huy động vốn, không có bảo lãnh phát hành, không phải phát hành để hoán đổi, hợp nhất, sáp nhập. Phương án của C:",
  "Không đáp ứng vì giá trị phát hành thêm theo mệnh giá vượt cổ phiếu đang lưu hành",
  ["Đáp ứng vì luật không giới hạn số lượng cổ phiếu chào bán thêm ra công chúng",
   "Đáp ứng nếu bán được tối thiểu 70% số cổ phiếu dự kiến chào bán",
   "Không đáp ứng vì chỉ được chào bán thêm tối đa 50% số cổ phiếu đang lưu hành"],
  "Điểm c khoản 2 Điều 15: giá trị cổ phiếu phát hành thêm theo mệnh giá không lớn hơn tổng giá trị cổ phiếu đang lưu hành theo mệnh giá, trừ trường hợp có bảo lãnh phát hành cam kết nhận mua toàn bộ hoặc mua số còn lại, phát hành từ nguồn vốn chủ sở hữu, phát hành để hoán đổi, hợp nhất, sáp nhập. 600 tỷ > 500 tỷ đồng nên không đáp ứng.",
  f"Điểm c khoản 2 Điều 15 {LCK}",
  "Giá trị cổ phiếu phát hành thêm theo mệnh giá không lớn hơn tổng giá trị cổ phiếu đang lưu hành tính theo mệnh giá")

q(T_CB, 3,
  "Công ty đại chúng D chào bán thêm cổ phiếu ra công chúng cho cổ đông hiện hữu theo tỷ lệ sở hữu nhằm huy động vốn thực hiện dự án nhà máy. Theo Luật Chứng khoán sửa đổi năm 2024, yêu cầu số cổ phiếu bán được tối thiểu 70% số cổ phiếu dự kiến chào bán:",
  "Không áp dụng đối với đợt chào bán cho cổ đông hiện hữu theo tỷ lệ sở hữu",
  ["Vẫn áp dụng, đợt chào bán bị hủy bỏ nếu bán được dưới 70%",
   "Được thay bằng tỷ lệ tối thiểu 50% đối với chào bán cho cổ đông hiện hữu",
   "Chỉ áp dụng khi đợt chào bán có tổ chức bảo lãnh phát hành"],
  "Điểm d khoản 2 Điều 15 (sửa đổi bởi điểm a khoản 6 Điều 1 Luật 56/2024/QH15): đợt chào bán để huy động vốn thực hiện dự án phải bán tối thiểu 70% số cổ phiếu dự kiến chào bán, trừ trường hợp chào bán cho các cổ đông hiện hữu theo tỷ lệ sở hữu; tổ chức phát hành phải có phương án bù đắp phần vốn thiếu hụt.",
  f"Điểm d khoản 2 Điều 15 {LCK}{SD}",
  "phải đạt tối thiểu 70% số cổ phiếu dự kiến được chào bán, trừ trường hợp chào bán cho các cổ đông hiện hữu theo tỷ lệ sở hữu.")

q(T_CB, 2,
  "Theo điểm g khoản 3 Điều 15 Luật Chứng khoán (sửa đổi bởi Luật 56/2024/QH15), doanh nghiệp chào bán trái phiếu ra công chúng phải đáp ứng quy định của Chính phủ về những nội dung nào?",
  "Đại diện người sở hữu trái phiếu, hệ số nợ, giá trị phát hành/VCSH, xếp hạng tín nhiệm",
  ["Tỷ lệ an toàn vốn, hạn mức tín dụng, tài sản bảo đảm và bảo hiểm trái phiếu",
   "Bảo lãnh thanh toán của ngân hàng và tài khoản phong tỏa tại Ngân hàng Nhà nước",
   "Tỷ lệ sở hữu nước ngoài, cơ cấu cổ đông và vốn điều lệ tối thiểu 100 tỷ đồng"],
  "Luật 56/2024/QH15 sửa điểm g khoản 3 Điều 15: tổ chức phát hành phải đáp ứng quy định của Chính phủ về đại diện người sở hữu trái phiếu, hệ số nợ, giá trị phát hành trên vốn chủ sở hữu và xếp hạng tín nhiệm. NĐ 245/2025 cụ thể hóa: nợ phải trả (gồm trái phiếu dự kiến phát hành) không quá 05 lần vốn chủ sở hữu (trừ một số loại hình), bắt buộc xếp hạng tín nhiệm (trừ trường hợp ngoại lệ).",
  f"Điểm g khoản 3 Điều 15 {LCK}{SD}; Điều 19 NĐ 155/2020/NĐ-CP (sửa đổi bởi NĐ 245/2025/NĐ-CP)",
  "Đáp ứng quy định của Chính phủ về đại diện người sở hữu trái phiếu, hệ số nợ, giá trị phát hành trên vốn chủ sở hữu và xếp hạng tín nhiệm")

q(T_CB, 2,
  "Trường hợp nào sau đây KHÔNG phải đăng ký chào bán chứng khoán ra công chúng với Ủy ban Chứng khoán Nhà nước?",
  "Chào bán trái phiếu chính quyền địa phương",
  ["Công ty đại chúng chào bán thêm cổ phiếu ra công chúng",
   "Công ty quản lý quỹ chào bán chứng chỉ quỹ đóng ra công chúng",
   "Ngân hàng thương mại cổ phần chào bán trái phiếu ra công chúng"],
  "Khoản 2 Điều 16 miễn đăng ký đối với: công cụ nợ của Chính phủ, trái phiếu được Chính phủ bảo lãnh do ngân hàng chính sách phát hành, trái phiếu chính quyền địa phương; trái phiếu của tổ chức tài chính quốc tế được Chính phủ chấp thuận; cổ phần hóa doanh nghiệp nhà nước; bán chứng khoán theo bản án, quyết định của Tòa án, Trọng tài hoặc trong phá sản.",
  f"Điểm a khoản 2 Điều 16 {LCK}",
  "Chào bán công cụ nợ của Chính phủ, trái phiếu được Chính phủ bảo lãnh do ngân hàng chính sách phát hành, trái phiếu chính quyền địa phương")

q(T_CB, 2,
  "Tổ chức bảo lãnh phát hành chứng khoán ra công chúng theo phương thức nhận mua một phần hoặc toàn bộ chứng khoán chỉ được bảo lãnh tổng giá trị chứng khoán:",
  "Không lớn hơn vốn chủ sở hữu và không quá 15 lần hiệu số tài sản ngắn hạn trừ nợ ngắn hạn",
  ["Không lớn hơn vốn điều lệ và không quá 10 lần hiệu số tài sản ngắn hạn trừ nợ ngắn hạn",
   "Không quá 02 lần vốn chủ sở hữu theo báo cáo tài chính năm gần nhất",
   "Không quá 15 lần vốn chủ sở hữu theo báo cáo tài chính quý gần nhất"],
  "Khoản 2 Điều 17: tổng giá trị bảo lãnh không lớn hơn vốn chủ sở hữu và không quá 15 lần hiệu số giữa giá trị tài sản ngắn hạn và nợ ngắn hạn tính theo báo cáo tài chính quý gần nhất. Hai giới hạn áp dụng đồng thời.",
  f"Khoản 2 Điều 17 {LCK}",
  "chỉ được phép bảo lãnh phát hành tổng giá trị chứng khoán không được lớn hơn vốn chủ sở hữu và không quá 15 lần hiệu số giữa giá trị tài sản ngắn hạn và nợ ngắn hạn tính theo báo cáo tài chính quý gần nhất")

q(T_CB, 3,
  "Công ty chứng khoán E (không phải người có liên quan của tổ chức phát hành) có số liệu theo báo cáo tài chính quý gần nhất: vốn chủ sở hữu 800 tỷ đồng, tài sản ngắn hạn 1.500 tỷ đồng, nợ ngắn hạn 1.450 tỷ đồng. Tổng giá trị chứng khoán tối đa E được bảo lãnh phát hành ra công chúng theo hình thức nhận mua là:",
  "750 tỷ đồng",
  ["800 tỷ đồng", "1.550 tỷ đồng", "12.000 tỷ đồng"],
  "Bước 1: hiệu số TSNH − nợ NH = 1.500 − 1.450 = 50 tỷ; giới hạn 15 lần = 15 × 50 = 750 tỷ. Bước 2: giới hạn vốn chủ sở hữu = 800 tỷ. Bước 3: áp dụng đồng thời hai giới hạn → mức tối đa = min(750; 800) = 750 tỷ đồng. 800 tỷ là chỉ xét VCSH; 1.550 tỷ là cộng hai giới hạn; 12.000 tỷ là nhân 15 với VCSH.",
  f"Khoản 2 Điều 17 {LCK}",
  "không quá 15 lần hiệu số giữa giá trị tài sản ngắn hạn và nợ ngắn hạn tính theo báo cáo tài chính quý gần nhất")

q(T_CB, 1,
  "Tổ chức phát hành phải hoàn thành việc phân phối chứng khoán ra công chúng trong thời hạn nào kể từ ngày Giấy chứng nhận đăng ký chào bán có hiệu lực?",
  "90 ngày; UBCKNN có thể xem xét gia hạn tối đa không quá 30 ngày",
  ["60 ngày; UBCKNN có thể xem xét gia hạn tối đa không quá 30 ngày",
   "90 ngày; UBCKNN có thể xem xét gia hạn tối đa không quá 60 ngày",
   "30 ngày; UBCKNN có thể xem xét gia hạn tối đa không quá 15 ngày"],
  "Khoản 4 Điều 26: thời hạn phân phối 90 ngày kể từ ngày Giấy chứng nhận có hiệu lực, gia hạn tối đa không quá 30 ngày; nếu chào bán nhiều đợt thì khoảng cách giữa các đợt không quá 12 tháng. Thời hạn đăng ký mua tối thiểu cho nhà đầu tư là 20 ngày.",
  f"Khoản 4 Điều 26 {LCK}",
  "Tổ chức phát hành phải hoàn thành việc phân phối chứng khoán trong thời hạn 90 ngày kể từ ngày Giấy chứng nhận đăng ký chào bán chứng khoán ra công chúng có hiệu lực.")

q(T_CB, 2,
  "Trong thời hạn 07 ngày làm việc kể từ ngày Giấy chứng nhận đăng ký chào bán chứng khoán ra công chúng có hiệu lực, tổ chức phát hành phải công bố Bản thông báo phát hành bằng cách nào?",
  "Trên 01 tờ báo điện tử hoặc báo in trong 03 số liên tiếp",
  ["Trên 02 tờ báo in trong 05 số liên tiếp",
   "Chỉ trên trang thông tin điện tử của Ủy ban Chứng khoán Nhà nước",
   "Trên 01 tờ báo in trong 01 số và niêm yết tại trụ sở công ty"],
  "Khoản 3 Điều 25: trong 07 ngày làm việc kể từ ngày Giấy chứng nhận có hiệu lực, tổ chức phát hành công bố Bản thông báo phát hành trên 01 tờ báo điện tử hoặc báo in trong 03 số liên tiếp; chứng khoán chỉ được chào bán sau khi đã công bố.",
  f"Khoản 3, 4 Điều 25 {LCK}",
  "tổ chức phát hành phải công bố Bản thông báo phát hành trên 01 tờ báo điện tử hoặc báo in trong 03 số liên tiếp")

q(T_CB, 3,
  "Công ty F kết thúc đợt chào bán cổ phiếu ra công chúng tháng 3/2026; cổ phiếu được đưa vào niêm yết từ tháng 5/2026. Tháng 9/2026, UBCKNN phát hiện hồ sơ đăng ký chào bán có thông tin sai lệch. Theo Luật Chứng khoán sửa đổi năm 2024, đợt chào bán:",
  "Không bị hủy bỏ vì cổ phiếu đã được đưa vào niêm yết",
  ["Bị hủy bỏ, F phải thu hồi cổ phiếu và hoàn tiền trong 15 ngày",
   "Bị đình chỉ tối đa 60 ngày để F khắc phục thiếu sót",
   "Bị Sở giao dịch chứng khoán hủy niêm yết đồng thời hủy bỏ đợt chào bán"],
  "Luật 56/2024 bổ sung điểm d khoản 1 Điều 28 (hủy bỏ khi phát hiện vi phạm sau khi kết thúc đợt chào bán nhưng cổ phiếu CHƯA niêm yết/đăng ký giao dịch) và khoản 2a Điều 28: cổ phiếu đã được đưa vào niêm yết hoặc đăng ký giao dịch thì không hủy bỏ đợt chào bán; vi phạm được xử lý theo quy định khác.",
  f"Điểm d khoản 1, khoản 2a Điều 28 {LCK}{SD}",
  "Sau khi chào bán ra công chúng, cổ phiếu hoặc cổ phiếu được chuyển đổi từ trái phiếu chuyển đổi hoặc cổ phiếu được mua từ chứng quyền đã được đưa vào niêm yết hoặc đăng ký giao dịch thì không hủy bỏ.")

# ---------------- Chào bán riêng lẻ (5) ----------------
q(T_RL, 2,
  "Đối tượng được tham gia đợt chào bán cổ phiếu riêng lẻ của công ty đại chúng gồm:",
  "Chỉ nhà đầu tư chiến lược và nhà đầu tư chứng khoán chuyên nghiệp",
  ["Bất kỳ nhà đầu tư nào, miễn là dưới 100 nhà đầu tư",
   "Chỉ cổ đông hiện hữu theo tỷ lệ sở hữu",
   "Nhà đầu tư chiến lược, nhà đầu tư chuyên nghiệp và người lao động"],
  "Điểm b khoản 1 Điều 31 (sửa đổi bởi Luật 56/2024): đối tượng tham gia đợt chào bán cổ phiếu, trái phiếu chuyển đổi riêng lẻ chỉ bao gồm nhà đầu tư chiến lược, nhà đầu tư chứng khoán chuyên nghiệp theo khoản 1 Điều 11.",
  f"Điểm b khoản 1 Điều 31 {LCK}{SD}",
  "Đối tượng tham gia đợt chào bán chỉ bao gồm nhà đầu tư chiến lược, nhà đầu tư chứng khoán chuyên nghiệp theo quy định tại khoản 1 Điều 11 của Luật này đối với đợt chào bán cổ phiếu, trái phiếu chuyển đổi")

q(T_RL, 3,
  "Công ty đại chúng G hoàn thành đợt chào bán cổ phiếu riêng lẻ ngày 15/3/2026 cho Quỹ đầu tư H (nhà đầu tư chứng khoán chuyên nghiệp) và Tập đoàn K (nhà đầu tư chiến lược). Ngoài các trường hợp ngoại lệ, mỗi bên được chuyển nhượng số cổ phiếu này sớm nhất từ khi nào?",
  "Quỹ H từ 15/3/2027; Tập đoàn K từ 15/3/2029",
  ["Quỹ H và Tập đoàn K đều từ 15/3/2027",
   "Quỹ H từ 15/9/2026; Tập đoàn K từ 15/3/2027",
   "Quỹ H từ 15/3/2029; Tập đoàn K từ 15/3/2027"],
  "Điểm c khoản 1 Điều 31: cổ phiếu chào bán riêng lẻ bị hạn chế chuyển nhượng tối thiểu 03 năm đối với nhà đầu tư chiến lược và tối thiểu 01 năm đối với nhà đầu tư chứng khoán chuyên nghiệp kể từ ngày hoàn thành đợt chào bán (trừ chuyển nhượng giữa các nhà đầu tư chuyên nghiệp, theo bản án, quyết định của Tòa án, Trọng tài hoặc thừa kế).",
  f"Điểm c khoản 1 Điều 31 {LCK}{SD}",
  "bị hạn chế tối thiểu là 03 năm đối với nhà đầu tư chiến lược và tối thiểu là 01 năm đối với nhà đầu tư chứng khoán chuyên nghiệp kể từ ngày hoàn thành đợt chào bán")

q(T_RL, 1,
  "Các đợt chào bán cổ phiếu riêng lẻ, trái phiếu chuyển đổi riêng lẻ, trái phiếu kèm chứng quyền riêng lẻ của công ty đại chúng phải cách nhau ít nhất bao lâu kể từ ngày kết thúc đợt chào bán gần nhất?",
  "06 tháng", ["03 tháng", "12 tháng", "01 tháng"],
  "Điểm d khoản 1 Điều 31: các đợt chào bán cổ phiếu, trái phiếu chuyển đổi, trái phiếu kèm chứng quyền riêng lẻ phải cách nhau ít nhất 06 tháng kể từ ngày kết thúc đợt chào bán gần nhất.",
  f"Điểm d khoản 1 Điều 31 {LCK}",
  "phải cách nhau ít nhất 06 tháng kể từ ngày kết thúc đợt chào bán gần nhất")

q(T_RL, 1,
  "Theo Điều 31a Luật Chứng khoán (bổ sung bởi Luật 56/2024/QH15), UBCKNN có quyền đình chỉ đợt chào bán chứng khoán riêng lẻ đã đăng ký với UBCKNN tối đa bao lâu?",
  "60 ngày", ["30 ngày", "90 ngày", "45 ngày"],
  "Điều 31a (mới): UBCKNN đình chỉ đợt chào bán riêng lẻ tối đa 60 ngày khi hồ sơ có thông tin sai lệch, bỏ sót nội dung quan trọng hoặc việc phân phối không đúng quy định — tương tự cơ chế đình chỉ chào bán ra công chúng tại Điều 27.",
  f"Khoản 1 Điều 31a {LCK}{SD}",
  "Ủy ban Chứng khoán Nhà nước có quyền đình chỉ đợt chào bán chứng khoán riêng lẻ đã đăng ký với Ủy ban Chứng khoán Nhà nước tối đa là 60 ngày")

q(T_RL, 3,
  "Công ty đại chúng M đã kết thúc đợt chào bán trái phiếu riêng lẻ. Sau đó UBCKNN phát hiện hồ sơ có thông tin sai lệch gây thiệt hại cho nhà đầu tư và quyết định hủy bỏ đợt chào bán. Nghĩa vụ của M là:",
  "Công bố việc hủy bỏ, thu hồi trái phiếu và hoàn tiền trong 15 ngày kể từ ngày bị hủy bỏ",
  ["Chỉ công bố thông tin, không phải hoàn tiền vì trái phiếu đã phát hành xong",
   "Công bố việc hủy bỏ trong 15 ngày và hoàn tiền trong 30 ngày kể từ ngày nhà đầu tư yêu cầu",
   "Hoàn tiền cho nhà đầu tư trong 90 ngày và được miễn bồi thường thiệt hại"],
  "Điều 31b (bổ sung bởi Luật 56/2024): UBCKNN hủy bỏ đợt chào bán trái phiếu riêng lẻ khi phát hiện vi phạm sau khi kết thúc đợt chào bán. Trong 07 ngày làm việc tổ chức phát hành công bố việc hủy bỏ, thu hồi chứng khoán và hoàn trả tiền trong 15 ngày kể từ ngày đợt chào bán bị hủy bỏ; quá hạn phải bồi thường thiệt hại.",
  f"Điểm c khoản 1, khoản 4 Điều 31b {LCK}{SD}",
  "phải thu hồi chứng khoán đã phát hành, đồng thời hoàn trả tiền cho nhà đầu tư trong thời hạn 15 ngày kể từ ngày đợt chào bán bị hủy bỏ")

# ---------------- Công ty đại chúng (14) ----------------
q(T_DC, 1,
  "Theo điểm a khoản 1 Điều 32 Luật Chứng khoán (sửa đổi bởi Luật 56/2024/QH15), công ty cổ phần có vốn điều lệ đã góp từ 30 tỷ đồng và có tối thiểu 10% số cổ phiếu có quyền biểu quyết do ít nhất 100 nhà đầu tư không phải cổ đông lớn nắm giữ còn phải đáp ứng thêm điều kiện nào để là công ty đại chúng?",
  "Vốn chủ sở hữu từ 30 tỷ đồng trở lên",
  ["Vốn chủ sở hữu từ 50 tỷ đồng trở lên",
   "Có ít nhất 02 năm liên tục kinh doanh có lãi",
   "Đã niêm yết hoặc đăng ký giao dịch cổ phiếu"],
  "Luật 56/2024 bổ sung tiêu chí vốn chủ sở hữu từ 30 tỷ đồng trở lên (hiệu lực từ 01/01/2026) bên cạnh vốn điều lệ đã góp từ 30 tỷ đồng và cơ cấu cổ đông. Luật không đòi hỏi điều kiện lãi 02 năm (đó là điều kiện IPO) hay phải niêm yết trước; việc đăng ký giao dịch là nghĩa vụ phát sinh sau khi trở thành công ty đại chúng.",
  f"Điểm a khoản 1 Điều 32 {LCK}{SD}",
  "Công ty có vốn điều lệ đã góp từ 30 tỷ đồng trở lên, có vốn chủ sở hữu từ 30 tỷ đồng trở lên và có tối thiểu 10% số cổ phiếu có quyền biểu quyết do ít nhất 100 nhà đầu tư không phải cổ đông lớn nắm giữ")

q(T_DC, 3,
  "Công ty cổ phần N có vốn điều lệ đã góp 45 tỷ đồng; 300 cổ đông nhỏ (không phải cổ đông lớn) nắm 40% cổ phiếu có quyền biểu quyết. Báo cáo tài chính năm 2025 được kiểm toán cho thấy vốn chủ sở hữu của N chỉ còn 25 tỷ đồng do lỗ lũy kế. Tại tháng 11/2026, nhận định nào đúng?",
  "N không đáp ứng điều kiện công ty đại chúng vì vốn chủ sở hữu dưới 30 tỷ đồng",
  ["N vẫn đáp ứng vì chỉ cần vốn điều lệ đã góp từ 30 tỷ đồng trở lên",
   "N vẫn đáp ứng vì tiêu chí vốn chủ sở hữu chỉ có hiệu lực từ năm 2027",
   "N không đáp ứng vì cổ đông nhỏ phải nắm tối thiểu 50% cổ phiếu có quyền biểu quyết"],
  "Tiêu chí vốn chủ sở hữu từ 30 tỷ đồng tại điểm a khoản 1 Điều 32 (Luật 56/2024) có hiệu lực từ 01/01/2026. N có VCSH 25 tỷ nên không đáp ứng; theo Điều 38, công ty phải báo cáo UBCKNN trong 15 ngày và sau 01 năm vẫn không đáp ứng thì bị xem xét hủy tư cách công ty đại chúng. Cơ cấu cổ đông chỉ yêu cầu tối thiểu 10%.",
  f"Điểm a khoản 1 Điều 32; khoản 2 Điều 38 {LCK}{SD}; khoản 2 Điều 10 Luật 56/2024/QH15",
  "đối với quy định về vốn chủ sở hữu có hiệu lực kể từ ngày 01 tháng 01 năm 2026.")

q(T_DC, 1,
  "Công ty cổ phần đáp ứng điều kiện tại điểm a khoản 1 Điều 32 Luật Chứng khoán phải nộp hồ sơ đăng ký công ty đại chúng cho UBCKNN trong thời hạn nào?",
  "90 ngày kể từ ngày hoàn thành việc góp vốn và có cơ cấu cổ đông đáp ứng quy định",
  ["30 ngày kể từ ngày hoàn thành việc góp vốn và có cơ cấu cổ đông đáp ứng quy định",
   "60 ngày kể từ ngày được cấp Giấy chứng nhận đăng ký doanh nghiệp",
   "15 ngày kể từ ngày Đại hội đồng cổ đông thông qua"],
  "Khoản 2 Điều 32: thời hạn nộp hồ sơ là 90 ngày kể từ ngày công ty hoàn thành việc góp vốn và có cơ cấu cổ đông đáp ứng điều kiện. UBCKNN xác nhận hoàn tất đăng ký trong 15 ngày kể từ ngày nhận hồ sơ đầy đủ, hợp lệ.",
  f"Khoản 2, 3 Điều 32 {LCK}",
  "trong thời hạn 90 ngày kể từ ngày công ty hoàn thành việc góp vốn và có cơ cấu cổ đông đáp ứng quy định tại điểm a khoản 1 Điều này")

q(T_DC, 2,
  "Công ty đại chúng hình thành theo điểm a khoản 1 Điều 32 (không qua IPO) phải đăng ký giao dịch cổ phiếu trên hệ thống giao dịch cho chứng khoán chưa niêm yết trong thời hạn nào?",
  "30 ngày kể từ ngày UBCKNN xác nhận hoàn tất đăng ký công ty đại chúng",
  ["90 ngày kể từ ngày nộp hồ sơ đăng ký công ty đại chúng cho UBCKNN",
   "01 năm kể từ ngày đáp ứng đủ điều kiện là công ty đại chúng",
   "30 ngày kể từ ngày được cấp Giấy chứng nhận đăng ký doanh nghiệp"],
  "Điểm d khoản 1 Điều 34: đăng ký giao dịch trong 30 ngày kể từ ngày UBCKNN xác nhận hoàn tất đăng ký công ty đại chúng; sau 02 năm kể từ ngày giao dịch đầu tiên trên hệ thống chứng khoán chưa niêm yết, công ty có quyền nộp hồ sơ niêm yết nếu đáp ứng điều kiện.",
  f"Điểm d khoản 1 Điều 34 {LCK}",
  "phải đăng ký giao dịch cổ phiếu trên hệ thống giao dịch cho chứng khoán chưa niêm yết trong thời hạn 30 ngày kể từ ngày Ủy ban Chứng khoán Nhà nước xác nhận hoàn tất việc đăng ký công ty đại chúng")

q(T_DC, 1,
  "Tổ chức, cá nhân và người có liên quan dự kiến mua cổ phiếu có quyền biểu quyết đang lưu hành dẫn đến sở hữu đạt từ bao nhiêu phần trăm trở lên số cổ phiếu có quyền biểu quyết của 01 công ty đại chúng thì phải chào mua công khai?",
  "25%", ["20%", "35%", "51%"],
  "Điểm a khoản 1 Điều 35: ngưỡng chào mua công khai đầu tiên là sở hữu đạt từ 25% trở lên; với người đã nắm từ 25%, mua tiếp đạt hoặc vượt 35%, 45%, 55%, 65%, 75% cũng phải chào mua công khai.",
  f"Điểm a khoản 1 Điều 35 {LCK}",
  "dẫn đến trực tiếp hoặc gián tiếp sở hữu đạt từ 25% trở lên số cổ phiếu có quyền biểu quyết của 01 công ty đại chúng")

q(T_DC, 3,
  "Công ty Q cùng người có liên quan đang nắm 30% cổ phiếu có quyền biểu quyết của công ty đại chúng R. Q dự kiến mua thêm 6% cổ phiếu R đang lưu hành qua giao dịch khớp lệnh (không thuộc trường hợp miễn trừ). Nhận định nào đúng?",
  "Q phải chào mua công khai vì tỷ lệ sở hữu sau giao dịch vượt mức 35%",
  ["Q không phải chào mua công khai vì đã vượt ngưỡng 25% từ trước",
   "Q chỉ phải chào mua công khai khi sở hữu đạt từ 51% trở lên",
   "Q không phải chào mua công khai vì giao dịch qua phương thức khớp lệnh"],
  "Điểm b khoản 1 Điều 35: người đang nắm từ 25% trở lên dự kiến mua tiếp dẫn đến sở hữu đạt hoặc vượt các mức 35%, 45%, 55%, 65%, 75% phải chào mua công khai. 30% + 6% = 36% > 35% nên phải chào mua công khai; phương thức giao dịch không phải căn cứ miễn trừ.",
  f"Điểm b khoản 1, khoản 2 Điều 35 {LCK}",
  "dự kiến mua tiếp dẫn đến trực tiếp hoặc gián tiếp sở hữu đạt hoặc vượt mức 35%, 45%, 55%, 65%, 75% số cổ phiếu có quyền biểu quyết")

q(T_DC, 2,
  "Trường hợp nào sau đây KHÔNG phải chào mua công khai dù tỷ lệ sở hữu đạt ngưỡng quy định tại khoản 1 Điều 35 Luật Chứng khoán?",
  "Nhận thừa kế cổ phiếu dẫn đến sở hữu 30% cổ phiếu có quyền biểu quyết",
  ["Mua thỏa thuận từ một cổ đông dẫn đến sở hữu 28%, chưa được ĐHĐCĐ thông qua",
   "Mua liên tục qua khớp lệnh trên sàn dẫn đến sở hữu 26%",
   "Nhóm người có liên quan cùng mua dẫn đến tổng sở hữu của nhóm đạt 25%"],
  "Khoản 2 Điều 35 liệt kê các trường hợp miễn chào mua công khai, trong đó có tặng cho, thừa kế cổ phiếu, chứng chỉ quỹ đóng. Nhận chuyển nhượng chỉ được miễn khi đã được ĐHĐCĐ thông qua và xác định rõ đối tượng; sở hữu của nhóm người có liên quan được cộng gộp.",
  f"Điểm e khoản 2 Điều 35 {LCK}",
  "Tặng cho, thừa kế cổ phiếu, chứng chỉ quỹ đóng;")

q(T_DC, 2,
  "Sau khi thực hiện chào mua công khai (không phải chào mua toàn bộ), tổ chức cùng người có liên quan nắm giữ từ 80% trở lên số cổ phiếu có quyền biểu quyết của công ty đại chúng thì phải:",
  "Mua tiếp cổ phiếu của cổ đông còn lại trong 30 ngày, giá và cách thanh toán như đợt chào mua",
  ["Được quyền buộc cổ đông còn lại bán cổ phiếu theo giá do Hội đồng quản trị quyết định",
   "Làm thủ tục hủy tư cách công ty đại chúng trong 30 ngày kể từ ngày kết thúc chào mua",
   "Mua tiếp cổ phiếu của cổ đông còn lại trong 90 ngày theo giá thị trường tại thời điểm mua"],
  "Điểm c khoản 1 Điều 35: sau chào mua công khai, nếu nắm từ 80% trở lên thì phải mua tiếp số cổ phiếu do các cổ đông còn lại nắm giữ trong 30 ngày theo điều kiện giá chào mua và phương thức thanh toán tương tự đợt chào mua (bảo vệ cổ đông thiểu số).",
  f"Điểm c khoản 1 Điều 35 {LCK}",
  "phải mua tiếp số cổ phiếu, chứng chỉ quỹ đóng do các cổ đông, nhà đầu tư còn lại nắm giữ trong thời hạn 30 ngày theo các điều kiện về giá chào mua và phương thức thanh toán tương tự với đợt chào mua công khai")

q(T_DC, 2,
  "Nguồn nào sau đây KHÔNG được sử dụng để công ty đại chúng mua lại cổ phiếu của chính mình theo khoản 1 Điều 36 Luật Chứng khoán?",
  "Khoản vay ngắn hạn ngân hàng",
  ["Thặng dư vốn cổ phần của công ty", "Quỹ đầu tư phát triển của công ty", "Lợi nhuận sau thuế chưa phân phối"],
  "Điểm b khoản 1 Điều 36: nguồn mua lại gồm thặng dư vốn cổ phần, quỹ đầu tư phát triển, lợi nhuận sau thuế chưa phân phối, quỹ khác thuộc vốn chủ sở hữu được sử dụng để bổ sung vốn điều lệ. Vốn vay không thuộc vốn chủ sở hữu.",
  f"Điểm b khoản 1 Điều 36 {LCK}",
  "thặng dư vốn cổ phần, quỹ đầu tư phát triển, lợi nhuận sau thuế chưa phân phối, quỹ khác thuộc vốn chủ sở hữu được sử dụng để bổ sung vốn điều lệ theo quy định của pháp luật")

q(T_DC, 3,
  "Công ty đại chúng S báo cáo kết quả đợt mua lại cổ phiếu (để giảm vốn điều lệ) ngày 10/02/2026. Ngày 01/6/2026, S muốn triển khai đợt mua lại mới không thuộc các trường hợp miễn trừ tại khoản 2 Điều 36. Nhận định nào đúng?",
  "Chưa được mua lại vì chưa đủ 06 tháng từ ngày báo cáo kết quả đợt trước",
  ["S được mua lại ngay nếu có nghị quyết Đại hội đồng cổ đông",
   "S được mua lại vì chỉ cần cách đợt trước tối thiểu 03 tháng",
   "S chưa được mua lại vì các đợt mua lại phải cách nhau tối thiểu 12 tháng"],
  "Điểm d khoản 3 Điều 36: công ty đại chúng không được mua lại cổ phiếu nếu đã thực hiện mua lại trong thời hạn 06 tháng kể từ ngày báo cáo kết quả mua lại (trừ trường hợp miễn trừ). Từ 10/02/2026 đến 01/6/2026 chưa đủ 06 tháng (sớm nhất từ 10/8/2026).",
  f"Điểm d khoản 3 Điều 36 {LCK}",
  "Đã thực hiện việc mua lại cổ phiếu của chính mình trong thời hạn 06 tháng kể từ ngày báo cáo kết quả mua lại")

q(T_DC, 2,
  "Theo khoản 6 Điều 36 Luật Chứng khoán (sửa đổi bởi Luật 56/2024/QH15), khi công ty mua lại cổ phiếu của người lao động theo quy chế phát hành cổ phiếu cho người lao động thì:",
  "Báo cáo tại ĐHĐCĐ thường niên gần nhất, không phải làm thủ tục giảm vốn điều lệ",
  ["Phải làm thủ tục giảm vốn điều lệ trong 10 ngày kể từ ngày báo cáo ĐHĐCĐ thường niên",
   "Phải được UBCKNN chấp thuận trước và giảm vốn điều lệ trong 30 ngày",
   "Phải hủy toàn bộ số cổ phiếu đã mua lại trong thời hạn 06 tháng"],
  "Luật 56/2024 sửa khoản 6 Điều 36: tổng số cổ phiếu của người lao động được mua lại phải báo cáo tại ĐHĐCĐ thường niên gần nhất; công ty không phải làm thủ tục giảm vốn điều lệ đối với số cổ phiếu này. Quy định cũ buộc giảm vốn điều lệ trong 10 ngày kể từ ngày báo cáo ĐHĐCĐ.",
  f"Khoản 6 Điều 36 {LCK}{SD}",
  "Công ty không phải làm thủ tục giảm vốn điều lệ đối với số cổ phiếu được công ty mua lại.")

q(T_DC, 2,
  "Công ty đại chúng T đã nhận được thông báo của UBCKNN về việc nhận đủ tài liệu báo cáo mua lại cổ phiếu và đã công bố thông tin theo quy định. Phát biểu nào đúng về thời gian thực hiện giao dịch mua lại của T?",
  "Mua sau 07 ngày làm việc kể từ ngày công bố; kết thúc trong 30 ngày kể từ ngày bắt đầu",
  ["Được mua lại ngay ngày làm việc kế tiếp sau ngày công bố; kết thúc tối đa 90 ngày",
   "Được mua lại sau 15 ngày kể từ ngày công bố thông tin; không giới hạn thời gian kết thúc",
   "Chỉ được mua lại sau khi UBCKNN cấp Giấy chứng nhận mua lại cổ phiếu"],
  "Khoản 4 Điều 37: công ty được thực hiện mua lại sau 07 ngày làm việc kể từ ngày công bố thông tin. Khoản 6 Điều 37: phải kết thúc theo thời gian đã công bố nhưng tối đa 30 ngày kể từ ngày bắt đầu giao dịch; báo cáo kết quả trong 10 ngày kể từ ngày kết thúc giao dịch.",
  f"Khoản 4, 6 Điều 37 {LCK}",
  "Công ty đại chúng được thực hiện mua lại cổ phiếu sau 07 ngày làm việc kể từ ngày công bố thông tin.")

q(T_DC, 2,
  "Theo Điều 38 Luật Chứng khoán (sửa đổi bởi Luật 56/2024/QH15), trường hợp nào sau đây công ty đại chúng bị hủy tư cách công ty đại chúng?",
  "Không công bố BCTC năm được kiểm toán trong 02 năm liên tục",
  ["Kết quả kinh doanh thua lỗ trong 02 năm tài chính liên tục gần nhất",
   "Chậm công bố báo cáo tài chính quý 02 lần trong cùng một năm tài chính",
   "Bị hủy niêm yết và chuyển sang đăng ký giao dịch trên hệ thống UPCoM"],
  "Khoản 1 Điều 38 (Luật 56/2024): hủy tư cách khi không còn đáp ứng điều kiện tại điểm a khoản 1 Điều 32; không công bố BCTC năm được kiểm toán hoặc nghị quyết ĐHĐCĐ thường niên trong 02 năm liên tục; hoặc trong 01 năm không đăng ký cổ phiếu tại VSDC/không đăng ký niêm yết, đăng ký giao dịch.",
  f"Điểm b khoản 1 Điều 38 {LCK}{SD}",
  "Không thực hiện công bố thông tin trong 02 năm liên tục về báo cáo tài chính năm được kiểm toán")

q(T_DC, 1,
  "Theo Điều 41 Luật Chứng khoán, Hội đồng quản trị công ty đại chúng phải tổ chức họp với tần suất tối thiểu nào?",
  "Mỗi quý 01 lần", ["Mỗi tháng 01 lần", "06 tháng 01 lần", "Mỗi năm 02 lần"],
  "Điểm c khoản 3 Điều 41: Hội đồng quản trị phải tổ chức họp ít nhất mỗi quý 01 lần theo trình tự, thủ tục tại Điều lệ công ty và Quy chế nội bộ về quản trị công ty.",
  f"Điểm c khoản 3 Điều 41 {LCK}",
  "Hội đồng quản trị phải tổ chức họp ít nhất mỗi quý 01 lần")

# ---------------- SGDCK & VSDC (7) ----------------
q(T_SG, 1,
  "Theo Luật Chứng khoán, Sở giao dịch chứng khoán Việt Nam là doanh nghiệp do Nhà nước nắm giữ:",
  "Trên 50% vốn điều lệ hoặc tổng số cổ phần có quyền biểu quyết",
  ["100% vốn điều lệ hoặc tổng số cổ phần có quyền biểu quyết",
   "Từ 65% vốn điều lệ hoặc tổng số cổ phần có quyền biểu quyết",
   "Từ 36% vốn điều lệ hoặc tổng số cổ phần có quyền biểu quyết"],
  "Khoản 1 Điều 43: SGDCK Việt Nam là doanh nghiệp thành lập và hoạt động theo Luật Chứng khoán và Luật Doanh nghiệp, do Nhà nước nắm giữ trên 50% vốn điều lệ hoặc tổng số cổ phần có quyền biểu quyết. VSDC cũng có quy định tương tự (Điều 52).",
  f"Khoản 1 Điều 43 {LCK}",
  "do Nhà nước nắm giữ trên 50% vốn điều lệ hoặc tổng số cổ phần có quyền biểu quyết")

q(T_SG, 1,
  "Cơ quan nào quyết định thành lập, giải thể, mô hình hoạt động, hình thức sở hữu của Sở giao dịch chứng khoán Việt Nam?",
  "Thủ tướng Chính phủ, theo đề nghị của Bộ trưởng Bộ Tài chính",
  ["Bộ trưởng Bộ Tài chính, theo đề nghị của Chủ tịch UBCKNN",
   "Chủ tịch Ủy ban Chứng khoán Nhà nước",
   "Quốc hội, theo đề nghị của Chính phủ"],
  "Khoản 2 Điều 43: Thủ tướng Chính phủ quyết định thành lập, giải thể, mô hình hoạt động, hình thức sở hữu, chức năng, quyền và nghĩa vụ của SGDCK Việt Nam và việc thành lập công ty con theo đề nghị của Bộ trưởng Bộ Tài chính.",
  f"Khoản 2 Điều 43 {LCK}",
  "Thủ tướng Chính phủ quyết định thành lập, giải thể, mô hình hoạt động, hình thức sở hữu, chức năng, quyền và nghĩa vụ của Sở giao dịch chứng khoán Việt Nam")

q(T_SG, 2,
  "Ngân hàng thương mại có thể trở thành loại thành viên nào của Sở giao dịch chứng khoán Việt Nam?",
  "Thành viên giao dịch đặc biệt",
  ["Thành viên giao dịch như công ty chứng khoán",
   "Thành viên lưu ký của Sở giao dịch chứng khoán",
   "Thành viên bù trừ của Sở giao dịch chứng khoán"],
  "Khoản 1 Điều 47: thành viên của SGDCK gồm thành viên giao dịch (công ty chứng khoán) và thành viên giao dịch đặc biệt (ngân hàng thương mại, chi nhánh ngân hàng nước ngoài và tổ chức khác được chấp thuận). Thành viên lưu ký, thành viên bù trừ là thành viên của VSDC (Điều 56).",
  f"Khoản 1 Điều 47 {LCK}",
  "Thành viên giao dịch đặc biệt là ngân hàng thương mại, chi nhánh ngân hàng nước ngoài và các tổ chức khác được Sở giao dịch chứng khoán Việt Nam chấp thuận trở thành thành viên giao dịch đặc biệt.")

q(T_SG, 2,
  "Chứng khoán niêm yết, đăng ký giao dịch có được giao dịch bên ngoài hệ thống giao dịch chứng khoán do SGDCK Việt Nam và công ty con tổ chức không?",
  "Không, trừ giao dịch không mang tính mua bán hoặc không thể qua hệ thống",
  ["Được, nếu hai bên lập hợp đồng chuyển nhượng có công chứng hợp lệ",
   "Được, nếu giá trị mỗi giao dịch dưới 100 triệu đồng và báo cáo SGDCK",
   "Không, trong mọi trường hợp kể cả thừa kế, tặng cho cổ phiếu"],
  "Khoản 2 Điều 50: chứng khoán niêm yết, đăng ký giao dịch không được giao dịch bên ngoài hệ thống, trừ giao dịch không mang tính chất mua bán (ví dụ thừa kế, tặng cho) hoặc giao dịch khác không thể thực hiện được thông qua hệ thống; Bộ trưởng Bộ Tài chính quy định chi tiết các trường hợp này.",
  f"Khoản 2, 4 Điều 50 {LCK}",
  "Chứng khoán niêm yết, đăng ký giao dịch không được giao dịch bên ngoài hệ thống giao dịch chứng khoán do Sở giao dịch chứng khoán Việt Nam và công ty con tổ chức, trừ trường hợp giao dịch không mang tính chất mua bán")

q(T_SG, 2,
  "Đối với chứng khoán đã lưu ký tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam (VSDC), việc chuyển quyền sở hữu chứng khoán có hiệu lực vào ngày nào?",
  "Ngày ghi sổ bút toán trên tài khoản lưu ký tại VSDC",
  ["Ngày khớp lệnh giao dịch trên hệ thống của SGDCK",
   "Ngày nhà đầu tư thanh toán đủ tiền cho công ty chứng khoán",
   "Ngày tổ chức phát hành ghi tên người mua vào sổ cổ đông"],
  "Khoản 2 Điều 64: chuyển quyền sở hữu chứng khoán đã lưu ký tại VSDC có hiệu lực vào ngày thực hiện bút toán ghi sổ trên tài khoản lưu ký tại VSDC; với chứng khoán đăng ký tập trung nhưng chưa lưu ký, hiệu lực vào ngày ghi Sổ đăng ký người sở hữu do VSDC quản lý.",
  f"Khoản 2 Điều 64 {LCK}",
  "việc chuyển quyền sở hữu chứng khoán có hiệu lực vào ngày thực hiện bút toán ghi sổ trên tài khoản lưu ký chứng khoán tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam")

q(T_SG, 1,
  "Ngân hàng thương mại V là thành viên bù trừ của VSDC. Đối với giao dịch chứng khoán phái sinh, V được thực hiện bù trừ, thanh toán giao dịch cho đối tượng nào?",
  "Chỉ cho chính ngân hàng V",
  ["Cho mọi nhà đầu tư mở tài khoản tại V",
   "Cho các công ty chứng khoán chưa là thành viên bù trừ",
   "Cho khách hàng là tổ chức, không cho khách hàng cá nhân"],
  "Điểm a khoản 4 Điều 56 (sửa đổi bởi Luật 56/2024): thành viên bù trừ là ngân hàng thương mại, chi nhánh ngân hàng nước ngoài khi bù trừ, thanh toán giao dịch chứng khoán phái sinh chỉ được thực hiện cho chính mình.",
  f"Điểm a khoản 4 Điều 56 {LCK}{SD}",
  "thành viên bù trừ là ngân hàng thương mại, chi nhánh ngân hàng nước ngoài chỉ được thực hiện bù trừ, thanh toán giao dịch cho chính thành viên bù trừ là ngân hàng thương mại, chi nhánh ngân hàng nước ngoài")

q(T_SG, 3,
  "Ngân hàng thương mại W có vốn điều lệ 9.500 tỷ đồng, kinh doanh có lãi 03 năm liên tục, đáp ứng tỷ lệ an toàn vốn tối thiểu và các yêu cầu kỹ thuật kết nối với VSDC, NHNN. W muốn được UBCKNN lựa chọn làm ngân hàng thanh toán. Nhận định nào đúng?",
  "W chưa đủ điều kiện vì vốn điều lệ phải trên 10.000 tỷ đồng",
  ["W đủ điều kiện vì đã có lãi trong 02 năm gần nhất",
   "W chưa đủ điều kiện vì phải có lãi 05 năm liên tục",
   "W đủ điều kiện nếu được Ngân hàng Nhà nước chấp thuận"],
  "Khoản 2 Điều 69: ngân hàng thương mại được chọn làm ngân hàng thanh toán phải có vốn điều lệ trên 10.000 tỷ đồng, có lãi 02 năm gần nhất, đáp ứng tỷ lệ an toàn vốn, có hệ thống kết nối với VSDC và NHNN, lưu trữ dữ liệu ít nhất 10 năm. W thiếu điều kiện vốn điều lệ.",
  f"Điểm b khoản 2 Điều 69 {LCK}",
  "Có vốn điều lệ trên 10.000 tỷ đồng;")

# ---------------- CTCK & CTQLQ (9) ----------------
q(T_CT, 1,
  "Nghiệp vụ nào sau đây KHÔNG thuộc nghiệp vụ kinh doanh của công ty chứng khoán theo Điều 72 Luật Chứng khoán?",
  "Quản lý quỹ đầu tư chứng khoán",
  ["Tư vấn đầu tư chứng khoán", "Bảo lãnh phát hành chứng khoán", "Tự doanh chứng khoán"],
  "Công ty chứng khoán được cấp phép một, một số hoặc toàn bộ nghiệp vụ: môi giới, tự doanh, bảo lãnh phát hành, tư vấn đầu tư chứng khoán. Quản lý quỹ đầu tư chứng khoán là nghiệp vụ của công ty quản lý quỹ (Điều 73).",
  f"Khoản 1 Điều 72 {LCK}",
  "Công ty chứng khoán được cấp phép thực hiện một, một số hoặc toàn bộ nghiệp vụ kinh doanh sau đây")

q(T_CT, 2,
  "Công ty chứng khoán X hiện chỉ được cấp phép nghiệp vụ môi giới chứng khoán và muốn bổ sung nghiệp vụ bảo lãnh phát hành. Nhận định nào đúng?",
  "Chỉ được cấp phép bảo lãnh khi X đã có nghiệp vụ tự doanh chứng khoán",
  ["X được cấp phép bảo lãnh phát hành ngay vì đã có nghiệp vụ môi giới",
   "X phải có nghiệp vụ tư vấn đầu tư chứng khoán mới được cấp phép bảo lãnh",
   "X không thể được cấp phép vì bảo lãnh phát hành chỉ dành cho ngân hàng"],
  "Khoản 2, 3 Điều 72: chỉ được cấp phép tự doanh khi đã có phép môi giới; chỉ được cấp phép bảo lãnh phát hành khi đã có phép tự doanh. Do đó X cần có nghiệp vụ tự doanh trước khi được cấp phép bảo lãnh phát hành.",
  f"Khoản 2, 3 Điều 72 {LCK}",
  "Công ty chứng khoán chỉ được cấp phép thực hiện nghiệp vụ bảo lãnh phát hành chứng khoán khi được cấp phép thực hiện nghiệp vụ tự doanh chứng khoán.")

q(T_CT, 2,
  "Phát biểu nào đúng về nghiệp vụ kinh doanh của công ty quản lý quỹ đầu tư chứng khoán theo Luật Chứng khoán?",
  "Quản lý quỹ, quản lý danh mục và tư vấn đầu tư, cấp chung trong Giấy phép",
  ["Gồm quản lý quỹ và môi giới chứng khoán, được cấp phép riêng từng nghiệp vụ",
   "Gồm quản lý quỹ, tự doanh và bảo lãnh phát hành chứng khoán",
   "Chỉ gồm quản lý quỹ; các nghiệp vụ khác phải đề nghị cấp phép bổ sung"],
  "Điều 73: công ty quản lý quỹ được thực hiện quản lý quỹ đầu tư chứng khoán, quản lý danh mục đầu tư chứng khoán, tư vấn đầu tư chứng khoán; các nghiệp vụ này được cấp chung trong Giấy phép thành lập và hoạt động kinh doanh chứng khoán.",
  f"Điều 73 {LCK}",
  "Các nghiệp vụ kinh doanh quy định tại khoản 1 Điều này được cấp chung trong Giấy phép thành lập và hoạt động kinh doanh chứng khoán của công ty quản lý quỹ đầu tư chứng khoán.")

q(T_CT, 3,
  "Nhóm sáng lập dự kiến thành lập công ty chứng khoán Z (công ty cổ phần) với cơ cấu: Công ty sản xuất A góp 40%, Ngân hàng thương mại B góp 20%, 05 cá nhân góp 40% vốn điều lệ. Cơ cấu này:",
  "Chưa đáp ứng tỷ lệ vốn góp tối thiểu của tổ chức và của ngân hàng, bảo hiểm",
  ["Đáp ứng vì đã có tối thiểu 02 cổ đông sáng lập là tổ chức góp vốn",
   "Đáp ứng vì các tổ chức nắm giữ trên 51% vốn điều lệ của công ty",
   "Chưa đáp ứng chỉ vì cá nhân không được góp vốn thành lập công ty chứng khoán"],
  "Khoản 3 Điều 74: tối thiểu 02 cổ đông sáng lập là tổ chức; tổng tỷ lệ vốn góp của các tổ chức tối thiểu 65% vốn điều lệ, trong đó doanh nghiệp bảo hiểm, ngân hàng thương mại sở hữu tối thiểu 30%. Z: tổ chức 60% < 65%, ngân hàng 20% < 30% nên không đạt. Cá nhân vẫn được góp vốn.",
  f"Khoản 3 Điều 74 {LCK}",
  "Tổng tỷ lệ vốn góp của các tổ chức tối thiểu là 65% vốn điều lệ, trong đó các tổ chức là doanh nghiệp bảo hiểm, ngân hàng thương mại sở hữu tối thiểu là 30% vốn điều lệ.")

q(T_CT, 1,
  "Theo Điều 74 Luật Chứng khoán, Tổng giám đốc (Giám đốc) công ty chứng khoán phải có loại chứng chỉ hành nghề nào?",
  "CCHN phân tích tài chính hoặc CCHN quản lý quỹ",
  ["CCHN môi giới chứng khoán hoặc CCHN phân tích tài chính",
   "Bất kỳ loại CCHN chứng khoán nào do UBCKNN cấp",
   "Chỉ CCHN quản lý quỹ, không chấp nhận loại khác"],
  "Điểm c khoản 5 Điều 74: Tổng giám đốc công ty chứng khoán phải có CCHN phân tích tài chính hoặc CCHN quản lý quỹ, có tối thiểu 02 năm kinh nghiệm và không bị xử phạt VPHC trong lĩnh vực chứng khoán trong 06 tháng gần nhất.",
  f"Điểm c khoản 5 Điều 74 {LCK}",
  "Có chứng chỉ hành nghề phân tích tài chính hoặc chứng chỉ hành nghề quản lý quỹ;")

q(T_CT, 2,
  "Điều kiện nhân sự để cấp Giấy phép thành lập và hoạt động cho công ty quản lý quỹ đầu tư chứng khoán gồm:",
  "Tổng giám đốc, tối thiểu 05 nhân viên có CCHN quản lý quỹ và 01 nhân viên kiểm soát tuân thủ",
  ["Tổng giám đốc, tối thiểu 03 nhân viên có CCHN quản lý quỹ và 01 nhân viên kiểm soát tuân thủ",
   "Tổng giám đốc, tối thiểu 05 nhân viên có CCHN bất kỳ và 01 nhân viên kiểm toán nội bộ",
   "Tổng giám đốc, tối thiểu 02 nhân viên có CCHN quản lý quỹ, không bắt buộc kiểm soát tuân thủ"],
  "Khoản 5 Điều 75: công ty quản lý quỹ phải có Tổng giám đốc, tối thiểu 05 nhân viên có CCHN quản lý quỹ và tối thiểu 01 nhân viên kiểm soát tuân thủ; Tổng giám đốc cần tối thiểu 04 năm kinh nghiệm. Con số 03 nhân viên/nghiệp vụ là điều kiện của công ty chứng khoán.",
  f"Khoản 5 Điều 75 {LCK}",
  "Có Tổng giám đốc (Giám đốc), tối thiểu 05 nhân viên có chứng chỉ hành nghề quản lý quỹ và tối thiểu 01 nhân viên kiểm soát tuân thủ.")

q(T_CT, 3,
  "Công ty chứng khoán P được cấp Giấy phép thành lập và hoạt động ngày 01/7/2024. Tháng 10/2026, cổ đông sáng lập Q muốn chuyển nhượng toàn bộ cổ phần của mình cho một nhà đầu tư không phải cổ đông sáng lập. Nhận định nào đúng?",
  "Không được, vì chưa hết 03 năm kể từ ngày P được cấp giấy phép",
  ["Được, vì đã quá 01 năm kể từ ngày P được cấp giấy phép",
   "Được, nếu Đại hội đồng cổ đông của P thông qua việc chuyển nhượng",
   "Không được, vì cổ đông sáng lập bị hạn chế chuyển nhượng 05 năm"],
  "Khoản 4 Điều 91: cổ đông sáng lập, thành viên góp vốn khi thành lập công ty chứng khoán, công ty quản lý quỹ không được chuyển nhượng cổ phần, phần vốn góp trong 03 năm kể từ ngày được cấp giấy phép, trừ chuyển nhượng giữa các cổ đông sáng lập. Hạn chế kéo dài đến 01/7/2027.",
  f"Khoản 4 Điều 91 {LCK}",
  "không được chuyển nhượng cổ phần hoặc phần vốn góp của mình trong thời hạn 03 năm kể từ ngày được cấp giấy phép, trừ trường hợp chuyển nhượng giữa các cổ đông sáng lập, thành viên góp vốn khi thành lập công ty")

q(T_CT, 2,
  "Hành vi nào sau đây công ty chứng khoán KHÔNG được thực hiện?",
  "Cam kết bảo đảm khách hàng không bị thua lỗ khi đầu tư cổ phiếu",
  ["Ưu tiên thực hiện lệnh của khách hàng trước lệnh tự doanh của công ty",
   "Cung cấp thông tin khách hàng theo yêu cầu của cơ quan có thẩm quyền",
   "Ký hợp đồng bằng văn bản với khách hàng khi cung cấp dịch vụ"],
  "Khoản 1 Điều 91 cấm đưa ra nhận định hoặc bảo đảm về mức thu nhập, lợi nhuận hoặc bảo đảm khách hàng không bị thua lỗ, trừ chứng khoán có thu nhập cố định. Ưu tiên lệnh khách hàng và ký hợp đồng bằng văn bản là nghĩa vụ (Điều 89); cung cấp thông tin theo yêu cầu cơ quan có thẩm quyền là ngoại lệ được phép (khoản 2 Điều 91).",
  f"Khoản 1, 2 Điều 91; khoản 4, 5 Điều 89 {LCK}",
  "Không được đưa ra nhận định hoặc bảo đảm với khách hàng về mức thu nhập hoặc lợi nhuận đạt được trên khoản đầu tư của mình hoặc bảo đảm khách hàng không bị thua lỗ, trừ trường hợp đầu tư vào chứng khoán có thu nhập cố định.")

q(T_CT, 3,
  "Ngày 05/8/2026, vốn chủ sở hữu của công ty chứng khoán R xuống thấp hơn vốn điều lệ tối thiểu theo quy định. Theo Điều 85 Luật Chứng khoán, R phải xử lý thế nào?",
  "Thông qua phương án khắc phục, báo cáo UBCKNN trong 30 ngày; thời gian khắc phục tối đa 06 tháng",
  ["Thông qua phương án khắc phục, báo cáo UBCKNN trong 15 ngày; thời gian khắc phục tối đa 03 tháng",
   "Thông qua phương án khắc phục, báo cáo UBCKNN trong 30 ngày; thời gian khắc phục tối đa 12 tháng",
   "Không cần khắc phục; UBCKNN thu hồi Giấy phép ngay khi phát sinh"],
  "Khoản 2 Điều 85: trong 30 ngày kể từ ngày không đáp ứng điều kiện hoặc VCSH thấp hơn vốn điều lệ tối thiểu, phải thông qua phương án khắc phục và báo cáo UBCKNN; thời gian khắc phục tối đa 06 tháng đối với điều kiện VCSH, 03 tháng đối với điều kiện khác. Trong thời gian này CTCK không được mở rộng hoạt động, chia lợi nhuận.",
  f"Khoản 2, 3 Điều 85 {LCK}",
  "Thời gian thực hiện phương án khắc phục tối đa là 06 tháng đối với điều kiện về vốn chủ sở hữu, tối đa là 03 tháng đối với các điều kiện khác kể từ ngày không đáp ứng điều kiện.")

# ---------------- Hành nghề chứng khoán – Luật (4) ----------------
q(T_HN, 1,
  "Loại nào sau đây KHÔNG phải là chứng chỉ hành nghề chứng khoán theo Điều 97 Luật Chứng khoán?",
  "Chứng chỉ hành nghề bảo lãnh phát hành",
  ["Chứng chỉ hành nghề môi giới chứng khoán", "Chứng chỉ hành nghề phân tích tài chính",
   "Chứng chỉ hành nghề quản lý quỹ"],
  "Khoản 1 Điều 97: CCHN chứng khoán gồm 03 loại: môi giới chứng khoán, phân tích tài chính, quản lý quỹ. Không có CCHN riêng cho bảo lãnh phát hành (người có CCHN phân tích tài chính hoặc quản lý quỹ được thực hiện nghiệp vụ bảo lãnh phát hành).",
  f"Khoản 1 Điều 97 {LCK}",
  "Chứng chỉ hành nghề môi giới chứng khoán; b) Chứng chỉ hành nghề phân tích tài chính; c) Chứng chỉ hành nghề quản lý quỹ.")

q(T_HN, 3,
  "Bà L được cấp CCHN môi giới chứng khoán năm 2019, làm việc tại công ty chứng khoán đến tháng 6/2022 rồi chuyển sang làm kế toán cho doanh nghiệp sản xuất, không hành nghề chứng khoán đến nay (tháng 11/2026). Nhận định nào đúng?",
  "Bà L bị thu hồi CCHN do không hành nghề chứng khoán 03 năm liên tục",
  ["CCHN của bà L vẫn có hiệu lực vì CCHN không ghi thời hạn sử dụng",
   "Bà L chỉ bị thu hồi CCHN nếu không tham gia tập huấn kiến thức hằng năm",
   "Bà L bị thu hồi CCHN và vĩnh viễn không được cấp lại"],
  "Điểm c khoản 3 Điều 97: CCHN bị thu hồi khi không hành nghề chứng khoán trong 03 năm liên tục (bà L ngừng từ 6/2022 đến 11/2026 > 03 năm). Theo khoản 4 Điều 97, chỉ trường hợp thu hồi do vi phạm Điều 12, khoản 2 Điều 98 mới không được cấp lại; bà L có thể đề nghị cấp lại khi đáp ứng điều kiện như cấp lần đầu (NĐ 245/2025).",
  f"Điểm c khoản 3, khoản 4 Điều 97 {LCK}; Điều 214 NĐ 155/2020/NĐ-CP (sửa đổi bởi NĐ 245/2025/NĐ-CP)",
  "Không hành nghề chứng khoán trong 03 năm liên tục.")

q(T_HN, 2,
  "Người bị thu hồi chứng chỉ hành nghề chứng khoán trong trường hợp nào thì KHÔNG được cấp lại chứng chỉ hành nghề?",
  "Vi phạm Điều 12 hoặc khoản 2 Điều 98 Luật Chứng khoán",
  ["Không còn đáp ứng điều kiện cấp chứng chỉ hành nghề",
   "Không hành nghề chứng khoán trong 03 năm liên tục",
   "Chứng chỉ hành nghề bị mất, bị hỏng hoặc rách nát"],
  "Khoản 4 Điều 97: người bị thu hồi CCHN theo điểm b khoản 3 (vi phạm Điều 12 hoặc khoản 2 Điều 98) không được cấp lại. Các trường hợp không còn đáp ứng điều kiện, không hành nghề 03 năm liên tục hoặc mất, hỏng chứng chỉ vẫn có thể được cấp lại.",
  f"Khoản 3, 4 Điều 97 {LCK}",
  "Người bị thu hồi chứng chỉ hành nghề chứng khoán trong trường hợp quy định tại điểm b khoản 3 Điều này không được cấp lại chứng chỉ hành nghề")

q(T_HN, 2,
  "Anh D có CCHN, làm chuyên viên phân tích tại công ty chứng khoán F (F có nghiệp vụ môi giới). Anh D muốn mở tài khoản giao dịch chứng khoán đứng tên mình tại công ty chứng khoán G để tự đầu tư. Nhận định nào đúng?",
  "Không được, vì công ty F có nghiệp vụ môi giới chứng khoán",
  ["Được, nếu anh D thông báo bằng văn bản cho công ty F",
   "Được, vì quy định chỉ áp dụng với người có CCHN môi giới",
   "Được, nếu tổng giá trị giao dịch dưới 02 tỷ đồng mỗi năm"],
  "Điểm b khoản 2 Điều 98: người hành nghề chứng khoán không được mở, quản lý tài khoản giao dịch tại công ty chứng khoán nơi mình không làm việc, trừ khi công ty chứng khoán nơi mình làm việc không có nghiệp vụ môi giới. Quy định áp dụng cho mọi người hành nghề, không phân biệt loại CCHN.",
  f"Điểm b khoản 2 Điều 98 {LCK}",
  "Mở, quản lý tài khoản giao dịch chứng khoán tại công ty chứng khoán nơi mình không làm việc, trừ trường hợp công ty chứng khoán nơi mình đang làm việc không có nghiệp vụ môi giới chứng khoán")

# ---------------- Quy chế thi 2026 & TT 135/2025 (10) ----------------
q(T_HN, 1,
  "Theo quy định hiện hành và thông báo của UBCKNN năm 2026, nội dung thi sát hạch cấp chứng chỉ hành nghề chứng khoán gồm:",
  "Phần pháp luật về chứng khoán và TTCK Việt Nam và phần chuyên môn",
  ["Phần lý thuyết nghiệp vụ và phần thực hành trên phần mềm giao dịch",
   "Phần kiến thức cơ bản, phần pháp luật và phần phỏng vấn trực tiếp",
   "Một bài thi tổng hợp duy nhất về chuyên môn chứng khoán"],
  "Khoản 5a Điều 213 NĐ 155/2020 (bổ sung bởi NĐ 245/2025) và thông báo kế hoạch thi 2026 của UBCKNN: nội dung sát hạch gồm hai phần — Phần pháp luật về chứng khoán và TTCK Việt Nam và Phần chuyên môn; hình thức thi trắc nghiệm trên máy vi tính.",
  "Khoản 5a Điều 213 NĐ 155/2020/NĐ-CP (bổ sung bởi khoản 73 Điều 1 NĐ 245/2025/NĐ-CP); Thông báo kế hoạch thi sát hạch 2026 của UBCKNN",
  "Nội dung sát hạch cấp chứng chỉ hành nghề chứng khoán gồm hai phần: Phần pháp luật về chứng khoán và thị trường chứng khoán Việt Nam và phần chuyên môn.",
  UBCK)

q(T_HN, 2,
  "Theo Thông báo số 11 của Hội đồng thi sát hạch (đợt III/2026), phát biểu nào ĐÚNG về thời gian làm bài thi sát hạch?",
  "Phân tích tài chính: 150 phút, mỗi phần 75 phút",
  ["Môi giới chứng khoán: 150 phút, mỗi phần 75 phút",
   "Quản lý quỹ: 120 phút, mỗi phần 60 phút",
   "Phân tích tài chính: 180 phút, mỗi phần 90 phút"],
  "Thời gian làm bài: Môi giới chứng khoán 120 phút (mỗi phần 60 phút); Phân tích tài chính 150 phút (mỗi phần 75 phút); Quản lý quỹ 180 phút (mỗi phần 90 phút).",
  "Thông báo số 11/TB-HĐTSH về lịch trình thi, ca thi, thời gian làm bài đợt III năm 2026",
  "Thời gian làm bài thi sát hạch cấp chứng chỉ hành nghề Phân tích tài chính là 150 phút, mỗi phần 75 phút.",
  UBCK)

q(T_HN, 3,
  "Thí sinh X thi sát hạch CCHN môi giới năm 2026: phần pháp luật trả lời đúng 58% số câu, phần chuyên môn trả lời đúng 85% số câu. Kết quả của X được xác định thế nào?",
  "Chưa đạt; X thi lại phần pháp luật, đạt khi đúng từ 60% số câu phần đó",
  ["Đạt, vì tỷ lệ trả lời đúng bình quân của hai phần thi trên 60%",
   "Chưa đạt, X phải thi lại cả hai phần thi ở kỳ thi tiếp theo",
   "Đạt, vì tổng số câu trả lời đúng của hai phần đạt từ 50% trở lên"],
  "Từ năm 2026, thí sinh đạt khi trả lời đúng từ 60% câu hỏi trở lên của MỖI phần thi; không lấy bình quân. X chưa đạt phần pháp luật (58%) nên thi lại phần này (trong thời hạn quy định) và đạt khi đúng từ 60% số câu của phần thi lại.",
  "Thông báo số 01/TB-HĐTSH đợt I năm 2026 (mục 8); điểm c khoản 6 Điều 213 NĐ 155/2020/NĐ-CP (sửa đổi bởi NĐ 245/2025/NĐ-CP)",
  "Từ năm 2026, người dự thi được công nhận là đạt yêu cầu khi trả lời đúng từ 60% câu hỏi trở lên của mỗi phần thi tại cả hai phần nội dung thi.",
  UBCK)

q(T_HN, 3,
  "Thí sinh Y dự thi đợt I/2026 (kết quả được UBCKNN thông báo tháng 5/2026), đạt phần chuyên môn nhưng chưa đạt phần pháp luật. Y không dự các kỳ thi tiếp theo trong năm 2026 và đến tháng 11/2027 mới đăng ký thi lại. Theo NĐ 245/2025, Y phải:",
  "Thi lại cả hai phần vì đã quá thời hạn được thi lại phần chưa đạt",
  ["Chỉ thi lại phần pháp luật vì kết quả phần đạt được bảo lưu không thời hạn",
   "Chỉ thi lại phần pháp luật vì kết quả phần đạt được bảo lưu 02 năm",
   "Học lại khóa chuyên môn trước khi được đăng ký thi lại phần pháp luật"],
  "Điểm c khoản 6 Điều 213 NĐ 155 (sửa đổi bởi NĐ 245/2025): thí sinh chưa đạt một phần được thi lại phần chưa đạt trong vòng 01 năm kể từ ngày UBCKNN thông báo kết quả thi lần đầu hoặc kỳ thi gần nhất liền sau kỳ thi đã dự; quá thời hạn phải thi lại cả hai phần. Tháng 11/2027 đã quá 01 năm kể từ tháng 5/2026.",
  "Điểm c khoản 6 Điều 213 NĐ 155/2020/NĐ-CP (sửa đổi bởi điểm đ khoản 73 Điều 1 NĐ 245/2025/NĐ-CP)",
  "thí sinh được thi lại phần chưa đạt trong vòng 01 năm kể từ ngày Ủy ban Chứng khoán Nhà nước thông báo kết quả thi lần đầu",
  ND245)

q(T_HN, 2,
  "Từ năm 2026, thí sinh không đồng ý với kết quả bài thi sát hạch trắc nghiệm trên máy vi tính có được đề nghị phúc khảo không?",
  "Không, HĐTSH không tổ chức phúc khảo bài thi trắc nghiệm trên máy tính",
  ["Có, trong thời hạn 15 ngày kể từ ngày công bố kết quả thi",
   "Có, nếu thí sinh nộp chi phí phúc khảo theo mức quy định của HĐTSH",
   "Chỉ được phúc khảo phần thi pháp luật, không phúc khảo phần chuyên môn"],
  "Thông báo của HĐTSH năm 2026: từ năm 2026, HĐTSH không tổ chức việc phúc khảo bài thi trắc nghiệm trên máy vi tính; điểm được báo ngay trên màn hình sau khi nộp bài và thí sinh được xem lại câu đúng/sai.",
  "Thông báo số 01/TB-HĐTSH đợt I năm 2026 (mục 8)",
  "Về phúc khảo bài thi: Từ năm 2026, HĐTSH không tổ chức việc phúc khảo bài thi trắc nghiệm trên máy vi tính.",
  UBCK)

q(T_HN, 1,
  "Mức chi phí dự thi sát hạch cấp chứng chỉ hành nghề chứng khoán từ năm 2026 (áp dụng cho cả thi mới và thi lại) là:",
  "1.000.000 đồng/thí sinh/loại chứng chỉ",
  ["500.000 đồng/thí sinh/phần thi",
   "1.000.000 đồng/thí sinh cho cả 03 loại chứng chỉ",
   "2.000.000 đồng/thí sinh/loại chứng chỉ"],
  "HĐTSH thông báo mức thu chi phí dự thi sát hạch (cho thí sinh thi mới và thi lại của 03 loại CCHN) từ năm 2026 là 1.000.000 đồng/thí sinh/loại chứng chỉ, nộp bằng chuyển khoản.",
  "Thông báo số 01/TB-HĐTSH đợt I năm 2026 (mục 5.1)",
  "từ năm 2026 là 1.000.000 đồng (một triệu đồng)/thí sinh/loại chứng chỉ.",
  UBCK)

q(T_HN, 2,
  "Chị N có bằng cử nhân Luật Kinh tế. Theo Thông tư 135/2025/TT-BTC, đối với chứng chỉ chuyên môn Pháp luật về chứng khoán và thị trường chứng khoán, chị N:",
  "Được miễn khóa học nhưng phải dự kiểm tra trình độ chuyên môn",
  ["Được miễn cả khóa học và kiểm tra, được cấp chứng chỉ ngay",
   "Không được miễn, phải học đủ khóa học và dự kiểm tra",
   "Chỉ được miễn khóa học Những vấn đề cơ bản về chứng khoán và TTCK"],
  "Khoản 5 Điều 3 TT 135/2025: người có bằng cử nhân trở lên ngành Luật Kinh tế được miễn khóa Pháp luật về chứng khoán và TTCK nhưng vẫn phải dự kiểm tra trình độ chuyên môn; người có bằng Kinh tế, Kinh doanh, Tài chính – Ngân hàng – Bảo hiểm, Kế toán – Kiểm toán được miễn khóa Những vấn đề cơ bản về chứng khoán và TTCK.",
  "Khoản 5 Điều 3 Thông tư 135/2025/TT-BTC",
  "Cases exempted from attending professional training courses but required to take professional proficiency examinations in order to be issued securities professional certificates include",
  TT135)

q(T_HN, 2,
  "Theo Thông tư 135/2025/TT-BTC, chứng chỉ CIIA hoặc văn bản xác nhận đạt kỳ thi CFA bậc II trở lên được coi là tương đương chứng chỉ chuyên môn nào sau đây?",
  "Quản lý quỹ và tài sản",
  ["Pháp luật về chứng khoán và thị trường chứng khoán",
   "Môi giới chứng khoán và tư vấn đầu tư chứng khoán",
   "Tư vấn tài chính và bảo lãnh phát hành chứng khoán"],
  "Khoản 1 Điều 4 TT 135/2025: CIIA hoặc CFA bậc II trở lên tương đương các chứng chỉ: Những vấn đề cơ bản về CK và TTCK; Phân tích và đầu tư CK; Phân tích BCTC doanh nghiệp; Quản lý quỹ và tài sản; Chứng khoán phái sinh và TTCK phái sinh. Không bao gồm Pháp luật, Môi giới – tư vấn, Tư vấn tài chính – bảo lãnh.",
  "Khoản 1 Điều 4 Thông tư 135/2025/TT-BTC",
  "written confirmation of passing the Chartered Financial Analyst (CFA) level II exam or higher is equivalent to certificates in: Basic issues of securities and the securities market, Securities analysis and investment, Corporate financial statement analysis, Fund and asset management",
  TT135)

q(T_HN, 2,
  "Theo Thông tư 135/2025/TT-BTC, khi UBCKNN triển khai cấp chứng chỉ hành nghề chứng khoán điện tử, người đã được cấp CCHN bản giấy phải:",
  "Chuyển đổi sang CCHN điện tử trong 01 năm kể từ khi có hướng dẫn chuyển đổi",
  ["Tiếp tục sử dụng song song CCHN bản giấy không giới hạn thời gian",
   "Chuyển đổi trong 06 tháng kể từ khi có hướng dẫn, quá hạn bị thu hồi CCHN",
   "Thi lại phần thi pháp luật để được cấp chứng chỉ hành nghề điện tử"],
  "Điều 5 TT 135/2025: người được cấp CCHN và tổ chức sử dụng người hành nghề phải chuyển đổi CCHN giấy sang điện tử trong 01 năm kể từ ngày UBCKNN ban hành hướng dẫn chuyển đổi; CCHN giấy hết hiệu lực khi chuyển đổi; quá hạn chưa chuyển đổi thì không được ghi nhận trạng thái 'người hành nghề chứng khoán' trên hệ thống của UBCKNN.",
  "Khoản 2, 3 Điều 5 Thông tư 135/2025/TT-BTC",
  "converting previously issued paper-based securities practicing certificates into electronic ones within 01 (one) year from the date the SSC issues the conversion guidelines.",
  TT135)

q(T_HN, 2,
  "Theo Thông tư 135/2025/TT-BTC, nghĩa vụ tập huấn kiến thức hằng năm của người hành nghề chứng khoán được quy định như thế nào?",
  "Tối thiểu 08 giờ/năm từ 01/01/2027; không bắt buộc trong năm được cấp CCHN",
  ["Tối thiểu 16 giờ/năm từ 09/02/2026; bắt buộc cả trong năm được cấp CCHN",
   "Tối thiểu 08 giờ mỗi 02 năm, áp dụng cả trong năm được cấp CCHN",
   "Không bắt buộc, chỉ khuyến khích người hành nghề tự cập nhật"],
  "Điều 8, 10, 12 TT 135/2025: người hành nghề phải tham gia tập huấn hằng năm (01/01–31/12), thời lượng tối thiểu 08 giờ/năm; không bắt buộc trong năm được cấp CCHN; Chương IV về tập huấn áp dụng từ 01/01/2027. Trước 31/01 hằng năm UBCKNN công khai danh sách người không hoàn thành.",
  "Điều 8, khoản 3 Điều 10, khoản 3 Điều 12 Thông tư 135/2025/TT-BTC",
  "ensuring a minimum training duration of 08 hours per year.",
  TT135)

# ---------------- Quỹ đầu tư (7) ----------------
q(T_QUY, 1,
  "Quỹ đại chúng (không phải quỹ hoán đổi danh mục) được thành lập khi đáp ứng điều kiện nào sau đây?",
  "Ít nhất 100 nhà đầu tư (không kể NĐT chuyên nghiệp) và đã bán ít nhất 50 tỷ đồng",
  ["Ít nhất 50 nhà đầu tư và tổng giá trị chứng chỉ quỹ đã bán ít nhất 100 tỷ đồng",
   "Ít nhất 100 nhà đầu tư kể cả NĐT chuyên nghiệp và đã bán ít nhất 30 tỷ đồng",
   "Từ 02 nhà đầu tư trở lên và tổng giá trị chứng chỉ quỹ đã bán ít nhất 50 tỷ đồng"],
  "Khoản 1 Điều 108: huy động vốn trong 90 ngày kể từ ngày Giấy chứng nhận chào bán có hiệu lực; quỹ được thành lập khi có ít nhất 100 nhà đầu tư, không kể NĐT chuyên nghiệp (trừ quỹ ETF) và tổng giá trị chứng chỉ quỹ đã bán đạt ít nhất 50 tỷ đồng.",
  f"Khoản 1 Điều 108 {LCK}",
  "Có ít nhất 100 nhà đầu tư, không kể nhà đầu tư chứng khoán chuyên nghiệp mua chứng chỉ quỹ, trừ quỹ hoán đổi danh mục")

q(T_QUY, 3,
  "Quỹ đóng ABC có tổng giá trị tài sản 500 tỷ đồng. Công ty XYZ có tổng giá trị chứng khoán đang lưu hành 800 tỷ đồng (không có trái phiếu Chính phủ). Giá trị tối đa quỹ ABC được đầu tư vào chứng khoán của XYZ là:",
  "80 tỷ đồng", ["100 tỷ đồng", "50 tỷ đồng", "160 tỷ đồng"],
  "Áp dụng đồng thời hai hạn chế tại khoản 1 Điều 110: (1) không quá 10% tổng giá trị chứng khoán đang lưu hành của XYZ = 10% × 800 = 80 tỷ; (2) không quá 20% tổng giá trị tài sản của quỹ = 20% × 500 = 100 tỷ. Mức tối đa = min(80; 100) = 80 tỷ đồng. 50 tỷ là nhầm 10% × tài sản quỹ; 160 tỷ là nhầm 20% × 800.",
  f"Điểm b, c khoản 1 Điều 110 {LCK}",
  "Đầu tư vào chứng khoán của 01 tổ chức phát hành quá 10% tổng giá trị chứng khoán đang lưu hành của tổ chức đó, trừ trái phiếu Chính phủ")

q(T_QUY, 2,
  "Quy định nào sau đây đúng về việc vay của quỹ đại chúng?",
  "Chỉ vay ngắn hạn cho chi phí, thanh toán chứng chỉ quỹ; tối đa 5% NAV, tối đa 30 ngày",
  ["Chỉ vay ngắn hạn để trang trải chi phí; tổng vay không quá 10% NAV, tối đa 90 ngày",
   "Được vay để đầu tư thêm nếu tổng dư nợ vay không quá 20% NAV của quỹ",
   "Không được vay dưới bất kỳ hình thức nào, kể cả vay ngắn hạn ngân hàng"],
  "Khoản 2 Điều 110: công ty quản lý quỹ không được vay để tài trợ hoạt động của quỹ đại chúng, trừ vay ngắn hạn để trang trải chi phí cần thiết hoặc thanh toán giao dịch chứng chỉ quỹ với nhà đầu tư; tổng các khoản vay ngắn hạn không quá 5% giá trị tài sản ròng tại mọi thời điểm, thời hạn vay tối đa 30 ngày.",
  f"Khoản 2 Điều 110 {LCK}",
  "Tổng giá trị các khoản vay ngắn hạn của quỹ đại chúng không được quá 5% giá trị tài sản ròng của quỹ đại chúng tại mọi thời điểm và thời hạn vay tối đa là 30 ngày.")

q(T_QUY, 1,
  "Ban đại diện quỹ đại chúng có số lượng thành viên và cơ cấu thành viên độc lập như thế nào?",
  "Từ 03 đến 11 thành viên, trong đó ít nhất hai phần ba là thành viên độc lập",
  ["Từ 03 đến 11 thành viên, trong đó ít nhất một nửa là thành viên độc lập",
   "Từ 05 đến 11 thành viên, trong đó ít nhất một phần ba là thành viên độc lập",
   "Từ 02 đến 09 thành viên, tất cả đều là thành viên độc lập"],
  "Khoản 3 Điều 109: Ban đại diện quỹ đại chúng có từ 03 đến 11 thành viên, ít nhất hai phần ba là thành viên độc lập, không phải người có liên quan của công ty quản lý quỹ và ngân hàng giám sát.",
  f"Khoản 3 Điều 109 {LCK}",
  "Ban đại diện quỹ đại chúng có từ 03 đến 11 thành viên, trong đó có ít nhất hai phần ba số thành viên Ban đại diện quỹ là thành viên độc lập")

q(T_QUY, 3,
  "Quỹ mở M có giá trị tài sản ròng giảm xuống và duy trì dưới 10 tỷ đồng liên tục từ tháng 01 đến hết tháng 6/2026. Theo Luật Chứng khoán, nhận định nào đúng?",
  "Phải giải thể; triệu tập Đại hội nhà đầu tư trong 30 ngày",
  ["Quỹ tiếp tục hoạt động vì chỉ giải thể khi NAV dưới 05 tỷ đồng",
   "Quỹ tự động chuyển đổi thành quỹ thành viên do cùng công ty quản lý",
   "Phải giải thể; triệu tập Đại hội nhà đầu tư 03 tháng trước ngày giải thể"],
  "Điểm đ khoản 1 Điều 104: quỹ giải thể khi NAV xuống dưới 10 tỷ đồng liên tục trong 06 tháng. Khoản 2 Điều 104: với trường hợp tại các điểm c, d, đ, e, công ty quản lý quỹ hoặc ngân hàng giám sát và Ban đại diện quỹ phải triệu tập Đại hội nhà đầu tư trong 30 ngày; mốc 03 tháng trước ngày giải thể áp dụng cho trường hợp hết thời hạn hoạt động hoặc ĐHNĐT quyết định.",
  f"Điểm đ khoản 1, khoản 2 Điều 104 {LCK}",
  "Giá trị tài sản ròng của quỹ đầu tư chứng khoán xuống dưới 10 tỷ đồng liên tục trong 06 tháng;")

q(T_QUY, 2,
  "Điều kiện nào sau đây KHÔNG thuộc điều kiện để quỹ đóng được tăng vốn theo Điều 112 Luật Chứng khoán?",
  "Giá trị tài sản ròng của quỹ tối thiểu 100 tỷ đồng",
  ["Lợi nhuận của quỹ năm liền trước năm đề nghị tăng vốn là số dương",
   "Công ty quản lý quỹ không bị xử phạt VPHC về chứng khoán trong 02 năm gần nhất",
   "Phương án phát hành thêm chứng chỉ quỹ đóng được Đại hội nhà đầu tư thông qua"],
  "Khoản 1 Điều 112: tăng vốn quỹ đóng phải được UBCKNN chấp thuận và đáp ứng: Điều lệ quỹ có quy định; lợi nhuận năm liền trước dương; công ty quản lý quỹ không bị xử phạt VPHC trong 02 năm; phương án phát hành được ĐHNĐT thông qua. Không có điều kiện NAV tối thiểu 100 tỷ (mốc NAV 50 tỷ áp dụng khi gia hạn thời hạn hoạt động).",
  f"Khoản 1, 3 Điều 112 {LCK}",
  "Lợi nhuận của quỹ trong năm liền trước năm đề nghị tăng vốn phải là số dương;")

q(T_QUY, 2,
  "Điều kiện thành lập quỹ thành viên theo Điều 113 Luật Chứng khoán gồm:",
  "Vốn góp tối thiểu 50 tỷ đồng, có từ 02 đến 99 thành viên đều là nhà đầu tư chứng khoán chuyên nghiệp",
  ["Vốn góp tối thiểu 10 tỷ đồng, có từ 02 đến 99 thành viên là nhà đầu tư bất kỳ",
   "Vốn góp tối thiểu 50 tỷ đồng, có tối đa 100 thành viên, do 02 công ty quản lý quỹ cùng quản lý",
   "Vốn góp tối thiểu 50 tỷ đồng, tài sản lưu ký tại chính công ty quản lý quỹ"],
  "Khoản 2 Điều 113: vốn góp tối thiểu 50 tỷ đồng; từ 02 đến 99 thành viên và chỉ gồm nhà đầu tư chứng khoán chuyên nghiệp; do 01 công ty quản lý quỹ quản lý; tài sản lưu ký tại 01 ngân hàng lưu ký độc lập với công ty quản lý quỹ.",
  f"Khoản 2 Điều 113 {LCK}",
  "Vốn góp tối thiểu là 50 tỷ đồng; b) Có từ 02 đến 99 thành viên góp vốn và chỉ bao gồm thành viên là nhà đầu tư chứng khoán chuyên nghiệp")

# ---------------- Công bố thông tin (7) ----------------
q(T_CB2, 1,
  "Theo Điều 119 Luật Chứng khoán, việc công bố thông tin phải bảo đảm nguyên tắc nào?",
  "Đầy đủ, chính xác, kịp thời",
  ["Công khai, minh bạch, công bằng", "Trung thực, khách quan, bảo mật",
   "Nhanh chóng, đơn giản, tiết kiệm"],
  "Khoản 1 Điều 119: việc công bố thông tin phải đầy đủ, chính xác, kịp thời; đối tượng công bố chịu trách nhiệm trước pháp luật về nội dung và phải đồng thời báo cáo UBCKNN, nơi chứng khoán niêm yết/đăng ký giao dịch.",
  f"Khoản 1 Điều 119 {LCK}",
  "Việc công bố thông tin phải đầy đủ, chính xác, kịp thời.")

q(T_CB2, 2,
  "Trường hợp nào cổ đông lớn KHÔNG phải công bố thông tin dù tỷ lệ sở hữu thay đổi qua ngưỡng 1% số cổ phiếu có quyền biểu quyết?",
  "Thay đổi do công ty đại chúng mua lại cổ phiếu quỹ hoặc phát hành thêm cổ phiếu",
  ["Cổ đông lớn bán cổ phiếu qua phương thức giao dịch thỏa thuận trên sàn",
   "Cổ đông lớn là tổ chức nước ngoài mua thêm cổ phiếu qua hệ thống giao dịch",
   "Cổ đông lớn mua thêm cổ phiếu qua phương thức khớp lệnh tập trung trên sàn"],
  "Khoản 3 Điều 127: nghĩa vụ công bố khi trở thành/không còn là cổ đông lớn và khi thay đổi qua ngưỡng 1% không áp dụng đối với thay đổi tỷ lệ phát sinh do công ty đại chúng mua lại cổ phiếu của chính mình hoặc phát hành thêm cổ phiếu, quỹ ETF thực hiện giao dịch hoán đổi và trường hợp khác theo pháp luật.",
  f"Điểm a khoản 3 Điều 127 {LCK}",
  "Thay đổi tỷ lệ nắm giữ cổ phiếu có quyền biểu quyết phát sinh do công ty đại chúng mua lại cổ phiếu của chính mình hoặc phát hành thêm cổ phiếu")

q(T_CB2, 3,
  "Quỹ đầu tư Z đang sở hữu 6,4% số cổ phiếu có quyền biểu quyết của công ty đại chúng Y. Z mua thêm qua sàn, tỷ lệ sở hữu tăng lên 7,2%. Nghĩa vụ công bố thông tin của Z là:",
  "Phải công bố thông tin vì số cổ phiếu sở hữu thay đổi qua ngưỡng 7%",
  ["Không phải công bố vì mức thay đổi 0,8% chưa đủ 1%",
   "Chỉ phải công bố khi tỷ lệ sở hữu đạt 10% số cổ phiếu có quyền biểu quyết",
   "Không phải công bố vì Z là nhà đầu tư chứng khoán chuyên nghiệp"],
  "Khoản 2 Điều 127: cổ đông lớn phải công bố thông tin khi số cổ phiếu sở hữu thay đổi QUA các ngưỡng 1% (6%, 7%, 8%...). Từ 6,4% lên 7,2% đã vượt ngưỡng 7% nên phải công bố, dù mức thay đổi chỉ 0,8%.",
  f"Khoản 2 Điều 127 {LCK}",
  "phải công bố thông tin khi có thay đổi về số lượng cổ phiếu sở hữu qua các ngưỡng 1% số cổ phiếu có quyền biểu quyết của công ty đại chúng")

q(T_CB2, 1,
  "Công ty đại chúng phải công bố thông tin bất thường khi quyết định mua, bán tài sản hoặc thực hiện giao dịch có giá trị lớn hơn bao nhiêu phần trăm tổng tài sản của công ty (theo BCTC năm gần nhất được kiểm toán hoặc BCTC 06 tháng gần nhất được soát xét)?",
  "15%", ["10%", "20%", "35%"],
  "Điểm h khoản 2 Điều 120: công ty đại chúng công bố thông tin bất thường khi quyết định mua, bán tài sản hoặc thực hiện các giao dịch có giá trị lớn hơn 15% tổng tài sản căn cứ BCTC năm gần nhất được kiểm toán hoặc BCTC 06 tháng gần nhất được soát xét. Mốc 35% là tiêu chí xác định giao dịch cơ cấu lại doanh nghiệp theo NĐ 155.",
  f"Điểm h khoản 2 Điều 120 {LCK}",
  "Quyết định mua, bán tài sản hoặc thực hiện các giao dịch có giá trị lớn hơn 15% tổng tài sản của công ty")

q(T_CB2, 2,
  "Bà G là vợ của Tổng giám đốc công ty niêm yết H; bà G không giữ chức vụ nào tại H. Bà G dự định mua 50.000 cổ phiếu H (giá trị vượt mức tối thiểu phải công bố). Nhận định nào đúng?",
  "Bà G phải công bố trước và sau giao dịch vì là người có liên quan",
  ["Bà G không phải công bố thông tin vì không giữ chức vụ tại công ty H",
   "Chỉ Tổng giám đốc phải công bố thông tin sau khi bà G giao dịch xong",
   "Bà G chỉ phải công bố nếu sau giao dịch trở thành cổ đông lớn"],
  "Khoản 1 Điều 128: người nội bộ của công ty đại chúng và người có liên quan của người nội bộ phải công bố thông tin trước và sau giao dịch cổ phiếu (trừ giao dịch chưa đạt giá trị tối thiểu phải công bố). Vợ là người có liên quan theo điểm d khoản 46 Điều 4.",
  f"Khoản 1 Điều 128; điểm d khoản 46 Điều 4 {LCK}",
  "Người nội bộ của công ty đại chúng, công ty đầu tư chứng khoán đại chúng, quỹ đại chúng và người có liên quan của các đối tượng này phải công bố thông tin trước và sau giao dịch")

q(T_CB2, 2,
  "Báo cáo tài chính nào sau đây công ty đại chúng phải công bố thông tin định kỳ theo Điều 120 Luật Chứng khoán?",
  "BCTC năm đã kiểm toán, BCTC 06 tháng đã được soát xét và BCTC quý",
  ["Chỉ BCTC năm đã được kiểm toán",
   "BCTC năm và BCTC 06 tháng đều đã kiểm toán, không yêu cầu BCTC quý",
   "BCTC quý đã được kiểm toán và BCTC năm đã được soát xét"],
  "Điểm a khoản 1 Điều 120: công ty đại chúng công bố định kỳ BCTC năm đã được kiểm toán, BCTC 06 tháng đã được soát xét bởi tổ chức kiểm toán được chấp thuận và BCTC quý; cùng với báo cáo thường niên, báo cáo tình hình quản trị, nghị quyết ĐHĐCĐ thường niên.",
  f"Điểm a khoản 1 Điều 120 {LCK}",
  "Báo cáo tài chính năm đã được kiểm toán, báo cáo tài chính 06 tháng đã được soát xét bởi tổ chức kiểm toán được chấp thuận, báo cáo tài chính quý")

q(T_CB2, 2,
  "Ngoài báo cáo tài chính, công ty chứng khoán phải công bố thông tin định kỳ về báo cáo tỷ lệ an toàn tài chính như thế nào?",
  "Tại 30/6 đã soát xét và tại 31/12 đã kiểm toán bởi tổ chức được chấp thuận",
  ["Hằng quý, không yêu cầu soát xét hay kiểm toán bởi tổ chức kiểm toán",
   "Chỉ tại ngày 31/12, đã được kiểm toán bởi tổ chức kiểm toán được chấp thuận",
   "Hằng tháng, chỉ gửi UBCKNN và không phải công bố ra công chúng"],
  "Điểm b khoản 1 Điều 123: công ty chứng khoán, công ty quản lý quỹ công bố định kỳ báo cáo tỷ lệ an toàn tài chính tại ngày 30 tháng 6 đã được soát xét và tại ngày 31 tháng 12 đã được kiểm toán bởi tổ chức kiểm toán được chấp thuận.",
  f"Điểm b khoản 1 Điều 123 {LCK}",
  "Báo cáo tỷ lệ an toàn tài chính tại ngày 30 tháng 6 đã được soát xét và tại ngày 31 tháng 12 đã được kiểm toán bởi tổ chức kiểm toán được chấp thuận")

# ---------------- Thanh tra & xử lý vi phạm (3) ----------------
q(T_TT, 1,
  "Mức phạt tiền tối đa trong xử phạt vi phạm hành chính đối với tổ chức có hành vi vi phạm khác trong lĩnh vực chứng khoán (ngoài các hành vi tại khoản 2, khoản 3 Điều 12) là:",
  "03 tỷ đồng", ["02 tỷ đồng", "05 tỷ đồng", "1,5 tỷ đồng"],
  "Khoản 4 Điều 132: mức phạt tiền tối đa đối với các hành vi vi phạm khác là 03 tỷ đồng; mức này áp dụng cho tổ chức, cá nhân vi phạm cùng hành vi thì tối đa bằng một phần hai (1,5 tỷ đồng).",
  f"Khoản 4, 5 Điều 132 {LCK}",
  "Mức phạt tiền tối đa trong xử phạt vi phạm hành chính đối với các hành vi vi phạm khác trong lĩnh vực chứng khoán là 03 tỷ đồng.")

q(T_TT, 3,
  "Cá nhân K thực hiện hành vi thao túng thị trường chứng khoán, thu lợi bất hợp pháp 800 triệu đồng. Mức phạt tiền tối đa có thể áp dụng đối với K theo Luật Chứng khoán là:",
  "04 tỷ đồng", ["08 tỷ đồng", "1,5 tỷ đồng", "03 tỷ đồng"],
  "Khoản 3 Điều 132: với hành vi tại khoản 2, 3 Điều 12, mức phạt tối đa (cho tổ chức) là 10 lần khoản thu trái pháp luật = 10 × 0,8 = 8 tỷ đồng (cao hơn 03 tỷ nên áp dụng 8 tỷ). Khoản 5: cá nhân tối đa bằng 1/2 mức của tổ chức = 8 : 2 = 4 tỷ đồng. 8 tỷ là quên chia đôi; 1,5 tỷ và 3 tỷ là áp nhầm khoản 4.",
  f"Khoản 3, 4, 5 Điều 132 {LCK}",
  "cá nhân thực hiện cùng hành vi vi phạm thì mức phạt tiền tối đa bằng một phần hai mức phạt tiền tối đa đối với tổ chức")

q(T_TT, 2,
  "Trong thanh tra, xử lý vi phạm, UBCKNN có quyền yêu cầu doanh nghiệp viễn thông cung cấp thông tin nào?",
  "Tên, địa chỉ, số máy gọi, số máy được gọi, thời gian gọi để xác minh vi phạm Điều 12",
  ["Nội dung ghi âm các cuộc gọi của mọi nhà đầu tư trên thị trường chứng khoán",
   "Toàn bộ danh bạ thuê bao để phục vụ giám sát giao dịch chứng khoán thường xuyên",
   "Tin nhắn và dữ liệu mạng xã hội của người hành nghề chứng khoán khi có yêu cầu"],
  "Điểm c khoản 1 Điều 130: UBCKNN được yêu cầu doanh nghiệp viễn thông cung cấp tên, địa chỉ, số máy gọi, số máy được gọi, thời gian gọi để xác minh, xử lý hành vi bị nghiêm cấm tại Điều 12; yêu cầu phải được Chủ tịch UBCKNN phê duyệt, bằng văn bản và thông tin được bảo mật.",
  f"Điểm c khoản 1, khoản 2, 3 Điều 130 {LCK}",
  "Yêu cầu doanh nghiệp viễn thông cung cấp tên, địa chỉ, số máy gọi, số máy được gọi, thời gian gọi để xác minh, xử lý hành vi bị nghiêm cấm quy định tại Điều 12 của Luật này.")


def build():
    n = len(Q)
    pos = [i % 4 for i in range(n)]
    random.Random(2026).shuffle(pos)
    out = []
    for i, (item, p) in enumerate(zip(Q, pos), 1):
        opts = item["o"][1:]
        opts.insert(p, item["o"][0])
        out.append({"id": f"L1-{i:03d}", "part": "LUAT", "subject": "LU",
                    "topic": item["topic"], "level": item["level"], "q": item["q"],
                    "o": opts, "a": p, "e": item["e"], "basis": item["basis"],
                    "quote": item["quote"], "src": item["src"], "as_of": "2026-11"})
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {n} questions to {OUT}")


if __name__ == "__main__":
    build()
