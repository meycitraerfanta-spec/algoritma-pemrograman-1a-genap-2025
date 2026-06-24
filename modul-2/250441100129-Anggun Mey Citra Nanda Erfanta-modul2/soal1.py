nilai = float(input("Masukkan nilai: "))

if nilai >= 85 and nilai <= 100:
    huruf = "A"
elif nilai >= 75:
    huruf = "B"
elif nilai >= 65:
    huruf = "C"
elif nilai >= 50:
    huruf = "D"
else:
    huruf = "E"

print("Nilai huruf yang diperoleh:", huruf)