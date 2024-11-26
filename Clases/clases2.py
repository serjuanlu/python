'''
Ejercicio de clases 2


Autor: Juan Luis Serrano Vilchez
'''

# Definicion de la clase persona
class Persona:
    # Creamos un valor por defecto, que va a ser privado
    __valorDefecto=None

    # Declaramos el constructor usando los valores por defecto.
    def __init__(self, nombre=__valorDefecto, apellidos=__valorDefecto, dni=__valorDefecto, edad=__valorDefecto):
        self.__nombre=nombre.upper()
        self.__apellidos=apellidos.upper()
        self.__dni=dni.upper()
        self.__edad=edad

    #Declaramos los getters y los setters
    @property #Getter
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):

        if nombre.strip():
            self.__nombre = nombre.upper()
        else:
            raise ValueError("El nombre no puede estar vacio")
    @property
    def apellidos(self):
        return self.__apellidos
   
    @apellidos.setter
    def apellidos(self, apellidos):
        if len(apellidos) != 0:
            self.__apellidos = apellidos.upper()
        else:
            raise ValueError("El apellido no puede estar vacio")
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        if dni != "":
            self.__dni = dni.upper()
        else:
            raise ValueError("El dni no puede estar vacio")
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if edad>=0:
            self.__edad=edad
        else:
            raise ValueError("La edad no puede ser negativa")
    
    # Metodo mostrar
    def mostrar(self):
        print(f"Nombre: {self.nombre}")    
        print(f"Apellidos: {self.apellidos}")    
        print(f"Dni: {self.dni}")    
        print(f"Edad: {self.edad}") 

    # Metodo que muestra si es mayor o menor de edad
    def esMayor(self):
        esMayor="Es menor de edad"
        if self.edad>=18:
            esMayor="Es mayor de edad"
        return esMayor 
    
# Definicion de la clase cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    # Getters
    @property
    def titular(self):
        return self.__titular
    @property
    def cantidad(self):
        return self.__cantidad
    
    #!AQUI PUEDE FALTAR UN SET TITULAR!!!

    # Metodos ingresar y retirar
    def ingresar(self, cantidadIngreso):
        if cantidadIngreso>0:
            self.__cantidad+=cantidadIngreso
        else:
            raise ValueError("La cantidad a ingresar no puede ser negativa")
    def retirar(self, cantidadRetirada):
        if cantidadRetirada>0:
            self.__cantidad-=cantidadRetirada
        else:
            raise ValueError("La cantidad a retirar no puede ser negativa")
        
    # Metodo para mostrar
    def mostrar(self):
        print("Info de la cuenta")
        print(f"Titular {self.titular.nombre} {self.titular.apellidos}")
        print(f"Saldo: {self.cantidad}")

# Definicion de la clase CuentaJoven
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100:
            self.__bonificacion=bonificacion
        else:
            raise ValueError("La bonificacion no puede ser negativa")
    def mostrar(self):
        # Accedemos al codigo anterior
        super().mostrar()
        print(f"Bonificacion: {self.bonificacion}%")

# 4. Crea un programa que haga uso de las tres clases para crear una cuenta normal
# y una cuenta joven

# Crear una persona mayor
persona1 = Persona("Manolo", "Galvez", "12345678A", 56)
persona2 = Persona("Alicia", "Ramirez", "87654321B", 30)
# Crear dos personas jovenes
persona3 = Persona("Esteban", "Rondo", "56789012C", 23)
persona4 = Persona("Maria", "Fernandez", "98765432C", 28)

# Crear una cuenta normal
cuenta_normal = Cuenta(persona1, 5000.0)
cuenta_normal.ingresar(500.0)
cuenta_normal.retirar(200.0)

cuenta_normal_2 = Cuenta(persona2, 1500.0)
cuenta_normal_2.ingresar(200.0)
cuenta_normal_2.retirar(100.0)

# Crear una cuenta joven
cuenta_joven1 = CuentaJoven(persona3, 1500.0, 12)
cuenta_joven1.ingresar(300.0)
cuenta_joven1.retirar(100.0)

cuenta_joven2 = CuentaJoven(persona4, 2000.0, 8)
cuenta_joven2.ingresar(500.0)
cuenta_joven2.retirar(200.0)

# Mostrar información
print("\nCUENTA NORMAL:")
persona1.nombre="juanda"
print(persona1.nombre)
persona1.mostrar()
cuenta_normal.mostrar()
persona2.mostrar()
cuenta_normal_2.mostrar()


print("\nCUENTA JOVEN:")
persona3.mostrar()
cuenta_joven1.mostrar()
persona4.mostrar()
cuenta_joven2.mostrar()
