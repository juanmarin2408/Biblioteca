-- Crear la base de datos (si no existe, por seguridad)
CREATE DATABASE IF NOT EXISTS libros_bd;

-- Crear usuario para la aplicación y darle permisos
CREATE USER IF NOT EXISTS 'appuser'@'%' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON libros_bd.* TO 'appuser'@'%';
FLUSH PRIVILEGES;

-- Seleccionar la base de datos
USE libros_bd;

-- Crear la tabla libros
CREATE TABLE IF NOT EXISTS libros (
    referencia VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio INT NOT NULL,
    genero VARCHAR(50),
    estado ENUM('leído', 'pendiente') NOT NULL DEFAULT 'pendiente',
    fecha_inicio DATE,
    fecha_final DATE
);