productos = [{"Nombre": "Cartón de huevos", "Precio": 35},{"Nombre": "Queso", "Precio": 20},{"Nombre": "Macarrones", "Precio": 10},{"Nombre": "Shampoo", "Precio": 60},{"Nombre": "Jabón", "Precio": 5},{"Nombre": "Detergente", "Precio": 30},{"Nombre": "Cloro", "Precio": 40},{"Nombre": "Secadora de pelo", "Precio": 150},{"Nombre": "Pintauñas", "Precio": 70},{"Nombre": "Camisa", "Precio": 70 },{"Nombre": "Pantalón", "Precio": 125}]
class Carrito:
    def __init__(self):
        self.carrito = []

    def add(self,nombre,precio,cantidad):
        item = {
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad
        }
        self.carrito.append(item)

    def largo(self):
        return len(self.carrito)

    def remove(self, nombre):
        deletion = False
        for item in self.carrito:
            if item["Nombre"] == nombre:
                self.carrito.remove(item)
                deletion = True
                break
        if not deletion:
            print("El objeto buscado no existe")
        return deletion

    def display(self):
        if not self.carrito:
            print("El carrito está vacío")
        else:
            total = 0
            print("\n Productos adquiridos ".center(50, "-"))
            print("Nombre".ljust(15) + "Precio".ljust(15) + "Cantidad".ljust(15) +"Subtotal".ljust(15))
            for i in self.carrito:
                subtotal = i.Precio * i.Cantidad
                total += subtotal
                print(i.Nombre.ljust(15) + "Q"+i.Precio.ljust(15) + i.Cantidad.ljust(15) + f"Subtotal: Q{subtotal}".ljust(15))
            print(f"TOTAL: Q{total}")

    def orden(self):
        orientacion = input("¿Desea que el carrito se ordene de fomrma ascendente? (s/n): ").lower()
        if orientacion.startswith("s"):
            self.carrito.sort()
        elif orientacion.startswith("n"):
            self.carrito.sort(reverse = True)
        else:
            print("Opción no válida")

    def clear_carrito(self):
        self.carrito.clear()

    def item_search(self,item):
        exist = False
        location = False
        for i in self.carrito:
            if i["Nombre"] == item:
                exist = True
                location = self.carrito.index(item)
                break
        return exist, location

main_carrito = Carrito()

while True:
    print("\n\n----------Bienvenido al carrito----------\n1. Agregar productos\n2. Ver el carrito\n3. Ordenar carrito\n4. Eliminar productos del carrito\n5. Buscar producto en el carrito\n6. Salir")
    select = input("Selccione una opción (1-5): ")
    match select:
        case "1":
            print("\n Productos disponibles ".center(40, "-"))
            for producto in productos:
                print(f"Nombre: {producto['Nombre']} Precio: Q{producto['Precio']}")

            while True:
                try:
                    nombre_select = input("Seleccione un producto: ").lower().capitalize()
                    cantidad_select = int(input("¿cuántos productos va a adquirir?: "))
                    producto_ok = True
                    cantidad_ok = True
                    if nombre_select not in any(producto["Nombre"] for producto in productos):
                        cantidad_ok = False
                        print("El producto seleccionado no existe")

                    if cantidad_select < 1:
                        cantidad_ok = False
                        print("La cantidad de productos debe ser positiva")

                    if producto_ok and cantidad_ok:
                        nombre = nombre_select
                        precio = 0
                        for producto in productos:
                            if producto["Nombre"] == nombre:
                                precio = producto["Precio"]
                        cantidad = cantidad_select
                        main_carrito.add(nombre,precio,cantidad)
                        break
                except ValueError:
                    print("La cantidad de productos debe ser un entero")
                except Exception as e:
                    print("Error inesperado: ",e)


        case "2":
            main_carrito.display()

        case "3":
            main_carrito.orden()

        case "4":
            print(f"\nSu carrito tiene {main_carrito.largo()} productos")
            while True:
                try:
                    del_cant = int(input("¿Cuántos productos va a eliminar?: "))
                    if del_cant < 1:
                        print("La cantidad de productos debe ser mayor a 0")
                    elif del_cant > main_carrito.largo():
                        print("No hay tantos productos en el carrito")
                    elif del_cant == main_carrito.largo():
                        main_carrito.clear_carrito()
                        print("Carrito limpiado exitosamente")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero")

            for i in range(del_cant):
                while True:
                    prod_name = input("Ingrese el nombre del producto: ")
                    trial = main_carrito.remove(prod_name)
                    if trial:
                        break


        case "5":
            pass

        case "6":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")