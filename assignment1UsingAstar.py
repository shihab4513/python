import csv
import queue
import math

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def create_graph(distances, coordinates):
    graph = {}
    for row in distances:
        source, destination, distance = row
        if source not in graph:
            graph[source] = {}
        graph[source][destination] = int(distance)
    return graph

def create_coordinates_dict(coordinates):
    coordinates_dict = {}
    for row in coordinates:
        star, x, y, z = row
        coordinates_dict[star] = (int(x), int(y), int(z))
    return coordinates_dict

def heuristic(vertex, goal, coordinates_dict):
    x1, y1, z1 = coordinates_dict[vertex]
    x2, y2, z2 = coordinates_dict[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def a_star(graph, start, end, coordinates_dict):
    pq = queue.PriorityQueue()
    pq.put((0, start))
    costs = {node: float('infinity') for node in graph}
    costs[start] = 0
    path = {}

    while not pq.empty():
        current_cost, current_vertex = pq.get()

        if current_vertex == end:
            break

        for adjacent, weight in graph[current_vertex].items():
            new_cost = costs[current_vertex] + weight
            if new_cost < costs.get(adjacent, float('infinity')):
                costs[adjacent] = new_cost
                priority = new_cost + heuristic(adjacent, end, coordinates_dict)
                pq.put((priority, adjacent))
                path[adjacent] = current_vertex

    if end not in path:
        return float('infinity'), ''

    # Reconstruct path from end to start
    path_output = end
    path_sequence = [end]
    while path_output != start:
        path_output = path[path_output]
        path_sequence.append(path_output)
    path_sequence.reverse()

    # Convert path sequence to string
    path_string = ' -> '.join(path_sequence)

    return costs[end], path_string

# Read data from CSV files
distances = read_csv_file('distances.csv')
coordinates = read_csv_file('Coordinates.csv')

# Create graph and coordinates dictionary
graph = create_graph(distances, coordinates)
coordinates_dict = create_coordinates_dict(coordinates)

# Apply A* algorithm using PriorityQueue
start = 'Sun'
end = '61 Virginis'
print(a_star(graph, start, end, coordinates_dict))
