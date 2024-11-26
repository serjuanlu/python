"""
Escribe un programa que recoja un número y calcule si es primo.
"""
numero = int(input("Introduce un número: "))
i = 2
bandera = True

while i < numero and bandera:
    if numero % i == 0:
        bandera = False
    i += 1

if bandera:
    print("El número es primo.")
else:
    print("El número no es primo.")
