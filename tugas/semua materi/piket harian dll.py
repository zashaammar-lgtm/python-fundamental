piket_hari_ini = ["Asep", "Budi", "Steven"]
print("PIKET HARIAN")
for i in piket_hari_ini:
    print("-", i)

print(" ")

rukun_islam = ("syahadat", "sholat", "zakat", "puasa", "haji (jika mampu)")
print("RUKUN ISLAM")
for i in range (len(rukun_islam)):
    print(f"{i + 1}, {rukun_islam[i]}")

print(" ")

kitab_pelajaran = ("kitab tajwid", "kitab fiqh", "kitab aqidh")
print("KITAB YANG DI PELAJARI")
for i in kitab_pelajaran:
    print("-", i)

print("-")

print ("BIODATA SANTRI")
boidata = {
    'nama': 'dzaky ammar banu',
    'kelas': 'X-B',
    'hafalan_juz': 5
}

for key, value in boidata. items():
    print(f"{key} -> {value}")