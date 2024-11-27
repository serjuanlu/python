class Habitacion:
    def __init__(self, tipo, precio_base):
        self.tipo = tipo
        self.precio_base = precio_base

    def calcular_precio(self, noches):
        return self.precio_base * noches


class Individual(Habitacion):
    def __init__(self):
        super().__init__("Individual", 50)


class Doble(Habitacion):
    def __init__(self):
        super().__init__("Doble", 75)

    def calcular_precio(self, noches, desayuno=False):
        total = super().calcular_precio(noches)
        if desayuno:
            total += 10 * noches
        return total


class Suite(Habitacion):
    def __init__(self):
        super().__init__("Suite", 150)

    def calcular_precio(self, noches):
        total = super().calcular_precio(noches)
        if noches > 3:
            total *= 0.9
        return total


# Reservas
habitaciones = [
    Individual(),
    Doble(),
    Suite()
]

reservas = [
    (habitaciones[0], 2),  # Individual, 2 noches
    (habitaciones[1], 3, True),  # Doble, 3 noches, desayuno
    (habitaciones[2], 5)  # Suite, 5 noches
]

for reserva in reservas:
    habitacion = reserva[0]
    noches = reserva[1]
    if isinstance(habitacion, Doble) and len(reserva) == 3:
        print(f"{habitacion.tipo}: {habitacion.calcular_precio(noches, desayuno=reserva[2])}€")
    else:
        print(f"{habitacion.tipo}: {habitacion.calcular_precio(noches)}€")
