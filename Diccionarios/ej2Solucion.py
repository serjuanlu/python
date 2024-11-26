
# Se crea el diccionario de teléfonos (inicialmente vacío)
listin = {"PACO":"123"}

# Se guardan las claves en mayúsculas para no complicar el ejercicio
def existeContacto(contacto) : return contacto.strip().upper() in listin
def actualizarListin(contacto, telefono): listin[contacto.strip().upper()] = telefono
def borrarContacto(contacto) : listin.pop(contacto.strip().upper(), None)

def imprimirContacto(contacto):
    if contacto in listin:
        print("{} - {}".format(contacto, listin[contacto]))

def listado(ordenado = False):
    contactos = list(listin.keys())
    if ordenado: 
        contactos.sort()

    print("== Listado de teléfonos ==")
    for c in contactos:
        imprimirContacto(c)
    print("== Fin del listado ==")
    
def nuevoContacto():
    contacto = input("Nombre: ")
    telefono = input("Teléfono: ")

    if not existeContacto(contacto):
        actualizarListin(contacto, telefono)
        print("Contacto añadido")
    else:
        if (input("El contacto '{}' ya existe. ¿Desea modificarlo (S/N)?: ".format(contacto)).upper()) == "S":
            actualizarListin(contacto, telefono)
            print("Contacto modificado")

def modificarContacto():
    contacto = input("Nombre: ")
    contactoExiste = True # Imagino que el listín se va a actualizar
    actualizar = True 
    if not existeContacto(contacto):
        contactoExiste = False
        actualizar = (input("El contacto {} no existe. ¿Desea añadirlo(S/N)?: ".format(contacto)).upper() == "S")

    if actualizar:
        telefono = input("Teléfono: ")
        actualizarListin(contacto, telefono)

        if contactoExiste:
            print("Contacto modificado")
        else:
            print("Contacto añadido")

def buscarTelefono():
    tlf = input("Indique el teléfono que desea buscar: ")
    encontrado = False
    for c in listin.items():
        if c[1] == tlf:
            print("El teléfono {} pertenece a '{}'.".format(tlf, c[0]))
            encontrado = True
            break
    
    if not encontrado:
        print("El teléfono no se encuentra.")
    
def eliminarContacto():
    contacto = input("Indique el contacto que desea eliminar: ")
    if not existeContacto(contacto):
        print("El contacto '{}' no se encuentra en el listín.".format(contacto))
    else:
        if input("El contacto '{}' va a ser borrado. ¿Desea continuar (S/N)?: ".format(contacto)).upper() == "S":
            borrarContacto(contacto)
            print("Contacto eliminado.")

def borrarListin():
    if input("¡ADVERTENCIA! Se perderán todos los teléfonos. ¿Desea continuar (S/N)?: ").upper() == "S":
        listin.clear()
        print("Listín borrado.")

def menu():
    print("MENÚ DE OPCIONES")
    print("a) Listado de teléfonos, usando el orden por defecto.")
    print("b) Listado de teléfonos por orden alfabético.")
    print("c) Añadir un nuevo contacto.")
    print("d) Modificar el teléfono de un contacto.")
    print("e) Buscar un número de teléfono.")
    print("f) Eliminar un contacto.")
    print("g) Borrar el listín telefónico.")
    print("h) Salir")

def leerOpcion():
    opcion = input("Introduzca la opción que desea realizar: ").upper()
    return opcion

def ejecutarOpcion(opcion):
    seguir = True

    match opcion:
        case "A":
            listado()
        case "B":
            listado(ordenado = True)
        case "C":
            nuevoContacto()
        case "D":
            modificarContacto()
        case "E":
            buscarTelefono()
        case "F":
            eliminarContacto()
        case "G":
            borrarListin()
        case "H":
            seguir = False
        case _:
            print("Opción errónea")
    
    x = input("Pulse una tecla para continuar...")
    return seguir

seguir = True
while seguir:
    menu()
    seguir = ejecutarOpcion(leerOpcion())
else:
    print("Que pases un buen día")
