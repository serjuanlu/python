# Pedimos al usuario que introduzca un número
numero = int(input("Introduce un número: "))

# Bucle externo que controla el número de filas
for i in range(1, numero * 2, 2):  # i incrementa de 2 en 2 para obtener solo impares
    # Bucle interno que imprime los números impares decrecientes
    for j in range(i, 0, -2):  # j comienza en i y decrece de 2 en 2
        print(j, end=" ")  # Imprimimos el número sin salto de línea

    print()  # Salto de línea después de cada fila