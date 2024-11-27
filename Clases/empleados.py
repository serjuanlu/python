from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    @abstractmethod
    def calcular_salario(self):
        pass


class Asalariado(Empleado):
    def __init__(self, nombre, id, salario_fijo):
        super().__init__(nombre, id)
        self.salario_fijo = salario_fijo

    def calcular_salario(self):
        return self.salario_fijo


class PorHora(Empleado):
    def __init__(self, nombre, id, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, id)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = min(horas_trabajadas, 160)

    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas


class Comisionista(Empleado):
    def __init__(self, nombre, id, salario_base, ventas, porcentaje_comision):
        super().__init__(nombre, id)
        self.salario_base = salario_base
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.porcentaje_comision / 100)


empleados = [
    Asalariado("Ana", 1, 1500),
    PorHora("Luis", 2, 15, 170),
    Comisionista("Carlos", 3, 1000, 5000, 10)
]

for empleado in empleados:
    print(f"{empleado.nombre} (ID: {empleado.id}) - Salario: {empleado.calcular_salario()}€")
