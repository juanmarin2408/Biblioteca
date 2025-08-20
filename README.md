# 📚 Sistema de Gestión de Libros (Tkinter + MySQL en Docker)

Este proyecto es una aplicación de escritorio en **Python con Tkinter** para gestionar tu biblioteca personal.  
Usa una base de datos **MySQL**, pero **no necesitas instalar MySQL**: se ejecuta automáticamente en **Docker**.

---

## 🚀 Requisitos previos

Antes de empezar, asegúrate de tener instalado en tu computadora:

1. **Python 3.11 o superior**  
   👉 Descárgalo desde: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Docker Desktop**  
   👉 Descárgalo desde: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)  
   > Una vez instalado, **abre Docker Desktop** y déjalo ejecutándose en segundo plano.

3. **Git (opcional)** si quieres clonar este proyecto desde GitHub.  
   👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)

---

## 📂 Estructura del proyecto

proyecto/
│── libros/
│ ├── app_libros.py # Programa principal (interfaz Tkinter)
│ ├── conexion_gui.py # Conexión a la BD
│ ├── Libros.py # Clase Libros
│ ├── Libros_dao_gui.py # Acceso a datos
│ ├── Ilibros.py # Interfaz abstracta
│── bd/
│ └── init.sql # Script para crear la base de datos y tabla
│── requirements.txt # Dependencias de Python
│── docker-compose.yml # Configuración de Docker
│── README.md # Este archivo

# pip install -r requirements.txt

# docker-compose up -d

# docker ps

# python libros/app_libros.py
