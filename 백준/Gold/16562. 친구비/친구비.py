import sys
input = sys.stdin.readline

# 입력 처리
n, m, k = map(int, input().split())  
costs = [0] + list(map(int, input().split())) 

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) 
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

for i in range(1, n + 1):
    find(i)

min_cost = [float('inf')] * (n + 1)
for i in range(1, n + 1):
    root = find(i)
    min_cost[root] = min(min_cost[root], costs[i])

total_cost = sum(cost for cost in min_cost if cost != float('inf'))

if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")
