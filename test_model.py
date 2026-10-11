from models.buku_model import BukuModel

model = BukuModel()

# 1. Menambahkan buku baru
print("=== Menambahkan Buku ===")
model.create_buku("Pemrograman Python MVC")
print("Data berhasil disimpan!")

# 2. Menampilkan semua buku
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()