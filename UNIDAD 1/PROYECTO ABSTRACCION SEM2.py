class POO:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_descuento(self, porcentaje):
        descuento = self.salario * (porcentaje / 100)
        return descuento

    def calcular_salario_neto(self, porcentaje_descuento):
        descuento = self.calcular_descuento(porcentaje_descuento)
        salario_neto = self.salario - descuento
        return salario_neto

# Ejemplo de uso
empleado1 = POO("Juan", 1000)
descuento = empleado1.calcular_descuento(10)
salario_neto = empleado1.calcular_salario_neto(10)

print(f"El salario de {empleado1.nombre} es: {empleado1.salario}")
print(f"El descuento es: {descuento}")
print(f"El salario neto es: {salario_neto}")
