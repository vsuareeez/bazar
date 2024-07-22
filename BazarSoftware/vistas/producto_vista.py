from controladores.producto_controller import agregar_producto, obtener_productos

def menu_producto():
    while True:
        print("\nMenú de Productos")
        print("1. Agregar Producto")
        print("2. Ver Productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = input("Precio del producto: ")
            agregar_producto(nombre, float(precio))
        elif opcion == "2":
            productos = obtener_productos()
            for producto in productos:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
