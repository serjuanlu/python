"""
Escribe un programa que lea tres números y que muestre los números mayor
y menor.
"""

numero1 = int(input("Escriba un número: "))
numero2 = int(input("Escriba otro número: "))
numero3 = int(input("Escriba otro número: "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print("El número más grande es", mayor,", y el más pequeño el", menor,".")