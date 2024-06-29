def convertir_unidades(valor, unidad_origen, unidad_destino):
    if unidad_origen == "metros" and unidad_destino == "pies":
        return valor * 3.28084
    elif unidad_origen == "litros" and unidad_destino == "galones":
        return valor * 0.264172
    else:
        return "Conversión no soportada"

valor = 10
unidad_origen = "metros"
unidad_destino = "pies"

resultado = convertir_unidades(valor, unidad_origen, unidad_destino)
print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")