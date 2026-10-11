import mysql.connector

class Database:
    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_buku" # Sesuaikan nama database Anda
        )