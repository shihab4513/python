# dequee 2 dike pop kora jai
# mutable
from collections import deque

q = deque("catataccagcaacataacgtagggttgagaacatactcgtac")
q[1] = "g"
q.appendleft("c")
q.appendleft("g")
q.popleft()
q.pop()
print(q);