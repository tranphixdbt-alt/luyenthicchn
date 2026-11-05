# Báo cáo phân tích CCHNEASY và kế hoạch làm bản nâng cấp

Ngày kiểm tra: 04/11/2026 · Trang: https://cchneasy.vercel.app/ (bản cập nhật ngày 03/11/2026)

## 1. Trang này là gì

**CCHNEASY** là ứng dụng web luyện thi **chứng chỉ hành nghề chứng khoán** (CCHN) năm 2026. Trang có:

- ôn luyện theo chủ đề;
- thi sát hạch mô phỏng (phần Luật trước, phần Chuyên môn sau);
- ngân hàng câu hỏi, lịch sử điểm;
- tóm tắt quy chế thi 2026 và danh mục tài liệu.

Người đứng tên trên trang là **Nguyễn Duy Khánh**. Trang có số điện thoại, nhóm Zalo, và **link cùng mã QR mở tài khoản Vietcap kèm mã giới thiệu**. Như vậy cách kiếm tiền là thu hút người học rồi mời mở tài khoản chứng khoán. Trang tự ghi "không phải website chính thức của UBCKNN".

## 2. Cách trang được làm (kỹ thuật)

| Hạng mục | Thực tế |
|---|---|
| Lưu trữ | Vercel, trang tĩnh, **một file HTML duy nhất ~1 MB** |
| Mã nguồn | JavaScript thuần ~27 KB, không dùng framework, CSS viết trực tiếp |
| Dữ liệu | Toàn bộ 829 câu hỏi nhúng sẵn trong file dạng JSON. Không có máy chủ, không có cơ sở dữ liệu |
| Mạng | Chính sách bảo mật chặn mọi kết nối ra ngoài, nên chạy offline được |
| Lưu tiến độ | Bộ nhớ trình duyệt (khóa `cchneasy_v1`); có xuất/nhập file JSON để sao lưu |
| Giao diện | Sáng/tối, có bản điện thoại, phím tắt (1–4 chọn đáp án, ←/→ đổi câu, B đánh dấu), in kết quả |
| Tài khoản | Không có. Không đồng bộ giữa các thiết bị |

**10 màn hình:**
1. Tổng quan
2. Ôn luyện: lọc theo phần, môn, chủ đề, dạng câu, độ khó, câu sai, câu chưa làm, câu đã lưu.
3. Thi sát hạch: 3 loại chứng chỉ, 35 câu/phần, đồng hồ riêng từng phần, có chế độ thi lại riêng một phần.
4. Ngân hàng câu hỏi (có tìm kiếm)
5. 8 môn SRTC
6. Lịch sử
7. Quy chế thi 2026
8. Slide & đề cương
9. Liên hệ & QR
10. Cài đặt

## 3. Dữ liệu câu hỏi

**829 câu, gồm 428 câu Luật và 401 câu Chuyên môn, chia 117 chủ đề.**

| Nguồn | Số câu |
|---|---|
| File người dùng gửi "luyen-thi-cchn-moigioi.html" | 472 |
| PDF "216 câu PTĐT" (tài liệu cũ) | 90 |
| File Excel "48 câu" | 45 |
| Trang tự biên soạn | 222 |

- **Câu bị gắn cờ:** trang tự gắn cờ **136 câu "cần rà soát"** và không đưa nhóm này vào đề thi.
- **Lệch giữa các môn:**

  | Môn | Số câu |
  |---|---|
  | Pháp luật | 428 |
  | Phân tích & đầu tư | 181 |
  | Môi giới | 40 |
  | Tư vấn tài chính & BLPH | 37 |
  | Quản lý quỹ | 36 |
  | Phân tích BCTC | 31 |
  | Phái sinh | 28 |
  | Cơ bản CK | **12** |

- **Đáp án B đúng ở 54% số câu.** Khi thi, trang có đảo thứ tự phương án nên không lợi dụng được. Nhưng ở mục Ngân hàng và khi tắt đảo phương án thì sự lệch này lộ ra.

## 4. Kiểm chứng quy chế thi trên trang

Đối chiếu với thông báo của UBCKNN/Hội đồng thi năm 2026 và NĐ 245/2025:

