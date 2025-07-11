n = int(input())
dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for i in range(5,101):
  dp[i] = dp[i-5] + dp[i-1]

for i in range(n):
  a = int(input())
  print(dp[a-1])

