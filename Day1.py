nama = "joshua,rafael"
umur = 28
tinggi = 170.5
aktif = True

# print(f"Nama: {nama}! Umur kamu {umur}.")
# print(type(nama), type(umur), type(tinggi), type(aktif))

# # inputan user
# kota = input("Kota asal kamu? ")
# print(f"Oh, dari {kota}")

print(f"Nama Customer : {nama.upper()}")
print("Pesanan : ")
print("- Nasi Goreng")
harga = input("Harga Nasi Goreng : ")
jumlah = input("Jumlah Pesanan : ")
total = int(harga) * int(jumlah)
print(f"Total Harga : {total}")

# strip hanya hapus yang sesuai di syntax, bukan di tengah kata
print(f"nama singkatan Joshua adalah {nama.strip('ua')}")

print(f"nama singkatan Joshua adalah {nama.split(',')[0].replace('ua', '')}")

# latihan .upper(), .lower(), .strip(), .split(","), .replace()

while True:
    email_input = input("Masukkan email kamu: ")
    email_clean = email_input.strip().lower()
    
    if "@" not in email_clean or " " in email_clean:
        print("Email tidak valid, silahkan masukkan email yang benar.")
        continue
    else:
        print(f"Email sudah dimasukan ke database {email_clean}")
        break

nama = "Joshua, Florencia, Rafael, Irena"

clean_nama = nama.strip().lower().replace(" ","")
print(clean_nama)
list_nama = clean_nama.split(",")

print(f"List Nama : {list_nama[0]}")