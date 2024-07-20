# Lista con temperaturas diarias
temperaturas = [20, 22, 24, 25, 23, 21, 20]

# Función para calcular el promedio de una lista de valores
def promedio(valores):
    return sum(valores) / len(valores)

# Calcular el promedio semanal
promedio_semanal = promedio(temperaturas)

print("El promedio semanal del clima es: ", promedio_semanal)
