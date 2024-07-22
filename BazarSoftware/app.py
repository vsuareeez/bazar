from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from models.producto_model import Producto
from models.cliente_model import Cliente
from models.cajero_model import Cajero
from models.venta_model import Venta
from datetime import datetime

# Configuración de la base de datos
engine = create_engine('sqlite:///bazar.db')

# Crear todas las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

def print_menu(title, options):
    """Imprime un menú con un título y opciones, con bordes cuadrados."""
    border = '+' + '-' * (len(title) + 2) + '+'
    print(border)
    print(f'| {title} |')
    print(border)
    for i, option in enumerate(options, 1):
        print(f'| {i}. {option:<{len(title)}} |')
    print(border)

def menu_principal():
    while True:
        print_menu("Menú Principal", [
            "Abrir Día de Ventas",
            "Cerrar Día de Ventas",
            "Productos",
            "Personas",
            "Salir"
        ])
        option = input("Seleccione una opción: ")

        if option == '1':
            menu_dia_ventas()
        elif option == '2':
            cerrar_dia_ventas()
        elif option == '3':
            menu_productos()
        elif option == '4':
            menu_personas()
        elif option == '5':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_dia_ventas():
    while True:
        print_menu("Menú Día de Ventas", [
            "Registrar Venta",
            "Cerrar Día de Ventas",
            "Volver"
        ])
        option = input("Seleccione una opción: ")

        if option == '1':
            registrar_venta()
        elif option == '2':
            cerrar_dia_ventas()
        elif option == '3':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_productos():
    while True:
        print_menu("Menú Productos", [
            "Agregar Producto",
            "Ver Productos",
            "Volver"
        ])
        option = input("Seleccione una opción: ")

        if option == '1':
            agregar_producto()
        elif option == '2':
            ver_productos()
        elif option == '3':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def menu_personas():
    while True:
        print_menu("Menú Personas", [
            "Agregar Cliente",
            "Ver Clientes",
            "Agregar Cajero",
            "Ver Cajeros",
            "Volver"
        ])
        option = input("Seleccione una opción: ")

        if option == '1':
            agregar_cliente()
        elif option == '2':
            ver_clientes()
        elif option == '3':
            agregar_cajero()
        elif option == '4':
            ver_cajeros()
        elif option == '5':
            break
        else:
            print("Opción inválida, intente nuevamente.")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto (CLP): "))
    producto = Producto(nombre=nombre, precio=precio)
    session.add(producto)
    session.commit()
    print("Producto agregado exitosamente.")

def ver_productos():
    productos = session.query(Producto).all()
    if productos:
        print("\nLista de Productos:")
        for producto in productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio} CLP")
    else:
        print("No hay productos disponibles.")

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    cliente = Cliente(nombre=nombre, direccion=direccion)
    session.add(cliente)
    session.commit()
    print("Cliente agregado exitosamente.")

def ver_clientes():
    clientes = session.query(Cliente).all()
    if clientes:
        print("\nLista de Clientes:")
        for cliente in clientes:
            print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Dirección: {cliente.direccion}")
    else:
        print("No hay clientes disponibles.")

def agregar_cajero():
    nombre = input("Ingrese el nombre del cajero: ")
    turno = input("Ingrese el turno del cajero: ")
    cajero = Cajero(nombre=nombre, turno=turno)
    session.add(cajero)
    session.commit()
    print("Cajero agregado exitosamente.")

def ver_cajeros():
    cajeros = session.query(Cajero).all()
    if cajeros:
        print("\nLista de Cajeros:")
        for cajero in cajeros:
            print(f"ID: {cajero.id}, Nombre: {cajero.nombre}, Turno: {cajero.turno}")
    else:
        print("No hay cajeros disponibles.")

def registrar_venta():
    id_producto = int(input("Ingrese el ID del producto: "))
    id_cliente = int(input("Ingrese el ID del cliente: "))
    id_cajero = int(input("Ingrese el ID del cajero: "))

    producto = session.query(Producto).get(id_producto)
    cliente = session.query(Cliente).get(id_cliente)
    cajero = session.query(Cajero).get(id_cajero)

    if producto and cliente and cajero:
        venta = Venta(id_producto=id_producto, id_cliente=id_cliente, id_cajero=id_cajero)
        session.add(venta)
        session.commit()
        print("Venta registrada exitosamente.")
    else:
        print("Error: Producto, cliente o cajero no encontrados.")

def cerrar_dia_ventas():
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ventas = session.query(Venta).all()
    total_ventas = 0

    if ventas:
        print(f"\nVentas del día ({fecha_actual}):")
        for venta in ventas:
            producto = session.query(Producto).get(venta.id_producto)
            cliente = session.query(Cliente).get(venta.id_cliente)
            cajero = session.query(Cajero).get(venta.id_cajero)

            if producto and cliente and cajero:
                print(f"Venta ID: {venta.id} - Producto: {producto.nombre}, Cliente: {cliente.nombre}, Cajero: {cajero.nombre}, Precio: {producto.precio} CLP")
                total_ventas += producto.precio

        print(f"\nTotal de ventas del día: {total_ventas} CLP")
    else:
        print("No se realizaron ventas hoy.")

if __name__ == "__main__":
    menu_principal()
