productos = [{"Nombre": "Cartón de huevos","Tipo": "Comida" , "Precio": 35},{"Nombre": "Queso","Tipo": "Comida" , "Precio": 20},{"Nombre": "Macarrones","Tipo": "Comida" , "Precio": 10},{"Nombre": "Shampoo","Tipo": "Higiene" , "Precio": 60},{"Nombre": "Jabón","Tipo": "Higiene" , "Precio": 5},{"Nombre": "Detergente","Tipo": "Limpieza" , "Precio": 30},{"Nombre": "Cloro","Tipo": "Limpieza" , "Precio": 40},{"Nombre": "Secadora de pelo","Tipo": "Belleza" , "Precio": 150},{"Nombre": "Pintauñas","Tipo": "Belleza" , "Precio": 70},{"Nombre": "Camisa","Tipo": "Ropa" , "Precio": 70 },{"Nombre": "Pantalón","Tipo": "Ropa" , "Precio": 125}]
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

    def remove(self, nombre):
        deletion = False
        for item in self.carrito:
            if item["Nombre"] == nombre:
                self.carrito.remove(item)
                deletion = True
                break
        if not deletion:
            print("El objeto buscado no existe")

    def display(self):
        print(" Productos adquiridos ".center(50, "-"))
        print("Nombre".ljust(15) + "Precio".ljust(15) + "Cantidad".ljust(15))
        for i in self.carrito:
            print(i.Nombre.ljust(15) + i.Precio.ljust(15) + i.Cantidad.ljust(15))

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
            if i == item:
                exist = True
                location = self.carrito.index(item)
                break
        return exist, location

main_carrito = Carrito()

while True:
    print("\n\n----------Bienvenido al carrito----------\n1. Agregar productos\n2. Ver el carrito\n3. Ordenar carrito\n4. Eliminar producto del carrito\n5. Salir")
    select = input("Selccione una opción: ")
    match select:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamente")