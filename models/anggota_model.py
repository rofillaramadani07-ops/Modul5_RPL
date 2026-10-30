import mysql.connector

class AnggotaModel:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_perpustakaan"
        )

    def create_anggota(self, nama, alamat):
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
            cursor.execute(query, (nama, alamat))
            self.db.commit()
            cursor.close()
            return True
        except Exception as e:
            print("ERROR DETAIL:", str(e))
            return False

    def get_all_anggota(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        result = cursor.fetchall()
        cursor.close()
        return result

    def update_anggota(self, id_anggota, nama, alamat):
        try:
            cursor = self.db.cursor()
            query = "UPDATE anggota SET nama = %s, alamat = %s WHERE id_anggota = %s"
            cursor.execute(query, (nama, alamat, id_anggota))
            self.db.commit()
            cursor.close()
            return True
        except Exception as e:
            print("ERROR DETAIL:", str(e))
            return False

    def delete_anggota(self, id_anggota):
        try:
            cursor = self.db.cursor()
            query = "DELETE FROM anggota WHERE id_anggota = %s"
            cursor.execute(query, (id_anggota,))
            self.db.commit()
            cursor.close()
            return True
        except Exception as e:
            print("ERROR DETAIL:", str(e))
            return False