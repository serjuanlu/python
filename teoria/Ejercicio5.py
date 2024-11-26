"""
Escribe un programa que calcule el precio de entrada a un museo a partir de
la edad del visitante.
"""

edad = int(input("Escriba su edad: "))

match edad:
    case edad if edad > 0 and edad < 5:
        print("Entrada gratuita.")
    case edad if edad >= 5 and edad < 18:
        print("Su entrada cuesta 3 euros.")
    case edad if edad >= 18 and edad < 65:
        print("Su entrada cuesta 6 euros.")
    case edad if edad > 65:
        print("Entrada gratuita.")
    case _:
        print("Error al introducir la edad.")