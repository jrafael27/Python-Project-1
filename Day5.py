from produk import Produk
from produk_2 import Produk as Produk2

items = [Produk2("Roti", 10000, 5), Produk2("Susu", 15000, 3), Produk2("Telur", 20000, 2)]

for p in items:
    print(p)
    print(f"Omzet: {p.omzet()}")
    