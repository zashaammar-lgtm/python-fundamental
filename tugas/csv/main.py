import csv

# Baca Semua Data Dari csv
with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

print(" ")
      
# 1. Tampilkan Semua Data
print("Semua Data")
for row in data:
    print(
        f"{row["Tanggal"]} | {row["Keterangan"]} | {row["Kategori"]} | Rp{row["Jumlah"]}")

print(" ")

#2. Hitung Semua Pengeluaran
Total = sum(int(row["Jumlah"]) for row in data)
print(f"Total Pengeluaran: Rp.{Total}")

print(" ")

# 3. Hitung Total Per Kategori
kategori_total = {}
for row in data:
    kategori = row["Kategori"]
    jumlah = int (row["Jumlah"])
    if kategori not in kategori_total:
        kategori_total[kategori] = 0
    kategori_total[kategori] += jumlah

print("😎 Pengeluaran per Kategori : ")
for kategori, jumlah in kategori_total.items():
    print(f"- {kategori} : Rp.{jumlah}")