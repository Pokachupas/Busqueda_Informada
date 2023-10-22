from queue import PriorityQueue

# Definición del grafo con 10 ciudades y distancias
grafo = {
    'Nueva York': {'Los Ángeles': 2444, 'Chicago': 789, 'Miami': 1288},
    'Los Ángeles': {'Nueva York': 2444, 'Chicago': 1745, 'San Francisco': 348},
    'Chicago': {'Nueva York': 789, 'Los Ángeles': 1745, 'Houston': 1085},
    'Miami': {'Nueva York': 1288, 'Houston': 1187},
    'San Francisco': {'Los Ángeles': 348},
    'Houston': {'Chicago': 1085, 'Miami': 1187},
}

# Función de búsqueda voraz
def best_first_search(grafo, inicio, destino):
    # Creamos una cola de prioridad para manejar la exploración de las ciudades.
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, [inicio]))  # Iniciamos desde la ciudad de inicio con un costo de 0 y una lista de camino.
    visitados = set()  # Utilizamos un conjunto para llevar un registro de las ciudades visitadas.

    while not cola_prioridad.empty():
        costo, camino = cola_prioridad.get()  # Obtenemos el costo y el camino actual.

        ciudad_actual = camino[-1]  # Obtenemos la ciudad actual desde el camino.

        if ciudad_actual == destino:  # Si hemos llegado al destino, hemos encontrado la ruta.
            print("Ruta encontrada:", costo)
            print("Camino:", " -> ".join(camino))
            break

        if ciudad_actual in visitados:  # Si la ciudad actual ya ha sido visitada, la ignoramos.
            continue

        visitados.add(ciudad_actual)  # Marcamos la ciudad actual como visitada.

        # Exploramos los vecinos (ciudades conectadas) de la ciudad actual.
        for vecino, distancia in grafo[ciudad_actual].items():
            if vecino not in visitados:  # Solo consideramos ciudades no visitadas.
                nuevo_costo = costo + distancia
                nuevo_camino = camino + [vecino]  # Agregamos el vecino al camino.
                cola_prioridad.put((nuevo_costo, nuevo_camino))  # Agregamos el vecino a la cola con el costo actualizado.

# Ejemplo de uso: buscamos la ruta desde "Nueva York" a "Los Ángeles".
best_first_search(grafo, 'Nueva York', 'Houston')