# 1 FUNCIONES
def mostrar_encabezado():
    print("====================")
    print(" Sistema de registro escolar")
    print("====================")

def datos_estudiantes():
    #CREAMOS UN DICCIONARIO
    estudiante = {}
    estudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            estudiante["semestre"] = int(input("Ingrese el semestre que cursa: "))
            if estudiante["semestre"] < 1 or estudiante["semestre"] > 5:
                print("Debe ingresar un semestre del 1 al 5")
            else:
                break
        except ValueError:
            print("Ingresa un numero")
    estudiante["carrera"] = input("Ingrese la carrera del estudiante: ")
    estudiante["rut"] = int (input("Ingresa el rut del estudiante: "))
    return estudiante

def mostrar_ficha(estudiante):
    print(f"Nombre estudiante: {estudiante["nombre"]}")
    print(f"Rut estudiante: {estudiante["rut"]}")
    print(f"Carrera estudiante: {estudiante["carrera"]}")
    print(f"Semestre estudiante: {estudiante["semestre"]}")

# 2 CODIGO PRINCIPAL
datos = datos_estudiantes()
mostrar_encabezado()
mostrar_ficha(datos)