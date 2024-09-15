import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de texto."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        nombre, cantidad, precio = linea.strip().split(',')
                        self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
            except (FileNotFoundError, ValueError) as e:
                print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de texto."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto al inventario."""
        if nombre in self.productos:
            self.productos[nombre].cantidad += cantidad
            print(f"Cantidad actualizada para {nombre}. Nueva cantidad: {self.productos[nombre].cantidad}")
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
            print(f"Producto {nombre} agregado al inventario.")
        self.guardar_inventario()

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la información de un producto."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre].cantidad = cantidad
            if precio is not None:
                self.productos[nombre].precio = precio
            print(f"Producto {nombre} actualizado.")
            self.guardar_inventario()
        else:
            print(f"Producto {nombre} no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto {nombre} eliminado del inventario.")
            self.guardar_inventario()
        else:
            print(f"Producto {nombre} no encontrado en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario."""
        for producto in self.productos.values():
            print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    # Agregando productos
    inventario.agregar_producto("Lápiz", 10, 0.5)
    inventario.agregar_producto("Goma", 5, 0.75)

    # Mostrando inventario
    inventario.mostrar_inventario()

    # Actualizando un producto existente
    inventario.actualizar_producto("Lápiz", cantidad=15)

    # Eliminando un producto
    inventario.eliminar_producto("Goma")

    # Mostrando inventario final
    inventario.mostrar_inventario()
