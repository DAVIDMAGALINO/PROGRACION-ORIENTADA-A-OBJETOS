import datetime

# concretamos la hora actual y una lista con las horas que se requiere la temperatura
hora_actual = datetime.datetime.now().time()
horas = [6, 9, 13, 16, 20]
# ejemplo de semana con las horas de cada día
semana_1 = {'lunes': [9, 12, 19, 17, 15], 'martes': [12, 19, 22, 20, 18], 'miercoles': [10, 12, 25, 25, 15],
            'jueves': [9, 12, 17, 17, 15], 'viernes': [9, 10, 14, 15, 11], 'sabado': [9, 12, 19, 17, 15],
            'domingo': [19, 12, 24, 27, 25]}


# funcion que mira las temperaturas altas, bajas y media de la semana que se le pase por argumento
def datos(d):
    temp_alta = []
    temp_baja = []
    for i in d.values():
        temp_alta.append(max(i))
        temp_baja.append(min(i))
    media_alta = sum(temp_alta) / len(temp_alta)
    media_baja = sum(temp_baja) / len(temp_baja)

    return temp_alta, media_alta, temp_baja, media_baja


# Función para sacar la media de todos los lunes de los martes etc...
def datos_2(d):
    l = []
    for i in range(5):
        l.append([(lista[i]) for lista in d.values()])
        return l
    # for i in l:
    # print(sum(i)/len(i))


print(datos_2(semana_1))


# Funcion que pide la temperatura si coincide la hora con las demandadas
def pedir_temp():
    if hora_actual.hour in horas and hora_actual.minute == 0:
        temperatura = float(input('Introduce la temperatura: '))
    else:
        print("Todavía no es la hora de anotar temperatura.")
    return temperatura


# muestra un ejemplo de como mostrar los datos de la semana 1 como ejemplo
def resultados(semana):
    temp_alta, media_alta, temp_baja, media_baja = datos(semana)
    media_dias = datos_2(semana)

    # sum(i)/len(i)

    return f'''Datos de la Semana
  - Temperatura más alta --> {temp_alta}
  - Temperatura más baja --> {temp_baja}
  - Media más alta --------> {round(media_alta, 2)}
  - Media más baja --------> {round(media_baja, 2)}
     Media de cada día de la semana
     - Lunes -----> {media_dias[0][0]}
     - Martes ----> {media_dias[0][1]}
     - Miércoles -> {media_dias[0][2]}
     - Jueves ----> {media_dias[0][3]}
     - Viernes ---> {media_dias[0][4]}
     - Sábado ----> {media_dias[0][5]}
     - Domingo ---> {media_dias[0][6]}
  '''


print(resultados(semana_1))