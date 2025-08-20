from conexion_gui import get_connection
import sys
import os
sys.path.append('/home/ubuntu/upload')
from Libros import Libros
from Ilibros import ILibros

class LibrosDao(ILibros):

    def libros(self):
        lista_libros = []
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = """SELECT referencia, nombre, autor, anio, genero, estado, fecha_inicio, fecha_final
                             FROM libros ORDER BY referencia"""
                    cursor.execute(sql)
                    for ref, nombre, autor, año, genero, estado, f_ini, f_fin in cursor.fetchall():
                        lista_libros.append(Libros(año, ref, autor, nombre, genero, estado, f_ini, f_fin))
            except Exception as e:
                pass  # Manejo silencioso de errores para GUI
            finally:
                conn.close()
        return lista_libros

    def agregar_libro(self, l):
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = """INSERT INTO libros
                            (referencia, nombre, autor, anio, genero, estado, fecha_inicio, fecha_final)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (
                        l.referencia,
                        l.nombre,
                        l.autor,
                        l.anio,
                        l.genero,
                        l.estado,
                        l.fecha_inicio,
                        l.fecha_fin
                    ))
                    conn.commit()
                    print(f"✅ Libro agregado con referencia {l.referencia}")
                    return True
            except Exception as e:
                print(f"❌ Error en agregar_libro: {e}")
                return False
            finally:
                conn.close()
        else:
            print("❌ No se pudo establecer conexión con la base de datos.")
        return False


    def modificar_libro(self, l):
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = """UPDATE libros
                            SET nombre=%s, autor=%s, anio=%s, genero=%s,
                                estado=%s, fecha_inicio=%s, fecha_final=%s
                            WHERE referencia=%s"""
                    cursor.execute(sql, (
                        l.nombre,
                        l.autor,
                        l.anio,
                        l.genero,
                        l.estado,
                        l.fecha_inicio,
                        l.fecha_fin,
                        l.referencia
                    ))
                    conn.commit()
                    print(f"✅ Libro con referencia {l.referencia} actualizado")
                    return True
            except Exception as e:
                print(f"❌ Error en modificar_libro: {e}")
                return False
            finally:
                conn.close()
        else:
            print("❌ No se pudo conectar a la base de datos.")
        return False



    def eliminar_libro(self, l: Libros) -> bool:
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM libros WHERE referencia=%s"
                    cursor.execute(sql, (l.referencia,))
                conn.commit()
                return True
            except Exception as e:
                pass  # Manejo silencioso de errores para GUI
            finally:
                conn.close()
        return False

    def busca_libro(self, l: Libros) -> bool:
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = """SELECT nombre, autor, anio, genero, estado, fecha_inicio, fecha_final
                             FROM libros WHERE referencia=%s"""
                    cursor.execute(sql, (l.referencia,))
                    row = cursor.fetchone()
                    if row:
                        l.nombre, l.autor, l.año, l.genero, l.estado, l.fecha_inicio, l.fecha_fin = row
                        return True
            except Exception as e:
                pass  # Manejo silencioso de errores para GUI
            finally:
                conn.close()
        return False

    # Nuevas funcionalidades
    def contar_por_estado(self):
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT LOWER(estado), COUNT(*) FROM libros GROUP BY LOWER(estado)")
                    return dict(cursor.fetchall())
            except Exception as e:
                pass  # Manejo silencioso de errores para GUI
            finally:
                conn.close()
        return {}

    def libros_por_genero(self, genero):
        lista = []
        conn = get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = """SELECT referencia, nombre, autor, anio, genero, estado, fecha_inicio, fecha_final
                             FROM libros WHERE genero=%s"""
                    cursor.execute(sql, (genero,))
                    for ref, nombre, autor, año, genero, estado, f_ini, f_fin in cursor.fetchall():
                        lista.append(Libros(año, ref, autor, nombre, genero, estado, f_ini, f_fin))
            except Exception as e:
                pass  # Manejo silencioso de errores para GUI
            finally:
                conn.close()
        return lista