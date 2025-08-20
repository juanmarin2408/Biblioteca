import pymysql

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            port=3307,
            user="appuser",        # 👈 nuevo usuario
            password="admin",
            database="libros_bd",
            charset="utf8mb4",
        )
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return None