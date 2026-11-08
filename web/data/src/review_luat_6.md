# Soát chéo luat_6.json (L6-001 … L6-014) và L4-017/018/019 – 08/11/2026

Người soát: agent soát chéo lần 2. Đối chiếu nguyên văn các file trong `tai_lieu_phap_ly/van_ban_txt/` và tra web ngày 08/11/2026.
Bản trước khi sửa: `web/data/src/work_l6/luat_6.before_review.json`.
`python3 -I web/tools/kiem_tra.py`: OK, 834 câu. Còn một cảnh báo có từ trước: C2-085 ~ C2-086.

## 1. Rủi ro được giao: đã kiểm

| Vấn đề | Kết quả kiểm tra | Xử lý |
|---|---|---|
| BLHS sửa đổi (Điều 209–212) | **Chưa thông qua.** Dự án Bộ luật Hình sự (sửa đổi) có trong chương trình Kỳ họp thứ 2 Quốc hội khóa XVI. Kỳ họp khai mạc 17/10/2026, thảo luận ngày 27/10/2026 và dự kiến bế mạc 21/11/2026. Nếu được thông qua, luật dự kiến có hiệu lực **01/3/2027**. Luật sửa BLHS gần nhất là Luật 86/2025/QH15 (hiệu lực 01/7/2025), đã có trong VBHN 135/2025. | Giữ đáp án L6-013, L6-014. Thêm chữ "hiện hành" vào đề: "Theo Điều 21x Bộ luật Hình sự hiện hành (văn bản hợp nhất năm 2025)". |
| Luật Chứng khoán sửa đổi sau Luật 56/2024 và Luật 142/2025 | **Không có luật nào đang có hiệu lực.** Dự án Luật Chứng khoán (sửa đổi) đang trình Kỳ họp thứ 2 (bài báo ngày 28/10/2026 vẫn gọi là dự thảo). Kỳ họp không thường lệ thứ nhất (8/2026) không sửa Luật Chứng khoán. VBHN 102/2026 vẫn là văn bản hiện hành. | L6-003, L6-006 đúng theo VBHN 102 và Luật Thanh tra 84/2025. Khi luật mới có hiệu lực, cần soát lại L4-017, L6-003 và L6-006, vì Điều 129 sẽ bị sửa. |
| NĐ 216/2025 có văn bản sửa đổi sau 08/2025 không | Không tìm thấy văn bản sửa đổi, bổ sung hay thay thế. Đã tìm trên báo Thanh tra, luatvietnam và vbpl. Thanh tra Chính phủ chỉ đang soạn các nghị định khác: phòng, chống tham nhũng; khiếu nại, tố cáo; tiếp công dân. | Giữ nguyên. |
| QĐ 1726/QĐ-TTg | Không có văn bản sửa đổi. QĐ 1413/QĐ-TTg ngày 27/7/2026 (Đề án cải cách tổng thể thị trường tài chính) chỉ yêu cầu cập nhật chiến lược của các thị trường cấu phần; chưa đọc nguyên văn quyết định này. | L6-002 giữ nguyên vì đề nêu rõ QĐ 1726. Câu "chưa có văn bản sửa đổi" đổi thành "chưa thấy văn bản sửa đổi". |
| Luật XLVPHC sửa đổi | Đang trình Kỳ họp thứ 2, chưa có hiệu lực. | Không ảnh hưởng đến câu nào trong luat_6. |

Nguồn web: luatvietnam.vn (danh sách dự án luật Kỳ họp thứ 2, ngày 26/10/2026); daibieunhandan.vn và vietnamplus (thông cáo báo chí Kỳ họp thứ 2); thitruongtaichinhtiente.vn (28/10/2026, Luật Chứng khoán sửa đổi); hatinh.gov.vn (Luật 86/2025); lsvn.vn (Kỳ họp không thường lệ thứ nhất). Mức 45 + 30 ngày của Luật Thanh tra 2022 (Điều 47) và hai hình thức thanh tra tại Điều 46 lấy từ hethongphapluat.com.

## 2. Kết luận từng câu

