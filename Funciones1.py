# 1 CREAR FUNCIONES

def datos_producto(name, stock, price):
    print("=============================")
    print(f"Nombre del producto {name} ")
    print(f"Precio del producto {price} ")
    print(f"Stock del producto {stock} ")
    print("=============================")

# 2 CODIGO PRINCIPAL

nombre = input("Ingrese el nombre del producto: ")
while True:
    try:
        precio = int(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("Ingresa un numero ")
while True:
    try:
        stock = int(input("Ingresa el stock del producto: "))
        if precio < 0:
            print("Debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("Ingresa un numero")

# 3 LLAMAR A LA FUNCION

datos_producto(nombre,stock,precio)
