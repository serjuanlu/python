ejercicio = int(input("Elige un ejercicio\nEjercicio 1\nEjercicio 2\nEjercicio 3\nEjercicio 4\nEjercicio 5\nEjercicio 6\nEjercicio 7\nEjercicio 8\nEjercicio 9\nEjercicio 10"))




# 1. Escriba un programa que recoja un valor por teclado y muestre de qué tipo
# es.
match ejercicio:

    case 1:
        valor = input("Introduce un valor por teclado para saber que tipo de dato es ")
        print("Es un tipo de dato "+str(type(valor)))

    
    case 2:
    # 2. Escribe un programa que recoja dos números enteros por teclado y muestre
    # los siguientes resultados: suma, resta, multiplicación, división real, división
    # entera, resto de la división entera y potencia.
    
            x = int(input("Introduce el primer valor: "))
            y = int(input("Introduce el segundo valor: "))

            print(x," + ",y," = "+str(x+y))
            print(x," - ",y," = "+str(x-y))
            print(x," * ",y," = "+str(x*y))
            print(x," / ",y," = "+str(x/y))

   
    case 3:    
    # 3. Escribe un programa que pida el nombre del usuario y le responda con un
    # saludo. En el saludo deberá utilizarse el nombre que introdujo el usuario.
    
        nombre = input("Introduce tu nombre: ")
        print("Hola " + nombre + ", encantado de conocerte!")


    # 4. Escribe un programa que recoja tres números y calcule su media aritmética.
    
    case 4:
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("Introduce el segundo numero: "))
        num3 = float(input("Introduce el tercer numero: "))

        print("Su media aritmetica es: "+str((num1+num2+num3)/3))

    # 5. Escribe un programa que recoja un número y muestre su valor absoluto.
    case 5:
        absol = float(input("Introduce un numero para calcular su valor absoluto: ")) 
        print("El valor absoluto de "+str(absol)+ " es: "+str(abs(absol)))


    # 6. Escribe un programa que recoja las notas de las tres evaluaciones de un
    # alumno. A continuación debe calcular y mostrar la nota final, teniendo en
    # cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
    # evaluación un 35% y la tercera evaluación un 45%.
    case 6:
        nota1 = float(input("Introduce la primer nota: "))
        nota2 = float(input("Introduce la segundo nota: "))
        nota3 = float(input("Introduce la tercer nota: "))

        media = (nota1*0.2)+(nota2*0.35)+(nota3*0.45)

        if media >= 5 :
            print("El alumno esta aprobado, su nota es: "+str(media))
        else:
            print("El alumno esta suspenso, su nota es: "+str(media))
    # 7. Escribe un programa que recoja un número y muestre su representación en
    # código binario.
 
    case 7:
        numBin = bin(int(input("Introduce un numero entero en decimal para pasarlo a binario")))
        print("El numero en binario es ",numBin)
    # 8.Escribe un programa que recoja un texto y lo muestre cinco veces
    # consecutivas en la misma línea.
    case 8:
        texto = input("Escribe un texto: ")
        for i in range(5):
            print(texto,end =" ")
    # 9. Escribe un programa que recoja un texto y que muestre su longitud,
    case 9:
        contarTexto = input("Introduce un texto para contar sus caracteres")
        print("El texto introducido tiene ",len(contarTexto)," caracteres")
    #10. Escribe un programa que recoja la edad del usuario y muestre la edad que
    # tendrá dentro de 5, 10 y 15 años. 
    