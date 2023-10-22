# Definición del grafo con ciudades y distancias
grafo = {
    'Nueva York': {'Los Ángeles': 2444, 'Chicago': 789, 'Miami': 1288},
    'Los Ángeles': {'Nueva York': 2444, 'Chicago': 1745, 'San Francisco': 348},
    'Chicago': {'Nueva York': 789, 'Los Ángeles': 1745, 'Houston': 1085},
    'Miami': {'Nueva York': 1288, 'Houston': 1187},
    'San Francisco': {'Los Ángeles': 348},
    'Houston': {'Chicago': 1085, 'Miami': 1187},
}

# Función de búsqueda tabú
def tabu_search(grafo, inicio, destino, max_iteraciones=100):
    solucion_actual = [inicio]  # Comenzamos desde la ciudad de inicio.
    distancia_actual = 0
    mejor_solucion = None
    mejor_distancia = float('inf')
    lista_tabu = []

    for _ in range(max_iteraciones):
        vecinos = grafo[solucion_actual[-1]]  # Obtenemos los vecinos de la última ciudad en la solución actual.
        mejor_vecino = None
        menor_distancia = float('inf')

        # Buscamos el vecino más cercano que no esté en la lista tabú.
        for vecino, distancia in vecinos.items():
            if vecino not in solucion_actual and (vecino, solucion_actual[-1]) not in lista_tabu:
                if distancia < menor_distancia:
                    mejor_vecino = vecino
                    menor_distancia = distancia

        if mejor_vecino is None:
            # No se encontraron vecinos disponibles, terminamos la búsqueda.
            break

        # Actualizamos la solución actual, la distancia y la lista tabú.
        solucion_actual.append(mejor_vecino)
        distancia_actual += menor_distancia
        lista_tabu.append((mejor_vecino, solucion_actual[-2]))

        # Si hemos llegado al destino, actualizamos la mejor solución encontrada.
        if mejor_vecino == destino:
            if distancia_actual < mejor_distancia:
                mejor_solucion = solucion_actual.copy()
                mejor_distancia = distancia_actual

    if mejor_solucion:
        print("Mejor Ruta encontrada:", mejor_distancia)
        print("Mejor Camino:", " -> ".join(mejor_solucion))
    else:
        print("No se pudo encontrar una ruta al destino.")

# Ejemplo de uso: buscamos la ruta desde "Nueva York" a "Los Ángeles".
tabu_search(grafo, 'Nueva York', 'Houston')