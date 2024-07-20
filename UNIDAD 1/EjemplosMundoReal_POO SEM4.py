class Producto:
    """
    Clase que representa un producto en la tienda.
    """
    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        """
        Método que permite reservar un producto si está disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"Se ha reservado el producto '{self.nombre}'.")
        else:
            print(f"Lo siento, el producto '{self.nombre}' no está disponible.")

class Cliente:
    """
    Clase que representa a un cliente de la tienda.
    """
    def __init__(self, nombre, carrito):
        self.nombre = nombre
        self.carrito = carrito

    def agregar_producto(self, producto):
        """
        Método que permite agregar un producto al carrito de compras.
        """
        self.carrito.append(producto)
        print(f"{self.nombre} ha agregado '{producto.nombre}' al carrito.")

    def realizar_reserva(self):
        """
        Método que permite realizar la reserva de los productos en el carrito.
        """
        for producto in self.carrito:
            producto.reservar()
        self.carrito = []
        print(f"{self.nombre} ha realizado la reserva de los productos en su carrito.")

# Crear algunos productos
producto1 = Producto("Camiseta", 19.99, True)
producto2 = Producto("Pantalón", 39.99, True)
producto3 = Producto("Zapatos", 59.99, False)

# Crear un cliente y agregar productos a su carrito
cliente = Cliente("Juan", [])
cliente.agregar_producto(producto1)
cliente.agregar_producto(producto2)
cliente.agregar_producto(producto3)

# Realizar la reserva de los productos en el carrito
cliente.realizar_reserva()