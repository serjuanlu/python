"""
Escribe un programa que recoja un mes del año (en número) y devuelva el
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
mostrar un mensaje de error.
"""

mes = int(input("Escriba el mes: "))

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31")
    case 4 | 6 | 9 | 11:
        print("30")
    case 2:
        print("28")
    case _:
        print("Mes incorrecto.")