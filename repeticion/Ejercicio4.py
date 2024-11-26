"""
Escribe un programa que recoja un número y muestre un triángulo.
"""
numero = int(input("Introduce un número: "))
i = 1

for _ in range(i, numero + 1):
    print("* " * i)
    i += 1
