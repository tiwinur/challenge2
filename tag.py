# if else
print("Menggunakan if else")

# Fungsi untuk menghitung tip
def hitung_tip(tagihan):
    if tagihan >= 50 and tagihan <= 300:
        tip = tagihan * 0.15
    else:
        tip = tagihan * 0.2
    return tip

# Data uji
data_uji = [275, 40, 430]

# Iterasi melalui data uji
for tagihan in data_uji:
    tip = hitung_tip(tagihan)
    total_nilai = tagihan + tip
    print(f"Tagihannya {tagihan}, tipnya {tip}, dan total nilainya {total_nilai}")




# ternary
print("Menggunakan ternary") 

# Fungsi untuk menghitung tip dengan operator ternary
def hitung_tip(tagihan):
    tip = tagihan * 0.15 if 50 <= tagihan <= 300 else tagihan * 0.2
    return tip

# Data uji
data_uji = [275, 40, 430]

# Iterasi melalui data uji
for tagihan in data_uji:
    tip = hitung_tip(tagihan)
    total_nilai = tagihan + tip
    print(f"Tagihannya {tagihan}, tipnya {tip}, dan total nilainya {total_nilai}")
