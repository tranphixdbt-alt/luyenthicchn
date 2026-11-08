# Review luat_5.json (second pass, 2026-11-08)

I checked all 35 L5 items against the texts in force in Nov 2026: Luật CK (VBHN 102/2026, which consolidates Luật 56/2024), NĐ 155 with the amendment list of NĐ 245/2025 (Art 1 items 1–80, Art 2.5 repeals), and NĐ 200/2026 (Art 5, 6, 9, 10, 13, 15–19, 49, 50). TT 115/2025 was not used. All 35 keys hold. Every quote is verbatim and supports its key or the deciding statement. No item was deleted and no id changed.

Duplicates: I compared the 41 bank items in the topics Chào bán ra công chúng, Chào bán riêng lẻ (& phát hành khác), Chào bán trái phiếu, Chào mua công khai and Nhà đầu tư chuyên nghiệp, plus about 80 keyword hits elsewhere (L1-039/040/042, L2-014..017, C1-070, C6-021…). No L5 item duplicates any of them. The closest overlaps test a different point:
- L5-022 vs L1-040 (L5-022 adds the exact-35% case and the 26→34% and 56→64% non-cases).
- L5-025 vs L2-016 (L5-025 adds the earlier-tender-offer floor).

An 8-gram check against the slides found no copied wording. The edit script is `scratchpad/review_l5/apply.py`, and the pre-edit copies are in the same folder.

## Fixes
- **Combination items (L5-004, 007, 008, 010, 012, 015, 017, 022, 035):** each statement I–IV now has its own line (`\n`; `.qtext` uses `white-space: pre-line`). I checked each statement on its own, and exactly one option matches.
  - L5-004 I now says "khi chào bán cổ phiếu ra công chúng". Cl. 4 Art 7 NĐ 155 is tied to public share offerings.
  - L5-022 stem: the ratio basis is stated, and "qua sàn" was dropped.
  - L5-035 II now reads "trái phiếu này"; its explanation and basis add Art 9.1(đ) and Art 10.2(a) NĐ 200.
  - Lead-in wording changed from "gồm" to "thuộc điều kiện … là".
- **L5-013:** the key used to depend on treating quỹ khen thưởng, phúc lợi as a liability. That is accounting knowledge, not in NĐ 155. The item is rewritten to test the NĐ 245 change in Art 62.2(a) ("BCTC năm gần nhất được kiểm toán", which replaced "kỳ gần nhất"). The key is 95 bn, from the audited FY2025 report. The distractors are 115 bn (the old rule, using the audited H1-2026 report), 70 bn (omits the development fund) and 55 bn (omits share premium).
- **L5-032:** the bond is now issued in 07/2026. Bonds issued before 05/6/2026 follow the transitional rules in Art 50.5–6 NĐ 200, under which repurchase from dissenting holders is not required.
- **L5-018:** the stem now also lists the swapped holders' written consent, so the only remaining requirement is approval by B's general meeting.
- **L5-024:** a date convention was added ("n ngày trước ngày D" = D − n), so 23/11 is unambiguous.
- **L5-033:** the explanation now says that a public company offering in several tranches must also be a credit institution (Art 16.1 → 13.3(a)).
- **Basis:** "(không bị NĐ 245/2025 sửa đổi)" was added to L5-005, 018 and 023–029.
- **Topic:** L5-004 and 009 now use "Chào bán ra công chúng", like the other L5 items. Both topic names map to the same SYL group.

## Existing items with an over-broad "chỉ"
Under Art 31.1(b) Luật CK and Art 9.1(d) NĐ 200, an individual professional investor may buy private **convertible** bonds of a public company, securities company or fund manager without a credit rating or collateral.
- **C1-070** (cm_1.json): the stem is now limited to private non-convertible bonds without warrants offered from 01/01/2026, so "chỉ" is exact under Art 11.1b and Art 9.1(đ). The distractor about convertible bonds was replaced with "có TSĐB hoặc bảo lãnh, không cần XHTN". The basis adds NĐ 200. The key is unchanged.
- **L1-010** (luat_1.json): the stem names the bond type, and the "mọi loại" distractor now reads "Mọi trái phiếu loại này". The explanation drops the absolute "chỉ" and notes the convertible-bond exception. The key is unchanged.

## Verified, no change
L5-001, 002, 003, 005, 006, 009, 011, 014, 016, 019, 020, 021, 023, 025–031, 034. Checks made:
- L5-002: 01/7 + 90 days = 29/9.
- L5-025: max(24,000; 26,500).
- L5-026: 40,000 × 3.0/4.8 = 25,000.

`python3 -I web/tools/kiem_tra.py`: OK, 834 items. The only warning is the old near-duplicate C2-085 ~ C2-086.
