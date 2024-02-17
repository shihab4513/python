import csv
import queue
import math


def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        # it will skip header
        next(reader)
        return list(reader)


def create_graph(distances):
    graph = {}
    for row in distances:
        (source, destination, distance) = row
        if source not in graph:
            graph[source] = {}
        graph[source][destination] = int(distance)
    return graph


def create_coordinates_dictionary(coordinates):
    coordinates_dict = {}
    for row in coordinates:
        (star, x, y, z) = row
        coordinates_dict[star] = (int(x), int(y), int(z))
    return coordinates_dict


# huristic
def heuristic(vertex, goal, coordinates_dictionary):
    x1, y1, z1 = coordinates_dictionary[vertex]
    x2, y2, z2 = coordinates_dictionary[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def a_star(graph, start, end, coordinates_dictionary):
    pq = queue.PriorityQueue()
    pq.put((0, start))
    # it will initialize
    costs = {node: float('infinity') for node in graph}
    costs[start] = 0
    path = {}

    while not pq.empty():
        current_cost, current_vertex = pq.get()

        if current_vertex == end:
            break

        for adjacent, weight in graph[current_vertex].items():
            new_cost = costs[current_vertex] + weight
            if adjacent not in costs or new_cost < costs[adjacent]:
                costs[adjacent] = new_cost
                priority = new_cost + heuristic(adjacent, end, coordinates_dictionary)
                pq.put((priority, adjacent))
                path[adjacent] = current_vertex

    if end not in path:
        return [0, 'Cant reach there']

    # Reconstructing path
    path_output = end
    path_sequence = [end]
    while path_output != start:
        path_output = path[path_output]
        path_sequence.append(path_output)
    path_sequence.reverse()

    # Convert path sequence to string
    path_string = ' -> '.join(path_sequence)

    return [costs[end], path_string]


if __name__ == "__main__":
    # Read csv file
    distances = read_csv_file('distances.csv')
    coordinates = read_csv_file('Coordinates.csv')

    # Create graph and coordinates dictionary
    graph = create_graph(distances)
    coordinates_dictionary = create_coordinates_dictionary(coordinates)

    # Apply A* algorithm
    start = 'Sun'
    end = 'Upsilon Andromedae'

    result = a_star(graph, start, end, coordinates_dictionary)
    print("Total cost: " + str(result[0]) + "\n")
    print("Path: " + result[1] + "\n")

