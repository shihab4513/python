import csv
import queue

def csv_file_reader(fileNAme):
    with open(fileNAme, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def createGraph(distances):
    graph={}

    for row in distances:
        (source,dest,distance)=row
        if source not in graph:
            graph[source]={}
        graph[source][dest]=int(distance)
    return graph

def dijakstra(start,end,graph):
    pq=queue.PriorityQueue()

    distances={node:float('infinity') for node in graph}
    pq.put((0, start))
    distances[start]=0
    path={}
    while pq.empty():
        (currnt_distance,current_vertice)=pq.get()
        if(distances[current_vertice])


if __name__ == "__main__":
    distances = csv_file_reader('distances.csv')

graph=createGraph(distances)
