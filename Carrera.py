import time
import random
from Vehiculos.Coche import Coche
from Vehiculos.Moto import Moto
from Vehiculos.Camion import Camion
from Decoradores.Turbo import turbo
from Decoradores.Acrobacia import acrobacia
from Decoradores.Carga import carga

# Función para simular la carrera
def simular_carrera(vehiculos):
    distancia_carrera = 1000
    tiempo_inicial = time.time()

    while True:
        for vehiculo in vehiculos:
            vehiculo.acelerar(random.randint(1, 20))
            vehiculo.recorrer()

            if vehiculo.distancia_recorrida >= distancia_carrera:
                tiempo_final = time.time()
                tiempo_carrera = tiempo_final - tiempo_inicial
                print(f"{type(vehiculo).__name__} ha ganado la carrera en {tiempo_carrera:.2f} segundos!")
                return

if __name__ == "__main__":
    coche = Coche(200, 50)
    moto = Moto(180, 30)
    camion = Camion(150, 100)

    # Iniciar la carrera con los vehículos
    simular_carrera([coche, moto, camion])
