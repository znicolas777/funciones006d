# FUNCIONES
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
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema")
