import heapq

# Heap is effective implementation of priority queue

data=[10,20,43,1,2,65,17,44,2,1]
heapq.heapify(data)
print(data)
print(heapq.heappop(data))
print(data)