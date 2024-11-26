# Ejercicios de clases
# 
# Autor: Juan Luis Serrano Vilchez

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
pers1 = Persona("MIGUEL ANGEL", "Altocino 13", "123456789")
pers2 = Persona("JUANA ISABEL", "Pio 12", "333444555")
pers3 = Persona("ALEXA", "Amazon 24", "666999111")


diccionario = {
    pers1.nombre:pers1,
    pers2.nombre:pers2,
    pers3.nombre:pers3,
    "DOC":Persona("DOC","Avenida de Peru, 1", "696969111"),
    "COR":Persona("COR","Avenida de Peru, 12", "555444555"),
    "DARUUK":Persona("DARUUK","En medio del bosque", "999777999"),
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



# A) Listado de contactos por orden alfabético. Se muestra el contenido ordenado
# por orden alfabético de los contactos, con el siguiente formato:
# Nombre: xxx Dirección: xxx Teléfono: xxx
def listarAgendaOrdenado():
    print("Agenda en orden alfabetico: ")
    # Esto se va a transformar en una lista ordenada
    for nombre, persona in sorted(diccionario.items()):
        print(f"Nombre: {nombre} Direccion: {persona.direccion} Telefono: {persona.telefono}")

# B) Funcion para aniadir un contacto, se va a llamar a esta desde B) y C)

def modificarDatos(nombre, direccion, telefono):
    nombre = nombre.upper()
    diccionario[nombre]=Persona(nombre, direccion, telefono)
    print(f"{diccionario[nombre].nombre} ha sido añadido con telefono {diccionario[nombre].telefono} y direccion {diccionario[nombre].direccion}")

# Añadir un nuevo contacto. Se debe leer por teclado un nombre de contacto,
# dirección y número de teléfono. Se añade en el diccionario. Si ya existe, se informa
# que ya existe y pregunta si se quiere actualizar su teléfono. Si se responde
# afirmativamente se actualiza.
def aniadirContacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in diccionario:
        print(f"El contacto {nombre} ya existe.")
        actualizar = input("Quieres actualizarlo? \n (S/N)")
        while seguir==True:
            match actualizar.upper():
                case "S":
                    # Pedimos el resto de datos
                    telefono = input("Ahora el numero de telefono: ")
                    # Y lo introducimos
                    modificarDatos(nombre, diccionario[nombre].direccion, telefono)
                    seguir = False
                case "N":
                    print("De acuerdo, hasta luego!")
                    seguir = False
                case _:
                    actualizar = input("Elige una opcion valida (S/N)")
    else:
        direccion = input("Ahora la direccion: ")
        telefono = input("Por ultimo el numero de telefono: ")
        modificarDatos(nombre,direccion,telefono)


# C) Modificar un contacto. Se pide un nombre de contacto. Si no existe, se pregunta
# si se desea insertar. Si se responde afirmativamente (o el contacto ya existía), se
# pide la dirección y el número de teléfono, y se actualiza el diccionario.
def modificarContacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre not in diccionario:
        if(input(f"Deseas insertar el contacto {nombre}? \n (S/N)\n").upper=="S"):
            direccion = input("Introduce la direccion: ")
            telefono = input("Ahora el numero de telefono: ")
            modificarDatos(nombre, direccion, telefono)
        else:
            print("Hasta luego!")
    else:
        print("El contacto existe, vamos a modificarlo")
        direccion = input("Introduce la direccion: ")
        telefono = input("Ahora el numero de telefono: ")
        modificarDatos(nombre, direccion, telefono)
# D) Buscar un número de teléfono. Se pide un número de teléfono de contacto y se
# busca en el diccionario. Si se encuentra, se indica el nombre del contacto, en otro
# caso se indica que no se encuentra.
def buscarTelefono():
    encontrado=False
    telefonoBuscado=input("Introduce el numero de telefono a buscar: ")
    for nombre, persona in diccionario.items():
        if persona.telefono == telefonoBuscado:
            print(f"Nombre: {nombre} Telefono: {persona.telefono}")
            encontrado = True
            return
    if encontrado==False:
        print("El numero de telefono no esta en la agenda.")
        
# D) Eliminar un contacto. Se pide un nombre de contacto. Si no existe, se indica que
# no se encuentra, si existe se debe eliminar del diccionario.
def eliminarContacto():
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        if nombre in diccionario:
            print(f"Nombre: {diccionario[nombre].nombre} Direccion: {diccionario[nombre].direccion} Telefono: {diccionario[nombre].telefono}")
            selector=input("Estas seguro de que quieres borrar este contacto? (S/N)").upper
            if selector == "S":
                del diccionario[nombre]
            else:
                print("Se va a cancelar la accion")
        else:
            print(f"El contacto {nombre} no esta en la agenda")

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
            buscarTelefono()
        case "E":
            eliminarContacto()
        case "F":
            seguir = False
        case _:
            print("Opción errónea")

    # Sólo se va a poner la espera de teclado si no hay que finalizar hay que darle enter
    if seguir:
        x = input("\nPulse una tecla para continuar...")

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