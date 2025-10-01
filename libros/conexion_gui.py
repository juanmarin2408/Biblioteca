import sqlite3
import os

# Archivo de base de datos (se guarda en la carpeta "libros")
DB_PATH = os.path.join(os.path.dirname(__file__), "libros.db")

def get_connection():
    """Conexión a la base de datos SQLite"""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return None

def init_db():
    """Crea la tabla si no existe"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    referencia TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    anio INTEGER NOT NULL,
                    genero TEXT,
                    estado TEXT CHECK(estado IN ('leído','pendiente')) NOT NULL DEFAULT 'pendiente',
                    fecha_inicio TEXT,
                    fecha_final TEXT
                )
            """)
            conn.commit()
        finally:
            conn.close()
