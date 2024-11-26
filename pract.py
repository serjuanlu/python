#Practica Juan Luis Serrano

#Importamos 
import random

#Opcion a, mostrar el valor de un dado
def mostrar_dado():
    dado = random.randint(1,6)
    print(f"\nEl valor del dado es {dado}")

#Opcion b, comprobar cual es mayor
def comprobarMayor():
    #iniciamos el try catch
    try:
        cantidad=int(input("\n¿Cuantos numeros vas a introducir? "))
        if cantidad<1:
            print("Debes introducir al menos un numero\n")

        #creamos el array que va a guardar los numeros
        numeros=[]
        for i in range(cantidad):
            num = int(input(f"Introduce el numero {i+1}: "))
            numeros.append(num)
            if i>0 and num <= numeros[i-1]:
                print(f"El numero {num} no es mayor que {numeros[i-1]}")
    except ValueError:
        print("Entrada no valida. Por favor, introduce un numero valido.")

#Opcion c: Mostrar anos bisiestos y multiplos de 10
def esBisiestoOMultiplo():
    try:
        inicio= int(input("\nIntroduce el primer año: "))
        fin= int(input("\nIntroduce el segundo año: "))
        if inicio>fin:
            #para cambiar el orden
            inicio, fin = fin, inicio
        #inicio del programa
        print(f"\nAños bisiestos y múltiplos de 10 entre {inicio} y {fin}")
        for anio in range(inicio, fin + 1):
            if(anio%4==0 and (anio%100!=0 or anio%400==0)) and anio %10==0:
                print(anio, end=" ")
        print()
    except ValueError:
        print("Entrada invalida. Por favor, introduce datos validos.")

#Opcion d: Mostrar rectangulo con numeros impares
def mostrarRectanguloImpares():
    try:
        filas = int(input("\nIntroduce el numero de filas: "))
        columnas = int(input("Introduce el numero de columnas: "))
        impares = [i for i in range(99, 0, -2)]

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

#menu
def menu():
    while True:
        print("MENU DE OPCIONES")
        print("a)Visualizar el valor de un dado.")
        print("b)Mensaje cuando el numero introducido no sea mayor que el primero.")
        print("c)Ingrese dos años para ver los que sean bisiestos en ese rango.")
        print("d)Mostrar un rectangulo con numeros impares entre 0 y 100")
        print("e)Salir")

        opcion = input("\nSelecciona una opcion: ").lower()

        if opcion == 'a':
            mostrar_dado()
        elif opcion == 'b':
            comprobarMayor()
        elif opcion == 'c':
            esBisiestoOMultiplo()
        elif opcion == 'd':
            mostrarRectanguloImpares()
        elif opcion == 'e':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    menu()