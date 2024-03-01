class Vehiculo:
    def __init__(self, velocidad_maxima, capacidad_tanque):
        self.velocidad_maxima = velocidad_maxima
        self.capacidad_tanque = capacidad_tanque
        self.velocidad_actual = 0
        self.distancia_recorrida = 0

    def acelerar(self, velocidad):
        if self.velocidad_actual + velocidad <= self.velocidad_maxima:
            self.velocidad_actual += velocidad
        else:
            self.velocidad_actual = self.velocidad_maxima

    def frenar(self, velocidad):
        if self.velocidad_actual - velocidad >= 0:
            self.velocidad_actual -= velocidad
        else:
            self.velocidad_actual = 0

    def recorrer(self):
        self.distancia_recorrida += self.velocidad_actual

    def __str__(self):
        return f"Vehículo: Velocidad actual - {self.velocidad_actual}, Distancia recorrida - {self.distancia_recorrida}"
