"""
Escribe un programa que recoja un año e indique si se trata de un año bisiesto
o no. 
"""
anno = int(input("Escriba un anno: "))

if (anno % 4 == 0 and anno % 100 != 0) or  anno % 400 == 0:
    
    print("Es bisiesto.")    
    
else:
    print("No es bisiesto.")
