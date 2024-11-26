"""
Escribe un programa que recoja un número por teclado y muestre el día de la
semana que es (1 = Lunes, 2 = Martes…). En caso de introducir un número
incorrecto, mostrará el mensaje “Día de la semana incorrecto.
"""

        
        
while True:
 try:
   numero = int(input("Escriba un número del 1 al 7: "))

   match numero:
    case 1:
        print("Lunes.")
    case 2:
        print("Martes.")
    case 3:
        print("Miércoles.")
    case 4:
        print("Jueves.")
    case 5:
        print("Viernes.")
    case 6:
        print("Sábado.")
    case 7:
        print("Domingo.")
    case _:
        print("Ese día no existe.")
 
 except ValueError:
            print("Error: Debes introducir un valor numérico entero.")
