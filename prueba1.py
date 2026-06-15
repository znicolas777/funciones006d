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

def solicitar_opciones ():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1 or opcion > 6:
                print("Debe seleccionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("Seleccione una opcion valida")
            return opcion
# CODIGO PRINCIPAL


# DECLARAR LISTAS
datos_mascotas = {}
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()

