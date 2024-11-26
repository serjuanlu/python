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

# Creamos 3 personas
pers1 = Persona("Miguel Angel", "Altocino 13", "123456789")
pers2 = Persona("Juana Isabel", "Pio 12", "333444555")
pers3 = Persona("Alexa", "Amazon 24", "666999111")


diccionario = {
    pers1.nombre:pers1,
    pers2.nombre:pers2,
    pers3.nombre:pers3,
    "Doc":Persona("Doc","Avenida de Peru, 1", "696969111"),
    "Cor":Persona("Cor","Avenida de Peru, 12", "555444555"),
    "Daruuk":Persona("Daruuk","En medio del bosque", "999777999"),
}


# Funcion para imprimir el menu
def menu():
    print("MENÚ DE OPCIONES")
    print("a) Listado de teléfonos por orden alfabético.")
    print("b) Añadir un nuevo contacto.")
    print("c) Modificar un contacto.")
    print("d) Buscar un número de teléfono.")
    print("e) Eliminar un contacto.")
    print("f) Salir")
# Funcion para leer una opcion
def leerOpcion():
    opcion = input("\nElige una opcion: ")
    return opcion.upper()



# Listado de contactos por orden alfabético. Se muestra el contenido ordenado
# por orden alfabético de los contactos, con el siguiente formato:
# Nombre: xxx Dirección: xxx Teléfono: xxx
def listarAgendaOrdenado():
    print("Agenda en orden alfabetico: ")
    for nombre, persona in sorted(diccionario.items()):
        print(f"Nombre: {nombre} Direccion: {persona.direccion} Telefono: {persona.telefono}")


def aniadirContacto():
    nombre = input("Introduce el nombre del contacto: ")
    direccion = input("Introduce la direccion: ")
    telefono = input("Ahora el numero de telefono: ")

    if nombre in diccionario:
        print(f"El contacto {nombre} ya existe.")
        actualizar=input("Quieres actualizarlo? \n (S/N)")

        





# Funcion menu
def ejecutarOpcion(opcion):
    seguir = True

    match opcion:
        case "A":
            listarAgendaOrdenado()
        case "B":
            aniadirContacto()
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