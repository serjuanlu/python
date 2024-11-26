
# Declaracion del diccionario
dicTelefonos= {
    "ANA": "555123456",
    "CARLOS": "555234567",
    "BEA": "555345678",
    "DAVID": "555456789",
    "ELENA": "555567890",
    "FRANCISCO": "555678901",
    "GABRIELA": "555789012",
    "HECTOR": "555890123",
    "ISA": "555901234",
    "JAVI": "555012345",
}

# Funcion que devuelve el contacto, toma un nombre y lo devuelve
def existeContacto(nombre):
    return nombre.strip().upper() in dicTelefonos

# Funcion que actualiza el diccionario, toma los datos de un contacto y le cambia el nombre
def actualizarDiccionario(nombre, telefono):
    dicTelefonos[nombre.strip().upper()]=telefono

# Funcion para borrar un contacto por nombre
def borrarContacto(nombre):
    dicTelefonos.pop(nombre.strip().upper(), None)

# Funcion para imprimir el contacto por nombre
def imprimirContacto(nombre):
    if nombre in dicTelefonos:
        print("{}-{}".format(nombre, dicTelefonos[nombre]))

# Funcion para imprimir el listado
def mostrarListado(ordenado = False):
    # Creamos una lista con los nombres
    nombres = list(dicTelefonos.keys())
    if ordenado:
        nombres.sort()
    print("\nDiccionario con los numeros en orden de introduccion")
    print("==LISTADO POR DEFECTO==")
    # Y los imprimimos
    for n in nombres:
        imprimirContacto(n)        
    print("==FIN DEL LISTADO==")

# Funcion que introduce un contacto
def nuevoContacto():
    nombre = input("Nombre: ")
    numero = input("Numero: ")

    if not existeContacto(nombre):
        actualizarDiccionario(nombre, numero)
    else:
        if(input("El contacto {} ya existe\nQuieres modificarlo? (S/N)\n".format(nombre)).upper())=="S":
            actualizarDiccionario(nombre,numero)
            print("Contacto modificado:")
            imprimirContacto(nombre)

# Funcion para modificar el contacto
def modificarContacto():
    nombre = input("Nombre: ")
    existe=True
    actualizar=True
    if not existeContacto(nombre):
        existe=False
        actualizar = (input("El contacto {} no existe. ¿Desea añadirlo(S/N)?: ".format(nombre)).upper() == "S")

    if actualizar:
        numero = input("Numero: ")
        actualizarDiccionario(nombre, numero)

        if existe:
            print("Contacto Modificado")
            imprimirContacto(nombre)
        else:
            print("Contacto añadido")
            imprimirContacto(nombre)


# Funcion para buscar por telefono
def buscarTelefono():
    num = input("Introduce el numero a buscar: ")
    existe = False
    for n in dicTelefonos.items():
        if n[1]==num:
            print("El numero {} es del contacto {}.".format(num, n[0]))
            existe = True
            break
    if not existe:
        print("El telefono {} no se ha encontrado".format(num))

# Funcion para eliminar un contacto
def eliminarContacto():
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if not existeContacto(nombre):
        print("El contacto {} no existe".format(nombre))
    else:
        if input("El contacto {} va a ser borrado.\n Quieres continuar?\n (S/N)".format(nombre)).upper=="S":
            borrarContacto(nombre)
            print("Contacto eliminado")

# Funcion para borrar el listin
def borrarDiccionario():
    if input("ATENCION!\n Se van a borrar todos los numeros\nQuieres continuar?\n(S/N)").upper() == "S":
        dicTelefonos.clear()

# El menu
def menu():
    while True:
        print("MENU DE OPCIONES")
        print("a) Listado de teléfonos, usando el orden por defecto.")
        print("b) Listado de teléfonos por orden alfabético.")
        print("c) Añadir un nuevo contacto.")
        print("d) Modificar el teléfono de un contacto.")
        print("e) Buscar un número de teléfono.")
        print("f) Eliminar un contacto.")
        print("g) Borrar el listín telefónico.")
        print("h)Salir")

        #Para que se pueda introducir mayusculas y minusculas
        opcion = input("\nSelecciona una opcion: ").lower()

        if opcion == 'a':
            mostrarListado()
        elif opcion == 'b':
            mostrarListado(ordenado = True)        
        elif opcion == 'c':
            nuevoContacto()
        elif opcion == 'd':
            modificarContacto()        
        elif opcion == 'e':
            buscarTelefono()
        elif opcion == 'f':
            eliminarContacto()
        elif opcion == 'g':
            borrarDiccionario()
        elif opcion == 'h':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    menu()