"""
Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto.
"""
palabra = input("Escriba una palabra: ")
letra = input("¿Qué letra quieres buscar? ")
cont = 0

for n in palabra:
    if n == letra:
        cont += 1
else:
    print(cont, "veces")
