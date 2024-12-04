import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INFINITY = int(1e9)

V, E = map(int, input().split())

K = int(input())

adjacency_list = [[] for _ in range(V + 1)]
min_distances = [INFINITY] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    adjacency_list[u].append((v, w))

def find_shortest_paths(start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    min_distances[start] = 0

    while priority_queue:
        cur_distance, cur_node = heapq.heappop(priority_queue)

        if cur_distance > min_distances[cur_node]:
            continue

        for neighbor, weight in adjacency_list[cur_node]:
            total_distance = cur_distance + weight
            if total_distance < min_distances[neighbor]:
                min_distances[neighbor] = total_distance
                heapq.heappush(priority_queue, (total_distance, neighbor))

find_shortest_paths(K)

for node in range(1, V + 1):
    if min_distances[node] != INFINITY:
        print(min_distances[node])
    else:
        print("INF")