| Trang ghi | Kết quả | Căn cứ |
|---|---|---|
| Thi 2 phần: Luật + Chuyên môn | ✅ Đúng | NĐ 245/2025, Điều 1 khoản 73 (bổ sung khoản 5a Điều 213 NĐ 155) |
| Môi giới 60'+60', Phân tích tài chính 75'+75', Quản lý quỹ 90'+90' | ✅ Đúng | Thông báo lịch thi đợt III/2026 |
| Đạt khi đúng từ 60% ở **mỗi** phần, không bù điểm | ✅ Đúng | Thông báo 01/2026 và 09/2026 của Hội đồng thi |
| Được thi lại phần chưa đạt | ✅ Đúng, nhưng thiếu ý | NĐ 245: thi lại trong 01 năm **hoặc** ở đợt thi liền kề tiếp theo; quá hạn thì thi lại cả hai phần |
| Không phúc khảo | ✅ Đúng | Thông báo 01/2026, 09/2026 |
| **35 câu/phần** | ❌ Không tìm thấy căn cứ | Không văn bản chính thức nào công bố số câu. Chính trang cũng ghi là "chưa xác minh" |

**Các điểm trang chưa nói:**
- **TT 135/2025/TT-BTC** đã thay TT 197/2015 từ 09/02/2026. Thông tư mới:
  - miễn học môn Cơ bản cho người tốt nghiệp khối Kinh tế;
  - miễn học môn Pháp luật cho người tốt nghiệp Luật kinh tế;
  - công nhận tương đương với CFA, CIIA, ACCA;
  - cấp chứng chỉ điện tử;
  - bắt buộc đào tạo tối thiểu 8 giờ/năm từ 01/01/2027.
- **Lệ phí thi** 1.000.000 đ cho mỗi loại chứng chỉ.

## 5. Kết quả soát toàn bộ 829 câu

**Cách soát:**
- **Câu Luật:** đối chiếu với văn bản hiện hành đã tải về, gồm:
  - Luật Chứng khoán hợp nhất (VBHN 24/2025);
  - NĐ 155/2020 cùng các điều đã được NĐ 245/2025 sửa;
  - NĐ 156, NĐ 158, NĐ 306;
  - các thông tư 121, 96, 98, 91, 99, 135, 08/2026, 102/2025, 136/2025.
- **Câu tính toán:** tính lại bằng Python.

Toàn bộ kết quả từng câu nằm ở `soat_xet/ket_qua_soat_829_cau.csv`.

### Nhóm 693 câu trang đang dùng để luyện và thi

| Kết luận | Luật (418) | Chuyên môn (275) |
|---|---|---|
| Đúng | 314 | 269 |
| **Sai đáp án hoặc lỗi thời do luật đã đổi** | **15** | 0 |
| Sai căn cứ trích dẫn (đáp án vẫn đúng) | 32 | 0 |
| Đề chưa chặt / có thể hiểu hai cách | 9 | 5 |
| Lời giải viết sai (đáp án đúng) | 0 | 1 |
| Chưa kiểm được vì thiếu văn bản | 48 | 0 |

Ghi chú về các con số trong bảng:
- 48 câu "chưa kiểm được" phần lớn thuộc quy chế giao dịch ký quỹ (QĐ 87/QĐ-UBCK), Luật Doanh nghiệp và Bộ luật Hình sự.
- Phần Chuyên môn đang dùng rất tốt: **98% đúng**.
- Rủi ro nằm ở **phần Luật**, vì luật thay đổi nhiều trong 2025–2026.

**Ví dụ câu sai hoặc lỗi thời:**

| Câu | Vấn đề |
|---|---|
| src-0432, 0433, 0435, 0427 | **TT 102/2025** đã bỏ quy định "25% vốn điều lệ tối thiểu cho CTCK phái sinh", nên đáp án cũ sai |
| src-0203 | **NĐ 245** sửa Điều 293: khoản vay trên 10% tổng tài sản với cổ đông sở hữu ≥51% nay phải do **ĐHĐCĐ** duyệt, không phải HĐQT |
| src-0345, 0347 | NĐ 245 đã bãi bỏ một số căn cứ hủy niêm yết mà câu hỏi vẫn dùng |
| src-0119 | **TT 08/2026** đổi quy trình báo cáo của CTCK |
| src-0173 | **TT 136/2025** bỏ trần 0,5% phí phát hành ETF |
| src-0079 | **NĐ 306/2025** bỏ yêu cầu 220% vốn khả dụng trong 12 tháng với kinh doanh phái sinh |
| src-0137 | Sai đáp án: chào bán ra công chúng cho dự án mà bán được dưới 70% thì đợt chào bán bị hủy |
| src-0451 (nhóm gắn cờ) | Cấp CCHN nay là **30 ngày kể từ khi công bố kết quả thi** (NĐ 245), không còn 7 ngày làm việc |

