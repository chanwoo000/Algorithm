import sys
a,b = map(int,sys.stdin.readline().split())
c = {}
for i in range(a):
  site,password = sys.stdin.readline().split()
  c[site] = password

for i in range(b):
  url = sys.stdin.readline().strip()
  print(c[url])
