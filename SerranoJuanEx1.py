# Autor: Juan Luis Serrano Vilchez

#Fecha: 23/10/24

#a) Reemplazar vocales de una frase
def reemplazarVocales():
    #Pedimos la frase original
    fraseOri = input("Introduce una frase para reemplazar sus vocales por * \n")
    #Introducimos la vocales
    vocales="aeiouAEIOU"
    #Creamos un string vacio para guardar la frase resultado
    fraseResult=""
    #Recorremos la frase original por caracter
    for i in fraseOri:
        #Si el indice esta en el String de Vocales, anyadimos un *
        if i in vocales:
            fraseResult+="*"
        #Si no, anyadimos la letra
        else:
            fraseResult+=i
    #Imprimimos el resultado
    print(fraseResult)


#b) comprobar cual es mayor
def comprobarMayor():
    #iniciamos el try catch
    try:
        #Pedimos los numeros que vamos a anyadir
        cantidad=int(input("\n¿Cuantos numeros vas a introducir? "))
        #Si es negativa, volvemos a pedir
        if cantidad<1:
            print("Debes introducir al menos un numero\n")
        #creamos el array que va a guardar los numeros
        numeros=[]
        #Recorremos el array para rellenarlo, poniendo de tope la cantidad pedida
        for i in range(cantidad):
            #Pedimos los numeros individualmente
            num = int(input(f"Introduce el numero {i+1}: "))
            #Y lo anyadimos al array
            numeros.append(num)
            #Si el numero es menor que el anterior, lo decimos
            if i>0 and num <= numeros[i-1]:
                print(f"El numero {num} no es mayor que {numeros[i-1]}")
    #Mensaje de error
    except ValueError:
        print("Entrada no valida. Por favor, introduce un numero valido.")

#c)Encontrar la primera palabra más larga 
def encontrarPalabraLarga():
    #Pedimos la frase
    cadena = input("Introduce una frase para comprobar que palabra es mas larga\n")
    #La dividimos en un array usando los espacios como separadores
    lista = cadena.split(" ")
    #Inicializamos una palabra como la mas corta (1 letra)
    placeholder = "a"
    for i in lista:
        #Si la longitud de una palabra es mayor que el placeholder, se sustituye
        #Por esto, se van sustituyendo conforme encuentra palabras mas largas
        if len(i)>len(placeholder):
            placeholder=i
    #Devolvemos la palabra mas larga
    print(f"La palabra mas larga es {placeholder}")

#d) Mostrar rectangulo con numeros impares
def mostrarRectanguloImpares():
    try:
        #Pedimos las filas y las columnas
        filas = int(input("\nIntroduce el numero de filas: "))
        columnas = int(input("Introduce el numero de columnas: "))
        #Guardamos los impares con un for decreciente de 99 a 0 de 2 en 2
        impares = [i for i in range(99, 0, -2)]
        #Si los numeros son mayores que los impares que hay, lo pedimos otra vez
        if filas*columnas>len(impares):
            print(f"No hay suficientes numeros impares para llenar el rectangulo")
            return
        
        print("n\Rectangulo de numeros impares:")
        for i in range(filas):
            for j in range(columnas):
                print(f"{impares[i*columnas+j]:2d}", end=" ")
            print()
    except ValueError:
        print("Entrada invalida. Por favor, introduce datos validos.")

#e)contar la aparicion de cada caracter dentro de una palabra
def contarCaracter():
    #Pedimos los datos por teclado y los pasamos a minuscula
    cadena = input("Introduce una cadena para contar sus caracteres\n").lower()
    #Creamos un set vacio
    setCad= set()
    #Recorremos los caracteres de la cadena
    for i in cadena:
            #Anyadimos el caracter, : , y las veces que aparece         
            setCad.add(i+":"+str(cadena.count(i)))
    #E imprimimos el set
    print(setCad)

#menu
def menu():
    while True:
        print("MENU DE OPCIONES")
        print("a)Reemplazar vocales de una frase")
        print("b) Mensaje cuando el numero introducido no sea mayor que el primero.")
        print("c)Encontrar la primera palabra más larga.")
        print("d)Mostrar un rectangulo con numeros impares entre 0 y 100")
        print("e)Contar la aparición de cada carácter en una palabra")
        print("f)Salir")

        opcion = input("\nSelecciona una opcion: ").lower()

        if opcion == 'a':
            reemplazarVocales()
        elif opcion == 'b':
            comprobarMayor()
        elif opcion == 'c':
            encontrarPalabraLarga()
        elif opcion == 'd':
            mostrarRectanguloImpares()
        elif opcion == 'e':
            contarCaracter()     
        elif opcion == 'f':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    menu()