def hello_world():
    print("hallo dunia")
hello_world()

# fungsi biasa dengan def
def hello_world(name):
    print("hello mr.", name)
    print ("how you duing {name}?")

hello_world("shidqi")
hello_world("ammar")
hello_world("dzaky")

# fungsi anonim denagn lambada
greenting = lambda name: print (f"hello, {name} ngapa lu jelek banget dah, kek tai")
greenting("mas jon")
greenting("mas boy")
greenting("mas ken")

# map() untuk mentrasformasi data
nilai_mentah = [1.9, 4.5, 6.9, 7.1, 9.9, 0.28, 2.6]
nilai_kali_seratus = map(lambda nilai: nilai * 100, nilai_mentah)
list_nilai_kali_seratus = list(nilai_kali_seratus)
print(f"Nilai mentahan: {nilai_mentah}")
print(f"Nilai x 100: {list_nilai_kali_seratus}")

# "" artinya string walaupun dia isinya angka
nilai_string = "1000"
nilai_integer = int(nilai_string)
kalikan_dua_salah = nilai_string *2
kalikan_dua_benar = nilai_integer *2
print(kalikan_dua_salah, kalikan_dua_benar)

# daftar siswa
daftar_siswa = [
    {"nama": "dzaky", "angka": 77},
    {"nama": "ammar", "angka": 90},
    {"nama": "shidqi", "angka": 12},
    {"nama": "banu", "angka": 8},
]
print("DAFTAR ANGKA ASLI", daftar_siswa)
daftar_siswa_terurut = sorted(daftar_siswa, key=lambda siswa:
siswa['angka'])

# for loop -> mengeluarkan isi list
for siswa in daftar_siswa_terurut:
    print(siswa)
# sorting list
daftar_nama_kelas_b = ["dzaky", "ammar", "banu", "shidqi", "anugrah", "maulana",]
daftar_siswa_terurut = sorted(daftar_nama_kelas_b)
daftar_siswa_terbaik = sorted(daftar_nama_kelas_b, reverse=True)
for nama in daftar_siswa_terurut:
    print(nama)
print("----------####----------")
for nama in daftar_siswa_terbaik:
    print(nama)

# filter() menyaring data
transaksi = [25000, 10000, 13000, 15000, 20000]
transaksi_besar = filter(lambda angka: angka >= 25000, transaksi)
list_transaksi_besar = list(transaksi_besar)
print("transaksi diatas 50rb:", list_transaksi_besar)