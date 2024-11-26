"""
Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares.
"""
numero = int(input("Introduzca un número: "))
impar = 1

for i in range(numero):
    impares = ""
    for j in range(impar, 0, -2):
        impares += str(j) + " "
    print(impares + " ")
    impar += 2


    

