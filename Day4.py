import json
import csv

with open('data.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    
for p in data["produk"]:
    omzet = p["harga"] * p["terjual"]
    print(f"{p['nama']} : {omzet:,}")
    
# Tulis Hasil
hasil = {p["nama"]: p["harga"] * p["terjual"] for p in data["produk"]}
# with open("hasil.json", "w", encoding="utf-8") as f:
#     json.dump(hasil, f, indent=2, ensure_ascii = False)
    
    
teks = '{"produk": [{"nama": "Nasi Goreng", "harga": 15000, "terjual": 2}, {"nama": "Mie Goreng", "harga": 12000, "terjual": 1}, {"nama": "Ayam Goreng", "harga": 20000, "terjual": 3}]}'
teks = json.loads(teks)
# print(teks["produk"][0]["nama"])
data = json.dumps(teks, indent=2, ensure_ascii=False)
# print(data)

with open("latihan_transaksi.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

    for p in data:
        harga = int(p["harga_satuan"])
        jumlah = int(p["jumlah"])
        produk = p["produk"]

        if(p["status"] == "diproses"):
            print("Barang:", produk)
            print("Harga:", harga)
            print("Terjual:", jumlah)
            print(f"Total {produk} terjual: {harga * jumlah:,}")
            
    data_hasil = {p["produk"]: harga * jumlah for p in data }
    
with open("hasil_transaksi.json", "w", encoding="utf-8") as f:   
    json.dump(data_hasil, f, indent=2, ensure_ascii=False) 

print(hasil)