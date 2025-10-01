# 📚 Biblioteca Virtual Personal (Tkinter + SQLite)

Aplicación de escritorio en **Python** para gestionar una biblioteca personal: registrar libros, editarlos, eliminarlos, buscarlos y filtrarlos; además, muestra estadísticas de lectura en tiempo real. La interfaz está construida con **Tkinter** (usando el tema **ttkthemes**), y la persistencia se maneja con **SQLite** (archivo local `libros.db`).

> Este README está basado únicamente en el código del proyecto: `app_libros.py`, `conexion_gui.py`, `Ilibros.py`, `Libros.py`, `Libros_dao_gui.py`, `gui_libros.py`.

---

## 🚀 Características principales

- **CRUD de libros**: agregar, modificar y eliminar registros.
- **Búsqueda en tiempo real** por referencia, nombre, autor, año o género.
- **Filtros** por **estado** (todos / leídos / pendientes) y **género** literario.
- **Validaciones**:
  - Referencia con formato **AAA111** (3 letras + 3 números).
  - **Año** numérico y **≤ año actual**.
  - **Campos obligatorios**: referencia, nombre, autor, año, género y estado.
  - **Coherencia de fechas**: *fecha de inicio ≤ fecha final*.
- **Estadísticas** básicas en tiempo real (total, leídos, pendientes, % de progreso) y **estadísticas detalladas**.
- **SQLite** local sin servidor externo (`libros.db` se crea automáticamente).

---

## 🧰 Requisitos

- **Python 3.8+**
- **Tkinter** (incluido con Python en Windows/macOS; en Linux puede requerir instalar `python3-tk`/`tk` del sistema).
- Paquetes de Python:
  - `ttkthemes`
  - `tkcalendar`

> Módulos estándar usados: `sqlite3`, `abc`, `typing`, `datetime`, `re`, `os` (no requieren instalación).

### (Opcional) `requirements.txt` sugerido

