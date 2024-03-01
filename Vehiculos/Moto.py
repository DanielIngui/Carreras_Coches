from Vehiculos.Vehiculo import Vehiculo
from Decoradores.Acrobacia import acrobacia

class Moto(Vehiculo):
    def __init__(self, velocidad_maxima, capacidad_tanque):
        super().__init__(velocidad_maxima, capacidad_tanque)

    @acrobacia
    def acelerar(self, velocidad):
        super().acelerar(velocidad)
