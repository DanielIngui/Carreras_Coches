import time
import random
from Vehiculos.Coche import Coche
from Vehiculos.Moto import Moto
from Vehiculos.Camion import Camion
from Decoradores.Turbo import turbo
from Decoradores.Acrobacia import acrobacia
from Decoradores.Carga import carga

# Función para simular la carrera con más detalles
def simular_carrera(vehiculos):
    distancia_carrera = 1000
    tiempo_inicial = time.time()
    intervalo_tiempo = 1  # Intervalo de tiempo para mostrar detalles (en segundos)

    while True:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial

        # Mostrar detalles cada intervalo de tiempo
        if tiempo_transcurrido >= intervalo_tiempo:
            print("\n--- Detalles de la carrera ---")
            for vehiculo in vehiculos:
                vehiculo.acelerar(random.randint(1, 20))
                vehiculo.recorrer()

                if vehiculo.distancia_recorrida >= distancia_carrera:
                    print(f"{type(vehiculo).__name__} ha ganado la carrera!")
                    mostrar_detalles_vehiculo(vehiculo)
                    return

                mostrar_detalles_vehiculo(vehiculo)

            tiempo_inicial = time.time()

        # Revisar si algún vehículo se quedó sin combustible
        for vehiculo in vehiculos:
            if vehiculo.capacidad_tanque <= 0:
                print(f"{type(vehiculo).__name__} se quedó sin combustible y debe frenar.")
                vehiculo.velocidad_actual = 0

        # Pausa para simular intervalo de tiempo
        time.sleep(0.5)

def mostrar_detalles_vehiculo(vehiculo):
    print(f"{type(vehiculo).__name__}:")
    print(f" - Distancia recorrida: {vehiculo.distancia_recorrida} km")
    print(f" - Velocidad actual: {vehiculo.velocidad_actual} km/h")
    print(f" - Combustible restante: {vehiculo.capacidad_tanque} litros\n")

if __name__ == "__main__":
    coche = Coche(200, 50)
    moto = Moto(180, 30)
    camion = Camion(150, 100)

    # Aplicar decoradores
    Coche.acelerar = turbo(Coche.acelerar)
    Moto.acelerar = acrobacia(Moto.acelerar)
    Camion.acelerar = carga(Camion.acelerar)

    print("--- Comienza la carrera ---")
    simular_carrera([coche, moto, camion])
