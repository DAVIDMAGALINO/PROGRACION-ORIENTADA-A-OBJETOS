class Figura:
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


figuras = [Circulo(5), Cuadrado(4)]

for figura in figuras:
    print(f"El área de la figura es: {figura.calcular_area()}")
