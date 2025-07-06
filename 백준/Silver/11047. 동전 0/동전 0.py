import sys
a,b = map(int,sys.stdin.readline().strip().split())
cnt = 0
money = []
for i in range(a):
  money.append(int(sys.stdin.readline().strip()))

for i in range(a-1,-1,-1):
  if b-money[i] >= 0:
    cnt += b//money[i]
    b %= money[i]
print(cnt)
