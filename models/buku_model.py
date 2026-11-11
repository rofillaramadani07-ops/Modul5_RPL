import uuid
from config.database import get_connection


class BukuModel:
    def __init__(self):
        self.conn = get_connection()
        self.table_name = "buku"

    def _ensure_connection(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = get_connection()
        if self.conn is None:
            print("ERROR: koneksi database gagal")
            return False
        return True

    def ambil_semua_buku(self):
        if not self._ensure_connection():
            return []
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute(
                f"SELECT id_buku, kode_buku, judul, penulis, tahun_terbit "
                f"FROM {self.table_name} ORDER BY id_buku"
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error ambil buku: {e}")
            return []
        finally:
            cursor.close()

    def tambah_buku(self, judul, penulis, tahun):
        if not self._ensure_connection():
            return False
        cursor = self.conn.cursor()
        try:
            kode = f"BK-{uuid.uuid4().hex[:8].upper()}"
            query = (
                f"INSERT INTO {self.table_name} "
                "(kode_buku, judul, penulis, tahun_terbit) VALUES (%s, %s, %s, %s)"
            )
            cursor.execute(query, (kode, judul, penulis, int(tahun)))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Error tambah buku: {e}")
            return False
        finally:
            cursor.close()

    def update_buku(self, id_buku, judul, penulis, tahun):
        if not self._ensure_connection():
            return False
        cursor = self.conn.cursor()
        try:
            query = (
                f"UPDATE {self.table_name} "
                "SET judul = %s, penulis = %s, tahun_terbit = %s "
                "WHERE id_buku = %s"
            )
            cursor.execute(query, (judul, penulis, int(tahun), id_buku))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Error update buku: {e}")
            return False
        finally:
            cursor.close()

    def hapus_buku(self, id_buku):
        if not self._ensure_connection():
            return False
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                f"DELETE FROM {self.table_name} WHERE id_buku = %s", (id_buku,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Error hapus buku: {e}")
            return False
        finally:
            cursor.close()
    def create_buku(self, judul, penulis, tahun):
        return self.tambah_buku(judul, penulis, tahun)

    def get_all_buku(self):
        return self.ambil_semua_buku()
