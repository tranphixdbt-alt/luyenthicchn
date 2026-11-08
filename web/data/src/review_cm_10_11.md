# Review cm_10.json + cm_11.json (second pass, 2026-11)

20 questions reviewed (C10-001..012, C11-001..008). None was deleted. Backups of the originals: `work_review_c10/cm_10.orig.json`, `cm_11.orig.json`. All edits are in `work_review_c10/edits.py` (it rebuilds both files from the backups). `work_review_c10/verify.py` recomputes every number, asserts each key and distractor, checks the quotes verbatim against `src`, and checks style (NEGATIVE words in caps, no option naming another, option-length ratio). `work_review_c10/dups.py` gives each item's overlap with the rest of `questions.json`: highest Jaccard 0,43 (C10-002 ~ C6-011, a different fact). No duplicates. `python3 -I web/tools/kiem_tra.py`: OK, 703 câu. The only warnings are luat_3/luat_4 missing and C2-085 ~ C2-086, which are not in these files.

All original keys were correct. Numeric keys: C11-007 = 40.000.000 đ (2nd smallest of the four options), C11-008 = 2.500 đ (3rd smallest).

## Flagged risks
- **Lecture-only customer labels.** C10-004 and C10-009 tested the labels themselves (“quan liêu/xã hội”, “có phương pháp”, with “tự phát” among the options). Both were rewritten so the stem describes the behaviour and asks for the fitting approach, which makes the key follow from the description. The labels now appear only in `e`, as “bài giảng gọi là…”. C10-005 asked about the “độc tài” type by name; its stem now describes the behaviour without the label. C10-006 (giao tiếp bổ sung/đối xứng/song song) was kept: these are the standard complementary/symmetrical/parallel patterns from communication theory, not a customer typology, and `e` defines each one.
- **C11-007.** The stem now states every assumption: the account holds only K and the loan; no deposits, withdrawals or other trades; each day is valued at the previous trading day's close; giá trị thực có = giá trị thị trường hiện hành − dư nợ; interest and fees are ignored. It also states explicitly which days the three closes belong to.
- **Margin ratios.** No item presents a ratio as Vietnamese law. The example ratios in `e` (C11-003, C11-005) are now worded “giả sử”. Note that the writer said no legal text covers margin trading, but TT 120/2020 (VBHN 08/VBHN-BTC/2026) does: khoản 10 Điều 2 defines giao dịch ký quỹ, and Điều 9 covers the contract, the stock list, the ban on foreign investors, the initial/maintenance ratios “theo hợp đồng” and lệnh gọi ký quỹ bổ sung. These provisions were added to the basis and `e` of C11-001, 003, 004, 005 and 006. TT 08/2026 does not amend Điều 2 khoản 10 or Điều 9 of TT 120 (checked against the SSC English text).

## Per item
- C10-002: the key was the longest option by a wide margin, so it was shortened (wording unchanged in substance). The quote (khoản 9 Điều 4) is verbatim and was not amended by Luật 56/2024.
- C10-004: rewritten (see above). Key: tài liệu đầy đủ, chính xác, đúng thủ tục, cho thời gian cân nhắc.
- C10-005: stem rewritten without the label. Options rebalanced; the key had been the longest.
- C10-006: key shortened (it had been the longest).
- C10-009: rewritten as a fitting-approach item. The customer trades on impulse with high turnover. Key: chỉ ra chi phí giao dịch dồn dập, lập kế hoạch có kỷ luật. `e` gives an illustration labelled “giả sử”: 20 × 0,4% = 8%/năm.
- C10-010, C10-011: options rebalanced; the key had been the longest.
- C10-012: key and quote verified against VBHN 09/2026 and TT 08/2026 Điều 10 khoản 1. `e` now says that khoản 1 Điều 15 TT 121 was itself amended by Điều 11 TT 08/2026, and notes the original 2020 wording.
- C11-001: the stem and options were reworded away from the handout's structure. Basis is now khoản 10 Điều 2 TT 120 and `src` points to TT 120.
- C11-002: options rebalanced.
- C11-003: the worked example in `e` is labelled “giả sử” and shown step by step. Basis is now khoản 1, 6 Điều 9 TT 120.
- C11-004: distractors evened out (each contains one item outside khoản 3 Điều 123). TT 120 khoản 5 Điều 9 added.
- C11-005: options balanced, the example in `e` labelled “giả sử”, and the TT 120 khoản 6 Điều 9 rule (lệnh gọi ký quỹ bổ sung) added.
- C11-006: distractor A reworded; key shortened; TT 120 basis added.
- C11-007: assumptions completed (see above). Distractor 58.000.000 (forgetting the debt) became trivial once the formula was given in the stem, so it was replaced by 42.000.000 (valuing at the purchase price). `e` lists each error with its arithmetic.
- C11-008: stem now states that the whole salary is spread evenly over the calls and replaces the lowercase “không tính” with “bỏ qua”. `e` shows the arithmetic behind each distractor.
- C10-001, 003, 007, 008: no change.
