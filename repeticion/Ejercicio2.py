"""
Escribe un programa que recoja un número y calcule su factorial.
"""

numero = int(input("Introduzca un número: "))
cont = 1

while numero > 0:
    cont = cont * numero 
    numero -= 1
else:
    print("El factorial es", cont)
