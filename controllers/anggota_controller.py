import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()
        
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        berhasil = self.model.create_anggota(nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_alamat.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data anggota yang ingin dihapus!")
            return
            
        item_data = self.view.tabel.item(selected_item)
        id_anggota = item_data['values'][0]
        
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            if self.model.delete_anggota(id_anggota):
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.muat_data_tabel()

    def perbarui_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data anggota yang ingin diperbarui!")
            return
            
        item_data = self.view.tabel.item(selected_item)
        id_anggota = item_data['values'][0]
        
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        
        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.muat_data_tabel()

    def run(self):
        self.view.mainloop()