from controladores.venta_controller import registrar_venta, obtener_ventas

def menu_venta():
    while True:
        print("\nMenú de Ventas")
        print("1. Registrar Venta")
        print("2. Ver Ventas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = int(input("ID del producto: "))
            id_cliente = int(input("ID del cliente: "))
            cantidad = int(input("Cantidad: "))
            total = float(input("Total: "))
            registrar_venta(id_producto, id_cliente, cantidad, total)
        elif opcion == "2":
            ventas = obtener_ventas()
            for venta in ventas:
                print(f"ID: {venta.id}, Producto: {venta.producto.nombre}, Cliente: {venta.cliente.nombre}, Cantidad: {venta.cantidad}, Total: {venta.total}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
