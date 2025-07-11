import sys
a,b = map(int,sys.stdin.readline().strip().split())
N = list(map(int,sys.stdin.readline().strip().split()))
dp = [0] * (a+1)
for i in range(1,a+1):
  dp[i] = dp[i-1] + N[i-1]

for z in range(b):
  i,j = map(int,sys.stdin.readline().strip().split())
  print(dp[j] - dp[i-1])
