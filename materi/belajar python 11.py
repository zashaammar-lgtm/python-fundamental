#list --> [] --> berurutan,berubah duplikat
#append()untuk menambah item diakhir list
#remove()untuk menghapus item bedasarkan velue / namanya
#insert()untukmitem ke spesifik index
daftarBelanja = [
    "es teh desa",#index 0
    "olive",#index 1
    "gorengan",#index
    ]
print("daftar belanja:",daftarBelanja)
daftarBelanja.append("esteh desa")
print("daftar belanja:",daftarBelanja)
daftarBelanja.remove("gorengan")
print("daftar belanja:",daftarBelanja)
daftarBelanja.insert(0,"pisang kembung")
print("daftar belanja:",daftarBelanja)
# memanggil salah satu index yang terdapat di list
print(daftarBelanja[2])
# no index:no_urut_item
print ("potong list: ", daftarBelanja[1:3])
# menggabung list +
jajananbilal = ("basreng", "makaroni")
jajanandzaky = ("pisang kembung", "pentol")
gabunganJajanan = jajanandzaky + jajananbilal
print("gabunganjajanan: ", gabunganJajanan)
# tuple -> () -> berurutan, berubah, tidak duplikat
ttl = ("Bekasi", 9, "desember", 2009)
print("TTL Dzaky:", ttl)
print("tgl lahir:", ttl[1])
# unpacking tuple ke variable baru
# harus berurutan sesuai value nya
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("tempat lahir:", tempat_lahir)
print("tahun lahir:", thn_lahir)
# list multi dimensi
daftarMinuman = [
["kopi", "teh", "susu jahe", "ronde"]]