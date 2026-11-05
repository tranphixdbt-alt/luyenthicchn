# Review luat_1.json and thay_doi.json (second pass)

I checked all 95 questions against the source texts: the consolidated Securities Law (VBHN 24/2025, including Law 56/2024), ND 155 as amended by ND 245/2025, TT 135/2025 and the 2026 SSC exam notices. Every key is the single correct answer under the text in force in November 2026, and every quote appears verbatim in its source. No key changed meaning; one key moved position (L1-007: the correct answer is still D, "Trên 100 tỷ đồng"). 18 questions changed. All 17 thay_doi items were checked against the amending texts; 5 were corrected and none was deleted. The checker (work_review_l1/check.py) passes.

## luat_1.json

- L1-007: the key was the only "Trên …" option, which gave the answer away → options are now "Trên 50 tỷ" / "Từ 30 tỷ trở lên" / "Từ 100 tỷ trở lên" / "Trên 100 tỷ" (key still D), so the "trên" vs "từ … trở lên" threshold is what is tested; explanation updated.
- L1-010: the transition rule (Art 11.1(a)(b) Law 56/2024) keeps private bonds offered before 01/01/2026 under the old law, so option D ("Mọi loại trái phiếu riêng lẻ") could be argued → the stem now places the offering's disclosure in 09/2026; explanation mentions the transition rule.
- L1-015: the key (32 characters) was much shorter than the distractors (49–54) → key is now "Thao túng thị trường chứng khoán, bị nghiêm cấm".
- L1-034: Art 31b covers private offerings "đã đăng ký với UBCKNN"; ordinary private bonds are not registered with the SSC → the stem now says "đợt chào bán trái phiếu riêng lẻ đã đăng ký với UBCKNN".
- L1-036: the stem did not say what N must "đáp ứng" → it now asks whether N meets the public-company conditions in Art 32.1(a); the explanation applies Art 38.2 only if N is already a public company.
- L1-042: option A ("Được quyền buộc…") did not follow the stem "thì phải:" grammatically → reworded to "Buộc các cổ đông còn lại bán…".
- L1-051: the key (29 characters) was much shorter than the distractors (44–46) → key is now "Thành viên giao dịch đặc biệt của Sở giao dịch chứng khoán"; option A lengthened to match.
- L1-054: the key (25 characters) was much shorter than the distractors (37–55) → key is now "Chỉ cho chính ngân hàng V, không cho khách hàng".
- L1-064: option D (64 characters) was much shorter than the three parallel 96-character options → lengthened to 88 characters (meaning unchanged).
- L1-066: the basis said only "Điều 214" → now "điểm a khoản 1 Điều 214 NĐ 155 (sửa đổi bởi khoản 74 Điều 1 NĐ 245)".
- L1-069: the basis cited "khoản 73 Điều 1 NĐ 245" → now "điểm d khoản 73 Điều 1 NĐ 245" (the point that adds khoản 5a).
- L1-076: the key "Quản lý quỹ và tài sản" (22 characters) was far shorter than the distractors (≈50) → the key is now another listed CIIA/CFA II equivalent, "Chứng khoán phái sinh và thị trường chứng khoán phái sinh"; the quote was extended to include "Derivatives and the derivatives market" (287 characters); explanation updated.
- L1-083: the key was the shortest option → "…trong 30 ngày kể từ ngày phát sinh".
- L1-084: the key was the shortest option → "Giá trị tài sản ròng của quỹ tại kỳ định giá gần nhất tối thiểu 100 tỷ đồng".
- L1-085: the key (100 characters) was the longest option → shortened to 80 characters (meaning unchanged).
- L1-087: "mua lại cổ phiếu quỹ" is not the statutory wording (Art 127.3(a) says "mua lại cổ phiếu của chính mình") → key reworded to the statutory phrase.
- L1-091: option A (30 characters) was much shorter than the others (55–66) → "Chỉ BCTC năm đã kiểm toán; BCTC bán niên, BCTC quý không bắt buộc".
- L1-093: one explanation sentence ran the organisation and individual rules together ("…áp dụng cho tổ chức, cá nhân vi phạm…") → split into two clauses: organisation 03 tỷ; individual ½ (1,5 tỷ).

## thay_doi.json

- "Công ty đại chúng: bổ sung điều kiện vốn chủ sở hữu": "effective" held two dates with notes (not dd/mm/yyyy) → now "01/01/2026"; the 01/01/2026 start of the equity test is stated in "what"; added the exception in Art 11.1(d) Law 56 for companies whose ĐHĐCĐ resolved to give up public-company status before 01/01/2026.
- "Nhà đầu tư chứng khoán chuyên nghiệp…": "effective" held two dates → now "01/01/2025" (the 01/01/2026 bond rule is already stated in "what").
- "Chào bán thêm để thực hiện dự án…": "effective" held two dates → now "01/01/2025"; the ND 245 date (11/09/2025) moved into "what".
- "Thi sát hạch và cấp CCHN…": "what" said that a candidate who misses the retake deadline does not need to resubmit the degree and professional certificates; in fact this exemption is for registering a retake of the failed part (Art 213.6(c): documents under points a, b, c, e of khoản 4 only) → rewritten; also added the start dates for the 15-day and 30-day deadlines.
- "Trái phiếu chào bán ra công chúng…": "effective" held two dates → now "11/09/2025" (the ND 245 detailed rules); the Law's effective date 01/01/2025 is stated in "what".
- The other 12 items were checked against Law 56/2024, ND 245/2025, ND 306/2025, TT 102/2025, TT 136/2025, TT 08/2026 and TT 135/2025 (article numbers, figures and effective dates) and are unchanged.

## Not fully verified

- In the ND 306 item, the "before" figures (01–12 months; 10–30 million) were checked against the original text of ND 156/2020 only. The ND 128/2021 text is a scanned PDF with no text layer, so I could not confirm that ND 128 left these figures unchanged.
