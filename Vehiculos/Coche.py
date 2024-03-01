from Vehiculos.Vehiculo import Vehiculo
from Decoradores.Turbo import turbo

class Coche(Vehiculo):
    def __init__(self, velocidad_maxima, capacidad_tanque):
        super().__init__(velocidad_maxima, capacidad_tanque)

    @turbo
    def acelerar(self, velocidad):
        super().acelerar(velocidad)

    def desactivar_turbo(self):
        self.velocidad_maxima -= 20
