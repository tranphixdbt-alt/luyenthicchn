# Review cm_15.json (second pass, 2026-11-08)

22 questions reviewed (C15-001..022). None deleted, ids kept, no key changed meaning, but four items had options or stems rewritten (C15-007 rewritten as a new scenario). Every `quote` (14 items, CM items included, which `kiem_tra.py` does not check) was matched against its `src` with the checker's own `norm_ws`/`loose` functions: all OK. `python3 -I web/tools/kiem_tra.py`: OK, 905 questions; only warning C2-085 ~ C2-086 (outside this file).

## Main finding: the AML law has been amended (writer said "chưa bị sửa đổi")
Downloaded from congbao.chinhphu.vn (source URL + date on line 1, in `tai_lieu_phap_ly/van_ban_txt/`):
- `Luat_23_2026_QH16_sua_Luat_PCRT_NHNN_TCTD_Cong_bao_so_519_2026.txt`: Luật 23/2026/QH16 (24/8/2026, **hiệu lực 01/12/2026**). Amends Luật PCRT: k7 Đ3; adds **điểm n "Dịch vụ tài sản mã hóa" to k1 Đ4**; Đ9 k2c; Đ10; Đ12 k1; Đ19 k1; Đ22; replaces **Đ26** (still reports to NHNN); adds Đ33a; replaces **k1 Đ38**; adds k3–4 Đ39, Đ48a; replaces **Đ51**–54, 58, 59; repeals Đ55, k1 Đ64. Unchanged: Đ3 k1–2, Đ31, Đ37, Đ38 k2, Đ44.
- `NQ_66.23_2026_NQ-CP_PCRT_Cong_bao_so_463_2026_OCR.txt`: Nghị quyết 66.23/2026/NQ-CP (24/7/2026–28/02/2027; scanned PDF, OCR text). Adjusts k7 Đ3, k4 Đ10, k1 Đ12, Đ22 of the Law; Đ7 NĐ 19/2023; Đ4 TT 27/2025/TT-NHNN.
- `ND_19_2023_ND-CP_huong_dan_Luat_PCRT_Cong_bao_so_705-706_2023.txt`: NĐ 19/2023 does **not** add reporting-entity activities under k3 Đ4 (its scope: national risk assessment, KYC, beneficial owner, complex transactions, information, blacklist/transaction delay in Đ12).
- NĐ 329/2025/NĐ-CP concerns banks/AML at the International Financial Centre only, not relevant to securities companies.
- The stale note on line 1 of `Luat_Phong_chong_rua_tien_14_2022_QH15_...txt` ("không thấy luật sửa đổi") was corrected (line 1 only; text untouched).

None of the provisions used for keys changed, so all AML keys hold before and after 01/12/2026. All `basis` fields saying "chưa bị sửa đổi" were rewritten to name what Luật 23/2026 / NQ 66.23 change and that the cited clause is unaffected (C15-012, 017, 018, 019, 020, 021).

## Per-item changes
- **C15-017 (flagged risk)**: stem now asks which activities are *listed in khoản 1 Điều 4*, so the key (I, III, IV) rests on the Law text itself. `e`/`basis` note điểm n added by Luật 23/2026 and that NĐ 19/2023 adds nothing. Key unchanged.
- **C15-007**: was a trivial "bảo đảm lợi nhuận tối thiểu" KHÔNG item (third item in this file with that same giveaway key). Rewritten as a mark-up scenario (company sells bonds from its proprietary book far above market) → "cấm tăng giá quá mức (markup)"; distractors churning / cơ sở hợp lý / lưu trữ hồ sơ (best execution deliberately left out to avoid ambiguity). Churning already covered by C4-023, C8-019, C4-030; mark-up was not. Quote added: k3 Đ91 Luật CK.
- **C15-009**: two of its "true" options (conflict-of-interest monitoring, AML control) duplicated C14-024. Replaced with Đ12 k2 điểm a (supervising practitioners) and điểm d (financial safety); key (independent evaluation of the KSNB system = ban kiểm soát/kiểm toán nội bộ, Đ9) unchanged. `e` softened: Đ9 k2 is the "Ban kiểm soát, kiểm toán nội bộ" function, not strictly "kiểm toán nội bộ".
- **C15-011**: key "Mức lợi nhuận tối thiểu công ty cam kết" → "Tỷ lệ chia sẻ lãi, lỗ giữa công ty và khách hàng" (prohibited by điểm b k6 Đ4 TT 121, verified); removes the repeated giveaway.
- **C15-002**: key "Bảo đảm mức lợi nhuận tối thiểu cho CTCK" → "Can thiệp để giá chứng khoán niêm yết luôn tăng ổn định"; option 3 reworded (was truncated "…trong nước"); `e` cites k4 Đ5 Luật CK.
- **C15-001, C15-004**: stems were near-verbatim slide sentences; reworded.
- **C15-006**: removed "(như Hiệp hội Kinh doanh chứng khoán Việt Nam)". The current VASB ethics code was not verifiable, so nothing about VASB is asserted; the item rests on Đ10 Luật CK only.
- **C15-010**: key shortened (was the longest option).
- **C15-019**: `e` no longer says "(UBCKNN)" for Bộ Tài chính's AML inspection; notes new Đ26 keeps NHNN as recipient.
- **C15-020**: `e`/`basis` add Đ12 NĐ 19/2023 (who receives the delay report).

## Conceptual items (textbook only)
C15-001, 002, 004, 008, 013, 014, 015, 016 kept: each key is fixed by the stem itself or by universally used terms (best execution definition; placement → layering → integration with English labels; scenario clearly layering; shell company/structuring/commingling vs ordinary sale; effects). Distractors are not state functions / not AML methods by any reading. C15-007 rewritten (above).

## Checked, no issue
Luật CK VBHN 102/2026: Đ8 k2, Đ9 k1 c/n, Đ10, Đ43 k3, Đ46 k1 d/e/h/i, Đ89 k5/7/10, Đ91 k1/3, Đ95, Đ98 k4. TT 121 VBHN 09/2026: Đ4 k2/k6b, Đ9 k2b/k3, Đ12 k2, Đ13 k2/k3 (sửa bởi k1 Đ9 TT 08/2026), Đ15a (Đ12 TT 08/2026), Đ22 k5/k7, Đ24 k1. Luật PCRT: Đ3 k1–2, Đ4 k1, Đ26, Đ31, Đ37, Đ38, Đ44, Đ51. BLHS Đ324. Combination items (003, 005, 006, 015, 017, 018) have one statement per line and exactly one correct option. Nearest neighbours in questions.json/cm_14/cm_13 now ≤ ~0,4 Jaccard with different tested points. Topic string matches SYL in app.js.

## Open points
- Luật 23/2026 takes effect 01/12/2026; after that, a consolidated text (VBHN) of Luật PCRT should replace the 2022 Công báo file as `src`. Quoted clauses (Đ3 k1, Đ4 k1 i–l, Đ31, Đ37 k2, Đ38 k2a, Đ44 k3) are unchanged, so quotes stay valid.
- New AML content not yet covered by any question: crypto-asset service providers as reporting entities (điểm n), Đ33a signs, Đ39 k3 (good-faith reporting immunity).
- NQ 66.23 text is OCR; do not quote from it without checking the PDF.
