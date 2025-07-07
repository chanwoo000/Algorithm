import sys
n = int(sys.stdin.readline())
atm = list(map(int,sys.stdin.readline().strip().split()))
atm.sort()
cnt = 0
for i in range(n):
  cnt+=atm[i]*(n-i)
print(cnt)
