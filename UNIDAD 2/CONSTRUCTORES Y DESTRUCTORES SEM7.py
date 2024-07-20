class MyClass:
    """
    Esta clase demuestra el uso de constructores y destructores.

    El constructor (__init__) se encarga de inicializar los atributos de la clase.
    El destructor (__del__) se encarga de realizar tareas de limpieza o cierre de recursos cuando el objeto es eliminado.
    """

    def __init__(self, name, age):
        """
        Constructor de la clase MyClass.
        Inicializa los atributos name y age del objeto.
        """
        self.name = name
        self.age = age
        print(f"Objeto {self.name} creado.")

    def __del__(self):
        """
        Destructor de la clase MyClass.
        Realiza una tarea de limpieza o cierre de recursos cuando el objeto es eliminado.
        """
        print(f"Objeto {self.name} eliminado.")
        # Aquí puedes agregar código para cerrar archivos, conexiones a bases de datos, etc.

    def display_info(self):
        """
        Método que muestra la información del objeto.
        """
        print(f"Nombre: {self.name}, Edad: {self.age}")


# Crear un objeto de la clase MyClass
person = MyClass("Juan", 30)
person.display_info()

# El objeto person será eliminado automáticamente cuando salga del bloque de código
# En este momento, se activará el destructor (__del__) y se imprimirá el mensaje de eliminación