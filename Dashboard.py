import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/1.2.1 ABSTRACCION/PROYECTO ABSTRACCION SEM2.py',
        '2': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/1.2.2 ENCAPSULACION/PROYECTO ENCAPSULACION SEM2.py',
        '3': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/1.2.3 HERENCIA/PROYECTO HERENCIA SEM2.py',
        '4': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/1.2.4 POLIMORFISMO/PROYECTO POLIMORFISMO SEM2.py',
        '5': 'UNIDAD 1/1.3 PROGRAMACION TRADICIONAL Y POO/METODO DE POO/METODO DE POO SEM3.py',
        '6': 'UNIDAD 1/1.3 PROGRAMACION TRADICIONAL Y POO/METODO TRADICIONAL/METODO TRADICIONAL DE PROGRAMACION SEM3.py',
        '7': 'UNIDAD 1/1.4 EJEMPLO DE MUNDO REAL/EJEMPLO MUNDO REAL POO/EjemploMundoReal_POO SEM4.py',
        '8': 'UNIDAD 2/1.5 TIPOS DE DATOS IDENTIFICADORES/CONVERTIR UNIDADES SEM5.py',
        '9': 'UNIDAD 2/1.6 CONCEPTOS DE POO UTILIZADOS/APLICACION DE CONCEPTOS POO SEM6.py',
        '10': 'UNIDAD 2/1.7 CONSTRUCTORES Y DESTRUCTORES/CONSTRUCTORES Y DESTRUCTORES SEM7.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()