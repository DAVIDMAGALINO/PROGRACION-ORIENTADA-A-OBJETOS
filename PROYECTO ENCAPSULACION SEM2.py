class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def get_atributo_privado(self):
        return self.__atributo_privado

    def set_atributo_privado(self, nuevo_valor):
        self.__atributo_privado = nuevo_valor

objeto = MiClase()
print(objeto.get_atributo_privado())  # Accediendo al atributo privado
objeto.set_atributo_privado(20)  # Modificando el atributo privado
print(objeto.get_atributo_privado())  # Verificando el cambio
