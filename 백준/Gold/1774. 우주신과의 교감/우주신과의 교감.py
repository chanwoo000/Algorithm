import sys
import math
input = sys.stdin.readline

def find(node):
    if root[node] != node:
        root[node] = find(root[node])  
    return root[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if root1 < root2:
            root[root2] = root1
        else:
            root[root1] = root2

num_nodes, num_edges = map(int, input().split())
coordinates = []
edges = []

root = list(range(num_nodes + 1))

for _ in range(num_nodes):
    x, y = map(int, input().split())
    coordinates.append((x, y))

for _ in range(num_edges):
    u, v = map(int, input().split())
    union(u, v)

for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if find(i + 1) != find(j + 1):  
            distance = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 +
                                 (coordinates[i][1] - coordinates[j][1])**2)
            edges.append((distance, i + 1, j + 1))

edges.sort()

mst_cost = 0
for cost, u, v in edges:
    if find(u) != find(v):  
        union(u, v)
        mst_cost += cost

print(f"{mst_cost:.2f}")
