# Soát lần 2 thẻ ghi nhớ PT, BC, BL, QU (200 thẻ, 11/2026)

Đối chiếu: Luật CK (VBHN 102/2026), NĐ 155 + NĐ 245/2025, TT 98 (VBHN 04/2026), TT 99/2020 (bản tiếng Việt, caselaw.vn; TT 88/2025 chỉ sửa khoản 4 Điều 29), TT 121 (VBHN 09/2026), VAS 24 (đoạn 22–23), TT 99/2025/TT-BTC (chế độ kế toán DN, hiệu lực 01/01/2026, thay TT 200/2014; đổi tên Bảng cân đối kế toán thành Báo cáo tình hình tài chính). Ví dụ số tính lại trong `work_review_the_1/kiem_so.py`; sửa áp bằng `work_review_the_1/sua_the.py`. Trùng lặp soát chéo với LU, PS, CB, MG. 176 thẻ đúng, giữ nguyên; 24 thẻ sửa:

- PT-05: phần niên kim vĩnh viễn tăng trưởng đều trùng mô hình Gordon (PT-32) → chỉ giữ niên kim vĩnh viễn đều, niên kim hoãn k kỳ, thêm ví dụ cổ tức ưu đãi.
- PT-11: hệ thức Cov = ρσAσB trùng PT-12 → bỏ, thêm ý Cov = 0, giải thích pᵢ.
- PT-37: công thức P/B = giá/BVPS trùng BC-33 → thay bằng P/B hợp lý (ROE − g)/(r − g), đã kiểm bằng Gordon.
- PT-39: ý "khi nào dùng FCFF" trùng BL-46 → thay bằng quan hệ FCFF = FCFE + lãi vay × (1 − t) − vay ròng.
- BC-05: dựa vào mã mẫu và chế độ kế toán cũ → nêu bộ BCTC theo TT 99/2025 (Báo cáo tình hình tài chính, trước gọi là Bảng cân đối kế toán), bỏ mã mẫu, căn cứ Điều 17 TT 99/2025 + VAS 21.
- BC-08: mặt trước dựa vào mẫu B03-DN; căn cứ chưa nêu đoạn → bỏ mã mẫu, nêu phạm vi (DN không phải ngân hàng, tổ chức tài chính), căn cứ VAS 24 đoạn 22–23.
- BC-09: viện dẫn mẫu B03-DN → nói "ở Việt Nam, điểm xuất phát là LN trước thuế", bỏ mã mẫu.
- BC-27: ROE = ROA × hệ số nhân vốn chủ trùng BC-28 (DuPont) → thay bằng lưu ý BCTC hợp nhất (phần cổ đông công ty mẹ), VCSH âm/nhỏ.
- BC-32: diễn giải "P/E cao do g cao, r thấp" trùng PT-36 → thay bằng P/E trượt, P/E dự phóng, EPS âm.
- BL-07: trùng LU-35 (hạn mức bảo lãnh ≤ VCSH và ≤ 15 lần) → thay bằng cam kết của cổ đông lớn khi IPO (≥ 20% vốn điều lệ, 01 năm; điểm đ khoản 1 Điều 15 Luật CK).
- BL-08: căn cứ chưa ghi văn bản hợp nhất → thêm VBHN 09/VBHN-BTC 2026.
- BL-09: như BL-08.
- BL-10: như BL-08.
- BL-11: như BL-08.
- BL-13: căn cứ chưa xác nhận tình trạng sửa đổi → ghi Điều 42 NĐ 155 không bị NĐ 245/2025 sửa.
- BL-18: "thưởng cổ phiếu" không phải chi phí ràng buộc theo Jensen–Meckling → định nghĩa lại chi phí ràng buộc (do người quản lý tự chịu).
- BL-20: như BL-08.
- BL-34: công thức TERP trùng MG-42 (giá tham chiếu điều chỉnh) → chỉ hỏi giá trị một quyền: (P₀ − S)/(N + 1) = (Pₓ − S)/N, ví dụ 2.000 đ (khớp C3-017).
- BL-38: giá điều chỉnh P/(1 + k) là trường hợp riêng của MG-42 → thay bằng tỷ lệ sở hữu không đổi, EPS, BVPS giảm còn 1/(1 + k).
- BL-45: mặt trước gắn với công thức xác định giá trị phần vốn nhà nước khi cổ phần hóa nhưng thiếu các khoản trừ theo quy định → viết lại thành phương pháp tài sản nói chung, kèm ưu, nhược điểm.
- QU-09: diễn đạt lỏng → nêu rõ lệnh bán − lệnh mua (kể cả chuyển đổi) ≥ 5% NAV, thời điểm áp dụng 12/02/2026.
- QU-13: căn cứ chỉ dẫn Điều 24 (quỹ đóng) → thêm khoản 3 Điều 110 Luật CK và khoản 5, 6 Điều 35 TT 98 cho quỹ mở.
- QU-14: SAI theo bản dịch tiếng Anh: ngoại lệ là "quỹ mở trái phiếu" (không phải mọi quỹ mở) có giá trị giao dịch năm dưới 300 tỷ; quỹ "chưa đủ 06 tháng tính đến hết năm thành lập" → sửa theo bản tiếng Việt, ghi rõ căn cứ.
- QU-46: hệ số Sortino ngoài giáo trình SRTC, không có trong ngân hàng câu hỏi → thay bằng cơ cấu phí "2 và 20" của quỹ phòng hộ (ví dụ khớp C3-058). Giữ QU-45 (M²): đúng, cùng nhóm chỉ số Sharpe/Treynor trong giáo trình.
