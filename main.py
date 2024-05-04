import Fisika
import time

def batas() :
    print("-"*15)

waktu_awal = time.time()

print(f"Massa jenis = {Fisika.massajenis.MassaJenis(10, 2)}")
print(f"Massa = {Fisika.massajenis.massa(10, 2)}")
print(f"Volume = {Fisika.massajenis.volume(10, 2)}")

waktu_akhir = time.time()
print(f"Waktu yang dibutuhkan : {waktu_akhir - waktu_awal} s")

batas()
print(f"Usaha = {Fisika.U(12, 3)}")
print(f"Gaya = {Fisika.G(12, 3)}")
print(f"Jarak = {Fisika.s(12, 3)}")

print(f"Ep = {Fisika.Ep(1, 2, 3)}")
print(f"Ek = {Fisika.Ek(4, 5)}")

diskon10 = Fisika.JL(10)
diskon20 = Fisika.JL(20)
print(f"Diskon 10% = {diskon10(10000)}")
print(f"Diskon 20% = {diskon20(10000)}")