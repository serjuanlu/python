# Ejercicio 1: Programa con un diccionario para un solo usuario
def ejercicio1():
    usuario = {}
    usuario["nombre"] = input("Introduce tu nombre: ")
    usuario["edad"] = int(input("Introduce tu edad: "))
    usuario["direccion"] = input("Introduce tu dirección: ")
    usuario["telefono"] = input("Introduce tu número de teléfono: ")

    print(f'{usuario["nombre"]} tiene {usuario["edad"]} años, vive en {usuario["direccion"]} y su número de teléfono es {usuario["telefono"]}.')

# Ejercicio 2: Manejo de múltiples usuarios
def ejercicio2():
    usuarios = {}
    while True:
        nombre = input("Introduce el nombre (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        edad = int(input("Introduce la edad: "))
        direccion = input("Introduce la dirección: ")
        telefono = input("Introduce el teléfono: ")

        usuarios[nombre] = {
            "edad": edad,
            "direccion": direccion,
            "telefono": telefono
        }

    for nombre, info in usuarios.items():
        print(f'{nombre} tiene {info["edad"]} años, vive en {info["direccion"]} y su número de teléfono es {info["telefono"]}.')

# Ejercicio 3: Análisis de ventas
def ejercicio3():
    ventas = {
        "A": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1},
        "B": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4},
        "C": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2},
        "D": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0}
    }

    # 1. Calcular el total de unidades vendidas en el mes para cada producto
    total_mensual = {producto: sum(dias.values()) for producto, dias in ventas.items()}
    print("\nTotal mensual de cada producto:")
    for producto, total in total_mensual.items():
        print(f"{producto}: {total} unidades")

    # 2. Identificar el producto con más y menos ventas en el mes
    producto_mas_vendido = max(total_mensual, key=total_mensual.get)
    producto_menos_vendido = min(total_mensual, key=total_mensual.get)
    print(f"\nProducto más vendido: {producto_mas_vendido} con {total_mensual[producto_mas_vendido]} unidades")
    print(f"Producto menos vendido: {producto_menos_vendido} con {total_mensual[producto_menos_vendido]} unidades")

    # 3. Mostrar las ventas diarias del producto más vendido
    print(f"\nVentas diarias del producto más vendido ({producto_mas_vendido}):")
    for dia, cantidad in ventas[producto_mas_vendido].items():
        print(f"Día {dia}: {cantidad} unidades")

    # 4. Encontrar el día con la mayor venta para cada producto
    print("\nDía con mayor cantidad de ventas para cada producto:")
    for producto, dias in ventas.items():
        dia_max = max(dias, key=dias.get)
        print(f"{producto}: Día {dia_max} con {dias[dia_max]} unidades")

# Menú principal
def menu():
    while True:
        print("\nMENÚ DE EJERCICIOS")
        print("1. Información de un usuario (Ejercicio 1)")
        print("2. Manejo de múltiples usuarios (Ejercicio 2)")
        print("3. Análisis de ventas (Ejercicio 3)")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            ejercicio1()
        elif opcion == '2':
            ejercicio2()
        elif opcion == '3':
            ejercicio3()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    menu()
