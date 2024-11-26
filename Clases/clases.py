#
#

# 1. Creacion de clase persona
class Persona:
    # Constructor
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    # Return
    def mostrar(self):
        return self.nombre, self.direccion

# 2. Crea un programa que utilice la clase Persona para almacenar un diccionario de
# contactos. El diccionario será un conjunto de datos donde la clave de cada entrada
# es el nombre de la persona (en mayúsculas) y el valor es un objeto de la clase
# Persona que guarda el nombre, dirección y teléfono.
diccionario = {}


# Listado de contactos por orden alfabético. Se muestra el contenido ordenado
# por orden alfabético de los contactos, con el siguiente formato:
# Nombre: xxx Dirección: xxx Teléfono: xxx

# Funcion menu
def ejecutarOpcion(opcion):
    seguir = True

    match opcion:
        case "A":
            listarAgendaOrdenado()
        case "B":
            incluirContacto()
        case "C":
            modificarContacto()
        case "D":
            buscarContacto()
        case "E":
            elminarContacto()
        case "F":
            seguir = False
        case _:
            print("Opción errónea")

    # Sólo se va a poner la espera de teclado si no hay que finalizar hay que darle enter
    if seguir:
        x = input("\n\nPulse una tecla para continuar... enter por favor.")

    return seguir


""" 
Comienzo del menu de la clase persona.
"""
seguir = True
while seguir:
    menu()
    seguir = ejecutarOpcion(leerOpcion())
else:
    print("Adios, Fin del Programa")