# Sistem Manajemen Perpustakaan

Aplikasi desktop berbasis Python untuk mengelola data perpustakaan: data buku, data anggota, serta login dengan pembagian hak akses (role) **Admin** dan pengguna biasa. Data disimpan di database MySQL dan aplikasi disusun dengan pola arsitektur **MVC (Model-View-Controller)**.

## Fitur

- Login dan otorisasi berdasarkan role pengguna
- CRUD data buku (tambah, tampilkan, perbarui, hapus)
- CRUD data anggota
- Pengujian otomatis dengan pytest dan GitHub Actions (CI)
- Pengecekan kualitas kode dengan flake8

## Struktur Direktori (MVC)

Alur kerja singkat: **View** menerima input pengguna, lalu meneruskannya ke **Controller**. Controller memanggil **Model** untuk membaca atau menulis data ke MySQL, kemudian hasilnya dikembalikan ke View untuk ditampilkan.

## Instalasi & Konfigurasi Database MySQL

### 1. Prasyarat

- Python 3.10 atau lebih baru
- MySQL Server (XAMPP, Laragon, atau MySQL Installer)
- Git

### 2. Clone repositori

```bash
git clone https://github.com/rofillaramadani07-ops/Modul5_RPL.git
cd Modul5_RPL
```

### 3. Virtual environment dan dependensi

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Siapkan database MySQL

Nyalakan MySQL, lalu jalankan:

```sql
CREATE DATABASE IF NOT EXISTS db_perpustakaan;
```

Buat tabel dengan menjalankan:

```bash
python buat_tabel.py
python buat_tabel_anggota.py
```

### 5. Konfigurasi koneksi

`config/database.py` membaca environment variable, dan memakai nilai bawaan jika tidak diatur:

| Variable | Nilai bawaan |
|---|---|
| `DB_HOST` | `localhost` |
| `DB_PORT` | `3306` |
| `DB_NAME` | `db_perpustakaan` |
| `DB_USER` | `root` |
| `DB_PASSWORD` | (kosong) |

Jika MySQL Anda memakai password, atur `DB_PASSWORD` atau ubah nilai bawaan di file tersebut.

## Cara Menjalankan Aplikasi

1. Pastikan MySQL sudah menyala.
2. Aktifkan virtual environment (`.venv\Scripts\activate`).
3. Jalankan:

```bash
python main.py
```

4. Login menggunakan akun yang ada di tabel pengguna.

Tanpa Python: unduh `AplikasiPerpustakaan.exe` dari halaman **Releases** repositori ini dan jalankan (MySQL tetap harus menyala).

## Pengujian dan Linter

```bash
pytest
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Membuat File .exe

```bash
pyinstaller --onefile --windowed --name AplikasiPerpustakaan main.py
```

Hasilnya di `dist/AplikasiPerpustakaan.exe`.
