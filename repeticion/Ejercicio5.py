"""
Escribe un programa que recoja un número por teclado y muestre los primeros
cuadrados hasta llegar al número introducido.
"""

numero = int(input("Escribe un numero: "))
i = 1

for _ in range(i, numero + 1):
    print(pow(i, 2), " ", end="")
    i += 1
