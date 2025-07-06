import sys
a,b = map(int,sys.stdin.readline().strip().split())
cnt = 0
money = []
for i in range(a):
  money.append(int(sys.stdin.readline().strip()))

while b!=0:
  for i in range(a-1,-1,-1):
    while b-money[i]>=0:
      cnt+=1
      b-=money[i]
  break
print(cnt)
