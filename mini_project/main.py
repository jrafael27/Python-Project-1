import json
import requests
from pathlib import Path
from dataclasses import asdict

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data.json"
OUTPUT_FILE = BASE_DIR / "ringkasan.json"

from produk import Produk

def load_products():
    with open("mini_project/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Produk(**item) for item in data]


def main():
    try:
        products = load_products()

        # Hitung omzet setiap produk
        detail = []

        for p in products:
            detail.append({
                **asdict(p),
                "omzet": p.omzet()
            })

        # Total omzet
        total_omzet = sum(p.omzet() for p in products)

        # Produk terlaris berdasarkan jumlah terjual
        terlaris = max(products, key=lambda p: p.terjual)

        # Ambil kurs USD
        try:
            res = requests.get(
                "https://open.er-api.com/v6/latest/USD",
                timeout=10
            )
            res.raise_for_status()

            kurs = res.json()["rates"]["IDR"]
            total_usd = total_omzet / kurs

        except (requests.exceptions.RequestException, KeyError, TypeError):
            kurs = None
            total_usd = None
            print("Kurs USD tidak tersedia.")

        # Buat ringkasan
        ringkasan = {
            "total_produk": len(products),
            "total_omzet": total_omzet,
            "produk_terlaris": {
                "nama": terlaris.nama,
                "terjual": terlaris.terjual,
                "omzet": terlaris.omzet()
            },
            "detail_produk": detail,
            "kurs_idr_per_usd": kurs,
            "total_omzet_usd": round(total_usd, 2) if total_usd is not None else None
        }

        # Simpan JSON
        with open("mini_project/ringkasan.json", "w", encoding="utf-8") as f:
            json.dump(ringkasan, f, indent=4, ensure_ascii=False)

        print("Total produk:", len(products))
        print("Total omzet: Rp", total_omzet)
        print("Produk terlaris:", terlaris.nama)

        if total_usd is not None:
            print("Total USD: $", round(total_usd, 2))

        print("Ringkasan berhasil disimpan!")

    except FileNotFoundError:
        print("File data.json tidak ditemukan.")

    except json.JSONDecodeError:
        print("Format JSON tidak valid.")

    except (KeyError, TypeError, ValueError) as e:
        print("Format data salah:", e)


if __name__ == "__main__":
    main()