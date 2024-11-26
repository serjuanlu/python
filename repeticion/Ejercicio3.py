"""
Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)
"""
numero = int(input("Introduce un número: "))
cont = 1
suma = numero
minimo = numero
maximo = numero

while numero != 0:
    numero = int(input("Introduce otro número: "))
    if numero == 0:
        break
    cont += 1
    suma += numero
    if numero < minimo:
        minimo = numero
    if numero > maximo:
        maximo = numero

if cont == 1:
    print("No se introdujeron valores distintos de cero.")
else:
    print(
        "La cantidad de números introducidos fueron",
        cont,
        ". El valor de su suma fue",
        suma,
        ". El valor mínimo introducido fue",
        minimo,
        "y el máximo fue",
        maximo,
        ". El valor de su media aritmética es",
        suma / (cont - 1),
    )
