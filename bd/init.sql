CREATE DATABASE libros_bd;

USE libros_bd;


CREATE TABLE libros (
    referencia VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio INT NOT NULL,
    genero VARCHAR(50),
    estado ENUM('leído', 'pendiente') NOT NULL DEFAULT 'pendiente',
    fecha_inicio DATE,
    fecha_final DATE
);