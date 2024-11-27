'''NOMBRE Y APELLIDOS: Juan Luis Serrano Vilchez
Fecha:27/11/202
Desarrolla un programa en Python que gestione un sistema de biblioteca.No hace falta que comentes cada cosa que realices pero sí lo que consideres debería saber otro compañero tuyo, para cuando te vayas de vacaciones y tu compañero debe manipular tu código. Este programa debe cumplir los siguientes requisitos:
'''

'''
1.Define una clase base Material que tenga atributos comunes a todos los materiales de la biblioteca, como:
id (único para cada material)
título
autor
año de publicación 
'''
# definimos la lista de ids
listaId = []
# y el diccionario vacio
almacen = {}

class Material:
    def __init__(self, id, titulo, autor, anyoPub):
        if id not in listaId:
            self.id=id
            self.titulo=titulo
            self.autor=autor
            self.anyoPub=anyoPub
            #Lo guardamos en el almacen y la lista
            almacen[self.id]=self
            listaId.append(id)
        else:
            raise ValueError(f"El id {id} ya esta registrado")

    def mostrar(self):
        print("Material")
        print(f"ID: {self.id}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicacion: {self.anyoPub}")
    
'''
2.Crea dos clases que hereden de Material:

Libro: Incluye atributos adicionales como género (debe seleccionarse entre una lista predefinida: "Ficción", "No Ficción", "Terror", "Ciencia") y número de páginas (debe ser mayor a 0).
'''

# Lista de generos
generos = ["FICCION", "NO FICCION", "TERROR", "CIENCIA"]

class Libro(Material):
    def __init__(self, id, titulo, autor, anyoPub, genero, paginas):
        if genero.upper() not in generos:
            raise ValueError(f"El genero tiene que estar en la lista de generos {generos}")
        if paginas<=0:
            raise ValueError("Las paginas no pueden ser inferiores a 1")
        else:
            super().__init__(id, titulo, autor, anyoPub)
            self.genero=genero.upper()
            self.paginas=paginas          
    def mostrar(self):
        super().mostrar()
        print(f"Genero {self.genero}")
        print(f"Paginas {self.paginas}")
'''
Revista: Incluye atributos adicionales como número de edición y mes de publicación (debe seleccionarse entre los meses válidos: "Enero", "Febrero", ..., "Diciembre")
'''
meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO","JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
class Revista(Material):
    def __init__(self, id, titulo, autor, anyoPub, mesPub, numEd):
        if mesPub.upper() in meses:
            super().__init__(id, titulo, autor, anyoPub)
            self.mesPub=mesPub.upper()
            self.numEd=numEd
        else:
            raise ValueError("El mes introducido no es valido")
    def mostrar(self):
        super().mostrar()
        print(f"Mes de publicacion: {self.mesPub}")
        print(f"Numero de edicion: {self.numEd}")

'''
3.Utiliza un diccionario para almacenar los materiales, donde la clave sea el id y el valor sea un objeto de tipo Libro o Revista.
'''
almacen={1:Revista(1, "NYT", "Jeff Bezos",2020, "Enero", 1), 2:Libro(2, "Mistborn", "Brandon Sanderson", 2012, "CIENCIA", 750)}
'''
4.Mantén una lista de todos los id existentes para verificar que no se repitan al agregar nuevos materiales.
'''


'''
5. Generar Estadísticas:debe devolver todos estos valores
Total de materiales registrados.
Número de libros y revistas.
Promedio de páginas para los libros.
Ayuda: se puede usar la siguiente función: Ej: isinstance(m, Libro)--> devuelve true si el objeto m es de tipo Libro
'''
def generarEstadisticas():
    #Creamos los acumuladores y los inicializamos a 0
    totalMat=0
    totaLibros=0
    acumPag=0
    totalRev=0
    # Recorremos el almacen
    for clave, material in almacen.items():
        # Por cada material sumamos
        totalMat+=1
        # Si es un libro, sumamos libros y su numero de paginas
        if isinstance(material, Libro):
            totaLibros+=1
            acumPag+=almacen[clave].paginas
        # Si es una revista, solo el elemento
        if isinstance(material, Revista):
            totalRev+=1
    # Vamos a imprimir
    print(f"Estadisticas: ")
    print(f"Total de Materiales: {totalMat}")
    print(f"Total de libros: {totaLibros} - Media de paginas: {acumPag/totaLibros}")
    print(f"Total de Revistas: {totalRev}")


