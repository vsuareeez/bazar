-- Crear la base de datos
CREATE DATABASE bazar;

-- Crear la tabla de productos
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
);

-- Crear la tabla de clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

-- Crear la tabla de ventas
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER,
    id_cliente INTEGER,
    cantidad INTEGER NOT NULL,
    total REAL NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
