"""
Escribe un programa que recoja un número de filas y columnas, y muestre una
tabla con tantas filas y columnas como indicadas, numerando las celdas de
izquierda a derecha y de arriba abajo.
"""

filas = int(input("¿Cuántas filas quieres mostrar? "))
columnas = int(input("¿Cuántas columnas quieres mostrar? "))

for i in range(1, filas + 1):
    for j in range(1, columnas + 1):
        valor = (i - 1) * columnas + j
        print(valor, " ", end=" ")
    print(" ")
