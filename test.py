import csv
import heapq


def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def create_graph(distances, coordinates):
    graph = {}
    for row in distances:
        source, destination, distance = row

        if source not in graph:
            graph[source] = {}
        graph[source][destination] = int(distance)

    return graph


def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    path = {}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
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

    return distances[end], path_string


# Read data from CSV files
distances = read_csv_file('distances.csv')
coordinates = read_csv_file('Coordinates.csv')

# Create graph
graph = create_graph(distances, coordinates)

# Apply Dijkstra's algorithm
start = 'Sun'
end = '61 Virginis'
print(dijkstra(graph, start, end))
