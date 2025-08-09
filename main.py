productos = [{"Nombre": "Cartón de huevos", "Precio": 35},{"Nombre": "Queso", "Precio": 20},{"Nombre": "Macarrones", "Precio": 10},{"Nombre": "Shampoo", "Precio": 60},{"Nombre": "Jabón", "Precio": 5},{"Nombre": "Detergente", "Precio": 30},{"Nombre": "Cloro", "Precio": 40},{"Nombre": "Secadora de pelo", "Precio": 150},{"Nombre": "Pintauñas", "Precio": 70},{"Nombre": "Camisa", "Precio": 70 },{"Nombre": "Pantalón", "Precio": 125}]
class Carrito:
    def __init__(self):
        self.carrito = []

    def add(self,nombre,precio,cantidad):
        for item in self.carrito:
            if item["Nombre"] == nombre:
                item_exist = True
                item["Cantidad"] += cantidad
                break

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
            print("\n"+" Productos adquiridos ".center(50, "-"))
            print("Nombre".ljust(20) + "Precio".ljust(15) + "Cantidad".ljust(15) +"Subtotal".ljust(15))
            for i in self.carrito:
                subtotal = i["Precio"] * i["Cantidad"]
                total += subtotal
                print(i["Nombre"].ljust(20) + "Q"+str(i["Precio"]).ljust(15) + str(i["Cantidad"]).ljust(15) + f"Q{subtotal}".ljust(15))
            print(f"\nTOTAL: Q{total}".rjust(55))

    def orden(self):
        orientacion = input("¿Desea que el carrito se ordene de fomrma ascendente? (s/n): ").lower()
        if orientacion.startswith("s"):
            self.carrito.sort(key=lambda x:x["Nombre"])
        elif orientacion.startswith("n"):
            self.carrito.sort(key=lambda x:x["Nombre"],reverse = True)
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
                location = self.carrito.index(i)
                break
        return exist, location

main_carrito = Carrito()

while True:
    print("\n\n----------Bienvenido al carrito----------\n1. Agregar productos\n2. Ver el carrito\n3. Ordenar carrito\n4. Eliminar productos del carrito\n5. Buscar producto en el carrito\n6. Salir")
    select = input("Selccione una opción (1-5): ")
    match select:
        case "1":
            print("\n   "+" Productos disponibles ".center(40, "-"))
            for producto in productos:
                print(f"Nombre: {producto['Nombre']}".ljust(30) + f"Precio: Q{producto['Precio']}".ljust(25))

            while True:
                try:
                    nombre_select = input("\nIngrese el nombre del producto que desea añadir: ").lower().capitalize()
                    cantidad_select = int(input("¿cuántos productos va a adquirir?: "))
                    producto_ok = True
                    cantidad_ok = True
                    if not  any(producto["Nombre"] == nombre_select for producto in productos):
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
                    carrito_clear = False
                    if del_cant < 1:
                        print("La cantidad de productos debe ser mayor a 0")
                    elif del_cant > main_carrito.largo():
                        print("No hay tantos productos en el carrito")
                    elif del_cant == main_carrito.largo():
                        main_carrito.clear_carrito()
                        carrito_clear = True
                        print("Carrito limpiado exitosamente")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero")

            if not carrito_clear:
                for i in range(del_cant):
                    while True:
                        prod_name = input("Ingrese el nombre del producto: ").lower().capitalize()
                        trial = main_carrito.remove(prod_name)
                        if trial:
                            break

        case "5":
            producto_search = input("Ingrese el nombre del producto a buscar: ").lower().capitalize()
            exist, location = main_carrito.item_search(producto_search)
            if exist:
                print(f"El producto se encuentra en la posición {location+1} en el orden actual del carrito")
            else:
                print("El producto no existe")

        case "6":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")