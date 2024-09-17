# Program dialog antara dua karakter: Bagas dan Jono

# Menyapa pengguna
print("Selamat datang di program dialog antara bagas dan jono!")
print("Bagas: Halo jon, Hari ini kita akan belajar menggambar.")
print("Jono: Hai bagas Aku paling semangat kalo soal menggambar!")
print("Bagas: yaudah lansung aku mulai yaa")
print("Jono: okee")

# Mengambil input dari pengguna untuk angka
try:
    angka1 = float(input("bagas: Berikan aku angka pertama: "))
    angka2 = float(input("bagas: Berikan aku angka kedua: "))
except ValueError:
    print("tolong masukkan angka yang valid.")
    exit()


# Melakukan operasi aritmatika
jumlah = angka1 + angka2
selisih = angka1 - angka2
produk = angka1 * angka2

if angka2 != 0:
    pembagian = angka1 / angka2
else:
    pembagian = None

# Menampilkan hasil operasi aritmatika
print("\nbagas: Aku sudah melakukan beberapa perhitungan.")
print(f"bagas: Jumlah dari {angka1} dan {angka2} adalah {jumlah}.")
print(f"bagas: Selisih antara {angka1} dan {angka2} adalah {selisih}.")
print(f"bagas: Produk dari {angka1} dan {angka2} adalah {produk}.")

if pembagian is not None:
    print(f"bagas: Pembagian dari {angka1} oleh {angka2} adalah {pembagian}.")
else:
    print("bagas: Pembagian dengan nol tidak diperbolehkan.")

# Operasi logika
if angka1 > angka2:
    print(f"\nbagas: {angka1} lebih besar dari {angka2}.")
elif angka1 < angka2:
    print(f"bagas: {angka1} lebih kecil dari {angka2}.")
else:
    print(f"bagas: {angka1} sama dengan {angka2}.")

# Mengakhiri dialog
print("\njono: Terima kasih, eko! Ini sangat membantu.")
print("bagas: Sama-sama, turam! Sampai jumpa di pelajaran matemattika berikutnya!")
print("jono: okeee")