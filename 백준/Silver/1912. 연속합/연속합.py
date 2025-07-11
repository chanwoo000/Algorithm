import sys
n = int(sys.stdin.readline())
num = [0] * n
dp = [0] * n

num = (list(map(int,sys.stdin.readline().strip().split())))

dp[0]= num[0]

for i in range(1,n):
  dp[i] = max(dp[i-1]+num[i],num[i])

print(max(dp))
