'''
Ejercicio 1: Gestion de productos
'''

# Creamos la clase producto
class Producto:
    def __init__(self, nombre, precio, descuento):
        self.__nombre =  nombre
        self.__precio =  precio
        self.__descuento =  descuento

    @property #Getter
    def nombre(self):
            return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
                self.__nombre = nombre.upper()
        else:
            raise ValueError("El nombre no puede estar vacio")

    @property #Precio
    def precio(self):
            return self.__precio
    @precio.setter
    def precio(self, precio):
        if precio>0:
            self.__precio = precio
        else:
            raise ValueError("El precio no puede ser negativo")
        
    @property #descuento
    def descuento(self):
            return self.__descuento
    @descuento.setter
    def descuento(self, descuento):
        if descuento>0:
            self.__descuento = descuento
        else:
            raise ValueError("El descuento no puede ser negativo")
        
    def mostrarProducto(self):
        print("Producto: ")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Descuento: {self.descuento}%")

    def calcularPrecioFinal(self):
        return self.precio-((self.precio*self.descuento)/100)
     
class Electronicos(Producto):
    def __init__(self, nombre, precio, descuento):
        if descuento <= 10:
            super().__init__(nombre, precio, descuento)
        else:
            raise ValueError("El descuento no puede ser superior al 10%")
        
    @Producto.descuento.setter  # Sobrescribimos el setter de descuento
    def descuento(self, descuento):
        if 0 <= descuento <= 10:  # Restricción específica: descuento no mayor a 20%
            self._Producto__descuento = descuento
        else:
            raise ValueError("El descuento para ropa no puede ser superior al 10%.")

class Ropa(Producto):
    def __init__(self, nombre, precio, descuento):
        if descuento <= 20:
            super().__init__(nombre, precio, descuento)
        else: 
            raise ValueError("El descuento no puede ser superior al 20%")
        
    @Producto.descuento.setter  # Sobrescribimos el setter de descuento
    def descuento(self, descuento):
        if 0 <= descuento <= 20:  # Restricción específica: descuento no mayor a 20%
            self._Producto__descuento = descuento
        else:
            raise ValueError("El descuento para ropa no puede ser superior al 20%.")

class Comida(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio, descuento=0)
    @Producto.descuento.setter
    def descuento(self, descuento):
        raise ValueError("No se puede asignar un descuento a un producto de comida.")