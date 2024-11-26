import array as arr
def diccionarioNum():
    numTope = int(input("Introduce el final del diccionario a crear\n"))
    dicVacio = dict()
    for i in range(1, numTope+1):
        dicVacio[i]=i*i
    print(dicVacio)
    # numeros=dict(for i in range(1, numTope, 1))

def diccionarioCadena():
    cadena = input("Introduce una frase para crear un diccionario\n")
    dicVacio = dict()

    for i in cadena:
        # contador = 0
        dicVacio[i]=i

    print(dicVacio)
    # numeros=dict(for i in range(1, numTope, 1))
def diccionarioFruta():
    dicVacio = dict()
    dicVacio={'Pera':1.60,
              'Ciruela':2,
              'Manzana':1.75,
              'Sandia':0.75}
    sigue = True
    while sigue:
        
        nombreFruta=input("Introduce el nombre de la fruta\n")
        for i in dicVacio.keys():
            print(i)
        cant=int(input("Introduce la cantidad de frutas vendidas\n"))

        print(dicVacio.get(nombreFruta),"*",cant,"=",dicVacio.get(nombreFruta)*cant )
        if input("Quieres que continue el programa?\n [y/n]\n")=='n':
            sigue = False

def diccionarioAlumnos():
    dicVacio = dict()

    numAlumn = int(input("Introduce el numero de alumnos: "))

    for i in range(0, numAlumn):
        nomAlumn=input("Introduce el nombre del alumno: ")
        sigue = True
        notas= []
        while sigue:
            nota = int(input("Introduce la nota: "))
            if nota > 0:
                notas.append(nota)
            else:
                sigue = False
        dicVacio[nomAlumn]=notas
    
    print("\nLista de alumnos y sus notas")
    for nomAlumn, notas in dicVacio.items():
        promedio= sum(notas)/len(notas)if notas else 0
        print(f"{nomAlumn}: Notas = {notas}, Promedio = {promedio:.2f}")





def menu():
    while True:
        print("MENU DE OPCIONES")
        print("a)Diccionario numerico")
        print("b)Cadena a diccionario.")
        print("c)Diccionario de fruta")
        print("d)Diccionario de alumnos")
        print("e)Salir")

        opcion = input("\nSelecciona una opcion: ").lower()

        if opcion == 'a':
            diccionarioNum()
        elif opcion == 'b':
            diccionarioCadena()
        elif opcion == 'c':
            diccionarioFruta()
        elif opcion == 'd':
            diccionarioAlumnos()   
        elif opcion == 'e':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    menu()