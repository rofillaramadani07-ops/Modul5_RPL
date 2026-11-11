import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = None
        self.role_login = None

    def _buat_login(self):
        self.role_login = None
        self.view = LoginView()
        # Menghubungkan tombol masuk di view ke fungsi proses_login
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get().strip()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan", "Username dan Password wajib diisi!"
            )
            return

        try:
            user = self.model.autentikasi(username, password)
        except ConnectionError as e:
            messagebox.showerror("Koneksi Gagal", str(e))
            return
        except Exception as e:
            messagebox.showerror(
                "Kesalahan Database", f"{type(e).__name__}: {e}"
            )
            return

        if not user:
            messagebox.showerror(
                "Login Gagal", "Username atau Password salah!"
            )
            return

        user_name = user.get("username", "User")
        user_role = user.get("role", "petugas")

        messagebox.showinfo(
            "Login Berhasil", f"Selamat datang, {user_name} ({user_role})!"
        )
        self.role_login = user_role
        self.view.destroy()

    def run(self):
        while True:
            self._buat_login()
            self.view.mainloop()

            # Login ditutup lewat tombol X tanpa login -> keluar aplikasi
            if self.role_login is None:
                break

            # Membuka halaman utama sesuai role
            app_utama = BukuController(role=self.role_login)
            app_utama.run()

            # Ditutup lewat tombol X (bukan Logout) -> keluar aplikasi
            if not app_utama.logout_diminta:
                break
            # Logout -> kembali ke atas, halaman login muncul lagi