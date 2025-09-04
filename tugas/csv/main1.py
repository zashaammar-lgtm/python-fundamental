import csv
# panggil module csv diatas dengsn import
print("MATERI 10 -  FILE HANDLING")
print("--------------------------")
# cari posisi file note.txt
file_path = r"C:\belajar pyhon\materi-10-file\note.txt"
# open() -> buka file target
# mode r -> ready only (hanya baca)
file_catatan = open(file_path, "r")
# read() -> baca isi file note.txt
catatan = file_catatan.read()
print(f"isi catatan: {catatan}")
# tutup file note.txt
file_catatan.close()
print("-------csv-------")
anime_file_path = r"C:\belajar pyhon\materi-10-file\anime.csv"
with open(anime_file_path, "r") as file_anime:
# guanakan fungsi reader() dari module csv
    baca_file_anime = csv.reader(file_anime)
# ubah objek csv ke list agar bisa di olah
    list_anime = list(baca_file_anime)
    # keluarkan seluruh data dengan forloop
    for anime in list_anime:
        print(anime)


# print("--------ADD CVS--------")
# anime_baru = [6,"Evan", "kaijuu no-8", 10.0]
# print(f"Anime_baru: {anime_baru}")
# # mode'a' (appened) -> tambah data keakhir
# with open(anime_file_path, 'a', newline='') as file_anime:
#   # gunakan writer() dari module csv
#   write_anime = csv.writer(file_anime)
#   # fungsi writerow() -> tambah baris baru
#   write_anime.writerow(anime_baru)
#   print("✓ anime baru berhasil di catat!") 

print("----------UPDATE CSV----------")
# open file 

print("--------OPEN & EKSTRAK CSV--------")
anime_file_path = r"C:\belajar pyhon\materi-10-file\anime.csv"
data_anime = [] # list kosong
with open(anime_file_path, "r") as file_anime:
    # baca dgn fungsi reader(import csv
# panggil module csv diatas dengsn import
print("MATERI 10 -  FILE HANDLING")
print("--------------------------")
# cari posisi file note.txt
file_path = r"C:\belajar pyhon\materi-10-file\note.txt"
# open() -> buka file target
# mode r -> ready only (hanya baca)
file_catatan = open(file_path, "r")
# read() -> baca isi file note.txt
catatan = file_catatan.read()
print(f"isi catatan: {catatan}")
# tutup file note.txt
file_catatan.close()
print("-------csv-------")
anime_file_path = r"C:\belajar pyhon\materi-10-file\anime.csv"
with open(anime_file_path, "r") as file_anime:
# guanakan fungsi reader() dari module csv
    baca_file_anime = csv.reader(file_anime)
# ubah objek csv ke list agar bisa di olah
    list_anime = list(baca_file_anime)
    # keluarkan seluruh data dengan forloop
    for anime in list_anime:
        print(anime)


# print("--------ADD CVS--------")
# anime_baru = [6,"Evan", "kaijuu no-8", 10.0]
# print(f"Anime_baru: {anime_baru}")
# # mode'a' (appened) -> tambah data keakhir
# with open(anime_file_path, 'a', newline='') as file_anime:
#   # gunakan writer() dari module csv
#   write_anime = csv.writer(file_anime)
#   # fungsi writerow() -> tambah baris baru
#   write_anime.writerow(anime_baru)
#   print("✓ anime baru berhasil di catat!") 

print("----------UPDATE CSV----------")
# open file 

print("--------OPEN & EKSTRAK CSV--------")
anime_file_path = r"C:\belajar pyhon\materi-10-file\anime.csv"
data_anime = [] # list kosong
with open(anime_file_path, "r") as file_anime:
    # baca dgn fungsi reader(import csv
# panggil module csv diatas dengsn import
print("MATERI 10 -  FILE HANDLING")
print("--------------------------")
# cari posisi file note.txt
file_path = r"C:\belajar pyhon\materi-10-file\note.txt"
# open() -> buka file target
# mode r -> ready only (hanya baca)
file_catatan = open(file_path, "r")
# read() -> baca isi file note.txt
catatan = file_catatan.read()
print(f"isi catatan: {catatan}")
# tutup file note.txt
file_catatan.close()
print("-------csv-------")
anime_file_path = r"C:\belajar pyhon\materi-10-file\anime.csv"
with open(anime_file_path, "r") as file_anime:
# guanakan fungsi reader() dari module csv
    baca_file_anime = csv.reader(file_anime)
# ubah objek csv ke list agar bisa di olah
    list_anime = list(baca_file_anime)
    # keluarkan seluruh data dengan forloop
    for anime in list_anime:
        print(anime)


# print("--------ADD CVS--------")
# anime_baru = [6,"Evan", "kaijuu no-8", 10.0]
# print(f"Anime_baru: {anime_baru}")
# # mode'a' (appened) -> tambah data keakhir
# with open(anime_file_path, 'a', newline='') as file_anime:
#   # gunakan writer() dari module csv
#   write_anime = csv.writer(file_anime)
#   # fungsi writerow() -> tambah baris baru
#   write_anime.writerow(anime_baru)
#   print("✓ anime baru berhasil di catat!") 

print("----------UPDATE CSV----------")
# open file 

print("--------OPEN & EKSTRAK CSV--------")
anime_file_path = r"C:\belajar pyhon\materi-10-file\anime.csv"
data_anime = [] # list kosong
with open(anime_file_path, "r") as file_anime:
    # baca dgn fungsi reader() dari module csv