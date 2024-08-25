class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("El producto ya existe. Utiliza 'actualizar_producto' para modificarlo.")
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            print("Producto agregado con éxito.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado con éxito.")
        else:
            print("El producto no existe.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado con éxito.")
        else:
            print("El producto no existe.")

    def buscar_producto(self, id_producto):
        if id_producto in self.productos:
            print(self.productos[id_producto])
        else:
            print("El producto no existe.")

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(producto)


def menu():
    inventario = Inventario()

    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Listar productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == '2':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío si no quieres cambiar): ")
            precio = input("Nuevo precio (deja vacío si no quieres cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

        elif opcion == '3':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '4':
            id_producto = input("ID del producto a buscar: ")
            inventario.buscar_producto(id_producto)

        elif opcion == '5':
            inventario.listar_productos()

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()