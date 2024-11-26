
# Declaracion del diccionario
dicTelefonos= {
    "ANA": "555-123-4567",
    "CARLOS": "555-234-5678",
    "BEA": "555-345-6789",
    "DAVID": "555-456-7890",
    "ELENA": "555-567-8901",
    "FRANCISCO": "555-678-9012",
    "GABRIELA": "555-789-0123",
    "HECTOR": "555-890-1234",
    "ISA": "555-901-2345",
    "JAVI": "555-012-3456",
}

# Funcion que imprime el diccionario
def mostrarDefecto():
    print("\nDiccionario con los numeros en orden de introduccion")
    print("LISTADO POR DEFECTO")
    for nombre,numero in dicTelefonos:
        print(f"Nombre: {nombre}____Telefono: {numero}")

# Funcion que ordena el diccionario y lo muestra
def mostrarAlfabetico():
    # dicOrdenado=dict(sorted(dicTelefonos.items(), key=lambda item:item[0]))
    dicOrdenado=dicTelefonos.sort()
    print("LISTADO ORDENADO")
    for nombre, numero in dicOrdenado:
        print(f"Nombre: {nombre}____Telefono: {numero}")

# Funcion para añadir el nuevo contacto
def aniadirContacto():
    nombre=input("Introduce el nombre del contacto")
    nombre=nombre.upper()
    num = input("Introduce el numero del contacto")
    if nombre in dicTelefonos.keys():
        print("El contacto ya esta guardado")
    else:
        dicTelefonos[nombre]=num



# Funcion para cambiar el numero
def cambiarNum():
    nombre=input("Introduce el nombre del contacto: \n")
    nombre=nombre.upper()
    if nombre in dicTelefonos:
        print(f"{dicTelefonos[nombre]} es el numero a cambiar")
        num=input("Introduce el nuevo numero \n")
        dicTelefonos[nombre]=num
        print(f"{dicTelefonos[nombre]} es nuevo numero")

# Funcion para buscar un numero de telefono
def buscarNum():
    num=input("Introduce el numero a buscar \n")
    if num in dicTelefonos.values():
        for key, numero in dicTelefonos:
            if 


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
            mostrarDefecto()
        elif opcion == 'b':
            mostrarAlfabetico()        
        elif opcion == 'c':
            cambiarNum()
        elif opcion == 'd':
            buscarNum()        
        elif opcion == 'e':
            print("\nSaliendo del programa...")
        elif opcion == 'f':
            print("\nSaliendo del programa...")
        elif opcion == 'g':
            print("\nSaliendo del programa...")
        elif opcion == 'h':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    menu()