# BT-INVEST — luyện thi chứng chỉ hành nghề chứng khoán

Trang web tĩnh (HTML + CSS + JavaScript thuần), không cần máy chủ hay cơ sở dữ liệu. Tiến độ học lưu trong trình duyệt của từng người.

## Cấu trúc
| Đường dẫn | Nội dung |
|---|---|
| `index.html` | Giao diện và CSS (dạng phần thân trang) |
| `app.js` | Toàn bộ logic: ôn luyện, ôn lặp lại, thi thử, kết quả, ngân hàng, thẻ ghi nhớ, máy tính, thư viện luật, cài đặt |
| `data/questions.json` | Ngân hàng câu hỏi đã gộp và kiểm tra (do `tools/kiem_tra.py` sinh ra) |
| `data/src/*.json` | Câu hỏi gốc theo nhóm biên soạn; sửa câu ở đây rồi chạy lại kiểm tra |
| `data/luat_ck.json` | Luật Chứng khoán hợp nhất theo từng điều (do `tools/tach_luat.py` sinh ra) |
| `data/so_lieu.json`, `data/thay_doi.json`, `data/van_ban.json` | Thẻ số liệu, thay đổi pháp luật 2025–2026, danh mục văn bản |
| `pwa/` | Manifest và service worker để cài lên điện thoại, chạy offline |
| `brand/` | Logo, avatar, biểu tượng app và ảnh chia sẻ BT-INVEST (`brand/out/*.png`) |
| `vendor/` | Thư viện bên ngoài đã tải sẵn (canvas-confetti) |
| `THAM_KHAO_THIET_KE.md` | Skill và repo thiết kế đã dùng/tham khảo |
| `dist/` | Bản đóng gói một file `index.html` để đưa lên mạng (do `tools/build.py` sinh ra) |

## Lệnh thường dùng
```bash
python3 -I tools/kiem_tra.py   # gộp + kiểm tra câu hỏi (trích dẫn phải khớp văn bản gốc)
python3 -I tools/build.py      # đóng gói dist/ (đặt SITE_URL nếu đổi tên miền, để ảnh chia sẻ link đúng)
cd dist && python3 -m http.server 8000   # xem thử tại http://localhost:8000
```

## Đưa lên mạng
- **Vercel**: tạo project mới, chọn thư mục `dist` làm Output Directory (không cần build command), hoặc chạy `npx vercel dist`.
- **GitHub Pages / Netlify**: tải nội dung thư mục `dist` lên.
- File `dist/index.html` cũng mở được trực tiếp bằng trình duyệt (chạy offline).

## Thêm hoặc sửa câu hỏi
Mỗi câu theo `data/src/SCHEMA.md`: 4 phương án, một đáp án, giải thích, căn cứ; câu Luật phải có `quote` trích nguyên văn và `src` là tên file văn bản trong `../tai_lieu_phap_ly/van_ban_txt/`. Khi luật thay đổi, cập nhật văn bản, sửa câu bị ảnh hưởng, chạy lại `kiem_tra.py` và `build.py`.

## Lưu ý pháp lý
Văn bản quy phạm pháp luật không được bảo hộ quyền tác giả (Điều 15 Luật SHTT) nên được trích dẫn tự do. Câu hỏi trong ứng dụng được biên soạn mới; không sao chép ngân hàng câu hỏi hay giáo trình của đơn vị khác. Ứng dụng không phải trang chính thức của UBCKNN và không bảo đảm kết quả thi.
