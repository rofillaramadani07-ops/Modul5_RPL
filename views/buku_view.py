
import customtkinter as ctk
from tkinter import ttk, messagebox


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Konfigurasi jendela
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("800x450")
        self.minsize(750, 400)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.nomor_buku = 1

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # =====================================
        # FRAME KIRI: FORM DATA BUKU
        # =====================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0,
            padx=(10, 5), pady=10,
            sticky="nsew"
        )

        self.frame_kiri.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 20))

        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku",
            height=35
        )
        self.entry_judul.pack(
            fill="x", padx=15, pady=7
        )

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis",
            height=35
        )
        self.entry_penulis.pack(
            fill="x", padx=15, pady=7
        )

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit (Misal: 2024)",
            height=35
        )
        self.entry_tahun.pack(
            fill="x", padx=15, pady=7
        )

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            command=self.simpan_data,
            fg_color="green",
            hover_color="darkgreen",
            height=35
        )
        self.btn_simpan.pack(
            fill="x", padx=15, pady=(15, 10)
        )

        # =====================================
        # FRAME KANAN: TABEL KOLEKSI BUKU
        # =====================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1,
            padx=(5, 10), pady=10,
            sticky="nsew"
        )

        self.frame_kanan.grid_rowconfigure(1, weight=1)
        self.frame_kanan.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, pady=15)

        # Gaya tabel
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=28,
            fieldbackground="white",
            font=("Arial", 10)
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold"),
            background="#eeeeee"
        )

        # Tabel
        self.tabel_buku = ttk.Treeview(
            self.frame_kanan,
            columns=("id", "judul", "penulis", "tahun"),
            show="headings"
        )

        self.tabel_buku.heading("id", text="ID")
        self.tabel_buku.heading("judul", text="Judul Buku")
        self.tabel_buku.heading("penulis", text="Penulis")
        self.tabel_buku.heading("tahun", text="Tahun")

        self.tabel_buku.column("id", width=45, anchor="center")
        self.tabel_buku.column("judul", width=160)
        self.tabel_buku.column("penulis", width=120)
        self.tabel_buku.column("tahun", width=65, anchor="center")

        self.tabel_buku.grid(
            row=1, column=0,
            padx=10, pady=(0, 10),
            sticky="nsew"
        )

        # Scrollbar tabel
        scrollbar = ttk.Scrollbar(
            self.frame_kanan,
            orient="vertical",
            command=self.tabel_buku.yview
        )
        scrollbar.grid(row=1, column=1, pady=(0, 10), sticky="ns")
        self.tabel_buku.configure(yscrollcommand=scrollbar.set)

    def simpan_data(self):
        judul = self.entry_judul.get().strip()
        penulis = self.entry_penulis.get().strip()
        tahun = self.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Data Belum Lengkap",
                "Mohon isi judul, penulis, dan tahun terbit."
            )
            return

        if not tahun.isdigit() or len(tahun) != 4:
            messagebox.showwarning(
                "Tahun Tidak Valid",
                "Masukkan tahun terbit dalam format 4 angka."
            )
            return

        self.tabel_buku.insert(
            "",
            "end",
            values=(self.nomor_buku, judul, penulis, tahun)
        )

        self.nomor_buku += 1

        self.entry_judul.delete(0, "end")
        self.entry_penulis.delete(0, "end")
        self.entry_tahun.delete(0, "end")

        messagebox.showinfo(
            "Berhasil",
            "Data buku berhasil ditambahkan ke tabel."
        )


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
