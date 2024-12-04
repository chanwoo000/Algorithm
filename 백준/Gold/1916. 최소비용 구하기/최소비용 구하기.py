import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[]for i in range(n+1)]
distance = [1e9] * (n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start , end = map(int,input().split())


def dijkstra(start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0

    while priority_queue:
        cur_cost, cur_node = heapq.heappop(priority_queue)

        if cur_cost > distance[cur_node]:
            continue

        for next_node, weight in graph[cur_node]:
            cost = cur_cost + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(priority_queue, (cost, next_node))


dijkstra(start)
print(distance[end])
