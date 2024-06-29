import json
from datetime import datetime

pizzas = [
    ["ID pizza","Tipo de pizza", "Tamaño", "Precio"],
    [1, "Margarita", "Pequeña", 5500],
    [2, "Margarita", "Mediana", 85000],
    [3, "Margarita", "Familia", 11000],
    [4, "Mexicana", "Pequeña", 7000],
    [5, "Mexicana", "Mediana", 10000],
    [6, "Mexicana", "Familiar", 13000],
    [7, "Barbacoa", "Pequeña", 6500],
    [8, "Barbacoa", "Mediana", 9500],
    [9, "Barbacoa", "Familiar", 12500],
    [10, "Vegetariana", "Pequeña", 5000],
    [11, "Vegetariana", "Mediana", 8000],
    [12, "Vegetariana", "Familiar", 10500],
]

ventas_registradas = []

def menu():

    print("\nBienvenido a PIZZAS DUOC.")
    print("1. Registrar una venta.")
    print("2. Mostrar todas las ventas.")
    print("3. Buscar ventas por cliente.")
    print("4. Guardas las ventas en un archivo.")
    print("5. Cargar las ventas desde un archivo.")
    print("6. Generar boleta.")
    print("7. Anular ventas.")
    print("8. Salir del programa")

    choice = int(input("\nIngrese una opcion: "))

    return choice

def datos_pizzas():

    print("Seleccione una Pizza: \n")

    for row in pizzas:
        print(row,"\n")

    id_pizza = int(input("Indique el ID de la pizza que desea comprar: "))

    pizza_finded = None

    for pizza in pizzas[1:]:

        if pizza[0] == id_pizza:
            pizza_finded = pizza
            break

    if pizza_finded:

        tipo_pizza = pizza_finded[1]
        tamaño_pizza = pizza_finded[2]
        precio_pizza = pizza_finded[3]

        return tipo_pizza, tamaño_pizza, precio_pizza

    else:

        print("Pizza no encontrada.")
        return None, None, None, None


def registrar_venta():

    rut = input("Por favor indiquime su RUT: ")
    nombre = input("Por favor deme su nombre: ")
    apellido = input("Por favor deme su apellido: ")
    tipo_cliente = ""

    print("\nIngrese el tipo de cliente.")
    print("1. diurno.")
    print("2. vespertino.")
    print("3. administrativo.")

    while True:

        try:

            choice = int(input("\nIngrese una opción: "))

            if choice == 1:

                tipo_cliente = "diurno"
                break
            elif choice == 2:

                tipo_cliente = "vespertino"
                break
            elif choice == 3:

                tipo_cliente = "administrativo"
                break

            else: print("Ingrese una opción válida.")

        except ValueError:
            print("Ingrese una opción válida.")

    tipo_pizza, tamaño_pizza, precio_pizza = datos_pizzas()

    if tipo_pizza:

        datos_venta = {
            "RUT": rut,
            "Nombre": nombre,
            "Apellido": apellido,
            "Tipo cliente": tipo_cliente,
            "Tipo Pizza": tipo_pizza,
            "Tamaño Pizza": tamaño_pizza,
            "Precio Pizza": precio_pizza
        }

        ventas_registradas.append(datos_venta)

        print("\nVenta registrada correctamente:")
        for key, value in datos_venta.items():
            print(f"{key}: {value}")

        return datos_venta

    else:

        print("\Pizza no encontrada. Venta no registrada.")
        return None

def visualizar_ventas():

    for rows in ventas_registradas:
        print(rows)

def exportar_ventas(nombre_archivo):

    with open(nombre_archivo, 'w') as file:
        json.dump(ventas_registradas, file, indent=4)

def buscar_ventas_por_rut(rut):

    encontradas = False

    for venta in ventas_registradas:

        if venta["RUT"] == rut:

            encontradas = True
            print("\nVenta encontrada:")

            for key, value in venta.items():
                print(f"{key}: {value}")

    if not encontradas:
        print("\nNo se encontraron ventas para el RUT proporcionado.")

def cargar_ventas(nombre_archivo):

    global ventas_registradas

    try:

        with open(nombre_archivo, 'r') as file:

            ventas_registradas = json.load(file)
            print(f"\nDatos de ventas cargados correctamente desde {nombre_archivo}.")

    except FileNotFoundError:

        print(f"\nEl archivo {nombre_archivo} no existe.")

def generar_factura(datos_ventas):

    print("\n************* FACTURA *************")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==================================")
    print(f"Nombre Cliente: {datos_ventas[0]['Nombre']} {datos_ventas[0]['Apellido']}")
    print(f"RUT Cliente: {datos_ventas[0]['RUT']}")
    print(f"Tipo Cliente: {datos_ventas[0]['Tipo cliente'].capitalize()}")
    print("----------- Detalles de Ventas -----------")

    total_sin_descuento = 0
    total_con_descuento = 0

    for datos_venta in datos_ventas:
        precio_pizza = datos_venta['Precio Pizza']

        # Calcular descuento según el tipo de cliente
        tipo_cliente = datos_venta['Tipo cliente']
        if tipo_cliente == 'diurno':
            descuento = 0.15
        elif tipo_cliente == 'vespertino':
            descuento = 0.18
        elif tipo_cliente == 'administrativo':
            descuento = 0.11
        else:
            descuento = 0

        precio_con_descuento = precio_pizza * (1 - descuento)


        total_sin_descuento += precio_pizza
        total_con_descuento += precio_con_descuento

        print(f"Tipo pizza: {datos_venta['Tipo Pizza']}")
        print(f"Tamaño pizza: {datos_venta['Tamaño Pizza']}")
        print(f"Precio pizza: ${precio_pizza}")
        print(f"Descuento aplicado: {descuento * 100}%")
        print(f"Precio con descuento: ${precio_con_descuento:.2f}")
        print("----------------------------------")


    print("==================================")
    print(f"Total sin descuento: ${total_sin_descuento:.2f}")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
    print("==================================")
    print("Gracias por su compra!")
    print("**********************************\n")



while True:

    choice = menu()

    if choice == 1:
        registrar_venta()

    elif choice == 2:
        visualizar_ventas()

    elif choice == 3:

        rut_buscar = input("\nIngrese el RUT del cliente para buscar las ventas: ")
        buscar_ventas_por_rut(rut_buscar)

    elif choice == 4:

        nombre_archivo = input("Asignale un nombre al archivo que deseas exportar: ")

        exportar_ventas(nombre_archivo)

        print(f"\nDatos de ventas exportados correctamente a {nombre_archivo}.")

    elif choice == 5:
        nombre_archivo = input("Ingrese el nombre del archivo que desea cargar: ")
        cargar_ventas(nombre_archivo)

    elif choice == 6:

        rut_buscar = input("\nIngrese el RUT del cliente para generar la factura: ")
        ventas_cliente = []

        for venta in ventas_registradas:
            if venta["RUT"] == rut_buscar:
                ventas_cliente.append(venta)

        if ventas_cliente:
            generar_factura(ventas_cliente)
        else:
            print("\nNo se encontraron ventas para el RUT proporcionado.")

    elif choice == 7:

        print("esta seguro que desea anular las ventas?! (1.si - 2.no) \n")
        anuu = int(input("Ingrese una opcion: "))

        if anuu == 1: 
          ventas_registradas = []
          print("ventas eliminadas")
        elif anuu == 2:
          print("no se eliminaron las ventas")
    elif anuu == 8:

        print("Adios!")
        break

    else: print("Ingrese una opcion valida.")