import sys
import heapq

input = sys.stdin.readline

# 위상 정렬을 위한 함수
def topological_sort(n, changes, initial_rank):
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    # 초기에 주어진 순위를 기반으로 간선 추가
    for i in range(n):
        for j in range(i + 1, n):
            adj[initial_rank[i]].append(initial_rank[j])
            in_degree[initial_rank[j]] += 1
    
    # 변경된 순위를 반영
    for a, b in changes:
        if b in adj[a]:
            adj[a].remove(b)
            in_degree[b] -= 1
            adj[b].append(a)
            in_degree[a] += 1
        else:
            adj[b].remove(a)
            in_degree[a] -= 1
            adj[a].append(b)
            in_degree[b] += 1
    
    # 최소 힙을 이용해 위상 정렬
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)
    
    result = []
    while heap:
        current = heapq.heappop(heap)
        result.append(current)
        
        for neighbor in adj[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)
    
    # 사이클이 존재하는지 확인
    if len(result) != n:
        return "IMPOSSIBLE"
    
    return " ".join(map(str, result))

# 입력 처리
t = int(input())  # 테스트 케이스 수
for _ in range(t):
    n = int(input())  # 문제 수
    initial_rank = list(map(int, input().split()))  # 작년 순위
    m = int(input())  # 변경 사항 개수
    
    changes = []
    for _ in range(m):
        a, b = map(int, input().split())
        changes.append((a, b))
    
    # 위상 정렬 수행
    result = topological_sort(n, changes, initial_rank)
    print(result)
