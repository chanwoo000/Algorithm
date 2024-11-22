import sys
from collections import deque

def BFS(target): 
    queue=deque()
    queue.append(target)
    while(queue):
        k=queue.pop()
        visited.add(k)
        for kk in people[k]:
            if kk not in visited:
                queue.append(kk)

N,M=map(int,sys.stdin.readline().split())
num_know,*known_people=map(int,sys.stdin.readline().split())
party_people=[]
visited=set()
people=[[] for _ in range(N+1)] 
for _ in range(M):
    num_party_people,*temp_party_people=map(int,sys.stdin.readline().split())
    for i in temp_party_people: 
        for j in temp_party_people:
            if i!=j:
                people[i].append(j)
    party_people.append(set(temp_party_people))


for know in known_people:
    if know not in visited:
        BFS(know)

cnt=0
for party in party_people:
    if not party.issubset(visited): 
        cnt+=1 

print(cnt)