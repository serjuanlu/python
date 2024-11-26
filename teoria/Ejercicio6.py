"""
Escribe un programa que muestre la nota final de un alumno a partir de su
calificación numérica (valor decimal).
"""

nota = float(input("Escriba su nota final: "))

match nota:
    case nota if nota >= 0 and nota < 5:
        print("Suspenso.")
    case nota if nota >= 5 and nota < 6:
        print("Aprobado.")
    case nota if nota >= 6 and nota < 7:
        print("Bien.")
    case edad if edad >= 7 and edad < 9:
        print("Notable.")
    case edad if edad >= 9 and edad < 10:
        print("Sobresaliente.")
    case edad if edad == 10:
        print("Matrícula de honor.")
    case _:
        print("Esa nota es incorrecta.")