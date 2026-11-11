import os
import mysql.connector
from mysql.connector import Error

_last_error = None


def get_connection():
    global _last_error
    try:
        _last_error = None
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            database=os.getenv("DB_NAME", "db_perpustakaan"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
        )
        if connection.is_connected():
            return connection
        _last_error = "Koneksi tidak aktif"
        return None
    except Error as e:
        _last_error = str(e)
        return None


def get_last_error():
    return _last_error
