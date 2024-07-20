# Clase base
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def hacer_sonido(self):
        pass

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza

    def hacer_sonido(self):
        return "Guau!"

    def get_raza(self):
        return self.__raza

# Crear instancias de las clases
animal_generico = Animal("Animal")
perro = Perro("Firulais", "Labrador")

# Acceder a métodos y atributos
print("Nombre del animal genérico:", animal_generico.get_nombre())
print("Nombre del perro:", perro.get_nombre())
print("Raza del perro:", perro.get_raza())

# Polimorfismo
def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

hacer_sonido_animal(animal_generico)
hacer_sonido_animal(perro)
def get_matricula(self):
    return self.__matricula

class Vehiculo:
    """
    Clase base Vehiculo
    """
    def __init__(self, marca, modelo, color):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color

    def __str__(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Color: {self.__color}"

    def arrancar(self):
        print("El vehículo ha arrancado.")

    def frenar(self):
        print("El vehículo ha frenado.")

class Automovil(Vehiculo):
    """
    Clase derivada Automovil que hereda de Vehiculo
    """
    def __init__(self, marca, modelo, color, num_puertas):
        super().__init__(marca, modelo, color)
        self.__num_puertas = num_puertas

    def __str__(self):
        return super().__str__() + f", Número de puertas: {self.__num_puertas}"

    def arrancar(self):
        print("El automóvil ha arrancado.")

    def frenar(self):
        print("El automóvil ha frenado.")

    def abrir_puertas(self):
        print("Las puertas del automóvil se han abierto.")

# Ejemplo de polimorfismo
def mostrar_vehiculo(vehiculo):
    print(vehiculo)
    vehiculo.arrancar()
    vehiculo.frenar()
    if isinstance(vehiculo, Automovil):
        vehiculo.abrir_puertas()

# Creación de objetos
vehiculo = Vehiculo("Toyota", "Corolla", "Azul")
automovil = Automovil("Honda", "Civic", "Rojo", 4)

# Llamada a la función polimórfica
mostrar_vehiculo(vehiculo)
print()
mostrar_vehiculo(automovil)