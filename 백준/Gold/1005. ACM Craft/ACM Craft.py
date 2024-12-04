from collections import deque
import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    construction_time = list(map(int, input().split()))
    total_time = [0] * (n+1)
    adj_list = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    
    for _ in range(k):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        in_degree[b] += 1
    
    queue = deque()
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            total_time[i] = construction_time[i-1]
    
    while queue:
        current = queue.popleft()
        
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            total_time[neighbor] = max(total_time[neighbor], total_time[current] + construction_time[neighbor-1])
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    target = int(input())
    print(total_time[target])

t = int(input())

for _ in range(t):
    solve()
