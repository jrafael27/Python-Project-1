# Function And Error Handling

def hitung_hpp(bahan, tenaga_kerja, overhead):
    # Hitung HPP sederhana
    return bahan + tenaga_kerja + overhead

# print(f"HPP: {hitung_hpp(100000, 50000, 20000)}")

# Parameter bernama dan defualt

def diskon(harga, persen=10):
    return harga * (1- persen / 100)

# print(diskon(20000))
# print(diskon(20000, persen=25))

# Error Handling    
def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Tidak bisa dibagi dengan nol"
    
# print(bagi(10, 5))

def angka_kuadrat():
    try:
        print("==== Program Hitung Angka Kuadrat ====")
        nilai = float(input("Masukkan angka Positif :"))
        
        if(nilai < 0):
            raise ValueError("Angka Harus Positif!")
        
        hasil = nilai ** 2
        print(f"Hasil Kuadrat dari {nilai} adalah {hasil}")
        
    except ValueError as e:
        print(f"Terjadi Error Input: {e}")
        
    finally:
        print("Program Selesai")
        
# angka_kuadrat()

def hpp_per_unit():
    try:
        print("==== Program Hitung HPP Per Unit ====")
        nilai = float(input("Masukkan Total Biaya :"))
        jumlah = int(input("Masukkan Jumlah Unit :"))
        
        if(jumlah <= 0):
            raise ValueError("Jumlah Unit Harus Lebih dari Nol!")
        
        return print(f"HPP Per Unit : {nilai / jumlah}")
        
    except ValueError as e:
        print(f"Terjadi Error Input: {e}")
        
    finally:
        print("Program Selesai")
        
# hpp_per_unit()
        
        
# Type Hints
nama : str = "Joshua"
usia : int = 28
height : float = 175.5
is_aktif : bool = True

def sapa_user(nama: str, tahun_lahir: int) -> str:
    if(nama != str):
        raise TypeError("Nama harus berupa string")
    elif(tahun_lahir != int):
        raise TypeError("Tahun lahir harus berupa integer")
    
    umur = 2026 - tahun_lahir
    return print(f"halo {nama}, umurmu adalah {umur} tahun")

sapa_user("Florencia","1999")
sapa_user("Joshua",1999)