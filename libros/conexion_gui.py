import os
import pymysql

def get_connection():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "admin"),
            database=os.getenv("DB_NAME", "libros_bd")
        )
        return conn
    except Exception as e:
        print("❌ Error al conectar a la BD:", e)
        return None


