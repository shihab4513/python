import csv
import queue

def csv_file_reader(fileName):
    with open(fileName, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def createGraph(distances):
    graph = {}
    for row in distances:
        (source, dest, distance) = row
        if source not in graph:
            graph[source] = {}
        graph[source][dest] = int(distance)
    return graph

def dijkstra(start, end, graph):
    pq = queue.PriorityQueue()
    distances = {node: float('infinity') for node in graph}
    pq.put((0, start))
    distances[start] = 0
    path = {}
    while not pq.empty():
        (current_distance, current_vertex) = pq.get()
        if distances[current_vertex] < current_distance:
            continue
        for (adjacent_vertex, weight) in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[adjacent_vertex]:
                distances[adjacent_vertex] = distance
                path[adjacent_vertex] = current_vertex
                pq.put((distance, adjacent_vertex))

    if end not in path:
        return 'No path found'
    path_output = end
    path_sequence = [end]
    while path_output != start:
        path_output = path[path_output]
        path_sequence.append(path_output)
    path_sequence.reverse()

    return '->'.join(path_sequence), distances[end]

if __name__ == "__main__":
    distances = csv_file_reader('distances.csv')
    start = 'Sun'
    end = '61 Virginis'
    graph = createGraph(distances)
    print(dijkstra(start, end, graph))
