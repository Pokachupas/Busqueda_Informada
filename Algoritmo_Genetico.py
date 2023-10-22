import random

distances = [
    [0, 2, 3, 5, 2, 4, 6, 1, 7, 8],
    [2, 0, 4, 6, 5, 7, 3, 2, 9, 1],
    [3, 4, 0, 2, 6, 8, 5, 3, 2, 4],
    [5, 6, 2, 0, 7, 9, 4, 6, 3, 2],
    [2, 5, 6, 7, 0, 2, 8, 4, 3, 5],
    [4, 7, 8, 9, 2, 0, 6, 4, 5, 7],
    [6, 3, 5, 4, 8, 6, 0, 3, 7, 1],
    [1, 2, 3, 6, 4, 4, 3, 0, 6, 8],
    [7, 9, 2, 3, 3, 5, 7, 6, 0, 2],
    [8, 1, 4, 2, 5, 7, 1, 8, 2, 0]
]

# Número de ciudades
num_cities = len(distances)

def initialize_population(num_individuals):
    # Inicializar una población de rutas aleatorias
    population = [random.sample(range(num_cities), num_cities) for _ in range(num_individuals)]
    return population

def calculate_total_distance(route):
    # Calcular la distancia total de una ruta
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]  # Volver a la ciudad de inicio
    return total_distance

def selection(population):
    # Seleccionar individuos basados en su aptitud (distancia total)
    # Puedes usar selección por torneo, ruleta, etc.
    # En este ejemplo, seleccionamos a los mejores individuos
    population.sort(key=calculate_total_distance)
    selected = population[:len(population) // 2]
    return selected

def crossover(parent1, parent2):
    # Aplicar cruce (orden de corte) entre dos padres para producir descendencia
    n = len(parent1)
    cut1, cut2 = random.sample(range(n), 2)
    if cut1 > cut2:
        cut1, cut2 = cut2, cut1
    child = [None] * n
    for i in range(cut1, cut2 + 1):
        child[i] = parent1[i]
    remaining = [gene for gene in parent2 if gene not in child]
    j = 0
    for i in range(n):
        if child[i] is None:
            child[i] = remaining[j]
            j += 1
    return child

def mutation(individual, mutation_rate):
    # Aplicar mutación intercambiando dos genes aleatorios con una cierta probabilidad
    if random.random() < mutation_rate:
        i, j = random.sample(range(num_cities), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm(num_generations, population_size, mutation_rate):
    population = initialize_population(population_size)
    for generation in range(num_generations):
        population = selection(population)
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population

    best_route = min(population, key=calculate_total_distance)
    best_distance = calculate_total_distance(best_route)
    return best_route, best_distance

# Uso del algoritmo genético
num_generations = 100
population_size = 100
mutation_rate = 0.02
best_route, best_distance = genetic_algorithm(num_generations, population_size, mutation_rate)

print("Mejor ruta encontrada:", best_route)
print("Distancia total de la mejor ruta:", best_distance)


