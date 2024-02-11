import csv


def csv_file_reader(fileNAme):
    with open(fileNAme, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def createGraph(distances):
    graph={}

    for row in distances:
        (source,dest,distance)=row
        if source not in graph:
            graph[source]={
                dest:int(distance)
            }

if __name__ == "__main__":
    distances = csv_file_reader('distances.csv')

graph=createGraph(distances)
