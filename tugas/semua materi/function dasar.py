print("MATERI 8 - FUNCTION DASAR")
print("-------------------------")
# sturktur fungsi dasar tanpa parameter
def halo_dunia():
    print("Hello World")
    print("Hallo Dunia")
# cara akses function, sertakan nama dan () nya
halo_dunia
# fungsi dengan parameter (variable di fungsi)
def sapa_sapa_gen(nama):
    print("Halo", nama, "selamat datang di HSI purworejo")
sapa_sapa_gen("ammar")
def rumus_luas_segi_tiga(alas, tinggi):
    print("Alas:", alas)
    print("Tinggi:", tinggi)
    rumusan = 1/2 * (alas * tinggi)
    print("hasil:", rumusan)
rumus_luas_segi_tiga(60, 68)

sapa_sapa_gen("Ujang")
sapa_sapa_gen("Asep")
# kalo manual begini misalnya report
print("Halo Ujang Selamat Gawe Di HSI")
print("Halo Asep Selamat Gawe Di HSI")
rumus_luas_segi_tiga(10, 58)
rumus_luas_segi_tiga(70, 500)