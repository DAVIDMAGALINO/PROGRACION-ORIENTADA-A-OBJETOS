# Definir la clase Clima
class Clima:
    def __init__(self, temperaturas):
        self.temperaturas = temperaturas

    def promedio_semanal(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase Clima con las temperaturas de la semana
clima_semanal = Clima([20, 22, 25, 23, 21, 20, 24])

# Calcular el promedio semanal del clima
promedio = clima_semanal.promedio_semanal()

# Imprimir el resultado
print("El promedio semanal del clima es:", promedio)