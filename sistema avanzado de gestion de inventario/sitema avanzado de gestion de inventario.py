import json


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio,
        }


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
            return True
        return False

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id].establecer_precio(precio)
            return True
        return False

    def buscar_producto_por_nombre(self, nombre):
        return {id: p for id, p in self.productos.items() if nombre.lower() in p.obtener_nombre().lower()}

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.obtener_id()}, Nombre: {producto.obtener_nombre()}, "
                  f"Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.productos = {id: Producto(**p) for id, p in data.items()}
        except FileNotFoundError:
            print("El archivo no existe, inicializando inventario vacío.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")


# Función principal para demostración
if __name__ == "__main__":
    inventario = Inventario()
    inventario.cargar_inventario('inventario.json')

    # Agregar productos
    inventario.agregar_producto(Producto(1, 'Laptop', 10, 999.99))
    inventario.agregar_producto(Producto(2, 'Mouse', 30, 19.99))

    # Mostrar productos
    print("Productos en el inventario:")
    inventario.mostrar_productos()

    # Actualizar un producto
    inventario.actualizar_producto(2, cantidad=25, precio=17.99)

    # Buscar productos por nombre
    print("\nBuscar productos que contienen 'Laptop':")
    resultados = inventario.buscar_producto_por_nombre('Laptop')
    for id, producto in resultados.items():
        print(f"ID: {id}, Nombre: {producto.obtener_nombre()}, Precio: {producto.obtener_precio()}")

    # Eliminar un producto
    inventario.eliminar_producto(1)

    # Mostrar productos después de eliminación
    print("\nProductos en el inventario después de eliminar la Laptop:")
    inventario.mostrar_productos()

    # Guardar inventario
    inventario.guardar_inventario('inventario.json')
