import heapq
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

def dijkstra(start, city):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        cur_cost, cur_node = heapq.heappop(priority_queue)

        if cur_cost > distance[cur_node]:
            continue

        for next_node, weight in city[cur_node]:
            cost = cur_cost + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(priority_queue, (cost, next_node))

    return distance

N, M, X = map(int, input().split())
city = [[] for i in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    city[a].append([b, t])

distance_from_X = dijkstra(X, city)

ans = [0] * (N+1)

for i in range(1, N+1):
    if i != X:
        distance_from_i = dijkstra(i, city)
        ans[i] = distance_from_X[i] + distance_from_i[X]

print(max(ans))