'''
6.Implementa un menú que permita al usuario realizar las siguientes acciones:
'''

'''
----------------------
OPCIONES DEL MENU
----------------------
'''
'''
1. Agregar Material: Permite al usuario agregar un nuevo Libro o Revista.
'''
def agregarMaterial():
    try:
        while True:
            libroRevista=input("Elige el tipo de material\n1.Libro\n2.Revista\n")
            if libroRevista=="1":
                    print("Vamos a crear un libro: ")
                    idLibro=input("Introduce el id del libro: ")
                    titulo=input("Introduce el titulo del libro: ")
                    autor=input("Introduce el autor del libro: ")
                    anyoPub=input("Introduce el año de publicacion: ")
                    genero=input("Introduce el genero del libro: ")
                    paginas=int(input("Introduce las paginas del libro: "))
                    libroCreado=Libro(idLibro,titulo,autor,anyoPub,genero,paginas)
                    libroCreado.mostrar()
                    break
            elif libroRevista=="2":
                    print("Vamos a crear una revista")
                    idRev=input("Introduce el id de la revista: ")
                    titulo=input("Introduce el titulo de la revista: ")
                    autor=input("Introduce el autor de la revista: ")
                    anyoPub=input("Introduce el año de publicacion: ")
                    mesPub=input("Introduce el mes de publicacion: ")
                    numEd=input("Introduce el num de publicacion: ")
                    revistaCreada=Revista(idRev, titulo, autor, anyoPub, mesPub, numEd)
                    revistaCreada.mostrar()
                    break
            else:
                    print("Por favor, introduce una opcion valida")
    except Exception as ex:
        print(ex)
            
'''
2.Listar Materiales: Muestra una lista de todos los materiales registrados con sus detalles. Elije la forma de presentación más adecuada para que el usuario lo vea claro.
'''
def listarMateriales():
    mostrados=list(almacen.values())
    for n in mostrados:
        if isinstance(n, Material):
            n.mostrar()
    
'''
3. Buscar Material por ID: Permite al usuario buscar un material específico por su id.
'''
def buscarMaterial():
    idBuscada = int(input("Introduce el id a buscar: "))
    if idBuscada in almacen.keys():
        almacen[idBuscada].mostrar()
    else:
        print("La id no existe")
'''
4.Eliminar Material: Elimina un material específico usando su id.
Generar Estadísticas
'''
def eliminarMaterial():
    idEliminar=int(input("Introduce el id del material a eliminar: "))
    if idEliminar in almacen.keys():
        almacen[idEliminar].mostrar()
        confirmar=input("Seguro que quieres eliminar este material? (S/N)")
        while True:
            match confirmar.upper():
                case 'S':
                    del(almacen[idEliminar])
                    del(listaId[idEliminar])
                    print("Ha sido eliminado")
                    break
                case 'N':
                    print("Cancelando...")
                    break
                case _:
                    print("Por favor, elige una opcion valida")
                
'''
Salir: Termina la ejecución del programa.'''
# Menú principal
def menu():
    while True:
        try:
            print("\nMENÚ DE EJERCICIOS")
            print("1. Agregar material")
            print("2. Listar materiales")
            print("3. Buscar por id un material")
            print("4. Eliminar un material")
            print("5. Generar estadisticas")
            print("0. Salir")


            opcion = input("Selecciona una opción: ")
            if opcion == '1':
                agregarMaterial()
            elif opcion == '2':
                listarMateriales()
            elif opcion == '3':
                buscarMaterial()
            elif opcion == '4':
                eliminarMaterial()
            elif opcion == '5':
                generarEstadisticas()
            elif opcion == '0':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intenta nuevamente.")
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    menu()