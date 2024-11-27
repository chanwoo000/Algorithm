import math

def find(node):
    if root[node] != node:
        root[node] = find(root[node])  
    return root[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            root[root2] = root1
        elif rank[root1] < rank[root2]:
            root[root1] = root2
        else:
            root[root2] = root1
            rank[root1] += 1

def kruskal(n, edges):
    global root, rank
    root = list(range(n))
    rank = [0] * n
    mst_cost = 0

    edges.sort()

    for cost, u, v in edges:
        if find(u) != find(v):  
            union(u, v)
            mst_cost += cost

    return mst_cost

def solution(n):
    stars = []
    edges = []

    for _ in range(n):
        x, y = map(float, input().split())
        stars.append((x, y))

    for i in range(n):
        for j in range(i + 1, n):
            distance = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
            edges.append((distance, i, j))

    mst_cost = kruskal(n, edges)
    print(mst_cost)

if __name__ == '__main__':
    n = int(input())
    solution(n)
