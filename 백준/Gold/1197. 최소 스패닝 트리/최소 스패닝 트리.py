import sys
sys.setrecursionlimit(10**6)

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])  # 경로 압축
    return parent[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if root1 > root2:
            parent[root1] = root2
        else:
            parent[root2] = root1

# 입력 처리
num_vertices, num_edges = map(int, input().split())
parent = list(range(num_vertices + 1))  # 부모 배열 초기화
edges = []

# 간선 정보 입력
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    edges.append((weight, u, v))  # 간선 정보를 (비용, 노드1, 노드2) 형태로 저장

# 간선 비용 기준으로 정렬
edges.sort()

# 최소 스패닝 트리 계산
total_cost = 0
for cost, u, v in edges:
    if find(u) != find(v):  # 사이클이 발생하지 않는 경우만 간선 선택
        union(u, v)
        total_cost += cost

# 결과 출력
print(total_cost)