### Nhóm 136 câu trang đã gắn cờ

Trong nhóm này có **18 câu sai đáp án** (đều ở môn Chuyên môn), 25 câu lỗi chữ do chép từ PDF, và 7 câu có phương án kiểu "a và c" bị hỏng khi đảo thứ tự. Ví dụ:
- **Lãi trả trước 10%:** tương đương 11,1% trả sau (10/90), không phải 11%.
- **Câu CAPM:** lợi suất yêu cầu 17% lớn hơn lợi suất kỳ vọng 16%, nên đáp án phải là "không đầu tư".
- **Đa dạng hóa:** nhiều câu cho rằng cổ phiếu tương quan dương thì không giảm được rủi ro. Điều này sai: tương quan dưới +1 vẫn giảm rủi ro.

→ Việc trang loại nhóm này khỏi đề thi là đúng. Tuy vậy, chúng vẫn hiện trong mục Ngân hàng (có kèm cảnh báo).

## 6. Lỗi và điểm yếu khác

1. **Đề Chuyên môn của chứng chỉ Môi giới lẫn môn ngoài chương trình.**
   - Mô phỏng 2.000 đề cho thấy khoảng **25% câu** (~9/35) lấy từ BLPH, Quản lý quỹ, Phái sinh, BCTC.
   - Theo NĐ 155 Điều 213, Môi giới chỉ cần Cơ bản, Pháp luật, Phân tích & đầu tư, Môi giới & tư vấn.
   - Trang tự thừa nhận "chứng chỉ khác vẫn dùng dữ liệu môi giới".
2. **Cả 11 link "↓ Tệp trong ZIP" ở mục Slide & đề cương đều lỗi 404.** Mục này chỉ là danh mục tên file (117 tài liệu nằm trong 2 file ZIP không công khai).
3. **Câu hỏi không ghi ngày hiệu lực** của văn bản. Khi luật đổi thì không biết câu nào cần sửa.
4. **Tiến độ chỉ nằm trong một trình duyệt.** Xóa dữ liệu hoặc đổi máy là mất.
5. **Thiếu các công cụ học hiệu quả:**
   - ôn lặp lại ngắt quãng;
   - theo dõi mức nắm vững từng chủ đề theo thời gian;
   - tra cứu điều luật;
   - bảng công thức và máy tính tài chính;
   - nút báo lỗi câu hỏi.
6. **Chế độ thi chỉ có 1 cấu hình 35 câu/phần**, mà con số này chưa được xác minh.

## 7. Tài liệu đã tải về (`tai_lieu_phap_ly/`, 51 file, ~178 MB, đều từ nguồn chính thức)

Nguồn: ssc.gov.vn, congbao.chinhphu.vn, datafiles.chinhphu.vn, srtc.org.vn.

- **Quy chế thi:**
  - TT 135/2025 (bản tiếng Việt và tiếng Anh);
  - các thông báo 01, 09, 10, 11/2026 của Hội đồng thi kèm phụ lục: đối tượng, hồ sơ, lịch, nội quy, hướng dẫn thi trên máy;
  - bản tổng hợp nguyên văn 10 thông báo (file `.md`).
- **Luật:**
  - Luật Chứng khoán 54/2019;
  - Luật 56/2024;
  - **Luật Chứng khoán hợp nhất VBHN 24/2025.**
- **Nghị định:**
  - NĐ 155/2020 và NĐ 245/2025 (cả bản tiếng Anh);
  - NĐ 156/2020, NĐ 158/2020, NĐ 128/2021, NĐ 306/2025.
