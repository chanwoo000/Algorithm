import sys
input = sys.stdin.readline


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
data =[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'Y' and i != j:
            data[i].append(j)
            for k in range(len(graph[j])):
                if graph[j][k] == 'Y' and i != k:
                    data[i].append(k)
data_flag = data
for i in range(len(data)):
    data[i] = list(set(data[i]))
Max = 0
for i in data:
    if len(i)>Max:
        Max = len(i)
print(Max)