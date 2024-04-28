import random
import math
import matplotlib.pyplot as plt

# Assuming g_data is your dataset
g_data = [
    [2.5, 2.4],
    [1.5, 2.3],
    [3.3, 2.9],
    [2.8, 2.5],
    [3.5, 3.0],
    [2.0, 1.7],
    [1.6, 1.8],
    [2.2, 2.0],
    [3.4, 3.2],
    [2.9, 2.7]
]
Data=g_data

def distance(a, b):
    return math.sqrt(sum([(a[i]-b[i])**2 for i in range(len(a))]))

def average(cluster):
    return [sum(x)/len(x) for x in zip(*cluster)]

def closest_center(S, Centers):
    distances = [distance(S, C) for C in Centers]
    return distances.index(min(distances))

def k_means(K, Data):
    Centers = random.sample(Data, K)
    Clusters = [[] for _ in range(K)]
    for S in Data:
        i = closest_center(S, Centers)
        Clusters[i].append(S)
    itr = 1
    Shift = 0
    while True:
        for i, L in enumerate(Clusters):
            Centers[i] = average(L)
        if itr > 1 and Shift < 50:
            break
        Shift = 0
        Temp_Clusters = [[] for _ in range(K)]
        for S in Data:
            i = closest_center(S, Centers)
            Temp_Clusters[i].append(S)
            if S not in Clusters[i]:
                Shift += 1
        Clusters = Temp_Clusters
        itr += 1
    return Clusters, Centers

def plot_clusters(Clusters, Centers):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, cluster in enumerate(Clusters):
        for point in cluster:
            plt.scatter(*point, c=colors[i%len(colors)])
        plt.scatter(*Centers[i], c='k', marker='x')
    plt.show()

def inertia(Clusters, Centers):
    total = 0
    for i, cluster in enumerate(Clusters):
        total += sum([distance(point, Centers[i])**2 for point in cluster])
    return total

for K in [2, 4, 6, 7]:
    Clusters, Centers = k_means(K, Data)
    plot_clusters(Clusters, Centers)
    print(f'Inertia for K={K}: {inertia(Clusters, Centers)}')
