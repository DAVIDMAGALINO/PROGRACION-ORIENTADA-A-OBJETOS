# Definir la clase base (superclase)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass


# Definir una clase que hereda de la clase Animal (subclase)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau guau"


# Crear una instancia de la clase Perro
mi_perro = Perro("Fido", 5, "Labrador")
print("Nombre:", mi_perro.nombre)
print("Edad:", mi_perro.edad)
print("Raza:", mi_perro.raza)
print("Sonido:", mi_perro.hacer_sonido())