- **Thông tư:**
  - 121/2020 + VBHN 09/2026;
  - 96/2020, 91/2020 + 102/2025, 99/2020;
  - 98/2020 + 136/2025 + VBHN 04/2026;
  - 68/2024, 08/2026;
  - VBHN 17/2026 (xử phạt).
- **SRTC:** giới thiệu 8 chương trình đào tạo chuyên môn.

**Chưa lấy được:**
- **Số câu chính thức mỗi phần:** không văn bản nào công bố.
- **Bản hợp nhất NĐ 155 + 245 (VBHN 48):** là bản scan 244 MB nên chỉ lấy phụ lục.
- **QĐ 87/QĐ-UBCK (ký quỹ), Luật Doanh nghiệp 2020, TT 119/120/2020:** cần tải thêm để soát nốt 48 câu chưa kiểm được.
- **Đề cương chi tiết từng môn của SRTC:** chưa tải được.

`phan_tich_web/` chứa bản lưu trang, dữ liệu tách ra và ảnh chụp từng màn hình. Đây là **tài liệu để nghiên cứu, không dùng lại**.

## 8. Đề xuất bản nâng cấp

**Giai đoạn 1 — Bản dùng được (lõi):**
- **Ngân hàng câu hỏi của riêng mình.** Mỗi câu có:
  - căn cứ đến từng điều khoản;
  - ngày hiệu lực của văn bản;
  - trạng thái kiểm duyệt (nháp → đã soát → đã duyệt).
  - Câu chưa duyệt không vào đề.
- **Đề thi đúng chương trình từng chứng chỉ**, theo NĐ 155 Điều 213 đã sửa:

  | Chứng chỉ | Các môn chuyên môn |
  |---|---|
  | Môi giới | Cơ bản, Phân tích & đầu tư, Môi giới & tư vấn |
  | Phân tích tài chính | Như Môi giới + BLPH + BCTC |
  | Quản lý quỹ | Như Phân tích tài chính + Quản lý quỹ & tài sản |

  Số câu mỗi phần **cho chỉnh được**, vì chưa có số chính thức.
- **Chấm theo quy chế 2026 đã xác minh:** đúng từ 60% mỗi phần; thi lại một phần trong 1 năm hoặc ở đợt kế tiếp.
- **Đảo phương án an toàn:** giữ cố định các phương án kiểu "Tất cả các ý trên"; cân bằng vị trí đáp án đúng khi biên soạn.
- **Cài được lên điện thoại và chạy offline** như trang gốc.

**Giai đoạn 2 — Học hiệu quả hơn:**
- Ôn lặp lại ngắt quãng câu sai; bản đồ nắm vững theo chủ đề; ước tính khả năng đỗ từng phần.
- **Thư viện văn bản pháp luật hợp nhất**, tra theo điều. Mỗi câu hỏi có nút "xem điều luật".
- Thẻ ghi nhớ các con số hay thi: mức vốn, tỷ lệ, thời hạn.
- Bảng công thức kèm máy tính: giá trị thời gian của tiền, trái phiếu, CAPM, chỉ số tài chính.
- Trang "Thay đổi pháp luật 2025–2026" (Luật 56, NĐ 245, TT 135, NĐ 306…).
- Nút báo lỗi câu hỏi.

**Giai đoạn 3 — Mở rộng:**
- Tài khoản và đồng bộ nhiều thiết bị; nhóm học, bảng xếp hạng.
- Trang quản trị nội dung: nhập và kiểm tra câu hỏi, cảnh báo khi văn bản bị sửa đổi.
- (Tùy chọn) Trợ lý giải thích có trích điều luật.

## 9. Lưu ý pháp lý khi làm trang tương tự

- **Văn bản quy phạm pháp luật không được bảo hộ quyền tác giả** (Điều 15 Luật Sở hữu trí tuệ). Có thể dùng, trích dẫn và đưa toàn văn lên trang.
- **Không sao chép** của CCHNEASY:
  - ngân hàng câu hỏi;
  - tên, thương hiệu, giao diện nhận diện;
  - thông tin liên hệ và link giới thiệu.
- **Không đăng lại** giáo trình SRTC, slide hay đề ôn thi của người khác khi chưa được phép.
- **Ghi rõ** "không phải trang chính thức của UBCKNN" và "không bảo đảm kết quả thi".
