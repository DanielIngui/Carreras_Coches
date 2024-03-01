from Vehiculos.Vehiculo import Vehiculo
from Decoradores.Carga import carga

class Camion(Vehiculo):
    def __init__(self, velocidad_maxima, capacidad_tanque):
        super().__init__(velocidad_maxima, capacidad_tanque)

    @carga
    def acelerar(self, velocidad):
        super().acelerar(velocidad)
