import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    indegree[v] += 1

queue = deque()
for node in range(1, N+1):
    if indegree[node] == 0:
        queue.append(node)

result = []

while queue:
    node = queue.popleft()
    result.append(node)
    
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
print(*result)
