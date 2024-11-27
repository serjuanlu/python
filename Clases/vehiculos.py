class Vehiculo:
    def __init__(self, modelo, año):
        self.modelo = modelo
        self.año = año

    def calcular_consumo(self, kilometros):
        pass


class Coche(Vehiculo):
    def calcular_consumo(self, kilometros):
        return kilometros * 5 / 100


class Camion(Vehiculo):
    def __init__(self, modelo, año, carga_toneladas):
        super().__init__(modelo, año)
        self.carga_toneladas = carga_toneladas

    def calcular_consumo(self, kilometros):
        consumo_base = kilometros * 20 / 100
        consumo_extra = consumo_base * 0.1 * self.carga_toneladas
        return consumo_base + consumo_extra


class Moto(Vehiculo):
    def calcular_consumo(self, kilometros):
        return kilometros * 3 / 100


vehiculos = [
    Coche("Toyota", 2020),
    Camion("Volvo", 2019, 10),
    Moto("Yamaha", 2022)
]

for vehiculo in vehiculos:
    print(f"{vehiculo.modelo}: {vehiculo.calcular_consumo(200)} litros para 200 km")
