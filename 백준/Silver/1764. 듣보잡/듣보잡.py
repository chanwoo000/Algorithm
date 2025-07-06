import sys
a,b = map(int,sys.stdin.readline().split())
look = set()
listen = []
ll = []
for i in range(a):
  look.add(sys.stdin.readline().strip())

for i in range(b):
  listen.append(sys.stdin.readline().strip())

for i in range(b):
  if listen[i] in look:
    ll.append(listen[i])

ll.sort()
print(len(ll))
for i in ll:
  print(i)

