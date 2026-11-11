import mysql.connector
from mysql.connector import Error

_last_error = None


def get_connection():
    global _last_error
    try:
        _last_error = None
        connection = mysql.connector.connect(
            host='localhost',
            database='db_perpustakaan',
            user='root',
            password=''
        )
        if connection.is_connected():
            return connection
        _last_error = "Koneksi tidak aktif"
        return None
    except Error as e:
        _last_error = str(e)
        print(f"ERROR koneksi database: {e}")
        return None


def get_last_error():
    return _last_error