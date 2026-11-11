import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self, role="anggota"):
        super().__init__()
        self.role = role.lower()

        # 1. Atur Window Title sesuai role
        if self.role in ["admin", "petugas"]:
            self.title("Sistem Manajemen Perpustakaan - Mode: ADMIN")
        else:
            self.title("Sistem Manajemen Perpustakaan - Mode: ANGGOTA")

        self.geometry("900x550")
        ctk.set_appearance_mode("light")

        # Grid Configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ================= LEFT FRAME (FORM DATA BUKU) =================
        self.frame_left = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.lbl_title_form = ctk.CTkLabel(
            self.frame_left, text="Form Data Buku", font=("Arial", 16, "bold")
        )
        self.lbl_title_form.pack(pady=(20, 15))

        # Entry Inputs
        self.entry_judul = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Judul Buku", width=220)
        self.entry_judul.pack(pady=8)

        self.entry_penulis = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Penulis", width=220)
        self.entry_penulis.pack(pady=8)

        self.entry_tahun = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Tahun Terbit", width=220)
        self.entry_tahun.pack(pady=8)

        # Tombol Aksi (Simpan, Update, Hapus)
        self.btn_simpan = ctk.CTkButton(self.frame_left, width=220)
        self.btn_simpan.pack(pady=(15, 8))

        self.btn_update = ctk.CTkButton(self.frame_left, width=220)
        self.btn_update.pack(pady=8)

        self.btn_hapus = ctk.CTkButton(self.frame_left, width=220)
        self.btn_hapus.pack(pady=8)

        self.btn_logout = ctk.CTkButton(
            self.frame_left, text="Logout", width=220, fg_color="#4A5568", hover_color="#2D3748"
        )
        self.btn_logout.pack(pady=(20, 10))

        # ================= RIGHT FRAME (DAFTAR BUKU) =================
        self.frame_right = ctk.CTkFrame(self, corner_radius=0, fg_color="white")
        self.frame_right.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(2, weight=1)

        self.lbl_header = ctk.CTkLabel(
            self.frame_right, text="Daftar Koleksi Buku", font=("Arial", 18, "bold"), text_color="#1A202C"
        )
        self.lbl_header.grid(row=0, column=0, pady=(15, 2))

        # Identitas Fila
        self.lbl_nama = ctk.CTkLabel(
            self.frame_right, text="ROFILLA_RAMADANI_REYNOLD_F5212530113", font=("Arial", 11, "bold"), text_color="#4A5568"
        )
        self.lbl_nama.grid(row=1, column=0, pady=(0, 15))

        # Tabel Data (Treeview)
        columns = ("id_buku", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_right, columns=columns, show="headings")
        
        self.tabel.heading("id_buku", text="ID Buku")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun Terbit")

        self.tabel.column("id_buku", width=70, anchor="center")
        self.tabel.column("judul", width=200, anchor="w")
        self.tabel.column("penulis", width=150, anchor="w")
        self.tabel.column("tahun", width=90, anchor="center")

        self.tabel.grid(row=2, column=0, sticky="nsew", padx=15, pady=(0, 15))

        # Terapkan Kondisi Role (Anggota vs Admin)
        self.apply_role_permissions()

    def apply_role_permissions(self):
        if self.role in ["admin", "petugas"]:
            # Mode Admin: Tombol Aktif & Warna Cerah
            self.btn_simpan.configure(
                text="Simpan Data", state="normal", fg_color="#27AE60", hover_color="#219150"
            )
            self.btn_update.configure(
                text="Perbarui Data (Update)", state="normal", fg_color="#2F80ED", hover_color="#1B60C1"
            )
            self.btn_hapus.configure(
                text="Hapus Data (Delete)", state="normal", fg_color="#EB5757", hover_color="#C0392B"
            )
        else:
            # Mode Anggota: Tombol Terkunci / Disabled
            self.btn_simpan.configure(
                text="Simpan (Admin Only)", state="disabled", fg_color="#52986E"
            )
            self.btn_update.configure(
                text="Update (Admin Only)", state="disabled", fg_color="#6189C3"
            )
            self.btn_hapus.configure(
                text="Hapus (Admin Only)", state="disabled", fg_color="#D56161"
            )