from dataclasses import dataclass

@dataclass
class Produk:
    nama: str
    harga: int
    terjual: int = 0

    def omzet(self) -> int:
        return self.harga * self.terjual