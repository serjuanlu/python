ejercicio = int(input("Elige un ejercicio\nEjercicio 1\nEjercicio 2\nEjercicio 3\nEjercicio 4\nEjercicio 5\nEjercicio 6\nEjercicio 7\nEjercicio 8\nEjercicio 9\nEjercicio 10\n"))

#1. Escribe un programa que recoja un texto y escriba cada letra del texto en una
#línea distinta.
match ejercicio:
    case 1:

        linea = input("Escribe un texto\n")

        for char in linea:
             print(char)
             
    #2. Escribe un programa que recoja un número y calcule su factorial.
    case 2:
        num = int(input("Escribe un numero para calcular su factorial\n"))
        fact = 1

        for i in range(1,num+1):
            fact *= i
        print("El factorial de ",num," es ",fact)
    
    case 3:
        num = int(input("Escribe un numero "))
        numMay=num
        numMin=num
        acum=0
        cont=0
        while num!=0:
            acum+=num
            cont+=1
            if(num>numMay):
                numMay=num

            if(num<numMin):
                numMin=num

            num = int(input("Escribe un numero ")) 
        
        media = acum/cont
        print(
            "El programa se ha cerrado con ",
            cont, 
            "numeros introducidos.",
            "\nSu suma es ", acum,
            "\nEl minimo ha sido",numMin,
            "\nEl maximo ha sido ",numMay,
            "\nSu media ha sido", media
        )

    #4. Escribe un programa que recoja números por teclado hasta que se introduzca
    # el valor cero. A continuación, debe mostrar el número de valores introducidos,
    # el valor mínimo introducido, el máximo, la suma de todos ellos y su media
    # aritmética (todos los cálculos sin contar el cero)
    case 4:
        altura = int(input("Escribe la altura de la piramide\n"))
        for i in range(1, altura+1):
            
            for j in range(1, i):
                print("*", end="")
        
            print("")
    case 5: 
        num = int(input("Escribe un numero para calcular los cuadrados hasta llegar a el\n"))
        fact = 1

        for i in range(1,num+1):
            print(i," x ",i," = ",i*i)
    case 6:
        filas = int(input("Introduce el numero de filas\n"))
        columnas = int(input("Introduce el numero de columnas\n"))
        cont = 1
        for i in range(1, filas+1):
            for j in range(1, columnas+1):
                print(cont, end="      ")
                cont+=1
            print("\n")

    case 7:
        cadena=input("Escribe una cadena\n")
        letra=input("Escribe una letra a contar\n")
        cont =0
        for n in cadena:
            if(n==letra):
                cont+=1
        print(f"En la cadena \"{cadena}\", la letra '{letra}' aparece {cont} veces")

    case 8:
        num=int(input("Escribe un numero para saber si es primo\n"))
        flag = False
        if num>1:
            for i in range(2, num):
                if (num%i)==0:
                    flag=True
                    break
        
        if flag:
            print(f"El numero ",num," no es primo")
        else:
            print(f"El numero ",num," es primo")
    case 9:
        num = int(input("Introduce un numero impar: "))
        while((num%2)==0):
            num = int(input("Error: Introduce un numero impar: "))
        altura = (num+1)//2

        for i in range(1, altura+1):
           spaces = altura - i
           asteriscos = 2 * i - 1
           linea = " " * spaces + "*" * asteriscos
           print(linea)
    case 10:
        num = int(input("Introduce un numero para generar una piramide: "))
        impar = 1

        for i in range(num):
            impares = ""
            for j in range(impar, 0, -2):
                impares+=str(j)+" "
            print(impares+" ")
            impar +=2

        
