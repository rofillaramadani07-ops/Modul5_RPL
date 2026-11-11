from models.buku_model import BukuModel
from views.buku_view import BukuView
import tkinter.messagebox as messagebox

class BukuController:
    def __init__(self, role="anggota"):
        self.role = role
        self.model = BukuModel()
        self.view = BukuView(role=self.role)
        
        self.selected_id = None

        # Hubungkan semua tombol aksi jika user adalah admin/petugas
        if self.role.lower() in ["petugas", "admin"]:
            self.view.btn_simpan.configure(command=self.tambah_buku)
            self.view.btn_update.configure(command=self.update_buku)
            self.view.btn_hapus.configure(command=self.hapus_buku)
            
            # Event klik pada tabel untuk memilih baris data
            self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)
        
        # Tombol Logout aktif untuk semua role
        if hasattr(self.view, 'btn_logout') and self.view.btn_logout:
            self.view.btn_logout.configure(command=self.logout)

        # Muat data ke tabel
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        try:
            daftar_buku = self.model.ambil_semua_buku()
            if not daftar_buku:
                return

            for buku in daftar_buku:
                id_buku = buku.get('id_buku', buku.get('id', ''))
                judul = buku.get('judul', buku.get('nama_buku', buku.get('title', '')))
                penulis = buku.get('penulis', buku.get('pengarang', ''))
                tahun = buku.get('tahun_terbit', buku.get('tahun', ''))

                self.view.tabel.insert("", "end", values=(id_buku, judul, penulis, tahun))
        except Exception as e:
            messagebox.showerror("Kesalahan", f"Gagal memuat data buku: {e}")

    def tambah_buku(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom input wajib diisi!")
            return
            
        try:
            sukses = self.model.tambah_buku(judul, penulis, tahun)
            if sukses:
                messagebox.showinfo("Sukses", "Data buku berhasil ditambahkan!")
                self.clear_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Gagal", "Gagal menambahkan data buku ke database.")
        except Exception as e:
            messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {e}")

    def pilih_data_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item)
            values = item_data['values']
            if values:
                self.selected_id = values[0]
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, values[1])
                
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, values[2])
                
                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, values[3])

    def update_buku(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin diperbarui!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom input wajib diisi!")
            return

        try:
            sukses = self.model.update_buku(self.selected_id, judul, penulis, tahun)
            if sukses:
                messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
                self.clear_form()
                self.muat_data_tabel()
                self.selected_id = None
            else:
                messagebox.showerror("Gagal", "Gagal memperbarui data buku.")
        except Exception as e:
            messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {e}")

    def hapus_buku(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin dihapus!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Fila yakin ingin menghapus data buku ini?")
        if konfirmasi:
            try:
                sukses = self.model.hapus_buku(self.selected_id)
                if sukses:
                    messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                    self.clear_form()
                    self.muat_data_tabel()
                    self.selected_id = None
                else:
                    messagebox.showerror("Gagal", "Gagal menghapus data buku.")
            except Exception as e:
                messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {e}")

    def clear_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def logout(self):
        self.view.destroy()

    def run(self):
        self.view.mainloop()