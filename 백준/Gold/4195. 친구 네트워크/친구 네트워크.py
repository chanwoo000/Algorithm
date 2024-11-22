import sys
input = sys.stdin.readline

def union(a,b):
    a, b = find(a), find(b)
    if a == b:
        return network[a]
    parents[b] = a
    network[a] += network[b]
    return network[a]

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

for _ in range(int(input())):
    parents, network = dict(), dict()
    for i in range(int(input())):
        a,b = input().split()
        if a not in parents.keys():
            parents[a], network[a] = a, 1
        if b not in parents.keys():
            parents[b], network[b] = b, 1
        print(union(a,b))