| Mã | Kết luận | Sửa |
|---|---|---|
| L6-001 | Đúng (điểm a khoản 2 Điều 8 Luật Chứng khoán; QĐ 1726 ghi "Theo đề nghị của Bộ trưởng Bộ Tài chính"). | – |
| L6-002 | Đúng. Phần trích dẫn cũ dừng ở "47% GDP", chưa có con số 58% của đáp án. | Kéo dài `quote` tới "đạt tối thiểu 58% GDP". |
| L6-003 | Đúng. Mệnh đề II có thể gây tranh cãi vì khoản 3 Điều 129 Luật Chứng khoán (chưa sửa) vẫn ghi Thanh tra Bộ Tài chính hướng dẫn nghiệp vụ. | Mỗi mệnh đề một dòng (`\n`). Giải thích thêm khoản 2 Điều 62 Luật Thanh tra (luật chưa sửa thì thực hiện theo Luật Thanh tra). Bổ sung căn cứ. |
| L6-004 | Đúng (30 + 10 = 40 ngày). | Sửa chú thích phương án 75 ngày: đây là mức 45 + 30 của Thanh tra bộ, tổng cục, cục, tỉnh theo Luật Thanh tra 2022. |
| L6-005 | Đáp án đúng, nhưng phương án dễ đoán: 3 phương án nhiễu cùng có ý "chỉ trực tiếp". | Viết lại 3 phương án nhiễu: thêm "thường xuyên"; "chỉ theo kế hoạch" nhưng có trực tuyến; chia "hành chính/chuyên ngành". Viết lại giải thích. Đáp án vẫn ở vị trí A. |
| L6-006 | Phương án B cũ ("đề nghị Tổng Thanh tra Chính phủ ban hành quyết định") có thể bị cãi: theo điểm đ, i khoản 1 Điều 10, Thanh tra Chính phủ thanh tra lĩnh vực của Bộ không có Thanh tra Bộ và thanh tra khi Bộ trưởng đề nghị. | Thay B bằng "Chủ tịch UBCKNN ban hành quyết định thanh tra sau khi Tổng Thanh tra Chính phủ cho ý kiến" (sai rõ ràng). Giải thích thêm. |
| L6-007 | Đúng (Điều 3, 3a, 7, 9, 17 TT 95 hợp nhất). Mệnh đề IV giao với L4-020, nhưng chỉ là một mệnh đề trong câu tổ hợp nên chấp nhận được. | Mỗi mệnh đề một dòng. |
| L6-008 | Đúng (Điều 25, khoản 6 Điều 23; khoản 5b Điều 26 NĐ 156, bổ sung bởi NĐ 306). | – |
| L6-009 | Đúng (điểm d khoản 1 Điều 9; khoản 2 Điều 43, khoản 2 Điều 52). | – |
| L6-010 | Đúng (điểm a, d, e khoản 49 Điều 4, khoản 49 bổ sung bởi Luật 56/2024). Mệnh đề III giao một phần với L1-015 và C1-036, nhưng câu tổ hợp có ý mới (điểm d). | Mỗi mệnh đề một dòng. |
| L6-011 | Đúng. Khoản 6 Điều 32 vẫn là 400–500 triệu; cá nhân bị phạt 1/2 theo điểm c khoản 3 Điều 5 (NĐ 128), NĐ 306 chỉ sửa khoản 2 Điều 5. Điểm b khoản 7 (NĐ 306) không còn tước CCHN với điểm a khoản 6. Điểm c khoản 8 (NĐ 128) và điểm a khoản 5 Điều 51 (NĐ 306) quy định buộc hoàn trả. Ghi chú: VBHN 17/2026 không có lớp chữ; đã đối chiếu thẳng NĐ 156, NĐ 128 và NĐ 306 bản Công báo. | – |
| L6-012 | Đúng (khoản 2, 3 Điều 97; điểm b khoản 2 Điều 98; Điều 214 NĐ 155 sửa bởi NĐ 245). | Mỗi mệnh đề một dòng. |
| L6-013 | Đúng (khoản 2 Điều 211: 2–4 tỷ đồng hoặc tù 02–07 năm). | Thêm "hiện hành" vào đề. |
| L6-014 | Đúng (điểm b khoản 4 Điều 210: 5–10 tỷ đồng; Điều 76 có Điều 210). | Thêm "hiện hành" vào đề. |
| L4-017 | Đúng; phần giải thích thêm của người viết khớp khoản 3 Điều 3 và Điều 7 NĐ 216. | – |
| L4-018 | Đúng; danh sách 04 cơ quan khớp Điều 7 NĐ 216. | Căn cứ thêm "Điều 7 Nghị định 216/2025/NĐ-CP". |
| L4-019 | Đúng. Đã kiểm mức cũ 45 + 30 ngày theo Điều 47 Luật Thanh tra 2022. | Căn cứ thêm điểm c khoản 1 Điều 20 và Điều 7 NĐ 216. |

Không xóa câu nào. Không có câu trùng với L1/L2/L4/C1/C7/C8. Các câu gần nhất đã đối chiếu: C7-009, C1-035, L4-020…024, L1-014/015/016/066/067/068, C8-012.

## 3. Cần theo dõi
- Sau ngày 21/11/2026, xem Bộ luật Hình sự (sửa đổi), Luật Chứng khoán (sửa đổi) và Luật XLVPHC (sửa đổi) có được thông qua không. Nếu có, ghi ngày hiệu lực, rồi soát lại L6-013, L6-014, C8-012, L4-017, L6-003, L6-006 trước ngày luật mới có hiệu lực (dự kiến 01/3/2027).
- `work_l6/build_l6.py` chưa cập nhật theo các sửa trên. Không dùng script này để ghi đè `luat_6.json`.
