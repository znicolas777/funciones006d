# FUNCIONES
def convertir_calificaion(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) +1
    return round(nota, 1)


#CODIGO PRINCIPAL
while True:
    try:
        p = float(input("Ingrese el puntaje del estudiante: "))
        if p < 0:
            print("Ingrese un valor valido")
        else:
            break
    except ValueError:
        print("Ingresa un numero")
while True:
    try:
        pt = float(input("Ingrese el puntaje total de la evaluacion: "))
        if pt < 0:
            print("Ingrese un valor valido")
        else:
            break
    except ValueError:
        print("Ingresa un numero")
# LLAMAR FUNCION
calificacion = convertir_calificaion(p,pt)
print(f"La calificacion en escala chilena es: {calificacion}")
