import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

pq = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)

result = []

while pq:
    current = heapq.heappop(pq)
    result.append(current)
    
    for neighbor in graph[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(pq, neighbor)

print(" ".join(map(str, result)))
