class Produk:
    def __init__(self, nama: str, harga: int, terjual: int=0):
        self.nama = nama
        self.harga = harga
        self.terjual = terjual
        
    def omzet(self) -> int:
        return self.harga * self.terjual
    
    def __repr__(self) -> str:
        return f"Produk({self.nama}, {self.harga})"
    