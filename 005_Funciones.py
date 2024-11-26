ejercicio = input("Menu de opciones\n"
"a) Mostrar un rombo.\n"       
"b) Adivinar un número.\n"
"c) Resolver una ecuación de segundo grado.\n"
"d) Tabla de números.\n"
"e) Cálculo del número factorial de un número.\n"
"f) Cálculo de un número de la sucesión de Fibonacci.\n"
"g) Tabla de multiplicar.\n"
"h) Salir\n")


while ejercicio!="h":
    match ejercicio:
        case 'a':
            numero = int(input("a)Introduce un numero impar: "))
            while numero % 2 == 0:
                numero = int(input("Por favor, escriba un número impar: "))
            altura = (numero+1)//2

            for i in range(1, altura+1):
                espacios=altura-i
                asteriscos = 2*i-1
                linea=" "*espacios+"*"*asteriscos
                print(linea)
            for i in range(altura, 0,-1):
                asteriscos=altura-i
                espacios = 2*i-1
                linea=" "*espacios+"*"*asteriscos
                print(linea)
        case 'b':
            print("b)Adivinar un numero")
        case 'c':
            print("c)Resolver una ecuación de segundo grado.")
            
        case 'd':
             print("d)Tabla de números.")
           
        case'e':
            print("e)Cálculo del número factorial de un número.")

        case 'f':
            print("f)Cálculo de un número de la sucesión de Fibonacci.")

        case 'g':
            print("g)Tabla de multiplicar.")

        case _:
            print("Por favor introduce una opcion valida")
    ejercicio = input("Menu de opciones\n"
"a) Mostrar un rombo.\n"       
"b) Adivinar un número.\n"
"c) Resolver una ecuación de segundo grado.\n"
"d) Tabla de números.\n"
"e) Cálculo del número factorial de un número.\n"
"f) Cálculo de un número de la sucesión de Fibonacci.\n"
"g) Tabla de multiplicar.\n"
"h) Salir\n")