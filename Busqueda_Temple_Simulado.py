import random
import math

# Definición del grafo con ciudades en México y distancias
grafo = {
    'Ciudad de México': {'Guadalajara': 532, 'Monterrey': 885, 'Puebla': 136},
    'Guadalajara': {'Ciudad de México': 532, 'Monterrey': 669, 'Veracruz': 350},
    'Monterrey': {'Ciudad de México': 885, 'Guadalajara': 669, 'Tijuana': 1882},
    'Puebla': {'Ciudad de México': 136, 'Veracruz': 263},
    'Veracruz': {'Guadalajara': 350, 'Puebla': 263},
    'Tijuana': {'Monterrey': 1882},
}

# Función de búsqueda de temple simulado
def simulated_annealing(grafo, inicio, destino, temperatura_inicial=1000, enfriamiento=0.98, max_iteraciones=1000):
    solucion_actual = [inicio]  # Comenzamos desde la ciudad de inicio.
    distancia_actual = 0
    mejor_solucion = None
    mejor_distancia = float('inf')
    temperatura = temperatura_inicial

    for _ in range(max_iteraciones):
        vecinos = grafo[solucion_actual[-1]]  # Obtenemos los vecinos de la última ciudad en la solución actual.
        vecino_aleatorio = random.choice(list(vecinos.keys()))

        # Calculamos la diferencia de distancia entre la solución actual y el vecino aleatorio.
        diferencia_distancia = grafo[solucion_actual[-1]][vecino_aleatorio]

        # Aceptamos el vecino si reduce la distancia o con una probabilidad decreciente.
        if diferencia_distancia < 0 or random.random() < math.exp(-diferencia_distancia / temperatura):
            solucion_actual.append(vecino_aleatorio)
            distancia_actual += diferencia_distancia

        # Si hemos llegado al destino, actualizamos la mejor solución encontrada.
        if vecino_aleatorio == destino:
            if distancia_actual < mejor_distancia:
                mejor_solucion = solucion_actual.copy()
                mejor_distancia = distancia_actual

        # Enfriamos la temperatura.
        temperatura *= enfriamiento

    if mejor_solucion:
        print("Mejor Ruta encontrada:", mejor_distancia)
        print("Mejor Camino:", " -> ".join(mejor_solucion))
    else:
        print("No se pudo encontrar una ruta al destino.")

# Ejemplo de uso: buscamos la ruta desde "Ciudad de México" a "Tijuana".
simulated_annealing(grafo, 'Ciudad de México', 'Tijuana')