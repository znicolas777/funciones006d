# FUNCIONES

def alctualizar_vacunacion():
    for m in lista_m:
        if m["edad"] >= 1:
            m["vacunada"] = True
        else:
            m["vacunada"] = False

def buscar_mascota(lista_m , nombre_m):
    for i in range(len(lista_m)):
        if lista_m[i]["nombre"]:
            return i
        return -1 # se termino el ciclo por lo tanto no lo encontro

def mostrar_menu():
    print("************************")
    print("**** MENU PRINCIPAL ****")
    print("1.- Agregar Mascota")
    print("2.- Buscar Mascota")
    print("3.- Eliminar Mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar Mascota")
    print("6.- Salir")
    print("************************")

    #Funciones de validacion
def validar_nombre(name):
    return name.strip() != ""

def validar_especie(especie):
    especies_validas = ["perro","gato", "ave"]
    return especie.strip().lower() in especies_validas

def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0 

def solicitar_opciones ():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if  opcion < 1 or opcion > 6:
                print("Debe seleccionar una opcion del 1 al 6")
            else:
                return opcion
                break
        except ValueError:
            print("Seleccione una opcion valida")
            
    
    #Funcion para la opcion
def agregar_mascota(lista_m):
    #Solicitamos los datos
    nombre = input("Ingrese el nombre de la mascota: ")
    correcta = validar_nombre(nombre)
    if not correcta:
        print("El nombre no puede estar en blanco")
        return
    especie = input("Ingrese la especie de su mascota (perro,gato o ave): ")
    correcta = validar_especie(especie)
    if not correcta:
        print("La especie solo puede ser perro, gato o ave")
        return
    edad = input("Ingrese la edad de la mascota: ")
    correcta = validar_edad(edad)
    if not correcta:
        print("La edad debe ser un numero entero mayor a cero")
        return

    #crear diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }

    #Agregar a lista

    lista_m.append(mascota)
    print("Mascota agregada correctamente")


# CODIGO PRINCIPAL


# DECLARAR LISTAS
datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()

    if op == 1:
        agregar_mascota(datos_mascotas)
    elif op == 2:
        print("***** Buscar Mascota *****")
        nom = input("Ingrese el nombre de la mascota a buscar: ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            m = datos_mascotas[posicion]
            print(f"mascota encontrada en la posicion: {posicion}")
            print(f"Nombre mascota: {m["nombre"]}")
            print(f"Especie mascota: {m["especie"]}")
            print(f"edad mascota: {m["edad"]}")
            print(f"vacunada: {m["vacunada"]}")
        else:
            print(f"No encontramos a la mascota con el nombre: {nom}")
    elif op == 3:
        print("***** Eliminar Mascota *****")
        nom = input("Ingrese el nombre de la mascota a eliminar: ")
        posicion = buscar_mascota(datos_mascotas, nom)
        if posicion != -1:
            datos_mascotas.pop(posicion)
            print("mascota eliminada correctamente")
        else:
            print(f"La mascota {nom} no se encuentra registrada")
    elif op == 4:
        print("estado de vacunas actualizadas")
    elif op == 5:
        alctualizar_vacunacion(datos_mascotas)
        if len(datos_mascotas):
            print("No hay mascotas en la lista")
        else:
            print("== Lista de mascotas")
            for m in datos_mascotas:
                print(f"Nombre: {m["nombre"]}")
                print(f"Especie: {m["especie"]}")
                print(f"edad: {m["edad"]}")
            estado = "AL DIA" if m["vacunada"] else "PENDIENTE"
            print(f"Estado Vacuna: {estado}")
    elif op == 6:
        print("Gracias por usar el sistema")
