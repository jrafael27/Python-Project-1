# List
bahan = ["gula", "tepung", "telur", "susu", "mentega"]

bahan.append("vanili")

# print(bahan[0], bahan[5], len(bahan))

# Dictionary
produk = {
    "nama": "Nasi Goreng",
    "harga": 15000,
    "jumlah": 2,
    "total": 30000
}

# print(f"Nama Produk : {produk['nama']}")
produk["harga"] = 20000
# print(produk)

# Looping
# print("List Bahan :")
for x in bahan:
    # print(f" - {x}")
    continue
    
for kunci, nilai in produk.items():
    # print(f"{kunci} : {nilai}")
    continue
    
# List of Dictionary
daftar = [
    {"nama": "Nasi Goreng", "harga": 15000, "jumlah": 2, "total": 30000},
    {"nama": "Mie Goreng", "harga": 12000, "jumlah": 1, "total": 12000},
    {"nama": "Ayam Goreng", "harga": 20000, "jumlah": 3, "total": 60000}
]

# murah = [p["nama"] for p in daftar if p["total"] < 20000]
# print(murah)

# total_semua = sum(p["total"] for p in daftar)
# print(f"Total Semua : {total_semua}")

termahal = max(daftar, key=lambda p: p["harga"])
# print(f"Termahal : {termahal['nama']}, dengan harga {termahal['harga']}")

total_terbesar = max(daftar, key=lambda p: p["total"])
# print(f"Total Terbesar : {total_terbesar['nama']}, dengan total {total_terbesar['total']}")

urutan_termurah = sorted(daftar, key=lambda p: p["harga"], reverse=False)
print("Urutan Termurah :")
for p in urutan_termurah:
    print(f"{p['nama']} : {p['harga']}")