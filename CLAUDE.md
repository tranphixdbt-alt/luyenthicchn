# BT-INVEST – trang luyện thi CCHN chứng khoán

Trang: https://luyenthicchn-dist.vercel.app (Vercel tự triển khai `web/dist` khi đẩy lên `main`). Trả lời người dùng bằng tiếng Việt.

## Khi người dùng gửi tài liệu (Word, PDF, slide, bộ câu hỏi…): tự làm đủ quy trình, không cần hỏi lại

1. **Chuyển sang .md** bằng skill `chuyen-md` (`bash .claude/skills/chuyen-md/to_md.sh <file> <ra.md>`), lưu vào `soat_xet/<tên_nhóm>/` (thư mục này bị .gitignore: tài liệu của bên thứ ba không đưa lên GitHub). Gửi file .md cho người dùng.
2. **Rà soát từng câu/ý**: kết luận Đúng / Sai / Lỗi thời / Mơ hồ, có căn cứ. Luật hiện hành lấy trong `tai_lieu_phap_ly/van_ban_txt/` (thiếu văn bản thì tải bản chính thức từ congbao.chinhphu.vn, ssc.gov.vn…, dòng đầu ghi nguồn + ngày). Bài tính thì tự tính lại bằng Python.
3. **Đối chiếu ngân hàng** `web/data/questions.json`: ý đã có thì không thêm; nếu tài liệu cho thấy câu của ta sai/lỗi thời/kém hơn thì sửa câu của ta trong file nguồn `web/data/src/*.json` (giữ id).
4. **Viết câu mới** cho ý còn thiếu vào file nguồn mới (`cm_N.json` mã `CN-xxx`, hoặc `luat_N.json` mã `LN-xxx`) theo `web/data/src/SCHEMA.md`, rồi thêm tên file vào `FILES` trong `web/tools/kiem_tra.py`. Viết bằng lời của ta, không chép nguyên văn tài liệu; 4 phương án, một đáp án; câu Luật phải có trích nguyên văn (`quote` + `src`); quy định giao dịch có thể đổi theo hệ thống KRX thì đưa thành giả định trong đề.
5. **Soát chéo** bằng một agent khác (tính lại số, kiểm căn cứ, trùng lặp, câu chữ); ghi `review_*.md`.
6. **Kiểm tra và xuất bản**: `python3 -I web/tools/kiem_tra.py` (phải OK) → cập nhật số câu trong `web/brand/brand.html` và chụp lại `og.png` nếu tổng số câu đổi → `python3 -I web/tools/build.py` → chạy `node web/tools/kiem_tra_thong_ke.js` và các bài kiểm thử `web/tools/*.mjs` (truyền URL trang) → commit, push `main`, kiểm tra trang thật.
7. **Báo cáo** ngắn: bảng kết luận, số câu đã có, số câu sửa, số câu mới theo môn, điểm chưa chắc; gửi kèm báo cáo chi tiết trong `soat_xet/`.

## Ghi nhớ
- Ứng dụng: `web/index.html` + `web/app.js` (JS thuần), dữ liệu `web/data/`, build ra một file `web/dist/index.html`. Hàm thống kê ẩn danh: `web/api/thong-ke.js` dùng kho Redis của dự án Vercel qua biến `REDIS_URL` (đã nối 11/2026; mã giả `Z9-999` trong kho là bản ghi thử, trang bỏ qua). Kiểm thử: `cd web && npm install && node tools/kiem_tra_thong_ke.js` (cần `redis-server`).
- Khóa localStorage `docchn_v1`: không đổi, để người dùng không mất tiến độ.
- Người dùng đang ôn để thi môn Pháp luật và Môi giới chứng khoán.
