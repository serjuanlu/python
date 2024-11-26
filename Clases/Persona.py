# 1. Crea una clase Persona para guardar nombre, dirección y teléfono de una
# persona.


class Persona:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre.upper()
        self.direccion = direccion
        self.telefono = telefono

    def mostrar(self):
        return self.nombre, self.direccion, self.telefono


# 2. Crea un programa que utilice la clase Persona para almacenar un diccionario de
# contactos. El diccionario será un conjunto de datos donde la clave de cada entrada
# es el nombre de la persona (en mayúsculas) y el valor es un objeto de la clase
# Persona que guarda el nombre, dirección y teléfono.
# El programa mostrará el siguiente menú de opciones:
# MENÚ DE OPCIONES
# a) Listado de contactos por orden alfabético.
# b) Añadir un nuevo contacto.
# c) Modificar un contacto.
# d) Buscar un número de teléfono.
# e) Eliminar un contacto.
# f) Salir
# Si se ha indicado una opción correcta, se ejecuta según estas instrucciones que
# se indican a continuación. Una vez finalizada la opción se espera a que se pulse
# una tecla para continuar.

"""
Creo el diccionario con algunos ejemplos
"""

Pers1 = Persona("JOSELE", "juan del cano n3", 623567845)
print (" estoy mostrando ")
Pers1.mostrar
Pers2 = Persona("MIRIAM", "jose arevalo n28", 657894321)

agenda = {
    "JOSELE": Pers1,
    "MIRIAM": Pers2,
    "ALBERTO": Persona("ALBERTO", "plaza ayuntamiento n13", 952245674),
    "JUANITO": Persona("JUANITO", "torroles n45", 1234),
}


def menu():
    print("MENÚ DE OPCIONES")
    print("a) Listado de teléfonos por orden alfabético.")
    print("b) Añadir un nuevo contacto.")
    print("c) Modificar un contacto.")
    print("d) Buscar un número de teléfono.")
    print("e) Eliminar un contacto.")
    print("f) Salir")


def leerOpcion():
    opcion = input("\nIntroduzca la opción que desea realizar: ").upper()
    return opcion


def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debes introducir un valor numérico entero. Intenta de nuevo.")


def listarAgendaOrdenado():
    if len(agenda) == 0:
        print("La agenda está vacía")
    else:
        print("Listado de contactos por orden alfabético:")
        for nombre, persona in sorted(agenda.items()):
            print(
                f"Nombre: {nombre} Dirección: {persona.direccion} Teléfono: {persona.telefono}"
            )


def incluirContacto():
    nombre = input("Dime el Nombre de la persona que quieres añadir: ").upper()
    direccion = input("Ahora dime la dirección: ")
    telefono = input("Ahora dime el número de teléfono: ")

    if nombre in agenda:
        print("El contacto ya existe")
        eleccion = input("¿Desea actualizarlo? s/n").upper()

        if eleccion == "S":
            persona = agenda[nombre]  #accede al objeto persona guardado en el valor de la clave nombre
            #persona.telefono=11111  ¿se puede actualizar así?
            print(" el elefono es ",persona.telefono)
            setattr(persona, "direccion", direccion)
            setattr(persona, "telefono", telefono)
            print("Contacto actualizado correctamente")
        else:
            print("Contacto no actualizado")
    else:
        nueva_persona = Persona(nombre, direccion, telefono)
        agenda[nombre] = nueva_persona
        print("Contacto añadido correctamente")


def buscarContacto():
    telefono = obtener_numero("Número de teléfono de la persona a buscar: ")
    nombre_encontrado = None

    for nombre, persona in agenda.items():
        if persona.telefono == telefono:
            nombre_encontrado = nombre

    if nombre_encontrado is not None:
        print("La persona con ese número es:", nombre_encontrado)
    else:
        print("Número de teléfono no encontrado en la Agenda")


def modificarContacto():
    nombre = input("Dime el nombre que deseas modificar: ").upper()

    if nombre in agenda:
        print("Nombre encontrado")

        eleccion = input("¿Desea actualizar la dirección y el teléfono? s/n").upper()

        if eleccion == "S":
            direccion = input("Dime la nueva dirección: ")
            telefono = input("Dime el nuevo teléfono: ")

            persona = agenda[nombre]
            setattr(persona, "direccion", direccion)
            setattr(persona, "telefono", telefono)

            # Tambien se pude hacer de esta forma:
            # agenda[nombre].direccion = direccion
            # agenda[nombre].telefono = telefono

            print("Información actualizada correctamente")
        else:
            print("Información no actualizada")
    else:
        respuesta = input(
            "Este nombre no está en la agenda, ¿Quieres incluirlo? s/n"
        ).upper()

        if respuesta == "S":
            incluirContacto()
        else:
            print("Operación cancelada")


def elminarContacto():
    nombre = input("Dime el nombre que deseas eliminar: ").upper()
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado correctamente de tu agenda")
    else:
        print("El contacto no existe en tu agenda")


# Las opciones del programa son:
# Listado de contactos por orden alfabético. Se muestra el contenido ordenado
# por orden alfabético de los contactos, con el siguiente formato:
# Nombre: xxx Dirección: xxx Teléfono: xxx
# Añadir un nuevo contacto. Se debe leer por teclado un nombre de contacto,
# dirección y número de teléfono. Se añade en el diccionario. Si ya existe, se informa
# que ya existe y pregunta si se quiere actualizar su teléfono. Si se responde
# afirmativamente se actualiza.
# Modificar un contacto. Se pide un nombre de contacto. Si no existe, se pregunta
# si se desea insertar. Si se responde afirmativamente (o el contacto ya existía), se
# pide la dirección y el número de teléfono, y se actualiza el diccionario.
# Buscar un número de teléfono. Se pide un número de teléfono de contacto y se
# busca en el diccionario. Si se encuentra, se indica el nombre del contacto, en otro
# caso se indica que no se encuentra.
# Eliminar un contacto. Se pide un nombre de contacto. Si no existe, se indica que
# no se encuentra, si existe se debe eliminar del diccionario.
# Salir. Mientras el usuario no seleccione esta opción, tras finalizar cada opción
# debe mostrar de nuevo el menú de opciones. Con esta opción el programa finaliza.


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


