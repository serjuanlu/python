'''
Escribe un programa que recoja un texto y escriba cada letra del texto en una
línea distinta.
'''

palabra = input("Escriba una palabra: ")
i=len(palabra)
print(i)
for n in palabra:
    print(n)
x=0
while x<i:
   print(palabra[x])
   x=x+1