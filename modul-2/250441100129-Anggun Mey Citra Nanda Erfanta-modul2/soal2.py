total_belanja = float(input("Masukkan total belanja: "))

if total_belanja >= 100000:
    diskon = (10/100) * total_belanja
elif total_belanja >= 50000:
    diskon = 0.05 * total_belanja
else:
    diskon = 0

print("Jumlah diskon yang didapat:", diskon)