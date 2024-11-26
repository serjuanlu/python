"""
Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido.
"""
numero = int(input("Escriba un número impar: "))

while numero % 2 == 0:
    numero = int(input("Por favor, escriba un número impar: "))

altura = (numero + 1) // 2
print("la altura es",altura)

for i in range(1, altura + 1):
    espacios = altura - i
    asteriscos = 2 * i - 1
    linea = " " * espacios + "*" * asteriscos
    print(linea)
