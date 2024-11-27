import sys
import math

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def get_root(node, parent):
    if node != parent[node]:
        parent[node] = get_root(parent[node], parent)  
    return parent[node]

def connect_nodes(node1, node2, parent):
    root1 = get_root(node1, parent)
    root2 = get_root(node2, parent)
    if root1 != root2:
        if root1 < root2:
            parent[root2] = root1
        else:
            parent[root1] = root2

test_cases = int(input())

for _ in range(test_cases):
    num_nodes = int(input())
    parent = list(range(num_nodes))  
    circles = [list(map(int, input().split())) for _ in range(num_nodes)]  

    for i in range(num_nodes):
        x1, y1, r1 = circles[i]
        for j in range(i + 1, num_nodes):
            x2, y2, r2 = circles[j]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance <= r1 + r2:  
                connect_nodes(i, j, parent)

    groups = set(get_root(node, parent) for node in range(num_nodes))
    print(len(groups))
