angka = int(input("Masukkan sebuah angka: "))
if angka % 2 == 0:
    jenis = "Genap"
else:
    jenis = "Ganjil"

if angka >= 0:
    if angka > 0:
        sifat = "Positif"
    else:
        sifat = "Nol"
else:
    sifat = "Negatif"

print("Angka tersebut adalah bilangan", jenis, "dan", sifat)