# Search a source file (whitespace-collapsed): python3 -I grep.py FILEKEY "regex" [context_chars]
import re, sys, pathlib
D = pathlib.Path("/home/user/cchn_moi/tai_lieu_phap_ly")
alias = {"L": "van_ban_txt/VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt",
         "L56": "van_ban_txt/Luat_56_2024_QH15_Cong_bao.txt",
         "L56E": "van_ban_txt/Luat_56_2024_QH15_English_SSC.txt",
         "N155": "van_ban_txt/ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt",
         "N245": "van_ban_txt/ND_245_2025_ND-CP_Cong_bao_so_1403-1408_2025.txt",
         "N245E": "van_ban_txt/ND_245_2025_ND-CP_English_SSC.txt",
         "T135": "van_ban_txt/TT_135_2025_TT-BTC_English_SSC.txt",
         "UB": "UBCK_thong_bao_thi_sat_hach_2026_va_gioi_thieu_TT135_ND245.md",
         "N306": "van_ban_txt/ND_306_2025_ND-CP_English_SSC.txt",
         "T102": "van_ban_txt/TT_102_2025_TT-BTC_sua_TT91.txt",
         "T136": "van_ban_txt/TT_136_2025_TT-BTC_sua_TT98.txt",
         "T08": "van_ban_txt/TT_08_2026_TT-BTC_English_SSC.txt",
         "L19": "van_ban_txt/Luat_Chung_khoan_54_2019_QH14_Cong_bao.txt",
         "T121V": "van_ban_txt/VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt",
         "T121": "van_ban_txt/TT_121_2020_TT-BTC_Cong_bao_so_447-448_2021.txt",
         "T91": "van_ban_txt/TT_91_2020_TT-BTC_Cong_bao.txt",
         "T96": "van_ban_txt/TT_96_2020_TT-BTC_Cong_bao.txt",
         "T96E": "van_ban_txt/TT_96_2020_TT-BTC_English_SSC.txt",
         "T98V": "van_ban_txt/VBHN_04_VBHN-BTC_2026_TT98_136_hop_nhat.txt",
         "N158": "van_ban_txt/ND_158_2020_ND-CP_Cong_bao.txt",
         "N156": "van_ban_txt/ND_156_2020_ND-CP_Cong_bao.txt",
         "N48": "van_ban_txt/VBHN_48_VBHN-BTC_Phu_luc_ND155_ND245.txt"}
p = D / alias.get(sys.argv[1], sys.argv[1])
t = " ".join(p.read_text(encoding="utf-8").split())
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 300
n = 0
for m in re.finditer(sys.argv[2], t, re.I):
    n += 1
    if n > 8: print("...more"); break
    print(f"--[{m.start()}] ...{t[max(0, m.start() - ctx):m.end() + ctx]}...\n")
print("matches:", n)
