nama = input("Masukkan Nama Lengkap Mu :")
umur = input("Berapa Umur Mu Sekarang :")
kelas = input("Berapa Kelas Mu Sekarang :")
citacita = input("Apa Cita-Cita Mu Di Masa Depan :")
hobi = input("Apa Hobi Mu :")
belajar = input("Lebih Suka Mana Nih, Belajar Pagi Apa Malam :")
(print("1. Wibu"))
(print("2. Gamer"))
(print("3. Bola"))
(print("4. Anak Konten"))
(print("5. Anak Nongki"))
TipeDigitalKamu = int(input("masukkan tipe gaya digital kamu :"))
if (TipeDigitalKamu == 1):
    wibu = input("Siapa waifu atau husbando Lu :")
    komentar1 = print("Wih, Pasti Lu Wibu Banget Kan")
elif (TipeDigitalKamu == 2):
    gamer = input("Game favorit Lu apa :")
    komentar2 = print("Wih, Lu Pasti Jago Main Gamenya")
elif (TipeDigitalKamu == 3):
    bola = input("Siapa Idola Pemain Bola Lu :")
    komentar3 = print("Wih, Lu Pasti Jago Main Bola")
elif (TipeDigitalKamu == 4):
    anakkonten = input("Siapa Youtuber Idola Lu :")
    komentar4 = print("Wih, Lu Pasti Suka Ngonten")
elif (TipeDigitalKamu == 5):
    anaknongki = input("Kenapa Suka Nongkrong :")
    komentar5 = print("Astaghfirullah, Lu Pasti Suka Maksiat")

bau = input("Apakah Temen Di Sebelah Lu Bau Ya/Tidak :")
if (bau == "ya"):
    komentarya = print("Buset Bau Amat Teman Lu Dah, Kasih Parfum Darurat Napa")
elif (bau == "tidak"):
     komentartidak = print("Hoki Banget Dong Teman Lu Kaga Bau")


print("=== PROFILE DIGITAL KAMU ===")
print("nama :", nama)
print("umur :", umur)
print("kelas :", kelas)
print("citacita :", citacita)
print("hobi :", hobi)
print("belajar :", belajar)
(" ")

print("=== TIPE DIGITAL ===")
if (TipeDigitalKamu == 1):
    print("Tipe : Wibu")
    print("Waifu/Husbando favorit :", wibu)
    print("Komentar :", komentar1)

if (TipeDigitalKamu == 2):
    print("Tipe : Gamer")
    print("Game favorit :", gamer)
    print("Komentar :", komentar2)

if (TipeDigitalKamu == 3):
    print("Tipe : Bola")
    print("Pemain favorit :", bola)
    print("Komentar :", komentar3)

elif (TipeDigitalKamu == 4):
    print("Tipe : Anak Konten")
    print("Conten creator favorit :", anakkonten)
    print("Komentar :", komentar4)

elif (TipeDigitalKamu == 5):
    print("Tipe : Anak Nongki")
    print("Tempat favorit :", anaknongki)
    print("Komentar :", komentar5)
print(" ")

print("= FUN CHEK =")
if (bau == "Ya"):
    print("Temen sebelah bau :", bau)
    print(komentarya)

elif (bau == "Tidak"):
    print("Temen sebelah bau :", bau)kemas pake zip
    print(komentartidak)