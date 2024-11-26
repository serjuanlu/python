"""
Escribe un programa que recoja la hora del día y devuelva un saludo:
"""

hora = int(input("Escriba la hora: "))

match hora:
    case hora if hora >= 7 and hora < 12:
        print("Buenos días")
    case hora if hora >= 12 and hora < 20:
        print("Buenas tardes")
    case hora if hora >= 20 and hora <= 24:
        print("Buenas noches")
    case hora if hora >= 0 and hora < 7:
        print("Buenas noches")
    case _:
        print("Esa hora es incorrecta.")