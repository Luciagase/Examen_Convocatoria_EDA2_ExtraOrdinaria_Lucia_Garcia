class Planet:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = {}
        self.min_distance = float("inf")
        self.previous = None

    def add_neighbor(self, planet, distance):
        self.neighbors.append(planet)
        self.distance[planet] = distance

def prim(graph, start_planet):
    included_planets = set()
    tree_edges = []
    included_planets.add(start_planet)
    while len(included_planets) < len(graph):
        min_edge_weight = float("inf")
        min_edge = None
        for planet in included_planets:
            for neighbor in planet.neighbors:
                if neighbor not in included_planets:
                    if planet.distance[neighbor] < min_edge_weight:
                        min_edge_weight = planet.distance[neighbor]
                        min_edge = (planet, neighbor)
        included_planets.add(min_edge[1])
        tree_edges.append(min_edge)
    return tree_edges

def dijkstra(graph, start_planet, end_planet):
    for planet in graph:
        planet.min_distance = float("inf")
    start_planet.min_distance = 0
    unvisited_planets = list(graph)
    while unvisited_planets:
        current_planet = min(unvisited_planets, key=lambda x: x.min_distance)
        if current_planet == end_planet:
            break
        unvisited_planets.remove(current_planet)
        for neighbor in current_planet.neighbors:
            if neighbor in unvisited_planets:
                distance = current_planet.distance[neighbor]
                if current_planet.min_distance + distance < neighbor.min_distance:
                    neighbor.min_distance = current_planet.min_distance + distance
                    neighbor.previous = current_planet
    path = []
    planet = end_planet
    while planet:
        path.append(planet)
        planet = planet.previous
    path.reverse()
    return path

def bfs(graph, start_planet):
    visited_planets = set()
    queue = [start_planet]
    visited_planets.add(start_planet)
    while queue:
        current_planet = queue.pop(0)
        for neighbor in current_planet.neighbors:
            if neighbor not in visited_planets:
                visited_planets.add(neighbor)
                queue.append(neighbor)
    return visited_planets

#Planetas
Tierra = Planet("Tierra")
Knowhere = Planet("Knowhere")
ZenWhoberi = Planet("Zen-Whoberi")
Vormir = Planet("Vormir")
Titan = Planet("Titan")
Nidavellir = Planet("Nidavellir")
planet1 = Planet("planet1")
planet2 = Planet("planet2")
planet3 = Planet("planet3")
planet4 = Planet("planet4")
planet5 = Planet("planet5")
planet6 = Planet("planet6")
planet7 = Planet("planet7")