import random

# Definición del grafo con ciudades en México y distancias
grafo = {
    'Ciudad de México': {'Guadalajara': 532, 'Monterrey': 885, 'Puebla': 136},
    'Guadalajara': {'Ciudad de México': 532, 'Monterrey': 669, 'Veracruz': 350},
    'Monterrey': {'Ciudad de México': 885, 'Guadalajara': 669, 'Tijuana': 1882},
    'Puebla': {'Ciudad de México': 136, 'Veracruz': 263},
    'Veracruz': {'Guadalajara': 350, 'Puebla': 263},
    'Tijuana': {'Monterrey': 1882},
}

# Función de búsqueda de haz local
def local_beam_search(grafo, inicio, destino, num_haces=5, max_iteraciones=100):
    haces = [[inicio] for _ in range(num_haces)]  # Iniciamos varios caminos desde la ciudad de inicio.
    distancias = [0] * num_haces
    mejor_camino = None
    mejor_distancia = float('inf')

    for _ in range(max_iteraciones):
        nuevos_haces = []

        for i in range(num_haces):
            camino_actual = haces[i]
            ciudad_actual = camino_actual[-1]
            vecinos = grafo[ciudad_actual]

            for vecino, distancia in vecinos.items():
                nuevo_camino = camino_actual + [vecino]
                nueva_distancia = distancias[i] + distancia

                if vecino == destino:
                    if nueva_distancia < mejor_distancia:
                        mejor_camino = nuevo_camino
                        mejor_distancia = nueva_distancia
                else:
                    nuevos_haces.append((nuevo_camino, nueva_distancia))

        # Filtramos los caminos que llegan al destino
        nuevos_haces = [(camino, distancia) for camino, distancia in nuevos_haces if camino[-1] == destino]

        if nuevos_haces:
            # Ordenamos los nuevos caminos por distancia y seleccionamos los mejores
            nuevos_haces.sort(key=lambda x: x[1])
            haces = [camino for camino, _ in nuevos_haces[:num_haces]]

    if mejor_camino:
        print("Mejor Ruta encontrada:", mejor_distancia)
        print("Mejor Camino:", " -> ".join(mejor_camino))
    else:
        print("No se pudo encontrar una ruta al destino.")

# Ejemplo de uso: buscamos la ruta desde "Ciudad de México" a "Tijuana".
local_beam_search(grafo, 'Ciudad de México', 'Guadalajara')