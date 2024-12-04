import sys
input = sys.stdin.readline

INFINITY = 1e9  # 무한대 값
n, m = map(int, input().split())  # 노드 수 n, 간선 수 m

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
dist = [INFINITY] * (n + 1)
dist[1] = 0  # 시작 노드의 거리는 0

# 간선 정보 입력 받기
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가는 간선, 비용 w

# 벨만포드 알고리즘
for i in range(n):  # 최대 n-1번 반복
    for u in range(1, n + 1):  # 모든 노드에 대해
        if dist[u] == INFINITY:  # 만약 현재 노드까지 도달할 수 없다면, 넘어간다
            continue
        for v, weight in graph[u]:  # u에서 갈 수 있는 모든 노드 v를 탐색
            if dist[u] + weight < dist[v]:  # 더 저렴한 경로가 있으면 갱신
                dist[v] = dist[u] + weight
                if i == n - 1:  # n-1번째 반복에서 여전히 갱신이 되면 음수 사이클 존재
                    print(-1)
                    sys.exit()

# 결과 출력
for i in range(2, n + 1):  # 1번 노드는 시작 노드이므로 제외
    if dist[i] == INFINITY:  # 도달할 수 없는 노드는 -1 출력
        print(-1)
    else:
        print(dist[i])
